from typing import final
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

from robot_navigator import BasicNavigator, NavigationResult

# Msgs
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist
# Services
from slam_toolbox.srv import DeserializePoseGraph
#`ros2 service call /slam_toolbox/deserialize_map slam_toolbox/DeserializePoseGraph {"filename: pozeywozey, match_type: 1"}`

# Target Point: 4.0 1.0
# Resting point 1.0 0

# ros2 topic pub /goal_pose geometry_msgs/PoseStamped "{header: {stamp: {sec: 0}, frame_id: 'map'}, pose: {position: {x: 0.0, y: 0.0, z: 0.0}, orientation: {w: 1.0}}}"

class ControllerNode(Node):

    ###
    # Makes robot go to specified [x,y] location in coords
    # Creates msg & publishes it to waypoint_publisher
    ###
    def goto(self, coords):
        goal = PoseStamped()
        goal.header.seq = 1
        goal.header.stamp.sec = 0
        goal.header.frame_id = "map"

        goal.pose.position.x = coords[0]
        goal.pose.position.y = coords[1]
        goal.pose.position.z = 0.0

        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0

        self.navigator.goToPose(goal)
        

    def dock(self):
        coords = [1.0, 0]
        # Go to coords
        self.goto(coords)
        # publish to dock
    
    def deliver_to(self):        
        # Get coordinate (should be passed in function)
        coords = [4.0, 1.0]



    def __init__(self):
        super().__init__('controller_node')

        # Setup Pub/Subs/Clients for misc actions
        self.waypoint_publisher = self.create_publisher(PoseStamped, 'goal_pose', 2)
        self.undock_publisher = self.create_publisher(Empty, 'undock', 2)
        self.dock_publisher = self.create_publisher(Empty, 'dock', 2)
        self.drive_publisher = self.create_publisher(Twist, "cmd_vel", 10)
        self.waypoint_subscriber = self.create_subscription()
    
        self.map_loader_client = self.create_client(DeserializePoseGraph, 'slam_toolbox/deserialize_map')

        # Load the map with current location being the dock location
        map_loader_data = DeserializePoseGraph()
        map_loader_data.Request.filename = 'pozeywozey'
        map_loader_data.Request.match_type = map_loader_data.Request.START_AT_FIRST_NODE
        
        self.map_loader_client.call(map_loader_data)

        # Setup Nav2 Library
        self.navigator = BasicNavigator()
        initial_pose = PoseStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        initial_pose.pose.position.x = 0.0
        initial_pose.pose.position.y = 0.0
        initial_pose.pose.orientation.z = 0.0
        initial_pose.pose.orientation.w = 0.0

        # I beleive we use this because we're starting nav2 in our main launch file...
        # we shall see
        self.navigator.waitUntilNav2Active()
        # The other option would be:
        # navigator.lifecycleStartup()



def main(args=None):
    rclpy.init(args=args)

    try:
        controller_node = ControllerNode()
        rclpy.spin(controller_node)
    finally:
        controller_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
