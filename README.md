# CQ utils

An attempt to create a utility module which allows a python
application/module to be used with straight python or cq-editor.

Adam has suggested "Another option" [here](https://groups.google.com/g/cadquery/c/ofvIsCJJK5M/m/iIj4Luk1CgAJ)
that worked perfectly, but said:
 "But it is relying on some side effects in CQ-editor that I
 intend to get rid of sooner or later."

Then his next [post](https://groups.google.com/g/cadquery/c/ofvIsCJJK5M/m/SD7wnY45CgAJ)
suggests that instead of `from __main__ import show_object` using
`self.component['object_tree'].addObject` would be preferred.

I then figured out that only `utils.py` needs to have
the magic imports and the other files simply use
`from utils import log, show_object`:

So `utils.py` is now:
```
(cq-dev) wink@3900x:~/prgs/CadQuery/projects/utils (master)
$ cat -n utils.py 
     1	import sys
     2	
     3	import cadquery as cq  # type: ignore
     4	
     5	if "cq_editor" in sys.modules:
     6	    from __main__ import self as _cq_editor
     7	    from logbook import info as _cq_log
     8	
     9	    def show_object(o: object):
    10	        _cq_editor.components["object_tree"].addObject(o)
    11	
    12	    def log(*args):
    13	        _cq_log(*args)
    14	
    15	
    16	else:
    17	
    18	    def show_object(o: object):
    19	        if o is None:
    20	            log("o=None")
    21	        elif isinstance(o, cq.Workplane):
    22	            for i, thing in enumerate(o.objects):
    23	                log(f"{i}: valid={o.val().isValid()} {vars(thing)}")
    24	        else:
    25	            log(vars(o))
    26	
    27	    def log(*args):
    28	        print(*args)```
```
x.py is:
```
(cq-dev) wink@3900x:~/prgs/CadQuery/projects/utils (master)
$ cat -n x.py
     1	import cadquery as cq  # type: ignore
     2	
     3	from utils import log, show_object
     4	
     5	box = cq.Workplane("XY").box(1, 2, 3)
     6	show_object(box)
     7	log(f"x: box={box}")
```
y.py is:
```
(cq-dev) wink@3900x:~/prgs/CadQuery/projects/utils (master)
$ cat -n y.py
     1	import cadquery as cq  # type: ignore
     2	
     3	from s import sphere
     4	from utils import log, show_object
     5	
     6	box = cq.Workplane("XY").box(1, 2, 3)
     7	show_object(box)
     8	log(f"y: box={box}")
     9	
    10	sphere = sphere(1)
    11	log(f"y: sphere={sphere}")
```
s.py is:
```
(cq-dev) wink@3900x:~/prgs/CadQuery/projects/utils (master)
$ cat -n s.py
     1	import cadquery as cq  # type: ignore
     2	
     3	from utils import log, show_object
     4	
     5	
     6	def sphere(radius: float) -> cq.Workplane:
     7	    log(f"s: radius={radius}")
     8	    s = cq.Workplane("XY").sphere(radius)
     9	    show_object(s)
    10	    return s
```
