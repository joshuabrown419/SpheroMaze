from time import sleep
from typing import Dict
import math

from pysphero.core import Sphero
from pysphero.device_api.sensor import Quaternion, Velocity
from pysphero.bluetooth.bluepy_adapter import BluepyAdapter


def notify_callback(data: Dict):
    vel = math.sqrt(data.get(Velocity.x)**2 + data.get(Velocity.y)**2)
    print(vel)


def main():
    mac_address = "EA:44:16:06:73:13"
    with Sphero(mac_address=mac_address) as sphero:
        # sphero.ble_adapter.close()
        # sphero.ble_adapter = BluepyAdapter(mac_address)
        sphero.power.wake()

        sphero.sensor.set_notify(notify_callback, Velocity, Quaternion)

        delay = False
        heading = 0

        while True:
            # vel = globals()["vel"]
            #
            # if vel < 1 and not delay:
            #     heading += 90
            #     if heading >= 360:
            #         heading -= 360

            sphero.driving.drive_with_heading(50, heading)

            sleep(1)


if __name__ == "__main__":
    main()
