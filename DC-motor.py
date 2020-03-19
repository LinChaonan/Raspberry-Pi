import RPi.GPIO as GPIO         # 引入GPIO模块
import time                     # 引入time模块

ENA = 13
IN1 = 19
IN2 = 26

try: # 初始化
    GPIO.setmode(GPIO.BCM)          # 使用BCM编号方式
    GPIO.setup(ENA, GPIO.OUT)       # 将连接ENA的GPIO引脚设置为输出模式
    GPIO.setup(IN1, GPIO.OUT)       # 将连接IN1的GPIO引脚设置为输出模式
    GPIO.setup(IN2, GPIO.OUT)       # 将连接IN2的GPIO引脚设置为输出模式

    while True:
        # 驱动电机正向旋转5秒
        GPIO.output(IN1, False)     # 将IN1设置为0
        GPIO.output(IN2, True)      # 将IN2设置为1
        GPIO.output(ENA, True)      # 将ENA设置为1，启动A通道电机
        time.sleep(5)            	# 等待电机转动5秒

        # 电机停止2秒
        GPIO.output(ENA, False)     # 将ENA设置为0
        time.sleep(2)            	# 等待电机停止2秒

        # 驱动电机反向旋转5秒
        GPIO.output(IN1, True)      # 将IN1设置为1
        GPIO.output(IN2, False)     # 将IN2设置为0
        GPIO.output(ENA, True)      # 将ENA设置为1，启动A通道电机
        time.sleep(5)            	# 等待电机转动5秒

        # 电机停止2秒
        GPIO.output(ENA, False)     # 将ENA设置为0
        time.sleep(2)            	# 等待电机停止2秒

finally:
    pwm.stop()                      # 停止PWM
    GPIO.cleanup()                  # 清理释放GPIO资源，将GPIO复位