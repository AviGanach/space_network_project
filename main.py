from space_network_lib import SpaceNetwork, Packet, TemporalInterferenceError, DataCorruptedError, LinkTerminatedError, \
    OutOfRangeError, BrokenConnectionError
from satellite import Satellite
import time

def transmission_attempt(packet: Packet):
    nt = SpaceNetwork(3)
    while True:
        try:
            nt.send(p)
            print("Success: The message has been sent")
            break
        except TemporalInterferenceError:
            print("TemporalInterferenceError wait 2 minute")
            time.sleep(2)
        except DataCorruptedError:
            print("Data retrying ,corrupted...")
        except LinkTerminatedError:
            raise BrokenConnectionError("Link lost")
        except OutOfRangeError:
            raise BrokenConnectionError("Target out of range")



s1 = Satellite('Sat1', 100)
s2 = Satellite('Sat2', 5000)

p = Packet("Hello Avi",s1, s2)

try:
    transmission_attempt(p)
except BrokenConnectionError:
    print("Transmission failed")