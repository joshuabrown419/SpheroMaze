from time import sleep
from typing import Dict
import math

from pysphero.core import Sphero
from pysphero.bluetooth.bluepy_adapter import BluepyAdapter

def main():
    mac_address = "EA:44:16:06:73:13"
    with Sphero(mac_address=mac_address) as sphero:
        # sphero.ble_adapter.close()
        # sphero.ble_adapter = BluepyAdapter(mac_address)
        sphero.power.wake()
        sleep(1)
        sphero.power.enter_soft_sleep()


if __name__ == "__main__":
    main()
