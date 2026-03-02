import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy
import csv
import os

# Importing the transformation library for Euler to Quaternion conversion
from tf_transformations import quaternion_from_euler

class PathPublisher(Node):
    def __init__(self):
        super().__init__('path_publisher')

        # --- QoS Profile Setup ---
        # Transient Local is crucial for visualization tools like RViz
        # so they can see the data even if they are started after the publisher.
        path_qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            depth=1
        )
        
        # Publisher for the Path message with the odom-friendly QoS
        
        # Publishing at 10Hz to keep the visualization alive and stable
        
        #Read data from .csv
        #Create empty msg Path()
        
        # Load the saved odometry data from the CSV file
        self.load_path_from_csv()

    def load_path_from_csv(self):
        """Reads CSV and converts stored x, y, yaw into a Path message."""
        if not os.path.exists(self.csv_filename):
            self.get_logger().error(f"File {self.csv_filename} not found! Run the logger first.")
            return

        # Setting the frame_id to 'odom' as requested 
        
        try:
            with open(self.csv_filename, mode='r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    # Parse .csv file and fill path msg
                    continue
                
                    
            
            self.get_logger().info(f"Successfully loaded {len(self.path_msg.poses)} points into 'odom' frame.")
            
        except Exception as e:
            self.get_logger().error(f"Error while reading CSV: {str(e)}")

    def timer_callback(self):
        """Periodically publishes the path with an updated timestamp."""
        #Fill with time and path msg data

def main(args=None):
    rclpy.init(args=args)
    node = PathPublisher()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('PathPublisher shutting down...')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()