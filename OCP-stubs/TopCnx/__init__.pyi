import OCP.TopCnx
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.TopAbs
__all__  = [
"TopCnx_EdgeFaceTransition"
]
class TopCnx_EdgeFaceTransition():
    """
    TheEdgeFaceTransition is an algorithm to compute the cumulated transition for interferences on an edge.
    """
    def AddInterference(self,Tole : float,Tang : OCP.gp.gp_Dir,Norm : OCP.gp.gp_Dir,Curv : float,Or : OCP.TopAbs.TopAbs_Orientation,Tr : OCP.TopAbs.TopAbs_Orientation,BTr : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Add a curve element to the boundary. Or is the orientation of the interference on the boundary curve. Tr is the transition of the interference. BTr is the boundary transition of the interference.
        """
    def BoundaryTransition(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the current cumulated BoundaryTransition.
        """
    @overload
    def Reset(self,Tgt : OCP.gp.gp_Dir,Norm : OCP.gp.gp_Dir,Curv : float) -> None: 
        """
        Initialize the algorithm with the local description of the edge.

        Initialize the algorithm with a linear Edge.
        """
    @overload
    def Reset(self,Tgt : OCP.gp.gp_Dir) -> None: ...
    def Transition(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the current cumulated transition.
        """
    def __init__(self) -> None: ...
    pass
