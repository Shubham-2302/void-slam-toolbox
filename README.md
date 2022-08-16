# Void-Slam-Toolbox
Simplified wrapper around slam_toolbox. 

This repo utilises docker to create a docker image for [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox) by SteveMacenski and uses [IGT repo](https://github.com/TechnoYantra/ros2-igt) to test the networking between ROS Host and Docker container 

## Installation
  * Install [Docker](https://docs.docker.com/engine/install/ubuntu/)
  * Install [Ignition-Fortress](https://gazebosim.org/docs/fortress/install_ubuntu).
  * Build ros_ign packages for humble  from [source](https://github.com/gazebosim/ros_gz/tree/ros2) 
  
* Create a workspace

```bash
mkdir -p colcon_ws/src && cd colcon_ws/src
```

  * Clone the repo
  * Build the workspace & source the setup 

```bash
cd ../
colcon build --symlink-install
source install/setup.bash
```

  * Build the docker image

  Note: For ROS humble users slamtoolbox ros distro is set to galactic 
  
  `sudo docker build -t stevemacenski/slam_toolbox .`
  

## Testing 

> Slam Toolbox inside docker container
Open another terminal
  
`sudo docker run --net=host -it stevemacenski/slam_toolbox `

Now that you are in the docker container 

`source install/setup.bash`
`ros2 launch slam-toolbox online_async_launch.py`

In a host terminal launch `ros2 topic list` to check the slam_toolbox is running

## Launch

>Ign-Gazebo 

```bash
ros2 launch igt_ignition igt_ignition.launch.py
```

Make sure you UNPAUSE physics by clicking "play" button in bottom left corner of ignition

 
Open another terminal and run
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
## Results

![](https://github.com/void-robotics/void-slam-toolbox/blob/master/SLAM_ignition.gif)

> Note: This repo stands as a guide for any ros distribution and the associated ignition gazebo version, Refer to this [table](https://github.com/gazebosim/ros_gz/tree/ros2) for more info. After cloning the repo change the value of $ROS_DISTRO based on the ROS distribution you are using

### References 
* https://github.com/TechnoYantra/ros2-igt
* https://github.com/SteveMacenski/slam_toolbox
