import cadquery as cq  # type: ignore

from utils import log, show_object

box = cq.Workplane("XY").box(1, 2, 3)
show_object(box)
log(f"x: box={box}")
