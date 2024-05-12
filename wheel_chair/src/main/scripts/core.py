#! /usr/bin/env python3
#coding=utf-8
'''
FashionStar Uart舵机 
> 设置舵机角度 <
--------------------------------------------------
 * 作者: 深圳市华馨京科技有限公司
 * 网站：https://fashionrobo.com/
 * 更新时间: 2023/03/13
--------------------------------------------------
'''
# 添加uservo.py的系统路径
import sys
sys.path.append("../../src")
# 导入依赖
import time
import struct
import serial
from uservo import UartServoManager

# 参数配置
# 角度定义
SERVO_PORT_NAME =  '/dev/ttyUSB0'		# 舵机串口号
SERVO_BAUDRATE = 57600			# 舵机的波特率
SERVO_ID0 = 0					# 舵机的ID号
SERVO_ID1 = 1	
SERVO_HAS_MTURN_FUNC = False	# 舵机是否拥有多圈模式

# 初始化串口
uart0 = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
					 parity=serial.PARITY_NONE, stopbits=1,\
					 bytesize=8,timeout=0)
# uart1 = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
# 					 parity=serial.PARITY_NONE, stopbits=1,\
# 					 bytesize=8,timeout=0)
# 初始化舵机管理器
uservo0 = UartServoManager(uart0, is_debug=True)
# uservo0 = UartServoManager(uart0, is_debug=True)
# uservo0.wait() # 等待舵机静止
# uservo0.wait() # 等待舵机静止



uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0) 
uservo0.wait() # 等待舵机静止
uservo0.set_servo_angle(SERVO_ID1, 0.0, interval=0) 
uservo0.wait() # 等待舵机静止

print("RESETTED")


def ctl_duoji(ctlNum):
    if ctlNum == 1: # 左前
        print("LF 0->92,1->-45")
        uservo0.set_servo_angle(SERVO_ID1, -45.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        uservo0.set_servo_angle(SERVO_ID0, 92.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        time.sleep(1)
        uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0)
        uservo0.wait() # 等待舵机静止 
    elif ctlNum == 2: # 前
        print("F 0->92,1->0")
        uservo0.set_servo_angle(SERVO_ID1, 0.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        uservo0.set_servo_angle(SERVO_ID0, 92.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        time.sleep(1)
        uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0)
        uservo0.wait() # 等待舵机静止
    elif ctlNum == 3: # 右前
        print("RF 0->92,1->45")
        uservo0.set_servo_angle(SERVO_ID1, 45.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        uservo0.set_servo_angle(SERVO_ID0, 92.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        time.sleep(1)
        uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0)
        uservo0.wait() # 等待舵机静止
    elif ctlNum == 4: # 左
        print("L 0->92,1->-90")
        uservo0.set_servo_angle(SERVO_ID1, -90.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        uservo0.set_servo_angle(SERVO_ID0, 92.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        time.sleep(1)
        uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0)
        uservo0.wait() # 等待舵机静止
    elif ctlNum == 5: # 停
        print("S 0->0,1->0")
        uservo0.set_servo_angle(SERVO_ID1, 0.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0) 
        uservo0.wait() # 等待舵机静止
    elif ctlNum == 6: # 右
        print("R 0->92,1->90")
        uservo0.set_servo_angle(SERVO_ID1, 90.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        uservo0.set_servo_angle(SERVO_ID0, 92.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        time.sleep(1)
        uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0)
        uservo0.wait() # 等待舵机静止
    elif ctlNum == 7: # 左后
        print("LB 0->92,1->-135")
        uservo0.set_servo_angle(SERVO_ID1, -135.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        uservo0.set_servo_angle(SERVO_ID0, 92.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        time.sleep(1)
        uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0)
    elif ctlNum == 8: # 后
        print("B 0->92,1->180")
        uservo0.set_servo_angle(SERVO_ID1, 180.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        uservo0.set_servo_angle(SERVO_ID0, 92.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        time.sleep(1)
        uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0)
        uservo0.wait() # 等待舵机静止
    elif ctlNum == 9: # 右后
        print("RB 0->92,1->135")
        uservo0.set_servo_angle(SERVO_ID1, 135.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        uservo0.set_servo_angle(SERVO_ID0, 92.0, interval=0) 
        uservo0.wait() # 等待舵机静止
        time.sleep(1)
        uservo0.set_servo_angle(SERVO_ID0, 0.0, interval=0)
        uservo0.wait() # 等待舵机静止


#x = 1
#while True:
#    x = x + 1
#    x = x%9 + 1
#    for a in range(10):
#        ctl_duoji(x)


