# Robot interfaces
screen -S transforms -dm bash -c "ros2 launch ./transforms/launch/tf_setup_launch.py"
screen -S create -dm bash -c "source ./create_ws/install/setup.bash; ros2 launch create_bringup create_2.launch use_sim_time:=false"
screen -S rplidar -dm bash -c "source ./rplidar_ros/install/setup.bash; ros2 launch rplidar_ros rplidar.launch.py scan:=laser"

# Nav, then SLAM
screen -S nav2 -dm bash -c "ros2 launch nav2_bringup navigation_launch.py use_sim_time:=false lethal_cost_threshold:=250"
screen -S slam -dm bash -c "ros2 launch slam_toolbox online_sync_launch.py use_sim_time:=false"
#screen -S slam -dm bash -c "source ~/slam_toolbox/install/setup.bash; ros2 launch ~/slam_toolbox/launch/online_sync_launch.py use_sim_time:=false"

