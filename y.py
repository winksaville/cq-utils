import cadquery as cq  # type: ignore

import sys
if "cq_editor" in sys.modules:
    print("x: cq_editor availablei")
    from logbook import info as log
    from __main__ import show_object
else:
    print("x: from utils import log, show_object")
    from utils import log, show_object

log(globals().keys())

box = cq.Workplane("XY").box(1,2,3)
show_object(box)
log(f"y: box={box}")

from s import sphere

sphere = sphere(1)
log(f"y: sphere={sphere}")
