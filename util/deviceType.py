from enum import Enum as PyEnum


class DeviceType(str, PyEnum):
    phone = "phone"
    tablet = "tablet"
    laptop = "laptop"
