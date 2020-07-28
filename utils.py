import sys

import cadquery as cq  # type: ignore

if "cq_editor" in sys.modules:
    from __main__ import self as _cq_editor
    from logbook import info as _cq_log

    def show_object(o: object):
        _cq_editor.components["object_tree"].addObject(o)

    def log(*args):
        _cq_log(*args)


else:

    def show_object(o: object):
        if o is None:
            log("o=None")
        elif isinstance(o, cq.Workplane):
            for i, thing in enumerate(o.objects):
                log(f"{i}: valid={o.val().isValid()} {vars(thing)}")
        else:
            log(vars(o))

    def log(*args):
        print(*args)
