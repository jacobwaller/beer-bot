some of these packages are not developed by me, but are required to be used in this way & have modifications. Specifially:
___
## create_ws/

Modified the config file as well as the driver file to change the port (I use a symlink to `/dev/ttyIRC`) & starting mode (from `create::MODE_FULL` to `create::MODE_SAFE`)

Contains:
  * [create_robot](https://github.com/AutonomyLab/create_robot) ROS2 Package for controlling the iRobot Create
  * [libcreate](https://github.com/AutonomyLab/libcreate) C++ Library to use iRobot Create

## rplidar_ros/

Modified to use 