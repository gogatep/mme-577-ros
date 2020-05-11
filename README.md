# Robot Operating System (ROS) Demonstration Project

ROS project for ROS mini-course [supplement to MME 577]

This project is aimed to demonstrate basic features of ROS. The project includes three packages that demonstrate three seperate functionalities of ROS. The packages are: my_topics,my_services,my_actions. 
* my_topics: Publishes and Subscribes to topics.
* my_services: Requests and offers services.
* my_actions: Performs requested actions.

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

The following instructions will aid in setting up the project on your local machine for demonstration and testing purposes. 

### Prerequisites

The following things are needed to run the project.

1. Ubuntu Bionic (18.04.4) LTS - The operating system needed.
2. Python 2 - Get python 2.7 from (https://www.python.org/downloads/)
3. ROS Melodic Morenia - Get the 'desktop-full' version from (http://wiki.ros.org/melodic/Installation/Ubuntu) 


### Installing

Make sure home directory does not have a 'mme-577-ros' folder or a 'code' folder. 
Then, follow the following code step by step to setup the project on local system - or create and run a shell script containing the following code.

```bash
sudo apt-get install git
cd ~ 
git clone 'https://github.com/gogatep/mme-577-ros/'
mkdir -p code 
cd code
mkdir -p ros_ws_01
cd ros_ws_01
mkdir -p src
cd src
catkin_init_workspace
cd .. 
catkin_make
source devel/setup.bash
cd ~/code/ros_ws_01/src
cp -a  ~/mme-577-ros/.  ~/code/ros_ws_01/src
chmod u+x ~/code/ros_ws_01/src/my_topics/src/topic_publisher.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/topic_subscriber.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/message_publisher.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/message_subscriber.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/doubler.py
chmod u+x ~/code/ros_ws_01/src/my_topics/src/doubled_subscriber.py
chmod u+x ~/code/ros_ws_01/src/my_services/src/service_client.py
chmod u+x ~/code/ros_ws_01/src/my_services/src/service_server.py
chmod u+x ~/code/ros_ws_01/src/my_actions/src/simple_action_client.py
chmod u+x ~/code/ros_ws_01/src/my_actions/src/fancy_action_client.py
chmod u+x ~/code/ros_ws_01/src/my_actions/src/simple_action_server.py
chmod u+x ~/code/ros_ws_01/src/my_actions/src/fancy_action_server.py
cd ..
source devel/setup.bash
catkin_make
source devel/setup.bash

```

Check if correctly installed using the following demonstration. 

If a shell script was used then the source needs to be set manually for the test to work correctly - i.e run the following code manually.

Run the following code in one shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roscore

```
Run the following code in another shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roslaunch my_topics topic_launch.launch

```

## Package Details and Testing

The three packages are explained in further details and test for functionality of each package is shown below. The following code needs to be run manually. 

The launch file is modified to close on its - i.e close without pressing ctrl+c. So using the launch file for the tests will throw some warnings but it's harmless. And testing can also be done manually using rosrun.

### My Topics

A topic is published by topics_publisher and that topic is subscribed to by topics_subscriber. Similarly a specific message is published by message_publisher and that topic is subscribed to by message_subscriber. For this project an arbitrary rate of publication was chosen.

And the doubler script publishes the doubled input, which is recieved from a subscribed topic - topic_publisher. So the doubler script initiates a node that does both - subscribing and publishing.


#### Usage

Each new terminal needs a source command as demonstrated below. 'roscore' command is needed to run ros packages.
roslaunch command is used to launch package. The syntaxt for the command is: roslaunch <topic> <file.launch>.
 
Topic publication is asynchronous process. The publication and subscribtion are independent of each other.

#### Testing

This runs the package and verifies that it is setup correctly.

Run the following code in one shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roscore

```
Run the following code in another shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roslaunch my_topics topic_launch.launch

```

### My Services

A service is made available by the services_server and that service is requested by a client - services_client. This package only has one pair of example scripts. 

While 'topics' allows for very flexible communication, it is not ideal for request and reply. So ros services is used - especially when remote procedure call is needed on a distributed computing network.


#### Usage

Each new terminal needs a source command as demonstrated below. 'roscore' command is needed to run ros packages.
roslaunch command is used to launch package. The syntaxt for the command is: roslaunch <topic> <file.launch>.
 
The server and the client are interdependent - i.e they cannot operate without each other. 

#### Testing

This runs the package and verifies that it is setup correctly.

Run the following code in one shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roscore

```
Run the following code in another shell/terminal.
There should be no gaps between ' in:=" '.The string "hello world" can be changed for a different string input.
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roslaunch my_services services.launch in:="hello world"

```
### My Actions

A action is made available by the simple/fancy action servers and that action is requested by an action client. This package has simple and fancy action. Simple action simple print the time elapsed but the fancy action shows time remaining and time elapsed during the execution.

ROS 'actions' are similar to 'services' but they provide feedback during execution. This can be used to gauge progress.

#### Usage

Each new terminal needs a source command as demonstrated below. 'roscore' command is needed to run ros packages.
roslaunch command is used to launch package. The syntaxt for the command is: roslaunch <topic> <file.launch>.
 
The server and the client are interdependent - i.e they cannot operate without each other. 

#### Testing

This runs the package and verifies that it is setup correctly.

Run the following code in one shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roscore

```
Run the following code in another shell/terminal
```bash
cd ~/code/ros_ws_01/
source devel/setup.bash
roslaunch my_actions action.launch

```
And run the following code in yet another shell/terminal
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

