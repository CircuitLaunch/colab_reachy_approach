#!/usr/bin/env python3
import sys
import tf
from apriltag_ros.msg import AprilTagDetectionArray
import rospy

def tf_handle():
    # Initiating your node
    rospy.init_node('pedestal_to_camera')

    # Creating a listener object
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    # Creating reference variables -- these should be set to the child ids that
    #   are in your launch files
    from_frame = 'pedestal'
    to_frame = 'camera'

    # Setting up the publisher object
    pub = rospy.Publisher('switch_transform', PoseStamped, queue_size=10)

    # Creating a PoseStamped sobject
    stamped_trans = tf2_geometry_msgs.PoseStamped()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            # Looks up the transform between from_frame and to_frame.
            trans = tfBuffer.lookup_transform(from_frame, to_frame, rospy.Time(1))
            
        except (LookupException, ConnectivityException, ExtrapolationException):
            rate.sleep()
            continue


        # Populating our PoseStamped object
        stamped_trans.pose = trans


        # Publishing trans, the transform that we're looking for
        rospy.loginfo(stamped_trans)
        pub.publish(stamped_trans) 

if __name__ == '__main__':
    try:
        tf_handle()

    except rospy.ROSInterruptException:
            pass
        