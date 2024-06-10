#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class MyNode(Node):
    def __init__ (self):
        super().__init__("Tu_puedes")
        self.get_logger().info("Hola mi amigo ROS2")
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) #El nodo va a correr infinitamente todo los callbacks van a retonar a èl
    rclpy.shutdown()
if __name__ == "__main__":
    main()