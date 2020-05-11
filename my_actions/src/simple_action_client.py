#! /usr/bin/env python
##importing modules
import rospy

import actionlib
from my_actions.msg import TimerAction, TimerGoal, TimerResult

#setup
rospy.init_node('timer_action_client')
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()#wait
goal = TimerGoal()#set goal object
goal.time_to_wait = rospy.Duration.from_sec(5.0)#duration
client.send_goal(goal)
client.wait_for_result()
print('Time elapsed: %f' % (client.get_result().time_elapsed.to_sec()))#print only once since no need to update.
