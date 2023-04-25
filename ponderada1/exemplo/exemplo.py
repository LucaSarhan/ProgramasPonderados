#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.twist_msg_ = Twist()

    def move_turtle2(self):
        self.twist_msg_.linear.x = 0.0
        self.twist_msg_.angular.z = 2.0
        self.publisher_.publish(self.twist_msg_)

    def move_turtle3(self):
        self.twist_msg_.linear.x = 2.0
        self.twist_msg_.angular.z = 0.0
        self.publisher_.publish(self.twist_msg_)

def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    for i in range(200):
        turtle_controller.create_timer(0.1, turtle_controller.move_turtle3)
        turtle_controller.create_timer(0.1, turtle_controller.move_turtle2)
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
