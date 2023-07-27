##############################################################################
# Project
##############################################################################

cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project(maliput_cc_examples LANGUAGES C CXX VERSION 3.0.0)

##############################################################################
# Find 3rd Party Packages
##############################################################################

find_package(ament_cmake REQUIRED)
find_package(gflags REQUIRED)
find_package(maliput REQUIRED)
find_package(maliput_malidrive REQUIRED)
# find_package(maliput_py REQUIRED)
find_package(yaml-cpp REQUIRED)

# phase these out
find_package(maliput_multilane REQUIRED)
find_package(maliput_dragway REQUIRED)
find_package(maliput_osm REQUIRED)
find_package(maliput_sparse REQUIRED)

##############################################################################
# Project Configuration
##############################################################################

message(STATUS "\n\n========= Project Configuration ========\n")

set(BUILD_SHARED_LIBS true)

set (CMAKE_CXX_STANDARD 17)
set (CMAKE_CXX_STANDARD_REQUIRED ON)
set (CMAKE_CXX_EXTENSIONS OFF)

##############################################################################
# Sources
##############################################################################

add_subdirectory(src)

##############################################################################
# Export
##############################################################################

ament_export_dependencies(ament_cmake)
ament_package()