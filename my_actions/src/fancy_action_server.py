#! /usr/bin/env python
## importing modules
import rospy

import time
import actionlib
from my_actions.msg import TimerAction, TimerResult, TimerFeedback


def do_timer(goal):# action function
    start_time = time.time()#needed to tell how much time has elapsed
    update_count = 0
    if goal.time_to_wait.to_sec() > 60.0:# check req duration
        result = TimerResult()
        result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        result.updates_sent = update_count
        server.set_aborted(result, "Timer aborted due to too-long wait")
        return# too long of a requested wait
    while (time.time() - start_time) < goal.time_to_wait.to_sec():# waiting to meet goal duration
        if server.is_preempt_requested():# check preemption
            result = TimerResult()
            result.time_elapsed = rospy.Duration.from_sec(
                    time.time() - start_time)
            result.updates_sent = update_count
            server.set_preempted(result, "Timer preempted")
            return
        feedback = TimerFeedback()
        feedback.time_elapsed = rospy.Duration.from_sec(
                time.time() - start_time)
        feedback.time_remaining = goal.time_to_wait - feedback.time_elapsed
        server.publish_feedback(feedback)
        update_count += 1#to show at the end 
        time.sleep(1.0)
    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = update_count
    server.set_succeeded(result, "Timer completed successfully")

#setup
rospy.init_node('timer_action_server')# initialize node
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
rospy.spin()#keep node alive
