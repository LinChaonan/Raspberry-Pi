import RPi.GPIO as GPIO                 # 引入GPIO模块
import time
# 110关闭，180打开
# 推杆，0-30
# 下方开盖，前80-0
# 下方开盖，后0-80
if __name__ == '__main__':
    ServoPin1 = 19
    ServoPin2 = 26
    PWMFreq = 50                        # PWM信号频率

    GPIO.setmode(GPIO.BCM)              # 使用BCM编号方式
    GPIO.setup(ServoPin1, GPIO.OUT)      # 将GPIO19设置为输出模式
    GPIO.setup(ServoPin2, GPIO.OUT)      # 将GPIO19设置为输出模式
    pwm1 = GPIO.PWM(ServoPin1, PWMFreq)   # 创建PWM对象，并设置频率为50
    pwm2 = GPIO.PWM(ServoPin2, PWMFreq)   # 创建PWM对象，并设置频率为50
    pwm1.start(0)                        # 启动PWM，并设置初始占空比0
    pwm2.start(0)                        # 启动PWM，并设置初始占空比0

    try:
        while True:
            # 等待输入一个0到180的角度
            pwm2.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止
            pwm1.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止
            direction2 = float(80)
            direction1 = float(0)
            duty2 = (1/18) * direction2 + 2.5   # 将角度转换为占空比
            duty1 = (1/18) * direction1 + 2.5   # 将角度转换为占空比
            pwm2.ChangeDutyCycle(duty2)         # 改变PWM占空比
            pwm1.ChangeDutyCycle(duty1)         # 改变PWM占空比
            time.sleep(4)                     #等待控制周期结束
            pwm2.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止            
            pwm1.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止


            pwm2.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止
            pwm1.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止
            direction2 = float(0)
            direction1 = float(80)
            duty2 = (1/18) * direction2 + 2.5   # 将角度转换为占空比
            duty1 = (1/18) * direction1 + 2.5   # 将角度转换为占空比
            pwm2.ChangeDutyCycle(duty2)         # 改变PWM占空比
            pwm1.ChangeDutyCycle(duty1)         # 改变PWM占空比
            time.sleep(4)                     #等待控制周期结束
            pwm2.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止            
            pwm1.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止

            break

    finally:
        pwm.stop()                      # 停止PWM
        GPIO.cleanup()                  # 清理释放GPIO资源，将GPIO复位0