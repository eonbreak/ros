import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
import redis
from datetime import datetime

class Subscriber(Node):

    def __init__(self):
        super().__init__('iot_to_redis')
        self.subscription = self.create_subscription(
            Float32,
            'iot_datax',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.redis_conn = redis.Redis(host='2.12.100.145', port=6379, db=0)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%f"' % msg.data)
        self.redis_conn.publish('iot-channel', f'msg: {msg.data}')

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = Subscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()