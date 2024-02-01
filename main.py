# #################################################################################

from time import sleep
from machine import Pin, PWM

DUTY_MAX = 2**16 - 1

duty_u16 = 0
delta_d = 16

p = PWM(Pin(2), 1000, duty_u16=duty_u16)
print(p)

while True:
    p.duty_u16(duty_u16)

    sleep(1 / 1000)

    duty_u16 += delta_d
    if duty_u16 >= DUTY_MAX:
        duty_u16 = DUTY_MAX
        delta_d = -delta_d
    elif duty_u16 <= 0:
        duty_u16 = 0
        delta_d = -delta_d

# #################################################################################

# from machine import Pin
# from time import sleep
#
# led = Pin(2, Pin.OUT)
#
# while True:
#   led.value(not led.value())
#   sleep(0.1)

# #################################################################################

# import machine
#
# machine.freq()          # get the current frequency of the CPU
# machine.freq(240000000) # set the CPU frequency to 240 MHz

# #################################################################################

# from machine import Pin
#
# p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
# p0.on()                 # set pin to "on" (high) level
# p0.off()                # set pin to "off" (low) level
# p0.value(1)             # set pin to on/high
#
# p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
# print(p2.value())       # get value, 0 or 1
#
# p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
# p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation
# p6 = Pin(6, Pin.OUT, drive=Pin.DRIVE_3) # set maximum drive strength

# #################################################################################

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
