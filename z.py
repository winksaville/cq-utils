import sys
import cadquery as cq  # type: ignore

if "cq_editor" in sys.modules:
    from __main__ import self
    show_object = self.components['object_tree'].addObject
else:
    def show_object(o):
        print(f"{vars(o)}")

box = cq.Workplane("XY").box(1, 2, 3)
#show_object(box)

sphere = cq.Workplane("XY").sphere(1)
show_object(sphere)
