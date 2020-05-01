#!/usr/bin/env python
import rospy
from my_services.srv import WordCount
import sys

rospy.init_node('service_client')

rospy.wait_for_service('word_count') # wait for registration
word_counter = rospy.ServiceProxy( # set up proxy
  'word_count', # service name
  WordCount     # service type
)
words = ' '.join(sys.argv[1:3]) # parse args # to remove the __name etc I have fixed the arg size. but if the input is to be changed then the arg size must be changed.
word_count = word_counter(words) # use service

print(words+'--> has '+str(word_count.count)+' words')