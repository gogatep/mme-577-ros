#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from random import random # for random numbers!

rospy.init_node('number_publisher') # initialize node

pub = rospy.Publisher(    # register topic
  'number',              # topic name
  Int32,                # custom message type
  queue_size=3            # queue size
)

rate = rospy.Rate(2) # set rate
count=0
while not rospy.is_shutdown(): # loop
  #msg = Int32()           # declare type
  #msg.data = random()       # assign value
  count += 1 # increment
  pub.publish(count)  # publish!
  rate.sleep()      # sleep to keep rate