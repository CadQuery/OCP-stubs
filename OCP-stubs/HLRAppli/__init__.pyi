import OCP.HLRAppli
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.HLRBRep
import OCP.TopoDS
__all__  = [
"HLRAppli_ReflectLines"
]
class HLRAppli_ReflectLines():
    """
    This class builds reflect lines on a shape according to the axes of view defined by user. Reflect lines are represented by edges in 3d.
    """
    def GetCompoundOf3dEdges(self,type : OCP.HLRBRep.HLRBRep_TypeOfResultingEdge,visible : bool,In3d : bool) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns resulting compound of lines of specified type and visibility represented by edges in 3d or 2d
        """
    def GetResult(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns resulting compound of reflect lines represented by edges in 3d
        """
    def Perform(self) -> None: 
        """
        None
        """
    def SetAxes(self,Nx : float,Ny : float,Nz : float,XAt : float,YAt : float,ZAt : float,XUp : float,YUp : float,ZUp : float) -> None: 
        """
        Sets the normal to the plane of visualisation, the coordinates of the view point and the coordinates of the vertical direction vector.
        """
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
