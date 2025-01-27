#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
import math

rospy.init_node('Turtle_poligono')
cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rospy.wait_for_service('/turtle1/teleport_absolute')
teleport = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)

#função que desenha os poligonos com lado <100
#max_lados = 2, pois é onde nao ocorre erro no desenho
def desenhando_poligono(lados, max_lados = 2.0):

    #Verificação de que se pode ser desenhado o poligono
    if lados < 3:
        rospy.logerr("Número de lados deve ser pelo menos 3.")
        return

    #Gambiarra pra calcular o tamnho dos lados, de acordo com o tanto de lados, para nao bater nas bordas da tela
    #Sendo assim lados nunca vai ser maior que 2
    lado = min(max_lados, 11.0 / lados)

    # Reseta a tartaruga para o meio exato da tela
    teleport(5.5, 5.5, 0)
    
    #calcula o tamnho do angulo extero, imortante para desenhar os poligonos
    angulo_exter = 360 / lados

    #taxa de publicação de movimento
    rate = rospy.Rate(1)

    #Nesse loop esta todos os movimentos, andar reto e rotacionar, repete de acordo com o numero de lados desejado
    for _ in range(lados):
        #linhas retas
        move_cmd = Twist()
        move_cmd.linear.x = lado
        cmd_vel_pub.publish(move_cmd)
        rate.sleep()

        #Rotaçao
        turn_cmd = Twist()
        turn_cmd.angular.z = -math.radians(angulo_exter) #o - faz girar no angulo externo
        cmd_vel_pub.publish(turn_cmd)
        rate.sleep()

#Função para desenhar o circulo caso lados>100
def desenhando_circulo():

    #define o moveimentoda tartaruga e o raio do circulo
    circle_cmd = Twist()
    circle_cmd.linear.x = 2.0
    circle_cmd.angular.z = 1.0

    t0 = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - t0 < 7.0:
        #o circulo é feito no tempo de 7 sec
        cmd_vel_pub.publish(circle_cmd)

    # Para o movimento
    circle_cmd.linear.x = 0
    circle_cmd.angular.z = 0
    cmd_vel_pub.publish(circle_cmd)

def main():
    #Tratamento pra saber se o numero é valido
    try:
        lados = int(input("Digite o número de lados do polígono: "))
        
        if lados > 100:
            #chama a funçao de desenhar circulo
            desenhando_circulo()
        else:
            #chama a função de desenhar o poligono
            desenhando_poligono(lados)
        
        rospy.spin()
    except ValueError:
        rospy.logerr("Por favor, digite um número inteiro válido.")
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()