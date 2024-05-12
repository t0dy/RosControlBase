import Brige
import serial
import time
mode= 0 #模式切换 0寻找钩码模式 1检测到钩码 2粗略定位位置 3校准pid位置误差并夹取
task_mode = 0 #任务切换 收集5个钩码任务：0 摆放任务：1
get_count = 0   #计钩码获取数
com = serial.Serial('COM8', 1000000)
data=Brige.Baseon(0,5,1,1)  #cm/s   0.1 rad/s
com.write(data)
time.sleep(1)
data=Brige.Baseoff()
com.write(data)