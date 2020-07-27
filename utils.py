import cadquery as cq  # type: ignore

def show_object(o: object):
    if o is None:
        log("utils.show_object: o=None")
    elif isinstance(o, cq.Shape):
        log(f"utils.show_object: o.val().isValid()={o.val().isValid()}")
    else:
        log(f"utils.show_object: vars={vars(o)}")

def log(*args):
    print(*args)
