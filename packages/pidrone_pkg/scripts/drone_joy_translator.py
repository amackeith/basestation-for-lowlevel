#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
import numpy as np
import os
from geometry_msgs.msg import Pose, Twist
from pidrone_pkg.msg import Mode, RC
from std_msgs.msg import Float32, Empty, Bool

z_total_steps = 24
#z_counter = (z_total_steps / 4) - 1
z_counter = -1
z_step = 5 # cm
scalar = 15
modeMsg = Mode()
modeMsg.mode = 'DISARMED'
positionMsg = Bool()
positionMsg.data = True
poseMsg = Pose()
twistMsg = Twist()

modepub = rospy.Publisher('desired/mode', Mode, queue_size=1)

#positionPub = rospy.Publisher('position_control', Bool, queue_size=1)
#positionControlPub = rospy.Publisher('desired/pose', Pose, queue_size=1)

#elocityControlPub = rospy.Publisher('desired/twist', Twist, queue_size=1)

#mappub = rospy.Publisher('map', Empty, queue_size=1)

#resetpub = rospy.Publisher('reset_transform', Empty, queue_size=1)
#togglepub = rospy.Publisher('toggle_transform', Empty, queue_size=1)
#rospy.set_param('joy/autorepeat_rate', 20)

roll = 1500
pitch = 1500
yaw = 1500
throttle = 1000
cmdpub = rospy.Publisher('/duckiedrone/fly_commands', RC, queue_size=1)





def cmd_prompt(rpyt):
    def publish_cmd(cmd):
        """Publish the controls to /pidrone/fly_commands """
        msg = RC()
        msg.roll = cmd[0]
        msg.pitch = cmd[1]
        msg.yaw = cmd[2]
        msg.throttle = cmd[3]
        print(cmd)
        cmdpub.publish(msg)



    try:

        r, p, y, t = rpyt.split()
        publish_cmd([int(r), int(p), int(y), int(t)])
    except:
        publish_cmd([1000, 1000, 1000,1000])
    

def main():
    node_name = os.path.splitext(os.path.basename(__file__))[0]
    rospy.init_node(node_name)
    while not rospy.is_shutdown():
        print "RPYT"
        
        rpyt = raw_input()
        cmd_prompt(rpyt)

main()
