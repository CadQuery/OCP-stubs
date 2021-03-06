import OCP.ChFiDS
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.GeomAbs
import OCP.TColStd
import OCP.Geom2d
import OCP.Law
import OCP.TopTools
import OCP.Adaptor3d
import OCP.Standard
import OCP.TopoDS
import OCP.BRepAdaptor
import OCP.Geom
import OCP.NCollection
import OCP.gp
__all__  = [
"ChFiDS_ChamfMethod",
"ChFiDS_ChamfMode",
"ChFiDS_Spine",
"ChFiDS_CircSection",
"ChFiDS_CommonPoint",
"ChFiDS_ElSpine",
"ChFiDS_ErrorStatus",
"ChFiDS_FaceInterference",
"ChFiDS_FilSpine",
"ChFiDS_SequenceOfSurfData",
"ChFiDS_HElSpine",
"ChFiDS_IndexedDataMapOfVertexListOfStripe",
"ChFiDS_ListOfHElSpine",
"ChFiDS_ListOfStripe",
"ChFiDS_Map",
"ChFiDS_Regul",
"ChFiDS_Regularities",
"ChFiDS_SecArray1",
"ChFiDS_SecHArray1",
"ChFiDS_SequenceOfSpine",
"ChFiDS_HData",
"ChFiDS_ChamfSpine",
"ChFiDS_State",
"ChFiDS_Stripe",
"ChFiDS_StripeArray1",
"ChFiDS_StripeMap",
"ChFiDS_SurfData",
"ChFiDS_AllSame",
"ChFiDS_BreakPoint",
"ChFiDS_ClassicChamfer",
"ChFiDS_Closed",
"ChFiDS_ConstThroatChamfer",
"ChFiDS_ConstThroatWithPenetrationChamfer",
"ChFiDS_DistAngle",
"ChFiDS_Error",
"ChFiDS_FreeBoundary",
"ChFiDS_Ok",
"ChFiDS_OnDiff",
"ChFiDS_OnSame",
"ChFiDS_StartsolFailure",
"ChFiDS_Sym",
"ChFiDS_Tangent",
"ChFiDS_TwistedSurface",
"ChFiDS_TwoDist",
"ChFiDS_WalkingFailure"
]
class ChFiDS_ChamfMethod():
    """
    None

    Members:

      ChFiDS_Sym

      ChFiDS_TwoDist

      ChFiDS_DistAngle
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    ChFiDS_DistAngle: OCP.ChFiDS.ChFiDS_ChamfMethod # value = ChFiDS_ChamfMethod.ChFiDS_DistAngle
    ChFiDS_Sym: OCP.ChFiDS.ChFiDS_ChamfMethod # value = ChFiDS_ChamfMethod.ChFiDS_Sym
    ChFiDS_TwoDist: OCP.ChFiDS.ChFiDS_ChamfMethod # value = ChFiDS_ChamfMethod.ChFiDS_TwoDist
    __entries: dict # value = {'ChFiDS_Sym': (ChFiDS_ChamfMethod.ChFiDS_Sym, None), 'ChFiDS_TwoDist': (ChFiDS_ChamfMethod.ChFiDS_TwoDist, None), 'ChFiDS_DistAngle': (ChFiDS_ChamfMethod.ChFiDS_DistAngle, None)}
    __members__: dict # value = {'ChFiDS_Sym': ChFiDS_ChamfMethod.ChFiDS_Sym, 'ChFiDS_TwoDist': ChFiDS_ChamfMethod.ChFiDS_TwoDist, 'ChFiDS_DistAngle': ChFiDS_ChamfMethod.ChFiDS_DistAngle}
    pass
class ChFiDS_ChamfMode():
    """
    this enumeration defines several modes of chamfer

    Members:

      ChFiDS_ClassicChamfer

      ChFiDS_ConstThroatChamfer

      ChFiDS_ConstThroatWithPenetrationChamfer
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    ChFiDS_ClassicChamfer: OCP.ChFiDS.ChFiDS_ChamfMode # value = ChFiDS_ChamfMode.ChFiDS_ClassicChamfer
    ChFiDS_ConstThroatChamfer: OCP.ChFiDS.ChFiDS_ChamfMode # value = ChFiDS_ChamfMode.ChFiDS_ConstThroatChamfer
    ChFiDS_ConstThroatWithPenetrationChamfer: OCP.ChFiDS.ChFiDS_ChamfMode # value = ChFiDS_ChamfMode.ChFiDS_ConstThroatWithPenetrationChamfer
    __entries: dict # value = {'ChFiDS_ClassicChamfer': (ChFiDS_ChamfMode.ChFiDS_ClassicChamfer, None), 'ChFiDS_ConstThroatChamfer': (ChFiDS_ChamfMode.ChFiDS_ConstThroatChamfer, None), 'ChFiDS_ConstThroatWithPenetrationChamfer': (ChFiDS_ChamfMode.ChFiDS_ConstThroatWithPenetrationChamfer, None)}
    __members__: dict # value = {'ChFiDS_ClassicChamfer': ChFiDS_ChamfMode.ChFiDS_ClassicChamfer, 'ChFiDS_ConstThroatChamfer': ChFiDS_ChamfMode.ChFiDS_ConstThroatChamfer, 'ChFiDS_ConstThroatWithPenetrationChamfer': ChFiDS_ChamfMode.ChFiDS_ConstThroatWithPenetrationChamfer}
    pass
class ChFiDS_Spine(OCP.Standard.Standard_Transient):
    """
    Contains information necessary for construction of a 3D fillet or chamfer:Contains information necessary for construction of a 3D fillet or chamfer:Contains information necessary for construction of a 3D fillet or chamfer:
    """
    @overload
    def Absc(self,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        None

        None

        None
        """
    @overload
    def Absc(self,U : float,I : int) -> float: ...
    @overload
    def Absc(self,U : float) -> float: ...
    def AppendElSpine(self,Els : ChFiDS_HElSpine) -> None: 
        """
        None
        """
    def AppendOffsetElSpine(self,Els : ChFiDS_HElSpine) -> None: 
        """
        None
        """
    def ChangeElSpines(self) -> ChFiDS_ListOfHElSpine: 
        """
        None
        """
    def ChangeOffsetElSpines(self) -> ChFiDS_ListOfHElSpine: 
        """
        None
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None
        """
    def CurrentElementarySpine(self,Index : int) -> OCP.BRepAdaptor.BRepAdaptor_Curve: 
        """
        sets the current curve and returns it
        """
    def CurrentIndexOfElementarySpine(self) -> int: 
        """
        None

        None
        """
    def D0(self,AbsC : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,AbsC : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,AbsC : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
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
    def Edges(self,I : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    @overload
    def ElSpine(self,IE : int) -> ChFiDS_HElSpine: 
        """
        None

        None

        None
        """
    @overload
    def ElSpine(self,E : OCP.TopoDS.TopoDS_Edge) -> ChFiDS_HElSpine: ...
    @overload
    def ElSpine(self,W : float) -> ChFiDS_HElSpine: ...
    def ErrorStatus(self) -> ChFiDS_ErrorStatus: 
        """
        None
        """
    @overload
    def FirstParameter(self,IndexSpine : int) -> float: 
        """
        None

        gives the total length of all arcs before the number IndexSp
        """
    @overload
    def FirstParameter(self) -> float: ...
    def FirstStatus(self) -> ChFiDS_State: 
        """
        returns if the set of edges starts on a free boundary or if the first vertex is a breakpoint or if the set is closed

        returns if the set of edges starts on a free boundary or if the first vertex is a breakpoint or if the set is closed
        """
    def FirstVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        None
        """
    def HasFirstTgt(self) -> bool: 
        """
        None
        """
    def HasLastTgt(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Index(self,W : float,Forward : bool=True) -> int: 
        """
        None

        None
        """
    @overload
    def Index(self,E : OCP.TopoDS.TopoDS_Edge) -> int: ...
    def IsClosed(self) -> bool: 
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
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def IsTangencyExtremity(self,IsFirst : bool) -> bool: 
        """
        returns if the set of edges starts (or end) on Tangency point.

        returns if the set of edges starts (or end) on Tangency point.
        """
    @overload
    def LastParameter(self) -> float: 
        """
        None

        gives the total length till the ark with number IndexSpine (inclus)
        """
    @overload
    def LastParameter(self,IndexSpine : int) -> float: ...
    def LastStatus(self) -> ChFiDS_State: 
        """
        returns the state at the end of the set

        returns the state at the end of the set
        """
    def LastVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def Length(self,IndexSpine : int) -> float: 
        """
        gives the length of ark with number IndexSp
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def Load(self) -> None: 
        """
        prepare the guideline depending on the edges that are elementary arks (take parameters from a single curvilinear abscissa); to be able to call methods on the geometry (first,last,value,d1,d2) it is necessary to start with preparation otherwise an exception will be raised
        """
    def Mode(self) -> ChFiDS_ChamfMode: 
        """
        Return the mode of chamfers used

        Return the mode of chamfers used
        """
    def NbEdges(self) -> int: 
        """
        None

        None
        """
    def OffsetEdges(self,I : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    @overload
    def Parameter(self,AbsC : float,Oriented : bool=True) -> Tuple[float]: 
        """
        None

        None
        """
    @overload
    def Parameter(self,Index : int,AbsC : float,Oriented : bool=True) -> Tuple[float]: ...
    def Period(self) -> float: 
        """
        None
        """
    def PutInFirst(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store the edge at the first position before all others

        store the edge at the first position before all others
        """
    def PutInFirstOffset(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store the offset edge at the first position before all others

        store the offset edge at the first position before all others
        """
    def Reset(self,AllData : bool=False) -> None: 
        """
        None
        """
    def Resolution(self,R3d : float) -> float: 
        """
        None
        """
    def SetCurrent(self,Index : int) -> None: 
        """
        None
        """
    def SetEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store edges composing the guideline

        store edges composing the guideline
        """
    def SetErrorStatus(self,state : ChFiDS_ErrorStatus) -> None: 
        """
        None
        """
    def SetFirstParameter(self,Par : float) -> None: 
        """
        None
        """
    def SetFirstStatus(self,S : ChFiDS_State) -> None: 
        """
        stores if the start of a set of edges starts on a section of free border or forms a closed contour

        stores if the start of a set of edges starts on a section of free border or forms a closed contour
        """
    def SetFirstTgt(self,W : float) -> None: 
        """
        None
        """
    def SetLastParameter(self,Par : float) -> None: 
        """
        None
        """
    def SetLastStatus(self,S : ChFiDS_State) -> None: 
        """
        stores if the end of a set of edges starts on a section of free border or forms a closed contour

        stores if the end of a set of edges starts on a section of free border or forms a closed contour
        """
    def SetLastTgt(self,W : float) -> None: 
        """
        None
        """
    def SetOffsetEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store offset edges composing the offset guideline

        store offset edges composing the offset guideline
        """
    @overload
    def SetReference(self,W : float) -> None: 
        """
        set a parameter reference for the approx.

        set a parameter reference for the approx, at the middle of edge I.
        """
    @overload
    def SetReference(self,I : int) -> None: ...
    def SetStatus(self,S : ChFiDS_State,IsFirst : bool) -> None: 
        """
        None

        None
        """
    def SetTangencyExtremity(self,IsTangency : bool,IsFirst : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SplitDone(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SplitDone(self) -> bool: ...
    def Status(self,IsFirst : bool) -> ChFiDS_State: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnsetReference(self) -> None: 
        """
        None
        """
    def Value(self,AbsC : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Tol : float) -> None: ...
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
class ChFiDS_CircSection():
    """
    A Section of fillet.
    """
    @overload
    def Get(self,C : OCP.gp.gp_Circ) -> Tuple[float, float]: 
        """
        None

        None
        """
    @overload
    def Get(self,C : OCP.gp.gp_Lin) -> Tuple[float, float]: ...
    @overload
    def Set(self,C : OCP.gp.gp_Circ,F : float,L : float) -> None: 
        """
        None

        None
        """
    @overload
    def Set(self,C : OCP.gp.gp_Lin,F : float,L : float) -> None: ...
    def __init__(self) -> None: ...
    pass
class ChFiDS_CommonPoint():
    """
    point start/end of fillet common to 2 adjacent filets and to an edge on one of 2 faces participating in the construction of the fillet
    """
    def Arc(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the arc of restriction containing the vertex.
        """
    def HasVector(self) -> bool: 
        """
        Returns TRUE if the output vector is stored.
        """
    def IsOnArc(self) -> bool: 
        """
        Returns TRUE if the point is a on an edge of the initial restriction facet of the surface.
        """
    def IsVertex(self) -> bool: 
        """
        Returns TRUE if the point is a vertex on the initial restriction facet of the surface.
        """
    def Parameter(self) -> float: 
        """
        Returns the parameter the paramter on the spine
        """
    def ParameterOnArc(self) -> float: 
        """
        Returns the parameter of the point on the arc returned by the method Arc().
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the 3d point
        """
    def Reset(self) -> None: 
        """
        default value for all fields
        """
    def SetArc(self,Tol : float,A : OCP.TopoDS.TopoDS_Edge,Param : float,TArc : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Sets the values of a point which is on the arc A, at parameter Param.
        """
    def SetParameter(self,Param : float) -> None: 
        """
        Sets the value of the parameter on the spine
        """
    def SetPoint(self,thePoint : OCP.gp.gp_Pnt) -> None: 
        """
        Set the 3d point for a commonpoint that is not a vertex or on an arc.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        This method set the fuzziness on the point.
        """
    def SetVector(self,theVector : OCP.gp.gp_Vec) -> None: 
        """
        Set the output 3d vector
        """
    def SetVertex(self,theVertex : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Sets the values of a point which is a vertex on the initial facet of restriction of one of the surface.
        """
    def Tolerance(self) -> float: 
        """
        This method returns the fuzziness on the point.
        """
    def TransitionOnArc(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the transition of the point on the arc returned by Arc().
        """
    def Vector(self) -> OCP.gp.gp_Vec: 
        """
        Returns the output 3d vector
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the information about the point when it is on the domain of the first patch, i-e when the function IsVertex returns True. Otherwise, an exception is raised.
        """
    def __init__(self) -> None: ...
    pass
class ChFiDS_ElSpine(OCP.Adaptor3d.Adaptor3d_Curve):
    """
    Elementary Spine for cheminements and approximations.
    """
    def AddVertexWithTangent(self,anAx1 : OCP.gp.gp_Ax1) -> None: 
        """
        None
        """
    def BSpline(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierCurve: 
        """
        None
        """
    def ChangeNext(self) -> ChFiDS_SurfData: 
        """
        None
        """
    def ChangePrevious(self) -> ChFiDS_SurfData: 
        """
        None
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def D0(self,AbsC : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,AbsC : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,AbsC : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D3(self,AbsC : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    def Degree(self) -> int: 
        """
        None
        """
    def Ellipse(self) -> OCP.gp.gp_Elips: 
        """
        None
        """
    @overload
    def FirstParameter(self) -> float: 
        """
        None

        None
        """
    @overload
    def FirstParameter(self,P : float) -> None: ...
    def FirstPointAndTgt(self,P : OCP.gp.gp_Pnt,T : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def GetSavedFirstParameter(self) -> float: 
        """
        None
        """
    def GetSavedLastParameter(self) -> float: 
        """
        None
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        None
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        None
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def IsRational(self) -> bool: 
        """
        None
        """
    @overload
    def LastParameter(self) -> float: 
        """
        None

        None
        """
    @overload
    def LastParameter(self,P : float) -> None: ...
    def LastPointAndTgt(self,P : OCP.gp.gp_Pnt,T : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        None
        """
    def NbKnots(self) -> int: 
        """
        None
        """
    def NbPoles(self) -> int: 
        """
        None
        """
    def NbVertices(self) -> int: 
        """
        None
        """
    def Next(self) -> ChFiDS_SurfData: 
        """
        None
        """
    def OffsetCurve(self) -> OCP.Geom.Geom_OffsetCurve: 
        """
        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab: 
        """
        None
        """
    def Period(self) -> float: 
        """
        None
        """
    def Previous(self) -> ChFiDS_SurfData: 
        """
        None
        """
    def Resolution(self,R3d : float) -> float: 
        """
        None
        """
    def SaveFirstParameter(self) -> None: 
        """
        None
        """
    def SaveLastParameter(self) -> None: 
        """
        None
        """
    def SetCurve(self,C : OCP.Geom.Geom_Curve) -> None: 
        """
        None
        """
    def SetFirstPointAndTgt(self,P : OCP.gp.gp_Pnt,T : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetLastPointAndTgt(self,P : OCP.gp.gp_Pnt,T : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetOrigin(self,O : float) -> None: 
        """
        None
        """
    def SetPeriodic(self,I : bool) -> None: 
        """
        None
        """
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion.
        """
    def Value(self,AbsC : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def VertexWithTangent(self,Index : int) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class ChFiDS_ErrorStatus():
    """
    --- Purpose statuts concernant la cause de l'erreur

    Members:

      ChFiDS_Ok

      ChFiDS_Error

      ChFiDS_WalkingFailure

      ChFiDS_StartsolFailure

      ChFiDS_TwistedSurface
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    ChFiDS_Error: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_Error
    ChFiDS_Ok: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_Ok
    ChFiDS_StartsolFailure: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_StartsolFailure
    ChFiDS_TwistedSurface: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_TwistedSurface
    ChFiDS_WalkingFailure: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_WalkingFailure
    __entries: dict # value = {'ChFiDS_Ok': (ChFiDS_ErrorStatus.ChFiDS_Ok, None), 'ChFiDS_Error': (ChFiDS_ErrorStatus.ChFiDS_Error, None), 'ChFiDS_WalkingFailure': (ChFiDS_ErrorStatus.ChFiDS_WalkingFailure, None), 'ChFiDS_StartsolFailure': (ChFiDS_ErrorStatus.ChFiDS_StartsolFailure, None), 'ChFiDS_TwistedSurface': (ChFiDS_ErrorStatus.ChFiDS_TwistedSurface, None)}
    __members__: dict # value = {'ChFiDS_Ok': ChFiDS_ErrorStatus.ChFiDS_Ok, 'ChFiDS_Error': ChFiDS_ErrorStatus.ChFiDS_Error, 'ChFiDS_WalkingFailure': ChFiDS_ErrorStatus.ChFiDS_WalkingFailure, 'ChFiDS_StartsolFailure': ChFiDS_ErrorStatus.ChFiDS_StartsolFailure, 'ChFiDS_TwistedSurface': ChFiDS_ErrorStatus.ChFiDS_TwistedSurface}
    pass
class ChFiDS_FaceInterference():
    """
    interference face/fillet
    """
    def ChangePCurveOnFace(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    def ChangePCurveOnSurf(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    def FirstParameter(self) -> float: 
        """
        None

        None
        """
    def LastParameter(self) -> float: 
        """
        None

        None
        """
    def LineIndex(self) -> int: 
        """
        None

        None
        """
    def PCurveOnFace(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    def PCurveOnSurf(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    def Parameter(self,IsFirst : bool) -> float: 
        """
        None
        """
    def SetFirstParameter(self,U1 : float) -> None: 
        """
        None

        None
        """
    def SetInterference(self,LineIndex : int,Trans : OCP.TopAbs.TopAbs_Orientation,PCurv1 : OCP.Geom2d.Geom2d_Curve,PCurv2 : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    def SetLastParameter(self,U1 : float) -> None: 
        """
        None

        None
        """
    def SetLineIndex(self,I : int) -> None: 
        """
        None

        None
        """
    def SetParameter(self,U1 : float,IsFirst : bool) -> None: 
        """
        None
        """
    def SetTransition(self,Trans : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        None
        """
    def Transition(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    def __init__(self) -> None: ...
    pass
class ChFiDS_FilSpine(ChFiDS_Spine, OCP.Standard.Standard_Transient):
    """
    Provides data specific to the fillets - vector or rule of evolution (C2).Provides data specific to the fillets - vector or rule of evolution (C2).Provides data specific to the fillets - vector or rule of evolution (C2).
    """
    @overload
    def Absc(self,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        None

        None

        None
        """
    @overload
    def Absc(self,U : float,I : int) -> float: ...
    @overload
    def Absc(self,U : float) -> float: ...
    def AppendElSpine(self,Els : ChFiDS_HElSpine) -> None: 
        """
        None
        """
    def AppendOffsetElSpine(self,Els : ChFiDS_HElSpine) -> None: 
        """
        None
        """
    def ChangeElSpines(self) -> ChFiDS_ListOfHElSpine: 
        """
        None
        """
    def ChangeLaw(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.Law.Law_Function: 
        """
        returns the elementary law
        """
    def ChangeOffsetElSpines(self) -> ChFiDS_ListOfHElSpine: 
        """
        None
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None
        """
    def CurrentElementarySpine(self,Index : int) -> OCP.BRepAdaptor.BRepAdaptor_Curve: 
        """
        sets the current curve and returns it
        """
    def CurrentIndexOfElementarySpine(self) -> int: 
        """
        None

        None
        """
    def D0(self,AbsC : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,AbsC : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,AbsC : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
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
    def Edges(self,I : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    @overload
    def ElSpine(self,IE : int) -> ChFiDS_HElSpine: 
        """
        None

        None

        None
        """
    @overload
    def ElSpine(self,E : OCP.TopoDS.TopoDS_Edge) -> ChFiDS_HElSpine: ...
    @overload
    def ElSpine(self,W : float) -> ChFiDS_HElSpine: ...
    def ErrorStatus(self) -> ChFiDS_ErrorStatus: 
        """
        None
        """
    @overload
    def FirstParameter(self,IndexSpine : int) -> float: 
        """
        None

        gives the total length of all arcs before the number IndexSp
        """
    @overload
    def FirstParameter(self) -> float: ...
    def FirstStatus(self) -> ChFiDS_State: 
        """
        returns if the set of edges starts on a free boundary or if the first vertex is a breakpoint or if the set is closed

        returns if the set of edges starts on a free boundary or if the first vertex is a breakpoint or if the set is closed
        """
    def FirstVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        None
        """
    def HasFirstTgt(self) -> bool: 
        """
        None
        """
    def HasLastTgt(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Index(self,W : float,Forward : bool=True) -> int: 
        """
        None

        None
        """
    @overload
    def Index(self,E : OCP.TopoDS.TopoDS_Edge) -> int: ...
    def IsClosed(self) -> bool: 
        """
        None
        """
    @overload
    def IsConstant(self,IE : int) -> bool: 
        """
        returns true if the radius is constant all along the spine.

        returns true if the radius is constant all along the edge E.
        """
    @overload
    def IsConstant(self) -> bool: ...
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
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def IsTangencyExtremity(self,IsFirst : bool) -> bool: 
        """
        returns if the set of edges starts (or end) on Tangency point.

        returns if the set of edges starts (or end) on Tangency point.
        """
    @overload
    def LastParameter(self) -> float: 
        """
        None

        gives the total length till the ark with number IndexSpine (inclus)
        """
    @overload
    def LastParameter(self,IndexSpine : int) -> float: ...
    def LastStatus(self) -> ChFiDS_State: 
        """
        returns the state at the end of the set

        returns the state at the end of the set
        """
    def LastVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def Law(self,Els : ChFiDS_HElSpine) -> OCP.Law.Law_Composite: 
        """
        None
        """
    def Length(self,IndexSpine : int) -> float: 
        """
        gives the length of ark with number IndexSp
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def Load(self) -> None: 
        """
        prepare the guideline depending on the edges that are elementary arks (take parameters from a single curvilinear abscissa); to be able to call methods on the geometry (first,last,value,d1,d2) it is necessary to start with preparation otherwise an exception will be raised
        """
    def MaxRadFromSeqAndLaws(self) -> float: 
        """
        returns the maximum radius if the fillet is non-constant
        """
    def Mode(self) -> ChFiDS_ChamfMode: 
        """
        Return the mode of chamfers used

        Return the mode of chamfers used
        """
    def NbEdges(self) -> int: 
        """
        None

        None
        """
    def OffsetEdges(self,I : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    @overload
    def Parameter(self,AbsC : float,Oriented : bool=True) -> Tuple[float]: 
        """
        None

        None
        """
    @overload
    def Parameter(self,Index : int,AbsC : float,Oriented : bool=True) -> Tuple[float]: ...
    def Period(self) -> float: 
        """
        None
        """
    def PutInFirst(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store the edge at the first position before all others

        store the edge at the first position before all others
        """
    def PutInFirstOffset(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store the offset edge at the first position before all others

        store the offset edge at the first position before all others
        """
    @overload
    def Radius(self,E : OCP.TopoDS.TopoDS_Edge) -> float: 
        """
        returns the radius if the fillet is constant all along the spine.

        returns the radius if the fillet is constant all along the edge E.

        returns the radius if the fillet is constant all along the edge E.
        """
    @overload
    def Radius(self) -> float: ...
    @overload
    def Radius(self,IE : int) -> float: ...
    def Reset(self,AllData : bool=False) -> None: 
        """
        None
        """
    def Resolution(self,R3d : float) -> float: 
        """
        None
        """
    def SetCurrent(self,Index : int) -> None: 
        """
        None
        """
    def SetEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store edges composing the guideline

        store edges composing the guideline
        """
    def SetErrorStatus(self,state : ChFiDS_ErrorStatus) -> None: 
        """
        None
        """
    def SetFirstParameter(self,Par : float) -> None: 
        """
        None
        """
    def SetFirstStatus(self,S : ChFiDS_State) -> None: 
        """
        stores if the start of a set of edges starts on a section of free border or forms a closed contour

        stores if the start of a set of edges starts on a section of free border or forms a closed contour
        """
    def SetFirstTgt(self,W : float) -> None: 
        """
        None
        """
    def SetLastParameter(self,Par : float) -> None: 
        """
        None
        """
    def SetLastStatus(self,S : ChFiDS_State) -> None: 
        """
        stores if the end of a set of edges starts on a section of free border or forms a closed contour

        stores if the end of a set of edges starts on a section of free border or forms a closed contour
        """
    def SetLastTgt(self,W : float) -> None: 
        """
        None
        """
    def SetOffsetEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store offset edges composing the offset guideline

        store offset edges composing the offset guideline
        """
    @overload
    def SetRadius(self,Radius : float,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        initializes the constant vector on edge E.

        initializes the vector on Vertex V.

        initializes the vector on the point of parameter W.

        initializes the constant vector on all spine.

        initializes the rule of evolution on all spine.
        """
    @overload
    def SetRadius(self,UandR : OCP.gp.gp_XY,IinC : int) -> None: ...
    @overload
    def SetRadius(self,Radius : float,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def SetRadius(self,Radius : float) -> None: ...
    @overload
    def SetRadius(self,C : OCP.Law.Law_Function,IinC : int) -> None: ...
    @overload
    def SetReference(self,W : float) -> None: 
        """
        set a parameter reference for the approx.

        set a parameter reference for the approx, at the middle of edge I.
        """
    @overload
    def SetReference(self,I : int) -> None: ...
    def SetStatus(self,S : ChFiDS_State,IsFirst : bool) -> None: 
        """
        None

        None
        """
    def SetTangencyExtremity(self,IsTangency : bool,IsFirst : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SplitDone(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SplitDone(self) -> bool: ...
    def Status(self,IsFirst : bool) -> ChFiDS_State: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def UnSetRadius(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        resets the constant vector on edge E.

        resets the vector on Vertex V.
        """
    @overload
    def UnSetRadius(self,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    def UnsetReference(self) -> None: 
        """
        None
        """
    def Value(self,AbsC : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @overload
    def __init__(self,Tol : float) -> None: ...
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
class ChFiDS_SequenceOfSurfData(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : ChFiDS_SequenceOfSurfData) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : ChFiDS_SurfData) -> None: ...
    def Assign(self,theOther : ChFiDS_SequenceOfSurfData) -> ChFiDS_SequenceOfSurfData: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> ChFiDS_SurfData: 
        """
        First item access
        """
    def ChangeLast(self) -> ChFiDS_SurfData: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> ChFiDS_SurfData: 
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
    def First(self) -> ChFiDS_SurfData: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : ChFiDS_SequenceOfSurfData) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : ChFiDS_SurfData) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ChFiDS_SequenceOfSurfData) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : ChFiDS_SurfData) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> ChFiDS_SurfData: 
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
    def Prepend(self,theSeq : ChFiDS_SequenceOfSurfData) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : ChFiDS_SurfData) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : ChFiDS_SurfData) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ChFiDS_SequenceOfSurfData) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> ChFiDS_SurfData: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : ChFiDS_SequenceOfSurfData) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class ChFiDS_HElSpine(OCP.Adaptor3d.Adaptor3d_HCurve, OCP.Standard.Standard_Transient):
    def BSpline(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None

        None
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierCurve: 
        """
        None

        None
        """
    def ChangeCurve(self) -> ChFiDS_ElSpine: 
        """
        Returns the curve used to create the GenHCurve.
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None

        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    def Curve(self) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        Returns the curve used to create the GenHCurve. This is redefined from HCurve, cannot be inline.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None

        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        None

        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        None

        None
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        None

        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
        """
        None

        None
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Ellipse(self) -> OCP.gp.gp_Elips: 
        """
        None

        None
        """
    def FirstParameter(self) -> float: 
        """
        None

        None
        """
    def GetCurve(self) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        Returns the curve used to create the GenHCurve. This is redefined from HCurve, cannot be inline.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        None

        None
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr: 
        """
        None

        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.

        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsClosed(self) -> bool: 
        """
        None

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
    def LastParameter(self) -> float: 
        """
        None

        None
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None

        None
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        None

        None
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
    def OffsetCurve(self) -> OCP.Geom.Geom_OffsetCurve: 
        """
        None

        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab: 
        """
        None

        None
        """
    def Period(self) -> float: 
        """
        None

        None
        """
    def Resolution(self,R3d : float) -> float: 
        """
        None

        None
        """
    def Set(self,C : ChFiDS_ElSpine) -> None: 
        """
        Sets the field of the GenHCurve.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion.

        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion.
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : ChFiDS_ElSpine) -> None: ...
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
class ChFiDS_IndexedDataMapOfVertexListOfStripe(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Vertex,theItem : ChFiDS_ListOfStripe) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : ChFiDS_IndexedDataMapOfVertexListOfStripe) -> ChFiDS_IndexedDataMapOfVertexListOfStripe: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> ChFiDS_ListOfStripe: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> ChFiDS_ListOfStripe: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> ChFiDS_ListOfStripe: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : ChFiDS_IndexedDataMapOfVertexListOfStripe) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> ChFiDS_ListOfStripe: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Vertex,theValue : ChFiDS_ListOfStripe) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> ChFiDS_ListOfStripe: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        FindKey
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
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> ChFiDS_ListOfStripe: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Vertex,theItem : ChFiDS_ListOfStripe) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : ChFiDS_IndexedDataMapOfVertexListOfStripe) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ChFiDS_ListOfHElSpine(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : ChFiDS_ListOfHElSpine) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : ChFiDS_HElSpine) -> ChFiDS_HElSpine: ...
    @overload
    def Append(self,theItem : ChFiDS_HElSpine,theIter : Any) -> None: ...
    def Assign(self,theOther : ChFiDS_ListOfHElSpine) -> ChFiDS_ListOfHElSpine: 
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
    def First(self) -> ChFiDS_HElSpine: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : ChFiDS_ListOfHElSpine,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : ChFiDS_HElSpine,theIter : Any) -> ChFiDS_HElSpine: ...
    @overload
    def InsertBefore(self,theItem : ChFiDS_HElSpine,theIter : Any) -> ChFiDS_HElSpine: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : ChFiDS_ListOfHElSpine,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> ChFiDS_HElSpine: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : ChFiDS_HElSpine) -> ChFiDS_HElSpine: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : ChFiDS_ListOfHElSpine) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : ChFiDS_ListOfHElSpine) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ChFiDS_ListOfStripe(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : ChFiDS_Stripe) -> ChFiDS_Stripe: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : ChFiDS_ListOfStripe) -> None: ...
    @overload
    def Append(self,theItem : ChFiDS_Stripe,theIter : Any) -> None: ...
    def Assign(self,theOther : ChFiDS_ListOfStripe) -> ChFiDS_ListOfStripe: 
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
    def First(self) -> ChFiDS_Stripe: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : ChFiDS_Stripe,theIter : Any) -> ChFiDS_Stripe: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : ChFiDS_ListOfStripe,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : ChFiDS_ListOfStripe,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : ChFiDS_Stripe,theIter : Any) -> ChFiDS_Stripe: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> ChFiDS_Stripe: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : ChFiDS_Stripe) -> ChFiDS_Stripe: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : ChFiDS_ListOfStripe) -> None: ...
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
    def __init__(self,theOther : ChFiDS_ListOfStripe) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ChFiDS_Map():
    """
    Encapsulation of IndexedDataMapOfShapeListOfShape.
    """
    def Contains(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def Fill(self,S : OCP.TopoDS.TopoDS_Shape,T1 : OCP.TopAbs.TopAbs_ShapeEnum,T2 : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        Fills the map with the subshapes of type T1 as keys and the list of ancestors of type T2 as items.
        """
    def FindFromIndex(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def FindFromKey(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class ChFiDS_Regul():
    """
    Storage of a curve and its 2 faces or surfaces of support.
    """
    def Curve(self) -> int: 
        """
        None
        """
    def IsSurface1(self) -> bool: 
        """
        None
        """
    def IsSurface2(self) -> bool: 
        """
        None
        """
    def S1(self) -> int: 
        """
        None
        """
    def S2(self) -> int: 
        """
        None
        """
    def SetCurve(self,IC : int) -> None: 
        """
        None
        """
    def SetS1(self,IS1 : int,IsFace : bool=True) -> None: 
        """
        None
        """
    def SetS2(self,IS2 : int,IsFace : bool=True) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class ChFiDS_Regularities(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : ChFiDS_Regularities) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : ChFiDS_Regul) -> ChFiDS_Regul: ...
    @overload
    def Append(self,theItem : ChFiDS_Regul,theIter : Any) -> None: ...
    def Assign(self,theOther : ChFiDS_Regularities) -> ChFiDS_Regularities: 
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
    def First(self) -> ChFiDS_Regul: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : ChFiDS_Regul,theIter : Any) -> ChFiDS_Regul: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : ChFiDS_Regularities,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : ChFiDS_Regul,theIter : Any) -> ChFiDS_Regul: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : ChFiDS_Regularities,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> ChFiDS_Regul: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : ChFiDS_Regul) -> ChFiDS_Regul: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : ChFiDS_Regularities) -> None: ...
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
    def __init__(self,theOther : ChFiDS_Regularities) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ChFiDS_SecArray1():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : ChFiDS_SecArray1) -> ChFiDS_SecArray1: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> ChFiDS_CircSection: 
        """
        Returns first element
        """
    def ChangeLast(self) -> ChFiDS_CircSection: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> ChFiDS_CircSection: 
        """
        Variable value access
        """
    def First(self) -> ChFiDS_CircSection: 
        """
        Returns first element
        """
    def Init(self,theValue : ChFiDS_CircSection) -> None: 
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
    def Last(self) -> ChFiDS_CircSection: 
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
    def Move(self,theOther : ChFiDS_SecArray1) -> ChFiDS_SecArray1: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : ChFiDS_CircSection) -> None: 
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
    def Value(self,theIndex : int) -> ChFiDS_CircSection: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : ChFiDS_CircSection,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : ChFiDS_SecArray1) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ChFiDS_SecHArray1(ChFiDS_SecArray1, OCP.Standard.Standard_Transient):
    def Array1(self) -> ChFiDS_SecArray1: 
        """
        None
        """
    def Assign(self,theOther : ChFiDS_SecArray1) -> ChFiDS_SecArray1: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> ChFiDS_SecArray1: 
        """
        None
        """
    def ChangeFirst(self) -> ChFiDS_CircSection: 
        """
        Returns first element
        """
    def ChangeLast(self) -> ChFiDS_CircSection: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> ChFiDS_CircSection: 
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
    def First(self) -> ChFiDS_CircSection: 
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
    def Init(self,theValue : ChFiDS_CircSection) -> None: 
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
    def Last(self) -> ChFiDS_CircSection: 
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
    def Move(self,theOther : ChFiDS_SecArray1) -> ChFiDS_SecArray1: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : ChFiDS_CircSection) -> None: 
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
    def Value(self,theIndex : int) -> ChFiDS_CircSection: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : ChFiDS_CircSection) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : ChFiDS_SecArray1) -> None: ...
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
class ChFiDS_SequenceOfSpine(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : ChFiDS_SequenceOfSpine) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : ChFiDS_Spine) -> None: ...
    def Assign(self,theOther : ChFiDS_SequenceOfSpine) -> ChFiDS_SequenceOfSpine: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> ChFiDS_Spine: 
        """
        First item access
        """
    def ChangeLast(self) -> ChFiDS_Spine: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> ChFiDS_Spine: 
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
    def First(self) -> ChFiDS_Spine: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : ChFiDS_Spine) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : ChFiDS_SequenceOfSpine) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : ChFiDS_Spine) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ChFiDS_SequenceOfSpine) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> ChFiDS_Spine: 
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
    def Prepend(self,theSeq : ChFiDS_SequenceOfSpine) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : ChFiDS_Spine) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : ChFiDS_Spine) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ChFiDS_SequenceOfSpine) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> ChFiDS_Spine: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : ChFiDS_SequenceOfSpine) -> None: ...
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
class ChFiDS_HData(ChFiDS_SequenceOfSurfData, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : ChFiDS_SequenceOfSurfData) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : ChFiDS_SurfData) -> None: ...
    def Assign(self,theOther : ChFiDS_SequenceOfSurfData) -> ChFiDS_SequenceOfSurfData: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> ChFiDS_SurfData: 
        """
        First item access
        """
    def ChangeLast(self) -> ChFiDS_SurfData: 
        """
        Last item access
        """
    def ChangeSequence(self) -> ChFiDS_SequenceOfSurfData: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> ChFiDS_SurfData: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
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
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> ChFiDS_SurfData: 
        """
        First item access
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
    def InsertAfter(self,theIndex : int,theSeq : ChFiDS_SequenceOfSurfData) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : ChFiDS_SurfData) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ChFiDS_SequenceOfSurfData) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : ChFiDS_SurfData) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> ChFiDS_SurfData: 
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
    def Prepend(self,theSeq : ChFiDS_SequenceOfSurfData) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : ChFiDS_SurfData) -> None: ...
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
    def Sequence(self) -> ChFiDS_SequenceOfSurfData: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : ChFiDS_SurfData) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ChFiDS_SequenceOfSurfData) -> None: 
        """
        Split in two sequences
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> ChFiDS_SurfData: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : ChFiDS_SequenceOfSurfData) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
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
class ChFiDS_ChamfSpine(ChFiDS_Spine, OCP.Standard.Standard_Transient):
    """
    Provides data specific to chamfers distances on each of faces.Provides data specific to chamfers distances on each of faces.Provides data specific to chamfers distances on each of faces.
    """
    @overload
    def Absc(self,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        None

        None

        None
        """
    @overload
    def Absc(self,U : float,I : int) -> float: ...
    @overload
    def Absc(self,U : float) -> float: ...
    def AppendElSpine(self,Els : ChFiDS_HElSpine) -> None: 
        """
        None
        """
    def AppendOffsetElSpine(self,Els : ChFiDS_HElSpine) -> None: 
        """
        None
        """
    def ChangeElSpines(self) -> ChFiDS_ListOfHElSpine: 
        """
        None
        """
    def ChangeOffsetElSpines(self) -> ChFiDS_ListOfHElSpine: 
        """
        None
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None
        """
    def CurrentElementarySpine(self,Index : int) -> OCP.BRepAdaptor.BRepAdaptor_Curve: 
        """
        sets the current curve and returns it
        """
    def CurrentIndexOfElementarySpine(self) -> int: 
        """
        None

        None
        """
    def D0(self,AbsC : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,AbsC : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,AbsC : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
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
    def Dists(self) -> Tuple[float, float]: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edges(self,I : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    @overload
    def ElSpine(self,IE : int) -> ChFiDS_HElSpine: 
        """
        None

        None

        None
        """
    @overload
    def ElSpine(self,E : OCP.TopoDS.TopoDS_Edge) -> ChFiDS_HElSpine: ...
    @overload
    def ElSpine(self,W : float) -> ChFiDS_HElSpine: ...
    def ErrorStatus(self) -> ChFiDS_ErrorStatus: 
        """
        None
        """
    @overload
    def FirstParameter(self,IndexSpine : int) -> float: 
        """
        None

        gives the total length of all arcs before the number IndexSp
        """
    @overload
    def FirstParameter(self) -> float: ...
    def FirstStatus(self) -> ChFiDS_State: 
        """
        returns if the set of edges starts on a free boundary or if the first vertex is a breakpoint or if the set is closed

        returns if the set of edges starts on a free boundary or if the first vertex is a breakpoint or if the set is closed
        """
    def FirstVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def GetDist(self) -> Tuple[float]: 
        """
        None
        """
    def GetDistAngle(self) -> Tuple[float, float]: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        None
        """
    def HasFirstTgt(self) -> bool: 
        """
        None
        """
    def HasLastTgt(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Index(self,W : float,Forward : bool=True) -> int: 
        """
        None

        None
        """
    @overload
    def Index(self,E : OCP.TopoDS.TopoDS_Edge) -> int: ...
    def IsChamfer(self) -> ChFiDS_ChamfMethod: 
        """
        Return the method of chamfers used
        """
    def IsClosed(self) -> bool: 
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
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def IsTangencyExtremity(self,IsFirst : bool) -> bool: 
        """
        returns if the set of edges starts (or end) on Tangency point.

        returns if the set of edges starts (or end) on Tangency point.
        """
    @overload
    def LastParameter(self) -> float: 
        """
        None

        gives the total length till the ark with number IndexSpine (inclus)
        """
    @overload
    def LastParameter(self,IndexSpine : int) -> float: ...
    def LastStatus(self) -> ChFiDS_State: 
        """
        returns the state at the end of the set

        returns the state at the end of the set
        """
    def LastVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def Length(self,IndexSpine : int) -> float: 
        """
        gives the length of ark with number IndexSp
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def Load(self) -> None: 
        """
        prepare the guideline depending on the edges that are elementary arks (take parameters from a single curvilinear abscissa); to be able to call methods on the geometry (first,last,value,d1,d2) it is necessary to start with preparation otherwise an exception will be raised
        """
    def Mode(self) -> ChFiDS_ChamfMode: 
        """
        Return the mode of chamfers used

        Return the mode of chamfers used
        """
    def NbEdges(self) -> int: 
        """
        None

        None
        """
    def OffsetEdges(self,I : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    @overload
    def Parameter(self,AbsC : float,Oriented : bool=True) -> Tuple[float]: 
        """
        None

        None
        """
    @overload
    def Parameter(self,Index : int,AbsC : float,Oriented : bool=True) -> Tuple[float]: ...
    def Period(self) -> float: 
        """
        None
        """
    def PutInFirst(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store the edge at the first position before all others

        store the edge at the first position before all others
        """
    def PutInFirstOffset(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store the offset edge at the first position before all others

        store the offset edge at the first position before all others
        """
    def Reset(self,AllData : bool=False) -> None: 
        """
        None
        """
    def Resolution(self,R3d : float) -> float: 
        """
        None
        """
    def SetCurrent(self,Index : int) -> None: 
        """
        None
        """
    def SetDist(self,Dis : float) -> None: 
        """
        None
        """
    def SetDistAngle(self,Dis : float,Angle : float) -> None: 
        """
        None
        """
    def SetDists(self,Dis1 : float,Dis2 : float) -> None: 
        """
        None
        """
    def SetEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store edges composing the guideline

        store edges composing the guideline
        """
    def SetErrorStatus(self,state : ChFiDS_ErrorStatus) -> None: 
        """
        None
        """
    def SetFirstParameter(self,Par : float) -> None: 
        """
        None
        """
    def SetFirstStatus(self,S : ChFiDS_State) -> None: 
        """
        stores if the start of a set of edges starts on a section of free border or forms a closed contour

        stores if the start of a set of edges starts on a section of free border or forms a closed contour
        """
    def SetFirstTgt(self,W : float) -> None: 
        """
        None
        """
    def SetLastParameter(self,Par : float) -> None: 
        """
        None
        """
    def SetLastStatus(self,S : ChFiDS_State) -> None: 
        """
        stores if the end of a set of edges starts on a section of free border or forms a closed contour

        stores if the end of a set of edges starts on a section of free border or forms a closed contour
        """
    def SetLastTgt(self,W : float) -> None: 
        """
        None
        """
    def SetMode(self,theMode : ChFiDS_ChamfMode) -> None: 
        """
        None
        """
    def SetOffsetEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        store offset edges composing the offset guideline

        store offset edges composing the offset guideline
        """
    @overload
    def SetReference(self,W : float) -> None: 
        """
        set a parameter reference for the approx.

        set a parameter reference for the approx, at the middle of edge I.
        """
    @overload
    def SetReference(self,I : int) -> None: ...
    def SetStatus(self,S : ChFiDS_State,IsFirst : bool) -> None: 
        """
        None

        None
        """
    def SetTangencyExtremity(self,IsTangency : bool,IsFirst : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SplitDone(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SplitDone(self) -> bool: ...
    def Status(self,IsFirst : bool) -> ChFiDS_State: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnsetReference(self) -> None: 
        """
        None
        """
    def Value(self,AbsC : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Tol : float) -> None: ...
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
class ChFiDS_State():
    """
    This enum describe the different kinds of extremities of a fillet. OnSame, Ondiff and AllSame are particular cases of BreakPoint for a corner with 3 edges and three faces : - AllSame means that the three concavities are on the same side of the Shape, - OnDiff means that the edge of the fillet has a concave side different than the two other edges, - OnSame means that the edge of the fillet has a concave side different than one of the two other edges and identical to the third edge.

    Members:

      ChFiDS_OnSame

      ChFiDS_OnDiff

      ChFiDS_AllSame

      ChFiDS_BreakPoint

      ChFiDS_FreeBoundary

      ChFiDS_Closed

      ChFiDS_Tangent
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    ChFiDS_AllSame: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_AllSame
    ChFiDS_BreakPoint: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_BreakPoint
    ChFiDS_Closed: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_Closed
    ChFiDS_FreeBoundary: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_FreeBoundary
    ChFiDS_OnDiff: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_OnDiff
    ChFiDS_OnSame: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_OnSame
    ChFiDS_Tangent: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_Tangent
    __entries: dict # value = {'ChFiDS_OnSame': (ChFiDS_State.ChFiDS_OnSame, None), 'ChFiDS_OnDiff': (ChFiDS_State.ChFiDS_OnDiff, None), 'ChFiDS_AllSame': (ChFiDS_State.ChFiDS_AllSame, None), 'ChFiDS_BreakPoint': (ChFiDS_State.ChFiDS_BreakPoint, None), 'ChFiDS_FreeBoundary': (ChFiDS_State.ChFiDS_FreeBoundary, None), 'ChFiDS_Closed': (ChFiDS_State.ChFiDS_Closed, None), 'ChFiDS_Tangent': (ChFiDS_State.ChFiDS_Tangent, None)}
    __members__: dict # value = {'ChFiDS_OnSame': ChFiDS_State.ChFiDS_OnSame, 'ChFiDS_OnDiff': ChFiDS_State.ChFiDS_OnDiff, 'ChFiDS_AllSame': ChFiDS_State.ChFiDS_AllSame, 'ChFiDS_BreakPoint': ChFiDS_State.ChFiDS_BreakPoint, 'ChFiDS_FreeBoundary': ChFiDS_State.ChFiDS_FreeBoundary, 'ChFiDS_Closed': ChFiDS_State.ChFiDS_Closed, 'ChFiDS_Tangent': ChFiDS_State.ChFiDS_Tangent}
    pass
class ChFiDS_Stripe(OCP.Standard.Standard_Transient):
    """
    Data characterising a band of fillet.Data characterising a band of fillet.Data characterising a band of fillet.
    """
    def ChangeFirstCurve(self,Index : int) -> None: 
        """
        None

        None
        """
    def ChangeFirstPCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    def ChangeFirstParameters(self,Pdeb : float,Pfin : float) -> None: 
        """
        None

        None
        """
    def ChangeIndexFirstPointOnS1(self,Index : int) -> None: 
        """
        None

        None
        """
    def ChangeIndexFirstPointOnS2(self,Index : int) -> None: 
        """
        None

        None
        """
    def ChangeIndexLastPointOnS1(self,Index : int) -> None: 
        """
        None

        None
        """
    def ChangeIndexLastPointOnS2(self,Index : int) -> None: 
        """
        None

        None
        """
    def ChangeLastCurve(self,Index : int) -> None: 
        """
        None

        None
        """
    def ChangeLastPCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    def ChangeLastParameters(self,Pdeb : float,Pfin : float) -> None: 
        """
        None

        None
        """
    def ChangePCurve(self,First : bool) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def ChangeSetOfSurfData(self) -> ChFiDS_HData: 
        """
        None

        None
        """
    def ChangeSpine(self) -> ChFiDS_Spine: 
        """
        None

        None
        """
    @overload
    def Choix(self) -> int: 
        """
        None

        None

        None

        None
        """
    @overload
    def Choix(self,C : int) -> None: ...
    def Curve(self,First : bool) -> int: 
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
    def FirstCurve(self) -> int: 
        """
        None

        None
        """
    def FirstPCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def FirstPCurveOrientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None

        None

        None
        """
    @overload
    def FirstPCurveOrientation(self,O : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def FirstParameters(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def InDS(self,First : bool,Nb : int=1) -> None: 
        """
        Set nb of SurfData's at end put in DS
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IndexFirstPointOnS1(self) -> int: 
        """
        None

        None
        """
    def IndexFirstPointOnS2(self) -> int: 
        """
        None

        None
        """
    def IndexLastPointOnS1(self) -> int: 
        """
        None

        None
        """
    def IndexLastPointOnS2(self) -> int: 
        """
        None

        None
        """
    def IndexPoint(self,First : bool,OnS : int) -> int: 
        """
        None
        """
    def IsInDS(self,First : bool) -> int: 
        """
        Returns nb of SurfData's at end being in DS
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
    def LastCurve(self) -> int: 
        """
        None

        None
        """
    def LastPCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def LastPCurveOrientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None

        None

        None
        """
    @overload
    def LastPCurveOrientation(self,O : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def LastParameters(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    @overload
    def Orientation(self,OnS : int) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    @overload
    def Orientation(self,First : bool) -> OCP.TopAbs.TopAbs_Orientation: ...
    @overload
    def OrientationOnFace1(self,Or1 : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def OrientationOnFace1(self) -> OCP.TopAbs.TopAbs_Orientation: ...
    @overload
    def OrientationOnFace2(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None

        None

        None
        """
    @overload
    def OrientationOnFace2(self,Or2 : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def PCurve(self,First : bool) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def Parameters(self,First : bool) -> Tuple[float, float]: 
        """
        None
        """
    def Reset(self) -> None: 
        """
        Reset everything except Spine.
        """
    def SetCurve(self,Index : int,First : bool) -> None: 
        """
        None
        """
    def SetIndexPoint(self,Index : int,First : bool,OnS : int) -> None: 
        """
        None
        """
    def SetOfSurfData(self) -> ChFiDS_HData: 
        """
        None

        None
        """
    @overload
    def SetOrientation(self,Or : OCP.TopAbs.TopAbs_Orientation,OnS : int) -> None: 
        """
        None

        None
        """
    @overload
    def SetOrientation(self,Or : OCP.TopAbs.TopAbs_Orientation,First : bool) -> None: ...
    def SetParameters(self,First : bool,Pdeb : float,Pfin : float) -> None: 
        """
        None
        """
    def SetSolidIndex(self,Index : int) -> None: 
        """
        None
        """
    def SolidIndex(self) -> int: 
        """
        None
        """
    def Spine(self) -> ChFiDS_Spine: 
        """
        None

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
class ChFiDS_StripeArray1():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : ChFiDS_StripeArray1) -> ChFiDS_StripeArray1: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> ChFiDS_Stripe: 
        """
        Returns first element
        """
    def ChangeLast(self) -> ChFiDS_Stripe: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> ChFiDS_Stripe: 
        """
        Variable value access
        """
    def First(self) -> ChFiDS_Stripe: 
        """
        Returns first element
        """
    def Init(self,theValue : ChFiDS_Stripe) -> None: 
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
    def Last(self) -> ChFiDS_Stripe: 
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
    def Move(self,theOther : ChFiDS_StripeArray1) -> ChFiDS_StripeArray1: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : ChFiDS_Stripe) -> None: 
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
    def Value(self,theIndex : int) -> ChFiDS_Stripe: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : ChFiDS_StripeArray1) -> None: ...
    @overload
    def __init__(self,theBegin : ChFiDS_Stripe,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ChFiDS_StripeMap():
    """
    encapsulation of IndexedDataMapOfVertexListOfStripe
    """
    def Add(self,V : OCP.TopoDS.TopoDS_Vertex,F : ChFiDS_Stripe) -> None: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def Extent(self) -> int: 
        """
        None

        None
        """
    def FindFromIndex(self,I : int) -> ChFiDS_ListOfStripe: 
        """
        None
        """
    def FindFromKey(self,V : OCP.TopoDS.TopoDS_Vertex) -> ChFiDS_ListOfStripe: 
        """
        None
        """
    def FindKey(self,I : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None

        None
        """
    def __init__(self) -> None: ...
    pass
class ChFiDS_SurfData(OCP.Standard.Standard_Transient):
    """
    data structure for all information related to the fillet and to 2 faces vis a visdata structure for all information related to the fillet and to 2 faces vis a visdata structure for all information related to the fillet and to 2 faces vis a vis
    """
    def ChangeIndexOfS1(self,Index : int) -> None: 
        """
        None

        None
        """
    def ChangeIndexOfS2(self,Index : int) -> None: 
        """
        None

        None
        """
    def ChangeInterference(self,OnS : int) -> ChFiDS_FaceInterference: 
        """
        None
        """
    def ChangeInterferenceOnS1(self) -> ChFiDS_FaceInterference: 
        """
        None

        None
        """
    def ChangeInterferenceOnS2(self) -> ChFiDS_FaceInterference: 
        """
        None

        None
        """
    def ChangeOrientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    def ChangeSurf(self,Index : int) -> None: 
        """
        None

        None
        """
    def ChangeVertex(self,First : bool,OnS : int) -> ChFiDS_CommonPoint: 
        """
        returns one of the four vertices wether First is true or wrong and OnS equals 1 or 2.
        """
    def ChangeVertexFirstOnS1(self) -> ChFiDS_CommonPoint: 
        """
        None

        None
        """
    def ChangeVertexFirstOnS2(self) -> ChFiDS_CommonPoint: 
        """
        None

        None
        """
    def ChangeVertexLastOnS1(self) -> ChFiDS_CommonPoint: 
        """
        None

        None
        """
    def ChangeVertexLastOnS2(self) -> ChFiDS_CommonPoint: 
        """
        None

        None
        """
    def Copy(self,Other : ChFiDS_SurfData) -> None: 
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
    def FirstExtensionValue(self,Extend : float) -> None: 
        """
        None

        None
        """
    @overload
    def FirstExtensionValue(self) -> float: ...
    @overload
    def FirstSpineParam(self,Par : float) -> None: 
        """
        None

        None
        """
    @overload
    def FirstSpineParam(self) -> float: ...
    @overload
    def Get2dPoints(self,First : bool,OnS : int) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
        """
    @overload
    def Get2dPoints(self,P2df1 : OCP.gp.gp_Pnt2d,P2dl1 : OCP.gp.gp_Pnt2d,P2df2 : OCP.gp.gp_Pnt2d,P2dl2 : OCP.gp.gp_Pnt2d) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self,OfS : int) -> int: 
        """
        None
        """
    def IndexOfC(self,OnS : int) -> int: 
        """
        None

        None
        """
    def IndexOfC1(self) -> int: 
        """
        None

        None
        """
    def IndexOfC2(self) -> int: 
        """
        None

        None
        """
    def IndexOfS1(self) -> int: 
        """
        None

        None
        """
    def IndexOfS2(self) -> int: 
        """
        None

        None
        """
    def Interference(self,OnS : int) -> ChFiDS_FaceInterference: 
        """
        None
        """
    def InterferenceOnS1(self) -> ChFiDS_FaceInterference: 
        """
        None

        None
        """
    def InterferenceOnS2(self) -> ChFiDS_FaceInterference: 
        """
        None

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
    def IsOnCurve(self,OnS : int) -> bool: 
        """
        None

        None
        """
    def IsOnCurve1(self) -> bool: 
        """
        None

        None
        """
    def IsOnCurve2(self) -> bool: 
        """
        None

        None
        """
    @overload
    def LastExtensionValue(self,Extend : float) -> None: 
        """
        None

        None
        """
    @overload
    def LastExtensionValue(self) -> float: ...
    @overload
    def LastSpineParam(self,Par : float) -> None: 
        """
        None

        None
        """
    @overload
    def LastSpineParam(self) -> float: ...
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    def ResetSimul(self) -> None: 
        """
        None
        """
    def Set2dPoints(self,P2df1 : OCP.gp.gp_Pnt2d,P2dl1 : OCP.gp.gp_Pnt2d,P2df2 : OCP.gp.gp_Pnt2d,P2dl2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    @overload
    def SetIndexOfC1(self,Index : int) -> None: 
        """
        None

        None
        """
    @overload
    def SetIndexOfC1(self,theIndex : int) -> None: ...
    @overload
    def SetIndexOfC2(self,theIndex : int) -> None: 
        """
        None

        None
        """
    @overload
    def SetIndexOfC2(self,Index : int) -> None: ...
    def SetSimul(self,S : OCP.Standard.Standard_Transient) -> None: 
        """
        None
        """
    def Simul(self) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Surf(self) -> int: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def TwistOnS1(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def TwistOnS1(self,T : bool) -> None: ...
    @overload
    def TwistOnS2(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def TwistOnS2(self,T : bool) -> None: ...
    def Vertex(self,First : bool,OnS : int) -> ChFiDS_CommonPoint: 
        """
        returns one of the four vertices wether First is true or wrong and OnS equals 1 or 2.
        """
    def VertexFirstOnS1(self) -> ChFiDS_CommonPoint: 
        """
        None

        None
        """
    def VertexFirstOnS2(self) -> ChFiDS_CommonPoint: 
        """
        None

        None
        """
    def VertexLastOnS1(self) -> ChFiDS_CommonPoint: 
        """
        None

        None
        """
    def VertexLastOnS2(self) -> ChFiDS_CommonPoint: 
        """
        None

        None
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
ChFiDS_AllSame: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_AllSame
ChFiDS_BreakPoint: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_BreakPoint
ChFiDS_ClassicChamfer: OCP.ChFiDS.ChFiDS_ChamfMode # value = ChFiDS_ChamfMode.ChFiDS_ClassicChamfer
ChFiDS_Closed: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_Closed
ChFiDS_ConstThroatChamfer: OCP.ChFiDS.ChFiDS_ChamfMode # value = ChFiDS_ChamfMode.ChFiDS_ConstThroatChamfer
ChFiDS_ConstThroatWithPenetrationChamfer: OCP.ChFiDS.ChFiDS_ChamfMode # value = ChFiDS_ChamfMode.ChFiDS_ConstThroatWithPenetrationChamfer
ChFiDS_DistAngle: OCP.ChFiDS.ChFiDS_ChamfMethod # value = ChFiDS_ChamfMethod.ChFiDS_DistAngle
ChFiDS_Error: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_Error
ChFiDS_FreeBoundary: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_FreeBoundary
ChFiDS_Ok: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_Ok
ChFiDS_OnDiff: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_OnDiff
ChFiDS_OnSame: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_OnSame
ChFiDS_StartsolFailure: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_StartsolFailure
ChFiDS_Sym: OCP.ChFiDS.ChFiDS_ChamfMethod # value = ChFiDS_ChamfMethod.ChFiDS_Sym
ChFiDS_Tangent: OCP.ChFiDS.ChFiDS_State # value = ChFiDS_State.ChFiDS_Tangent
ChFiDS_TwistedSurface: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_TwistedSurface
ChFiDS_TwoDist: OCP.ChFiDS.ChFiDS_ChamfMethod # value = ChFiDS_ChamfMethod.ChFiDS_TwoDist
ChFiDS_WalkingFailure: OCP.ChFiDS.ChFiDS_ErrorStatus # value = ChFiDS_ErrorStatus.ChFiDS_WalkingFailure
