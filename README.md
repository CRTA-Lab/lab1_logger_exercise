# Lab 1 – Logger Exercise

**Autonomous Systems Course · CRTA Lab, University of Zagreb**

This repository contains a template for the first laboratory exercise. The goal is to implement a ROS 2 node that subscribes to one or more topics and logs the received data to the terminal and/or a file using ROS 2 logging utilities.

---

## Prerequisites

Before you begin, make sure the following are installed on your system:

- **Ubuntu 22.04** (recommended) or a compatible Linux distribution
- **ROS 2 Humble** (or the distro specified by your instructor)
- **Python 3.10+**
- **colcon** build tool

If ROS 2 is not yet installed, follow the official guide:
https://docs.ros.org/en/humble/Installation.html

---

## Creating a ROS 2 Workspace

If you do not already have a workspace, create one with the following commands:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

Source your ROS 2 installation (add this to `~/.bashrc` to avoid repeating it):

```bash
source /opt/ros/humble/setup.bash
```

---

## Cloning the Repository

Clone the package into the `src` directory of your workspace:

```bash
cd ~/ros2_ws/src
git clone https://github.com/CRTA-Lab/lab1_logger_exercise.git
```

Your workspace structure should now look like this:

```
ros2_ws/
└── src/
    └── lab1_logger_exercise/
        ├── lab1_logger_exercise/
        ├── resource/
        ├── test/
        ├── package.xml
        ├── setup.cfg
        └── setup.py
```

---

## Installing Dependencies

From the root of your workspace, install any declared dependencies:

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```

---

## Building the Package

Build the workspace using `colcon`:

```bash
cd ~/ros2_ws
colcon build --symlink-install
```

After a successful build, source the local workspace overlay:

```bash
source install/setup.bash
```

> **Tip:** Add `source ~/ros2_ws/install/setup.bash` to your `~/.bashrc` so you don't have to source it manually every time.

---

## Running the Node

Once built, run the logger node with:

```bash
ros2 run lab1_logger_exercise <node_name>
```

Replace `<node_name>` with the entry point defined in `setup.py` (e.g. `logger_node`).

---

## Task Description

### Objective

Your task is to implement a ROS 2 node in Python that:

1. **Subscribes** to a topic (specified by your instructor, e.g. `/turtle1/pose` or a custom topic).
2. **Logs** every received message using the ROS 2 logger (`self.get_logger().info(...)`).
3. **Writes** the logged data to a `.txt` or `.csv` file on disk, with a timestamp for each entry.
4. **Handles node shutdown** gracefully (closes the file, logs a summary message).

### Steps

1. Open the template file located at `lab1_logger_exercise/lab1_logger_exercise/logger_node.py` (or the file indicated by your instructor).
2. Find all sections marked with `# TODO` and implement the missing logic.
3. Build and run the node, then verify its output by publishing messages to the subscribed topic in a separate terminal:

```bash
ros2 topic pub /your_topic std_msgs/msg/String "data: 'Hello ROS 2'"
```

4. Confirm that messages appear in the terminal log and in the output file.

### Acceptance Criteria

- The node starts without errors.
- Received messages are printed to the terminal using the ROS 2 logger at `INFO` level.
- Each message is appended to a log file with a human-readable timestamp.
- The node shuts down cleanly when interrupted with `Ctrl+C`.

### Useful ROS 2 Commands

```bash
# List all active topics
ros2 topic list

# Monitor messages on a topic
ros2 topic echo /your_topic

# Check node info
ros2 node info /logger_node
```

---

## Project Structure

| Path | Description |
|------|-------------|
| `lab1_logger_exercise/` | Main Python package containing node source files |
| `resource/` | Package resource marker (required by ament) |
| `test/` | Unit and integration tests |
| `package.xml` | Package metadata and dependencies |
| `setup.py` | Python package build configuration |
| `setup.cfg` | Entry points and install settings |

---

## License

This project is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) for details.
