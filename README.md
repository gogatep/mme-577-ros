# Robot Operating System (ROS) Demonstration Package

ROS project for ROS mini-course [supplement to MME 577]

One Paragraph of project description goes here

## Table of Contents
<!--- - [Robot Operating System (ROS) Demonstration Package](#robot-operating-system--ros--demonstration-package)--->
  * [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Installing](#installing)
  * [Running the tests / configuring](#running-the-tests---configuring)
    + [ROS package: my_topics](#ros-package--my-topics)
      - [Getting started](#getting-started)
      - [Usage](#usage)
      - [Break down into end to end tests](#break-down-into-end-to-end-tests)
      - [And coding style tests](#and-coding-style-tests)
    + [ROS package: my_services](#ros-package--my-services)
      - [Getting started](#getting-started-1)
      - [Usage](#usage-1)
      - [Break down into end to end tests](#break-down-into-end-to-end-tests-1)
      - [And coding style tests](#and-coding-style-tests-1)
    + [ROS package: my_actions](#ros-package--my-actions)
      - [Getting started](#getting-started-2)
      - [Usage](#usage-2)
      - [Break down into end to end tests](#break-down-into-end-to-end-tests-2)
      - [And coding style tests](#and-coding-style-tests-2)
  * [Deployment](#deployment)
  * [Built With](#built-with)
  * [Authors](#authors)
  * [License](#license)
  * [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

linux system is needed. git is reccommeded -for convinence. 

### Prerequisites

What things you need to install the software and how to install them

create a directory for the code. add a src sub directory. and convert the main directory to be your workspace.
then use git to get the code inside the src folder - or use the download option on github. 
1. Ubuntu Bionic (18.04.4) LTS
2. Python 2
3. ROS Melodic Moreni (http://wiki.ros.org/melodic/Installation/Ubuntu) [desktop-full]
4. Set up an workspace

```bash
cd ~ # change directory to user home
mkdir -p code # -p creates dir only if it doesn't exist
cd code # change directory into code
mkdir -p ros_ws_01
cd ros_ws_01
mkdir -p src
cd src
catkin_init_workspace
cd .. # up a level to ros_ws
catkin_make
source devel/setup.bash
```

### Installing

Download package from github.com and copy the files to the source folder in the workspace. Or use the git clone command. [A workspace is shown as an example]

```bash
sudo apt-get install git
cd ~/code/ros_ws_01/src
git clone 'https://github.com/gogatep/mme-577-ros/'
```
Check if correctly installed using the following demonstration. 

In one shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roscore

```
In another shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roslaunch my_topics topic_launch.launch

```

## Package details and testing

Explain how to run the automated tests for this system

### ROS package: my_topics

A topic is published by a script to a node and that topic is subscribed to by a script. There are three topics in this 


#### Getting started
launch the launch file.

#### Usage

send information via nodes

#### Break down into end to end tests

Explain what these tests test and why

In one shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roscore

```
In another shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roslaunch my_topics topic_launch.launch

```

### ROS package: my_services

nodes request services from other nodes

#### Getting started

launch the launch file.

#### Usage

send information via nodes

#### Break down into end to end tests

Explain what these tests test and why

In one shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roscore

```
In another shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roslaunch my_services services.launch

```
### ROS package: my_actions

sends action through nodes.

#### Getting started

launch the launch file.

#### Usage

send information via nodes

#### Break down into end to end tests

Explain what these tests test and why

In one shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roscore

```
In another shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roslaunch my_actions action.launch

```
In another shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roslaunch my_actions fancy_action.launch

```
## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python](http://www.python.org/) - main code
* [ros](https://wiki.ros.org/) - OS 


## Authors

* **Parth Gogate**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Dr.Rico Picone: https://github.com/ricopicone/robotics-book-code

