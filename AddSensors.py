# -----------------------------------------------------------------------------
# Copyright (c) 2015 Ralph Hempel <rhempel@hempeldesigngroup.com>
# Copyright (c) 2015 Anton Vanhoucke <antonvh@gmail.com>
# Copyright (c) 2015 Denis Demidov <dennis.demidov@gmail.com>
# Copyright (c) 2015 Eric Pascual <eric@pobot.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----------------------------------------------------------------------------

# Addition of sensors by Bichon (BrickStory)

import sys

if sys.version_info < (3,4):
    raise SystemError('Must be using Python 3.4 or higher')

import time
from ev3dev2.sensor import Sensor

class AngleSensor(Sensor):
    """
     HiTechnic Angle sensor.
    """

    SYSTEM_CLASS_NAME = Sensor.SYSTEM_CLASS_NAME
    SYSTEM_DEVICE_NAME_CONVENTION = Sensor.SYSTEM_DEVICE_NAME_CONVENTION

    #: Angle renvoyé.
    MODE_ANGLE = 'ANGLE'

    #: Angle accumulé.
    MODE_ANGLE_ACC = 'ANGLE-ACC'

    #: vitesse angulaire.
    MODE_SPEED = 'SPEED'

    MODES = (
        MODE_ANGLE,
        MODE_ANGLE_ACC,
        MODE_SPEED,
    )

    def __init__(self, address=None, name_pattern=SYSTEM_DEVICE_NAME_CONVENTION, name_exact=False, **kwargs):
        super(AngleSensor, self).__init__(address, name_pattern, name_exact, driver_name='ht-nxt-angle', **kwargs)

    @property
    def angle(self):
        """
        Measurement of the angle detected by the sensor,
        in degree.

        The sensor will continue to take measurements so
        they are available for future reads.

        """
        self._ensure_mode(self.MODE_US_DIST_CM)
        return self.value(0) * self._scale('US_DIST_CM')

    @property
    def distance_centimeters_ping(self):
        """
        Measurement of the distance detected by the sensor,
        in centimeters.

        The sensor will take a single measurement then stop
        broadcasting.

        If you use this property too frequently (e.g. every
        100msec), the sensor will sometimes lock up and writing
        to the mode attribute will return an error. A delay of
        250msec between each usage seems sufficient to keep the
        sensor from locking up.
        """
        # This mode is special; setting the mode causes the sensor to send out
        # a "ping", but the mode isn't actually changed.
        self.mode = self.MODE_US_SI_CM
        return self.value(0)

    @property
    def distance_centimeters(self):
        """
        Measurement of the distance detected by the sensor,
        in centimeters.

        Equivalent to :meth:`UltrasonicSensor.distance_centimeters_continuous`.
        """
        return self.distance_centimeters_continuous

    @property
    def distance_inches_continuous(self):
        """
        Measurement of the distance detected by the sensor,
        in inches.

        The sensor will continue to take measurements so
        they are available for future reads.

        Prefer using the equivalent :meth:`UltrasonicSensor.distance_inches` property.
        """
        self._ensure_mode(self.MODE_US_DIST_IN)
        return self.value(0) * self._scale('US_DIST_IN')

    @property
    def distance_inches_ping(self):
        """
        Measurement of the distance detected by the sensor,
        in inches.

        The sensor will take a single measurement then stop
        broadcasting.

        If you use this property too frequently (e.g. every
        100msec), the sensor will sometimes lock up and writing
        to the mode attribute will return an error. A delay of
        250msec between each usage seems sufficient to keep the
        sensor from locking up.
        """
        # This mode is special; setting the mode causes the sensor to send out
        # a "ping", but the mode isn't actually changed.
        self.mode = self.MODE_US_SI_IN
        return self.value(0) * self._scale('US_DIST_IN')

    @property
    def distance_inches(self):
        """
        Measurement of the distance detected by the sensor,
        in inches.

        Equivalent to :meth:`UltrasonicSensor.distance_inches_continuous`.
        """
        return self.distance_inches_continuous

    @property
    def other_sensor_present(self):
        """
        Boolean indicating whether another ultrasonic sensor could
        be heard nearby.
        """
        self._ensure_mode(self.MODE_US_LISTEN)
        return bool(self.value(0))
