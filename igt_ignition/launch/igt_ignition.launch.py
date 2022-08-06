import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

	pkg_ros_ign_gazebo = get_package_share_directory('ros_ign_gazebo')
	pkg_igt_ignition = get_package_share_directory('igt_ignition')
	urdf_path = pkg_igt_ignition + '/models/igt_one/igt_one.urdf'
	use_sim_time = LaunchConfiguration('use_sim_time')

	# Gazebo launch
	gazebo = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
		    os.path.join(pkg_ros_ign_gazebo, 'launch', 'ign_gazebo.launch.py'),
		),
	)

	# launch ign_bridge if with_bridge is true
	ign_bridge = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
		    os.path.join(pkg_igt_ignition, 'launch', 'ign_bridge.launch.py'),
		),
        launch_arguments={
            'use_sim_time': use_sim_time}.items(),
		condition = IfCondition(LaunchConfiguration('with_bridge'))
	)

	# spawn sdf
	spawn_sdf = Node(package='ros_ign_gazebo', executable='create',
			arguments=['-name', 'igt_one',
				'-x', '4.5',
                '-y', '0.0',
				'-z', '0.0',
				'-Y', '-1.57',
				'-file', os.path.join(pkg_igt_ignition, 'models', 'igt_one', 'model.sdf')],
			output='screen')

	# robot state publisher node
	state_publisher = Node(package='robot_state_publisher', executable='robot_state_publisher',
				output='screen',
				parameters = [
					{'ignore_timestamp': False},
                                        {'use_sim_time': use_sim_time},
					{'use_tf_static': True},
					{'robot_description': open(urdf_path).read()}],
				arguments = [urdf_path])	

	return LaunchDescription([
		DeclareLaunchArgument(
		  'ign_args', default_value=[os.path.join(pkg_igt_ignition, 'worlds', 'wall_world.sdf') +
					 ' -v 4 --gui-config ' +
					 os.path.join(pkg_igt_ignition, 'ign', 'gui.config'), ''],
		  description='Ignition Gazebo arguments'),
		DeclareLaunchArgument('with_bridge', default_value=['true'],
					description='Launch simulation with ros ign brigde'),
        DeclareLaunchArgument('use_sim_time', default_value=['true'],
                    description='Enable sim time from /clock'),
		gazebo,
		spawn_sdf,
		ign_bridge,
		state_publisher
	])






