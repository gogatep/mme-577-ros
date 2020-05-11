#!/usr/bin/env python

##import modules
import rospy
from my_services.srv import WordCount, WordCountResponse

##define the service function to count words
def count_words(request):
  return len(request.words.split()) # num of words

##setup
rospy.init_node('service_server')

service = rospy.Service( # register service
  'word_count', # service name
  WordCount,    # service type
  count_words   # function service provides
)

rospy.spin()##keep node alive