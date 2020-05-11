#! /usr/bin/env python
## import modules
import rospy

import time
import actionlib
from my_actions.msg import TimerAction, TimerGoal


def feedback_cb(feedback):# feedback callback function
    print('[Feedback] Time elapsed: %f' % (feedback.time_elapsed.to_sec()))
    print('[Feedback] Time remaining: %f' % (feedback.time_remaining.to_sec()))

#setup
rospy.init_node('timer_action_client')# initialize node
client = actionlib.SimpleActionClient('timer', TimerAction)# register client
client.wait_for_server()# wait for action server
goal = TimerGoal()# create goal
goal.time_to_wait = rospy.Duration.from_sec(5.0)# set field
# Uncomment this line to test server-side abort:
#goal.time_to_wait = rospy.Duration.from_sec(500.0)

client.send_goal(goal, feedback_cb=feedback_cb)# send goal
# Uncomment these lines to test goal preemption:
#time.sleep(3.0)
#client.cancel_goal()

client.wait_for_result()# wait for action server to finish
##printing
print('[Result] State: %d' % (client.get_state()))
print('[Result] Status: %s' % (client.get_goal_status_text()))
print('[Result] Time elapsed: %f' %
      (client.get_result().time_elapsed.to_sec()))
print('[Result] Updates sent: %d' % (client.get_result().updates_sent))
