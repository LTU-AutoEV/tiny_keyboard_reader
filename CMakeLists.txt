cmake_minimum_required(VERSION 2.8.3)
project(tiny_keyboard_reader)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  rospy
)


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES actor_obstacle
#  CATKIN_DEPENDS roscpp
#  CATKIN_DEPENDS message_runtime
#  DEPENDS system_lib
)



###########
## Build ##
###########
include_directories(
  ${catkin_INCLUDE_DIRS}
)
