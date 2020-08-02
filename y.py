import cadquery as cq  # type: ignore

from s import sphere
from utils import log, show_object

box = cq.Workplane("XY").box(1, 2, 3)
#show_object(box)
log(f"y: box={box}")

sphere = sphere(1)
log(f"y: sphere={sphere}")
