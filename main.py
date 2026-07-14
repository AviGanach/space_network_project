from space_network_lib import SpaceNetwork, Packet
from satellite import Satellite

nt = SpaceNetwork()

s1 = Satellite('Sat1', 100)
s2 = Satellite('Sat2', 200)

p = Packet("Hello Avi",s1, s2)

nt.send(p)