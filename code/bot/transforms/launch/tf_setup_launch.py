from launch import LaunchDescription
from launch_ros.actions import Node
## Somewhere higher-up...


#### tf2 static transforms
def generate_launch_description():
    return LaunchDescription([
        Node(
            name='tf2_ros_fp_laser',
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['-0.09', '0', '0.229', '3.1419926535', '0.0', '0.0', 'base_link', 'laser'],   
        )
    ])
