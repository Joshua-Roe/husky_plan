#!/usr/bin/env python

import sys
import rospy
from rosplan_problem_interface.srv import *
from rosplan_planner_interface.srv import *

rospy.wait_for_service('problem_generation_server')
rospy.wait_for_service('planning_server')

problem_generation_server = rospy.ServiceProxy('problem_generation_server', problem_generation_server)
planning_server = rospy.ServiceProxy('planning_server', planning_server)

resp1 = problem_generation_server()
print(resp1)
resp2 = planning_server()
print(resp2)
exit()