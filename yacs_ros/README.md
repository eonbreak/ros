# ROS2 Foxy installtion on Ubuntu 22.04 Focal
- https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

# Colcon installation
- https://colcon.readthedocs.io/en/released/user/installation.html

# Network Setup
- for master ros (svrn is username)
- export ROS_IP=2.12.100.13
- export ROS_HOSTNAME=svrn.local
- export ROS_MASTER_URI=http://svrn.local:11311

- for client ros, only ros ip
- export ROS_IP=2.12.100.158

# Activate ROS2 Foxy
```bash
source /opt/ros/foxy/setup.bash
```

# Create ROS2 Workspace
- DO NOT USE HYPEN IN PACKAGE NAMES (-)
- cd into src folder in root directory
- ros2 pkg create --build-type ament_python package_name --dependencies aaa bbb ccc

# Build
- cd into root folder
- check dependencies needed are already installed
- rosdep install -i --from-path src --rosdistro foxy -y
- build
- colcon build --packages-select package_name

# Run
- source setup.sh from install/package-name folder
- ros2 run package-name node-name

# Parallel Run
- seq 1 5 | parallel ros2 run yacs_ros iot_publisher

# TIPS
- ROS changes the current working directory for nodes when using rosrun and roslaunch. You cannot use relative paths. Use absolute path instead.