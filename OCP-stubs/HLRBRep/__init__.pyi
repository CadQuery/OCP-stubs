import OCP.HLRBRep
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.HLRTopoBRep
import OCP.math
import OCP.NCollection
import OCP.Geom
import OCP.TColgp
import OCP.TopoDS
import OCP.Bnd
import OCP.HLRAlgo
import OCP.BRepAdaptor
import OCP.IntSurf
import OCP.IntCurveSurface
import OCP.Standard
import OCP.TopAbs
import OCP.Adaptor3d
import OCP.TopTools
import OCP.TColStd
import OCP.BRepTopAdaptor
import OCP.Extrema
import OCP.Intf
import OCP.gp
import OCP.GeomAbs
import OCP.Geom2d
import OCP.IntRes2d
__all__  = [
"HLRBRep",
"HLRBRep_InternalAlgo",
"HLRBRep_AreaLimit",
"HLRBRep_Array1OfEData",
"HLRBRep_Array1OfFData",
"HLRBRep_BCurveTool",
"HLRBRep_BSurfaceTool",
"HLRBRep_BiPnt2D",
"HLRBRep_BiPoint",
"HLRBRep_CInter",
"HLRBRep_CLProps",
"HLRBRep_Curve",
"HLRBRep_CurveTool",
"HLRBRep_Data",
"HLRBRep_EdgeBuilder",
"HLRBRep_EdgeData",
"HLRBRep_EdgeFaceTool",
"HLRBRep_EdgeIList",
"HLRBRep_EdgeInterferenceTool",
"HLRBRep_ExactIntersectionPointOfTheIntPCurvePCurveOfCInter",
"HLRBRep_FaceData",
"HLRBRep_FaceIterator",
"HLRBRep_HLRToShape",
"HLRBRep_Hider",
"HLRBRep_IntConicCurveOfCInter",
"HLRBRep_InterCSurf",
"HLRBRep_Algo",
"HLRBRep_Intersector",
"HLRBRep_LineTool",
"HLRBRep_ListOfBPnt2D",
"HLRBRep_ListOfBPoint",
"HLRBRep_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfCInter",
"HLRBRep_PCLocFOfTheLocateExtPCOfTheProjPCurOfCInter",
"HLRBRep_PolyAlgo",
"HLRBRep_PolyHLRToShape",
"HLRBRep_SLProps",
"HLRBRep_SLPropsATool",
"HLRBRep_SeqOfShapeBounds",
"HLRBRep_ShapeBounds",
"HLRBRep_ShapeToHLR",
"HLRBRep_Surface",
"HLRBRep_SurfaceTool",
"HLRBRep_TheCSFunctionOfInterCSurf",
"HLRBRep_TheCurveLocatorOfTheProjPCurOfCInter",
"HLRBRep_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfCInter",
"HLRBRep_TheExactInterCSurf",
"HLRBRep_TheIntConicCurveOfCInter",
"HLRBRep_TheIntPCurvePCurveOfCInter",
"HLRBRep_TheInterferenceOfInterCSurf",
"HLRBRep_TheIntersectorOfTheIntConicCurveOfCInter",
"HLRBRep_TheLocateExtPCOfTheProjPCurOfCInter",
"HLRBRep_ThePolygon2dOfTheIntPCurvePCurveOfCInter",
"HLRBRep_ThePolygonOfInterCSurf",
"HLRBRep_ThePolygonToolOfInterCSurf",
"HLRBRep_ThePolyhedronOfInterCSurf",
"HLRBRep_ThePolyhedronToolOfInterCSurf",
"HLRBRep_TheProjPCurOfCInter",
"HLRBRep_TheQuadCurvExactInterCSurf",
"HLRBRep_TheQuadCurvFuncOfTheQuadCurvExactInterCSurf",
"HLRBRep_TypeOfResultingEdge",
"HLRBRep_VertexList",
"HLRBRep_IsoLine",
"HLRBRep_OutLine",
"HLRBRep_Rg1Line",
"HLRBRep_RgNLine",
"HLRBRep_Sharp",
"HLRBRep_Undefined"
]
class HLRBRep():
    """
    Hidden Lines Removal algorithms on the BRep DataStructure.
    """
    @staticmethod
    def MakeEdge3d_s(ec : HLRBRep_Curve,U1 : float,U2 : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    @staticmethod
    def MakeEdge_s(ec : HLRBRep_Curve,U1 : float,U2 : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    @staticmethod
    def PolyHLRAngleAndDeflection_s(InAngl : float) -> Tuple[float, float]: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_InternalAlgo(OCP.Standard.Standard_Transient):
    def DataStructure(self) -> HLRBRep_Data: 
        """
        None
        """
    @overload
    def Debug(self,deb : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Debug(self) -> bool: ...
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def Hide(self) -> None: 
        """
        hide all the DataStructure.

        hide the Shape <S> by itself.

        hide the Shape <S1> by the shape <S2>.
        """
    @overload
    def Hide(self,I : int) -> None: ...
    @overload
    def Hide(self,I : int,J : int) -> None: ...
    @overload
    def HideAll(self,I : int) -> None: 
        """
        set to hide all the edges.

        set to hide all the edges of the Shape <S>.
        """
    @overload
    def HideAll(self) -> None: ...
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self,S : OCP.HLRTopoBRep.HLRTopoBRep_OutLiner) -> int: 
        """
        return the index of the Shape <S> and return 0 if the Shape <S> is not found.
        """
    def InitEdgeStatus(self) -> None: 
        """
        init the status of the selected edges depending of the back faces of a closed shell.
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
    def Load(self,S : OCP.HLRTopoBRep.HLRTopoBRep_OutLiner,SData : OCP.Standard.Standard_Transient,nbIso : int=0) -> None: 
        """
        add the shape <S>.

        add the shape <S>.
        """
    @overload
    def Load(self,S : OCP.HLRTopoBRep.HLRTopoBRep_OutLiner,nbIso : int=0) -> None: ...
    def NbShapes(self) -> int: 
        """
        None
        """
    def PartialHide(self) -> None: 
        """
        own hiding of all the shapes of the DataStructure without hiding by each other.
        """
    @overload
    def Projector(self) -> OCP.HLRAlgo.HLRAlgo_Projector: 
        """
        set the projector.

        set the projector.
        """
    @overload
    def Projector(self,P : OCP.HLRAlgo.HLRAlgo_Projector) -> None: ...
    def Remove(self,I : int) -> None: 
        """
        remove the Shape of Index <I>.
        """
    @overload
    def Select(self,I : int) -> None: 
        """
        select all the DataStructure.

        select only the Shape of index <I>.
        """
    @overload
    def Select(self) -> None: ...
    def SelectEdge(self,I : int) -> None: 
        """
        select only the edges of the Shape <S>.
        """
    def SelectFace(self,I : int) -> None: 
        """
        select only the faces of the Shape <S>.
        """
    def SeqOfShapeBounds(self) -> HLRBRep_SeqOfShapeBounds: 
        """
        None
        """
    def ShapeBounds(self,I : int) -> HLRBRep_ShapeBounds: 
        """
        None
        """
    def ShapeData(self,I : int,SData : OCP.Standard.Standard_Transient) -> None: 
        """
        Change the Shape Data of the Shape of index <I>.
        """
    @overload
    def ShowAll(self) -> None: 
        """
        set to visible all the edges.

        set to visible all the edges of the Shape <S>.
        """
    @overload
    def ShowAll(self,I : int) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self) -> None: 
        """
        update the DataStructure.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,A : HLRBRep_InternalAlgo) -> None: ...
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
class HLRBRep_AreaLimit(OCP.Standard.Standard_Transient):
    """
    The private nested class AreaLimit represents a -- vertex on the Edge with the state on the left and -- the right.The private nested class AreaLimit represents a -- vertex on the Edge with the state on the left and -- the right.The private nested class AreaLimit represents a -- vertex on the Edge with the state on the left and -- the right.
    """
    def Clear(self) -> None: 
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
    @overload
    def EdgeAfter(self) -> OCP.TopAbs.TopAbs_State: 
        """
        None

        None
        """
    @overload
    def EdgeAfter(self,St : OCP.TopAbs.TopAbs_State) -> None: ...
    @overload
    def EdgeBefore(self) -> OCP.TopAbs.TopAbs_State: 
        """
        None

        None
        """
    @overload
    def EdgeBefore(self,St : OCP.TopAbs.TopAbs_State) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsBoundary(self) -> bool: 
        """
        None
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInterference(self) -> bool: 
        """
        None
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    @overload
    def Next(self) -> HLRBRep_AreaLimit: 
        """
        None

        None
        """
    @overload
    def Next(self,N : HLRBRep_AreaLimit) -> None: ...
    @overload
    def Previous(self) -> HLRBRep_AreaLimit: 
        """
        None

        None
        """
    @overload
    def Previous(self,P : HLRBRep_AreaLimit) -> None: ...
    @overload
    def StateAfter(self) -> OCP.TopAbs.TopAbs_State: 
        """
        None

        None
        """
    @overload
    def StateAfter(self,St : OCP.TopAbs.TopAbs_State) -> None: ...
    @overload
    def StateBefore(self,St : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None

        None
        """
    @overload
    def StateBefore(self) -> OCP.TopAbs.TopAbs_State: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vertex(self) -> OCP.HLRAlgo.HLRAlgo_Intersection: 
        """
        None
        """
    def __init__(self,V : OCP.HLRAlgo.HLRAlgo_Intersection,Boundary : bool,Interference : bool,StateBefore : OCP.TopAbs.TopAbs_State,StateAfter : OCP.TopAbs.TopAbs_State,EdgeBefore : OCP.TopAbs.TopAbs_State,EdgeAfter : OCP.TopAbs.TopAbs_State) -> None: ...
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
class HLRBRep_Array1OfEData():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : HLRBRep_Array1OfEData) -> HLRBRep_Array1OfEData: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> HLRBRep_EdgeData: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRBRep_EdgeData: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRBRep_EdgeData: 
        """
        Variable value access
        """
    def First(self) -> HLRBRep_EdgeData: 
        """
        Returns first element
        """
    def Init(self,theValue : HLRBRep_EdgeData) -> None: 
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
    def Last(self) -> HLRBRep_EdgeData: 
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
    def Move(self,theOther : HLRBRep_Array1OfEData) -> HLRBRep_Array1OfEData: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRBRep_EdgeData) -> None: 
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
    def Value(self,theIndex : int) -> HLRBRep_EdgeData: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : HLRBRep_Array1OfEData) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : HLRBRep_EdgeData,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRBRep_Array1OfFData():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : HLRBRep_Array1OfFData) -> HLRBRep_Array1OfFData: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> HLRBRep_FaceData: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRBRep_FaceData: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRBRep_FaceData: 
        """
        Variable value access
        """
    def First(self) -> HLRBRep_FaceData: 
        """
        Returns first element
        """
    def Init(self,theValue : HLRBRep_FaceData) -> None: 
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
    def Last(self) -> HLRBRep_FaceData: 
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
    def Move(self,theOther : HLRBRep_Array1OfFData) -> HLRBRep_Array1OfFData: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRBRep_FaceData) -> None: 
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
    def Value(self,theIndex : int) -> HLRBRep_FaceData: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : HLRBRep_FaceData,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : HLRBRep_Array1OfFData) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRBRep_BCurveTool():
    """
    None
    """
    @staticmethod
    def BSpline_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.Geom.Geom_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.gp.gp_Circ: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U on the curve.
        """
    @staticmethod
    def D1_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    @staticmethod
    def D2_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    @staticmethod
    def D3_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    @staticmethod
    def DN_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    @staticmethod
    def Degree_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> int: 
        """
        None
        """
    @staticmethod
    def Ellipse_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.gp.gp_Elips: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Hyperbola_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    @staticmethod
    def Intervals_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def IsClosed_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPeriodic_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> bool: 
        """
        None
        """
    @staticmethod
    def IsRational_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> bool: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.gp.gp_Lin: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(myclass) >= <S>
        """
    @staticmethod
    def NbKnots_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> int: 
        """
        None
        """
    @staticmethod
    def NbPoles_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> int: 
        """
        None
        """
    @staticmethod
    def NbSamples_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,U0 : float,U1 : float) -> int: 
        """
        None
        """
    @staticmethod
    def Parabola_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.gp.gp_Parab: 
        """
        None
        """
    @staticmethod
    def Period_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def PolesAndWeights_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,T : OCP.TColgp.TColgp_Array1OfPnt,W : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    @staticmethod
    def Poles_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,T : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    @staticmethod
    def Value_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_BSurfaceTool():
    """
    None
    """
    @staticmethod
    def AxeOfRevolution_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    @staticmethod
    def BSpline_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.Geom.Geom_BSplineSurface: 
        """
        None
        """
    @staticmethod
    def BasisCurve_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.Geom.Geom_BezierSurface: 
        """
        None
        """
    @staticmethod
    def Cone_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.gp.gp_Cone: 
        """
        None
        """
    @staticmethod
    def Cylinder_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.gp.gp_Cylinder: 
        """
        None
        """
    @staticmethod
    def D0_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,u : float,v : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def D1_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,u : float,v : float,P : OCP.gp.gp_Pnt,D1u : OCP.gp.gp_Vec,D1v : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D2_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,u : float,v : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D3_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,u : float,v : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def DN_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,u : float,v : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def Direction_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.gp.gp_Dir: 
        """
        None
        """
    @staticmethod
    def FirstUParameter_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def FirstVParameter_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.GeomAbs.GeomAbs_SurfaceType: 
        """
        None
        """
    @staticmethod
    def IsUClosed_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def IsUPeriodic_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def IsURational_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def IsVClosed_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def IsVPeriodic_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def IsVRational_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def LastUParameter_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def LastVParameter_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> float: 
        """
        None
        """
    @staticmethod
    @overload
    def NbSamplesU_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,u1 : float,u2 : float) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbSamplesU_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> int: ...
    @staticmethod
    @overload
    def NbSamplesV_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,v1 : float,v2 : float) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbSamplesV_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> int: ...
    @staticmethod
    def NbUIntervals_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,Sh : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        None
        """
    @staticmethod
    def NbUKnots_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> int: 
        """
        None
        """
    @staticmethod
    def NbUPoles_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> int: 
        """
        None
        """
    @staticmethod
    def NbVIntervals_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,Sh : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        None
        """
    @staticmethod
    def NbVKnots_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> int: 
        """
        None
        """
    @staticmethod
    def NbVPoles_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> int: 
        """
        None
        """
    @staticmethod
    def Plane_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.gp.gp_Pln: 
        """
        None
        """
    @staticmethod
    def Sphere_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.gp.gp_Sphere: 
        """
        None
        """
    @staticmethod
    def Torus_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.gp.gp_Torus: 
        """
        None
        """
    @staticmethod
    def UContinuity_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def UDegree_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> int: 
        """
        None
        """
    @staticmethod
    def UIntervals_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,T : OCP.TColStd.TColStd_Array1OfReal,Sh : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def UPeriod_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def UResolution_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,R3d : float) -> float: 
        """
        None
        """
    @staticmethod
    def UTrim_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        If <First> >= <Last>
        """
    @staticmethod
    def VContinuity_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def VDegree_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> int: 
        """
        None
        """
    @staticmethod
    def VIntervals_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,T : OCP.TColStd.TColStd_Array1OfReal,Sh : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def VPeriod_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def VResolution_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,R3d : float) -> float: 
        """
        None
        """
    @staticmethod
    def VTrim_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        If <First> >= <Last>
        """
    @staticmethod
    def Value_s(S : OCP.BRepAdaptor.BRepAdaptor_Surface,u : float,v : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_BiPnt2D():
    """
    Contains the colors of a shape.
    """
    @overload
    def IntLine(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def IntLine(self) -> bool: ...
    @overload
    def OutLine(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def OutLine(self) -> bool: ...
    def P1(self) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def P2(self) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    @overload
    def Rg1Line(self) -> bool: 
        """
        None

        None
        """
    @overload
    def Rg1Line(self,B : bool) -> None: ...
    @overload
    def RgNLine(self) -> bool: 
        """
        None

        None
        """
    @overload
    def RgNLine(self,B : bool) -> None: ...
    @overload
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    @overload
    def Shape(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self,x1 : float,y1 : float,x2 : float,y2 : float,S : OCP.TopoDS.TopoDS_Shape,reg1 : bool,regn : bool,outl : bool,intl : bool) -> None: ...
    @overload
    def __init__(self,thePoint1 : OCP.gp.gp_XY,thePoint2 : OCP.gp.gp_XY,S : OCP.TopoDS.TopoDS_Shape,reg1 : bool,regn : bool,outl : bool,intl : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class HLRBRep_BiPoint():
    """
    Contains the colors of a shape.
    """
    @overload
    def IntLine(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def IntLine(self) -> bool: ...
    @overload
    def OutLine(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def OutLine(self) -> bool: ...
    def P1(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def P2(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @overload
    def Rg1Line(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Rg1Line(self) -> bool: ...
    @overload
    def RgNLine(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def RgNLine(self) -> bool: ...
    @overload
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    @overload
    def Shape(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self,x1 : float,y1 : float,z1 : float,x2 : float,y2 : float,z2 : float,S : OCP.TopoDS.TopoDS_Shape,reg1 : bool,regn : bool,outl : bool,intl : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class HLRBRep_CInter(OCP.IntRes2d.IntRes2d_Intersection):
    """
    None
    """
    def GetMinNbSamples(self) -> int: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        returns TRUE when the computation was successful.

        returns TRUE when the computation was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.

        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbPoints(self) -> int: 
        """
        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbSegments(self) -> int: 
        """
        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def Point(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionPoint: 
        """
        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def Segment(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionSegment: 
        """
        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def SetMinNbSamples(self,theMinNbSamples : int) -> None: 
        """
        Set / get minimum number of points in polygon intersection.
        """
    @overload
    def SetReversedParameters(self,Reverseflag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetReversedParameters(self,flag : bool) -> None: ...
    def __init__(self) -> None: ...
    pass
class HLRBRep_CLProps():
    """
    None
    """
    def CentreOfCurvature(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns the centre of curvature <P>.
        """
    def Curvature(self) -> float: 
        """
        Returns the curvature.
        """
    def D1(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the first derivative. The derivative is computed if it has not been yet.
        """
    def D2(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the second derivative. The derivative is computed if it has not been yet.
        """
    def D3(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the third derivative. The derivative is computed if it has not been yet.
        """
    def IsTangentDefined(self) -> bool: 
        """
        Returns True if the tangent is defined. For example, the tangent is not defined if the three first derivatives are all null.
        """
    def Normal(self,N : OCP.gp.gp_Dir2d) -> None: 
        """
        Returns the normal direction <N>.
        """
    def SetParameter(self,U : float) -> None: 
        """
        Initializes the local properties of the curve for the parameter value <U>.
        """
    def Tangent(self,D : OCP.gp.gp_Dir2d) -> None: 
        """
        output the tangent direction <D>
        """
    def Value(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the Point.
        """
    def __init__(self,N : int,Resolution : float) -> None: ...
    pass
class HLRBRep_Curve():
    """
    Defines a 2d curve by projection of a 3D curve on a plane with an optional perspective transformation.
    """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Curve(self) -> OCP.BRepAdaptor.BRepAdaptor_Curve: 
        """
        Sets the 3D curve to be projected.

        Returns the 3D curve.

        Returns the 3D curve.
        """
    @overload
    def Curve(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the 3D point of parameter U on the curve.

        Computes the point of parameter U on the curve.

        Computes the 3D point of parameter U on the curve.
        """
    @overload
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative.

        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.

        Computes the point of parameter U on the curve with its first derivative.
        """
    @overload
    def D1(self,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: ...
    def D2(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Raised if the continuity of the current interval is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    def Degree(self) -> int: 
        """
        None

        None
        """
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        None

        None
        """
    def GetCurve(self) -> OCP.BRepAdaptor.BRepAdaptor_Curve: 
        """
        Returns the 3D curve.

        Returns the 3D curve.
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.

        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        None
        """
    @overload
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.

        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @overload
    def Intervals(self,Tab : OCP.TColStd.TColStd_Array1OfReal,Sh : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def IsClosed(self) -> bool: 
        """
        None

        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None

        None
        """
    def IsRational(self) -> bool: 
        """
        None

        None
        """
    def Knots(self,kn : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        None

        None
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    def Multiplicities(self,mu : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        If necessary, breaks the curve in intervals of continuity <S>. And returns the number of intervals.

        If necessary, breaks the curve in intervals of continuity <S>. And returns the number of intervals.
        """
    def NbKnots(self) -> int: 
        """
        None

        None
        """
    def NbPoles(self) -> int: 
        """
        None

        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    def Parameter2d(self,P3d : float) -> float: 
        """
        Returns the parameter on the 2d curve from the parameter on the 3d curve.
        """
    def Parameter3d(self,P2d : float) -> float: 
        """
        Returns the parameter on the 3d curve from the parameter on the 2d curve.
        """
    def Period(self) -> float: 
        """
        None

        None
        """
    @overload
    def Poles(self,aCurve : OCP.Geom.Geom_BSplineCurve,TP : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        None

        None
        """
    @overload
    def Poles(self,TP : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @overload
    def PolesAndWeights(self,TP : OCP.TColgp.TColgp_Array1OfPnt2d,TW : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None
        """
    @overload
    def PolesAndWeights(self,aCurve : OCP.Geom.Geom_BSplineCurve,TP : OCP.TColgp.TColgp_Array1OfPnt2d,TW : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    def Projector(self,Proj : OCP.HLRAlgo.HLRAlgo_Projector) -> None: 
        """
        None
        """
    def Resolution(self,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.

        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    def Tangent(self,AtStart : bool,P : OCP.gp.gp_Pnt2d,D : OCP.gp.gp_Dir2d) -> None: 
        """
        Depending on <AtStart> computes the 2D point and tangent on the curve at sart (or at end). If the first derivative is null look after at start (or before at end) with the second derivative.
        """
    def Update(self,TotMin : float,TotMax : float) -> float: 
        """
        Update the minmax and the internal data
        """
    def UpdateMinMax(self,TotMin : float,TotMax : float) -> float: 
        """
        Update the minmax returns tol for enlarge;
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.

        Computes the point of parameter U on the curve.
        """
    def Value3D(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the 3D point of parameter U on the curve.

        Computes the 3D point of parameter U on the curve.
        """
    def Z(self,U : float) -> float: 
        """
        Computes the Z coordinate of the point of parameter U on the curve in the viewing coordinate system
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_CurveTool():
    """
    None
    """
    @staticmethod
    def BSpline_s(C : capsule) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : capsule) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : capsule) -> OCP.gp.gp_Circ2d: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : capsule) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : capsule,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Computes the point of parameter U on the curve.
        """
    @staticmethod
    def D1_s(C : capsule,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    @staticmethod
    def D2_s(C : capsule,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    @staticmethod
    def D3_s(C : capsule,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    @staticmethod
    def DN_s(C : capsule,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    @staticmethod
    def Degree_s(C : capsule) -> int: 
        """
        None
        """
    @staticmethod
    def Ellipse_s(C : capsule) -> OCP.gp.gp_Elips2d: 
        """
        None
        """
    @staticmethod
    def EpsX_s(C : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def GetInterval_s(C : capsule,Index : int,Tab : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float, float]: 
        """
        output the bounds of interval of index <Index> used if Type == Composite.
        """
    @staticmethod
    def GetType_s(C : capsule) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Hyperbola_s(C : capsule) -> OCP.gp.gp_Hypr2d: 
        """
        None
        """
    @staticmethod
    def Intervals_s(C : capsule,T : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def IsClosed_s(C : capsule) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPeriodic_s(C : capsule) -> bool: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : capsule) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : capsule) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(myclass) >= <S>
        """
    @staticmethod
    @overload
    def NbSamples_s(C : capsule,U0 : float,U1 : float) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbSamples_s(C : capsule) -> int: ...
    @staticmethod
    def Parabola_s(C : capsule) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @staticmethod
    def Period_s(C : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : capsule,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    @staticmethod
    def TheType_s(C : capsule) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Value_s(C : capsule,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_Data(OCP.Standard.Standard_Transient):
    def AboveInterference(self) -> bool: 
        """
        Returns True if the rejected interference is above the face.
        """
    def Classify(self,E : int,ED : HLRBRep_EdgeData,LevelFlag : bool,Level : int,param : float) -> OCP.TopAbs.TopAbs_State: 
        """
        Classification of an edge.
        """
    def Compare(self,E : int,ED : HLRBRep_EdgeData) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the state of the Edge <ED> after classification.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EDataArray(self) -> HLRBRep_Array1OfEData: 
        """
        None

        None
        """
    def Edge(self) -> int: 
        """
        Returns the current Edge
        """
    def EdgeMap(self) -> OCP.TopTools.TopTools_IndexedMapOfShape: 
        """
        None

        None
        """
    @overload
    def EdgeOfTheHidingFace(self,arg1 : int,ED : HLRBRep_EdgeData) -> bool: 
        """
        Returns the true if the Edge <ED> belongs to the Hiding Face.

        Returns the true if the Edge <ED> belongs to the Hiding Face.
        """
    @overload
    def EdgeOfTheHidingFace(self,E : int,ED : HLRBRep_EdgeData) -> bool: ...
    def EdgeState(self,p1 : float,p2 : float,stbef : OCP.TopAbs.TopAbs_State,staf : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Returns the local 3D state of the intersection between the current edge and the current face at the <p1> and <p2> parameters.
        """
    def FDataArray(self) -> HLRBRep_Array1OfFData: 
        """
        None

        None
        """
    def FaceMap(self) -> OCP.TopTools.TopTools_IndexedMapOfShape: 
        """
        None

        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HidingStartLevel(self,E : int,ED : HLRBRep_EdgeData,IL : OCP.HLRAlgo.HLRAlgo_InterferenceList) -> int: 
        """
        Returns the number of levels of hiding face above the first point of the edge <ED>. The InterferenceList is given to compute far away of the Interferences and then come back.
        """
    def HidingTheFace(self) -> bool: 
        """
        Returns true if the current edge to be hidden belongs to the hiding face.

        Returns true if the current edge to be hidden belongs to the hiding face.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitBoundSort(self,MinMaxTot : Any,e1 : int,e2 : int) -> None: 
        """
        to compare with only non rejected edges.
        """
    def InitEdge(self,FI : int,MST : OCP.BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool) -> None: 
        """
        Begin an iteration only on visible Edges crossing the face number <FI>.
        """
    def InitInterference(self) -> None: 
        """
        Intersect the current Edge with the boundary of the hiding face. The interferences are given by the More, Next, and Value methods.
        """
    def Interference(self) -> OCP.HLRAlgo.HLRAlgo_Interference: 
        """
        None

        None
        """
    def IsBadFace(self) -> bool: 
        """
        Returns true if the current face is bad.
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
    def LocalFEGeometry2D(self,FE : int,Param : float,Tg : OCP.gp.gp_Dir2d,Nm : OCP.gp.gp_Dir2d) -> Tuple[float]: 
        """
        Returns the local description of the projection of the current FEdge at parameter <Param>.
        """
    def LocalLEGeometry2D(self,Param : float,Tg : OCP.gp.gp_Dir2d,Nm : OCP.gp.gp_Dir2d) -> Tuple[float]: 
        """
        Returns the local description of the projection of the current LEdge at parameter <Param>.
        """
    def MoreEdge(self) -> bool: 
        """
        None
        """
    def MoreInterference(self) -> bool: 
        """
        None

        None
        """
    def NbEdges(self) -> int: 
        """
        None

        None
        """
    def NbFaces(self) -> int: 
        """
        None

        None
        """
    def NbVertices(self) -> int: 
        """
        None

        None
        """
    def NextEdge(self,skip : bool=True) -> None: 
        """
        None
        """
    def NextInterference(self) -> None: 
        """
        None
        """
    def Projector(self) -> OCP.HLRAlgo.HLRAlgo_Projector: 
        """
        None

        None
        """
    def RejectedInterference(self) -> bool: 
        """
        Returns True if the interference is rejected.
        """
    def SimplClassify(self,E : int,ED : HLRBRep_EdgeData,Nbp : int,p1 : float,p2 : float) -> OCP.TopAbs.TopAbs_State: 
        """
        Simple classification of part of edge [p1, p2] returns OUT if at least 1 of Nbp points of edge is out othewise returns IN It is used to check "suspision" hided part of edge.
        """
    def SimpleHidingFace(self) -> bool: 
        """
        Returns true if the current hiding face is not an auto-intersected one.

        Returns true if the current hiding face is not an auto-intersected one.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tolerance(self,tol : float) -> None: 
        """
        Set the tolerance for the rejections during the exploration

        returns the tolerance for the rejections during the exploration

        Set the tolerance for the rejections during the exploration

        returns the tolerance for the rejections during the exploration
        """
    @overload
    def Tolerance(self) -> float: ...
    def Update(self,P : OCP.HLRAlgo.HLRAlgo_Projector) -> None: 
        """
        end of building of the Data and updating all the informations linked to the projection.
        """
    def Write(self,DS : HLRBRep_Data,dv : int,de : int,df : int) -> None: 
        """
        Write <DS> in me with a translation of <dv>,<de>,<df>.
        """
    def __init__(self,NV : int,NE : int,NF : int) -> None: ...
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
class HLRBRep_EdgeBuilder():
    """
    None
    """
    def AreaEdgeState(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the edge state of the current area.
        """
    def AreaState(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the state of the current area.
        """
    def Builds(self,ToBuild : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Reinitialize the results iteration to the parts with State <ToBuild>. If this method is not called after construction the default is <ToBuild> = IN.
        """
    def Current(self) -> OCP.HLRAlgo.HLRAlgo_Intersection: 
        """
        Returns the current vertex of the current edge.
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def HasArea(self) -> bool: 
        """
        Returns True if there is a current area.
        """
    def InitAreas(self) -> None: 
        """
        Initialize an iteration on the areas.
        """
    def IsBoundary(self) -> bool: 
        """
        Returns True if the current vertex comes from the boundary of the edge.
        """
    def IsInterference(self) -> bool: 
        """
        Returns True if the current vertex was an interference.
        """
    def LeftLimit(self) -> HLRBRep_AreaLimit: 
        """
        Returns the AreaLimit beginning the current area. This is a NULL handle when the area is infinite on the left.
        """
    def MoreEdges(self) -> bool: 
        """
        Returns True if there are more new edges to build.
        """
    def MoreVertices(self) -> bool: 
        """
        True if there are more vertices in the current new edge.
        """
    def NextArea(self) -> None: 
        """
        Set the current area to the next area.
        """
    def NextEdge(self) -> None: 
        """
        Proceeds to the next edge to build. Skip all remaining vertices on the current edge.
        """
    def NextVertex(self) -> None: 
        """
        Proceeds to the next vertex of the current edge.
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the new orientation of the current vertex.
        """
    def PreviousArea(self) -> None: 
        """
        Set the current area to the previous area.
        """
    def RightLimit(self) -> HLRBRep_AreaLimit: 
        """
        Returns the AreaLimit ending the current area. This is a NULL handle when the area is infinite on the right.
        """
    def __init__(self,VList : HLRBRep_VertexList) -> None: ...
    pass
class HLRBRep_EdgeData():
    """
    None
    """
    @overload
    def AutoIntersectionDone(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def AutoIntersectionDone(self) -> bool: ...
    def ChangeGeometry(self) -> HLRBRep_Curve: 
        """
        None

        None
        """
    def Curve(self) -> HLRBRep_Curve: 
        """
        None
        """
    @overload
    def CutAtEnd(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def CutAtEnd(self) -> bool: ...
    @overload
    def CutAtSta(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def CutAtSta(self) -> bool: ...
    def Geometry(self) -> HLRBRep_Curve: 
        """
        None

        None
        """
    @overload
    def HideCount(self,I : int) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def HideCount(self) -> int: ...
    def MinMax(self) -> Any: 
        """
        None
        """
    @overload
    def OutLVEnd(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def OutLVEnd(self) -> bool: ...
    @overload
    def OutLVSta(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def OutLVSta(self) -> bool: ...
    @overload
    def Rg1Line(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Rg1Line(self) -> bool: ...
    @overload
    def RgNLine(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def RgNLine(self,B : bool) -> None: ...
    @overload
    def Selected(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Selected(self) -> bool: ...
    def Set(self,Reg1 : bool,RegN : bool,EG : OCP.TopoDS.TopoDS_Edge,V1 : int,V2 : int,Out1 : bool,Out2 : bool,Cut1 : bool,Cut2 : bool,Start : float,TolStart : float,End : float,TolEnd : float) -> None: 
        """
        None
        """
    @overload
    def Simple(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def Simple(self,B : bool) -> None: ...
    def Status(self) -> OCP.HLRAlgo.HLRAlgo_EdgeStatus: 
        """
        None

        None
        """
    def Tolerance(self) -> float: 
        """
        None

        None
        """
    def UpdateMinMax(self,theTotMinMax : Any) -> None: 
        """
        None
        """
    @overload
    def Used(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def Used(self,B : bool) -> None: ...
    @overload
    def VEnd(self,I : int) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def VEnd(self) -> int: ...
    @overload
    def VSta(self) -> int: 
        """
        None

        None

        None

        None
        """
    @overload
    def VSta(self,I : int) -> None: ...
    @overload
    def VerAtEnd(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def VerAtEnd(self,B : bool) -> None: ...
    @overload
    def VerAtSta(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def VerAtSta(self,B : bool) -> None: ...
    @overload
    def Vertical(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Vertical(self) -> bool: ...
    def __init__(self) -> None: ...
    pass
class HLRBRep_EdgeFaceTool():
    """
    The EdgeFaceTool computes the UV coordinates at a given parameter on a Curve and a Surface. It also compute the signed curvature value in a direction at a given u,v point on a surface.
    """
    @staticmethod
    def CurvatureValue_s(F : capsule,U : float,V : float,Tg : OCP.gp.gp_Dir) -> float: 
        """
        None
        """
    @staticmethod
    def UVPoint_s(Par : float,E : capsule,F : capsule,U : float,V : float) -> bool: 
        """
        return True if U and V are found.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_EdgeIList():
    """
    None
    """
    @staticmethod
    def AddInterference_s(IL : OCP.HLRAlgo.HLRAlgo_InterferenceList,I : OCP.HLRAlgo.HLRAlgo_Interference,T : HLRBRep_EdgeInterferenceTool) -> None: 
        """
        Add the interference <I> to the list <IL>.
        """
    @staticmethod
    def ProcessComplex_s(IL : OCP.HLRAlgo.HLRAlgo_InterferenceList,T : HLRBRep_EdgeInterferenceTool) -> None: 
        """
        Process complex transitions on the list IL.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_EdgeInterferenceTool():
    """
    Implements the methods required to instantiates the EdgeInterferenceList from HLRAlgo.
    """
    def CurrentOrientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    def CurrentParameter(self) -> float: 
        """
        None

        None
        """
    def CurrentVertex(self) -> OCP.HLRAlgo.HLRAlgo_Intersection: 
        """
        None

        None
        """
    def EdgeGeometry(self,Param : float,Tgt : OCP.gp.gp_Dir,Nrm : OCP.gp.gp_Dir) -> Tuple[float]: 
        """
        Returns local geometric description of the Edge at parameter <Para>. See method Reset of class EdgeFaceTransition from TopCnx for other arguments.
        """
    def InitVertices(self) -> None: 
        """
        None

        None
        """
    def InterferenceBoundaryGeometry(self,I : OCP.HLRAlgo.HLRAlgo_Interference,Tang : OCP.gp.gp_Dir,Norm : OCP.gp.gp_Dir) -> Tuple[float]: 
        """
        Returns the geometry of the boundary at the interference <I>. See the AddInterference method of the class EdgeFaceTransition from TopCnx for the other arguments.
        """
    def IsPeriodic(self) -> bool: 
        """
        None

        None
        """
    def LoadEdge(self) -> None: 
        """
        None
        """
    def MoreVertices(self) -> bool: 
        """
        None

        None
        """
    def NextVertex(self) -> None: 
        """
        None

        None
        """
    def ParameterOfInterference(self,I : OCP.HLRAlgo.HLRAlgo_Interference) -> float: 
        """
        None

        None
        """
    def SameInterferences(self,I1 : OCP.HLRAlgo.HLRAlgo_Interference,I2 : OCP.HLRAlgo.HLRAlgo_Interference) -> bool: 
        """
        True if the two interferences are on the same geometric locus.
        """
    def SameVertexAndInterference(self,I : OCP.HLRAlgo.HLRAlgo_Interference) -> bool: 
        """
        True if the Interference and the current Vertex are on the same geometric locus.
        """
    def __init__(self,DS : HLRBRep_Data) -> None: ...
    pass
class HLRBRep_ExactIntersectionPointOfTheIntPCurvePCurveOfCInter():
    """
    None
    """
    def AnErrorOccurred(self) -> bool: 
        """
        None
        """
    def NbRoots(self) -> int: 
        """
        None
        """
    @overload
    def Perform(self,Uo : float,Vo : float,UInf : float,VInf : float,USup : float,VSup : float) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,Poly1 : HLRBRep_ThePolygon2dOfTheIntPCurvePCurveOfCInter,Poly2 : HLRBRep_ThePolygon2dOfTheIntPCurvePCurveOfCInter) -> Tuple[int, int, float, float]: ...
    def Roots(self) -> Tuple[float, float]: 
        """
        None
        """
    pass
class HLRBRep_FaceData():
    """
    None
    """
    @overload
    def Back(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Back(self) -> bool: ...
    @overload
    def Closed(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Closed(self) -> bool: ...
    @overload
    def Cone(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Cone(self) -> bool: ...
    @overload
    def Cut(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def Cut(self,B : bool) -> None: ...
    @overload
    def Cylinder(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Cylinder(self) -> bool: ...
    def Geometry(self) -> HLRBRep_Surface: 
        """
        None

        None
        """
    @overload
    def Hiding(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def Hiding(self,B : bool) -> None: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None

        None

        None
        """
    @overload
    def Orientation(self,O : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def Plane(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Plane(self) -> bool: ...
    @overload
    def Selected(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def Selected(self,B : bool) -> None: ...
    def Set(self,FG : OCP.TopoDS.TopoDS_Face,Or : OCP.TopAbs.TopAbs_Orientation,Cl : bool,NW : int) -> None: 
        """
        <Or> is the orientation of the face. <Cl> is true if the face belongs to a closed volume. <NW> is the number of wires ( or block of edges ) of the face.
        """
    def SetWEdge(self,WI : int,EWI : int,EI : int,Or : OCP.TopAbs.TopAbs_Orientation,OutL : bool,Inte : bool,Dble : bool,IsoL : bool) -> None: 
        """
        Set the edge number <EWI> of the wire <WI>.
        """
    def SetWire(self,WI : int,NE : int) -> None: 
        """
        Set <NE> the number of edges of the wire number <WI>.
        """
    @overload
    def Side(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def Side(self,B : bool) -> None: ...
    @overload
    def Simple(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def Simple(self,B : bool) -> None: ...
    @overload
    def Size(self,S : float) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Size(self) -> float: ...
    @overload
    def Sphere(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Sphere(self) -> bool: ...
    def Tolerance(self) -> float: 
        """
        None

        None
        """
    @overload
    def Torus(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def Torus(self,B : bool) -> None: ...
    def Wires(self) -> OCP.HLRAlgo.HLRAlgo_WiresBlock: 
        """
        None

        None
        """
    @overload
    def WithOutL(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def WithOutL(self,B : bool) -> None: ...
    def __init__(self) -> None: ...
    pass
class HLRBRep_FaceIterator():
    """
    None
    """
    def BeginningOfWire(self) -> bool: 
        """
        Returns True if the current edge is the first of a wire.

        Returns True if the current edge is the first of a wire.
        """
    def Double(self) -> bool: 
        """
        None

        None
        """
    def Edge(self) -> int: 
        """
        None

        None
        """
    def EndOfWire(self) -> bool: 
        """
        Returns True if the current edge is the last of a wire.

        Returns True if the current edge is the last of a wire.
        """
    def InitEdge(self,fd : HLRBRep_FaceData) -> None: 
        """
        Begin an exploration of the edges of the face <fd>
        """
    def Internal(self) -> bool: 
        """
        None

        None
        """
    def IsoLine(self) -> bool: 
        """
        None

        None
        """
    def MoreEdge(self) -> bool: 
        """
        None

        None
        """
    def NextEdge(self) -> None: 
        """
        None
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    def OutLine(self) -> bool: 
        """
        None

        None
        """
    def SkipWire(self) -> None: 
        """
        Skip the current wire in the exploration.

        Skip the current wire in the exploration.
        """
    def Wire(self) -> OCP.HLRAlgo.HLRAlgo_EdgesBlock: 
        """
        Returns the edges of the current wire.

        Returns the edges of the current wire.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_HLRToShape():
    """
    A framework for filtering the computation results of an HLRBRep_Algo algorithm by extraction. From the results calculated by the algorithm on a shape, a filter returns the type of edge you want to identify. You can choose any of the following types of output: - visible sharp edges - hidden sharp edges - visible smooth edges - hidden smooth edges - visible sewn edges - hidden sewn edges - visible outline edges - hidden outline edges. - visible isoparameters and - hidden isoparameters. Sharp edges present a C0 continuity (non G1). Smooth edges present a G1 continuity (non G2). Sewn edges present a C2 continuity. The result is composed of 2D edges in the projection plane of the view which the algorithm has worked with. These 2D edges are not included in the data structure of the visualized shape. In order to obtain a complete image, you must combine the shapes given by each of the chosen filters. The construction of the shape does not call a new computation of the algorithm, but only reads its internal results. The methods of this shape are almost identic to those of the HLRBrep_PolyHLRToShape class.
    """
    @overload
    def CompoundOfEdges(self,type : HLRBRep_TypeOfResultingEdge,visible : bool,In3d : bool) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns compound of resulting edges of required type and visibility, taking into account the kind of space (2d or 3d)

        For specified shape returns compound of resulting edges of required type and visibility, taking into account the kind of space (2d or 3d)

        Returns compound of resulting edges of required type and visibility, taking into account the kind of space (2d or 3d)

        For specified shape returns compound of resulting edges of required type and visibility, taking into account the kind of space (2d or 3d)
        """
    @overload
    def CompoundOfEdges(self,S : OCP.TopoDS.TopoDS_Shape,type : HLRBRep_TypeOfResultingEdge,visible : bool,In3d : bool) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def HCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def HCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def IsoLineHCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def IsoLineHCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def IsoLineVCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def IsoLineVCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def OutLineHCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def OutLineHCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def OutLineVCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def OutLineVCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    def OutLineVCompound3d(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    @overload
    def Rg1LineHCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def Rg1LineHCompound(self) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def Rg1LineVCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def Rg1LineVCompound(self) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def RgNLineHCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def RgNLineHCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def RgNLineVCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def RgNLineVCompound(self) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def VCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def VCompound(self) -> OCP.TopoDS.TopoDS_Shape: ...
    def __init__(self,A : HLRBRep_Algo) -> None: ...
    pass
class HLRBRep_Hider():
    """
    None
    """
    def Hide(self,FI : int,MST : OCP.BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool) -> None: 
        """
        Removes from the edges, the parts hidden by the hiding face number <FI>.
        """
    def OwnHiding(self,FI : int) -> None: 
        """
        own hiding the side face number <FI>.
        """
    def __init__(self,DS : HLRBRep_Data) -> None: ...
    pass
class HLRBRep_IntConicCurveOfCInter(OCP.IntRes2d.IntRes2d_Intersection):
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        returns TRUE when the computation was successful.

        returns TRUE when the computation was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.

        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbPoints(self) -> int: 
        """
        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbSegments(self) -> int: 
        """
        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def Point(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionPoint: 
        """
        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def Segment(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionSegment: 
        """
        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    @overload
    def SetReversedParameters(self,Reverseflag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetReversedParameters(self,flag : bool) -> None: ...
    def __init__(self) -> None: ...
    pass
class HLRBRep_InterCSurf(OCP.IntCurveSurface.IntCurveSurface_Intersection):
    """
    None
    """
    def Dump(self) -> None: 
        """
        Dump all the fields.
        """
    def IsDone(self) -> bool: 
        """
        returns the <done> field.
        """
    def IsParallel(self) -> bool: 
        """
        Returns true if curve is parallel or belongs surface This case is recognized only for some pairs of analytical curves and surfaces (plane - line, ...)
        """
    def NbPoints(self) -> int: 
        """
        returns the number of IntersectionPoint if IsDone returns True. else NotDone is raised.
        """
    def NbSegments(self) -> int: 
        """
        returns the number of IntersectionSegment if IsDone returns True. else NotDone is raised.
        """
    def Point(self,Index : int) -> OCP.IntCurveSurface.IntCurveSurface_IntersectionPoint: 
        """
        returns the IntersectionPoint of range <Index> raises NotDone if the computation has failed or if the computation has not been done raises OutOfRange if Index is not in the range <1..NbPoints>
        """
    def Segment(self,Index : int) -> OCP.IntCurveSurface.IntCurveSurface_IntersectionSegment: 
        """
        returns the IntersectionSegment of range <Index> raises NotDone if the computation has failed or if the computation has not been done raises OutOfRange if Index is not in the range <1..NbSegment>
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_Algo(HLRBRep_InternalAlgo, OCP.Standard.Standard_Transient):
    """
    Inherited from InternalAlgo to provide methods with Shape from TopoDS. A framework to compute a shape as seen in a projection plane. This is done by calculating the visible and the hidden parts of the shape. HLRBRep_Algo works with three types of entity: - shapes to be visualized - edges in these shapes (these edges are the basic entities which will be visualized or hidden), and - faces in these shapes which hide the edges. HLRBRep_Algo is based on the principle of comparing each edge of the shape to be visualized with each of its faces, and calculating the visible and the hidden parts of each edge. For a given projection, HLRBRep_Algo calculates a set of lines characteristic of the object being represented. It is also used in conjunction with the HLRBRep_HLRToShape extraction utilities, which reconstruct a new, simplified shape from a selection of calculation results. This new shape is made up of edges, which represent the shape visualized in the projection. HLRBRep_Algo takes the shape itself into account whereas HLRBRep_PolyAlgo works with a polyhedral simplification of the shape. When you use HLRBRep_Algo, you obtain an exact result, whereas, when you use HLRBRep_PolyAlgo, you reduce computation time but obtain polygonal segments. In the case of complicated shapes, HLRBRep_Algo may be time-consuming. An HLRBRep_Algo object provides a framework for: - defining the point of view - identifying the shape or shapes to be visualized - calculating the outlines - calculating the visible and hidden lines of the shape. Warning - Superimposed lines are not eliminated by this algorithm. - There must be no unfinished objects inside the shape you wish to visualize. - Points are not treated. - Note that this is not the sort of algorithm used in generating shading, which calculates the visible and hidden parts of each face in a shape to be visualized by comparing each face in the shape with every other face in the same shape.Inherited from InternalAlgo to provide methods with Shape from TopoDS. A framework to compute a shape as seen in a projection plane. This is done by calculating the visible and the hidden parts of the shape. HLRBRep_Algo works with three types of entity: - shapes to be visualized - edges in these shapes (these edges are the basic entities which will be visualized or hidden), and - faces in these shapes which hide the edges. HLRBRep_Algo is based on the principle of comparing each edge of the shape to be visualized with each of its faces, and calculating the visible and the hidden parts of each edge. For a given projection, HLRBRep_Algo calculates a set of lines characteristic of the object being represented. It is also used in conjunction with the HLRBRep_HLRToShape extraction utilities, which reconstruct a new, simplified shape from a selection of calculation results. This new shape is made up of edges, which represent the shape visualized in the projection. HLRBRep_Algo takes the shape itself into account whereas HLRBRep_PolyAlgo works with a polyhedral simplification of the shape. When you use HLRBRep_Algo, you obtain an exact result, whereas, when you use HLRBRep_PolyAlgo, you reduce computation time but obtain polygonal segments. In the case of complicated shapes, HLRBRep_Algo may be time-consuming. An HLRBRep_Algo object provides a framework for: - defining the point of view - identifying the shape or shapes to be visualized - calculating the outlines - calculating the visible and hidden lines of the shape. Warning - Superimposed lines are not eliminated by this algorithm. - There must be no unfinished objects inside the shape you wish to visualize. - Points are not treated. - Note that this is not the sort of algorithm used in generating shading, which calculates the visible and hidden parts of each face in a shape to be visualized by comparing each face in the shape with every other face in the same shape.Inherited from InternalAlgo to provide methods with Shape from TopoDS. A framework to compute a shape as seen in a projection plane. This is done by calculating the visible and the hidden parts of the shape. HLRBRep_Algo works with three types of entity: - shapes to be visualized - edges in these shapes (these edges are the basic entities which will be visualized or hidden), and - faces in these shapes which hide the edges. HLRBRep_Algo is based on the principle of comparing each edge of the shape to be visualized with each of its faces, and calculating the visible and the hidden parts of each edge. For a given projection, HLRBRep_Algo calculates a set of lines characteristic of the object being represented. It is also used in conjunction with the HLRBRep_HLRToShape extraction utilities, which reconstruct a new, simplified shape from a selection of calculation results. This new shape is made up of edges, which represent the shape visualized in the projection. HLRBRep_Algo takes the shape itself into account whereas HLRBRep_PolyAlgo works with a polyhedral simplification of the shape. When you use HLRBRep_Algo, you obtain an exact result, whereas, when you use HLRBRep_PolyAlgo, you reduce computation time but obtain polygonal segments. In the case of complicated shapes, HLRBRep_Algo may be time-consuming. An HLRBRep_Algo object provides a framework for: - defining the point of view - identifying the shape or shapes to be visualized - calculating the outlines - calculating the visible and hidden lines of the shape. Warning - Superimposed lines are not eliminated by this algorithm. - There must be no unfinished objects inside the shape you wish to visualize. - Points are not treated. - Note that this is not the sort of algorithm used in generating shading, which calculates the visible and hidden parts of each face in a shape to be visualized by comparing each face in the shape with every other face in the same shape.
    """
    @overload
    def Add(self,S : OCP.TopoDS.TopoDS_Shape,SData : OCP.Standard.Standard_Transient,nbIso : int=0) -> None: 
        """
        add the Shape <S>.

        Adds the shape S to this framework, and specifies the number of isoparameters nbiso desired in visualizing S. You may add as many shapes as you wish. Use the function Add once for each shape.
        """
    @overload
    def Add(self,S : OCP.TopoDS.TopoDS_Shape,nbIso : int=0) -> None: ...
    def DataStructure(self) -> HLRBRep_Data: 
        """
        None
        """
    @overload
    def Debug(self,deb : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Debug(self) -> bool: ...
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def Hide(self) -> None: 
        """
        hide all the DataStructure.

        hide the Shape <S> by itself.

        hide the Shape <S1> by the shape <S2>.
        """
    @overload
    def Hide(self,I : int) -> None: ...
    @overload
    def Hide(self,I : int,J : int) -> None: ...
    @overload
    def HideAll(self,I : int) -> None: 
        """
        set to hide all the edges.

        set to hide all the edges of the Shape <S>.
        """
    @overload
    def HideAll(self) -> None: ...
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        return the index of the Shape <S> and return 0 if the Shape <S> is not found.
        """
    def InitEdgeStatus(self) -> None: 
        """
        init the status of the selected edges depending of the back faces of a closed shell.
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
    def Load(self,S : OCP.HLRTopoBRep.HLRTopoBRep_OutLiner,SData : OCP.Standard.Standard_Transient,nbIso : int=0) -> None: 
        """
        add the shape <S>.

        add the shape <S>.
        """
    @overload
    def Load(self,S : OCP.HLRTopoBRep.HLRTopoBRep_OutLiner,nbIso : int=0) -> None: ...
    def NbShapes(self) -> int: 
        """
        None
        """
    def OutLinedShapeNullify(self) -> None: 
        """
        nullify all the results of OutLiner from HLRTopoBRep.
        """
    def PartialHide(self) -> None: 
        """
        own hiding of all the shapes of the DataStructure without hiding by each other.
        """
    @overload
    def Projector(self) -> OCP.HLRAlgo.HLRAlgo_Projector: 
        """
        set the projector.

        set the projector.
        """
    @overload
    def Projector(self,P : OCP.HLRAlgo.HLRAlgo_Projector) -> None: ...
    def Remove(self,I : int) -> None: 
        """
        remove the Shape of Index <I>.
        """
    @overload
    def Select(self,I : int) -> None: 
        """
        select all the DataStructure.

        select only the Shape of index <I>.
        """
    @overload
    def Select(self) -> None: ...
    def SelectEdge(self,I : int) -> None: 
        """
        select only the edges of the Shape <S>.
        """
    def SelectFace(self,I : int) -> None: 
        """
        select only the faces of the Shape <S>.
        """
    def SeqOfShapeBounds(self) -> HLRBRep_SeqOfShapeBounds: 
        """
        None
        """
    def ShapeBounds(self,I : int) -> HLRBRep_ShapeBounds: 
        """
        None
        """
    def ShapeData(self,I : int,SData : OCP.Standard.Standard_Transient) -> None: 
        """
        Change the Shape Data of the Shape of index <I>.
        """
    @overload
    def ShowAll(self) -> None: 
        """
        set to visible all the edges.

        set to visible all the edges of the Shape <S>.
        """
    @overload
    def ShowAll(self,I : int) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self) -> None: 
        """
        update the DataStructure.
        """
    @overload
    def __init__(self,A : HLRBRep_Algo) -> None: ...
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
class HLRBRep_Intersector():
    """
    The Intersector computes 2D intersections of the projections of 3D curves.
    """
    def CSPoint(self,N : int) -> OCP.IntCurveSurface.IntCurveSurface_IntersectionPoint: 
        """
        None
        """
    def CSSegment(self,N : int) -> OCP.IntCurveSurface.IntCurveSurface_IntersectionSegment: 
        """
        None
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
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
    @overload
    def Perform(self,L : OCP.gp.gp_Lin,P : float) -> None: 
        """
        Performs the auto intersection of an edge. The edge domain is cutted at start with da1*(b-a) and at end with db1*(b-a).

        Performs the intersection between the two edges. The edges domains are cutted at start with da*(b-a) and at end with db*(b-a).

        None
        """
    @overload
    def Perform(self,A1 : capsule,da1 : float,db1 : float) -> None: ...
    @overload
    def Perform(self,nA : int,A1 : capsule,da1 : float,db1 : float,nB : int,A2 : capsule,da2 : float,db2 : float,NoBound : bool) -> None: ...
    def Point(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionPoint: 
        """
        None
        """
    def Segment(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionSegment: 
        """
        None
        """
    def SimulateOnePoint(self,A1 : capsule,U : float,A2 : capsule,V : float) -> None: 
        """
        Create a single IntersectionPoint (U on A1) (V on A2) The point is middle on both curves.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_LineTool():
    """
    The LineTool class provides class methods to access the methodes of the Line.
    """
    @staticmethod
    def BSpline_s(C : OCP.gp.gp_Lin) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : OCP.gp.gp_Lin) -> OCP.Geom.Geom_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : OCP.gp.gp_Lin) -> OCP.gp.gp_Circ: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : OCP.gp.gp_Lin) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : OCP.gp.gp_Lin,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U on the line.
        """
    @staticmethod
    def D1_s(C : OCP.gp.gp_Lin,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U on the line with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    @staticmethod
    def D2_s(C : OCP.gp.gp_Lin,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    @staticmethod
    def D3_s(C : OCP.gp.gp_Lin,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    @staticmethod
    def DN_s(C : OCP.gp.gp_Lin,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    @staticmethod
    def Degree_s(C : OCP.gp.gp_Lin) -> int: 
        """
        None
        """
    @staticmethod
    def Ellipse_s(C : OCP.gp.gp_Lin) -> OCP.gp.gp_Elips: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.gp.gp_Lin) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(C : OCP.gp.gp_Lin) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the line in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Hyperbola_s(C : OCP.gp.gp_Lin) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    @staticmethod
    def IntervalContinuity_s(C : OCP.gp.gp_Lin) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def IntervalFirst_s(C : OCP.gp.gp_Lin) -> float: 
        """
        Returns the first parameter of the current interval.
        """
    @staticmethod
    def IntervalLast_s(C : OCP.gp.gp_Lin) -> float: 
        """
        Returns the last parameter of the current interval.
        """
    @staticmethod
    def Intervals_s(C : OCP.gp.gp_Lin,T : OCP.TColStd.TColStd_Array1OfReal,Sh : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Sets the current working interval.
        """
    @staticmethod
    def IsClosed_s(C : OCP.gp.gp_Lin) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPeriodic_s(C : OCP.gp.gp_Lin) -> bool: 
        """
        None
        """
    @staticmethod
    def IsRational_s(C : OCP.gp.gp_Lin) -> bool: 
        """
        None
        """
    @staticmethod
    def KnotsAndMultiplicities_s(C : OCP.gp.gp_Lin,TK : OCP.TColStd.TColStd_Array1OfReal,TM : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.gp.gp_Lin) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.gp.gp_Lin) -> OCP.gp.gp_Lin: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : OCP.gp.gp_Lin,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        If necessary, breaks the line in intervals of continuity <S>. And returns the number of intervals.
        """
    @staticmethod
    def NbKnots_s(C : OCP.gp.gp_Lin) -> int: 
        """
        None
        """
    @staticmethod
    def NbPoles_s(C : OCP.gp.gp_Lin) -> int: 
        """
        None
        """
    @staticmethod
    def NbSamples_s(C : OCP.gp.gp_Lin,U0 : float,U1 : float) -> int: 
        """
        None
        """
    @staticmethod
    def Parabola_s(C : OCP.gp.gp_Lin) -> OCP.gp.gp_Parab: 
        """
        None
        """
    @staticmethod
    def Period_s(C : OCP.gp.gp_Lin) -> float: 
        """
        None
        """
    @staticmethod
    def PolesAndWeights_s(C : OCP.gp.gp_Lin,TP : OCP.TColgp.TColgp_Array1OfPnt,TW : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    @staticmethod
    def Poles_s(C : OCP.gp.gp_Lin,TP : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : OCP.gp.gp_Lin,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    @staticmethod
    def SamplePars_s(C : OCP.gp.gp_Lin,U0 : float,U1 : float,Defl : float,NbMin : int,Pars : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    @staticmethod
    def Value_s(C : OCP.gp.gp_Lin,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the line.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_ListOfBPnt2D(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : HLRBRep_ListOfBPnt2D) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : HLRBRep_BiPnt2D) -> HLRBRep_BiPnt2D: ...
    @overload
    def Append(self,theItem : HLRBRep_BiPnt2D,theIter : Any) -> None: ...
    def Assign(self,theOther : HLRBRep_ListOfBPnt2D) -> HLRBRep_ListOfBPnt2D: 
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
    def First(self) -> HLRBRep_BiPnt2D: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : HLRBRep_BiPnt2D,theIter : Any) -> HLRBRep_BiPnt2D: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : HLRBRep_ListOfBPnt2D,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : HLRBRep_BiPnt2D,theIter : Any) -> HLRBRep_BiPnt2D: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : HLRBRep_ListOfBPnt2D,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> HLRBRep_BiPnt2D: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : HLRBRep_ListOfBPnt2D) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : HLRBRep_BiPnt2D) -> HLRBRep_BiPnt2D: ...
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
    def __init__(self,theOther : HLRBRep_ListOfBPnt2D) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRBRep_ListOfBPoint(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : HLRBRep_ListOfBPoint) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : HLRBRep_BiPoint) -> HLRBRep_BiPoint: ...
    @overload
    def Append(self,theItem : HLRBRep_BiPoint,theIter : Any) -> None: ...
    def Assign(self,theOther : HLRBRep_ListOfBPoint) -> HLRBRep_ListOfBPoint: 
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
    def First(self) -> HLRBRep_BiPoint: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : HLRBRep_BiPoint,theIter : Any) -> HLRBRep_BiPoint: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : HLRBRep_ListOfBPoint,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : HLRBRep_ListOfBPoint,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : HLRBRep_BiPoint,theIter : Any) -> HLRBRep_BiPoint: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> HLRBRep_BiPoint: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : HLRBRep_BiPoint) -> HLRBRep_BiPoint: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : HLRBRep_ListOfBPoint) -> None: ...
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
    def __init__(self,theOther : HLRBRep_ListOfBPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRBRep_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfCInter(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,Param : float,D : float) -> bool: 
        """
        Computes the derivative of the previous function at parameter Param.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,Param : float,F : float) -> bool: 
        """
        Computes the value of the signed distance between the implicit curve and the point at parameter Param on the parametrised curve.
        """
    def Values(self,Param : float,F : float,D : float) -> bool: 
        """
        Computes the value and the derivative of the function.
        """
    pass
class HLRBRep_PCLocFOfTheLocateExtPCOfTheProjPCurOfCInter(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,U : float,DF : float) -> bool: 
        """
        Calculation of F'(U).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Shows if the Nth distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Return the nunber of found extrema.
        """
    def Point(self,N : int) -> OCP.Extrema.Extrema_POnCurv2d: 
        """
        Returns the Nth extremum.
        """
    def SearchOfTolerance(self) -> float: 
        """
        Computes a Tol value. If 1st derivative of curve |D1|<Tol, it is considered D1=0.
        """
    def SetPoint(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        sets the field P of the function.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the Nth distance.
        """
    def SubIntervalInitialize(self,theUfirst : float,theUlast : float) -> None: 
        """
        Determines boundaries of subinterval for find of root.
        """
    def Value(self,U : float,F : float) -> bool: 
        """
        Calculation of F(U).
        """
    def Values(self,U : float,F : float,DF : float) -> bool: 
        """
        Calculation of F(U) and F'(U).
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_PolyAlgo(OCP.Standard.Standard_Transient):
    """
    to remove Hidden lines on Shapes with Triangulations. A framework to compute the shape as seen in a projection plane. This is done by calculating the visible and the hidden parts of the shape. HLRBRep_PolyAlgo works with three types of entity: - shapes to be visualized (these shapes must have already been triangulated.) - edges in these shapes (these edges are defined as polygonal lines on the triangulation of the shape, and are the basic entities which will be visualized or hidden), and - triangles in these shapes which hide the edges. HLRBRep_PolyAlgo is based on the principle of comparing each edge of the shape to be visualized with each of the triangles produced by the triangulation of the shape, and calculating the visible and the hidden parts of each edge. For a given projection, HLRBRep_PolyAlgo calculates a set of lines characteristic of the object being represented. It is also used in conjunction with the HLRBRep_PolyHLRToShape extraction utilities, which reconstruct a new, simplified shape from a selection of calculation results. This new shape is made up of edges, which represent the shape visualized in the projection. HLRBRep_PolyAlgo works with a polyhedral simplification of the shape whereas HLRBRep_Algo takes the shape itself into account. When you use HLRBRep_Algo, you obtain an exact result, whereas, when you use HLRBRep_PolyAlgo, you reduce computation time but obtain polygonal segments. An HLRBRep_PolyAlgo object provides a framework for: - defining the point of view - identifying the shape or shapes to be visualized - calculating the outlines - calculating the visible and hidden lines of the shape. Warning - Superimposed lines are not eliminated by this algorithm. - There must be no unfinished objects inside the shape you wish to visualize. - Points are not treated. - Note that this is not the sort of algorithm used in generating shading, which calculates the visible and hidden parts of each face in a shape to be visualized by comparing each face in the shape with every other face in the same shape.to remove Hidden lines on Shapes with Triangulations. A framework to compute the shape as seen in a projection plane. This is done by calculating the visible and the hidden parts of the shape. HLRBRep_PolyAlgo works with three types of entity: - shapes to be visualized (these shapes must have already been triangulated.) - edges in these shapes (these edges are defined as polygonal lines on the triangulation of the shape, and are the basic entities which will be visualized or hidden), and - triangles in these shapes which hide the edges. HLRBRep_PolyAlgo is based on the principle of comparing each edge of the shape to be visualized with each of the triangles produced by the triangulation of the shape, and calculating the visible and the hidden parts of each edge. For a given projection, HLRBRep_PolyAlgo calculates a set of lines characteristic of the object being represented. It is also used in conjunction with the HLRBRep_PolyHLRToShape extraction utilities, which reconstruct a new, simplified shape from a selection of calculation results. This new shape is made up of edges, which represent the shape visualized in the projection. HLRBRep_PolyAlgo works with a polyhedral simplification of the shape whereas HLRBRep_Algo takes the shape itself into account. When you use HLRBRep_Algo, you obtain an exact result, whereas, when you use HLRBRep_PolyAlgo, you reduce computation time but obtain polygonal segments. An HLRBRep_PolyAlgo object provides a framework for: - defining the point of view - identifying the shape or shapes to be visualized - calculating the outlines - calculating the visible and hidden lines of the shape. Warning - Superimposed lines are not eliminated by this algorithm. - There must be no unfinished objects inside the shape you wish to visualize. - Points are not treated. - Note that this is not the sort of algorithm used in generating shading, which calculates the visible and hidden parts of each face in a shape to be visualized by comparing each face in the shape with every other face in the same shape.to remove Hidden lines on Shapes with Triangulations. A framework to compute the shape as seen in a projection plane. This is done by calculating the visible and the hidden parts of the shape. HLRBRep_PolyAlgo works with three types of entity: - shapes to be visualized (these shapes must have already been triangulated.) - edges in these shapes (these edges are defined as polygonal lines on the triangulation of the shape, and are the basic entities which will be visualized or hidden), and - triangles in these shapes which hide the edges. HLRBRep_PolyAlgo is based on the principle of comparing each edge of the shape to be visualized with each of the triangles produced by the triangulation of the shape, and calculating the visible and the hidden parts of each edge. For a given projection, HLRBRep_PolyAlgo calculates a set of lines characteristic of the object being represented. It is also used in conjunction with the HLRBRep_PolyHLRToShape extraction utilities, which reconstruct a new, simplified shape from a selection of calculation results. This new shape is made up of edges, which represent the shape visualized in the projection. HLRBRep_PolyAlgo works with a polyhedral simplification of the shape whereas HLRBRep_Algo takes the shape itself into account. When you use HLRBRep_Algo, you obtain an exact result, whereas, when you use HLRBRep_PolyAlgo, you reduce computation time but obtain polygonal segments. An HLRBRep_PolyAlgo object provides a framework for: - defining the point of view - identifying the shape or shapes to be visualized - calculating the outlines - calculating the visible and hidden lines of the shape. Warning - Superimposed lines are not eliminated by this algorithm. - There must be no unfinished objects inside the shape you wish to visualize. - Points are not treated. - Note that this is not the sort of algorithm used in generating shading, which calculates the visible and hidden parts of each face in a shape to be visualized by comparing each face in the shape with every other face in the same shape.
    """
    def Algo(self) -> OCP.HLRAlgo.HLRAlgo_PolyAlgo: 
        """
        None
        """
    @overload
    def Debug(self) -> bool: 
        """
        None

        None
        """
    @overload
    def Debug(self,theDebug : bool) -> None: ...
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hide(self,status : OCP.HLRAlgo.HLRAlgo_EdgeStatus,S : OCP.TopoDS.TopoDS_Shape,reg1 : bool,regn : bool,outl : bool,intl : bool) -> Any: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        return the index of the Shape <S> and return 0 if the Shape <S> is not found.
        """
    def InitHide(self) -> None: 
        """
        None
        """
    def InitShow(self) -> None: 
        """
        None
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
    def Load(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Loads the shape S into this framework. Warning S must have already been triangulated.
        """
    def MoreHide(self) -> bool: 
        """
        None
        """
    def MoreShow(self) -> bool: 
        """
        None
        """
    def NbShapes(self) -> int: 
        """
        None
        """
    def NextHide(self) -> None: 
        """
        None
        """
    def NextShow(self) -> None: 
        """
        None
        """
    def OutLinedShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Make a shape with the internal outlines in each face.
        """
    @overload
    def Projector(self,theProj : OCP.HLRAlgo.HLRAlgo_Projector) -> None: 
        """
        None

        Sets the parameters of the view for this framework. These parameters are defined by an HLRAlgo_Projector object, which is returned by the Projector function on a Prs3d_Projector object.
        """
    @overload
    def Projector(self) -> OCP.HLRAlgo.HLRAlgo_Projector: ...
    def Remove(self,I : int) -> None: 
        """
        remove the Shape of Index <I>.
        """
    def Shape(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Show(self,S : OCP.TopoDS.TopoDS_Shape,reg1 : bool,regn : bool,outl : bool,intl : bool) -> Any: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def TolAngular(self) -> float: 
        """
        None

        None
        """
    @overload
    def TolAngular(self,theTol : float) -> None: ...
    @overload
    def TolCoef(self,theTol : float) -> None: 
        """
        None

        None
        """
    @overload
    def TolCoef(self) -> float: ...
    def Update(self) -> None: 
        """
        Launches calculation of outlines of the shape visualized by this framework. Used after setting the point of view and defining the shape or shapes to be visualized.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,A : HLRBRep_PolyAlgo) -> None: ...
    @overload
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
class HLRBRep_PolyHLRToShape():
    """
    A framework for filtering the computation results of an HLRBRep_Algo algorithm by extraction. From the results calculated by the algorithm on a shape, a filter returns the type of edge you want to identify. You can choose any of the following types of output: - visible sharp edges - hidden sharp edges - visible smooth edges - hidden smooth edges - visible sewn edges - hidden sewn edges - visible outline edges - hidden outline edges. - visible isoparameters and - hidden isoparameters. Sharp edges present a C0 continuity (non G1). Smooth edges present a G1 continuity (non G2). Sewn edges present a C2 continuity. The result is composed of 2D edges in the projection plane of the view which the algorithm has worked with. These 2D edges are not included in the data structure of the visualized shape. In order to obtain a complete image, you must combine the shapes given by each of the chosen filters. The construction of the shape does not call a new computation of the algorithm, but only reads its internal results.
    """
    @overload
    def HCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def HCompound(self) -> OCP.TopoDS.TopoDS_Shape: ...
    def Hide(self) -> None: 
        """
        None

        None
        """
    @overload
    def OutLineHCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        Sets the extraction filter for hidden outlines. Hidden outlines occur, for instance, in tori. In this case, the inner outlines of the torus seen on its side are hidden.

        None

        Sets the extraction filter for hidden outlines. Hidden outlines occur, for instance, in tori. In this case, the inner outlines of the torus seen on its side are hidden.
        """
    @overload
    def OutLineHCompound(self) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def OutLineVCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        Sets the extraction filter for visible outlines.

        None

        Sets the extraction filter for visible outlines.
        """
    @overload
    def OutLineVCompound(self) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def Rg1LineHCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        Sets the extraction filter for hidden smooth edges.

        None

        Sets the extraction filter for hidden smooth edges.
        """
    @overload
    def Rg1LineHCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def Rg1LineVCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Sets the extraction filter for visible smooth edges.

        None

        Sets the extraction filter for visible smooth edges.

        None
        """
    @overload
    def Rg1LineVCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def RgNLineHCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        Sets the extraction filter for hidden sewn edges.

        None

        Sets the extraction filter for hidden sewn edges.
        """
    @overload
    def RgNLineHCompound(self) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def RgNLineVCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Sets the extraction filter for visible sewn edges.

        None

        Sets the extraction filter for visible sewn edges.

        None
        """
    @overload
    def RgNLineVCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    def Show(self) -> None: 
        """
        None

        None
        """
    def Update(self,A : HLRBRep_PolyAlgo) -> None: 
        """
        None
        """
    @overload
    def VCompound(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def VCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    def __init__(self) -> None: ...
    pass
class HLRBRep_SLProps():
    """
    None
    """
    def CurvatureDirections(self,MaxD : OCP.gp.gp_Dir,MinD : OCP.gp.gp_Dir) -> None: 
        """
        Returns the direction of the maximum and minimum curvature <MaxD> and <MinD>
        """
    def D1U(self) -> OCP.gp.gp_Vec: 
        """
        Returns the first U derivative. The derivative is computed if it has not been yet.
        """
    def D1V(self) -> OCP.gp.gp_Vec: 
        """
        Returns the first V derivative. The derivative is computed if it has not been yet.
        """
    def D2U(self) -> OCP.gp.gp_Vec: 
        """
        Returns the second U derivatives The derivative is computed if it has not been yet.
        """
    def D2V(self) -> OCP.gp.gp_Vec: 
        """
        Returns the second V derivative. The derivative is computed if it has not been yet.
        """
    def DUV(self) -> OCP.gp.gp_Vec: 
        """
        Returns the second UV cross-derivative. The derivative is computed if it has not been yet.
        """
    def GaussianCurvature(self) -> float: 
        """
        Returns the Gaussian curvature
        """
    def IsCurvatureDefined(self) -> bool: 
        """
        returns True if the curvature is defined.
        """
    def IsNormalDefined(self) -> bool: 
        """
        Tells if the normal is defined.
        """
    def IsTangentUDefined(self) -> bool: 
        """
        returns True if the U tangent is defined. For example, the tangent is not defined if the two first U derivatives are null.
        """
    def IsTangentVDefined(self) -> bool: 
        """
        returns if the V tangent is defined. For example, the tangent is not defined if the two first V derivatives are null.
        """
    def IsUmbilic(self) -> bool: 
        """
        returns True if the point is umbilic (i.e. if the curvature is constant).
        """
    def MaxCurvature(self) -> float: 
        """
        Returns the maximum curvature
        """
    def MeanCurvature(self) -> float: 
        """
        Returns the mean curvature.
        """
    def MinCurvature(self) -> float: 
        """
        Returns the minimum curvature
        """
    def Normal(self) -> OCP.gp.gp_Dir: 
        """
        Returns the normal direction.
        """
    def SetParameters(self,U : float,V : float) -> None: 
        """
        Initializes the local properties of the surface S for the new parameter values (<U>, <V>).
        """
    def TangentU(self,D : OCP.gp.gp_Dir) -> None: 
        """
        Returns the tangent direction <D> on the iso-V.
        """
    def TangentV(self,D : OCP.gp.gp_Dir) -> None: 
        """
        Returns the tangent direction <D> on the iso-V.
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point.
        """
    def __init__(self,N : int,Resolution : float) -> None: ...
    pass
class HLRBRep_SLPropsATool():
    """
    None
    """
    @staticmethod
    def Bounds_s(A : capsule) -> Tuple[float, float, float, float]: 
        """
        returns the bounds of the Surface.
        """
    @staticmethod
    def Continuity_s(A : capsule) -> int: 
        """
        returns the order of continuity of the Surface <A>. returns 1 : first derivative only is computable returns 2 : first and second derivative only are computable.
        """
    @staticmethod
    def D1_s(A : capsule,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P> and first derivative <D1*> of parameter <U> and <V> on the Surface <A>.
        """
    @staticmethod
    def D2_s(A : capsule,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,DUV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P>, the first derivative <D1*> and second derivative <D2*> of parameter <U> and <V> on the Surface <A>.
        """
    @staticmethod
    def DN_s(A : capsule,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def Value_s(A : capsule,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point <P> of parameter <U> and <V> on the Surface <A>.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_SeqOfShapeBounds(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : HLRBRep_ShapeBounds) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : HLRBRep_SeqOfShapeBounds) -> None: ...
    def Assign(self,theOther : HLRBRep_SeqOfShapeBounds) -> HLRBRep_SeqOfShapeBounds: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> HLRBRep_ShapeBounds: 
        """
        First item access
        """
    def ChangeLast(self) -> HLRBRep_ShapeBounds: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> HLRBRep_ShapeBounds: 
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
    def First(self) -> HLRBRep_ShapeBounds: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : HLRBRep_ShapeBounds) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : HLRBRep_SeqOfShapeBounds) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : HLRBRep_SeqOfShapeBounds) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : HLRBRep_ShapeBounds) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> HLRBRep_ShapeBounds: 
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
    def Prepend(self,theItem : HLRBRep_ShapeBounds) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : HLRBRep_SeqOfShapeBounds) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : HLRBRep_ShapeBounds) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : HLRBRep_SeqOfShapeBounds) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> HLRBRep_ShapeBounds: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : HLRBRep_SeqOfShapeBounds) -> None: ...
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
class HLRBRep_ShapeBounds():
    """
    Contains a Shape and the bounds of its vertices, edges and faces in the DataStructure.
    """
    def Bounds(self) -> Tuple[int, int, int, int, int, int]: 
        """
        None
        """
    def MinMax(self) -> Any: 
        """
        None
        """
    @overload
    def NbOfIso(self) -> int: 
        """
        None

        None

        None

        None
        """
    @overload
    def NbOfIso(self,nbIso : int) -> None: ...
    @overload
    def Shape(self,S : OCP.HLRTopoBRep.HLRTopoBRep_OutLiner) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Shape(self) -> OCP.HLRTopoBRep.HLRTopoBRep_OutLiner: ...
    @overload
    def ShapeData(self,SD : OCP.Standard.Standard_Transient) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def ShapeData(self) -> OCP.Standard.Standard_Transient: ...
    def Sizes(self) -> Tuple[int, int, int]: 
        """
        None
        """
    def Translate(self,NV : int,NE : int,NF : int) -> None: 
        """
        None
        """
    def UpdateMinMax(self,theTotMinMax : Any) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.HLRTopoBRep.HLRTopoBRep_OutLiner,nbIso : int,V1 : int,V2 : int,E1 : int,E2 : int,F1 : int,F2 : int) -> None: ...
    @overload
    def __init__(self,S : OCP.HLRTopoBRep.HLRTopoBRep_OutLiner,SData : OCP.Standard.Standard_Transient,nbIso : int,V1 : int,V2 : int,E1 : int,E2 : int,F1 : int,F2 : int) -> None: ...
    pass
class HLRBRep_ShapeToHLR():
    """
    compute the OutLinedShape of a Shape with an OutLiner, a Projector and create the Data Structure of a Shape.
    """
    @staticmethod
    def Load_s(S : OCP.HLRTopoBRep.HLRTopoBRep_OutLiner,P : OCP.HLRAlgo.HLRAlgo_Projector,MST : OCP.BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool,nbIso : int=0) -> HLRBRep_Data: 
        """
        Creates a DataStructure containing the OutLiner <S> depending on the projector <P> and nbIso.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_Surface():
    """
    None
    """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        None

        None
        """
    def Cone(self) -> OCP.gp.gp_Cone: 
        """
        None

        None
        """
    def Cylinder(self) -> OCP.gp.gp_Cylinder: 
        """
        None

        None
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameters U,V on the surface.

        Computes the point of parameters U,V on the surface.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point and the first derivatives on the surface. Raised if the continuity of the current intervals is not C1.

        Computes the point and the first derivatives on the surface. Raised if the continuity of the current intervals is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first and second derivatives on the surface. Raised if the continuity of the current intervals is not C2.

        Computes the point, the first and second derivatives on the surface. Raised if the continuity of the current intervals is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first, second and third derivatives on the surface. Raised if the continuity of the current intervals is not C3.

        Computes the point, the first, second and third derivatives on the surface. Raised if the continuity of the current intervals is not C3.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V). Raised if the current U interval is not not CNu and the current V interval is not CNv. Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.

        Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V). Raised if the current U interval is not not CNu and the current V interval is not CNv. Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """
    def FirstUParameter(self) -> float: 
        """
        None

        None
        """
    def FirstVParameter(self) -> float: 
        """
        None

        None
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_SurfaceType: 
        """
        Returns the type of the surface : Plane, Cylinder, Cone, Sphere, Torus, BezierSurface, BSplineSurface, SurfaceOfRevolution, SurfaceOfExtrusion, OtherSurface

        Returns the type of the surface : Plane, Cylinder, Cone, Sphere, Torus, BezierSurface, BSplineSurface, SurfaceOfRevolution, SurfaceOfExtrusion, OtherSurface
        """
    def IsAbove(self,back : bool,A : HLRBRep_Curve,tolC : float) -> bool: 
        """
        None
        """
    def IsSide(self,tolf : float,toler : float) -> bool: 
        """
        returns true if it is a side face
        """
    def IsUClosed(self) -> bool: 
        """
        None

        None
        """
    def IsUPeriodic(self) -> bool: 
        """
        None

        None
        """
    def IsVClosed(self) -> bool: 
        """
        None

        None
        """
    def IsVPeriodic(self) -> bool: 
        """
        None

        None
        """
    def LastUParameter(self) -> float: 
        """
        None

        None
        """
    def LastVParameter(self) -> float: 
        """
        None

        None
        """
    def NbUIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        If necessary, breaks the surface in U intervals of continuity <S>. And returns the number of intervals.

        If necessary, breaks the surface in U intervals of continuity <S>. And returns the number of intervals.
        """
    def NbUKnots(self) -> int: 
        """
        None

        None
        """
    def NbUPoles(self) -> int: 
        """
        None

        None
        """
    def NbVIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        If necessary, breaks the surface in V intervals of continuity <S>. And returns the number of intervals.

        If necessary, breaks the surface in V intervals of continuity <S>. And returns the number of intervals.
        """
    def NbVKnots(self) -> int: 
        """
        None

        None
        """
    def NbVPoles(self) -> int: 
        """
        None

        None
        """
    def Plane(self) -> OCP.gp.gp_Pln: 
        """
        None
        """
    def Projector(self,Proj : OCP.HLRAlgo.HLRAlgo_Projector) -> None: 
        """
        None
        """
    def Sphere(self) -> OCP.gp.gp_Sphere: 
        """
        None

        None
        """
    @overload
    def Surface(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the 3D Surface to be projected.

        Returns the 3D Surface.

        Returns the 3D Surface.
        """
    @overload
    def Surface(self) -> OCP.BRepAdaptor.BRepAdaptor_Surface: ...
    def Torus(self) -> OCP.gp.gp_Torus: 
        """
        None

        None
        """
    def UContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    def UDegree(self) -> int: 
        """
        None

        None
        """
    def UPeriod(self) -> float: 
        """
        None

        None
        """
    def VContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    def VDegree(self) -> int: 
        """
        None

        None
        """
    def VPeriod(self) -> float: 
        """
        None

        None
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameters U,V on the surface.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_SurfaceTool():
    """
    None
    """
    @staticmethod
    def AxeOfRevolution_s(S : capsule) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    @staticmethod
    def BSpline_s(S : capsule) -> OCP.Geom.Geom_BSplineSurface: 
        """
        None
        """
    @staticmethod
    def BasisCurve_s(S : capsule) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    @staticmethod
    def BasisSurface_s(S : capsule) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        None
        """
    @staticmethod
    def Bezier_s(S : capsule) -> OCP.Geom.Geom_BezierSurface: 
        """
        None
        """
    @staticmethod
    def Cone_s(S : capsule) -> OCP.gp.gp_Cone: 
        """
        None
        """
    @staticmethod
    def Cylinder_s(S : capsule) -> OCP.gp.gp_Cylinder: 
        """
        None
        """
    @staticmethod
    def D0_s(S : capsule,u : float,v : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def D1_s(S : capsule,u : float,v : float,P : OCP.gp.gp_Pnt,D1u : OCP.gp.gp_Vec,D1v : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D2_s(S : capsule,u : float,v : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D3_s(S : capsule,u : float,v : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def DN_s(S : capsule,u : float,v : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def Direction_s(S : capsule) -> OCP.gp.gp_Dir: 
        """
        None
        """
    @staticmethod
    def FirstUParameter_s(S : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def FirstVParameter_s(S : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(S : capsule) -> OCP.GeomAbs.GeomAbs_SurfaceType: 
        """
        None
        """
    @staticmethod
    def IsUClosed_s(S : capsule) -> bool: 
        """
        None
        """
    @staticmethod
    def IsUPeriodic_s(S : capsule) -> bool: 
        """
        None
        """
    @staticmethod
    def IsVClosed_s(S : capsule) -> bool: 
        """
        None
        """
    @staticmethod
    def IsVPeriodic_s(S : capsule) -> bool: 
        """
        None
        """
    @staticmethod
    def LastUParameter_s(S : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def LastVParameter_s(S : capsule) -> float: 
        """
        None
        """
    @staticmethod
    @overload
    def NbSamplesU_s(S : capsule,u1 : float,u2 : float) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbSamplesU_s(S : capsule) -> int: ...
    @staticmethod
    @overload
    def NbSamplesV_s(S : capsule) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbSamplesV_s(S : capsule,v1 : float,v2 : float) -> int: ...
    @staticmethod
    def NbUIntervals_s(S : capsule,Sh : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        None
        """
    @staticmethod
    def NbVIntervals_s(S : capsule,Sh : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        None
        """
    @staticmethod
    def OffsetValue_s(S : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def Plane_s(S : capsule) -> OCP.gp.gp_Pln: 
        """
        None
        """
    @staticmethod
    def Sphere_s(S : capsule) -> OCP.gp.gp_Sphere: 
        """
        None
        """
    @staticmethod
    def Torus_s(S : capsule) -> OCP.gp.gp_Torus: 
        """
        None
        """
    @staticmethod
    def UIntervals_s(S : capsule,T : OCP.TColStd.TColStd_Array1OfReal,Sh : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def UPeriod_s(S : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def UResolution_s(S : capsule,R3d : float) -> float: 
        """
        None
        """
    @staticmethod
    def UTrim_s(S : capsule,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        If <First> >= <Last>
        """
    @staticmethod
    def VIntervals_s(S : capsule,T : OCP.TColStd.TColStd_Array1OfReal,Sh : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def VPeriod_s(S : capsule) -> float: 
        """
        None
        """
    @staticmethod
    def VResolution_s(S : capsule,R3d : float) -> float: 
        """
        None
        """
    @staticmethod
    def VTrim_s(S : capsule,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        If <First> >= <Last>
        """
    @staticmethod
    def Value_s(S : capsule,u : float,v : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_TheCSFunctionOfInterCSurf(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def AuxillarCurve(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def AuxillarSurface(self) -> capsule: 
        """
        None
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Root(self) -> float: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    pass
class HLRBRep_TheCurveLocatorOfTheProjPCurOfCInter():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class HLRBRep_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfCInter(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        returns 2.
        """
    def NbVariables(self) -> int: 
        """
        returns 2.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    pass
class HLRBRep_TheExactInterCSurf():
    """
    None
    """
    def Function(self) -> HLRBRep_TheCSFunctionOfInterCSurf: 
        """
        return the math function which is used to compute the intersection
        """
    def IsDone(self) -> bool: 
        """
        Returns TRUE if the creation completed without failure.
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def ParameterOnCurve(self) -> float: 
        """
        None
        """
    def ParameterOnSurface(self) -> Tuple[float, float]: 
        """
        None
        """
    def Perform(self,U : float,V : float,W : float,Rsnld : OCP.math.math_FunctionSetRoot,u0 : float,v0 : float,u1 : float,v1 : float,w0 : float,w1 : float) -> None: 
        """
        compute the solution it's possible to write to optimize: IntImp_IntCS inter(S1,C1,Toltangency) math_FunctionSetRoot rsnld(Inter.function()) while ...{ u=... v=... w=... inter.Perform(u,v,w,rsnld) } or IntImp_IntCS inter(Toltangency) inter.SetSurface(S); math_FunctionSetRoot rsnld(Inter.function()) while ...{ C=... inter.SetCurve(C); u=... v=... w=... inter.Perform(u,v,w,rsnld) }
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        returns the intersection point The exception NotDone is raised if IsDone is false. The exception DomainError is raised if IsEmpty is true.
        """
    @overload
    def __init__(self,F : HLRBRep_TheCSFunctionOfInterCSurf,TolTangency : float) -> None: ...
    @overload
    def __init__(self,U : float,V : float,W : float,F : HLRBRep_TheCSFunctionOfInterCSurf,TolTangency : float,MarginCoef : float=0.0) -> None: ...
    pass
class HLRBRep_TheIntConicCurveOfCInter(OCP.IntRes2d.IntRes2d_Intersection):
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        returns TRUE when the computation was successful.

        returns TRUE when the computation was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.

        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbPoints(self) -> int: 
        """
        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbSegments(self) -> int: 
        """
        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def Point(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionPoint: 
        """
        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def Segment(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionSegment: 
        """
        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    @overload
    def SetReversedParameters(self,Reverseflag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetReversedParameters(self,flag : bool) -> None: ...
    def __init__(self) -> None: ...
    pass
class HLRBRep_TheIntPCurvePCurveOfCInter(OCP.IntRes2d.IntRes2d_Intersection):
    """
    None
    """
    def GetMinNbSamples(self) -> int: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        returns TRUE when the computation was successful.

        returns TRUE when the computation was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.

        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbPoints(self) -> int: 
        """
        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbSegments(self) -> int: 
        """
        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def Point(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionPoint: 
        """
        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def Segment(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionSegment: 
        """
        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def SetMinNbSamples(self,theMinNbSamples : int) -> None: 
        """
        Set / get minimum number of points in polygon for intersection.
        """
    @overload
    def SetReversedParameters(self,Reverseflag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetReversedParameters(self,flag : bool) -> None: ...
    def __init__(self) -> None: ...
    pass
class HLRBRep_TheInterferenceOfInterCSurf(OCP.Intf.Intf_Interference):
    """
    None
    """
    def Contains(self,ThePnt : OCP.Intf.Intf_SectionPoint) -> bool: 
        """
        Tests if the polylines of intersection or the zones of tangence contain the point of intersection <ThePnt>.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def GetTolerance(self) -> float: 
        """
        Gives the tolerance used for the calculation.

        Gives the tolerance used for the calculation.
        """
    @overload
    def Insert(self,pdeb : OCP.Intf.Intf_SectionPoint,pfin : OCP.Intf.Intf_SectionPoint) -> None: 
        """
        Inserts a new zone of tangence in the current list of tangent zones of the interference and returns True when done.

        Insert a new segment of intersection in the current list of polylines of intersection of the interference.
        """
    @overload
    def Insert(self,TheZone : OCP.Intf.Intf_TangentZone) -> bool: ...
    @overload
    def Interference(self,thePolyg : HLRBRep_ThePolygonOfInterCSurf,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: 
        """
        Compares the boundings between the segment of <thePolyg> and the facets of <thePolyh>.

        Compares the boundings between the segment of <thePolyg> and the facets of <thePolyh>.
        """
    @overload
    def Interference(self,thePolyg : HLRBRep_ThePolygonOfInterCSurf,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...
    def LineValue(self,Index : int) -> OCP.Intf.Intf_SectionLine: 
        """
        Gives the polyline of intersection at address <Index> in the interference.

        Gives the polyline of intersection at address <Index> in the interference.
        """
    def NbSectionLines(self) -> int: 
        """
        Gives the number of polylines of intersection in the interference.

        Gives the number of polylines of intersection in the interference.
        """
    def NbSectionPoints(self) -> int: 
        """
        Gives the number of points of intersection in the interference.

        Gives the number of points of intersection in the interference.
        """
    def NbTangentZones(self) -> int: 
        """
        Gives the number of zones of tangence in the interference.

        Gives the number of zones of tangence in the interference.
        """
    @overload
    def Perform(self,theLins : OCP.Intf.Intf_Array1OfLin,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: 
        """
        Computes an interference between the Polygon and the Polyhedron.

        Computes an interference between the Straight Line and the Polyhedron.

        Computes an interference between the Straight Lines and the Polyhedron.

        Computes an interference between the Polygon and the Polyhedron.

        Computes an interference between the Straight Line and the Polyhedron.

        Computes an interference between the Straight Lines and the Polyhedron.
        """
    @overload
    def Perform(self,thePolyg : HLRBRep_ThePolygonOfInterCSurf,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def Perform(self,theLin : OCP.gp.gp_Lin,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...
    @overload
    def Perform(self,theLins : OCP.Intf.Intf_Array1OfLin,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...
    @overload
    def Perform(self,thePolyg : HLRBRep_ThePolygonOfInterCSurf,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...
    @overload
    def Perform(self,theLin : OCP.gp.gp_Lin,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    def PntValue(self,Index : int) -> OCP.Intf.Intf_SectionPoint: 
        """
        Gives the point of intersection of address Index in the interference.

        Gives the point of intersection of address Index in the interference.
        """
    def ZoneValue(self,Index : int) -> OCP.Intf.Intf_TangentZone: 
        """
        Gives the zone of tangence at address Index in the interference.

        Gives the zone of tangence at address Index in the interference.
        """
    @overload
    def __init__(self,theLin : OCP.gp.gp_Lin,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...
    @overload
    def __init__(self,theLin : OCP.gp.gp_Lin,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,thePolyg : HLRBRep_ThePolygonOfInterCSurf,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...
    @overload
    def __init__(self,theLins : OCP.Intf.Intf_Array1OfLin,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def __init__(self,thePolyg : HLRBRep_ThePolygonOfInterCSurf,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def __init__(self,theLins : OCP.Intf.Intf_Array1OfLin,thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> None: ...
    pass
class HLRBRep_TheIntersectorOfTheIntConicCurveOfCInter(OCP.IntRes2d.IntRes2d_Intersection):
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        returns TRUE when the computation was successful.

        returns TRUE when the computation was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.

        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbPoints(self) -> int: 
        """
        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbSegments(self) -> int: 
        """
        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def Point(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionPoint: 
        """
        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def Segment(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionSegment: 
        """
        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    @overload
    def SetReversedParameters(self,Reverseflag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetReversedParameters(self,flag : bool) -> None: ...
    def __init__(self) -> None: ...
    pass
class HLRBRep_TheLocateExtPCOfTheProjPCurOfCInter():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def IsMin(self) -> bool: 
        """
        Returns True if the extremum distance is a minimum.
        """
    def Perform(self,P : OCP.gp.gp_Pnt2d,U0 : float) -> None: 
        """
        the algorithm is done with the point P. An exception is raised if the fields have not been initialized.
        """
    def Point(self) -> OCP.Extrema.Extrema_POnCurv2d: 
        """
        Returns the point of the extremum distance.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_ThePolygon2dOfTheIntPCurvePCurveOfCInter(OCP.Intf.Intf_Polygon2d):
    """
    None
    """
    def ApproxParamOnCurve(self,Index : int,ParamOnLine : float) -> float: 
        """
        Give an approximation of the parameter on the curve according to the discretization of the Curve.
        """
    def AutoIntersectionIsPossible(self) -> bool: 
        """
        None
        """
    def Bounding(self) -> OCP.Bnd.Bnd_Box2d: 
        """
        Returns the bounding box of the polygon.

        Returns the bounding box of the polygon.
        """
    def CalculRegion(self,x : float,y : float,x1 : float,x2 : float,y1 : float,y2 : float) -> int: 
        """
        None
        """
    @overload
    def Closed(self) -> bool: 
        """
        None

        Returns True if the polyline is closed.
        """
    @overload
    def Closed(self,clos : bool) -> None: ...
    def DeflectionOverEstimation(self) -> float: 
        """
        None
        """
    def Dump(self) -> None: 
        """
        None
        """
    def InfParameter(self) -> float: 
        """
        Returns the parameter (On the curve) of the first point of the Polygon
        """
    def NbSegments(self) -> int: 
        """
        Give the number of Segments in the polyline.
        """
    def Segment(self,theIndex : int,theBegin : OCP.gp.gp_Pnt2d,theEnd : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns the points of the segment <Index> in the Polygon.
        """
    def SetDeflectionOverEstimation(self,x : float) -> None: 
        """
        None
        """
    def SupParameter(self) -> float: 
        """
        Returns the parameter (On the curve) of the last point of the Polygon
        """
    pass
class HLRBRep_ThePolygonOfInterCSurf():
    """
    None
    """
    def ApproxParamOnCurve(self,Index : int,ParamOnLine : float) -> float: 
        """
        Give an approximation of the parameter on the curve according to the discretization of the Curve.
        """
    def BeginOfSeg(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of range Index in the Polygon.
        """
    def Bounding(self) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the polygon.
        """
    @overload
    def Closed(self,clos : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Closed(self) -> bool: ...
    def DeflectionOverEstimation(self) -> float: 
        """
        None
        """
    def Dump(self) -> None: 
        """
        None
        """
    def EndOfSeg(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of range Index in the Polygon.
        """
    def InfParameter(self) -> float: 
        """
        Returns the parameter (On the curve) of the first point of the Polygon
        """
    def NbSegments(self) -> int: 
        """
        Give the number of Segments in the polyline.
        """
    def SetDeflectionOverEstimation(self,x : float) -> None: 
        """
        None
        """
    def SupParameter(self) -> float: 
        """
        Returns the parameter (On the curve) of the last point of the Polygon
        """
    @overload
    def __init__(self,Curve : OCP.gp.gp_Lin,NbPnt : int) -> None: ...
    @overload
    def __init__(self,Curve : OCP.gp.gp_Lin,Upars : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,Curve : OCP.gp.gp_Lin,U1 : float,U2 : float,NbPnt : int) -> None: ...
    pass
class HLRBRep_ThePolygonToolOfInterCSurf():
    """
    None
    """
    @staticmethod
    def BeginOfSeg_s(thePolygon : HLRBRep_ThePolygonOfInterCSurf,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of range Index in the Polygon.
        """
    @staticmethod
    def Bounding_s(thePolygon : HLRBRep_ThePolygonOfInterCSurf) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the polygon.
        """
    @staticmethod
    def Closed_s(thePolygon : HLRBRep_ThePolygonOfInterCSurf) -> bool: 
        """
        None
        """
    @staticmethod
    def DeflectionOverEstimation_s(thePolygon : HLRBRep_ThePolygonOfInterCSurf) -> float: 
        """
        None
        """
    @staticmethod
    def Dump_s(thePolygon : HLRBRep_ThePolygonOfInterCSurf) -> None: 
        """
        None
        """
    @staticmethod
    def EndOfSeg_s(thePolygon : HLRBRep_ThePolygonOfInterCSurf,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of range Index in the Polygon.
        """
    @staticmethod
    def NbSegments_s(thePolygon : HLRBRep_ThePolygonOfInterCSurf) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_ThePolyhedronOfInterCSurf():
    """
    None
    """
    def Bounding(self) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the MaTriangle.
        """
    def ComponentsBounding(self) -> OCP.Bnd.Bnd_HArray1OfBox: 
        """
        Give the array of boxes. The box <n> corresponding to the triangle <n>.
        """
    def Contain(self,Triang : int,ThePnt : OCP.gp.gp_Pnt) -> bool: 
        """
        Give the plane equation of the triangle of addresse Triang.
        """
    @overload
    def DeflectionOverEstimation(self) -> float: 
        """
        None

        None
        """
    @overload
    def DeflectionOverEstimation(self,flec : float) -> None: ...
    def Destroy(self) -> None: 
        """
        None
        """
    def Dump(self) -> None: 
        """
        None
        """
    def FillBounding(self) -> None: 
        """
        Compute the array of boxes. The box <n> corresponding to the triangle <n>.
        """
    def GetBorderDeflection(self) -> float: 
        """
        This method returns a border deflection.
        """
    def IsOnBound(self,Index1 : int,Index2 : int) -> bool: 
        """
        This method returns true if the edge based on points with indices Index1 and Index2 represents a boundary edge. It is necessary to take into account the boundary deflection for this edge.
        """
    def NbPoints(self) -> int: 
        """
        Give the number of point in the double array of triangles ((nbdu+1)*(nbdv+1)).
        """
    def NbTriangles(self) -> int: 
        """
        Give the number of triangles in this double array of
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        None
        """
    def PlaneEquation(self,Triang : int,NormalVector : OCP.gp.gp_XYZ) -> Tuple[float]: 
        """
        Give the plane equation of the triangle of addresse Triang.
        """
    @overload
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Set the value of a field of the double array of points.

        Give the point of index i in the MaTriangle.

        Give the point of index i in the MaTriangle.

        Give the point of index i in the MaTriangle.
        """
    @overload
    def Point(self,Index : int,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Point(self,Index : int,U : float,V : float) -> OCP.gp.gp_Pnt: ...
    @overload
    def Point(self,thePnt : OCP.gp.gp_Pnt,lig : int,col : int,U : float,V : float) -> None: ...
    def Size(self) -> Tuple[int, int]: 
        """
        get the size of the discretization.
        """
    def TriConnex(self,Triang : int,Pivot : int,Pedge : int,TriCon : int,OtherP : int) -> int: 
        """
        Give the addresse Tricon of the triangle connexe to the triangle of address Triang by the edge Pivot Pedge and the third point of this connexe triangle. When we are on a free edge TriCon==0 but the function return the value of the triangle in the other side of Pivot on the free edge. Used to turn around a vertex.
        """
    def Triangle(self,Index : int) -> Tuple[int, int, int]: 
        """
        Give the 3 points of the triangle of addresse Index in the double array of triangles.
        """
    pass
class HLRBRep_ThePolyhedronToolOfInterCSurf():
    """
    None
    """
    @staticmethod
    def Bounding_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the PolyhedronTool.
        """
    @staticmethod
    def ComponentsBounding_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> OCP.Bnd.Bnd_HArray1OfBox: 
        """
        Give the array of boxes. The box <n> corresponding to the triangle <n>.
        """
    @staticmethod
    def DeflectionOverEstimation_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> float: 
        """
        Give the tolerance of the polygon.
        """
    @staticmethod
    def Dump_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> None: 
        """
        None
        """
    @staticmethod
    def GetBorderDeflection_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> float: 
        """
        This method returns a border deflection of the polyhedron.
        """
    @staticmethod
    def IsOnBound_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,Index1 : int,Index2 : int) -> bool: 
        """
        This method returns true if the edge based on points with indices Index1 and Index2 represents a boundary edge. It is necessary to take into account the boundary deflection for this edge.
        """
    @staticmethod
    def NbTriangles_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf) -> int: 
        """
        Give the number of triangles in this polyedral surface.
        """
    @staticmethod
    def Point_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of index i in the polyedral surface.
        """
    @staticmethod
    def TriConnex_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,Triang : int,Pivot : int,Pedge : int,TriCon : int,OtherP : int) -> int: 
        """
        Give the addresse Tricon of the triangle connexe to the triangle of address Triang by the edge Pivot Pedge and the third point of this connexe triangle. When we are on a free edge TriCon==0 but the function return the value of the triangle in the other side of Pivot on the free edge. Used to turn around a vertex.
        """
    @staticmethod
    def Triangle_s(thePolyh : HLRBRep_ThePolyhedronOfInterCSurf,Index : int) -> Tuple[int, int, int]: 
        """
        Give the indices of the 3 points of the triangle of address Index in the PolyhedronTool.
        """
    def __init__(self) -> None: ...
    pass
class HLRBRep_TheProjPCurOfCInter():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class HLRBRep_TheQuadCurvExactInterCSurf():
    """
    None
    """
    def Intervals(self,Index : int) -> Tuple[float, float]: 
        """
        U1 and U2 are the parameters of a segment on the curve.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbIntervals(self) -> int: 
        """
        None
        """
    def NbRoots(self) -> int: 
        """
        None
        """
    def Root(self,Index : int) -> float: 
        """
        None
        """
    pass
class HLRBRep_TheQuadCurvFuncOfTheQuadCurvExactInterCSurf(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,Param : float,D : float) -> bool: 
        """
        Computes the derivative of the previous function at parameter Param. Derivative always returns True.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,Param : float,F : float) -> bool: 
        """
        Computes the value of the signed distance between the implicit surface and the point at parameter Param on the parametrised curve. Value always returns True.
        """
    def Values(self,Param : float,F : float,D : float) -> bool: 
        """
        Computes the value and the derivative of the function. returns True.
        """
    def __init__(self,Q : OCP.IntSurf.IntSurf_Quadric,C : OCP.gp.gp_Lin) -> None: ...
    pass
class HLRBRep_TypeOfResultingEdge():
    """
    Identifies the type of resulting edge of HLRBRep_Algo

    Members:

      HLRBRep_Undefined

      HLRBRep_IsoLine

      HLRBRep_OutLine

      HLRBRep_Rg1Line

      HLRBRep_RgNLine

      HLRBRep_Sharp
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    HLRBRep_IsoLine: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_IsoLine: 1>
    HLRBRep_OutLine: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_OutLine: 2>
    HLRBRep_Rg1Line: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_Rg1Line: 3>
    HLRBRep_RgNLine: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_RgNLine: 4>
    HLRBRep_Sharp: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_Sharp: 5>
    HLRBRep_Undefined: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_Undefined: 0>
    __entries: dict # value = {'HLRBRep_Undefined': (<HLRBRep_TypeOfResultingEdge.HLRBRep_Undefined: 0>, None), 'HLRBRep_IsoLine': (<HLRBRep_TypeOfResultingEdge.HLRBRep_IsoLine: 1>, None), 'HLRBRep_OutLine': (<HLRBRep_TypeOfResultingEdge.HLRBRep_OutLine: 2>, None), 'HLRBRep_Rg1Line': (<HLRBRep_TypeOfResultingEdge.HLRBRep_Rg1Line: 3>, None), 'HLRBRep_RgNLine': (<HLRBRep_TypeOfResultingEdge.HLRBRep_RgNLine: 4>, None), 'HLRBRep_Sharp': (<HLRBRep_TypeOfResultingEdge.HLRBRep_Sharp: 5>, None)}
    __members__: dict # value = {'HLRBRep_Undefined': <HLRBRep_TypeOfResultingEdge.HLRBRep_Undefined: 0>, 'HLRBRep_IsoLine': <HLRBRep_TypeOfResultingEdge.HLRBRep_IsoLine: 1>, 'HLRBRep_OutLine': <HLRBRep_TypeOfResultingEdge.HLRBRep_OutLine: 2>, 'HLRBRep_Rg1Line': <HLRBRep_TypeOfResultingEdge.HLRBRep_Rg1Line: 3>, 'HLRBRep_RgNLine': <HLRBRep_TypeOfResultingEdge.HLRBRep_RgNLine: 4>, 'HLRBRep_Sharp': <HLRBRep_TypeOfResultingEdge.HLRBRep_Sharp: 5>}
    pass
class HLRBRep_VertexList():
    """
    None
    """
    def BoundaryTransition(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the transition of the current vertex relative to the boundary if it is an interference.
        """
    def Current(self) -> OCP.HLRAlgo.HLRAlgo_Intersection: 
        """
        Returns the current vertex
        """
    def IsBoundary(self) -> bool: 
        """
        Returns True if the current vertex is is on the boundary of the edge.
        """
    def IsInterference(self) -> bool: 
        """
        Returns True if the current vertex is an interference.
        """
    def IsPeriodic(self) -> bool: 
        """
        Returns True when the curve is periodic.
        """
    def More(self) -> bool: 
        """
        Returns True when there are more vertices.
        """
    def Next(self) -> None: 
        """
        Proceeds to the next vertex.
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the orientation of the current vertex if it is on the boundary of the edge.
        """
    def Transition(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the transition of the current vertex if it is an interference.
        """
    def __init__(self,T : HLRBRep_EdgeInterferenceTool,I : Any) -> None: ...
    pass
HLRBRep_IsoLine: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_IsoLine: 1>
HLRBRep_OutLine: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_OutLine: 2>
HLRBRep_Rg1Line: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_Rg1Line: 3>
HLRBRep_RgNLine: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_RgNLine: 4>
HLRBRep_Sharp: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_Sharp: 5>
HLRBRep_Undefined: OCP.HLRBRep.HLRBRep_TypeOfResultingEdge # value = <HLRBRep_TypeOfResultingEdge.HLRBRep_Undefined: 0>
