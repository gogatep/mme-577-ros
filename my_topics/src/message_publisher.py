#!/usr/bin/env python

##import modules
import rospy
from my_topics.msg import Complex # custom message type
from random import random # for random numbers!


##setup
rospy.init_node('message_publisher') # initialize node

pub = rospy.Publisher(    # register topic
  'complex',              # topic name
  Complex,                # custom message type
  queue_size=3            # queue size
)

rate = rospy.Rate(2) # set rate


## while loop is used since data needs to be published constantly at a set rate

while not rospy.is_shutdown(): # loop
  msg = Complex()           # declare type
  msg.real = random()       # assign value
  msg.imaginary = random()  # assign value

  pub.publish(msg)  # publish!
  rate.sleep()      # sleep to keep rate