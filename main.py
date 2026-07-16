from space_network_lib import SpaceNetwork, Packet, RelayPacket, Satellite, BrokenConnectionError


earth = Satellite('Earth', 0)
s1 = Satellite('Sat1', 100)
s2 = Satellite('Sat2', 200)
s3 = Satellite('Sat3', 300)
s4 = Satellite('Sat4', 400)

final_p = Packet("from Hello Earth!!",s3, s4)
p_sat2_to_sat3 = RelayPacket(final_p, s2, s3)
p_sat1_to_sat2 = RelayPacket(p_sat2_to_sat3, s1, s2)
p_earth_to_sat1 = RelayPacket(p_sat1_to_sat2, earth, s1)

try:
    SpaceNetwork.attempt_transmission(p_earth_to_sat1)
except BrokenConnectionError:
    print("Transmission failed")