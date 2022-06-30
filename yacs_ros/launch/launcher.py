from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    logger = LaunchConfiguration("logger")
    return LaunchDescription([
        DeclareLaunchArgument(
            "logger",
            default_value=["info"], #debug
      ),
        Node(
            package='yacs_ros',
            executable='iot_publisher',
            name='iot_publisher',
            output='log',
            arguments=['--ros-args', '--log-level', logger]
        )
    ])
