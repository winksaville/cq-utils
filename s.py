import cadquery as cq  # type: ignore

from utils import log, show_object


def sphere(radius: float) -> cq.Workplane:
    print(f"s: sphere({radius}):+")
    s = cq.Workplane("XY").sphere(radius)
    show_object(s)
    print(f"s: sphere({radius}):-")
    return s
