import cadquery as cq  # type: ignore

from utils import log, show_object


def sphere(radius: float) -> cq.Workplane:
    log(f"s: radius={radius}")
    s = cq.Workplane("XY").sphere(radius)
    show_object(s)
    return s
