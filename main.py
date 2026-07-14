from space_network_lib import SpaceNetwork, Packet, TemporalInterferenceError, DataCorruptedError
from satellite import Satellite
import time

def transmission_attempt(packet: Packet):
    nt = SpaceNetwork(2)
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


s1 = Satellite('Sat1', 100)
s2 = Satellite('Sat2', 200)

p = Packet("Hello Avi",s1, s2)

transmission_attempt(p)