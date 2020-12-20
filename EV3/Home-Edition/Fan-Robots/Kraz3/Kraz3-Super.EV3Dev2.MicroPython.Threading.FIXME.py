#!/usr/bin/env micropython


from threading import Thread

from kraz3_ev3dev2 import Kraz3


KRAZ3 = Kraz3()

Thread(target=KRAZ3.kungfu_manoeuvre_whenever_touched_or_remote_controlled) \
    .start()

Thread(target=KRAZ3.react_to_color).start()

KRAZ3.keep_driving_by_ir_beacon()

# FIXME: ValueError: invalid syntax for integer with base 10: ''
# when multiple threads access the same Infrared Sensor