import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

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
        self.waypoint_publisher.publish(goal)

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
        self.waypoint_publisher = self.create_publisher(String, 'topic', 10)
    


def main():
    rclpy.init(args=args)

    controller_node = ControllerNode()

    rclpy.spin(controller_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    controller_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
