import OCP.BRepProj
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.TopoDS
__all__  = [
"BRepProj_Projection"
]
class BRepProj_Projection():
    """
    The Projection class provides conical and cylindrical projections of Edge or Wire on a Shape from TopoDS. The result will be a Edge or Wire from TopoDS.
    """
    def Current(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the current result wire.

        Returns the current result wire.
        """
    def Init(self) -> None: 
        """
        Resets the iterator by resulting wires.

        Resets the iterator by resulting wires.
        """
    def IsDone(self) -> bool: 
        """
        returns False if the section failed

        returns False if the section failed
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current result wire

        Returns True if there is a current result wire
        """
    def Next(self) -> None: 
        """
        Move to the next result wire.

        Move to the next result wire.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Compound: 
        """
        Returns the complete result as compound of wires.

        Returns the complete result as compound of wires.
        """
    @overload
    def __init__(self,Wire : OCP.TopoDS.TopoDS_Shape,Shape : OCP.TopoDS.TopoDS_Shape,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Wire : OCP.TopoDS.TopoDS_Shape,Shape : OCP.TopoDS.TopoDS_Shape,D : OCP.gp.gp_Dir) -> None: ...
    pass
