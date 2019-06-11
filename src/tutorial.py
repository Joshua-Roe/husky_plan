#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty

rospy.wait_for_service('/rosplan_problem_interface/problem_generation_server')
rospy.wait_for_service('/rosplan_planner_interface/planning_server')

problem_generation_server = rospy.ServiceProxy('/rosplan_problem_interface/problem_generation_server', Empty)
planning_server = rospy.ServiceProxy('/rosplan_planner_interface/planning_server', Empty)

resp1 = problem_generation_server()
print(resp1)
resp2 = planning_server()
print(resp2)
exit()