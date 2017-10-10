cmake_minimum_required(VERSION 2.8.3)
project(mv_base_v01)
find_package(catkin 
		REQUIRED 
		COMPONENTS 
		genmsg 
		roscpp 
		std_msgs )
find_package(OpenCV REQUIRED)
catkin_package()
include_directories(${catkin_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS})
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(listen_cmd src/listen_cmd.cpp)
target_link_libraries(listen_cmd ${catkin_LIBRARIES})  
add_dependencies(listen_cmd beginner_tutorials_generate_messages_cpp)  	  

add_executable(stepDis src/stepDis.cpp)  
target_link_libraries(stepDis ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})  
add_dependencies(stepDis beginner_tutorials_generate_messages_cpp)
