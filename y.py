import cadquery as cq  # type: ignore

import sys
if "cq_editor" not in sys.modules:
    print("x: importing log and show_object")
    from utils import log, show_object
else:
    print("x: NOT importing log and show_object")

log(globals().keys())

box = cq.Workplane("XY").box(1,2,3)
show_object(box)
log(f"y: box={box}")

from s import sphere

sphere = sphere(1)
log(f"y: sphere={sphere}")
