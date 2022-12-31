import OCP.Sweep
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
__all__  = [
"Sweep_NumShape",
"Sweep_NumShapeIterator",
"Sweep_NumShapeTool"
]
class Sweep_NumShape():
    """
    Gives a simple indexed representation of a Directing Edge topology.
    """
    def BegInfinite(self) -> bool: 
        """
        None

        None
        """
    def Closed(self) -> bool: 
        """
        None

        None
        """
    def EndInfinite(self) -> bool: 
        """
        None

        None
        """
    def Index(self) -> int: 
        """
        None

        None
        """
    def Init(self,Index : int,Type : OCP.TopAbs.TopAbs_ShapeEnum,Closed : bool=False,BegInf : bool=False,EndInf : bool=False) -> None: 
        """
        Reinitialize a simple indexed edge.
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Type(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        None

        None
        """
    @overload
    def __init__(self,Index : int,Type : OCP.TopAbs.TopAbs_ShapeEnum,Closed : bool=False,BegInf : bool=False,EndInf : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Sweep_NumShapeIterator():
    """
    This class provides iteration services required by the Swept Primitives for a Directing NumShape Line.
    """
    def Init(self,aShape : Sweep_NumShape) -> None: 
        """
        Reset the NumShapeIterator on sub-shapes of <aShape>.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current sub-shape.

        Returns True if there is a current sub-shape.
        """
    def Next(self) -> None: 
        """
        Moves to the next sub-shape.
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the orientation of the current sub-shape.

        Returns the orientation of the current sub-shape.
        """
    def Value(self) -> Sweep_NumShape: 
        """
        Returns the current sub-shape.

        Returns the current sub-shape.
        """
    def __init__(self) -> None: ...
    pass
class Sweep_NumShapeTool():
    """
    This class provides the indexation and type analysis services required by the NumShape Directing Shapes of Swept Primitives.
    """
    def FirstVertex(self) -> Sweep_NumShape: 
        """
        Returns the first vertex.
        """
    def HasFirstVertex(self) -> bool: 
        """
        Returns true if there is a First Vertex in the Shape.
        """
    def HasLastVertex(self) -> bool: 
        """
        Returns true if there is a Last Vertex in the Shape.
        """
    def Index(self,aShape : Sweep_NumShape) -> int: 
        """
        Returns the index of <aShape>.
        """
    def LastVertex(self) -> Sweep_NumShape: 
        """
        Returns the last vertex.
        """
    def NbShapes(self) -> int: 
        """
        Returns the number of subshapes in the shape.
        """
    def Orientation(self,aShape : Sweep_NumShape) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the orientation of <aShape>.
        """
    def Shape(self,anIndex : int) -> Sweep_NumShape: 
        """
        Returns the Shape at index anIndex
        """
    def Type(self,aShape : Sweep_NumShape) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the type of <aShape>.
        """
    def __init__(self,aShape : Sweep_NumShape) -> None: ...
    pass
