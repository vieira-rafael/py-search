from distutils.core import setupfrom catkin_pkg.python_setup import generate_distutils_setup
setup(**generate_distutils_setup( packages=['robot_upstart'], package_dir={'': 'src'}))