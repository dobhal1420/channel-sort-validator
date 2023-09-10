from enum import Enum as PyEnum


class Source(str, PyEnum):
    source1 = "DVBS"
    source2 = "DVBT"
    source3 = "DVBC"
