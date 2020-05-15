#coding=UTF-8
import RPi.GPIO as GPIO
import time

def checkdist():
        #发出触发信号
        GPIO.output(2,GPIO.HIGH)
        #保持10us以上（我选择15us）
        time.sleep(0.000015)
        GPIO.output(2,GPIO.LOW)
        while not GPIO.input(3):
                pass
        #发现高电平时开时计时
        t1 = time.time()
        while GPIO.input(3):
                pass
        #高电平结束停止计时
        t2 = time.time()
        global d
        d = (t2-t1)*340/2
        #返回距离，单位为米
        return (t2-t1)*340/2
GPIO.setmode(GPIO.BCM)
#第3号针，GPIO2
GPIO.setup(2,GPIO.OUT,initial=GPIO.LOW)
#第5号针，GPIO3
GPIO.setup(3,GPIO.IN)

time.sleep(2)

def servo ():
    ServoPin = 26
    PWMFreq = 50                        # PWM信号频率

    GPIO.setmode(GPIO.BCM)              # 使用BCM编号方式
    GPIO.setup(ServoPin, GPIO.OUT)      # 将GPIO19设置为输出模式
    pwm = GPIO.PWM(ServoPin, PWMFreq)   # 创建PWM对象，并设置频率为50
    pwm.start(0)                        # 启动PWM，并设置初始占空比0

        while True:
            pwm.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止
            direction = float(input("Pleas input the direction: "))
            if direction < 0 or direction > 180:
                print("Please input a direction between 0 an 180.")
                continue

            duty = (1/18) * direction + 2.5   # 将角度转换为占空比
            pwm.ChangeDutyCycle(duty)         # 改变PWM占空比
            time.sleep(4)                    #等待控制周期结束
            pwm.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止
            pwm.stop()
            break

try:
        while True:
            print ('Distance: %0.2f m' %checkdist())
            if d < 0.5 :
                servo ()
            time.sleep(0.4)

except KeyboardInterrupt:
        GPIO.cleanup()