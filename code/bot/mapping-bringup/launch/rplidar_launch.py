from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace

def generate_launch_description():
  # Arguments
  use_sim_time = DeclareLaunchArgument("use_sim_time", default_value="false")

  # Static Transforms
  transforms = IncludeLaunchDescription(
      PythonLaunchDescriptionSource('/home/jacob/beer-bot/code/bot/transforms/launch/tf_setup_launch.py')
  )

  # RPLidar
  rplidar = IncludeLaunchDescription(
      PythonLaunchDescriptionSource('/home/jacob/beer-bot/code/bot/rplidar_ros/launch/rplidar.launch.py')
  )

  
  return LaunchDescription([
    transforms,
    rplidar,
  ])