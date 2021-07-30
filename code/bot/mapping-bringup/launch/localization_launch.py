from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
          parameters=[
            '/home/jacob/beer-bot/code/bot/mapping-bringup/config/slam_localization_config.yaml'
          ],
          package='slam_toolbox',
          executable='localization_slam_toolbox_node',
          name='slam_toolbox',
          output='screen'
        )
    ])