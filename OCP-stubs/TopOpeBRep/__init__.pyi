import OCP.TopOpeBRep
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IntRes2d
import OCP.Bnd
import OCP.TopTools
import OCP.gp
import OCP.Geom2dAdaptor
import OCP.Geom
import OCP.TopoDS
import OCP.NCollection
import OCP.TCollection
import OCP.TopAbs
import OCP.Geom2d
import OCP.BRepAdaptor
import OCP.Standard
import OCP.IntSurf
import OCP.TopOpeBRepTool
import OCP.IntPatch
import OCP.TopOpeBRepDS
__all__  = [
"TopOpeBRep",
"TopOpeBRep_Array1OfLineInter",
"TopOpeBRep_Array1OfVPointInter",
"TopOpeBRep_Bipoint",
"TopOpeBRep_DSFiller",
"TopOpeBRep_EdgesFiller",
"TopOpeBRep_EdgesIntersector",
"TopOpeBRep_FFDumper",
"TopOpeBRep_FFTransitionTool",
"TopOpeBRep_FaceEdgeFiller",
"TopOpeBRep_FaceEdgeIntersector",
"TopOpeBRep_FacesFiller",
"TopOpeBRep_FacesIntersector",
"TopOpeBRep_GeomTool",
"TopOpeBRep_HArray1OfLineInter",
"TopOpeBRep_HArray1OfVPointInter",
"TopOpeBRep_Hctxee2d",
"TopOpeBRep_Hctxff2d",
"TopOpeBRep_LineInter",
"TopOpeBRep_ListOfBipoint",
"TopOpeBRep_P2Dstatus",
"TopOpeBRep_Point2d",
"TopOpeBRep_PointClassifier",
"TopOpeBRep_PointGeomTool",
"TopOpeBRep_SequenceOfPoint2d",
"TopOpeBRep_ShapeIntersector",
"TopOpeBRep_ShapeIntersector2d",
"TopOpeBRep_ShapeScanner",
"TopOpeBRep_TypeLineCurve",
"TopOpeBRep_VPointInter",
"TopOpeBRep_VPointInterClassifier",
"TopOpeBRep_VPointInterIterator",
"TopOpeBRep_WPointInter",
"TopOpeBRep_WPointInterIterator",
"TopOpeBRep_ANALYTIC",
"TopOpeBRep_CIRCLE",
"TopOpeBRep_ELLIPSE",
"TopOpeBRep_HYPERBOLA",
"TopOpeBRep_LINE",
"TopOpeBRep_OTHERTYPE",
"TopOpeBRep_P2DINT",
"TopOpeBRep_P2DNEW",
"TopOpeBRep_P2DSGF",
"TopOpeBRep_P2DSGL",
"TopOpeBRep_P2DUNK",
"TopOpeBRep_PARABOLA",
"TopOpeBRep_RESTRICTION",
"TopOpeBRep_WALKING"
]
class TopOpeBRep():
    """
    This package provides the topological operations on the BRep data structure.
    """
    @staticmethod
    def Print_s(TLC : TopOpeBRep_TypeLineCurve,OS : Any) -> Any: 
        """
        Prints the name of <TLC> as a String on the Stream <S> and returns <S>.
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_Array1OfLineInter():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TopOpeBRep_Array1OfLineInter) -> TopOpeBRep_Array1OfLineInter: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> TopOpeBRep_LineInter: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TopOpeBRep_LineInter: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TopOpeBRep_LineInter: 
        """
        Variable value access
        """
    def First(self) -> TopOpeBRep_LineInter: 
        """
        Returns first element
        """
    def Init(self,theValue : TopOpeBRep_LineInter) -> None: 
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
    def Last(self) -> TopOpeBRep_LineInter: 
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
    def Move(self,theOther : TopOpeBRep_Array1OfLineInter) -> TopOpeBRep_Array1OfLineInter: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TopOpeBRep_LineInter) -> None: 
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
    def Value(self,theIndex : int) -> TopOpeBRep_LineInter: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : TopOpeBRep_LineInter,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRep_Array1OfLineInter) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TopOpeBRep_Array1OfVPointInter():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TopOpeBRep_Array1OfVPointInter) -> TopOpeBRep_Array1OfVPointInter: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> TopOpeBRep_VPointInter: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TopOpeBRep_VPointInter: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TopOpeBRep_VPointInter: 
        """
        Variable value access
        """
    def First(self) -> TopOpeBRep_VPointInter: 
        """
        Returns first element
        """
    def Init(self,theValue : TopOpeBRep_VPointInter) -> None: 
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
    def Last(self) -> TopOpeBRep_VPointInter: 
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
    def Move(self,theOther : TopOpeBRep_Array1OfVPointInter) -> TopOpeBRep_Array1OfVPointInter: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TopOpeBRep_VPointInter) -> None: 
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
    def Value(self,theIndex : int) -> TopOpeBRep_VPointInter: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : TopOpeBRep_VPointInter,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRep_Array1OfVPointInter) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TopOpeBRep_Bipoint():
    """
    None
    """
    def I1(self) -> int: 
        """
        None
        """
    def I2(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self,I1 : int,I2 : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_DSFiller():
    """
    Provides class methods to fill a datastructure with results of intersections.
    """
    def ChangeEdgesFiller(self) -> TopOpeBRep_EdgesFiller: 
        """
        None
        """
    def ChangeFaceEdgeFiller(self) -> TopOpeBRep_FaceEdgeFiller: 
        """
        None
        """
    def ChangeFacesFiller(self) -> TopOpeBRep_FacesFiller: 
        """
        None
        """
    def ChangeShapeIntersector(self) -> TopOpeBRep_ShapeIntersector: 
        """
        None
        """
    def ChangeShapeIntersector2d(self) -> TopOpeBRep_ShapeIntersector2d: 
        """
        None
        """
    def Checker(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        None
        """
    def Complete(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        None
        """
    def CompleteDS(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        Update the data structure with relevant informations deduced from the intersections.
        """
    def CompleteDS2d(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        Update the data structure with relevant informations deduced from the intersections 2d.
        """
    def Filter(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        None
        """
    def GapFiller(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        None
        """
    def Insert(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure,orientFORWARD : bool=True) -> None: 
        """
        Stores in <DS> the intersections of <S1> and <S2>. if orientFORWARD = True S FORWARD,REVERSED --> FORWARD S EXTERNAL,INTERNAL --> EXTERNAL,INTERNAL
        """
    def Insert1d(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure,orientFORWARD : bool=False) -> None: 
        """
        Stores in <DS> the intersections of <S1> and <S2>. S1 and S2 are edges or wires. S1 edges have a 2d representation in face F1 S2 edges have a 2d representation in face F2 F1 is the face which surface is taken as reference for 2d description of S1 and S2 edges. if orientFORWARD = True S FORWARD,REVERSED --> FORWARD S EXTERNAL,INTERNAL --> EXTERNAL,INTERNAL
        """
    def Insert2d(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        Stores in <DS> the intersections of <S1> and <S2>. S1 et S2 contain only SameDomain Face
        """
    def InsertIntersection(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure,orientFORWARD : bool=True) -> None: 
        """
        Stores in <DS> the intersections of <S1> and <S2>. if orientFORWARD = True S FORWAR,REVERSED --> FORWARD S EXTERNAL,INTERNAL --> EXTERNAL,INTERNAL
        """
    def InsertIntersection2d(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        S1, S2 set of tangent face lance les intersections 2d pour coder correctement les faces SameDomain.
        """
    def IsContext1d(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsMadeOf1d(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def Reducer(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        None
        """
    def RemoveUnsharedGeometry(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_EdgesFiller():
    """
    Fills a TopOpeBRepDS_DataStructure with Edge/Edge instersection data described by TopOpeBRep_EdgesIntersector.
    """
    @overload
    def Face(self,I : int,F : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def Face(self,I : int) -> OCP.TopoDS.TopoDS_Shape: ...
    def Insert(self,E1 : OCP.TopoDS.TopoDS_Shape,E2 : OCP.TopoDS.TopoDS_Shape,EI : TopOpeBRep_EdgesIntersector,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_EdgesIntersector():
    """
    Describes the intersection of two edges on the same surface
    """
    def Curve(self,Index : int) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        None
        """
    @overload
    def Dimension(self,D : int) -> None: 
        """
        None

        set working space dimension D = 1 for E &|| W, 2 for E in F
        """
    @overload
    def Dimension(self) -> int: ...
    def Dump(self,str : OCP.TCollection.TCollection_AsciiString,ie1 : int=0,ie2 : int=0) -> None: 
        """
        None
        """
    def Edge(self,Index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Face(self,Index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def FacesSameOriented(self) -> bool: 
        """
        None
        """
    def ForceTolerances(self,Tol1 : float,Tol2 : float) -> None: 
        """
        None
        """
    def HasSegment(self) -> bool: 
        """
        true if at least one intersection segment.
        """
    def InitPoint(self,selectkeep : bool=True) -> None: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def MorePoint(self) -> bool: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        None
        """
    def NbSegments(self) -> int: 
        """
        None
        """
    def NextPoint(self) -> None: 
        """
        None
        """
    def Perform(self,E1 : OCP.TopoDS.TopoDS_Shape,E2 : OCP.TopoDS.TopoDS_Shape,ReduceSegments : bool=True) -> None: 
        """
        None
        """
    @overload
    def Point(self) -> TopOpeBRep_Point2d: 
        """
        None

        None
        """
    @overload
    def Point(self,I : int) -> TopOpeBRep_Point2d: ...
    def Points(self) -> TopOpeBRep_SequenceOfPoint2d: 
        """
        None
        """
    def ReduceSegment(self,P1 : TopOpeBRep_Point2d,P2 : TopOpeBRep_Point2d,Pn : TopOpeBRep_Point2d) -> bool: 
        """
        None
        """
    def SameDomain(self) -> bool: 
        """
        = mySameDomain.
        """
    @overload
    def SetFaces(self,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def SetFaces(self,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape,B1 : OCP.Bnd.Bnd_Box,B2 : OCP.Bnd.Bnd_Box) -> None: ...
    def Status1(self) -> TopOpeBRep_P2Dstatus: 
        """
        None
        """
    def Surface(self,Index : int) -> OCP.BRepAdaptor.BRepAdaptor_Surface: 
        """
        None
        """
    def SurfacesSameOriented(self) -> bool: 
        """
        None
        """
    def ToleranceMax(self) -> float: 
        """
        None
        """
    def Tolerances(self) -> Tuple[float, float]: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_FFDumper(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpDSP(self,VP : TopOpeBRep_VPointInter,GK : OCP.TopOpeBRepDS.TopOpeBRepDS_Kind,G : int,newinDS : bool) -> None: 
        """
        None
        """
    @overload
    def DumpLine(self,I : int) -> None: 
        """
        None

        None
        """
    @overload
    def DumpLine(self,L : TopOpeBRep_LineInter) -> None: ...
    @overload
    def DumpVP(self,VP : TopOpeBRep_VPointInter,ISI : int) -> None: 
        """
        None

        None
        """
    @overload
    def DumpVP(self,VP : TopOpeBRep_VPointInter) -> None: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExploreIndex(self,S : OCP.TopoDS.TopoDS_Shape,ISI : int) -> int: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def PFacesFillerDummy(self) -> TopOpeBRep_FacesFiller: 
        """
        None
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
class TopOpeBRep_FFTransitionTool():
    """
    None
    """
    @staticmethod
    def ProcessEdgeONTransition_s(VP : TopOpeBRep_VPointInter,Index : int,R : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: 
        """
        compute transition on "IntPatch_Restriction line" edge <R> when crossing edge <E> of face <F> at point <VP>. VP is given on edge <E> of face <F> of index <Index> (1 or 2). <VP> has been classified by FacesFiller as TopAbs_ON an edge <R> of the other face than <F> of current (face/face) intersection. Transition depends on the orientation of E in F. This method should be provided by IntPatch_Line (NYI)
        """
    @staticmethod
    def ProcessEdgeTransition_s(P : TopOpeBRep_VPointInter,Index : int,LineOrientation : OCP.TopAbs.TopAbs_Orientation) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: 
        """
        None
        """
    @staticmethod
    def ProcessFaceTransition_s(L : TopOpeBRep_LineInter,Index : int,FaceOrientation : OCP.TopAbs.TopAbs_Orientation) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: 
        """
        None
        """
    @staticmethod
    @overload
    def ProcessLineTransition_s(P : TopOpeBRep_VPointInter,L : TopOpeBRep_LineInter) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def ProcessLineTransition_s(P : TopOpeBRep_VPointInter,Index : int,EdgeOrientation : OCP.TopAbs.TopAbs_Orientation) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: ...
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_FaceEdgeFiller():
    """
    None
    """
    def Insert(self,F : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape,FEINT : TopOpeBRep_FaceEdgeIntersector,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_FaceEdgeIntersector():
    """
    Describes the intersection of a face and an edge.
    """
    def ForceTolerance(self,tol : float) -> None: 
        """
        Force the tolerance values used by the next Perform(S1,S2) call.
        """
    def Index(self) -> int: 
        """
        trace only
        """
    def InitPoint(self) -> None: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    @overload
    def IsVertex(self,I : int,V : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        None

        None
        """
    @overload
    def IsVertex(self,S : OCP.TopoDS.TopoDS_Shape,P : OCP.gp.gp_Pnt,Tol : float,V : OCP.TopoDS.TopoDS_Vertex) -> bool: ...
    def MorePoint(self) -> bool: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        None
        """
    def NextPoint(self) -> None: 
        """
        None
        """
    def Parameter(self) -> float: 
        """
        parametre de Value() sur l'arete
        """
    def Perform(self,F : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Shape(self,Index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns intersected face or edge according to value of <Index> = 1 or 2
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        IN ou ON / a la face. Les points OUT ne sont pas retournes.
        """
    def Tolerance(self) -> float: 
        """
        Return the tolerance value used in the last Perform() call If ForceTolerance() has been called, return the given value. If not, return value extracted from shapes.
        """
    def Transition(self,Index : int,FaceOrientation : OCP.TopAbs.TopAbs_Orientation) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: 
        """
        Index = 1 transition par rapport a la face, en cheminant sur l'arete
        """
    def UVPoint(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        parametre de Value() sur la face
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        return the 3D point of the current intersection point.
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_FacesFiller():
    """
    Fills a DataStructure from TopOpeBRepDS with the result of Face/Face instersection described by FacesIntersector from TopOpeBRep. if the faces have same Domain, record it in the DS. else record lines and points and attach list of interferences to the faces, the lines and the edges.
    """
    def AddShapesLine(self) -> None: 
        """
        compute 3d curve, pcurves and face/curve interferences for current NDSC. Add them to the DS.
        """
    def ChangeDataStructure(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure: 
        """
        None
        """
    def ChangeFacesIntersector(self) -> TopOpeBRep_FacesIntersector: 
        """
        None
        """
    def ChangePointClassifier(self) -> TopOpeBRep_PointClassifier: 
        """
        None
        """
    def CheckLine(self,L : TopOpeBRep_LineInter) -> bool: 
        """
        None
        """
    @staticmethod
    def EqualpPonR_s(Lrest : TopOpeBRep_LineInter,VP1 : TopOpeBRep_VPointInter,VP2 : TopOpeBRep_VPointInter) -> bool: 
        """
        None
        """
    def Face(self,I : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    @overload
    def FaceFaceTransition(self,I : int) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: 
        """
        None

        None
        """
    @overload
    def FaceFaceTransition(self,L : TopOpeBRep_LineInter,I : int) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: ...
    def FillLine(self) -> None: 
        """
        None
        """
    def FillLineVPonR(self) -> None: 
        """
        VP processing for restriction line and line sharing same domain with section edges : - if restriction : Adds restriction edges as section edges and compute face/edge interference. - if same domain : If line share same domain with section edges, compute parts of line IN/IN the two faces, and compute curve/point interference for VP boundaries.
        """
    def GetESL(self,LES : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Get map <mapES > of restriction edges having parts IN one of the 2 faces.
        """
    @overload
    def GetFFGeometry(self,DSP : OCP.TopOpeBRepDS.TopOpeBRepDS_Point,K : OCP.TopOpeBRepDS.TopOpeBRepDS_Kind,G : int) -> bool: 
        """
        search for G = geometry of Point which is identical to <DSP> among the DS Points created in the CURRENT face/face intersection ( current Insert() call).

        search for G = geometry of Point which is identical to <VP> among the DS Points created in the CURRENT face/face intersection ( current Insert() call).
        """
    @overload
    def GetFFGeometry(self,VP : TopOpeBRep_VPointInter,K : OCP.TopOpeBRepDS.TopOpeBRepDS_Kind,G : int) -> bool: ...
    def GetGeometry(self,IT : Any,VP : TopOpeBRep_VPointInter,G : int,K : OCP.TopOpeBRepDS.TopOpeBRepDS_Kind) -> bool: 
        """
        Get the geometry of a DS point <DSP>. Search for it with ScanInterfList (previous method). if found, set <G> to the geometry of the interference found. else, add the point <DSP> in the <DS> and set <G> to the value of the new geometry such created. returns the value of ScanInterfList().
        """
    def GetTraceIndex(self) -> Tuple[int, int]: 
        """
        None
        """
    def HDataStructure(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure: 
        """
        None
        """
    def Insert(self,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape,FACINT : TopOpeBRep_FacesIntersector,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        Stores in <DS> the intersections of <S1> and <S2>.
        """
    @staticmethod
    def IsVPtransLok_s(L : TopOpeBRep_LineInter,iVP : int,SI12 : int,T : OCP.TopOpeBRepDS.TopOpeBRepDS_Transition) -> bool: 
        """
        Computes the transition <T> of the VPoint <iVP> on the edge of <SI12>. Returns <False> if the status is unknown.
        """
    @staticmethod
    def LSameDomainERL_s(L : TopOpeBRep_LineInter,ERL : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        Returns <True> if <L> shares a same geometric domain with at least one of the section edges of <ERL>.
        """
    @staticmethod
    def Lminmax_s(L : TopOpeBRep_LineInter) -> Tuple[float, float]: 
        """
        Computes <pmin> and <pmax> the upper and lower bounds of <L> enclosing all vpoints.
        """
    def LoadLine(self,L : TopOpeBRep_LineInter) -> None: 
        """
        None
        """
    def MakeGeometry(self,VP : TopOpeBRep_VPointInter,ShapeIndex : int,K : OCP.TopOpeBRepDS.TopOpeBRepDS_Kind) -> int: 
        """
        None
        """
    def PDataStructureDummy(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure: 
        """
        None
        """
    def PFacesIntersectorDummy(self) -> TopOpeBRep_FacesIntersector: 
        """
        None
        """
    def PLineInterDummy(self) -> TopOpeBRep_LineInter: 
        """
        None
        """
    def ProcessLine(self) -> None: 
        """
        Process current intersection line (set by LoadLine)
        """
    def ProcessRLine(self) -> None: 
        """
        Process current restriction line, adding restriction edge and computing face/edge interference.
        """
    def ProcessSectionEdges(self) -> None: 
        """
        None
        """
    def ProcessVPInotonR(self,VPI : TopOpeBRep_VPointInterIterator) -> None: 
        """
        processing ProcessVPnotonR for VPI.
        """
    def ProcessVPIonR(self,VPI : TopOpeBRep_VPointInterIterator,trans1 : OCP.TopOpeBRepDS.TopOpeBRepDS_Transition,F1 : OCP.TopoDS.TopoDS_Shape,ShapeIndex : int) -> None: 
        """
        processing ProcessVPonR for VPI.
        """
    def ProcessVPR(self,FF : TopOpeBRep_FacesFiller,VP : TopOpeBRep_VPointInter) -> None: 
        """
        calling the followings ProcessVPIonR and ProcessVPonR.
        """
    def ProcessVPnotonR(self,VP : TopOpeBRep_VPointInter) -> None: 
        """
        adds <VP>'s geometrical point to the DS (if not stored) and computes curve point interference.
        """
    def ProcessVPonR(self,VP : TopOpeBRep_VPointInter,trans1 : OCP.TopOpeBRepDS.TopOpeBRepDS_Transition,F1 : OCP.TopoDS.TopoDS_Shape,ShapeIndex : int) -> None: 
        """
        adds <VP>'s geometric point (if not stored) and computes (curve or edge)/(point or vertex) interference.
        """
    def ProcessVPonclosingR(self,VP : TopOpeBRep_VPointInter,F1 : OCP.TopoDS.TopoDS_Shape,ShapeIndex : int,transEdge : OCP.TopOpeBRepDS.TopOpeBRepDS_Transition,PVKind : OCP.TopOpeBRepDS.TopOpeBRepDS_Kind,PVIndex : int,EPIfound : bool,IEPI : OCP.TopOpeBRepDS.TopOpeBRepDS_Interference) -> None: 
        """
        VP processing on closing arc.
        """
    def ProcessVPondgE(self,VP : TopOpeBRep_VPointInter,ShapeIndex : int,PVKind : OCP.TopOpeBRepDS.TopOpeBRepDS_Kind,PVIndex : int,EPIfound : bool,IEPI : OCP.TopOpeBRepDS.TopOpeBRepDS_Interference,CPIfound : bool,ICPI : OCP.TopOpeBRepDS.TopOpeBRepDS_Interference) -> bool: 
        """
        VP processing on degenerated arc.
        """
    def ResetDSC(self) -> None: 
        """
        None
        """
    def SetTraceIndex(self,exF1 : int,exF2 : int) -> None: 
        """
        None
        """
    def StoreCurveInterference(self,I : OCP.TopOpeBRepDS.TopOpeBRepDS_Interference) -> None: 
        """
        Add interference <I> to list myDSCIL. on a given line, at first call, add a new DS curve.
        """
    @staticmethod
    def TransvpOK_s(L : TopOpeBRep_LineInter,iVP : int,SI : int,isINOUT : bool) -> bool: 
        """
        Computes transition on line for VP<iVP> on edge restriction of <SI>. If <isINOUT> : returns <true> if transition computed is IN/OUT else : returns <true> if transition computed is OUT/IN.
        """
    @staticmethod
    def VPParamOnER_s(vp : TopOpeBRep_VPointInter,Lrest : TopOpeBRep_LineInter) -> float: 
        """
        Returns parameter u of vp on the restriction edge.
        """
    @overload
    def VP_Position(self,L : TopOpeBRep_LineInter) -> None: 
        """
        compute position of VPoints of lines

        compute position of VPoints of line L

        compute position of VP with current faces, according to VP.ShapeIndex() .
        """
    @overload
    def VP_Position(self,VP : TopOpeBRep_VPointInter,VPC : TopOpeBRep_VPointInterClassifier) -> None: ...
    @overload
    def VP_Position(self,FACINT : TopOpeBRep_FacesIntersector) -> None: ...
    def VP_PositionOnL(self,L : TopOpeBRep_LineInter) -> None: 
        """
        compute position of VPoints of non-restriction line L.
        """
    def VP_PositionOnR(self,L : TopOpeBRep_LineInter) -> None: 
        """
        compute position of VPoints of restriction line L.
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_FacesIntersector():
    """
    Describes the intersection of two faces.
    """
    def ChangeLine(self,IL : int) -> TopOpeBRep_LineInter: 
        """
        None
        """
    def CurrentLine(self) -> TopOpeBRep_LineInter: 
        """
        None
        """
    def CurrentLineIndex(self) -> int: 
        """
        None
        """
    def Face(self,Index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns first or second intersected face.
        """
    def ForceTolerances(self,tolarc : float,toltang : float) -> None: 
        """
        Force the tolerance values used by the next Perform(S1,S2) call.
        """
    def GetTolerances(self) -> Tuple[float, float]: 
        """
        Return the tolerance values used in the last Perform() call If ForceTolerances() has been called, return the given values. If not, return values extracted from shapes.
        """
    def InitLine(self) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def IsRestriction(self,E : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        returns true if edge <E> is found as same as the edge associated with a RESTRICTION line.
        """
    def Lines(self) -> TopOpeBRep_HArray1OfLineInter: 
        """
        None
        """
    def MoreLine(self) -> bool: 
        """
        None
        """
    def NbLines(self) -> int: 
        """
        None
        """
    def NextLine(self) -> None: 
        """
        None
        """
    @overload
    def Perform(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,B1 : OCP.Bnd.Bnd_Box,B2 : OCP.Bnd.Bnd_Box) -> None: 
        """
        Computes the intersection of faces S1 and S2.

        Computes the intersection of faces S1 and S2.
        """
    @overload
    def Perform(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def PrepareLines(self) -> None: 
        """
        None
        """
    def Restrictions(self) -> OCP.TopTools.TopTools_IndexedMapOfShape: 
        """
        returns the map of edges found as TopeBRepBRep_RESTRICTION
        """
    def SameDomain(self) -> bool: 
        """
        Returns True if Perform() arguments are two faces with the same surface.
        """
    def SurfacesSameOriented(self) -> bool: 
        """
        Returns True if Perform() arguments are two faces SameDomain() and normals on both side. Raise if SameDomain is False
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_GeomTool():
    """
    Provide services needed by the DSFiller
    """
    @staticmethod
    def MakeBSpline1fromWALKING2d_s(L : TopOpeBRep_LineInter,SI : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    @staticmethod
    def MakeBSpline1fromWALKING3d_s(L : TopOpeBRep_LineInter) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    @staticmethod
    def MakeCurve_s(min : float,max : float,L : TopOpeBRep_LineInter,C : OCP.Geom.Geom_Curve) -> None: 
        """
        None
        """
    @staticmethod
    def MakeCurves_s(min : float,max : float,L : TopOpeBRep_LineInter,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,C : OCP.TopOpeBRepDS.TopOpeBRepDS_Curve,PC1 : OCP.Geom2d.Geom2d_Curve,PC2 : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Make the DS curve <C> and the pcurves <PC1,PC2> from intersection line <L> lying on shapes <S1,S2>. <min,max> = <L> bounds
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_HArray1OfLineInter(TopOpeBRep_Array1OfLineInter, OCP.Standard.Standard_Transient):
    def Array1(self) -> TopOpeBRep_Array1OfLineInter: 
        """
        None
        """
    def Assign(self,theOther : TopOpeBRep_Array1OfLineInter) -> TopOpeBRep_Array1OfLineInter: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TopOpeBRep_Array1OfLineInter: 
        """
        None
        """
    def ChangeFirst(self) -> TopOpeBRep_LineInter: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TopOpeBRep_LineInter: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TopOpeBRep_LineInter: 
        """
        Variable value access
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
    def First(self) -> TopOpeBRep_LineInter: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : TopOpeBRep_LineInter) -> None: 
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
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> TopOpeBRep_LineInter: 
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
    def Move(self,theOther : TopOpeBRep_Array1OfLineInter) -> TopOpeBRep_Array1OfLineInter: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TopOpeBRep_LineInter) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> TopOpeBRep_LineInter: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : TopOpeBRep_LineInter) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRep_Array1OfLineInter) -> None: ...
    def __iter__(self) -> iterator: ...
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
class TopOpeBRep_HArray1OfVPointInter(TopOpeBRep_Array1OfVPointInter, OCP.Standard.Standard_Transient):
    def Array1(self) -> TopOpeBRep_Array1OfVPointInter: 
        """
        None
        """
    def Assign(self,theOther : TopOpeBRep_Array1OfVPointInter) -> TopOpeBRep_Array1OfVPointInter: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TopOpeBRep_Array1OfVPointInter: 
        """
        None
        """
    def ChangeFirst(self) -> TopOpeBRep_VPointInter: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TopOpeBRep_VPointInter: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TopOpeBRep_VPointInter: 
        """
        Variable value access
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
    def First(self) -> TopOpeBRep_VPointInter: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : TopOpeBRep_VPointInter) -> None: 
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
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> TopOpeBRep_VPointInter: 
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
    def Move(self,theOther : TopOpeBRep_Array1OfVPointInter) -> TopOpeBRep_Array1OfVPointInter: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TopOpeBRep_VPointInter) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> TopOpeBRep_VPointInter: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRep_Array1OfVPointInter) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : TopOpeBRep_VPointInter) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class TopOpeBRep_Hctxee2d(OCP.Standard.Standard_Transient):
    def Curve(self,I : int) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
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
    def Domain(self,I : int) -> OCP.IntRes2d.IntRes2d_Domain: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetEdges(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,BAS1 : OCP.BRepAdaptor.BRepAdaptor_Surface,BAS2 : OCP.BRepAdaptor.BRepAdaptor_Surface) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class TopOpeBRep_Hctxff2d(OCP.Standard.Standard_Transient):
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
    def Face(self,I : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def FaceSameOrientedWithRef(self,I : int) -> bool: 
        """
        None
        """
    def FacesSameOriented(self) -> bool: 
        """
        None
        """
    def GetMaxTolerance(self) -> float: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerances(self) -> Tuple[float, float]: 
        """
        None
        """
    def HSurface(self,I : int) -> OCP.BRepAdaptor.BRepAdaptor_HSurface: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetFaces(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def SetHSurfaces(self,S1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,S2 : OCP.BRepAdaptor.BRepAdaptor_HSurface) -> None: 
        """
        None
        """
    def SetTolerances(self,Tol1 : float,Tol2 : float) -> None: 
        """
        None
        """
    def SurfacesSameOriented(self) -> bool: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class TopOpeBRep_LineInter():
    """
    None
    """
    def Arc(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns the edge of a RESTRICTION line (or a null edge).
        """
    def ArcIsEdge(self,I : int) -> bool: 
        """
        returns true if Arc() edge (of a RESTRICTION line) is an edge of the original face <Index> (1 or 2).
        """
    def Bounds(self) -> Tuple[float, float]: 
        """
        None
        """
    def ChangeVPoint(self,I : int) -> TopOpeBRep_VPointInter: 
        """
        None
        """
    def ComputeFaceFaceTransition(self) -> None: 
        """
        None
        """
    @overload
    def Curve(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve(self,parmin : float,parmax : float) -> OCP.Geom.Geom_Curve: ...
    def DumpBipoint(self,B : TopOpeBRep_Bipoint,s1 : OCP.TCollection.TCollection_AsciiString,s2 : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def DumpLineTransitions(self,OS : Any) -> Any: 
        """
        None
        """
    def DumpType(self) -> None: 
        """
        None
        """
    def DumpVPoint(self,I : int,s1 : OCP.TCollection.TCollection_AsciiString,s2 : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def FaceFaceTransition(self,I : int) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: 
        """
        None
        """
    def GetTraceIndex(self) -> Tuple[int, int]: 
        """
        None
        """
    def HasFirstPoint(self) -> bool: 
        """
        None
        """
    def HasLastPoint(self) -> bool: 
        """
        None
        """
    def HasVInternal(self) -> bool: 
        """
        None
        """
    def HasVPonR(self) -> bool: 
        """
        None

        None
        """
    def INL(self) -> bool: 
        """
        None

        None
        """
    @overload
    def Index(self,I : int) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Index(self) -> int: ...
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def IsVClosed(self) -> bool: 
        """
        None

        None
        """
    def LineG(self) -> OCP.IntPatch.IntPatch_GLine: 
        """
        None

        None
        """
    def LineR(self) -> OCP.IntPatch.IntPatch_RLine: 
        """
        None

        None
        """
    def LineW(self) -> OCP.IntPatch.IntPatch_WLine: 
        """
        None

        None
        """
    def NbVPoint(self) -> int: 
        """
        None

        None
        """
    def NbWPoint(self) -> int: 
        """
        None
        """
    def OK(self) -> bool: 
        """
        None

        None
        """
    def Period(self) -> float: 
        """
        None
        """
    def SetFaces(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None

        None
        """
    def SetHasVPonR(self) -> None: 
        """
        None
        """
    def SetINL(self) -> None: 
        """
        None
        """
    def SetIsVClosed(self) -> None: 
        """
        None
        """
    def SetLine(self,L : OCP.IntPatch.IntPatch_Line,S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface) -> None: 
        """
        None
        """
    def SetOK(self,B : bool) -> None: 
        """
        None
        """
    def SetTraceIndex(self,exF1 : int,exF2 : int) -> None: 
        """
        None
        """
    def SetVPBounds(self) -> None: 
        """
        None
        """
    def SituationS1(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        None

        None
        """
    def SituationS2(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        None

        None
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        None

        None
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        None

        None
        """
    def TypeLineCurve(self) -> TopOpeBRep_TypeLineCurve: 
        """
        None

        None
        """
    def VPBounds(self) -> Tuple[int, int, int]: 
        """
        None
        """
    def VPoint(self,I : int) -> TopOpeBRep_VPointInter: 
        """
        None
        """
    def WPoint(self,I : int) -> TopOpeBRep_WPointInter: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_ListOfBipoint(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TopOpeBRep_Bipoint) -> TopOpeBRep_Bipoint: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TopOpeBRep_ListOfBipoint) -> None: ...
    @overload
    def Append(self,theItem : TopOpeBRep_Bipoint,theIter : Any) -> None: ...
    def Assign(self,theOther : TopOpeBRep_ListOfBipoint) -> TopOpeBRep_ListOfBipoint: 
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
    def First(self) -> TopOpeBRep_Bipoint: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : TopOpeBRep_Bipoint,theIter : Any) -> TopOpeBRep_Bipoint: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TopOpeBRep_ListOfBipoint,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : TopOpeBRep_Bipoint,theIter : Any) -> TopOpeBRep_Bipoint: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TopOpeBRep_ListOfBipoint,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TopOpeBRep_Bipoint: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : TopOpeBRep_Bipoint) -> TopOpeBRep_Bipoint: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TopOpeBRep_ListOfBipoint) -> None: ...
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
    def __init__(self,theOther : TopOpeBRep_ListOfBipoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TopOpeBRep_P2Dstatus():
    """
    None

    Members:

      TopOpeBRep_P2DUNK

      TopOpeBRep_P2DINT

      TopOpeBRep_P2DSGF

      TopOpeBRep_P2DSGL

      TopOpeBRep_P2DNEW
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    TopOpeBRep_P2DINT: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DINT
    TopOpeBRep_P2DNEW: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DNEW
    TopOpeBRep_P2DSGF: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGF
    TopOpeBRep_P2DSGL: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGL
    TopOpeBRep_P2DUNK: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DUNK
    __entries: dict # value = {'TopOpeBRep_P2DUNK': (TopOpeBRep_P2Dstatus.TopOpeBRep_P2DUNK, None), 'TopOpeBRep_P2DINT': (TopOpeBRep_P2Dstatus.TopOpeBRep_P2DINT, None), 'TopOpeBRep_P2DSGF': (TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGF, None), 'TopOpeBRep_P2DSGL': (TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGL, None), 'TopOpeBRep_P2DNEW': (TopOpeBRep_P2Dstatus.TopOpeBRep_P2DNEW, None)}
    __members__: dict # value = {'TopOpeBRep_P2DUNK': TopOpeBRep_P2Dstatus.TopOpeBRep_P2DUNK, 'TopOpeBRep_P2DINT': TopOpeBRep_P2Dstatus.TopOpeBRep_P2DINT, 'TopOpeBRep_P2DSGF': TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGF, 'TopOpeBRep_P2DSGL': TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGL, 'TopOpeBRep_P2DNEW': TopOpeBRep_P2Dstatus.TopOpeBRep_P2DNEW}
    pass
class TopOpeBRep_Point2d():
    """
    None
    """
    def ChangeTransition(self,I : int) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: 
        """
        None
        """
    def Dump(self,ie1 : int=0,ie2 : int=0) -> None: 
        """
        None
        """
    def EdgesConfig(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Config: 
        """
        None

        None
        """
    def HasPint(self) -> bool: 
        """
        None

        None
        """
    def Hctxee2d(self) -> TopOpeBRep_Hctxee2d: 
        """
        None

        None
        """
    def Hctxff2d(self) -> TopOpeBRep_Hctxff2d: 
        """
        None

        None
        """
    def Index(self) -> int: 
        """
        None

        None
        """
    def IsPointOfSegment(self) -> bool: 
        """
        None

        None
        """
    @overload
    def IsVertex(self,I : int) -> bool: 
        """
        None

        None
        """
    @overload
    def IsVertex(self,Index : int) -> bool: ...
    def Keep(self) -> bool: 
        """
        None

        None
        """
    @overload
    def Parameter(self,I : int) -> float: 
        """
        None

        None
        """
    @overload
    def Parameter(self,Index : int) -> float: ...
    def Pint(self) -> OCP.IntRes2d.IntRes2d_IntersectionPoint: 
        """
        None

        None
        """
    def SegmentAncestors(self,IP1 : int,IP2 : int) -> bool: 
        """
        None

        None
        """
    @overload
    def SetEdgesConfig(self,C : OCP.TopOpeBRepDS.TopOpeBRepDS_Config) -> None: 
        """
        None

        None
        """
    @overload
    def SetEdgesConfig(self,B : OCP.TopOpeBRepDS.TopOpeBRepDS_Config) -> None: ...
    @overload
    def SetHctxee2d(self,ee2d : TopOpeBRep_Hctxee2d) -> None: 
        """
        None

        None
        """
    @overload
    def SetHctxee2d(self,h : TopOpeBRep_Hctxee2d) -> None: ...
    @overload
    def SetHctxff2d(self,h : TopOpeBRep_Hctxff2d) -> None: 
        """
        None

        None
        """
    @overload
    def SetHctxff2d(self,ff2d : TopOpeBRep_Hctxff2d) -> None: ...
    @overload
    def SetIndex(self,X : int) -> None: 
        """
        None

        None
        """
    @overload
    def SetIndex(self,I : int) -> None: ...
    def SetIsPointOfSegment(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetIsVertex(self,I : int,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetIsVertex(self,Index : int,B : bool) -> None: ...
    def SetKeep(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetParameter(self,I : int,P : float) -> None: 
        """
        None

        None
        """
    @overload
    def SetParameter(self,Index : int,P : float) -> None: ...
    def SetPint(self,P : OCP.IntRes2d.IntRes2d_IntersectionPoint) -> None: 
        """
        None

        None
        """
    def SetSegmentAncestors(self,IP1 : int,IP2 : int) -> None: 
        """
        None

        None
        """
    @overload
    def SetStatus(self,S : TopOpeBRep_P2Dstatus) -> None: 
        """
        None

        None
        """
    @overload
    def SetStatus(self,I : TopOpeBRep_P2Dstatus) -> None: ...
    @overload
    def SetTolerance(self,T : float) -> None: 
        """
        None

        None
        """
    @overload
    def SetTolerance(self,t : float) -> None: ...
    @overload
    def SetTransition(self,Index : int,T : OCP.TopOpeBRepDS.TopOpeBRepDS_Transition) -> None: 
        """
        None

        None
        """
    @overload
    def SetTransition(self,I : int,T : OCP.TopOpeBRepDS.TopOpeBRepDS_Transition) -> None: ...
    def SetValue(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        None

        None
        """
    def SetValue2d(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None
        """
    @overload
    def SetVertex(self,Index : int,V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None

        None
        """
    @overload
    def SetVertex(self,I : int,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    def Status(self) -> TopOpeBRep_P2Dstatus: 
        """
        None

        None
        """
    def Tolerance(self) -> float: 
        """
        None

        None
        """
    def Transition(self,I : int) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Transition: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def Value2d(self) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
        """
    def Vertex(self,I : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_PointClassifier():
    """
    None
    """
    def Classify(self,F : OCP.TopoDS.TopoDS_Face,P : OCP.gp.gp_Pnt2d,Tol : float) -> OCP.TopAbs.TopAbs_State: 
        """
        compute position of point <P> regarding with the face <F>.
        """
    def Init(self) -> None: 
        """
        None
        """
    def Load(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_PointGeomTool():
    """
    Provide services needed by the Fillers
    """
    @staticmethod
    def IsEqual_s(DSP1 : OCP.TopOpeBRepDS.TopOpeBRepDS_Point,DSP2 : OCP.TopOpeBRepDS.TopOpeBRepDS_Point) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def MakePoint_s(FEI : TopOpeBRep_FaceEdgeIntersector) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Point: 
        """
        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def MakePoint_s(P2D : TopOpeBRep_Point2d) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Point: ...
    @staticmethod
    @overload
    def MakePoint_s(IP : TopOpeBRep_VPointInter) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Point: ...
    @staticmethod
    @overload
    def MakePoint_s(S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Point: ...
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_SequenceOfPoint2d(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TopOpeBRep_Point2d) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : TopOpeBRep_SequenceOfPoint2d) -> None: ...
    def Assign(self,theOther : TopOpeBRep_SequenceOfPoint2d) -> TopOpeBRep_SequenceOfPoint2d: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> TopOpeBRep_Point2d: 
        """
        First item access
        """
    def ChangeLast(self) -> TopOpeBRep_Point2d: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> TopOpeBRep_Point2d: 
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
    def First(self) -> TopOpeBRep_Point2d: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : TopOpeBRep_Point2d) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TopOpeBRep_SequenceOfPoint2d) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : TopOpeBRep_Point2d) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TopOpeBRep_SequenceOfPoint2d) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> TopOpeBRep_Point2d: 
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
    def Prepend(self,theItem : TopOpeBRep_Point2d) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TopOpeBRep_SequenceOfPoint2d) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : TopOpeBRep_Point2d) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TopOpeBRep_SequenceOfPoint2d) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> TopOpeBRep_Point2d: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TopOpeBRep_SequenceOfPoint2d) -> None: ...
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
class TopOpeBRep_ShapeIntersector():
    """
    Intersect two shapes.
    """
    def ChangeEdgesIntersector(self) -> TopOpeBRep_EdgesIntersector: 
        """
        return the current intersection of two Edges.
        """
    def ChangeFaceEdgeIntersector(self) -> TopOpeBRep_FaceEdgeIntersector: 
        """
        return the current intersection of a Face and an Edge.
        """
    def ChangeFacesIntersector(self) -> TopOpeBRep_FacesIntersector: 
        """
        return the current intersection of two Faces.
        """
    def CurrentGeomShape(self,Index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        return geometric shape <Index> ( = 1 or 2 ) of current intersection.
        """
    def DumpCurrent(self,K : int) -> None: 
        """
        None
        """
    def GetTolerances(self) -> Tuple[float, float]: 
        """
        return MAX of intersection tolerances with which FacesIntersector from TopOpeBRep was working.
        """
    def Index(self,K : int) -> int: 
        """
        None
        """
    @overload
    def InitIntersection(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize the intersection of shapes S1,S2.

        Initialize the intersection of shapes S1,S2.
        """
    @overload
    def InitIntersection(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> None: ...
    def MoreIntersection(self) -> bool: 
        """
        returns True if there are more intersection between two the shapes.
        """
    def NextIntersection(self) -> None: 
        """
        search for the next intersection between the two shapes.
        """
    def RejectedFaces(self,anObj : OCP.TopoDS.TopoDS_Shape,aReference : OCP.TopoDS.TopoDS_Shape,aListOfShape : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def Shape(self,Index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        return the shape <Index> ( = 1 or 2) given to InitIntersection(). Index = 1 will return S1, Index = 2 will return S2.
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_ShapeIntersector2d():
    """
    Intersect two shapes.
    """
    def ChangeEdgesIntersector(self) -> TopOpeBRep_EdgesIntersector: 
        """
        return the current intersection of two Edges.
        """
    def CurrentGeomShape(self,Index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        return geometric shape <Index> ( = 1 or 2 ) of current intersection.
        """
    def DumpCurrent(self,K : int) -> None: 
        """
        None
        """
    def Index(self,K : int) -> int: 
        """
        None
        """
    def InitIntersection(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize the intersection of shapes S1,S2.
        """
    def MoreIntersection(self) -> bool: 
        """
        returns True if there are more intersection between two the shapes.
        """
    def NextIntersection(self) -> None: 
        """
        search for the next intersection between the two shapes.
        """
    def Shape(self,Index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        return the shape <Index> ( = 1 or 2) given to InitIntersection(). Index = 1 will return S1, Index = 2 will return S2.
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_ShapeScanner():
    """
    Find, among the subshapes SS of a reference shape RS, the ones which 3D box interfers with the box of a shape S (SS and S are of the same type).
    """
    def AddBoxesMakeCOB(self,S : OCP.TopoDS.TopoDS_Shape,TS : OCP.TopAbs.TopAbs_ShapeEnum,TA : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: 
        """
        None
        """
    def BoxSort(self) -> OCP.TopOpeBRepTool.TopOpeBRepTool_BoxSort: 
        """
        None
        """
    def ChangeBoxSort(self) -> OCP.TopOpeBRepTool.TopOpeBRepTool_BoxSort: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def Current(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def DumpCurrent(self,OS : Any) -> Any: 
        """
        None
        """
    def Index(self) -> int: 
        """
        None
        """
    @overload
    def Init(self,E : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,X : OCP.TopOpeBRepTool.TopOpeBRepTool_ShapeExplorer) -> None: ...
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_TypeLineCurve():
    """
    None

    Members:

      TopOpeBRep_ANALYTIC

      TopOpeBRep_RESTRICTION

      TopOpeBRep_WALKING

      TopOpeBRep_LINE

      TopOpeBRep_CIRCLE

      TopOpeBRep_ELLIPSE

      TopOpeBRep_PARABOLA

      TopOpeBRep_HYPERBOLA

      TopOpeBRep_OTHERTYPE
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    TopOpeBRep_ANALYTIC: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_ANALYTIC
    TopOpeBRep_CIRCLE: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_CIRCLE
    TopOpeBRep_ELLIPSE: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_ELLIPSE
    TopOpeBRep_HYPERBOLA: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_HYPERBOLA
    TopOpeBRep_LINE: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_LINE
    TopOpeBRep_OTHERTYPE: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_OTHERTYPE
    TopOpeBRep_PARABOLA: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_PARABOLA
    TopOpeBRep_RESTRICTION: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_RESTRICTION
    TopOpeBRep_WALKING: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_WALKING
    __entries: dict # value = {'TopOpeBRep_ANALYTIC': (TopOpeBRep_TypeLineCurve.TopOpeBRep_ANALYTIC, None), 'TopOpeBRep_RESTRICTION': (TopOpeBRep_TypeLineCurve.TopOpeBRep_RESTRICTION, None), 'TopOpeBRep_WALKING': (TopOpeBRep_TypeLineCurve.TopOpeBRep_WALKING, None), 'TopOpeBRep_LINE': (TopOpeBRep_TypeLineCurve.TopOpeBRep_LINE, None), 'TopOpeBRep_CIRCLE': (TopOpeBRep_TypeLineCurve.TopOpeBRep_CIRCLE, None), 'TopOpeBRep_ELLIPSE': (TopOpeBRep_TypeLineCurve.TopOpeBRep_ELLIPSE, None), 'TopOpeBRep_PARABOLA': (TopOpeBRep_TypeLineCurve.TopOpeBRep_PARABOLA, None), 'TopOpeBRep_HYPERBOLA': (TopOpeBRep_TypeLineCurve.TopOpeBRep_HYPERBOLA, None), 'TopOpeBRep_OTHERTYPE': (TopOpeBRep_TypeLineCurve.TopOpeBRep_OTHERTYPE, None)}
    __members__: dict # value = {'TopOpeBRep_ANALYTIC': TopOpeBRep_TypeLineCurve.TopOpeBRep_ANALYTIC, 'TopOpeBRep_RESTRICTION': TopOpeBRep_TypeLineCurve.TopOpeBRep_RESTRICTION, 'TopOpeBRep_WALKING': TopOpeBRep_TypeLineCurve.TopOpeBRep_WALKING, 'TopOpeBRep_LINE': TopOpeBRep_TypeLineCurve.TopOpeBRep_LINE, 'TopOpeBRep_CIRCLE': TopOpeBRep_TypeLineCurve.TopOpeBRep_CIRCLE, 'TopOpeBRep_ELLIPSE': TopOpeBRep_TypeLineCurve.TopOpeBRep_ELLIPSE, 'TopOpeBRep_PARABOLA': TopOpeBRep_TypeLineCurve.TopOpeBRep_PARABOLA, 'TopOpeBRep_HYPERBOLA': TopOpeBRep_TypeLineCurve.TopOpeBRep_HYPERBOLA, 'TopOpeBRep_OTHERTYPE': TopOpeBRep_TypeLineCurve.TopOpeBRep_OTHERTYPE}
    pass
class TopOpeBRep_VPointInter():
    """
    None
    """
    def ArcOnS1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def ArcOnS2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def ChangeKeep(self,keep : bool) -> None: 
        """
        updates VPointInter flag "keep" with <keep>.

        updates VPointInter flag "keep" with <keep>.
        """
    @overload
    def Dump(self,I : int,F : OCP.TopoDS.TopoDS_Face,OS : Any) -> Any: 
        """
        None

        None
        """
    @overload
    def Dump(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,OS : Any) -> Any: ...
    def Edge(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        get the edge of shape I (1,2) containing the point. Returned shape is null if the VPoint is not on an edge of shape I (1,2).
        """
    @overload
    def EdgeON(self,Eon : OCP.TopoDS.TopoDS_Shape,Par : float,I : int) -> None: 
        """
        set the shape Eon of shape I (1,2) containing the point, and parameter <Par> of point on <Eon>.

        get the edge of shape I (1,2) containing the point.
        """
    @overload
    def EdgeON(self,I : int) -> OCP.TopoDS.TopoDS_Shape: ...
    def EdgeONParameter(self,I : int) -> float: 
        """
        get the parameter on edge of shape I (1,2) containing the point.
        """
    def EdgeParameter(self,I : int) -> float: 
        """
        get the parameter on edge of shape I (1,2) containing the point
        """
    def EqualpP(self,VP : TopOpeBRep_VPointInter) -> bool: 
        """
        returns <True> if the 3d points and the parameters of the VPoints are same
        """
    def GetShapes(self) -> Tuple[int, int]: 
        """
        None

        None
        """
    @overload
    def Index(self,I : int) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Index(self) -> int: ...
    def IsInternal(self) -> bool: 
        """
        None

        None
        """
    def IsMultiple(self) -> bool: 
        """
        Returns True if the point belongs to several intersection lines.

        Returns True if the point belongs to several intersection lines.
        """
    def IsOnDomS1(self) -> bool: 
        """
        None

        None
        """
    def IsOnDomS2(self) -> bool: 
        """
        None

        None
        """
    def IsVertex(self,I : int) -> bool: 
        """
        None
        """
    def IsVertexOnS1(self) -> bool: 
        """
        Returns TRUE if the point is a vertex on the initial restriction facet of the first surface.

        Returns TRUE if the point is a vertex on the initial restriction facet of the first surface.
        """
    def IsVertexOnS2(self) -> bool: 
        """
        Returns TRUE if the point is a vertex on the initial restriction facet of the second surface.

        Returns TRUE if the point is a vertex on the initial restriction facet of the second surface.
        """
    def Keep(self) -> bool: 
        """
        Returns value of myKeep (does not evaluate states) False at creation of VPoint. Updated by State(State from TopAbs,Integer from Standard)

        Returns value of myKeep (does not evaluate states) False at creation of VPoint. Updated by State(State from TopAbs,Integer from Standard)
        """
    def PThePointOfIntersectionDummy(self) -> OCP.IntPatch.IntPatch_Point: 
        """
        None
        """
    def ParameterOnArc1(self) -> float: 
        """
        None

        None
        """
    def ParameterOnArc2(self) -> float: 
        """
        None

        None
        """
    def ParameterOnLine(self) -> float: 
        """
        None

        None
        """
    def ParametersOnS1(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def ParametersOnS2(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def ParonE(self,E : OCP.TopoDS.TopoDS_Edge,par : float) -> bool: 
        """
        returns <false> if the vpoint is not given on arc <E>, else returns <par> parameter on <E>
        """
    def SetPoint(self,P : OCP.IntPatch.IntPatch_Point) -> None: 
        """
        None
        """
    def SetShapes(self,I1 : int,I2 : int) -> None: 
        """
        None

        None
        """
    @overload
    def ShapeIndex(self,I : int) -> None: 
        """
        returns value of filed myShapeIndex = 0,1,2,3 0 means the VPoint is on no restriction 1 means the VPoint is on the restriction 1 2 means the VPoint is on the restriction 2 3 means the VPoint is on the restrictions 1 and 2

        set value of shape supporting me (0,1,2,3).

        returns value of filed myShapeIndex = 0,1,2,3 0 means the VPoint is on no restriction 1 means the VPoint is on the restriction 1 2 means the VPoint is on the restriction 2 3 means the VPoint is on the restrictions 1 and 2

        set value of shape supporting me (0,1,2,3).
        """
    @overload
    def ShapeIndex(self) -> int: ...
    @overload
    def State(self,S : OCP.TopAbs.TopAbs_State,I : int) -> None: 
        """
        get state of VPoint within the domain of geometric shape domain <I> (= 1 or 2).

        Set the state of VPoint within the domain of the geometric shape <I> (= 1 or 2).
        """
    @overload
    def State(self,I : int) -> OCP.TopAbs.TopAbs_State: ...
    def SurfaceParameters(self,I : int) -> OCP.gp.gp_Pnt2d: 
        """
        get the parameter on surface of shape I (1,2) containing the point
        """
    def Tolerance(self) -> float: 
        """
        None

        None
        """
    def TransitionLineArc1(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        None

        None
        """
    def TransitionLineArc2(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        None

        None
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        None

        None
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        None

        None
        """
    def UpdateKeep(self) -> None: 
        """
        set myKeep value according to current states.
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def Vertex(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def VertexOnS1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the information about the point when it is on the domain of the first patch, i-e when the function IsVertexOnS1 returns True. Otherwise, an exception is raised.
        """
    def VertexOnS2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the information about the point when it is on the domain of the second patch, i-e when the function IsVertexOnS2 returns True. Otherwise, an exception is raised.
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_VPointInterClassifier():
    """
    None
    """
    def Edge(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns the edge containing the VPoint <VP> used in the last VPointPosition() call. Edge is defined if the state previously computed is ON, else Edge is a null shape.
        """
    def EdgeParameter(self) -> float: 
        """
        returns the parameter of the VPoint <VP> on Edge()
        """
    def VPointPosition(self,F : OCP.TopoDS.TopoDS_Shape,VP : TopOpeBRep_VPointInter,ShapeIndex : int,PC : TopOpeBRep_PointClassifier,AssumeINON : bool,Tol : float) -> OCP.TopAbs.TopAbs_State: 
        """
        compute position of VPoint <VP> regarding with face <F>. <ShapeIndex> (= 1,2) indicates which (u,v) point of <VP> is used. when state is ON, set VP.EdgeON() with the edge containing <VP> and associated parameter. returns state of VP on ShapeIndex.
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_VPointInterIterator():
    """
    None
    """
    def ChangeCurrentVP(self) -> TopOpeBRep_VPointInter: 
        """
        None
        """
    def CurrentVP(self) -> TopOpeBRep_VPointInter: 
        """
        None
        """
    def CurrentVPIndex(self) -> int: 
        """
        None
        """
    @overload
    def Init(self) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,LI : TopOpeBRep_LineInter,checkkeep : bool=False) -> None: ...
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def PLineInterDummy(self) -> TopOpeBRep_LineInter: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,LI : TopOpeBRep_LineInter) -> None: ...
    pass
class TopOpeBRep_WPointInter():
    """
    None
    """
    def PPntOn2SDummy(self) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        None
        """
    def Parameters(self) -> Tuple[float, float, float, float]: 
        """
        None
        """
    def ParametersOnS1(self) -> Tuple[float, float]: 
        """
        None
        """
    def ParametersOnS2(self) -> Tuple[float, float]: 
        """
        None
        """
    def Set(self,P : OCP.IntSurf.IntSurf_PntOn2S) -> None: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def ValueOnS1(self) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def ValueOnS2(self) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRep_WPointInterIterator():
    """
    None
    """
    def CurrentWP(self) -> TopOpeBRep_WPointInter: 
        """
        None
        """
    @overload
    def Init(self) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,LI : TopOpeBRep_LineInter) -> None: ...
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def PLineInterDummy(self) -> TopOpeBRep_LineInter: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,LI : TopOpeBRep_LineInter) -> None: ...
    pass
TopOpeBRep_ANALYTIC: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_ANALYTIC
TopOpeBRep_CIRCLE: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_CIRCLE
TopOpeBRep_ELLIPSE: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_ELLIPSE
TopOpeBRep_HYPERBOLA: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_HYPERBOLA
TopOpeBRep_LINE: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_LINE
TopOpeBRep_OTHERTYPE: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_OTHERTYPE
TopOpeBRep_P2DINT: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DINT
TopOpeBRep_P2DNEW: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DNEW
TopOpeBRep_P2DSGF: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGF
TopOpeBRep_P2DSGL: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGL
TopOpeBRep_P2DUNK: OCP.TopOpeBRep.TopOpeBRep_P2Dstatus # value = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DUNK
TopOpeBRep_PARABOLA: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_PARABOLA
TopOpeBRep_RESTRICTION: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_RESTRICTION
TopOpeBRep_WALKING: OCP.TopOpeBRep.TopOpeBRep_TypeLineCurve # value = TopOpeBRep_TypeLineCurve.TopOpeBRep_WALKING
