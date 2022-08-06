ARG USERNAME=shubham

# Where to store the built application in the runtime image.
ARG IMAGE_WS_DIR=/home/$USERNAME/void-slam-toolbox

# ROS Distribution (ex: melodic, foxy, etc.)
ARG ROS_DISTRO=galactic

FROM ros:$ROS_DISTRO-ros-base


# USE BASH
SHELL ["/bin/bash", "-c"]

# RUN LINE BELOW TO REMOVE debconf ERRORS (MUST RUN BEFORE ANY apt-get CALLS)
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends apt-utils 


# slam_toolbox

WORKDIR /home/$USERNAME/void-slam-toolbox/src
RUN git clone -b $ROS_DISTRO https://github.com/SteveMacenski/slam_toolbox.git

WORKDIR /home/$USERNAME/void-slam-toolbox
RUN source /opt/ros/$ROS_DISTRO/setup.bash \
    && rosdep update \
    && rosdep install -y -r --from-paths src --ignore-src --rosdistro=$ROS_DISTRO -y 


RUN source /opt/ros/$ROS_DISTRO/setup.bash \
    && colcon build  --cmake-args=-DCMAKE_BUILD_TYPE=Release \
    && colcon test
