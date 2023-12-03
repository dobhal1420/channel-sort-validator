from enum import Enum as PyEnum


class Source(str, PyEnum):
    source1 = "TYPE_DVB_S2"
    source2 = "TYPE_DVB_T2"
    source3 = "TYPE_DVB_C"
