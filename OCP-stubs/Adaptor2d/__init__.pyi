import OCP.Adaptor2d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.GeomAbs
import OCP.TColStd
import OCP.Geom2d
import OCP.Standard
import OCP.gp
__all__  = [
"Adaptor2d_Curve2d",
"Adaptor2d_HCurve2d",
"Adaptor2d_HLine2d",
"Adaptor2d_HOffsetCurve",
"Adaptor2d_Line2d",
"Adaptor2d_OffsetCurve"
]
class Adaptor2d_Curve2d():
    """
    Root class for 2D curves on which geometric algorithms work. An adapted curve is an interface between the services provided by a curve, and those required of the curve by algorithms, which use it. A derived concrete class is provided: Geom2dAdaptor_Curve for a curve from the Geom2d package.
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
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Computes the point of parameter U on the curve.
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
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
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
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
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
    def Resolution(self,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> Adaptor2d_HCurve2d: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self) -> None: ...
    pass
class Adaptor2d_HCurve2d(OCP.Standard.Standard_Transient):
    """
    Root class for 2D curves manipulated by handles, on which geometric algorithms work. An adapted curve is an interface between the services provided by a curve, and those required of the curve by algorithms, which use it. A derived specific class is provided: Geom2dAdaptor_HCurve for a curve from the Geom2d package.Root class for 2D curves manipulated by handles, on which geometric algorithms work. An adapted curve is an interface between the services provided by a curve, and those required of the curve by algorithms, which use it. A derived specific class is provided: Geom2dAdaptor_HCurve for a curve from the Geom2d package.Root class for 2D curves manipulated by handles, on which geometric algorithms work. An adapted curve is an interface between the services provided by a curve, and those required of the curve by algorithms, which use it. A derived specific class is provided: Geom2dAdaptor_HCurve for a curve from the Geom2d package.
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
    def Curve2d(self) -> Adaptor2d_Curve2d: 
        """
        Returns a reference to the Curve2d inside the HCurve2d.
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> Adaptor2d_HCurve2d: 
        """
        If <First> >= <Last>

        If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
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
class Adaptor2d_HLine2d(Adaptor2d_HCurve2d, OCP.Standard.Standard_Transient):
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
    def ChangeCurve2d(self) -> Adaptor2d_Line2d: 
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
    def Curve2d(self) -> Adaptor2d_Curve2d: 
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
    def Set(self,C : Adaptor2d_Line2d) -> None: 
        """
        Sets the field of the GenHCurve2d.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> Adaptor2d_HCurve2d: 
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
    def __init__(self,C : Adaptor2d_Line2d) -> None: ...
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
class Adaptor2d_HOffsetCurve(Adaptor2d_HCurve2d, OCP.Standard.Standard_Transient):
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
    def ChangeCurve2d(self) -> Adaptor2d_OffsetCurve: 
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
    def Curve2d(self) -> Adaptor2d_Curve2d: 
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
    def Set(self,C : Adaptor2d_OffsetCurve) -> None: 
        """
        Sets the field of the GenHCurve2d.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> Adaptor2d_HCurve2d: 
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
    def __init__(self,C : Adaptor2d_OffsetCurve) -> None: ...
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
class Adaptor2d_Line2d(Adaptor2d_Curve2d):
    """
    Use by the TopolTool to trim a surface.
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
    def D0(self,X : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    def D1(self,X : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def D2(self,X : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def D3(self,X : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        None
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
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
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
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    @overload
    def Load(self,L : OCP.gp.gp_Lin2d) -> None: 
        """
        None

        None
        """
    @overload
    def Load(self,L : OCP.gp.gp_Lin2d,UFirst : float,ULast : float) -> None: ...
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
    def Resolution(self,R3d : float) -> float: 
        """
        None
        """
    def Trim(self,First : float,Last : float,Tol : float) -> Adaptor2d_HCurve2d: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,X : float) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,D : OCP.gp.gp_Dir2d,UFirst : float,ULast : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Adaptor2d_OffsetCurve(Adaptor2d_Curve2d):
    """
    Defines an Offset curve (algorithmic 2d curve).
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
    def Curve(self) -> Adaptor2d_HCurve2d: 
        """
        None

        None
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Computes the point of parameter U on the curve.
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
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
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
    def Load(self,Offset : float) -> None: 
        """
        Changes the curve. The Offset is reset to 0.

        Changes the Offset on the current Curve.

        Changes the Offset Curve on the current Curve.
        """
    @overload
    def Load(self,Offset : float,WFirst : float,WLast : float) -> None: ...
    @overload
    def Load(self,S : Adaptor2d_HCurve2d) -> None: ...
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
    def Offset(self) -> float: 
        """
        None

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
    def Resolution(self,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> Adaptor2d_HCurve2d: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : Adaptor2d_HCurve2d) -> None: ...
    @overload
    def __init__(self,C : Adaptor2d_HCurve2d,Offset : float) -> None: ...
    @overload
    def __init__(self,C : Adaptor2d_HCurve2d,Offset : float,WFirst : float,WLast : float) -> None: ...
    pass
