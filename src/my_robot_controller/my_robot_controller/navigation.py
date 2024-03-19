#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from sensor_msgs.msg import LaserScan
from turtlesim.msg import Pose
import tf_transformations
import time


class TurtleNavigationNode(Node):

    def __init__(self):
        super().__init__("navigation")
        self.get_logger().info("our navigation is started")

        self.initial_pose_publisher = self.create_publisher(
            PoseWithCovarianceStamped, "/initialpose", 10)
        
        self.goal_pose_publisher = self.create_publisher(
            PoseStamped, "/goal_pose", 10)
        
        self.odom_listener = self.create_subscription(
            Odometry, "/odom", self.odom_callback, 10)
        
        ############# [Initial Location] #####################
        initial_pose = PoseWithCovarianceStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.pose.pose.position.x = 0.0
        initial_pose.pose.pose.position.y = 0.0
        
        qq = tf_transformations.quaternion_from_euler(0,0,0)#
        initial_pose.pose.pose.orientation.x = qq[0]
        initial_pose.pose.pose.orientation.y = qq[1]
        initial_pose.pose.pose.orientation.z = qq[2]
        initial_pose.pose.pose.orientation.w = qq[3]
        self.initial_pose_publisher.publish(initial_pose)
        #################################
        #time.sleep(1)
        ############### [Destination] ##################
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 3.5
        goal.pose.position.y = 0.0
        qq = tf_transformations.quaternion_from_euler(0,0,1.57)

        goal.pose.orientation.x = qq[0]
        goal.pose.orientation.x = qq[1]
        goal.pose.orientation.x = qq[2]
        goal.pose.orientation.x = qq[3]
        self.goal_pose_publisher.publish(goal)


    def odom_callback(self, msg: Odometry):
        pass
       
    

def main(args=None):
    rclpy.init(args=args)
    node = TurtleNavigationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__': 
    main()