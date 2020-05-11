# Robot Operating System (ROS) Demonstration Project

ROS project for ROS mini-course [supplement to MME 577]

This project is aimed to demonstrate basic features of ROS. The project includes three packages that demonstrate three seperate functionalities of ROS. my_topics,my_services,my_actions. 
* my_topics: Publishes and Subscribes to topics.
* my_services: requests and offers services.
* my_actions: performs requested actions.

## Table of Contents
<!--- - [Robot Operating System (ROS) Demonstration Package](#robot-operating-system--ros--demonstration-package)--->
  * [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Installing](#installing)
  * [ROS Package Details And Testing](#package-details-and-testing)
    + [my_topics](#my-topics)
      - [Usage](#usage)
      - [Break down into end to end tests](#break-down-into-end-to-end-tests)
      - [And coding style tests](#and-coding-style-tests)
    + [my_services](#my-services)
      - [Usage](#usage-1)
      - [Break down into end to end tests](#break-down-into-end-to-end-tests-1)
      - [And coding style tests](#and-coding-style-tests-1)
    + [my_actions](#my-actions)
      - [Usage](#usage-2)
      - [Break down into end to end tests](#break-down-into-end-to-end-tests-2)
      - [And coding style tests](#and-coding-style-tests-2)
  * [Built With](#built-with)
  * [Authors](#authors)
  * [License](#license)
  * [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for demonstration and testing purposes. 

### Prerequisites

The following things are needed to run the project.

1. Ubuntu Bionic (18.04.4) LTS - the operating system
2. Python 2 - get python 2.7 from (https://www.python.org/downloads/)
3. ROS Melodic Moreni - get from (http://wiki.ros.org/melodic/Installation/Ubuntu) [desktop-full]
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
git clone 'https://github.com/gogatep/mme-577-ros/my_topics'
chmod u+x ~/code/ros_ws_01/src/my_topics/src/topic_publisher.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/topic_subscriber.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/message_publisher.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/message_subscriber.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/number_publisher.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/doubled_subscriber.py
cd ..
source devel/setup.bash
catkin_make
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

## Package Details And Testing

The three packages are explained in further details and test for functionality of each package is shown below.

### my topics

A topic is published by topics_publisher and that topic is subscribed to by topics_subscriber. Similarly a sepcific message is published by message_publisher and subscribed by message_subscriber. And doubler both subscribes to topic_publisher and publishes the doubled int from topic_publisher to a seperate node. 


#### Usage

send information via nodes

#### Testing

This runs the package and verifies that it is setup correctly.

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

### my services

A service is requested by a script and completed by another.


#### Usage

send information via nodes

#### Testing

This runs the package and verifies that it is setup correctly.

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
### my actions

Simple action stops after 5 seconds and does not print anthing. Fancy action prints time elapsed and time remaining.

#### Usage

send information via nodes

#### Testing

This runs the package and verifies that it is setup correctly.

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

## Built With

* [Python](http://www.python.org/) 
* [ROS](https://wiki.ros.org/) 


## Authors

* **Parth Gogate**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Dr.Rico Picone: https://github.com/ricopicone/robotics-book-code

