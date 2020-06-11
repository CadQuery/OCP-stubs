import OCP.IntImpParGen
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IntRes2d
import OCP.gp
__all__  = [
"IntImpParGen",
"IntImpParGen_ImpTool",
"Determine_Position",
"Determine_Transition",
"NormalizeOnDomain"
]
class IntImpParGen():
    """
    Gives a generic algorithm to intersect Implicit Curves and Bounded Parametric Curves.
    """
    @staticmethod
    def DeterminePosition_s(Pos1 : OCP.IntRes2d.IntRes2d_Position,Dom1 : OCP.IntRes2d.IntRes2d_Domain,P1 : OCP.gp.gp_Pnt2d,Tol : float) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def DetermineTransition_s(Pos1 : OCP.IntRes2d.IntRes2d_Position,Tan1 : OCP.gp.gp_Vec2d,Trans1 : OCP.IntRes2d.IntRes2d_Transition,Pos2 : OCP.IntRes2d.IntRes2d_Position,Tan2 : OCP.gp.gp_Vec2d,Trans2 : OCP.IntRes2d.IntRes2d_Transition,Tol : float) -> bool: 
        """
        Template class for an implicit curve. Math function, instantiated inside the Intersector. Tool used by the package IntCurve and IntImpParGen

        None
        """
    @staticmethod
    @overload
    def DetermineTransition_s(Pos1 : OCP.IntRes2d.IntRes2d_Position,Tan1 : OCP.gp.gp_Vec2d,Norm1 : OCP.gp.gp_Vec2d,Trans1 : OCP.IntRes2d.IntRes2d_Transition,Pos2 : OCP.IntRes2d.IntRes2d_Position,Tan2 : OCP.gp.gp_Vec2d,Norm2 : OCP.gp.gp_Vec2d,Trans2 : OCP.IntRes2d.IntRes2d_Transition,Tol : float) -> None: ...
    @staticmethod
    def NormalizeOnDomain_s(Par1 : float,Dom1 : OCP.IntRes2d.IntRes2d_Domain) -> float: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IntImpParGen_ImpTool():
    """
    Template class for an implicit curve.
    """
    def __init__(self) -> None: ...
    pass
def Determine_Position(arg0 : OCP.IntRes2d.IntRes2d_Position,arg1 : OCP.IntRes2d.IntRes2d_Domain,arg2 : OCP.gp.gp_Pnt2d,arg3 : float) -> None:
    """
    None
    """
def Determine_Transition(Pos1 : OCP.IntRes2d.IntRes2d_Position,Tan1 : OCP.gp.gp_Vec2d,Norm1 : OCP.gp.gp_Vec2d,Trans1 : OCP.IntRes2d.IntRes2d_Transition,Pos2 : OCP.IntRes2d.IntRes2d_Position,Tan2 : OCP.gp.gp_Vec2d,Norm2 : OCP.gp.gp_Vec2d,Trans2 : OCP.IntRes2d.IntRes2d_Transition,ToleranceAng : float) -> None:
    """
    None
    """
def NormalizeOnDomain(arg0 : float,arg1 : OCP.IntRes2d.IntRes2d_Domain) -> float:
    """
    None
    """
