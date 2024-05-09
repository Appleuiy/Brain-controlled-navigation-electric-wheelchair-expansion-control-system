import threading
from threading import Thread
import time
import openMvSerial
import imuSerial
import arduinoSerial

lock = threading.Lock()


def dealData(data):
    print(f"处理数据{data}")
    if data[2] == 0:
        return data[1]
    return data[2]

def sendData(var):
    print(f'发送指令给单片机{var}')
    arduinoSerial.sendData(var)


data = {}
def getData(type,value):
    with lock:
        global data 
        print(f'type:{type}, value:{value}')
        data[type]=value

    if len(data) == 2:
        var = dealData(data)
        sendData(var)
        data.clear()


def main():
    # 创建 Thread 实例
    # imuSerial.main(getData)
    

    # task1 = asyncio.create_task(openMvSerial.serialStartWork(getData))
    # task2 = asyncio.create_task(imuSerial.main(getData))
    # asyncio.gather(task2,task1)


    t2 = Thread(target=imuSerial.main, args=(getData,))
    # # 启动线程运行
    t2.start()
    time.sleep(30)

    t1 = Thread(target=openMvSerial.serialStartWork,args=(getData,))
    t1.start()
    
    # # 等待所有线程执行完毕
    # t1.join()  # join() 等待线程终止，要不然一直挂起
    t2.join()
    t1.join()

if __name__=="__main__":
    main()