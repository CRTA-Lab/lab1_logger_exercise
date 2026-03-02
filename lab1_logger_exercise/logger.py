import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import csv
import matplotlib.pyplot as plt
from tf_transformations import euler_from_quaternion

class OdomLogger(Node):
    def __init__(self):
        super().__init__('odom_logger')
        
        # Subscrib to the /odom topic

        # Flag to track the first message
        self.first_message_received = False
        self.get_logger().info("OdomLogger started. Waiting for the first /odom message (play the bag file now)...")

        # Data storage for plotting
        self.x_data = []
        self.y_data = []
        self.yaw_data = []

        # CSV Setup
        self.csv_filename = 'robot_odometry.csv'
        self.csv_file = open(self.csv_filename, mode='w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['x', 'y', 'yaw_rad'])

    def odom_callback(self, msg: Odometry):
        """
        Callback triggered for every new Odometry message.
        """
        # Visual feedback when the first message arrives
        
        #Create flag when first msg arrives

        # 1. Extract Position
        x = 0.0 #Fill
        y = 0.0 #Fill
        
        # 2. Extract Orientation as a list [x, y, z, w]
        q = 0.0 #Fill
        quaternion_list = [q.x, q.y, q.z, q.w]
        
        # 3. Convert Quaternion to Euler angles (returns roll, pitch, yaw)
        # We only need the third value (index 2) which is Yaw
        (roll, pitch, yaw) = euler_from_quaternion(quaternion_list)
        
        # 4. Store and Save data
        # Save data as lists
        
        self.csv_writer.writerow([x, y, yaw])

    def plot_data(self):
        """
        Generates plots after the node is shut down.
        """
        if not self.x_data:
            self.get_logger().warn("No data collected. It seems no /odom messages were received.")
            return

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

        # Trajectory Plot
        ax1.plot(self.x_data, self.y_data, color='teal', label='Trajectory')
        ax1.set_xlabel('X [m]')
        ax1.set_ylabel('Y [m]')
        ax1.set_title('Robot Path (Odometry)')
        ax1.axis('equal')
        ax1.grid(True)

        # Yaw Plot
        ax2.plot(self.yaw_data, color='orange', label='Yaw')
        ax2.set_xlabel('Sample Index')
        ax2.set_ylabel('Yaw [rad]')
        ax2.set_title('Heading (Yaw) over Samples')
        ax2.grid(True)

        plt.tight_layout()
        plt.show()

    def cleanup(self):
        """
        Close file safely.
        """
        if hasattr(self, 'csv_file'):
            self.csv_file.close()
            self.get_logger().info(f"CSV file saved to: {self.csv_filename}")

def main(args=None):
    rclpy.init(args=args)
    node = OdomLogger()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT) received.')
    finally:
        # Final sequence: Close file -> Plot -> Shutdown
        node.cleanup()
        node.plot_data()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()