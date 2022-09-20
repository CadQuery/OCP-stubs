import OCP.LocOpe
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.TColgp
import OCP.NCollection
import io
import OCP.gp
import OCP.TopAbs
import OCP.Geom
import OCP.Standard
import OCP.TopoDS
import OCP.TColGeom
__all__  = [
"LocOpe",
"LocOpe_BuildShape",
"LocOpe_BuildWires",
"LocOpe_CSIntersector",
"LocOpe_CurveShapeIntersector",
"LocOpe_DPrism",
"LocOpe_DataMapOfShapePnt",
"LocOpe_FindEdges",
"LocOpe_FindEdgesInFace",
"LocOpe_GeneratedShape",
"LocOpe_Generator",
"LocOpe_GluedShape",
"LocOpe_Gluer",
"LocOpe_LinearForm",
"LocOpe_Operation",
"LocOpe_Pipe",
"LocOpe_PntFace",
"LocOpe_Prism",
"LocOpe_Revol",
"LocOpe_RevolutionForm",
"LocOpe_SequenceOfCirc",
"LocOpe_SequenceOfLin",
"LocOpe_SequenceOfPntFace",
"LocOpe_SplitDrafts",
"LocOpe_SplitShape",
"LocOpe_Spliter",
"LocOpe_WiresOnShape",
"LocOpe_CUT",
"LocOpe_FUSE",
"LocOpe_INVALID"
]
class LocOpe():
    """
    Provides tools to implement local topological operations on a shape.
    """
    @staticmethod
    @overload
    def Closed_s(W : OCP.TopoDS.TopoDS_Wire,OnF : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns Standard_True when the wire <W> is closed on the face <OnF>.

        Returns Standard_True when the edge <E> is closed on the face <OnF>.
        """
    @staticmethod
    @overload
    def Closed_s(E : OCP.TopoDS.TopoDS_Edge,OnF : OCP.TopoDS.TopoDS_Face) -> bool: ...
    @staticmethod
    def SampleEdges_s(S : OCP.TopoDS.TopoDS_Shape,Pt : OCP.TColgp.TColgp_SequenceOfPnt) -> None: 
        """
        None
        """
    @staticmethod
    def TgtFaces_s(E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns Standard_True when the faces are tangent
        """
    def __init__(self) -> None: ...
    pass
class LocOpe_BuildShape():
    """
    None
    """
    def Perform(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Builds shape(s) from the list <L>. Uses only the faces of <L>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    @overload
    def __init__(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class LocOpe_BuildWires():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Perform(self,Ledges : OCP.TopTools.TopTools_ListOfShape,PW : LocOpe_WiresOnShape) -> None: 
        """
        None
        """
    def Result(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Ledges : OCP.TopTools.TopTools_ListOfShape,PW : LocOpe_WiresOnShape) -> None: ...
    pass
class LocOpe_CSIntersector():
    """
    This class provides the intersection between a set of axis or a circle and the faces of a shape. The intersection points are sorted in increasing parameter along each axis or circle.
    """
    def Destroy(self) -> None: 
        """
        None
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Performs the intersection between <Ax1 and <S>.
        """
    def IsDone(self) -> bool: 
        """
        Returns <Standard_True> if the intersection has been done.

        Returns <Standard_True> if the intersection has been done.
        """
    @overload
    def LocalizeAfter(self,I : int,From : float,Tol : float,Or : OCP.TopAbs.TopAbs_Orientation,IndFrom : int,IndTo : int) -> bool: 
        """
        On the element of range <I>, searches the first intersection point located after the parameter <From>, which orientation is not TopAbs_EXTERNAL. If found, returns <Standard_True>. <Or> contains the orientation of the point, <IndFrom> and <IndTo> represents the interval of index in the sequence of intersection point corresponding to the point. (IndFrom <= IndTo). <Tol> is used to determine if 2 parameters are equal.

        On the element of range <I>, searches the first intersection point located after the index <FromInd> ( >= FromInd + 1), which orientation is not TopAbs_EXTERNAL. If found, returns <Standard_True>. <Or> contains the orientation of the point, <IndFrom> and <IndTo> represents the interval of index in the sequence of intersection point corresponding to the point. (IndFrom <= IndTo). <Tol> is used to determine if 2 parameters are equal.
        """
    @overload
    def LocalizeAfter(self,I : int,FromInd : int,Tol : float,Or : OCP.TopAbs.TopAbs_Orientation,IndFrom : int,IndTo : int) -> bool: ...
    @overload
    def LocalizeBefore(self,I : int,From : float,Tol : float,Or : OCP.TopAbs.TopAbs_Orientation,IndFrom : int,IndTo : int) -> bool: 
        """
        On the element of range <I>, searches the first intersection point located before the parameter <From>, which orientation is not TopAbs_EXTERNAL. If found, returns <Standard_True>. <Or> contains the orientation of the point, <IndFrom> and <IndTo> represents the interval of index in the sequence of intersection point corresponding to the point (IndFrom <= IndTo). <Tol> is used to determine if 2 parameters are equal.

        On the element of range <I>, searches the first intersection point located before the index <FromInd> ( <= FromInd -1), which orientation is not TopAbs_EXTERNAL. If found, returns <Standard_True>. <Or> contains the orientation of the point, <IndFrom> and <IndTo> represents the interval of index in the sequence of intersection point corresponding to the point (IndFrom <= IndTo). <Tol> is used to determine if 2 parameters are equal.
        """
    @overload
    def LocalizeBefore(self,I : int,FromInd : int,Tol : float,Or : OCP.TopAbs.TopAbs_Orientation,IndFrom : int,IndTo : int) -> bool: ...
    def NbPoints(self,I : int) -> int: 
        """
        Returns the number of intersection point on the element of range <I>.
        """
    @overload
    def Perform(self,Scur : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Perform(self,Scir : LocOpe_SequenceOfCirc) -> None: ...
    @overload
    def Perform(self,Slin : LocOpe_SequenceOfLin) -> None: ...
    def Point(self,I : int,Index : int) -> LocOpe_PntFace: 
        """
        Returns the intersection point of range <Index> on element of range <I>. The points are sorted in increasing order of parameter along the axis.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class LocOpe_CurveShapeIntersector():
    """
    This class provides the intersection between an axis or a circle and the faces of a shape. The intersection points are sorted in increasing parameter along the axis.
    """
    @overload
    def Init(self,Axis : OCP.gp.gp_Ax1,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Performs the intersection between <Ax1 and <S>.

        Performs the intersection between <Ax1 and <S>.
        """
    @overload
    def Init(self,C : OCP.gp.gp_Circ,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns <Standard_True> if the intersection has been done.

        Returns <Standard_True> if the intersection has been done.
        """
    @overload
    def LocalizeAfter(self,FromInd : int,Or : OCP.TopAbs.TopAbs_Orientation,IndFrom : int,IndTo : int) -> bool: 
        """
        Searches the first intersection point located after the parameter <From>, which orientation is not TopAbs_EXTERNAL. If found, returns <Standard_True>. <Or> contains the orientation of the point, <IndFrom> and <IndTo> represents the interval of index in the sequence of intersection point corresponding to the point. (IndFrom <= IndTo).

        Searches the first intersection point located after the index <FromInd> ( >= FromInd + 1), which orientation is not TopAbs_EXTERNAL. If found, returns <Standard_True>. <Or> contains the orientation of the point, <IndFrom> and <IndTo> represents the interval of index in the sequence of intersection point corresponding to the point. (IndFrom <= IndTo).
        """
    @overload
    def LocalizeAfter(self,From : float,Or : OCP.TopAbs.TopAbs_Orientation,IndFrom : int,IndTo : int) -> bool: ...
    @overload
    def LocalizeBefore(self,FromInd : int,Or : OCP.TopAbs.TopAbs_Orientation,IndFrom : int,IndTo : int) -> bool: 
        """
        Searches the first intersection point located before the parameter <From>, which orientation is not TopAbs_EXTERNAL. If found, returns <Standard_True>. <Or> contains the orientation of the point, <IndFrom> and <IndTo> represents the interval of index in the sequence of intersection point corresponding to the point (IndFrom <= IndTo).

        Searches the first intersection point located before the index <FromInd> ( <= FromInd -1), which orientation is not TopAbs_EXTERNAL. If found, returns <Standard_True>. <Or> contains the orientation of the point, <IndFrom> and <IndTo> represents the interval of index in the sequence of intersection point corresponding to the point (IndFrom <= IndTo).
        """
    @overload
    def LocalizeBefore(self,From : float,Or : OCP.TopAbs.TopAbs_Orientation,IndFrom : int,IndTo : int) -> bool: ...
    def NbPoints(self) -> int: 
        """
        Returns the number of intersection point.

        Returns the number of intersection point.
        """
    @overload
    def Point(self,Index : int) -> LocOpe_PntFace: 
        """
        Returns the intersection point of range <Index>. The points are sorted in increasing order of parameter along the axis.

        Returns the intersection point of range <Index>. The points are sorted in increasing order of parameter along the axis.
        """
    @overload
    def Point(self,I : int) -> LocOpe_PntFace: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class LocOpe_DPrism():
    """
    Defines a pipe (near from Pipe from BRepFill), with modifications provided for the Pipe feature.
    """
    def BarycCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def Curves(self,SCurves : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Profile(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shapes(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Spine(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Face,Height : float,Angle : float) -> None: ...
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Face,Height1 : float,Height2 : float,Angle : float) -> None: ...
    pass
class LocOpe_DataMapOfShapePnt(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : LocOpe_DataMapOfShapePnt) -> LocOpe_DataMapOfShapePnt: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.gp.gp_Pnt) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.gp.gp_Pnt: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.gp.gp_Pnt: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : LocOpe_DataMapOfShapePnt) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.gp.gp_Pnt) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.gp.gp_Pnt: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.gp.gp_Pnt: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : LocOpe_DataMapOfShapePnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class LocOpe_FindEdges():
    """
    None
    """
    def EdgeFrom(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    def EdgeTo(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    def InitIterator(self) -> None: 
        """
        None

        None
        """
    def More(self) -> bool: 
        """
        None

        None
        """
    def Next(self) -> None: 
        """
        None

        None
        """
    def Set(self,FFrom : OCP.TopoDS.TopoDS_Shape,FTo : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,FFrom : OCP.TopoDS.TopoDS_Shape,FTo : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class LocOpe_FindEdgesInFace():
    """
    None
    """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    def Init(self) -> None: 
        """
        None

        None
        """
    def More(self) -> bool: 
        """
        None

        None
        """
    def Next(self) -> None: 
        """
        None

        None
        """
    def Set(self,S : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class LocOpe_GeneratedShape(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def Generated(self,V : OCP.TopoDS.TopoDS_Vertex) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge created by the vertex <V>. If none, must return a null shape.

        Returns the face created by the edge <E>. If none, must return a null shape.
        """
    @overload
    def Generated(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Face: ...
    def GeneratingEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def OrientedFaces(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of correctly oriented generated faces.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class LocOpe_Generator():
    """
    None
    """
    def DescendantFace(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the descendant face of <F>. <F> may belong to the original shape or to the "generated" shape. The returned face may be a null shape (when <F> disappears).
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes the algorithm on the shape <S>.

        Initializes the algorithm on the shape <S>.
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def Perform(self,G : LocOpe_GeneratedShape) -> None: 
        """
        None
        """
    def ResultingShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the new shape

        Returns the new shape
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the initial shape

        Returns the initial shape
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class LocOpe_GluedShape(LocOpe_GeneratedShape, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def Generated(self,V : OCP.TopoDS.TopoDS_Vertex) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge created by the vertex <V>. If none, must return a null shape.

        Returns the face created by the edge <E>. If none, must return a null shape.
        """
    @overload
    def Generated(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Face: ...
    def GeneratingEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlueOnFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def OrientedFaces(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of correctly oriented generated faces.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class LocOpe_Gluer():
    """
    None
    """
    def BasisShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    @overload
    def Bind(self,Enew : OCP.TopoDS.TopoDS_Edge,Ebase : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None

        None
        """
    @overload
    def Bind(self,Fnew : OCP.TopoDS.TopoDS_Face,Fbase : OCP.TopoDS.TopoDS_Face) -> None: ...
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Edges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def GluedShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    def Init(self,Sbase : OCP.TopoDS.TopoDS_Shape,Snew : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def OpeType(self) -> LocOpe_Operation: 
        """
        None

        None
        """
    def Perform(self) -> None: 
        """
        None
        """
    def ResultingShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    def TgtEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Sbase : OCP.TopoDS.TopoDS_Shape,Snew : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class LocOpe_LinearForm():
    """
    Defines a linear form (using Prism from BRepSweep) with modifications provided for the LinearForm feature.
    """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def Perform(self,Base : OCP.TopoDS.TopoDS_Shape,V : OCP.gp.gp_Vec,Pnt1 : OCP.gp.gp_Pnt,Pnt2 : OCP.gp.gp_Pnt) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,Base : OCP.TopoDS.TopoDS_Shape,V : OCP.gp.gp_Vec,Vectra : OCP.gp.gp_Vec,Pnt1 : OCP.gp.gp_Pnt,Pnt2 : OCP.gp.gp_Pnt) -> None: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shapes(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    @overload
    def __init__(self,Base : OCP.TopoDS.TopoDS_Shape,V : OCP.gp.gp_Vec,Pnt1 : OCP.gp.gp_Pnt,Pnt2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Base : OCP.TopoDS.TopoDS_Shape,V : OCP.gp.gp_Vec,Vectra : OCP.gp.gp_Vec,Pnt1 : OCP.gp.gp_Pnt,Pnt2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class LocOpe_Operation():
    """
    None

    Members:

      LocOpe_FUSE

      LocOpe_CUT

      LocOpe_INVALID
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self,value : int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self,other : object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self,state : int) -> None: ...
    @property
    def name(self) -> None:
        """
        :type: None
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    LocOpe_CUT: OCP.LocOpe.LocOpe_Operation # value = <LocOpe_Operation.LocOpe_CUT: 1>
    LocOpe_FUSE: OCP.LocOpe.LocOpe_Operation # value = <LocOpe_Operation.LocOpe_FUSE: 0>
    LocOpe_INVALID: OCP.LocOpe.LocOpe_Operation # value = <LocOpe_Operation.LocOpe_INVALID: 2>
    __entries: dict # value = {'LocOpe_FUSE': (<LocOpe_Operation.LocOpe_FUSE: 0>, None), 'LocOpe_CUT': (<LocOpe_Operation.LocOpe_CUT: 1>, None), 'LocOpe_INVALID': (<LocOpe_Operation.LocOpe_INVALID: 2>, None)}
    __members__: dict # value = {'LocOpe_FUSE': <LocOpe_Operation.LocOpe_FUSE: 0>, 'LocOpe_CUT': <LocOpe_Operation.LocOpe_CUT: 1>, 'LocOpe_INVALID': <LocOpe_Operation.LocOpe_INVALID: 2>}
    pass
class LocOpe_Pipe():
    """
    Defines a pipe (near from Pipe from BRepFill), with modifications provided for the Pipe feature.
    """
    def BarycCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def Curves(self,Spt : OCP.TColgp.TColgp_SequenceOfPnt) -> OCP.TColGeom.TColGeom_SequenceOfCurve: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    def Profile(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shapes(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Spine(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Wire,Profile : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class LocOpe_PntFace():
    """
    None
    """
    def ChangeOrientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Parameter(self) -> float: 
        """
        None
        """
    def Pnt(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def UParameter(self) -> float: 
        """
        None
        """
    def VParameter(self) -> float: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,F : OCP.TopoDS.TopoDS_Face,Or : OCP.TopAbs.TopAbs_Orientation,Param : float,UPar : float,VPar : float) -> None: ...
    pass
class LocOpe_Prism():
    """
    Defines a prism (using Prism from BRepSweep) with modifications provided for the Prism feature.
    """
    def BarycCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def Curves(self,SCurves : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def Perform(self,Base : OCP.TopoDS.TopoDS_Shape,V : OCP.gp.gp_Vec,Vtra : OCP.gp.gp_Vec) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,Base : OCP.TopoDS.TopoDS_Shape,V : OCP.gp.gp_Vec) -> None: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shapes(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Base : OCP.TopoDS.TopoDS_Shape,V : OCP.gp.gp_Vec,Vectra : OCP.gp.gp_Vec) -> None: ...
    @overload
    def __init__(self,Base : OCP.TopoDS.TopoDS_Shape,V : OCP.gp.gp_Vec) -> None: ...
    pass
class LocOpe_Revol():
    """
    Defines a prism (using Prism from BRepSweep) with modifications provided for the Prism feature.
    """
    def BarycCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def Curves(self,SCurves : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def Perform(self,Base : OCP.TopoDS.TopoDS_Shape,Axis : OCP.gp.gp_Ax1,Angle : float,angledec : float) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,Base : OCP.TopoDS.TopoDS_Shape,Axis : OCP.gp.gp_Ax1,Angle : float) -> None: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shapes(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class LocOpe_RevolutionForm():
    """
    Defines a revolution form (using Revol from BRepSweep) with modifications provided for the RevolutionForm feature.
    """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Perform(self,Base : OCP.TopoDS.TopoDS_Shape,Axe : OCP.gp.gp_Ax1,Angle : float) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shapes(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class LocOpe_SequenceOfCirc(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.gp.gp_Circ) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : LocOpe_SequenceOfCirc) -> None: ...
    def Assign(self,theOther : LocOpe_SequenceOfCirc) -> LocOpe_SequenceOfCirc: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.gp.gp_Circ: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.gp.gp_Circ: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_Circ: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> OCP.gp.gp_Circ: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : LocOpe_SequenceOfCirc) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.gp.gp_Circ) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.gp.gp_Circ) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : LocOpe_SequenceOfCirc) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.gp.gp_Circ: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : OCP.gp.gp_Circ) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : LocOpe_SequenceOfCirc) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_Circ) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : LocOpe_SequenceOfCirc) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.gp.gp_Circ: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : LocOpe_SequenceOfCirc) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class LocOpe_SequenceOfLin(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : LocOpe_SequenceOfLin) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OCP.gp.gp_Lin) -> None: ...
    def Assign(self,theOther : LocOpe_SequenceOfLin) -> LocOpe_SequenceOfLin: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.gp.gp_Lin: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.gp.gp_Lin: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_Lin: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> OCP.gp.gp_Lin: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.gp.gp_Lin) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : LocOpe_SequenceOfLin) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.gp.gp_Lin) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : LocOpe_SequenceOfLin) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.gp.gp_Lin: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theSeq : LocOpe_SequenceOfLin) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.gp.gp_Lin) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_Lin) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : LocOpe_SequenceOfLin) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.gp.gp_Lin: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : LocOpe_SequenceOfLin) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class LocOpe_SequenceOfPntFace(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : LocOpe_PntFace) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : LocOpe_SequenceOfPntFace) -> None: ...
    def Assign(self,theOther : LocOpe_SequenceOfPntFace) -> LocOpe_SequenceOfPntFace: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> LocOpe_PntFace: 
        """
        First item access
        """
    def ChangeLast(self) -> LocOpe_PntFace: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> LocOpe_PntFace: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> LocOpe_PntFace: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : LocOpe_SequenceOfPntFace) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : LocOpe_PntFace) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : LocOpe_SequenceOfPntFace) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : LocOpe_PntFace) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> LocOpe_PntFace: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : LocOpe_PntFace) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : LocOpe_SequenceOfPntFace) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : LocOpe_PntFace) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : LocOpe_SequenceOfPntFace) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> LocOpe_PntFace: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : LocOpe_SequenceOfPntFace) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class LocOpe_SplitDrafts():
    """
    This class provides a tool to realize the following operations on a shape : - split a face of the shape with a wire, - put draft angle on both side of the wire. For each side, the draft angle may be different.
    """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes the algorithm with the shape <S>.
        """
    def IsDone(self) -> bool: 
        """
        Returns <Standard_True> if the modification has been successfully performed.
        """
    def OriginalShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def Perform(self,F : OCP.TopoDS.TopoDS_Face,W : OCP.TopoDS.TopoDS_Wire,Extract : OCP.gp.gp_Dir,NPl : OCP.gp.gp_Pln,Angle : float) -> None: 
        """
        Splits the face <F> of the former given shape with the wire <W>. The wire is assumed to lie on the face. Puts a draft angle on both parts of the wire. <Extractg>, <Nplg>, <Angleg> define the arguments for the left part of the wire. <Extractd>, <Npld>, <Angled> define the arguments for the right part of the wire. The draft angle is measured with the direction <Extract>. <Npl> defines the neutral plane (points belonging to the neutral plane are not modified). <Angle> is the value of the draft angle. If <ModifyLeft> is set to <Standard_False>, no draft angle is applied to the left part of the wire. If <ModifyRight> is set to <Standard_False>,no draft angle is applied to the right part of the wire.

        Splits the face <F> of the former given shape with the wire <W>. The wire is assumed to lie on the face. Puts a draft angle on the left part of the wire. The draft angle is measured with the direction <Extract>. <Npl> defines the neutral plane (points belonging to the neutral plane are not modified). <Angle> is the value of the draft angle.
        """
    @overload
    def Perform(self,F : OCP.TopoDS.TopoDS_Face,W : OCP.TopoDS.TopoDS_Wire,Extractg : OCP.gp.gp_Dir,NPlg : OCP.gp.gp_Pln,Angleg : float,Extractd : OCP.gp.gp_Dir,NPld : OCP.gp.gp_Pln,Angled : float,ModifyLeft : bool=True,ModifyRight : bool=True) -> None: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the modified shape.
        """
    def ShapesFromShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Manages the descendant shapes.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class LocOpe_SplitShape():
    """
    Provides a tool to cut : - edges with a vertices, - faces with wires, and rebuilds the shape containing the edges and the faces.
    """
    @overload
    def Add(self,W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Adds the vertex <V> on the edge <E>, at parameter <P>.

        Adds the wire <W> on the face <F>.

        Adds the list of wires <Lwires> on the face <F>.
        """
    @overload
    def Add(self,V : OCP.TopoDS.TopoDS_Vertex,P : float,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def Add(self,Lwires : OCP.TopTools.TopTools_ListOfShape,F : OCP.TopoDS.TopoDS_Face) -> bool: ...
    def CanSplit(self,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Tests if it is possible to split the edge <E>.
        """
    def DescendantShapes(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of descendant shapes of <S>.
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes the process on the shape <S>.
        """
    def LeftOf(self,W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the "left" part defined by the wire <W> on the face <F>. The returned list of shape is in fact a list of faces. The face <F> is considered with its topological orientation in the original shape. <W> is considered with its orientation.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the "original" shape.

        Returns the "original" shape.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class LocOpe_Spliter():
    """
    None
    """
    def DescendantShapes(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of descendant shapes of <S>.
        """
    def DirectLeft(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the faces which are the left of the projected wires and which are
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes the algorithm on the shape <S>.

        Initializes the algorithm on the shape <S>.
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def Left(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the faces of the "left" part on the shape. (It is build from DirectLeft, with the faces connected to this set, and so on...).
        """
    def Perform(self,PW : LocOpe_WiresOnShape) -> None: 
        """
        None
        """
    def ResultingShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the new shape

        Returns the new shape
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the initial shape

        Returns the initial shape
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class LocOpe_WiresOnShape(OCP.Standard.Standard_Transient):
    def Add(self,theEdges : OCP.TopTools.TopTools_SequenceOfShape) -> bool: 
        """
        Add splitting edges or wires for whole initial shape without additional specification edge->face, edge->edge This method puts edge on the corresponding faces from initial shape
        """
    @overload
    def Bind(self,Comp : OCP.TopoDS.TopoDS_Compound,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Bind(self,EfromW : OCP.TopoDS.TopoDS_Edge,EonFace : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def Bind(self,W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def Bind(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    def BindAll(self) -> None: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitEdgeIterator(self) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def IsFaceWithSection(self,aFace : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        tells is the face to be split by section or not

        tells is the face to be split by section or not
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def MoreEdge(self) -> bool: 
        """
        None
        """
    def NextEdge(self) -> None: 
        """
        None
        """
    @overload
    def OnEdge(self,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        If the current edge is projected on an edge, returns <Standard_True> and sets the value of <E>. Otherwise, returns <Standard_False>.

        If the vertex <V> lies on an edge of the original shape, returns <Standard_True> and sets the concerned edge in <E>, and the parameter on the edge in <P>. Else returns <Standard_False>.

        If the vertex <V> lies on an edge of the original shape, returns <Standard_True> and sets the concerned edge in <E>, and the parameter on the edge in <P>. Else returns <Standard_False>.
        """
    @overload
    def OnEdge(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float) -> bool: ...
    @overload
    def OnEdge(self,V : OCP.TopoDS.TopoDS_Vertex,EdgeFrom : OCP.TopoDS.TopoDS_Edge,E : OCP.TopoDS.TopoDS_Edge,P : float) -> bool: ...
    def OnFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the face of the shape on which the current edge is projected.
        """
    def OnVertex(self,Vwire : OCP.TopoDS.TopoDS_Vertex,Vshape : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        None
        """
    def SetCheckInterior(self,ToCheckInterior : bool) -> None: 
        """
        Set the flag of check internal intersections default value is True (to check)

        Set the flag of check internal intersections default value is True (to check)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
LocOpe_CUT: OCP.LocOpe.LocOpe_Operation # value = <LocOpe_Operation.LocOpe_CUT: 1>
LocOpe_FUSE: OCP.LocOpe.LocOpe_Operation # value = <LocOpe_Operation.LocOpe_FUSE: 0>
LocOpe_INVALID: OCP.LocOpe.LocOpe_Operation # value = <LocOpe_Operation.LocOpe_INVALID: 2>
