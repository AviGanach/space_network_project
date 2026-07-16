from space_network_lib import SpaceNetwork, Packet, RelayPacket, Satellite, BrokenConnectionError


s1 = Satellite('Sat1', 100)
s2 = Satellite('Sat2', 200)
earth = Satellite('Earth', 0)

final_p = Packet("from Hello Earth!!",s1, s2)
sat_to_earth_p = RelayPacket(final_p, earth, s1)

try:
    SpaceNetwork.attempt_transmission(sat_to_earth_p)
except BrokenConnectionError:
    print("Transmission failed")