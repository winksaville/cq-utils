import cadquery as cq  # type: ignore

import sys
if "cq_editor" in sys.modules:
    print("x: cq_editor availablei")
    from logbook import info as log
    from __main__ import show_object
else:
    print("x: from utils import log, show_object")
    from utils import log, show_object

print(f"s: {globals().keys()}")

def sphere(radius: float) -> cq.Workplane:
    log(f"s: radius={radius}")
    s = cq.Workplane("XY").sphere(radius)
    show_object(s)
    return s
