#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, SetMode, CommandTOL
import time

# Variáveis globais
current_state = State()
current_pose = PoseStamped()

# Callbacks para os tópicos
def state_cb(state):
    global current_state
    current_state = state

def pose_cb(pose):
    global current_pose
    current_pose = pose

# Função para armar o drone
def arm_drone():
    rospy.wait_for_service('/edrn/mavros/cmd/arming')
    try:
        arm_service = rospy.ServiceProxy('/edrn/mavros/cmd/arming', CommandBool)
        result = arm_service(True)
        rospy.loginfo("Resultado do arming: %s", result)
        return result.success
    except rospy.ServiceException as e:
        rospy.logerr("Falha ao armar o drone: %s" % e)
        return False

# Função para mudar o modo do drone
def set_mode(mode):
    rospy.wait_for_service('/edrn/mavros/set_mode')
    try:
        mode_service = rospy.ServiceProxy('/edrn/mavros/set_mode', SetMode)
        result = mode_service(custom_mode=mode)
        rospy.loginfo("Resultado da mudança de modo para %s: %s", mode, result)
        return result.mode_sent
    except rospy.ServiceException as e:
        rospy.logerr("Falha ao mudar o modo do drone: %s" % e)
        return False

# Função para decolar
def takeoff(altitude):
    rospy.wait_for_service('/edrn/mavros/cmd/takeoff')
    try:
        takeoff_service = rospy.ServiceProxy('/edrn/mavros/cmd/takeoff', CommandTOL)
        result = takeoff_service(altitude=altitude)
        rospy.loginfo("Resultado do takeoff: %s", result)
        return result.success
    except rospy.ServiceException as e:
        rospy.logerr("Falha ao decolar o drone: %s" % e)
        return False

# Função para pousar
def land():
    rospy.wait_for_service('/edrn/mavros/cmd/land')
    try:
        land_service = rospy.ServiceProxy('/edrn/mavros/cmd/land', CommandTOL)
        result = land_service()
        rospy.loginfo("Resultado do land: %s", result)
        return result.success
    except rospy.ServiceException as e:
        rospy.logerr("Falha ao pousar o drone: %s" % e)
        return False

# Função para enviar waypoints
def send_waypoint(x, y, z):
    waypoint = PoseStamped()
    waypoint.header.frame_id = "map"
    waypoint.header.stamp = rospy.Time.now()
    waypoint.pose.position.x = x
    waypoint.pose.position.y = y
    waypoint.pose.position.z = z
    waypoint_pub.publish(waypoint)
    rospy.loginfo("Waypoint enviado: (%f, %f, %f)" % (x, y, z))

# Função para reiniciar o voo
def restart_flight():
    rospy.loginfo("Reiniciando o voo...")
    
    # Desativar o modo de voo atual
    set_mode("STABILIZE")
    rospy.sleep(2)
    
    # Mudar para GUIDED e rearmar
    if set_mode("GUIDED"):
        rospy.sleep(2)
        if arm_drone():
            rospy.sleep(2)
            return True
    return False

# Função principal
def main():
    rospy.init_node('drone_mission', anonymous=True)
    
    # Subscribers
    rospy.Subscriber('/edrn/mavros/state', State, state_cb)
    rospy.Subscriber('/edrn/mavros/local_position/pose', PoseStamped, pose_cb)
    
    # Publishers
    global waypoint_pub
    waypoint_pub = rospy.Publisher('/edrn/mavros/setpoint_position/local', PoseStamped, queue_size=20)
    
    # Taxa de publicação
    rate = rospy.Rate(20)
    
    # Aguardar a conexão com o FCU
    while not rospy.is_shutdown() and not current_state.connected:
        rospy.loginfo("Aguardando conexão com FCU...")
        rospy.sleep(1)
    
    rospy.loginfo("Conectado ao FCU!")
    
    # Configuração inicial
    if not set_mode("GUIDED"):
        rospy.logerr("Falha ao configurar modo GUIDED inicial")
        return
    
    if not arm_drone():
        rospy.logerr("Falha ao armar o drone inicialmente")
        return
    
    # Decolar para 5 metros
    if not takeoff(5):
        rospy.logerr("Falha na decolagem inicial")
        return
    
    rospy.sleep(10)  # Aguardar a decolagem

    ### INÍCIO DA VARREDURA DA ARENA ###
    rospy.loginfo("Iniciando varredura da arena")
    # Definindo uma sequência de waypoints que cobrem a arena.
    # Ajuste as coordenadas conforme as dimensões reais da arena.
    arena_waypoints = [
        (0, 0, 5),
        (0, 10, 5),
        (10, 10, 5),
        (10, 0, 5),
        (0, 0, 5)  # Retorno ao ponto de decolagem
    ]
    
    for i, wp in enumerate(arena_waypoints):
        rospy.loginfo("Viajando para o waypoint de arena %d: %s", i+1, str(wp))
        send_waypoint(wp[0], wp[1], wp[2])
        rospy.sleep(10)  # Aguarda o drone chegar ao waypoint (ajuste o tempo conforme necessário)
    ### FIM DA VARREDURA DA ARENA ###
    
    # Navegar para as bases de pouso
    bases = [(0, 5.5, 2), (12, 0, 1)]
    
    for i, base in enumerate(bases):
        rospy.loginfo("Indo para a base %d: %s", i+1, str(base))
        
        send_waypoint(base[0], base[1], base[2])
        rospy.sleep(15)  # Aguarda o drone chegar ao waypoint
        
        if land():
            rospy.loginfo("Pouso realizado com sucesso na base %d", i+1)
            rospy.sleep(5)  # Aguarda o pouso completo
            
            if i < len(bases) - 1:  # Se não for a última base
                if not restart_flight():
                    rospy.logerr("Falha ao reiniciar o voo após o pouso na base %d", i+1)
                    return
                rospy.sleep(5)  # Aguarda a estabilização
    
    # Retornar à base de decolagem
    rospy.loginfo("Retornando à base inicial")
    if restart_flight():
        send_waypoint(0, 0, 5)
        rospy.sleep(15)
        land()
    
    rospy.loginfo("Missão concluída!")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
