import serial, time


def serialStartWork(getData):

    print("openmv串口通信开始")
    Port = "/dev/ttyACM0"  # 串口
    baudRate = 115200  # 波特率
    ser = serial.Serial(Port, baudRate, timeout=1)
    while True:
        # send = '1'  # 发送给arduino的数据
        #ser.write(send.encode())
        time.sleep(0.1)
        str = ser.readline().strip().decode()  # 获取arduino发送的数据
        #str = '8'
        #print('openmv的数据是'+str)
        if str != "":
            getData(2, int(str))

    ser.close()