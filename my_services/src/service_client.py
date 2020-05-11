#!/usr/bin/env python

##import modules
import rospy
from my_services.srv import WordCount
import sys

##setup
rospy.init_node('service_client')

rospy.wait_for_service('word_count') # wait for registration
word_counter = rospy.ServiceProxy( # set up proxy
  'word_count', # service name
  WordCount     # service type
)

## take all string inputs and join them
words = ' '.join(sys.argv[1:3]) # parse args # to remove the __name etc the arg size can be modified. but if the input is to be changed then the arg size must be changed.
words2=[k for k in sys.argv[1:] if '_' not in k] ## improved way to remove __name etc from input
words3 = ' '.join(words2) 
word_count = word_counter(words3) # use service

## print word count
print(words3+'--> has '+str(word_count.count)+' words')