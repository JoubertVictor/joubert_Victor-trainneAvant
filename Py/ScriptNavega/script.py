#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, SetMode, CommandTOL
import time

# Variaveis que guardam o estado e a posicao atual do drone
estado_atual = State()
posicao_atual = PoseStamped()

# Callback para o estado do drone
def estado_callback(state):
    global estado_atual
    estado_atual = state
   
# Callback para a posicao do drone 
def posicao_callback(posicao):
    global posicao_atual
    posicao_atual = posicao
    
# Funcao para armar
def armar_drone():
    rospy.wait_for_service('/edrn/mavros/cmd/arming')
    try:
        armar = rospy.ServiceProxy('/edrn/mavros/cmd/arming', CommandBool)
        armar(True)
        rospy.loginfo("Drone armado")
    except rospy.ServiceException as e:
        print("Falha ao armar: %s"%e)
        return False
    
# Funcao para Setar o modo do drono
def setar_modo(modo):
    rospy.wait_for_service('/edrn/mavros/set_mode')
    try:
        setar_modo = rospy.ServiceProxy('/edrn/mavros/set_mode', SetMode)
        setar_modo(0, modo)
        rospy.loginfo("Modo setado para %s"%modo)
    except rospy.ServiceException as e:
        print("Falha ao setar: %s"%e)
        return False

# Funcao para decolar
def decolar(altura):
    rospy.wait_for_service('/edrn/mavros/cmd/takeoff')
    try:
        decolar = rospy.ServiceProxy('/edrn/mavros/cmd/takeoff', CommandTOL)
        decolar(0, 0, posicao_atual.pose.position.latitude, posicao_atual.pose.position.longitude, posicao_atual.pose.position.altitude)
        rospy.loginfo("Decolando")
    except rospy.ServiceException as e:
        print("Falha ao decolar: %s"%e)
        return False
    
# Funcao para pousar
def pousar():
    rospy.wait_for_service('/edrn/mavros/cmd/land')
    try:
        pousar = rospy.ServiceProxy('/edrn/mavros/cmd/land', CommandTOL)
        pousar(0, 0, posicao_atual.pose.position.latitude, posicao_atual.pose.position.longitude, 0)
        rospy.loginfo("Pousando")
    except rospy.ServiceException as e:
        print("Falha ao pousar: %s"%e)
        return False
    
def navegar(x, y, z):
    waypoint = PoseStamped()
    waypoint.header.frame_id = "map"
    waypoint.header.stamp = rospy.Time.now()
    waypoint.pose.position.x = x
    waypoint.pose.position.y = y
    waypoint.pose.position.z = z
    waypoint_pub.publish(waypoint)
    rospy.loginfo("Waypoint enviado: (%f, %f, %f)" % (x, y, z))
    
# Funcao para varrer a arena
def varrer_arena(waypoints):
    rospy.loginfo("Iniciando varredura da arena")
    for i, wp in enumerate(waypoints):
        rospy.loginfo("Viajando para o waypoint de arena %d: %s", i+1, str(wp))
        navegar(wp[0], wp[1], wp[2])
        rospy.sleep(10)  # Aguarda o drone chegar ao waypoint
    rospy.loginfo("Varredura da arena completa")
    
# Funcao principal
def main():
    rospy.init_node('missao_drone', anonymous=True)
    
    # Subscribers
    rospy.Subscriber('/edrn/mavros/state', State, estado_callback)
    rospy.Subscriber('/edrn/mavros/local_position/pose', PoseStamped, posicao_callback)
    
    # Publishers
    global waypoint_pub
    waypoint_pub = rospy.Publisher('/edrn/mavros/setpoint_position/local', PoseStamped, queue_size=20)
    
    # Aguardar conexão com o FCU
    while not rospy.is_shutdown() and not estado_atual.connected:
        rospy.loginfo("Aguardando conexão com FCU...")
        rospy.sleep(1)
    
    rospy.loginfo("Conectado ao FCU!")
    
    # Configuração inicial
    setar_modo("GUIDED")
    rospy.sleep(2)
    
    armar_drone()
    rospy.sleep(2)
    
    decolar(5)
    rospy.sleep(10)  # Aguarda a decolagem
    
    ### INÍCIO DA VARREDURA DA ARENA ###
    arena_waypoints = [
        (0, 0, 5),
        (0, 10, 5),
        (10, 10, 5),
        (10, 0, 5),
        (0, 0, 5)  # Retorno ao ponto de decolagem
    ]
    
    varrer_arena(arena_waypoints)
    
    ### FIM DA VARREDURA DA ARENA ###
    
    # Navegar para as bases de pouso
    bases = [(0, 5.5, 2), (12, 0, 1)]
    
    for i, base in enumerate(bases):
        rospy.loginfo("Indo para a base %d: %s", i+1, str(base))
        
        navegar(base[0], base[1], base[2])
        rospy.sleep(15)  # Aguarda o drone chegar ao waypoint
        
        pousar()
        rospy.sleep(5)  # Aguarda o pouso completo
        
        if i < len(bases) - 1:  # Se não for a última base
            setar_modo("GUIDED")
            rospy.sleep(2)
            armar_drone()
            rospy.sleep(2)
            decolar(5)
            rospy.sleep(10)
    
    # Retornar à base de decolagem
    rospy.loginfo("Retornando à base inicial")
    setar_modo("GUIDED")
    rospy.sleep(2)
    armar_drone()
    rospy.sleep(2)
    decolar(5)
    rospy.sleep(10)
    
    navegar(0, 0, 5)
    rospy.sleep(15)
    pousar()
    
    rospy.loginfo("Missão concluída!")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
