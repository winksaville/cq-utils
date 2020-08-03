import cadquery as cq  # type: ignore

from s import sphere
from utils import log, show_object

print("y:+")

print("y: before box(1,2,3)")
box = cq.Workplane("XY").box(1, 2, 3)
print("y: after box(1,2,3)")

print("y: before show_object(box)")
show_object(box)
print("y: after  show_object(box)")

print("y: before sphere")
sphere = sphere(1)
print("y: after sphere")

print("y:-")
