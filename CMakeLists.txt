cmake_minimum_required(VERSION 3.10)  #require a minimum level of CMAKE

project(TEST LANGUAGES CXX VERSION 0.1)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_CXX_FLAGS "-Wall -pthread ") 

file("test.cpp")

find_package(OpenCV REQUIRED) 

include_directories(../include /usr/local/include) 
include_directories(${OpenCV_INCLUDE_DIRS}) 

#target_link_libraries(test.cpp ${OPENCV_LIBS})

set(EXECUTABLE_OUTPUT_PATH make_directory/bin) 

add_executable(${PROJECT_NAME} ${SOURCES})  
