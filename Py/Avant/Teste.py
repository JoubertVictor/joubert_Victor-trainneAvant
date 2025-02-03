import rospy
from geometry_msgs.msg import Twist

def pentafogo_regular():
    # Inicia um nó e declara o publisher da velocidade
    rospy.init_node('turtlesim_pentagon', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    		
    #Recebe o numero de lados
    print("Vamos desenhar um pentágono!")
    lados = int(input("Escolha o número de lados: "))
    
    if lados < 5:
        print("Número de lados inválido!")
        return
    else:
    
        velocidade = 10
        angulo = 360/lados
        distancia = 3    
        
        # Para definir o movimento somente na direção x
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0