#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, INPUT_1, INPUT_3, INPUT_4, 
    Leds, Screen, Sound
)
from ev3dev.helper import RemoteControlledTank

from multiprocessing import Process
from PIL import Image


class Ev3rstorm(RemoteControlledTank):
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            shooting_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3):
        super().__init__(
            left_motor=left_foot_motor_port, right_motor=right_foot_motor_port,
            polarity='normal')
        
        self.shooting_motor = MediumMotor(address=shooting_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.leds = Leds()
        self.screen = Screen()
        self.speaker = Sound()


    def detect_object_by_ir_sensor(self):
        if self.ir_sensor.proximity < 25: 
            self.leds.set_color(
                group=Leds.LEFT,
                color=Leds.RED,
                pct=1)
            self.leds.set_color(
                group=Leds.RIGHT,
                color=Leds.RED,
                pct=1)
            
            self.speaker.play(wav_file='/home/robot/sound/Object.wav').wait()
            self.speaker.play(wav_file='/home/robot/sound/Detected.wav').wait()
            self.speaker.play(wav_file='/home/robot/sound/Error alarm.wav').wait()

        else:
            self.leds.all_off()

    def keep_detecting_objects_by_ir_sensor(self):
        while True:
            self.detect_object_by_ir_sensor()
            

    def shoot_when_touched(self):
        if self.touch_sensor.is_pressed:
            if self.color_sensor.ambient_light_intensity < 5:   # 15 not dark enough
                self.speaker.play(wav_file='/home/robot/sound/Up.wav').wait()

                self.shooting_motor.run_to_rel_pos(
                    speed_sp=1000,   # degrees per second
                    position_sp=-3 * 360,   # degrees
                    stop_action=Motor.STOP_ACTION_HOLD)

            else:
                self.speaker.play(wav_file='/home/robot/sound/Down.wav').wait()

                self.shooting_motor.run_to_rel_pos(
                    speed_sp=1000,   # degrees per second
                    position_sp=3 * 360,   # degrees
                    stop_action=Motor.STOP_ACTION_HOLD)

            while self.touch_sensor.is_pressed:
                pass

    def shoot_whenever_touched(self):
        while True:
            self.shoot_when_touched()


    def main(self):
        self.screen.image.paste(im=Image.open('/home/robot/image/Target.bmp'))
        self.screen.update()

        Process(target=self.keep_detecting_objects_by_ir_sensor,
                daemon=True).start()

        Process(target=self.shoot_whenever_touched,
                daemon=True).start()

        super().main()   # RemoteControlledTank.main()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()