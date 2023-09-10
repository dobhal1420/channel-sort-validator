from enum import Enum as PyEnum


class DeviceType(str, PyEnum):
    capri = "Capri"
    marigold = "Marigold"
    shine = "Shine"
    datura = "Datura"
    vale = "Vale"
