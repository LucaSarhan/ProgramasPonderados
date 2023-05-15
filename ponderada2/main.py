# Import the necessary libraries
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion

# Class that controls the movement of the turtlebot
class TurtlebotMove(Node):
    def __init__(self):
        super().__init__('turtlebot_controller')

        # Variable that defines the directions taken by the turtlebot
        self.directions_ = [1.0, -1.0, 3.0]
        self.directions_size = len(self.directions_)
        self.directions_index_ = 0
        
        # Creates the publisher of type Twist in the topic /cmd_vel
        self.publisher_ = self.create_publisher(Twist,'/cmd_vel',10)
        # Creates the message Twist
        self.twist_ = Twist()

        # Creates the subscriber of type Odometry in the topic /odom
        self.subscription_ = self.create_subscription(Odometry,'/odom',self.call_odom,10)
        # Enables the subscriber
        self.subscription_.enabled = True 
        
        # Initializes the variables odom_ and target_ with -1000.0
        self.odom_ = -1000.0
        self.target_ = -1000.0

        # Creates a loop with a period of 0.1 seconds
        self.loop_ = self.create_timer(0.1, self.call_loop)

    # Function that receives the odometry from the turtlebot
    def call_odom(self, odom):
        self.odom_ = odom

    # Function that controls the movement of the turtlebot
    def call_loop(self):
        # If the turtlebot has received the odometry data
        if self.odom_ != -1000.0:
            x = self.odom_.pose.pose.position.x
            y = self.odom_.pose.pose.position.y
            z = self.odom_.pose.pose.position.z
            ang = self.odom_.pose.pose.orientation
            _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
            self.get_logger().info(f"x={x}, y={y}, z={z}, theta={theta}")

            # If the turtlebot has not reached the target
            if self.directions_index_ < self.directions_size:
                
                # If the turtlebot has not received the target
                if self.target_ == -1000.0: self.target_ = x + self.directions_[self.directions_index_]
                
                # If the turtlebot has not reached the target
                if abs(x - self.target_) > 0.5:
                    self.twist_.linear.x = 0.5 if self.target_ > x else -0.5
                    self.publisher_.publish(self.twist_)
                
                # If the turtlebot has reached the target
                else:
                    self.twist_.linear.x = 0.0
                    self.publisher_.publish(self.twist_)
                    self.directions_index_ += 1
                    self.target_ = -1000.0

            # If the turtlebot has reached the final target
            else: 
                self.twist_.linear.x = 0.0
                self.publisher_.publish(self.twist_)
                self.loop_.cancel()

def main(args=None):
    rclpy.init(args=args)
    turtlebot = TurtlebotMove()
    rclpy.spin(turtlebot)
    turtlebot.destroy_node()
    rclpy.shutdown()

# Run the main function
if __name__ == '__main__':
    main()
