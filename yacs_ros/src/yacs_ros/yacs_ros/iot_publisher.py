import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from json import load
from datetime import datetime

class Publisher(Node):

    def __init__(self):
        super().__init__('iot_publisher')
        self.publisher_ = self.create_publisher(Float32, 'iot_datax', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.data = load(
            open('/home/ubuntu/Desktop/yacs-ros/src/yacs_ros/yacs_ros/data.json'))

    def timer_callback(self):
        msg = Float32()
        msg.data = float(self.i)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%f"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Publisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
