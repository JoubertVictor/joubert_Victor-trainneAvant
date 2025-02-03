#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move():
    # Inicia um nó e declara o publisher da velocidade
    rospy.init_node('turtlesim_straight_line', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    		
    # Recebe os valores de velocidade e posição
    print("Vamos mover seu robô!")
    speed = int(input("Escolha a velocidade: "))
    distance = int(input("Escolha a distância: "))
    isForward = input("Mover em direção positiva? (Responder com S ou N) ")

    if(isForward == "S" or isForward == "s"):
        isForward = True
    elif(isForward == "N" or isForward == "n"):
        isForward = False
    else:
        print("Resposta inválida!")

    # Verifica se o movimento é positivo ou negativo
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    # Para definir o movimento somente na direção x
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        # Verificando o tempo atual 
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        # Publica a velocidade enquanto a distância não é alcançada
        while(current_distance < distance):

            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()

            current_distance = speed * (t1 - t0)

        # Força o robô a parar quando atinge o ponto desejado
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        # Testando a função
        move()
    except rospy.ROSInterruptException: pass