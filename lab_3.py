from collections import Container
from collections import Hashable
from collections import Iterable
from collections import Sized
from collections import Callable
from collections import Sequence
from collections import MutableSequence
from collections import Set
from collections import MutableSet
from collections import Mapping
from collections import MutableMapping


def type_info(value):
    s = " no ABC-class"
    if (isinstance(value, Container)):
        s = " Container"
    if (isinstance(value, Hashable)):
        s = " Hashable"
    if (isinstance(value, Iterable)):
        s = " Iterable"
    if (isinstance(value, Sized)):
        s = " Sized"
    if (isinstance(value, Callable)):
        s = " Callable"
    if (isinstance(value, Sequence)):
        s = " Sequence"
    if (isinstance(value, MutableSequence)):
        s = " MutableSequence"
    if (isinstance(value, Set)):
        s = " Set"
    if (isinstance(value, MutableSet)):
        s = " MutableSet"
    if (isinstance(value, Mapping)):
        s = " Mapping"
    if (isinstance(value, MutableMapping)):
        s = " MutableMapping"

    print(str(value) + "\t" + str(type(value)) + "\t" + s)


tint = int(12)
tfloat = float(12.5)
tbool = bool(True)
tstr = "string"
tlist = ["a", "b"]

a_list = [tint, tfloat, tbool, tstr, tlist]

for pa in a_list:
    type_info(pa)
