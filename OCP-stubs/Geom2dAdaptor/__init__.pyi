import OCP.Geom2dAdaptor
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor2d
import OCP.Geom2d
import OCP.Standard
import OCP.gp
import OCP.TColStd
import OCP.GeomAbs
__all__  = [
"Geom2dAdaptor",
"Geom2dAdaptor_Curve",
"Geom2dAdaptor_GHCurve",
"Geom2dAdaptor_HCurve"
]
class Geom2dAdaptor():
    """
    this package contains the geometric definition of 2d curves compatible with the Adaptor package templates.
    """
    @staticmethod
    def MakeCurve_s(HC : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Inherited from GHCurve. Provides a curve handled by reference. Creates a 2d curve from a HCurve2d. This cannot process the OtherCurves.
        """
    def __init__(self) -> None: ...
    pass
class Geom2dAdaptor_Curve(OCP.Adaptor2d.Adaptor2d_Curve2d):
    """
    An interface between the services provided by any curve from the package Geom2d and those required of the curve by algorithms which use it.
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
    def Degree(self) -> int: 
        """
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
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        None

        None
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        None
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
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
    def LastParameter(self) -> float: 
        """
        None

        None
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    @overload
    def Load(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        ConstructionError is raised if Ufirst>Ulast

        None

        ConstructionError is raised if Ufirst>Ulast
        """
    @overload
    def Load(self,C : OCP.Geom2d.Geom2d_Curve,UFirst : float,ULast : float) -> None: ...
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
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
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
    def __init__(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Curve,UFirst : float,ULast : float) -> None: ...
    pass
class Geom2dAdaptor_GHCurve(OCP.Adaptor2d.Adaptor2d_HCurve2d, OCP.Standard.Standard_Transient):
    def BSpline(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None

        None
        """
    def Bezier(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None

        None
        """
    def ChangeCurve2d(self) -> Geom2dAdaptor_Curve: 
        """
        Returns the curve used to create the GenHCurve.
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        None

        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    def Curve2d(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Returns the curve used to create the GenHCurve2d. This is redefined from HCurve2d, cannot be inline.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec2d: 
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
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        None

        None
        """
    def FirstParameter(self) -> float: 
        """
        None

        None
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
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
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
        None

        None
        """
    def IsClosed(self) -> bool: 
        """
        None

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
    def Line(self) -> OCP.gp.gp_Lin2d: 
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
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
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
    def Set(self,C : Geom2dAdaptor_Curve) -> None: 
        """
        Sets the field of the GenHCurve2d.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        If <First> >= <Last>

        If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : Geom2dAdaptor_Curve) -> None: ...
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
class Geom2dAdaptor_HCurve(Geom2dAdaptor_GHCurve, OCP.Adaptor2d.Adaptor2d_HCurve2d, OCP.Standard.Standard_Transient):
    """
    Provides an interface between the services provided by any curve from the package Geom2d and those required of the curve by algorithms, which use it.Provides an interface between the services provided by any curve from the package Geom2d and those required of the curve by algorithms, which use it.Provides an interface between the services provided by any curve from the package Geom2d and those required of the curve by algorithms, which use it.
    """
    def BSpline(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None

        None
        """
    def Bezier(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None

        None
        """
    def ChangeCurve2d(self) -> Geom2dAdaptor_Curve: 
        """
        Returns the curve used to create the GenHCurve.
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        None

        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    def Curve2d(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Returns the curve used to create the GenHCurve2d. This is redefined from HCurve2d, cannot be inline.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec2d: 
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
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        None

        None
        """
    def FirstParameter(self) -> float: 
        """
        None

        None
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
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
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
        None

        None
        """
    def IsClosed(self) -> bool: 
        """
        None

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
    def Line(self) -> OCP.gp.gp_Lin2d: 
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
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
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
    def Set(self,C : Geom2dAdaptor_Curve) -> None: 
        """
        Sets the field of the GenHCurve2d.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        If <First> >= <Last>

        If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
        """
    @overload
    def __init__(self,S : OCP.Geom2d.Geom2d_Curve,UFirst : float,ULast : float) -> None: ...
    @overload
    def __init__(self,AS : Geom2dAdaptor_Curve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.Geom2d.Geom2d_Curve) -> None: ...
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
