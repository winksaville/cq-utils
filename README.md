# CQ utils

An attempt to create a utility module which allows a python
application/module to be used with straight python or cq-editor.

Adam suggested "Another option" [here](https://groups.google.com/g/cadquery/c/ofvIsCJJK5M/m/iIj4Luk1CgAJ)
that worked perfectly.

By adding the following code at the beginning of each file:
```
import cadquery as cq  # type: ignore

import sys
if "cq_editor" in sys.modules:
    from logbook import info as log
    from __main__ import show_object
else:
    from utils import log, show_object
```
You can use `log` and `show_object` in your code and exuecute
it with either python or cq-editor. The only problem is, he said:

 "But it is relying on some side effects in CQ-editor that I
 intend to get rid of sooner or later."

So this obviously isn't a long term solution.