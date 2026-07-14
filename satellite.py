from space_network_lib import SpaceEntity, Packet


class Satellite(SpaceEntity):
    def __init__(self, name: str, distance_from_earth: float):
        super().__init__(name, distance_from_earth)

    def receive_signal(self, packet: Packet):
        print(f'{self.name} received: {packet}')
