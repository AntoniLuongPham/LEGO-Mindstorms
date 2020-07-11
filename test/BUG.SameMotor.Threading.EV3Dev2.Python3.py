#!/usr/bin/env python3


from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor

from threading import Thread


TOUCH_SENSOR = TouchSensor(address=INPUT_1)
IR_SENSOR = InfraredSensor(address=INPUT_4)
MOTOR = MediumMotor(address=OUTPUT_A)


def touch_to_turn_motor():
    while True:
        if TOUCH_SENSOR.is_pressed:
            MOTOR.on_for_seconds(
                speed=100,
                seconds=1,
                brake=True,
                block=True)


def press_ir_button_to_turn_motor():
    while True:
        if IR_SENSOR.buttons_pressed(channel=1):
            MOTOR.on_for_seconds(
                speed=-100,
                seconds=1,
                brake=True,
                block=True)


Thread(target=touch_to_turn_motor,
       daemon=True).start()

press_ir_button_to_turn_motor()
