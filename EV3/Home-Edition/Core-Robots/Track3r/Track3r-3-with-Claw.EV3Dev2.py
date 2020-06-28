#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)
IR_BEACON_DRIVER = \
    IRBeaconRemoteControlledTank(
        left_motor_port=OUTPUT_B,
        right_motor_port=OUTPUT_C,
        motor_class=LargeMotor,
        ir_sensor_port=INPUT_4,
        ir_beacon_channel=1)

IR_SENSOR = InfraredSensor(address=INPUT_4)

SPEAKER = Sound()


def drive_once_by_ir_beacon(channel: int = 1, speed: float = 100):
    if IR_SENSOR.top_left(channel) and IR_SENSOR.top_right(channel):
        # go forward
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=speed)

    elif IR_SENSOR.bottom_left(channel) and IR_SENSOR.bottom_right(channel):
        # go backward
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=-speed)

    elif IR_SENSOR.top_left(channel) and IR_SENSOR.bottom_right(channel):
        # turn around left
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=speed)

    elif IR_SENSOR.top_right(channel) and IR_SENSOR.bottom_left(channel):
        # turn around right
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=-speed)

    elif IR_SENSOR.top_left(channel):
        # turn left
        TANK_DRIVER.on(
            left_speed=0,
            right_speed=speed)

    elif IR_SENSOR.top_right(channel):
        # turn right
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=0)

    elif IR_SENSOR.bottom_left(channel):
        # left backward
        TANK_DRIVER.on(
            left_speed=0,
            right_speed=-speed)

    elif IR_SENSOR.bottom_right(channel):
        # right backward
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=0)

    else:
        TANK_DRIVER.off(brake=False)


is_grabbing = False


def grab_or_release_objects_by_ir_beacon(channel: int = 1, speed: float = 1):
    global is_grabbing

    if IR_SENSOR.beacon(channel=channel):
        if is_grabbing:
            MEDIUM_MOTOR.on(
                speed=-speed,
                block=False,
                brake=False)

            SPEAKER.play_file(
                wav_file='/home/robot/sound/Air release.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            is_grabbing = False

        else:
            MEDIUM_MOTOR.on(
                speed=speed,
                block=False,
                brake=False)

            SPEAKER.play_file(
                wav_file='/home/robot/sound/Airbrake.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            is_grabbing = True

        while IR_SENSOR.beacon(channel=channel):
            pass


while True:
    IR_BEACON_DRIVER.drive(speed=100)
    # drive_once_by_ir_beacon(
    #     channel=1,
    #     speed=100)

    grab_or_release_objects_by_ir_beacon(
        channel=1,
        speed=100)
