#!/usr/bin/env micropython


from dinor3x_ev3dev2 import Dinor3x


DINOR3X = Dinor3x()


while True:
    # recalibrate legs every 5 seconds so that the legs don't get too tired
    DINOR3X.calibrate_legs()

    DINOR3X.steer_driver.on_for_seconds(
        steering=0,
        speed=-40,
        seconds=5,
        brake=True,
        block=True)

    # TODO: terminate by Brick buttons
