#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.tools import wait


class El3ctricGuitar(EV3Brick):
    NOTES = [1318, 1174, 987, 880, 783, 659, 587, 493, 440, 392, 329, 293]
    N_NOTES = len(NOTES)

    def __init__(
            self, lever_motor_port: Port = Port.D,
            touch_sensor_port: Port = Port.S1, ir_sensor_port: Port = Port.S4):
        self.lever_motor = Motor(port=lever_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)

        self.lever_motor.run_time(
            speed=50,
            time=1000,
            then=Stop.COAST,
            wait=True)

        self.lever_motor.run_angle(
            speed=50,
            rotation_angle=-30,
            then=Stop.BRAKE,
            wait=True)

        wait(100)

        self.lever_motor.reset_angle(angle=0)

    def read_lever(self):
        self.lever = self.lever_motor.angle()

        if abs(self.lever) <= 4:
            self.lever = 0

    def keep_reading_lever(self):
        while True:
            self.read_lever()

    def play_music(self):
        # fret = 0

        raw = sum(self.ir_sensor.distance() for _ in range(4)) / 4

        # for i in range(self.N_NOTES):
        #     if 5 * i - 1 <= raw <= 5 * (i + 1):
        #         fret = i

        # if fret >= self.N_NOTES:
        #     fret = self.N_NOTES - 1

        if not self.touch_sensor.pressed():
            self.speaker.beep(
                frequency=self.NOTES[min(int(raw / 5), self.N_NOTES - 1)]
                          - 11 * self.lever,
                duration=100)

    def main(self):
        self.screen.load_image(ImageFile.EV3)

        self.light.on(color=Color.ORANGE)

        while True:
            self.read_lever()
            self.play_music()


if __name__ == '__main__':
    EL3CTRIC_GUITAR = El3ctricGuitar()

    EL3CTRIC_GUITAR.main()
