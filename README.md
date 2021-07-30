# beer-bot
This repository will store all of the Code, CAD, BoM, and instructions for building the DIY Beer Delivery Robot

Add these to bash RC
`source /home/jacob/beer-bot/code/bot/create_ws/install/setup.bash`
`source /home/jacob/beer-bot/code/bot/controller_ws/install/setup.bash`

Save pose graph
`ros2 service call /slam_toolbox/serialize_map slam_toolbox/SerializePoseGraph "filename: pozeywozey"`
Load pose graph
`ros2 service call /slam_toolbox/deserialize_map slam_toolbox/DeserializePoseGraph {"filename: pozeywozey, match_type: 1"}`