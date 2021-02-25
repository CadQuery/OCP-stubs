import OCP.TopExp
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.TopoDS
import OCP.TopAbs
__all__  = [
"TopExp",
"TopExp_Explorer"
]
class TopExp():
    """
    This package provides basic tools to explore the topological data structures.
    """
    @staticmethod
    def CommonVertex_s(E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,V : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        Finds the vertex <V> common to the two edges <E1,E2>, returns True if this vertex exists.
        """
    @staticmethod
    def FirstVertex_s(E : OCP.TopoDS.TopoDS_Edge,CumOri : bool=False) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex of orientation FORWARD in E. If there is none returns a Null Shape. CumOri = True : taking account the edge orientation
        """
    @staticmethod
    def LastVertex_s(E : OCP.TopoDS.TopoDS_Edge,CumOri : bool=False) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex of orientation REVERSED in E. If there is none returns a Null Shape. CumOri = True : taking account the edge orientation
        """
    @staticmethod
    def MapShapesAndAncestors_s(S : OCP.TopoDS.TopoDS_Shape,TS : OCP.TopAbs.TopAbs_ShapeEnum,TA : OCP.TopAbs.TopAbs_ShapeEnum,M : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape) -> None: 
        """
        Stores in the map <M> all the subshape of <S> of type <TS> for each one append to the list all the ancestors of type <TA>. For example map all the edges and bind the list of faces. Warning: The map is not cleared at first.
        """
    @staticmethod
    def MapShapesAndUniqueAncestors_s(S : OCP.TopoDS.TopoDS_Shape,TS : OCP.TopAbs.TopAbs_ShapeEnum,TA : OCP.TopAbs.TopAbs_ShapeEnum,M : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape,useOrientation : bool=False) -> None: 
        """
        Stores in the map <M> all the subshape of <S> of type <TS> for each one append to the list all unique ancestors of type <TA>. For example map all the edges and bind the list of faces. useOrientation = True : taking account the ancestor orientation Warning: The map is not cleared at first.
        """
    @staticmethod
    @overload
    def MapShapes_s(S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum,M : OCP.TopTools.TopTools_IndexedMapOfShape) -> None: 
        """
        Tool to explore a topological data structure. Stores in the map <M> all the sub-shapes of <S> of type <T>.

        Stores in the map <M> all the sub-shapes of <S>.

        Stores in the map <M> all the sub-shapes of <S>.
        """
    @staticmethod
    @overload
    def MapShapes_s(S : OCP.TopoDS.TopoDS_Shape,M : OCP.TopTools.TopTools_MapOfShape) -> None: ...
    @staticmethod
    @overload
    def MapShapes_s(S : OCP.TopoDS.TopoDS_Shape,M : OCP.TopTools.TopTools_IndexedMapOfShape) -> None: ...
    @staticmethod
    @overload
    def Vertices_s(W : OCP.TopoDS.TopoDS_Wire,Vfirst : OCP.TopoDS.TopoDS_Vertex,Vlast : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Returns in Vfirst, Vlast the FORWARD and REVERSED vertices of the edge <E>. May be null shapes. CumOri = True : taking account the edge orientation

        Returns in Vfirst, Vlast the first and last vertices of the open wire <W>. May be null shapes. if <W> is closed Vfirst and Vlast are a same vertex on <W>. if <W> is no manifold. VFirst and VLast are null shapes.
        """
    @staticmethod
    @overload
    def Vertices_s(E : OCP.TopoDS.TopoDS_Edge,Vfirst : OCP.TopoDS.TopoDS_Vertex,Vlast : OCP.TopoDS.TopoDS_Vertex,CumOri : bool=False) -> None: ...
    def __init__(self) -> None: ...
    pass
class TopExp_Explorer():
    """
    An Explorer is a Tool to visit a Topological Data Structure form the TopoDS package.
    """
    def Clear(self) -> None: 
        """
        Clears the content of the explorer. It will return False on More().

        Clears the content of the explorer. It will return False on More().
        """
    def Current(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the current shape in the exploration. Exceptions Standard_NoSuchObject if this explorer has no more shapes to explore.
        """
    def Depth(self) -> int: 
        """
        Returns the current depth of the exploration. 0 is the shape to explore itself.

        Returns the current depth of the exploration. 0 is the shape to explore itself.
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape,ToFind : OCP.TopAbs.TopAbs_ShapeEnum,ToAvoid : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: 
        """
        Resets this explorer on the shape S. It is initialized to search the shape S, for shapes of type ToFind, that are not part of a shape ToAvoid. If the shape ToAvoid is equal to TopAbs_SHAPE, or if it is the same as, or less complex than, the shape ToFind it has no effect on the search.
        """
    def More(self) -> bool: 
        """
        Returns True if there are more shapes in the exploration.

        Returns True if there are more shapes in the exploration.
        """
    def Next(self) -> None: 
        """
        Moves to the next Shape in the exploration. Exceptions Standard_NoMoreObject if there are no more shapes to explore.
        """
    def ReInit(self) -> None: 
        """
        Reinitialize the exploration with the original arguments.
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the current shape in the exploration. Exceptions Standard_NoSuchObject if this explorer has no more shapes to explore.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,ToFind : OCP.TopAbs.TopAbs_ShapeEnum,ToAvoid : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
