import OCP.BRepAdaptor
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.Adaptor3d
import OCP.Geom2dAdaptor
import OCP.TopoDS
import OCP.gp
import OCP.GeomAdaptor
import OCP.Geom2d
import OCP.GeomAbs
import OCP.Standard
import OCP.TColStd
import OCP.Adaptor2d
__all__  = [
"BRepAdaptor_Array1OfCurve",
"BRepAdaptor_CompCurve",
"BRepAdaptor_Curve",
"BRepAdaptor_Curve2d",
"BRepAdaptor_HArray1OfCurve",
"BRepAdaptor_Surface"
]
class BRepAdaptor_Array1OfCurve():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : BRepAdaptor_Array1OfCurve) -> BRepAdaptor_Array1OfCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> BRepAdaptor_Curve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BRepAdaptor_Curve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BRepAdaptor_Curve: 
        """
        Variable value access
        """
    def First(self) -> BRepAdaptor_Curve: 
        """
        Returns first element
        """
    def Init(self,theValue : BRepAdaptor_Curve) -> None: 
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
    def Last(self) -> BRepAdaptor_Curve: 
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
    def Move(self,theOther : BRepAdaptor_Array1OfCurve) -> BRepAdaptor_Array1OfCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : BRepAdaptor_Curve) -> None: 
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
    def Value(self,theIndex : int) -> BRepAdaptor_Curve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : BRepAdaptor_Curve,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : BRepAdaptor_Array1OfCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepAdaptor_CompCurve(OCP.Adaptor3d.Adaptor3d_Curve, OCP.Standard.Standard_Transient):
    """
    The Curve from BRepAdaptor allows to use a Wire of the BRep topology like a 3D curve. Warning: With this class of curve, C0 and C1 continuities are not assumed. So be careful with some algorithm! Please note that BRepAdaptor_CompCurve cannot be periodic curve at all (even if it contains single periodic edge).The Curve from BRepAdaptor allows to use a Wire of the BRep topology like a 3D curve. Warning: With this class of curve, C0 and C1 continuities are not assumed. So be careful with some algorithm! Please note that BRepAdaptor_CompCurve cannot be periodic curve at all (even if it contains single periodic edge).
    """
    def BSpline(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierCurve: 
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
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
        """
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
    def Edge(self,U : float,E : OCP.TopoDS.TopoDS_Edge) -> Tuple[float]: 
        """
        returns an edge and one parameter on them corresponding to the parameter U.
        """
    def Ellipse(self) -> OCP.gp.gp_Elips: 
        """
        None
        """
    def FirstParameter(self) -> float: 
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
    def Hyperbola(self) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Initialize(self,W : OCP.TopoDS.TopoDS_Wire,KnotByCurvilinearAbcissa : bool) -> None: 
        """
        Sets the wire <W>.

        Sets wire <W> and trimmed parameter.
        """
    @overload
    def Initialize(self,W : OCP.TopoDS.TopoDS_Wire,KnotByCurvilinearAbcissa : bool,First : float,Last : float,Tol : float) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
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
    def IsRational(self) -> bool: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbKnots(self) -> int: 
        """
        None
        """
    def NbPoles(self) -> int: 
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
    def Resolution(self,R3d : float) -> float: 
        """
        returns the parametric resolution
        """
    def ShallowCopy(self) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        Shallow copy of adaptor
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,KnotByCurvilinearAbcissa : bool,First : float,Last : float,Tol : float) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,KnotByCurvilinearAbcissa : bool=False) -> None: ...
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
class BRepAdaptor_Curve(OCP.Adaptor3d.Adaptor3d_Curve, OCP.Standard.Standard_Transient):
    """
    The Curve from BRepAdaptor allows to use an Edge of the BRep topology like a 3D curve.The Curve from BRepAdaptor allows to use an Edge of the BRep topology like a 3D curve.
    """
    def BSpline(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        Warning: This will make a copy of the BSpline Curve since it applies to it myTsrf. Be careful when using this method.
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierCurve: 
        """
        Warning: This will make a copy of the Bezier Curve since it applies to it myTsrf. Be careful when using this method.
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def Curve(self) -> OCP.GeomAdaptor.GeomAdaptor_Curve: 
        """
        Returns the Curve of the edge.
        """
    def CurveOnSurface(self) -> OCP.Adaptor3d.Adaptor3d_CurveOnSurface: 
        """
        Returns the CurveOnSurface of the edge.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
        """
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
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge.
        """
    def Ellipse(self) -> OCP.gp.gp_Elips: 
        """
        None
        """
    def FirstParameter(self) -> float: 
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
    def Hyperbola(self) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Initialize(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Sets the Curve <me> to access the geometry of edge <E>.

        Sets the Curve <me> to access the geometry of edge <E>. The geometry will be computed using the parametric curve of <E> on the face <F>. An Error is raised if the edge does not have a pcurve on the face.
        """
    @overload
    def Initialize(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def Is3DCurve(self) -> bool: 
        """
        Returns True if the edge geometry is computed from a 3D curve.
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsCurveOnSurface(self) -> bool: 
        """
        Returns True if the edge geometry is computed from a pcurve on a surface.
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
    def IsRational(self) -> bool: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbKnots(self) -> int: 
        """
        None
        """
    def NbPoles(self) -> int: 
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
    def Reset(self) -> None: 
        """
        Reset currently loaded curve (undone Load()).
        """
    def Resolution(self,R3d : float) -> float: 
        """
        returns the parametric resolution
        """
    def ShallowCopy(self) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        Shallow copy of adaptor
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Tolerance(self) -> float: 
        """
        Returns the edge tolerance.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Trsf(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the coordinate system of the curve.
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve
        """
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
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
class BRepAdaptor_Curve2d(OCP.Geom2dAdaptor.Geom2dAdaptor_Curve, OCP.Adaptor2d.Adaptor2d_Curve2d, OCP.Standard.Standard_Transient):
    """
    The Curve2d from BRepAdaptor allows to use an Edge on a Face like a 2d curve. (curve in the parametric space).The Curve2d from BRepAdaptor allows to use an Edge on a Face like a 2d curve. (curve in the parametric space).
    """
    def BSpline(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def Curve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Computes the point of parameter U.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
        """
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
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge.
        """
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face.
        """
    def FirstParameter(self) -> float: 
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
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Initialize(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Initialize with the pcurve of <E> on <F>.
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
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
    def IsRational(self) -> bool: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    @overload
    def Load(self,theCurve : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        Standard_ConstructionError is raised if theUFirst>theULast
        """
    @overload
    def Load(self,theCurve : OCP.Geom2d.Geom2d_Curve,theUFirst : float,theULast : float) -> None: ...
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        If necessary, breaks the curve in intervals of continuity <S>. And returns the number of intervals.
        """
    def NbKnots(self) -> int: 
        """
        None
        """
    def NbPoles(self) -> int: 
        """
        None
        """
    def NbSamples(self) -> int: 
        """
        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    def Period(self) -> float: 
        """
        None
        """
    def Reset(self) -> None: 
        """
        Reset currently loaded curve (undone Load()).
        """
    def Resolution(self,Ruv : float) -> float: 
        """
        returns the parametric resolution
        """
    def ShallowCopy(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Shallow copy of adaptor
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
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
class BRepAdaptor_HArray1OfCurve(BRepAdaptor_Array1OfCurve, OCP.Standard.Standard_Transient):
    def Array1(self) -> BRepAdaptor_Array1OfCurve: 
        """
        None
        """
    def Assign(self,theOther : BRepAdaptor_Array1OfCurve) -> BRepAdaptor_Array1OfCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> BRepAdaptor_Array1OfCurve: 
        """
        None
        """
    def ChangeFirst(self) -> BRepAdaptor_Curve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BRepAdaptor_Curve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BRepAdaptor_Curve: 
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
    def First(self) -> BRepAdaptor_Curve: 
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
    def Init(self,theValue : BRepAdaptor_Curve) -> None: 
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
    def Last(self) -> BRepAdaptor_Curve: 
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
    def Move(self,theOther : BRepAdaptor_Array1OfCurve) -> BRepAdaptor_Array1OfCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : BRepAdaptor_Curve) -> None: 
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
    def Value(self,theIndex : int) -> BRepAdaptor_Curve: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : BRepAdaptor_Curve) -> None: ...
    @overload
    def __init__(self,theOther : BRepAdaptor_Array1OfCurve) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class BRepAdaptor_Surface(OCP.Adaptor3d.Adaptor3d_Surface, OCP.Standard.Standard_Transient):
    """
    The Surface from BRepAdaptor allows to use a Face of the BRep topology look like a 3D surface.The Surface from BRepAdaptor allows to use a Face of the BRep topology look like a 3D surface.
    """
    def AxeOfRevolution(self) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    def BSpline(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Warning : this will make a copy of the BSpline Surface since it applies to it the myTsrf transformation Be Careful when using this method
        """
    def BasisCurve(self) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        only for SurfaceOfExtrusion and SurfaceOfRevolution Warning: this will make a copy of the underlying curve since it applies to it the transformation myTrsf. Be careful when using this method.
        """
    def BasisSurface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierSurface: 
        """
        None
        """
    def ChangeSurface(self) -> OCP.GeomAdaptor.GeomAdaptor_Surface: 
        """
        Returns the surface.
        """
    def Cone(self) -> OCP.gp.gp_Cone: 
        """
        None
        """
    def Cylinder(self) -> OCP.gp.gp_Cylinder: 
        """
        None
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameters U,V on the surface.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point and the first derivatives on the surface. Raised if the continuity of the current intervals is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first and second derivatives on the surface. Raised if the continuity of the current intervals is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first, second and third derivatives on the surface. Raised if the continuity of the current intervals is not C3.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V). Raised if the current U interval is not not CNu and the current V interval is not CNv. Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the face.
        """
    def FirstUParameter(self) -> float: 
        """
        None
        """
    def FirstVParameter(self) -> float: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_SurfaceType: 
        """
        Returns the type of the surface : Plane, Cylinder, Cone, Sphere, Torus, BezierSurface, BSplineSurface, SurfaceOfRevolution, SurfaceOfExtrusion, OtherSurface
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Initialize(self,F : OCP.TopoDS.TopoDS_Face,Restriction : bool=True) -> None: 
        """
        Sets the surface to the geometry of <F>.
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
    def IsUClosed(self) -> bool: 
        """
        None
        """
    def IsUPeriodic(self) -> bool: 
        """
        None
        """
    def IsURational(self) -> bool: 
        """
        None
        """
    def IsVClosed(self) -> bool: 
        """
        None
        """
    def IsVPeriodic(self) -> bool: 
        """
        None
        """
    def IsVRational(self) -> bool: 
        """
        None
        """
    def LastUParameter(self) -> float: 
        """
        None
        """
    def LastVParameter(self) -> float: 
        """
        None
        """
    def NbUIntervals(self,theSh : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        If necessary, breaks the surface in U intervals of continuity <S>. And returns the number of intervals.
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVIntervals(self,theSh : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        If necessary, breaks the surface in V intervals of continuity <S>. And returns the number of intervals.
        """
    def NbVKnots(self) -> int: 
        """
        None
        """
    def NbVPoles(self) -> int: 
        """
        None
        """
    def OffsetValue(self) -> float: 
        """
        None
        """
    def Plane(self) -> OCP.gp.gp_Pln: 
        """
        None
        """
    def ShallowCopy(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Shallow copy of adaptor
        """
    def Sphere(self) -> OCP.gp.gp_Sphere: 
        """
        None
        """
    def Surface(self) -> OCP.GeomAdaptor.GeomAdaptor_Surface: 
        """
        Returns the surface.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Tolerance(self) -> float: 
        """
        Returns the face tolerance.
        """
    def Torus(self) -> OCP.gp.gp_Torus: 
        """
        None
        """
    def Trsf(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the surface coordinate system.
        """
    def UContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UIntervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Returns the intervals with the requested continuity in the U direction.
        """
    def UPeriod(self) -> float: 
        """
        None
        """
    def UResolution(self,theR3d : float) -> float: 
        """
        Returns the parametric U resolution corresponding to the real space resolution <R3d>.
        """
    def UTrim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns a surface trimmed in the U direction equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def VContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    def VIntervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Returns the intervals with the requested continuity in the V direction.
        """
    def VPeriod(self) -> float: 
        """
        None
        """
    def VResolution(self,theR3d : float) -> float: 
        """
        Returns the parametric V resolution corresponding to the real space resolution <R3d>.
        """
    def VTrim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns a surface trimmed in the V direction between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameters U,V on the surface. Tip: use GeomLib::NormEstim() to calculate surface normal at specified (U, V) point.
        """
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,R : bool=True) -> None: ...
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
