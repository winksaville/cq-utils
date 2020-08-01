import cadquery as cq  # type: ignore
import sys

from __main__ import self
from logbook import info as log

show_object = self.components["object_tree"].addObject

box = cq.Workplane("XY").box(1, 2, 3)
#show_object(box)
log(f"z: box={box}")

sphere = cq.Workplane("XY").sphere(1)
show_object(sphere)
log(f"z: sphere={sphere}")
