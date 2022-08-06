# Void-Slam-Toolbox
Simplified wrapper around slam_toolbox 

`sudo docker build -t stevemacenski/slam_toolbox galactic .`

## Installation
  * Install [Ignition-Edifice](https://gazebosim.org/docs/edifice/install_ubuntu_src) or greater (Source is preffered).
  * Build ros_ign packages for galactic  from [source](https://github.com/gazebosim/ros_gz/tree/galactic) 
  * Install [Docker](https://docs.docker.com/engine/install/ubuntu/)
  
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
  
  `sudo docker build -t stevemacenski/slam_toolbox galactic .`
  

## RUN 

> Slam Toolbox inside docker container
Open another terminal
  
`sudo docker run --net=host -it stevemacenski/slam_toolbox:galactic `

Now that you in the docker container 

`source install/setup.bash`
`ros2 launch slam-toolbox online_async_launch.py`

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

### Refernces 
* https://github.com/TechnoYantra/ros2-igt
* https://github.com/SteveMacenski/slam_toolbox


