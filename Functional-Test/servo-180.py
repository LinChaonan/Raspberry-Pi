import RPi.GPIO as GPIO                 # 引入GPIO模块
import time
# 110关闭，180打开
# 推杆，0-35
# 下方开盖，前80-0
# 下方开盖，后0-80
if __name__ == '__main__':
    ServoPin = 26
    PWMFreq = 50                        # PWM信号频率

    GPIO.setmode(GPIO.BCM)              # 使用BCM编号方式
    GPIO.setup(ServoPin, GPIO.OUT)      # 将GPIO19设置为输出模式
    pwm = GPIO.PWM(ServoPin, PWMFreq)   # 创建PWM对象，并设置频率为50
    pwm.start(0)                        # 启动PWM，并设置初始占空比0

    try:
        while True:
            # 等待输入一个0到180的角度
            pwm.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止
            direction = float(input("Pleas input the direction: "))
            if direction < 0 or direction > 180:
                print("Please input a direction between 0 an 180.")
                continue

            duty = (1/18) * direction + 2.5   # 将角度转换为占空比
            pwm.ChangeDutyCycle(duty)         # 改变PWM占空比
            time.sleep(4)                     #等待控制周期结束
            pwm.ChangeDutyCycle(0)            #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止
    finally:
        pwm.stop()                      # 停止PWM
        GPIO.cleanup()                  # 清理释放GPIO资源，将GPIO复位0
