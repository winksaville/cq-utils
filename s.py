import cadquery as cq  # type: ignore

import sys
#if "cq_editor" not in sys.modules:
if "cq_editor" not in globals().keys():
    print("s: importing log and show_object")
    from utils import log, show_object
else:
    print("s: NOT importing log and show_object")

print(f"s: {globals().keys()}")

def sphere(radius: float) -> cq.Workplane:
    log(f"s: radius={radius}")
    s = cq.Workplane("XY").sphere(radius)
    show_object(s)
    return s
