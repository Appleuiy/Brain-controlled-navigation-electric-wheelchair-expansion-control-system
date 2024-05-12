#! /usr/bin/env python3
# coding=utf-8


import rospy
import sys
from std_msgs.msg import String
import signal
import threading
import core

lock = threading.Lock()
data = {}


def dealData(data):
    print(f"处理数据{data}")
    if int(data[2]) == 0:
        return data[1]
    return data[2]


def sendData(var):
    print(f'发送指令给duoji{var}')
    core.ctl_duoji(int(var))


def deal_imu_msg(msg):
    with lock:
        global data
        print(f'type:1, value:{msg.data}')
        data[1] = msg.data
        if len(data) == 2:
            var = dealData(data)
            sendData(var)
            data.clear()


def deal_openmv_msg(msg):
    # rospy.loginfo("I heard:%s",msg.data)
    with lock:
        global data
        print(f'type:2.om, value:{msg.data}')
        data[2] = msg.data
        if len(data) == 2:
            var = dealData(data)
            sendData(var)
            data.clear()


def deal_laser_msg(msg):
    # rospy.loginfo("I heard:%s",msg.data)
    with lock:
        global data
        print(f'type:2.la, value:{msg.data}')
        data[2] = msg.data
        if len(data) == 2:
            var = dealData(data)
            sendData(var)
            data.clear()


def sigint_handler(sig, frame):
    print("\nReceived SIGINT, exiting...")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    rospy.init_node("center")
    sub_openmv = rospy.Subscriber("openmv_serial", String, deal_openmv_msg, queue_size=10)
    sub_imu = rospy.Subscriber("imu_serial", String, deal_imu_msg, queue_size=10)
    sub_laser = rospy.Subscriber("laser_serial", String, deal_laser_msg, queue_size=10)
    rospy.spin()

