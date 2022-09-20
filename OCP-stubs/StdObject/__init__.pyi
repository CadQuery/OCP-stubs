import OCP.StdObject
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopLoc
import OCP.gp
import OCP.TopoDS
import OCP.StdObjMgt
__all__  = [
"StdObject_Location",
"StdObject_Shape",
"write"
]
class StdObject_Location():
    """
    None
    """
    def PChildren(self,theChildren : Any) -> None: 
        """
        Gets persistent child objects
        """
    @staticmethod
    def Translate_s(theLoc : OCP.TopLoc.TopLoc_Location,theMap : Any) -> StdObject_Location: 
        """
        Creates a persistent wrapper object for a location
        """
    def __init__(self) -> None: ...
    pass
class StdObject_Shape():
    """
    None
    """
    def Import(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Import transient object from the persistent data.
        """
    def PChildren(self,theChildren : Any) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
@overload
def write(theWriteData : OCP.StdObjMgt.StdObjMgt_WriteData,theAx : OCP.gp.gp_Ax2d) -> OCP.StdObjMgt.StdObjMgt_WriteData:
    """
    None

    None
    """
@overload
def write(theWriteData : OCP.StdObjMgt.StdObjMgt_WriteData,theAx : OCP.gp.gp_Ax1) -> OCP.StdObjMgt.StdObjMgt_WriteData:
    pass
