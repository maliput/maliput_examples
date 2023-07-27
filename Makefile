################################################################################
# Shell Environment
################################################################################
SHELL:=/bin/bash
PWD:=$(shell pwd)

################################################################################
# Variables
################################################################################
# use with e.g. 'make one PACKAGE=py_trees'
PACKAGE?=maliput_examples

################################################################################
# Build Arguments
################################################################################

COLCON_ARGS=--symlink-install --event-handlers console_direct+
COLCON_QUIET_ARGS=--symlink-install --event-handlers

# OR make a single tarball or binary
# COLCON_ARGS=--merge-install --event-handlers console_direct+
# COLCON_QUIET_ARGS=--merge-install --event-handlers

CMAKE_ARGS=--cmake-args -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_VERBOSE_MAKEFILE:=ON
# CMAKE_ARGS=--cmake-args -C ${PWD}/config.cache

################################################################################
# Distro & Underlay Setup
################################################################################

UBUNTU_DISTRO=$(shell lsb_release -cs)
ifeq ($(UBUNTU_DISTRO),bionic)
  DISTRO:=dashing
else ifeq ($(UBUNTU_DISTRO),focal)
  DISTRO:=foxy
else ifeq ($(UBUNTU_DISTRO),jammy)
  DISTRO:=humble
endif
SETUP_ENV:=. /opt/ros/${DISTRO}/setup.bash

distro:
	@echo "**************************************************************************************"
	@echo "                             Distro Variables"
	@echo "**************************************************************************************"
	@echo "UBUNTU DISTRO: ${UBUNTU_DISTRO}"
	@echo "ROS DISTRO   : ${DISTRO}"

help:
	@echo ""
	@echo "Valid Targets:"
	@echo ""
	@echo "    info               : detailed information on each package"
	@echo "    list               : print the topologically ordered build list"
	@echo "    graph              : view the topologically ordered build graph with xdot"
	@echo ""
	@echo "    build_essential    : install build tools (git, colcon, ...)"
	@echo "    update_dependencies: update package dependencies with rosdep"
	@echo ""
	@echo "    all                : build and install everything"
	@echo "    quiet              : build quietly"
	@echo "    one                : build only one package, e.g. 'make one PACKAGE=ecl_time'"
	@echo ""
	@echo "    tests              : run tests with verbosity on failure"
	@echo "    clean              : clean all cmake project build and install directories"
	@echo ""

################################################################################
# Dependencies
################################################################################

SYSTEM_DEPS=build-essential curl git lsb-release wget python3-dev software-properties-common xdot
BUILD_DEPS=python3-colcon-core python3-colcon-common-extensions python3-rosdep python3-vcstool

################################################################################
# Files
################################################################################

ros_apt_source_file = /etc/apt/sources.list.d/ros2.list

################################################################################
# Targets
################################################################################

# devcontainer provisions already

$(ros_apt_source_file):
	@echo "**************************************************************************************"
	@echo "                         ROS2 Apt Repository"
	@echo "**************************************************************************************"
	curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
	sudo sh -c 'echo "deb [arch=`dpkg --print-architecture`] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2.list'
	sudo apt update
 
build_essential: $(ros_apt_source_file)
#build_essential:
	@echo "**************************************************************************************"
	@echo "                         Install Build Dependencies"
	@echo "**************************************************************************************"
	@dpkg -s ${SYSTEM_DEPS} > /dev/null || sudo apt install ${SYSTEM_DEPS}
	@dpkg -s ${BUILD_DEPS} > /dev/null || sudo apt install ${BUILD_DEPS}

update_dependencies:
	@echo "**************************************************************************************"
	@echo "                           Update ROS Dependencies"
	@echo "**************************************************************************************"
	test -f /etc/ros/rosdep/sources.list.d/20-default.list || { sudo rosdep init; rosdep update --include-eol-distros; }
	rosdep install --from-paths src --rosdistro ${DISTRO} --ignore-src -r -y --include-eol-distros

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	rm -rf build install log

all:
	@echo "**************************************************************************************"
	@echo "                                Build All";
	@echo "**************************************************************************************"
	${SETUP_ENV} && VERBOSE=1 colcon build ${COLCON_ARGS} ${CMAKE_ARGS}

build: all

quiet:
	@echo "**************************************************************************************"
	@echo "                             Build Quietly";
	@echo "**************************************************************************************"
	${SETUP_ENV} && VERBOSE=1 colcon build ${COLCON_QUIET_ARGS} ${CMAKE_ARGS}

one:
	@echo "**************************************************************************************"
	@echo "                                Build One";
	@echo "**************************************************************************************"
	${SETUP_ENV} && VERBOSE=1 colcon build ${COLCON_ARGS} ${CMAKE_ARGS} --packages-select ${PACKAGE}

testone:
	@echo "**************************************************************************************"
	@echo "                                Tests";
	@echo "**************************************************************************************"
	# for python packages, this is just running python3 setup.py test
	${SETUP_ENV} && colcon test --packages-select ${PACKAGE} --abort-on-error
	${SETUP_ENV} && colcon test-result --test-result-base build/${PACKAGE} --all

tests:
	@echo "**************************************************************************************"
	@echo "                                Tests";
	@echo "**************************************************************************************"
	# for python packages, this is just running python3 setup.py test
	${SETUP_ENV} && colcon test
	${SETUP_ENV} && colcon test-result --all

info:
	@echo "**************************************************************************************"
	@echo "                            Package Information";
	@echo "**************************************************************************************"
	colcon info

list:
	@echo "**************************************************************************************"
	@echo "                              Package Build Order";
	@echo "**************************************************************************************"
	colcon list -t -n  # text list

graph:
	@echo "**************************************************************************************"
	@echo "                              Package Build Graph";
	@echo "**************************************************************************************"
	colcon graph --dot > /tmp/graph.dot && xdot /tmp/graph.dot

.PHONY: tests clean