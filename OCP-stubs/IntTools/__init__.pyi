import OCP.IntTools
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.Geom2d
import OCP.GeomInt
import OCP.Adaptor3d
import OCP.GeomAdaptor
import OCP.TopoDS
import OCP.BRepAdaptor
import OCP.NCollection
import OCP.Adaptor2d
import OCP.gp
import OCP.GeomAbs
import OCP.TColStd
import OCP.GeomAPI
import OCP.Bnd
import OCP.IntSurf
import OCP.IntPatch
import OCP.Standard
import OCP.Geom2dHatch
import OCP.Geom
import OCP.BRepClass3d
__all__  = [
"IntTools",
"IntTools_Array1OfRange",
"IntTools_Array1OfRoots",
"IntTools_BaseRangeSample",
"IntTools_BeanFaceIntersector",
"IntTools_CArray1OfInteger",
"IntTools_CArray1OfReal",
"IntTools_CommonPrt",
"IntTools_Context",
"IntTools_Curve",
"IntTools_CurveRangeLocalizeData",
"IntTools_CurveRangeSample",
"IntTools_CurveRangeSampleMapHasher",
"IntTools_DataMapOfCurveSampleBox",
"IntTools_DataMapOfSurfaceSampleBox",
"IntTools_EdgeEdge",
"IntTools_EdgeFace",
"IntTools_FClass2d",
"IntTools_FaceFace",
"IntTools_ListOfBox",
"IntTools_ListOfCurveRangeSample",
"IntTools_ListOfSurfaceRangeSample",
"IntTools_MapOfCurveSample",
"IntTools_MapOfSurfaceSample",
"IntTools_MarkedRangeSet",
"IntTools_PntOn2Faces",
"IntTools_PntOnFace",
"IntTools_Range",
"IntTools_Root",
"IntTools_SequenceOfCommonPrts",
"IntTools_SequenceOfCurves",
"IntTools_SequenceOfPntOn2Faces",
"IntTools_SequenceOfRanges",
"IntTools_SequenceOfRoots",
"IntTools_ShrunkRange",
"IntTools_SurfaceRangeLocalizeData",
"IntTools_SurfaceRangeSample",
"IntTools_SurfaceRangeSampleMapHasher",
"IntTools_Tools",
"IntTools_TopolTool",
"IntTools_WLineTool"
]
class IntTools():
    """
    Contains classes for intersection and classification purposes and accompanying classes
    """
    @staticmethod
    def FindRootStates_s(aSeq : IntTools_SequenceOfRoots,anEpsNull : float) -> None: 
        """
        Find the states (before and after) for each Root from the sequence aSeq
        """
    @staticmethod
    def GetRadius_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,t1 : float,t3 : float,R : float) -> int: 
        """
        None
        """
    @staticmethod
    def Length_s(E : OCP.TopoDS.TopoDS_Edge) -> float: 
        """
        returns the length of the edge;
        """
    @staticmethod
    def Parameter_s(P : OCP.gp.gp_Pnt,Curve : OCP.Geom.Geom_Curve,aParm : float) -> int: 
        """
        None
        """
    @staticmethod
    def PrepareArgs_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,tMax : float,tMin : float,Discret : int,Deflect : float,anArgs : IntTools_CArray1OfReal) -> int: 
        """
        None
        """
    @staticmethod
    def RemoveIdenticalRoots_s(aSeq : IntTools_SequenceOfRoots,anEpsT : float) -> None: 
        """
        Remove from the sequence aSeq the Roots that have values ti and tj such as |ti-tj] < anEpsT.
        """
    @staticmethod
    def SortRoots_s(aSeq : IntTools_SequenceOfRoots,anEpsT : float) -> None: 
        """
        Sort the sequence aSeq of the Roots to arrange the Roons in increasing order
        """
    def __init__(self) -> None: ...
    pass
class IntTools_Array1OfRange():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IntTools_Array1OfRange) -> IntTools_Array1OfRange: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IntTools_Range: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IntTools_Range: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IntTools_Range: 
        """
        Variable value access
        """
    def First(self) -> IntTools_Range: 
        """
        Returns first element
        """
    def Init(self,theValue : IntTools_Range) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> IntTools_Range: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : IntTools_Array1OfRange) -> IntTools_Array1OfRange: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IntTools_Range) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> IntTools_Range: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : IntTools_Range,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_Array1OfRange) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IntTools_Array1OfRoots():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IntTools_Array1OfRoots) -> IntTools_Array1OfRoots: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IntTools_Root: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IntTools_Root: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IntTools_Root: 
        """
        Variable value access
        """
    def First(self) -> IntTools_Root: 
        """
        Returns first element
        """
    def Init(self,theValue : IntTools_Root) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> IntTools_Root: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : IntTools_Array1OfRoots) -> IntTools_Array1OfRoots: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IntTools_Root) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> IntTools_Root: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : IntTools_Root,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_Array1OfRoots) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IntTools_BaseRangeSample():
    """
    base class for range index management
    """
    def GetDepth(self) -> int: 
        """
        None

        None
        """
    def SetDepth(self,theDepth : int) -> None: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theDepth : int) -> None: ...
    pass
class IntTools_BeanFaceIntersector():
    """
    The class BeanFaceIntersector computes ranges of parameters on the curve of a bean(part of edge) that bound the parts of bean which are on the surface of a face according to edge and face tolerances. Warning: The real boundaries of the face are not taken into account, Most of the result parts of the bean lays only inside the region of the surface, which includes the inside of the face. And the parts which are out of this region can be excluded from the result.
    """
    def Context(self) -> IntTools_Context: 
        """
        Gets the intersecton context
        """
    @overload
    def Init(self,theCurve : OCP.BRepAdaptor.BRepAdaptor_Curve,theSurface : OCP.BRepAdaptor.BRepAdaptor_Surface,theFirstParOnCurve : float,theLastParOnCurve : float,theUMinParameter : float,theUMaxParameter : float,theVMinParameter : float,theVMaxParameter : float,theBeanTolerance : float,theFaceTolerance : float) -> None: 
        """
        Initializes the algorithm

        Initializes the algorithm

        Initializes the algorithm theUMinParameter, ... are used for optimization purposes
        """
    @overload
    def Init(self,theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def Init(self,theCurve : OCP.BRepAdaptor.BRepAdaptor_Curve,theSurface : OCP.BRepAdaptor.BRepAdaptor_Surface,theBeanTolerance : float,theFaceTolerance : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns Done/NotDone state of the algorithm.
        """
    def Perform(self) -> None: 
        """
        Launches the algorithm
        """
    @overload
    def Result(self,theResults : IntTools_SequenceOfRanges) -> None: 
        """
        None

        None
        """
    @overload
    def Result(self) -> IntTools_SequenceOfRanges: ...
    def SetBeanParameters(self,theFirstParOnCurve : float,theLastParOnCurve : float) -> None: 
        """
        Set restrictions for curve
        """
    def SetContext(self,theContext : IntTools_Context) -> None: 
        """
        Sets the intersecton context
        """
    def SetSurfaceParameters(self,theUMinParameter : float,theUMaxParameter : float,theVMinParameter : float,theVMaxParameter : float) -> None: 
        """
        Set restrictions for surface
        """
    @overload
    def __init__(self,theCurve : OCP.BRepAdaptor.BRepAdaptor_Curve,theSurface : OCP.BRepAdaptor.BRepAdaptor_Surface,theBeanTolerance : float,theFaceTolerance : float) -> None: ...
    @overload
    def __init__(self,theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCurve : OCP.BRepAdaptor.BRepAdaptor_Curve,theSurface : OCP.BRepAdaptor.BRepAdaptor_Surface,theFirstParOnCurve : float,theLastParOnCurve : float,theUMinParameter : float,theUMaxParameter : float,theVMinParameter : float,theVMaxParameter : float,theBeanTolerance : float,theFaceTolerance : float) -> None: ...
    pass
class IntTools_CArray1OfInteger():
    """
    None
    """
    def Append(self,Value : int) -> None: 
        """
        None
        """
    def ChangeValue(self,Index : int) -> int: 
        """
        Returns the value of the <Index>th element of the array.
        """
    def Destroy(self) -> None: 
        """
        Frees the allocated area corresponding to the array.
        """
    def Init(self,V : int) -> None: 
        """
        Initializes the array with a given value.
        """
    def IsEqual(self,Other : IntTools_CArray1OfInteger) -> bool: 
        """
        Applys the == operator on each array item
        """
    def Length(self) -> int: 
        """
        Returns the number of elements of <me>.
        """
    def Resize(self,theNewLength : int) -> None: 
        """
        destroy current content and realloc the new size does nothing if Length() == theLength
        """
    def SetValue(self,Index : int,Value : int) -> None: 
        """
        Sets the <Index>th element of the array to <Value>.
        """
    def Value(self,Index : int) -> int: 
        """
        Returns the value of the <Index>th element of the array.
        """
    @overload
    def __init__(self,Item : int,Length : int) -> None: ...
    @overload
    def __init__(self,Length : int=0) -> None: ...
    pass
class IntTools_CArray1OfReal():
    """
    None
    """
    def Append(self,Value : float) -> None: 
        """
        None
        """
    def ChangeValue(self,Index : int) -> float: 
        """
        Returns the value of the <Index>th element of the array.
        """
    def Destroy(self) -> None: 
        """
        Frees the allocated area corresponding to the array.
        """
    def Init(self,V : float) -> None: 
        """
        Initializes the array with a given value.
        """
    def IsEqual(self,Other : IntTools_CArray1OfReal) -> bool: 
        """
        Applys the == operator on each array item
        """
    def Length(self) -> int: 
        """
        Returns the number of elements of <me>.
        """
    def Resize(self,theNewLength : int) -> None: 
        """
        destroy current content and realloc the new size does nothing if Length() == theLength
        """
    def SetValue(self,Index : int,Value : float) -> None: 
        """
        Sets the <Index>th element of the array to <Value>.
        """
    def Value(self,Index : int) -> float: 
        """
        Returns the value of the <Index>th element of the array.
        """
    @overload
    def __init__(self,Item : float,Length : int) -> None: ...
    @overload
    def __init__(self,Length : int=0) -> None: ...
    pass
class IntTools_CommonPrt():
    """
    The class is to describe a common part between two edges in 3-d space.
    """
    def AllNullFlag(self) -> bool: 
        """
        Modifier
        """
    @overload
    def AppendRange2(self,aR : IntTools_Range) -> None: 
        """
        Appends the range of second edge.

        Appends the range of second edge.
        """
    @overload
    def AppendRange2(self,tf : float,tl : float) -> None: ...
    def Assign(self,Other : IntTools_CommonPrt) -> IntTools_CommonPrt: 
        """
        None
        """
    def BoundingPoints(self,aP1 : OCP.gp.gp_Pnt,aP2 : OCP.gp.gp_Pnt) -> None: 
        """
        Selector
        """
    def ChangeRanges2(self) -> IntTools_SequenceOfRanges: 
        """
        Returns the ranges of second edge.
        """
    def Copy(self,anOther : IntTools_CommonPrt) -> None: 
        """
        Copies me to anOther
        """
    def Edge1(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the first edge.
        """
    def Edge2(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the second edge
        """
    @overload
    def Range1(self) -> Tuple[float, float]: 
        """
        Returns the range of first edge.

        Returns the range of first edge
        """
    @overload
    def Range1(self) -> IntTools_Range: ...
    def Ranges2(self) -> IntTools_SequenceOfRanges: 
        """
        Returns the ranges of second edge.
        """
    def SetAllNullFlag(self,aFlag : bool) -> None: 
        """
        Selector
        """
    def SetBoundingPoints(self,aP1 : OCP.gp.gp_Pnt,aP2 : OCP.gp.gp_Pnt) -> None: 
        """
        Modifier
        """
    def SetEdge1(self,anE : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Sets the first edge.
        """
    def SetEdge2(self,anE : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Sets the second edge.
        """
    @overload
    def SetRange1(self,tf : float,tl : float) -> None: 
        """
        Sets the range of first edge.

        Sets the range of first edge.
        """
    @overload
    def SetRange1(self,aR : IntTools_Range) -> None: ...
    def SetType(self,aType : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        Sets the type of the common part Vertex or Edge
        """
    def SetVertexParameter1(self,tV : float) -> None: 
        """
        Sets a parameter of first vertex
        """
    def SetVertexParameter2(self,tV : float) -> None: 
        """
        Sets a parameter of second vertex
        """
    def Type(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the type of the common part
        """
    def VertexParameter1(self) -> float: 
        """
        Returns parameter of first vertex
        """
    def VertexParameter2(self) -> float: 
        """
        Returns parameter of second vertex
        """
    @overload
    def __init__(self,aCPrt : IntTools_CommonPrt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntTools_Context(OCP.Standard.Standard_Transient):
    """
    The intersection Context contains geometrical and topological toolkit (classifiers, projectors, etc). The intersection Context is for caching the tools to increase the performance.The intersection Context contains geometrical and topological toolkit (classifiers, projectors, etc). The intersection Context is for caching the tools to increase the performance.
    """
    def BndBox(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def ComputePE(self,theP : OCP.gp.gp_Pnt,theTolP : float,theE : OCP.TopoDS.TopoDS_Edge,theT : float,theDist : float) -> int: 
        """
        Computes parameter of the Point theP on the edge aE. Returns zero if the distance between point and edge is less than sum of tolerance value of edge and theTopP, otherwise and for following conditions returns negative value 1. the edge is degenerated (-1) 2. the edge does not contain 3d curve and pcurves (-2) 3. projection algorithm failed (-3)
        """
    def ComputeVE(self,theV : OCP.TopoDS.TopoDS_Vertex,theE : OCP.TopoDS.TopoDS_Edge,theT : float,theTol : float,theFuzz : float=1e-07) -> int: 
        """
        Computes parameter of the vertex aV on the edge aE and correct tolerance value for the vertex on the edge. Returns zero if the distance between vertex and edge is less than sum of tolerances and the fuzzy value, otherwise and for following conditions returns negative value: 1. the edge is degenerated (-1) 2. the edge does not contain 3d curve and pcurves (-2) 3. projection algorithm failed (-3)
        """
    def ComputeVF(self,theVertex : OCP.TopoDS.TopoDS_Vertex,theFace : OCP.TopoDS.TopoDS_Face,theU : float,theV : float,theTol : float,theFuzz : float=1e-07) -> int: 
        """
        Computes UV parameters of the vertex aV on face aF and correct tolerance value for the vertex on the face. Returns zero if the distance between vertex and face is less than or equal the sum of tolerances and the fuzzy value and the projection point lays inside boundaries of the face. For following conditions returns negative value 1. projection algorithm failed (-1) 2. distance is more than sum of tolerances (-2) 3. projection point out or on the boundaries of face (-3)
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
    def FClass2d(self,aF : OCP.TopoDS.TopoDS_Face) -> IntTools_FClass2d: 
        """
        Returns a reference to point classifier for given face
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hatcher(self,aF : OCP.TopoDS.TopoDS_Face) -> OCP.Geom2dHatch.Geom2dHatch_Hatcher: 
        """
        Returns a reference to 2D hatcher for given face
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsInfiniteFace(self,theFace : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns true if the solid <theFace> has infinite bounds
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    @overload
    def IsPointInFace(self,aF : OCP.TopoDS.TopoDS_Face,aP2D : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Returns true if the point aP2D is inside the boundaries of the face aF, otherwise returns false

        Returns true if the point aP2D is inside the boundaries of the face aF, otherwise returns false
        """
    @overload
    def IsPointInFace(self,aP3D : OCP.gp.gp_Pnt,aF : OCP.TopoDS.TopoDS_Face,aTol : float) -> bool: ...
    def IsPointInOnFace(self,aF : OCP.TopoDS.TopoDS_Face,aP2D : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Returns true if the point aP2D is inside or on the boundaries of aF
        """
    def IsValidBlockForFace(self,aT1 : float,aT2 : float,aIC : IntTools_Curve,aF : OCP.TopoDS.TopoDS_Face,aTol : float) -> bool: 
        """
        Returns true if IsValidPointForFace returns true for some 3d point that lay on the curve aIC bounded by parameters aT1 and aT2
        """
    def IsValidBlockForFaces(self,aT1 : float,aT2 : float,aIC : IntTools_Curve,aF1 : OCP.TopoDS.TopoDS_Face,aF2 : OCP.TopoDS.TopoDS_Face,aTol : float) -> bool: 
        """
        Returns true if IsValidBlockForFace returns true for both faces aF1 and aF2
        """
    def IsValidPointForFace(self,aP3D : OCP.gp.gp_Pnt,aF : OCP.TopoDS.TopoDS_Face,aTol : float) -> bool: 
        """
        Returns true if the distance between point aP3D and face aF is less or equal to tolerance aTol and projection point is inside or on the boundaries of the face aF
        """
    def IsValidPointForFaces(self,aP3D : OCP.gp.gp_Pnt,aF1 : OCP.TopoDS.TopoDS_Face,aF2 : OCP.TopoDS.TopoDS_Face,aTol : float) -> bool: 
        """
        Returns true if IsValidPointForFace returns true for both face aF1 and aF2
        """
    @overload
    def IsVertexOnLine(self,aV : OCP.TopoDS.TopoDS_Vertex,aTolV : float,aIC : IntTools_Curve,aTolC : float,aT : float) -> bool: 
        """
        Computes parameter of the vertex aV on the curve aIC. Returns true if the distance between vertex and curve is less than sum of tolerance of aV and aTolC, otherwise or if projection algorithm failed returns false (in this case aT isn't significant)

        Computes parameter of the vertex aV on the curve aIC. Returns true if the distance between vertex and curve is less than sum of tolerance of aV and aTolC, otherwise or if projection algorithm failed returns false (in this case aT isn't significant)
        """
    @overload
    def IsVertexOnLine(self,aV : OCP.TopoDS.TopoDS_Vertex,aIC : IntTools_Curve,aTolC : float,aT : float) -> bool: ...
    def OBB(self,theShape : OCP.TopoDS.TopoDS_Shape,theFuzzyValue : float=1e-07) -> OCP.Bnd.Bnd_OBB: 
        """
        Builds and stores an Oriented Bounding Box for the shape. Returns a reference to OBB.
        """
    def ProjPC(self,aE : OCP.TopoDS.TopoDS_Edge) -> OCP.GeomAPI.GeomAPI_ProjectPointOnCurve: 
        """
        Returns a reference to point projector for given edge
        """
    def ProjPS(self,aF : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAPI.GeomAPI_ProjectPointOnSurf: 
        """
        Returns a reference to point projector for given face
        """
    def ProjPT(self,aC : OCP.Geom.Geom_Curve) -> OCP.GeomAPI.GeomAPI_ProjectPointOnCurve: 
        """
        Returns a reference to point projector for given curve
        """
    def ProjectPointOnEdge(self,aP : OCP.gp.gp_Pnt,aE : OCP.TopoDS.TopoDS_Edge,aT : float) -> bool: 
        """
        Computes parameter of the point aP on the edge aE. Returns false if projection algorithm failed other wiese returns true.
        """
    def SetPOnSProjectionTolerance(self,theValue : float) -> None: 
        """
        Sets tolerance to be used for projection of point on surface. Clears map of already cached projectors in order to maintain correct value for all projectors
        """
    def SolidClassifier(self,aSolid : OCP.TopoDS.TopoDS_Solid) -> OCP.BRepClass3d.BRepClass3d_SolidClassifier: 
        """
        Returns a reference to solid classifier for given solid
        """
    def StatePointFace(self,aF : OCP.TopoDS.TopoDS_Face,aP2D : OCP.gp.gp_Pnt2d) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the state of the point aP2D relative to face aF
        """
    def SurfaceAdaptor(self,theFace : OCP.TopoDS.TopoDS_Face) -> OCP.BRepAdaptor.BRepAdaptor_Surface: 
        """
        Returns a reference to surface adaptor for given face
        """
    def SurfaceData(self,aF : OCP.TopoDS.TopoDS_Face) -> IntTools_SurfaceRangeLocalizeData: 
        """
        Returns a reference to surface localization data for given face
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UVBounds(self,theFace : OCP.TopoDS.TopoDS_Face) -> Tuple[float, float, float, float]: 
        """
        Computes the boundaries of the face using surface adaptor
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
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
class IntTools_Curve():
    """
    The class is a container of one 3D curve, two 2D curves and two Tolerance values. It is used in the Face/Face intersection algorithm to store the results of intersection. In this context: **the 3D curve** is the intersection curve; **the 2D curves** are the PCurves of the 3D curve on the intersecting faces; **the tolerance** is the valid tolerance for 3D curve computed as maximal deviation between 3D curve and 2D curves (or surfaces in case there are no 2D curves); **the tangential tolerance** is the maximal distance from 3D curve to the end of the tangential zone between faces in terms of their tolerance values.
    """
    def Bounds(self,theFirst : float,theLast : float,theFirstPnt : OCP.gp.gp_Pnt,theLastPnt : OCP.gp.gp_Pnt) -> bool: 
        """
        If the 3d curve is bounded curve the method will return TRUE and modify the output parameters with boundary parameters of the curve and corresponded 3d points. If the curve does not have bounds, the method will return false and the output parameters will stay untouched.
        """
    def Curve(self) -> OCP.Geom.Geom_Curve: 
        """
        Returns 3d curve
        """
    def D0(self,thePar : float,thePnt : OCP.gp.gp_Pnt) -> bool: 
        """
        Computes 3d point corresponded to the given parameter if this parameter is inside the boundaries of the curve. Returns TRUE in this case. Otherwise, the point will not be computed and the method will return FALSE.
        """
    def FirstCurve2d(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns first 2d curve
        """
    def HasBounds(self) -> bool: 
        """
        Returns TRUE if 3d curve is BoundedCurve
        """
    def SecondCurve2d(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns second 2d curve
        """
    def SetCurve(self,the3dCurve : OCP.Geom.Geom_Curve) -> None: 
        """
        Sets the 3d curve
        """
    def SetCurves(self,the3dCurve : OCP.Geom.Geom_Curve,the2dCurve1 : OCP.Geom2d.Geom2d_Curve,the2dCurve2 : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Sets the curves
        """
    def SetFirstCurve2d(self,the2dCurve1 : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Sets the first 2d curve
        """
    def SetSecondCurve2d(self,the2dCurve2 : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Sets the second 2d curve
        """
    def SetTangentialTolerance(self,theTangentialTolerance : float) -> None: 
        """
        Sets the tangential tolerance
        """
    def SetTolerance(self,theTolerance : float) -> None: 
        """
        Sets the tolerance for the curve
        """
    def TangentialTolerance(self) -> float: 
        """
        Returns the tangential tolerance
        """
    def Tolerance(self) -> float: 
        """
        Returns the tolerance
        """
    def Type(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the 3d curve
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,the3dCurve3d : OCP.Geom.Geom_Curve,the2dCurve1 : OCP.Geom2d.Geom2d_Curve,the2dCurve2 : OCP.Geom2d.Geom2d_Curve,theTolerance : float=0.0,theTangentialTolerance : float=0.0) -> None: ...
    pass
class IntTools_CurveRangeLocalizeData():
    """
    None
    """
    def AddBox(self,theRange : IntTools_CurveRangeSample,theBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        None
        """
    def AddOutRange(self,theRange : IntTools_CurveRangeSample) -> None: 
        """
        None
        """
    def FindBox(self,theRange : IntTools_CurveRangeSample,theBox : OCP.Bnd.Bnd_Box) -> bool: 
        """
        None
        """
    def GetMinRange(self) -> float: 
        """
        None

        None
        """
    def GetNbSample(self) -> int: 
        """
        None

        None
        """
    def IsRangeOut(self,theRange : IntTools_CurveRangeSample) -> bool: 
        """
        None
        """
    def ListRangeOut(self,theList : IntTools_ListOfCurveRangeSample) -> None: 
        """
        None
        """
    def __init__(self,theNbSample : int,theMinRange : float) -> None: ...
    pass
class IntTools_CurveRangeSample(IntTools_BaseRangeSample):
    """
    class for range index management of curve
    """
    def GetDepth(self) -> int: 
        """
        None

        None
        """
    def GetRange(self,theFirst : float,theLast : float,theNbSample : int) -> IntTools_Range: 
        """
        None
        """
    def GetRangeIndex(self) -> int: 
        """
        None

        None
        """
    def GetRangeIndexDeeper(self,theNbSample : int) -> int: 
        """
        None

        None
        """
    def IsEqual(self,Other : IntTools_CurveRangeSample) -> bool: 
        """
        None

        None
        """
    def SetDepth(self,theDepth : int) -> None: 
        """
        None

        None
        """
    def SetRangeIndex(self,theIndex : int) -> None: 
        """
        None

        None
        """
    @overload
    def __init__(self,theIndex : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntTools_CurveRangeSampleMapHasher():
    """
    class for range index management of curve
    """
    @staticmethod
    def HashCode_s(theKey : IntTools_CurveRangeSample,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(S1 : IntTools_CurveRangeSample,S2 : IntTools_CurveRangeSample) -> bool: 
        """
        Returns True when the two keys are the same. Two same keys must have the same hashcode, the contrary is not necessary.
        """
    def __init__(self) -> None: ...
    pass
class IntTools_DataMapOfCurveSampleBox(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : IntTools_DataMapOfCurveSampleBox) -> IntTools_DataMapOfCurveSampleBox: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : IntTools_CurveRangeSample,theItem : OCP.Bnd.Bnd_Box) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : IntTools_CurveRangeSample,theItem : OCP.Bnd.Bnd_Box) -> OCP.Bnd.Bnd_Box: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : IntTools_CurveRangeSample) -> OCP.Bnd.Bnd_Box: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : IntTools_CurveRangeSample) -> OCP.Bnd.Bnd_Box: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : IntTools_DataMapOfCurveSampleBox) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : IntTools_CurveRangeSample) -> OCP.Bnd.Bnd_Box: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : IntTools_CurveRangeSample,theValue : OCP.Bnd.Bnd_Box) -> bool: ...
    def IsBound(self,theKey : IntTools_CurveRangeSample) -> bool: 
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
    def Seek(self,theKey : IntTools_CurveRangeSample) -> OCP.Bnd.Bnd_Box: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : IntTools_CurveRangeSample) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_DataMapOfCurveSampleBox) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IntTools_DataMapOfSurfaceSampleBox(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : IntTools_DataMapOfSurfaceSampleBox) -> IntTools_DataMapOfSurfaceSampleBox: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : IntTools_SurfaceRangeSample,theItem : OCP.Bnd.Bnd_Box) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : IntTools_SurfaceRangeSample,theItem : OCP.Bnd.Bnd_Box) -> OCP.Bnd.Bnd_Box: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : IntTools_SurfaceRangeSample) -> OCP.Bnd.Bnd_Box: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : IntTools_SurfaceRangeSample) -> OCP.Bnd.Bnd_Box: 
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
    def Exchange(self,theOther : IntTools_DataMapOfSurfaceSampleBox) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : IntTools_SurfaceRangeSample) -> OCP.Bnd.Bnd_Box: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : IntTools_SurfaceRangeSample,theValue : OCP.Bnd.Bnd_Box) -> bool: ...
    def IsBound(self,theKey : IntTools_SurfaceRangeSample) -> bool: 
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
    def Seek(self,theKey : IntTools_SurfaceRangeSample) -> OCP.Bnd.Bnd_Box: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : IntTools_SurfaceRangeSample) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_DataMapOfSurfaceSampleBox) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IntTools_EdgeEdge():
    """
    The class provides Edge/Edge intersection algorithm based on the intersection between edges bounding boxes.
    """
    def CommonParts(self) -> IntTools_SequenceOfCommonPrts: 
        """
        Returns common parts

        Returns common parts
        """
    def FuzzyValue(self) -> float: 
        """
        Returns Fuzzy value

        Returns Fuzzy value
        """
    def IsCoincidenceCheckedQuickly(self) -> bool: 
        """
        Returns the flag myQuickCoincidenceCheck
        """
    def IsDone(self) -> bool: 
        """
        Returns TRUE if common part(s) is(are) found

        Returns TRUE if common part(s) is(are) found
        """
    def Perform(self) -> None: 
        """
        Performs the intersection between edges
        """
    @overload
    def SetEdge1(self,theEdge : OCP.TopoDS.TopoDS_Edge,aT1 : float,aT2 : float) -> None: 
        """
        Sets the first edge

        Sets the first edge and its range

        Sets the first edge

        Sets the first edge and its range
        """
    @overload
    def SetEdge1(self,theEdge : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def SetEdge2(self,theEdge : OCP.TopoDS.TopoDS_Edge,aT1 : float,aT2 : float) -> None: 
        """
        Sets the second edge

        Sets the first edge and its range

        Sets the second edge

        Sets the first edge and its range
        """
    @overload
    def SetEdge2(self,theEdge : OCP.TopoDS.TopoDS_Edge) -> None: ...
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the Fuzzy value

        Sets the Fuzzy value
        """
    @overload
    def SetRange1(self,theRange1 : IntTools_Range) -> None: 
        """
        Sets the range for the first edge

        Sets the range for the first edge

        Sets the range for the first edge

        Sets the range for the first edge
        """
    @overload
    def SetRange1(self,aT1 : float,aT2 : float) -> None: ...
    @overload
    def SetRange1(self,theRange : IntTools_Range) -> None: ...
    @overload
    def SetRange2(self,theRange : IntTools_Range) -> None: 
        """
        Sets the range for the second edge

        Sets the range for the second edge

        Sets the range for the second edge

        Sets the range for the second edge
        """
    @overload
    def SetRange2(self,aT1 : float,aT2 : float) -> None: ...
    def UseQuickCoincidenceCheck(self,bFlag : bool) -> None: 
        """
        Sets the flag myQuickCoincidenceCheck
        """
    @overload
    def __init__(self,theEdge1 : OCP.TopoDS.TopoDS_Edge,aT11 : float,aT12 : float,theEdge2 : OCP.TopoDS.TopoDS_Edge,aT21 : float,aT22 : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theEdge1 : OCP.TopoDS.TopoDS_Edge,theEdge2 : OCP.TopoDS.TopoDS_Edge) -> None: ...
    pass
class IntTools_EdgeFace():
    """
    The class provides Edge/Face intersection algorithm to determine common parts between edge and face in 3-d space. Common parts between Edge and Face can be: - Vertices - in case of intersection or touching; - Edge - in case of full coincidence of the edge with the face.
    """
    def CommonParts(self) -> IntTools_SequenceOfCommonPrts: 
        """
        Returns resulting common parts
        """
    def Context(self) -> IntTools_Context: 
        """
        Returns the intersection context
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge
        """
    def ErrorStatus(self) -> int: 
        """
        Returns the code of completion: 0 - means successful completion; 1 - the process was not started; 2,3 - invalid source data for the algorithm; 4 - projection failed.
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the face
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the Fuzzy value
        """
    def IsCoincidenceCheckedQuickly(self) -> bool: 
        """
        Returns the flag myQuickCoincidenceCheck
        """
    def IsDone(self) -> bool: 
        """
        Returns TRUE if computation was successful. Otherwise returns FALSE.
        """
    def Perform(self) -> None: 
        """
        Launches the process
        """
    def Range(self) -> IntTools_Range: 
        """
        Returns intersection range of the edge
        """
    def SetContext(self,theContext : IntTools_Context) -> None: 
        """
        Sets the intersection context
        """
    def SetEdge(self,theEdge : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Sets the edge for intersection
        """
    def SetFace(self,theFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the face for intersection
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the Fuzzy value
        """
    @overload
    def SetRange(self,theRange : IntTools_Range) -> None: 
        """
        Sets the boundaries for the edge. The algorithm processes edge inside these boundaries.

        Sets the boundaries for the edge. The algorithm processes edge inside these boundaries.
        """
    @overload
    def SetRange(self,theFirst : float,theLast : float) -> None: ...
    def UseQuickCoincidenceCheck(self,theFlag : bool) -> None: 
        """
        Sets the flag for quick coincidence check. It is safe to use the quick check for coincidence only if both of the following conditions are met: - The vertices of edge are lying on the face; - The edge does not intersect the boundaries of the face on the given range.
        """
    def __init__(self) -> None: ...
    pass
class IntTools_FClass2d():
    """
    Class provides an algorithm to classify a 2d Point in 2d space of face using boundaries of the face.
    """
    def Destroy(self) -> None: 
        """
        Destructor
        """
    def Init(self,F : OCP.TopoDS.TopoDS_Face,Tol : float) -> None: 
        """
        Initializes algorithm by the face F and tolerance Tol
        """
    def IsHole(self) -> bool: 
        """
        None
        """
    def Perform(self,Puv : OCP.gp.gp_Pnt2d,RecadreOnPeriodic : bool=True) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns state of the 2d point Puv. If RecadreOnPeriodic is true (defalut value), for the periodic surface 2d point, adjusted to period, is classified.
        """
    def PerformInfinitePoint(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns state of infinite 2d point relatively to (0, 0)
        """
    def TestOnRestriction(self,Puv : OCP.gp.gp_Pnt2d,Tol : float,RecadreOnPeriodic : bool=True) -> OCP.TopAbs.TopAbs_State: 
        """
        Test a point with +- an offset (Tol) and returns On if some points are OUT an some are IN (Caution: Internal use . see the code for more details)
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,Tol : float) -> None: ...
    pass
class IntTools_FaceFace():
    """
    This class provides the intersection of face's underlying surfaces.
    """
    def Context(self) -> IntTools_Context: 
        """
        Gets the intersecton context
        """
    def Face1(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns first of processed faces
        """
    def Face2(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns second of processed faces
        """
    def FuzzyValue(self) -> float: 
        """
        Returns Fuzzy value
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the intersection was successful
        """
    def Lines(self) -> IntTools_SequenceOfCurves: 
        """
        Returns sequence of 3d curves as result of intersection
        """
    def Perform(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Intersects underliing surfaces of F1 and F2 Use sum of tolerance of F1 and F2 as intersection criteria
        """
    def Points(self) -> IntTools_SequenceOfPntOn2Faces: 
        """
        Returns sequence of 3d curves as result of intersection
        """
    def PrepareLines3D(self,bToSplit : bool=True) -> None: 
        """
        Provides post-processing the result lines. <bToSplit> - the flag. In case of <bToSplit> is true the closed 3D-curves will be splitted on parts. In case of <bToSplit> is false the closed 3D-curves remain untouched.
        """
    def SetContext(self,aContext : IntTools_Context) -> None: 
        """
        Sets the intersecton context
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the Fuzzy value
        """
    def SetList(self,ListOfPnts : OCP.IntSurf.IntSurf_ListOfPntOn2S) -> None: 
        """
        None
        """
    def SetParameters(self,ApproxCurves : bool,ComputeCurveOnS1 : bool,ComputeCurveOnS2 : bool,ApproximationTolerance : float) -> None: 
        """
        Modifier
        """
    def TangentFaces(self) -> bool: 
        """
        Returns True if faces are tangent
        """
    def __init__(self) -> None: ...
    pass
class IntTools_ListOfBox(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.Bnd.Bnd_Box) -> OCP.Bnd.Bnd_Box: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : IntTools_ListOfBox) -> None: ...
    @overload
    def Append(self,theItem : OCP.Bnd.Bnd_Box,theIter : Any) -> None: ...
    def Assign(self,theOther : IntTools_ListOfBox) -> IntTools_ListOfBox: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> OCP.Bnd.Bnd_Box: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.Bnd.Bnd_Box,theIter : Any) -> OCP.Bnd.Bnd_Box: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : IntTools_ListOfBox,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : IntTools_ListOfBox,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : OCP.Bnd.Bnd_Box,theIter : Any) -> OCP.Bnd.Bnd_Box: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.Bnd.Bnd_Box: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : IntTools_ListOfBox) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OCP.Bnd.Bnd_Box) -> OCP.Bnd.Bnd_Box: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self,theOther : IntTools_ListOfBox) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IntTools_ListOfCurveRangeSample(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntTools_CurveRangeSample,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : IntTools_CurveRangeSample) -> IntTools_CurveRangeSample: ...
    @overload
    def Append(self,theOther : IntTools_ListOfCurveRangeSample) -> None: ...
    def Assign(self,theOther : IntTools_ListOfCurveRangeSample) -> IntTools_ListOfCurveRangeSample: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> IntTools_CurveRangeSample: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : IntTools_CurveRangeSample,theIter : Any) -> IntTools_CurveRangeSample: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : IntTools_ListOfCurveRangeSample,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : IntTools_ListOfCurveRangeSample,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : IntTools_CurveRangeSample,theIter : Any) -> IntTools_CurveRangeSample: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> IntTools_CurveRangeSample: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : IntTools_CurveRangeSample) -> IntTools_CurveRangeSample: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : IntTools_ListOfCurveRangeSample) -> None: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_ListOfCurveRangeSample) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IntTools_ListOfSurfaceRangeSample(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntTools_SurfaceRangeSample) -> IntTools_SurfaceRangeSample: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : IntTools_ListOfSurfaceRangeSample) -> None: ...
    @overload
    def Append(self,theItem : IntTools_SurfaceRangeSample,theIter : Any) -> None: ...
    def Assign(self,theOther : IntTools_ListOfSurfaceRangeSample) -> IntTools_ListOfSurfaceRangeSample: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> IntTools_SurfaceRangeSample: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : IntTools_ListOfSurfaceRangeSample,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : IntTools_SurfaceRangeSample,theIter : Any) -> IntTools_SurfaceRangeSample: ...
    @overload
    def InsertBefore(self,theOther : IntTools_ListOfSurfaceRangeSample,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : IntTools_SurfaceRangeSample,theIter : Any) -> IntTools_SurfaceRangeSample: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> IntTools_SurfaceRangeSample: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : IntTools_SurfaceRangeSample) -> IntTools_SurfaceRangeSample: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : IntTools_ListOfSurfaceRangeSample) -> None: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self,theOther : IntTools_ListOfSurfaceRangeSample) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IntTools_MapOfCurveSample(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : IntTools_CurveRangeSample) -> bool: 
        """
        Add
        """
    def Added(self,K : IntTools_CurveRangeSample) -> IntTools_CurveRangeSample: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : IntTools_MapOfCurveSample) -> IntTools_MapOfCurveSample: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def Contains(self,theOther : IntTools_MapOfCurveSample) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : IntTools_CurveRangeSample) -> bool: ...
    def Differ(self,theOther : IntTools_MapOfCurveSample) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : IntTools_MapOfCurveSample,theRight : IntTools_MapOfCurveSample) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : IntTools_MapOfCurveSample) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : IntTools_MapOfCurveSample) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : IntTools_MapOfCurveSample) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : IntTools_MapOfCurveSample,theRight : IntTools_MapOfCurveSample) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : IntTools_MapOfCurveSample) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : IntTools_CurveRangeSample) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : IntTools_MapOfCurveSample) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : IntTools_MapOfCurveSample,theRight : IntTools_MapOfCurveSample) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : IntTools_MapOfCurveSample,theRight : IntTools_MapOfCurveSample) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : IntTools_MapOfCurveSample) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_MapOfCurveSample) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class IntTools_MapOfSurfaceSample(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : IntTools_SurfaceRangeSample) -> bool: 
        """
        Add
        """
    def Added(self,K : IntTools_SurfaceRangeSample) -> IntTools_SurfaceRangeSample: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : IntTools_MapOfSurfaceSample) -> IntTools_MapOfSurfaceSample: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,theOther : IntTools_MapOfSurfaceSample) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : IntTools_SurfaceRangeSample) -> bool: ...
    def Differ(self,theOther : IntTools_MapOfSurfaceSample) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : IntTools_MapOfSurfaceSample,theRight : IntTools_MapOfSurfaceSample) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : IntTools_MapOfSurfaceSample) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : IntTools_MapOfSurfaceSample) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : IntTools_MapOfSurfaceSample) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : IntTools_MapOfSurfaceSample,theRight : IntTools_MapOfSurfaceSample) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : IntTools_MapOfSurfaceSample) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : IntTools_SurfaceRangeSample) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : IntTools_MapOfSurfaceSample) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : IntTools_MapOfSurfaceSample,theRight : IntTools_MapOfSurfaceSample) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : IntTools_MapOfSurfaceSample,theRight : IntTools_MapOfSurfaceSample) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : IntTools_MapOfSurfaceSample) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_MapOfSurfaceSample) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class IntTools_MarkedRangeSet():
    """
    class MarkedRangeSet provides continuous set of ranges marked with flags
    """
    def Flag(self,theIndex : int) -> int: 
        """
        Returns flag of the range with index theIndex
        """
    @overload
    def GetIndex(self,theValue : float,UseLower : bool) -> int: 
        """
        Returns index of range which contains theValue. If theValue do not belong any range returns 0.

        Returns index of range which contains theValue If theValue do not belong any range returns 0. If UseLower is Standard_True then lower boundary of the range can be equal to theValue, otherwise upper boundary of the range can be equal to theValue.
        """
    @overload
    def GetIndex(self,theValue : float) -> int: ...
    def GetIndices(self,theValue : float) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        None
        """
    @overload
    def InsertRange(self,theRange : IntTools_Range,theFlag : int) -> bool: 
        """
        Inserts a new range marked with flag theFlag It replace the existing ranges or parts of ranges and their flags. Returns True if the range is inside the initial boundaries, otherwise or in case of some error returns False

        Inserts a new range marked with flag theFlag It replace the existing ranges or parts of ranges and their flags. Returns True if the range is inside the initial boundaries, otherwise or in case of some error returns False

        Inserts a new range marked with flag theFlag It replace the existing ranges or parts of ranges and their flags. The index theIndex is a position where the range will be inserted. Returns True if the range is inside the initial boundaries, otherwise or in case of some error returns False

        Inserts a new range marked with flag theFlag It replace the existing ranges or parts of ranges and their flags. The index theIndex is a position where the range will be inserted. Returns True if the range is inside the initial boundaries, otherwise or in case of some error returns False
        """
    @overload
    def InsertRange(self,theFirstBoundary : float,theLastBoundary : float,theFlag : int,theIndex : int) -> bool: ...
    @overload
    def InsertRange(self,theRange : IntTools_Range,theFlag : int,theIndex : int) -> bool: ...
    @overload
    def InsertRange(self,theFirstBoundary : float,theLastBoundary : float,theFlag : int) -> bool: ...
    def Length(self) -> int: 
        """
        Returns number of ranges

        Returns number of ranges
        """
    def Range(self,theIndex : int) -> IntTools_Range: 
        """
        Returns the range with index theIndex. the Index can be from 1 to Length()
        """
    def SetBoundaries(self,theFirstBoundary : float,theLastBoundary : float,theInitFlag : int) -> None: 
        """
        build set of ranges which consists of one range with boundary values theFirstBoundary and theLastBoundary
        """
    def SetFlag(self,theIndex : int,theFlag : int) -> None: 
        """
        Set flag theFlag for range with index theIndex
        """
    def SetRanges(self,theSortedArray : IntTools_CArray1OfReal,theInitFlag : int) -> None: 
        """
        Build set of ranges based on the array of progressive sorted values
        """
    @overload
    def __init__(self,theSortedArray : IntTools_CArray1OfReal,theInitFlag : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theFirstBoundary : float,theLastBoundary : float,theInitFlag : int) -> None: ...
    pass
class IntTools_PntOn2Faces():
    """
    Contains two points PntOnFace from IntTools and a flag
    """
    def IsValid(self) -> bool: 
        """
        Selector
        """
    def P1(self) -> IntTools_PntOnFace: 
        """
        Selector
        """
    def P2(self) -> IntTools_PntOnFace: 
        """
        Selector
        """
    def SetP1(self,aP1 : IntTools_PntOnFace) -> None: 
        """
        Modifier
        """
    def SetP2(self,aP2 : IntTools_PntOnFace) -> None: 
        """
        Modifier
        """
    def SetValid(self,bF : bool) -> None: 
        """
        Modifier
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aP1 : IntTools_PntOnFace,aP2 : IntTools_PntOnFace) -> None: ...
    pass
class IntTools_PntOnFace():
    """
    Contains a Face, a 3d point, corresponded UV parameters and a flag
    """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Selector
        """
    def Init(self,aF : OCP.TopoDS.TopoDS_Face,aP : OCP.gp.gp_Pnt,U : float,V : float) -> None: 
        """
        Initializes me by aFace, a 3d point and it's UV parameters on face
        """
    def Parameters(self) -> Tuple[float, float]: 
        """
        Selector
        """
    def Pnt(self) -> OCP.gp.gp_Pnt: 
        """
        Selector
        """
    def SetFace(self,aF : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Modifier
        """
    def SetParameters(self,U : float,V : float) -> None: 
        """
        Modifier
        """
    def SetPnt(self,aP : OCP.gp.gp_Pnt) -> None: 
        """
        Modifier
        """
    def SetValid(self,bF : bool) -> None: 
        """
        Modifier
        """
    def Valid(self) -> bool: 
        """
        Selector
        """
    def __init__(self) -> None: ...
    pass
class IntTools_Range():
    """
    The class describes the 1-d range [myFirst, myLast].
    """
    def First(self) -> float: 
        """
        Selector
        """
    def Last(self) -> float: 
        """
        Selector
        """
    def Range(self) -> Tuple[float, float]: 
        """
        Selector
        """
    def SetFirst(self,aFirst : float) -> None: 
        """
        Modifier
        """
    def SetLast(self,aLast : float) -> None: 
        """
        Modifier
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aFirst : float,aLast : float) -> None: ...
    pass
class IntTools_Root():
    """
    The class is to describe the root of function of one variable for Edge/Edge and Edge/Surface algorithms.
    """
    def Interval(self) -> Tuple[float, float, float, float]: 
        """
        Returns the values of interval from which the Root was found [t1,t2] and the corresponding values of the function on the bounds f(t1), f(t2).
        """
    def IsValid(self) -> bool: 
        """
        Returns the validity flag for the root, True if myStateBefore==TopAbs_OUT && myStateAfter==TopAbs_IN or myStateBefore==TopAbs_OUT && myStateAfter==TopAbs_ON or myStateBefore==TopAbs_ON && myStateAfter==TopAbs_OUT or myStateBefore==TopAbs_IN && myStateAfter==TopAbs_OUT . For other cases it returns False.
        """
    def LayerHeight(self) -> float: 
        """
        Not used in Edge/Edge algorithm
        """
    def Root(self) -> float: 
        """
        Returns the Root value
        """
    def SetInterval(self,t1 : float,t2 : float,f1 : float,f2 : float) -> None: 
        """
        Sets the interval from which the Root was found [t1,t2] and the corresponding values of the function on the bounds f(t1), f(t2).
        """
    def SetLayerHeight(self,aHeight : float) -> None: 
        """
        Not used in Edge/Edge algorithm
        """
    def SetRoot(self,aRoot : float) -> None: 
        """
        Sets the Root's value
        """
    def SetStateAfter(self,aState : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Set the value of the state after the root (at t=Root-dt)
        """
    def SetStateBefore(self,aState : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Set the value of the state before the root (at t=Root-dt)
        """
    def SetType(self,aType : int) -> None: 
        """
        Sets the Root's Type
        """
    def StateAfter(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the state after the root
        """
    def StateBefore(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the state before the root
        """
    def Type(self) -> int: 
        """
        Returns the type of the root =0 - Simple (was found by bisection method); =2 - Smart when f1=0, f2!=0 or vice versa (was found by Fibbonacci method); =1 - Pure (pure zero for all t [t1,t2] );
        """
    @overload
    def __init__(self,aRoot : float,aType : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntTools_SequenceOfCommonPrts(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : IntTools_SequenceOfCommonPrts) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : IntTools_CommonPrt) -> None: ...
    def Assign(self,theOther : IntTools_SequenceOfCommonPrts) -> IntTools_SequenceOfCommonPrts: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntTools_CommonPrt: 
        """
        First item access
        """
    def ChangeLast(self) -> IntTools_CommonPrt: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntTools_CommonPrt: 
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
    def First(self) -> IntTools_CommonPrt: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntTools_SequenceOfCommonPrts) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntTools_CommonPrt) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntTools_SequenceOfCommonPrts) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntTools_CommonPrt) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntTools_CommonPrt: 
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
    def Prepend(self,theSeq : IntTools_SequenceOfCommonPrts) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntTools_CommonPrt) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntTools_CommonPrt) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntTools_SequenceOfCommonPrts) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntTools_CommonPrt: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : IntTools_SequenceOfCommonPrts) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntTools_SequenceOfCurves(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : IntTools_SequenceOfCurves) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : IntTools_Curve) -> None: ...
    def Assign(self,theOther : IntTools_SequenceOfCurves) -> IntTools_SequenceOfCurves: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntTools_Curve: 
        """
        First item access
        """
    def ChangeLast(self) -> IntTools_Curve: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntTools_Curve: 
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
    def First(self) -> IntTools_Curve: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntTools_Curve) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntTools_SequenceOfCurves) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntTools_SequenceOfCurves) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntTools_Curve) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntTools_Curve: 
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
    def Prepend(self,theSeq : IntTools_SequenceOfCurves) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntTools_Curve) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntTools_Curve) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntTools_SequenceOfCurves) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntTools_Curve: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_SequenceOfCurves) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntTools_SequenceOfPntOn2Faces(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntTools_PntOn2Faces) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntTools_SequenceOfPntOn2Faces) -> None: ...
    def Assign(self,theOther : IntTools_SequenceOfPntOn2Faces) -> IntTools_SequenceOfPntOn2Faces: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntTools_PntOn2Faces: 
        """
        First item access
        """
    def ChangeLast(self) -> IntTools_PntOn2Faces: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntTools_PntOn2Faces: 
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
    def First(self) -> IntTools_PntOn2Faces: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntTools_PntOn2Faces) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntTools_SequenceOfPntOn2Faces) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntTools_SequenceOfPntOn2Faces) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntTools_PntOn2Faces) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntTools_PntOn2Faces: 
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
    def Prepend(self,theItem : IntTools_PntOn2Faces) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : IntTools_SequenceOfPntOn2Faces) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntTools_PntOn2Faces) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntTools_SequenceOfPntOn2Faces) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntTools_PntOn2Faces: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_SequenceOfPntOn2Faces) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntTools_SequenceOfRanges(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntTools_Range) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntTools_SequenceOfRanges) -> None: ...
    def Assign(self,theOther : IntTools_SequenceOfRanges) -> IntTools_SequenceOfRanges: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntTools_Range: 
        """
        First item access
        """
    def ChangeLast(self) -> IntTools_Range: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntTools_Range: 
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
    def First(self) -> IntTools_Range: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntTools_SequenceOfRanges) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntTools_Range) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntTools_Range) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntTools_SequenceOfRanges) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntTools_Range: 
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
    def Prepend(self,theSeq : IntTools_SequenceOfRanges) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntTools_Range) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntTools_Range) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntTools_SequenceOfRanges) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntTools_Range: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_SequenceOfRanges) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntTools_SequenceOfRoots(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntTools_Root) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntTools_SequenceOfRoots) -> None: ...
    def Assign(self,theOther : IntTools_SequenceOfRoots) -> IntTools_SequenceOfRoots: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntTools_Root: 
        """
        First item access
        """
    def ChangeLast(self) -> IntTools_Root: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntTools_Root: 
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
    def First(self) -> IntTools_Root: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntTools_Root) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntTools_SequenceOfRoots) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntTools_Root) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntTools_SequenceOfRoots) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntTools_Root: 
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
    def Prepend(self,theItem : IntTools_Root) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : IntTools_SequenceOfRoots) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntTools_Root) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntTools_SequenceOfRoots) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntTools_Root: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntTools_SequenceOfRoots) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntTools_ShrunkRange():
    """
    The class provides the computation of a working (shrunk) range [t1, t2] for the 3D-curve of the edge.
    """
    def BndBox(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def Context(self) -> IntTools_Context: 
        """
        None
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        Returns TRUE in case the shrunk range is computed
        """
    def IsSplittable(self) -> bool: 
        """
        Returns FALSE in case the shrunk range is too short and the edge cannot be split, otherwise returns TRUE
        """
    def Length(self) -> float: 
        """
        Returns the length of the edge if computed.
        """
    def Perform(self) -> None: 
        """
        None
        """
    def SetContext(self,aCtx : IntTools_Context) -> None: 
        """
        None
        """
    def SetData(self,aE : OCP.TopoDS.TopoDS_Edge,aT1 : float,aT2 : float,aV1 : OCP.TopoDS.TopoDS_Vertex,aV2 : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None
        """
    def SetShrunkRange(self,aT1 : float,aT2 : float) -> None: 
        """
        None
        """
    def ShrunkRange(self) -> Tuple[float, float]: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IntTools_SurfaceRangeLocalizeData():
    """
    None
    """
    def AddBox(self,theRange : IntTools_SurfaceRangeSample,theBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        None
        """
    def AddOutRange(self,theRange : IntTools_SurfaceRangeSample) -> None: 
        """
        None
        """
    def Assign(self,Other : IntTools_SurfaceRangeLocalizeData) -> IntTools_SurfaceRangeLocalizeData: 
        """
        None
        """
    def ClearGrid(self) -> None: 
        """
        Clears the grid of points.
        """
    def FindBox(self,theRange : IntTools_SurfaceRangeSample,theBox : OCP.Bnd.Bnd_Box) -> bool: 
        """
        None
        """
    def GetGridDeflection(self) -> float: 
        """
        Query the grid deflection.

        Query the grid deflection.
        """
    def GetGridPoint(self,theUIndex : int,theVIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Set the grid point.

        Set the grid point.
        """
    def GetMinRangeU(self) -> float: 
        """
        None

        None
        """
    def GetMinRangeV(self) -> float: 
        """
        None

        None
        """
    def GetNBUPointsInFrame(self) -> int: 
        """
        Returns the number of grid points on U direction in frame.

        Returns the number of grid points on U direction in frame.
        """
    def GetNBVPointsInFrame(self) -> int: 
        """
        Returns the number of grid points on V direction in frame.

        Returns the number of grid points on V direction in frame.
        """
    def GetNbSampleU(self) -> int: 
        """
        None

        None
        """
    def GetNbSampleV(self) -> int: 
        """
        None

        None
        """
    def GetPointInFrame(self,theUIndex : int,theVIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the grid point in frame.
        """
    def GetRangeUGrid(self) -> int: 
        """
        Query the range U of the grid of points.

        Query the range U of the grid of points.
        """
    def GetRangeVGrid(self) -> int: 
        """
        Query the range V of the grid of points.

        Query the range V of the grid of points.
        """
    def GetUParam(self,theIndex : int) -> float: 
        """
        Query the U parameter of the grid points at that index.

        Query the U parameter of the grid points at that index.
        """
    def GetUParamInFrame(self,theIndex : int) -> float: 
        """
        Query the U parameter of the grid points at that index in frame.
        """
    def GetVParam(self,theIndex : int) -> float: 
        """
        Query the V parameter of the grid points at that index.

        Query the V parameter of the grid points at that index.
        """
    def GetVParamInFrame(self,theIndex : int) -> float: 
        """
        Query the V parameter of the grid points at that index in frame.
        """
    def IsRangeOut(self,theRange : IntTools_SurfaceRangeSample) -> bool: 
        """
        None
        """
    def ListRangeOut(self,theList : IntTools_ListOfSurfaceRangeSample) -> None: 
        """
        None
        """
    def RemoveRangeOutAll(self) -> None: 
        """
        None
        """
    def SetFrame(self,theUMin : float,theUMax : float,theVMin : float,theVMax : float) -> None: 
        """
        Sets the frame area. Used to work with grid points.
        """
    def SetGridDeflection(self,theDeflection : float) -> None: 
        """
        Set the grid deflection.

        Set the grid deflection.
        """
    def SetGridPoint(self,theUIndex : int,theVIndex : int,thePoint : OCP.gp.gp_Pnt) -> None: 
        """
        Set the grid point.

        Set the grid point.
        """
    def SetRangeUGrid(self,theNbUGrid : int) -> None: 
        """
        Set the range U of the grid of points.
        """
    def SetRangeVGrid(self,theNbVGrid : int) -> None: 
        """
        Set the range V of the grid of points.
        """
    def SetUParam(self,theIndex : int,theUParam : float) -> None: 
        """
        Set the U parameter of the grid points at that index.

        Set the U parameter of the grid points at that index.
        """
    def SetVParam(self,theIndex : int,theVParam : float) -> None: 
        """
        Set the V parameter of the grid points at that index.

        Set the V parameter of the grid points at that index.
        """
    @overload
    def __init__(self,theNbSampleU : int,theNbSampleV : int,theMinRangeU : float,theMinRangeV : float) -> None: ...
    @overload
    def __init__(self,Other : IntTools_SurfaceRangeLocalizeData) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntTools_SurfaceRangeSample():
    """
    class for range index management of surface
    """
    def Assign(self,Other : IntTools_SurfaceRangeSample) -> IntTools_SurfaceRangeSample: 
        """
        None
        """
    def GetDepthU(self) -> int: 
        """
        None

        None
        """
    def GetDepthV(self) -> int: 
        """
        None

        None
        """
    def GetDepths(self) -> Tuple[int, int]: 
        """
        None

        None
        """
    def GetIndexU(self) -> int: 
        """
        None

        None
        """
    def GetIndexV(self) -> int: 
        """
        None

        None
        """
    def GetIndexes(self) -> Tuple[int, int]: 
        """
        None

        None
        """
    def GetRangeIndexUDeeper(self,theNbSampleU : int) -> int: 
        """
        None

        None
        """
    def GetRangeIndexVDeeper(self,theNbSampleV : int) -> int: 
        """
        None

        None
        """
    def GetRangeU(self,theFirstU : float,theLastU : float,theNbSampleU : int) -> IntTools_Range: 
        """
        None
        """
    def GetRangeV(self,theFirstV : float,theLastV : float,theNbSampleV : int) -> IntTools_Range: 
        """
        None
        """
    def GetRanges(self,theRangeU : IntTools_CurveRangeSample,theRangeV : IntTools_CurveRangeSample) -> None: 
        """
        None

        None
        """
    def GetSampleRangeU(self) -> IntTools_CurveRangeSample: 
        """
        None

        None
        """
    def GetSampleRangeV(self) -> IntTools_CurveRangeSample: 
        """
        None

        None
        """
    def IsEqual(self,Other : IntTools_SurfaceRangeSample) -> bool: 
        """
        None

        None
        """
    def SetDepthU(self,theDepthU : int) -> None: 
        """
        None

        None
        """
    def SetDepthV(self,theDepthV : int) -> None: 
        """
        None

        None
        """
    def SetIndexU(self,theIndexU : int) -> None: 
        """
        None

        None
        """
    def SetIndexV(self,theIndexV : int) -> None: 
        """
        None

        None
        """
    def SetIndexes(self,theIndexU : int,theIndexV : int) -> None: 
        """
        None

        None
        """
    def SetRanges(self,theRangeU : IntTools_CurveRangeSample,theRangeV : IntTools_CurveRangeSample) -> None: 
        """
        None

        None
        """
    def SetSampleRangeU(self,theRangeSampleU : IntTools_CurveRangeSample) -> None: 
        """
        None

        None
        """
    def SetSampleRangeV(self,theRangeSampleV : IntTools_CurveRangeSample) -> None: 
        """
        None

        None
        """
    @overload
    def __init__(self,Other : IntTools_SurfaceRangeSample) -> None: ...
    @overload
    def __init__(self,theIndexU : int,theDepthU : int,theIndexV : int,theDepthV : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theRangeU : IntTools_CurveRangeSample,theRangeV : IntTools_CurveRangeSample) -> None: ...
    pass
class IntTools_SurfaceRangeSampleMapHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(theKey : IntTools_SurfaceRangeSample,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(S1 : IntTools_SurfaceRangeSample,S2 : IntTools_SurfaceRangeSample) -> bool: 
        """
        Returns True when the two keys are the same. Two same keys must have the same hashcode, the contrary is not necessary.
        """
    def __init__(self) -> None: ...
    pass
class IntTools_Tools():
    """
    The class contains handy static functions dealing with the geometry and topology.
    """
    @staticmethod
    def CheckCurve_s(theCurve : IntTools_Curve,theBox : OCP.Bnd.Bnd_Box) -> bool: 
        """
        Checks if the curve is not covered by the default tolerance (confusion). Builds bounding box for the curve and stores it into <theBox>.
        """
    @staticmethod
    def ClassifyPointByFace_s(aF : OCP.TopoDS.TopoDS_Face,P : OCP.gp.gp_Pnt2d) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    @staticmethod
    def ComputeIntRange_s(theTol1 : float,theTol2 : float,theAngle : float) -> float: 
        """
        Computes the correct Intersection range for Line/Line, Line/Plane and Plane/Plane intersections
        """
    @staticmethod
    def ComputeTolerance_s(theCurve3D : OCP.Geom.Geom_Curve,theCurve2D : OCP.Geom2d.Geom2d_Curve,theSurf : OCP.Geom.Geom_Surface,theFirst : float,theLast : float,theMaxDist : float,theMaxPar : float,theTolRange : float=9.999999999999999e-10) -> bool: 
        """
        Computes the max distance between points taken from 3D and 2D curves by the same parameter
        """
    @staticmethod
    def ComputeVV_s(V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> int: 
        """
        Computes distance between vertex V1 and vertex V2, if the distance is less than sum of vertex tolerances returns zero, otherwise returns negative value
        """
    @staticmethod
    def CurveTolerance_s(aC : OCP.Geom.Geom_Curve,aTolBase : float) -> float: 
        """
        Returns adaptive tolerance for given aTolBase if aC is trimmed curve and basis curve is parabola, otherwise returns value of aTolBase
        """
    @staticmethod
    def HasInternalEdge_s(aW : OCP.TopoDS.TopoDS_Wire) -> bool: 
        """
        Returns True if wire aW contains edges with INTERNAL orientation
        """
    @staticmethod
    def IntermediatePoint_s(aFirst : float,aLast : float) -> float: 
        """
        Returns some value between aFirst and aLast
        """
    @staticmethod
    def IsClosed_s(aC : OCP.Geom.Geom_Curve) -> bool: 
        """
        Returns True if aC is BoundedCurve from Geom and the distance between first point of the curve aC and last point is less than 1.e-12
        """
    @staticmethod
    @overload
    def IsDirsCoinside_s(D1 : OCP.gp.gp_Dir,D2 : OCP.gp.gp_Dir,aTol : float) -> bool: 
        """
        Returns True if D1 and D2 coinside

        Returns True if D1 and D2 coinside with given tolerance
        """
    @staticmethod
    @overload
    def IsDirsCoinside_s(D1 : OCP.gp.gp_Dir,D2 : OCP.gp.gp_Dir) -> bool: ...
    @staticmethod
    def IsInRange_s(theRRef : IntTools_Range,theR : IntTools_Range,theTol : float) -> bool: 
        """
        Checks if the range <theR> interfere with the range <theRRef>
        """
    @staticmethod
    def IsMiddlePointsEqual_s(E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Gets boundary of parameters of E1 and E2. Computes 3d points on each corresponded to average parameters. Returns True if distance between computed points is less than sum of edge tolerance, otherwise returns False.
        """
    @staticmethod
    def IsOnPave1_s(theT : float,theRange : IntTools_Range,theTol : float) -> bool: 
        """
        None
        """
    @staticmethod
    def IsOnPave_s(theT : float,theRange : IntTools_Range,theTol : float) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def IsVertex_s(aCmnPrt : IntTools_CommonPrt) -> bool: 
        """
        Computes square distance between a point on the edge E corresponded to parameter t and vertices of edge E. Returns True if this distance is less than square tolerance of vertex, otherwise returns false.

        Returns True if square distance between vertex V and a point on the edge E corresponded to parameter t is less than square tolerance of V

        Returns True if IsVertx for middle parameter of fist range and first edge returns True and if IsVertex for middle parameter of second range and second range returns True, otherwise returns False

        Returns True if the distance between point aP and vertex aV is less or equal to sum of aTolPV and vertex tolerance, otherwise returns False
        """
    @staticmethod
    @overload
    def IsVertex_s(E : OCP.TopoDS.TopoDS_Edge,t : float) -> bool: ...
    @staticmethod
    @overload
    def IsVertex_s(aP : OCP.gp.gp_Pnt,aTolPV : float,aV : OCP.TopoDS.TopoDS_Vertex) -> bool: ...
    @staticmethod
    @overload
    def IsVertex_s(E : OCP.TopoDS.TopoDS_Edge,V : OCP.TopoDS.TopoDS_Vertex,t : float) -> bool: ...
    @staticmethod
    def MakeFaceFromWireAndFace_s(aW : OCP.TopoDS.TopoDS_Wire,aF : OCP.TopoDS.TopoDS_Face,aFNew : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Build a face based on surface of given face aF and bounded by wire aW
        """
    @staticmethod
    def RejectLines_s(aSIn : IntTools_SequenceOfCurves,aSOut : IntTools_SequenceOfCurves) -> None: 
        """
        Puts curves from aSIn to aSOut except those curves that are coincide with first curve from aSIn.
        """
    @staticmethod
    def SegPln_s(theLin : OCP.gp.gp_Lin,theTLin1 : float,theTLin2 : float,theTolLin : float,thePln : OCP.gp.gp_Pln,theTolPln : float,theP : OCP.gp.gp_Pnt,theT : float,theTolP : float,theTmin : float,theTmax : float) -> int: 
        """
        None
        """
    @staticmethod
    def SplitCurve_s(aC : IntTools_Curve,aS : IntTools_SequenceOfCurves) -> int: 
        """
        Split aC by average parameter if aC is closed in 3D. Returns positive value if splitting has been done, otherwise returns zero.
        """
    @staticmethod
    def VertexParameter_s(theCP : IntTools_CommonPrt) -> Tuple[float]: 
        """
        None
        """
    @staticmethod
    def VertexParameters_s(theCP : IntTools_CommonPrt) -> Tuple[float, float]: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IntTools_TopolTool(OCP.Adaptor3d.Adaptor3d_TopolTool, OCP.Standard.Standard_Transient):
    """
    Class redefine methods of TopolTool from Adaptor3d concerning sample pointsClass redefine methods of TopolTool from Adaptor3d concerning sample pointsClass redefine methods of TopolTool from Adaptor3d concerning sample points
    """
    def BSplSamplePnts(self,theDefl : float,theNUmin : int,theNVmin : int) -> None: 
        """
        compute the sample-points for the intersections algorithms by adaptive algorithm for BSpline surfaces - is used in SamplePnts theDefl is a requred deflection theNUmin, theNVmin are minimal nb points for U and V.
        """
    def Classify(self,P : OCP.gp.gp_Pnt2d,Tol : float,ReacdreOnPeriodic : bool=True) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def ComputeSamplePoints(self) -> None: 
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
    def DomainIsInfinite(self) -> bool: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self) -> capsule: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Has3d(self) -> bool: 
        """
        answers if arcs and vertices may have 3d representations, so that we could use Tol3d and Pnt methods.
        """
    def Identical(self,V1 : OCP.Adaptor3d.Adaptor3d_HVertex,V2 : OCP.Adaptor3d.Adaptor3d_HVertex) -> bool: 
        """
        Returns True if the vertices V1 and V2 are identical. This method does not take the orientation of the vertices in account.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        None
        """
    def InitVertexIterator(self) -> None: 
        """
        None
        """
    @overload
    def Initialize(self,theSurface : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: 
        """
        Redefined empty initializer

        Initializes me by surface
        """
    @overload
    def Initialize(self) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsThePointOn(self,P : OCP.gp.gp_Pnt2d,Tol : float,ReacdreOnPeriodic : bool=True) -> bool: 
        """
        None
        """
    def IsUniformSampling(self) -> bool: 
        """
        Returns true if provide uniform sampling of points.
        """
    def More(self) -> bool: 
        """
        None
        """
    def MoreVertex(self) -> bool: 
        """
        None
        """
    def NbSamples(self) -> int: 
        """
        Computes the sample-points for the intersections algorithms
        """
    def NbSamplesU(self) -> int: 
        """
        Computes the sample-points for the intersections algorithms
        """
    def NbSamplesV(self) -> int: 
        """
        Computes the sample-points for the intersections algorithms
        """
    def Next(self) -> None: 
        """
        None
        """
    def NextVertex(self) -> None: 
        """
        None
        """
    @overload
    def Orientation(self,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        If the function returns the orientation of the arc. If the orientation is FORWARD or REVERSED, the arc is a "real" limit of the surface. If the orientation is INTERNAL or EXTERNAL, the arc is considered as an arc on the surface.

        Returns the orientation of the vertex V. The vertex has been found with an exploration on a given arc. The orientation is the orientation of the vertex on this arc.
        """
    @overload
    def Orientation(self,C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.TopAbs.TopAbs_Orientation: ...
    def Pnt(self,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> OCP.gp.gp_Pnt: 
        """
        returns 3d point of the vertex V
        """
    def SamplePnts(self,theDefl : float,theNUmin : int,theNVmin : int) -> None: 
        """
        compute the sample-points for the intersections algorithms by adaptive algorithm for BSpline surfaces. For other surfaces algorithm is the same as in method ComputeSamplePoints(), but only fill arrays of U and V sample parameters; theDefl is a requred deflection theNUmin, theNVmin are minimal nb points for U and V.
        """
    def SamplePoint(self,Index : int,P2d : OCP.gp.gp_Pnt2d,P3d : OCP.gp.gp_Pnt) -> None: 
        """
        Returns a 2d point from surface myS and a corresponded 3d point for given index. The index should be from 1 to NbSamples()
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tol3d(self,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> float: 
        """
        returns 3d tolerance of the arc C

        returns 3d tolerance of the vertex V
        """
    @overload
    def Tol3d(self,C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: ...
    def UParameters(self,theArray : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        return the set of U parameters on the surface obtained by the method SamplePnts
        """
    def VParameters(self,theArray : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        return the set of V parameters on the surface obtained by the method SamplePnts
        """
    def Value(self) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        None
        """
    def Vertex(self) -> OCP.Adaptor3d.Adaptor3d_HVertex: 
        """
        None
        """
    @overload
    def __init__(self,theSurface : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: ...
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
class IntTools_WLineTool():
    """
    IntTools_WLineTool provides set of static methods related to walking lines.
    """
    @staticmethod
    def DecompositionOfWLine_s(theWLine : OCP.IntPatch.IntPatch_WLine,theSurface1 : OCP.GeomAdaptor.GeomAdaptor_HSurface,theSurface2 : OCP.GeomAdaptor.GeomAdaptor_HSurface,theFace1 : OCP.TopoDS.TopoDS_Face,theFace2 : OCP.TopoDS.TopoDS_Face,theLConstructor : OCP.GeomInt.GeomInt_LineConstructor,theAvoidLConstructor : bool,theTol : float,theNewLines : OCP.IntPatch.IntPatch_SequenceOfLine,theReachedTol3d : float,arg10 : IntTools_Context) -> bool: 
        """
        None
        """
    @staticmethod
    def NotUseSurfacesForApprox_s(aF1 : OCP.TopoDS.TopoDS_Face,aF2 : OCP.TopoDS.TopoDS_Face,WL : OCP.IntPatch.IntPatch_WLine,ifprm : int,ilprm : int) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
