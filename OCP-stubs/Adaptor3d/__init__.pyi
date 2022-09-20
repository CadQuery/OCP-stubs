import OCP.Adaptor3d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor2d
import OCP.GeomAbs
import OCP.math
import OCP.gp
import OCP.Geom
import OCP.Standard
import OCP.TopAbs
import OCP.TColStd
__all__  = [
"Adaptor3d_Curve",
"Adaptor3d_CurveOnSurface",
"Adaptor3d_HSurfaceTool",
"Adaptor3d_HVertex",
"Adaptor3d_InterFunc",
"Adaptor3d_IsoCurve",
"Adaptor3d_Surface",
"Adaptor3d_TopolTool"
]
class Adaptor3d_Curve(OCP.Standard.Standard_Transient):
    """
    Root class for 3D curves on which geometric algorithms work. An adapted curve is an interface between the services provided by a curve and those required of the curve by algorithms which use it. Two derived concrete classes are provided: - GeomAdaptor_Curve for a curve from the Geom package - Adaptor3d_CurveOnSurface for a curve lying on a surface from the Geom package.Root class for 3D curves on which geometric algorithms work. An adapted curve is an interface between the services provided by a curve and those required of the curve by algorithms which use it. Two derived concrete classes are provided: - GeomAdaptor_Curve for a curve from the Geom package - Adaptor3d_CurveOnSurface for a curve lying on a surface from the Geom package.Root class for 3D curves on which geometric algorithms work. An adapted curve is an interface between the services provided by a curve and those required of the curve by algorithms which use it. Two derived concrete classes are provided: - GeomAdaptor_Curve for a curve from the Geom package - Adaptor3d_CurveOnSurface for a curve lying on a surface from the Geom package.
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
        Computes the point of parameter U on the curve.
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
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    def ShallowCopy(self) -> Adaptor3d_Curve: 
        """
        Shallow copy of adaptor
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> Adaptor3d_Curve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve.
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
class Adaptor3d_CurveOnSurface(Adaptor3d_Curve, OCP.Standard.Standard_Transient):
    """
    An interface between the services provided by a curve lying on a surface from the package Geom and those required of the curve by algorithms which use it. The curve is defined as a 2D curve from the Geom2d package, in the parametric space of the surface.An interface between the services provided by a curve lying on a surface from the package Geom and those required of the curve by algorithms which use it. The curve is defined as a 2D curve from the Geom2d package, in the parametric space of the surface.
    """
    def BSpline(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierCurve: 
        """
        None
        """
    def ChangeCurve(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        None
        """
    def ChangeSurface(self) -> Adaptor3d_Surface: 
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
        Computes the point of parameter U on the curve.
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
    def Ellipse(self) -> OCP.gp.gp_Elips: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        None
        """
    def GetCurve(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSurface(self) -> Adaptor3d_Surface: 
        """
        None
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
    @overload
    def Load(self,S : Adaptor3d_Surface) -> None: 
        """
        Changes the surface.

        Changes the 2d curve.

        Load both curve and surface.
        """
    @overload
    def Load(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def Load(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,S : Adaptor3d_Surface) -> None: ...
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
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    def ShallowCopy(self) -> Adaptor3d_Curve: 
        """
        Shallow copy of adaptor
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> Adaptor3d_Curve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve.
        """
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,S : Adaptor3d_Surface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : Adaptor3d_Surface) -> None: ...
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
class Adaptor3d_HSurfaceTool():
    """
    None
    """
    @staticmethod
    def AxeOfRevolution_s(theSurf : Adaptor3d_Surface) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    @staticmethod
    def BSpline_s(theSurf : Adaptor3d_Surface) -> OCP.Geom.Geom_BSplineSurface: 
        """
        None
        """
    @staticmethod
    def BasisCurve_s(theSurf : Adaptor3d_Surface) -> Adaptor3d_Curve: 
        """
        None
        """
    @staticmethod
    def BasisSurface_s(theSurf : Adaptor3d_Surface) -> Adaptor3d_Surface: 
        """
        None
        """
    @staticmethod
    def Bezier_s(theSurf : Adaptor3d_Surface) -> OCP.Geom.Geom_BezierSurface: 
        """
        None
        """
    @staticmethod
    def Cone_s(theSurf : Adaptor3d_Surface) -> OCP.gp.gp_Cone: 
        """
        None
        """
    @staticmethod
    def Cylinder_s(theSurf : Adaptor3d_Surface) -> OCP.gp.gp_Cylinder: 
        """
        None
        """
    @staticmethod
    def D0_s(theSurf : Adaptor3d_Surface,theU : float,theV : float,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def D1_s(theSurf : Adaptor3d_Surface,theU : float,theV : float,thePnt : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D2_s(theSurf : Adaptor3d_Surface,theU : float,theV : float,thePnt : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D3_s(theSurf : Adaptor3d_Surface,theU : float,theV : float,thePnt : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec,theD3U : OCP.gp.gp_Vec,theD3V : OCP.gp.gp_Vec,theD3UUV : OCP.gp.gp_Vec,theD3UVV : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def DN_s(theSurf : Adaptor3d_Surface,theU : float,theV : float,theNU : int,theNV : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def Direction_s(theSurf : Adaptor3d_Surface) -> OCP.gp.gp_Dir: 
        """
        None
        """
    @staticmethod
    def FirstUParameter_s(theSurf : Adaptor3d_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def FirstVParameter_s(theSurf : Adaptor3d_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(theSurf : Adaptor3d_Surface) -> OCP.GeomAbs.GeomAbs_SurfaceType: 
        """
        None
        """
    @staticmethod
    def IsUClosed_s(theSurf : Adaptor3d_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def IsUPeriodic_s(theSurf : Adaptor3d_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def IsVClosed_s(theSurf : Adaptor3d_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def IsVPeriodic_s(theSurf : Adaptor3d_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def LastUParameter_s(theSurf : Adaptor3d_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def LastVParameter_s(theSurf : Adaptor3d_Surface) -> float: 
        """
        None
        """
    @staticmethod
    @overload
    def NbSamplesU_s(S : Adaptor3d_Surface) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbSamplesU_s(S : Adaptor3d_Surface,u1 : float,u2 : float) -> int: ...
    @staticmethod
    @overload
    def NbSamplesV_s(arg0 : Adaptor3d_Surface,v1 : float,v2 : float) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbSamplesV_s(S : Adaptor3d_Surface) -> int: ...
    @staticmethod
    def NbUIntervals_s(theSurf : Adaptor3d_Surface,theSh : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        None
        """
    @staticmethod
    def NbVIntervals_s(theSurf : Adaptor3d_Surface,theSh : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        None
        """
    @staticmethod
    def OffsetValue_s(theSurf : Adaptor3d_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def Plane_s(theSurf : Adaptor3d_Surface) -> OCP.gp.gp_Pln: 
        """
        None
        """
    @staticmethod
    def Sphere_s(theSurf : Adaptor3d_Surface) -> OCP.gp.gp_Sphere: 
        """
        None
        """
    @staticmethod
    def Torus_s(theSurf : Adaptor3d_Surface) -> OCP.gp.gp_Torus: 
        """
        None
        """
    @staticmethod
    def UIntervals_s(theSurf : Adaptor3d_Surface,theTab : OCP.TColStd.TColStd_Array1OfReal,theSh : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def UPeriod_s(theSurf : Adaptor3d_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def UResolution_s(theSurf : Adaptor3d_Surface,theR3d : float) -> float: 
        """
        None
        """
    @staticmethod
    def UTrim_s(theSurf : Adaptor3d_Surface,theFirst : float,theLast : float,theTol : float) -> Adaptor3d_Surface: 
        """
        If <First> >= <Last>
        """
    @staticmethod
    def VIntervals_s(theSurf : Adaptor3d_Surface,theTab : OCP.TColStd.TColStd_Array1OfReal,theSh : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def VPeriod_s(theSurf : Adaptor3d_Surface) -> float: 
        """
        None
        """
    @staticmethod
    def VResolution_s(theSurf : Adaptor3d_Surface,theR3d : float) -> float: 
        """
        None
        """
    @staticmethod
    def VTrim_s(theSurf : Adaptor3d_Surface,theFirst : float,theLast : float,theTol : float) -> Adaptor3d_Surface: 
        """
        If <First> >= <Last>
        """
    @staticmethod
    def Value_s(theSurf : Adaptor3d_Surface,theU : float,theV : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Adaptor3d_HVertex(OCP.Standard.Standard_Transient):
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
    def IsSame(self,Other : Adaptor3d_HVertex) -> bool: 
        """
        None
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Parameter(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    def Resolution(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        Parametric resolution (2d).
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,Ori : OCP.TopAbs.TopAbs_Orientation,Resolution : float) -> None: ...
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
class Adaptor3d_InterFunc(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    Used to find the points U(t) = U0 or V(t) = V0 in order to determine the Cn discontinuities of an Adpator_CurveOnSurface relatively to the discontinuities of the surface. Used to find the roots of the functions
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        computes the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        computes the value <F>of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        computes the value <F> and the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,FixVal : float,Fix : int) -> None: ...
    pass
class Adaptor3d_IsoCurve(Adaptor3d_Curve, OCP.Standard.Standard_Transient):
    """
    Defines an isoparametric curve on a surface. The type of isoparametric curve (U or V) is defined with the enumeration IsoType from GeomAbs if NoneIso is given an error is raised.Defines an isoparametric curve on a surface. The type of isoparametric curve (U or V) is defined with the enumeration IsoType from GeomAbs if NoneIso is given an error is raised.
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
        Computes the point of parameter U on the curve.
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
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def IsRational(self) -> bool: 
        """
        None
        """
    def Iso(self) -> OCP.GeomAbs.GeomAbs_IsoType: 
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
    @overload
    def Load(self,Iso : OCP.GeomAbs.GeomAbs_IsoType,Param : float) -> None: 
        """
        Changes the surface. The iso is reset to NoneIso.

        Changes the iso on the current surface.

        Changes the iso on the current surface.
        """
    @overload
    def Load(self,S : Adaptor3d_Surface) -> None: ...
    @overload
    def Load(self,Iso : OCP.GeomAbs.GeomAbs_IsoType,Param : float,WFirst : float,WLast : float) -> None: ...
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
    def Parameter(self) -> float: 
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
    def ShallowCopy(self) -> Adaptor3d_Curve: 
        """
        Shallow copy of adaptor
        """
    def Surface(self) -> Adaptor3d_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> Adaptor3d_Curve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve.
        """
    @overload
    def __init__(self,S : Adaptor3d_Surface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : Adaptor3d_Surface,Iso : OCP.GeomAbs.GeomAbs_IsoType,Param : float,WFirst : float,WLast : float) -> None: ...
    @overload
    def __init__(self,S : Adaptor3d_Surface,Iso : OCP.GeomAbs.GeomAbs_IsoType,Param : float) -> None: ...
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
class Adaptor3d_Surface(OCP.Standard.Standard_Transient):
    """
    Root class for surfaces on which geometric algorithms work. An adapted surface is an interface between the services provided by a surface and those required of the surface by algorithms which use it. A derived concrete class is provided: GeomAdaptor_Surface for a surface from the Geom package. The Surface class describes the standard behaviour of a surface for generic algorithms.Root class for surfaces on which geometric algorithms work. An adapted surface is an interface between the services provided by a surface and those required of the surface by algorithms which use it. A derived concrete class is provided: GeomAdaptor_Surface for a surface from the Geom package. The Surface class describes the standard behaviour of a surface for generic algorithms.Root class for surfaces on which geometric algorithms work. An adapted surface is an interface between the services provided by a surface and those required of the surface by algorithms which use it. A derived concrete class is provided: GeomAdaptor_Surface for a surface from the Geom package. The Surface class describes the standard behaviour of a surface for generic algorithms.
    """
    def AxeOfRevolution(self) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    def BSpline(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        None
        """
    def BasisCurve(self) -> Adaptor3d_Curve: 
        """
        None
        """
    def BasisSurface(self) -> Adaptor3d_Surface: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierSurface: 
        """
        None
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
    def NbUIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of U intervals for continuity <S>. May be one if UContinuity(me) >= <S>
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of V intervals for continuity <S>. May be one if VContinuity(me) >= <S>
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
    def ShallowCopy(self) -> Adaptor3d_Surface: 
        """
        Shallow copy of adaptor
        """
    def Sphere(self) -> OCP.gp.gp_Sphere: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Torus(self) -> OCP.gp.gp_Torus: 
        """
        None
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
    def UResolution(self,R3d : float) -> float: 
        """
        Returns the parametric U resolution corresponding to the real space resolution <R3d>.
        """
    def UTrim(self,First : float,Last : float,Tol : float) -> Adaptor3d_Surface: 
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
    def VResolution(self,R3d : float) -> float: 
        """
        Returns the parametric V resolution corresponding to the real space resolution <R3d>.
        """
    def VTrim(self,First : float,Last : float,Tol : float) -> Adaptor3d_Surface: 
        """
        Returns a surface trimmed in the V direction between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameters U,V on the surface.
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
class Adaptor3d_TopolTool(OCP.Standard.Standard_Transient):
    """
    This class provides a default topological tool, based on the Umin,Vmin,Umax,Vmax of an HSurface from Adaptor3d. All methods and fields may be redefined when inheriting from this class. This class is used to instantiate algorithms as Intersection, outlines,...This class provides a default topological tool, based on the Umin,Vmin,Umax,Vmax of an HSurface from Adaptor3d. All methods and fields may be redefined when inheriting from this class. This class is used to instantiate algorithms as Intersection, outlines,...
    """
    def BSplSamplePnts(self,theDefl : float,theNUmin : int,theNVmin : int) -> None: 
        """
        Compute the sample-points for the intersections algorithms by adaptive algorithm for BSpline surfaces - is used in SamplePnts
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
    def Identical(self,V1 : Adaptor3d_HVertex,V2 : Adaptor3d_HVertex) -> bool: 
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
    def Initialize(self) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Initialize(self,S : Adaptor3d_Surface) -> None: ...
    @overload
    def Initialize(self,Curve : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
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
        compute the sample-points for the intersections algorithms
        """
    def NbSamplesU(self) -> int: 
        """
        compute the sample-points for the intersections algorithms
        """
    def NbSamplesV(self) -> int: 
        """
        compute the sample-points for the intersections algorithms
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
    def Orientation(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        If the function returns the orientation of the arc. If the orientation is FORWARD or REVERSED, the arc is a "real" limit of the surface. If the orientation is INTERNAL or EXTERNAL, the arc is considered as an arc on the surface.

        Returns the orientation of the vertex V. The vertex has been found with an exploration on a given arc. The orientation is the orientation of the vertex on this arc.
        """
    @overload
    def Orientation(self,V : Adaptor3d_HVertex) -> OCP.TopAbs.TopAbs_Orientation: ...
    def Pnt(self,V : Adaptor3d_HVertex) -> OCP.gp.gp_Pnt: 
        """
        returns 3d point of the vertex V
        """
    def SamplePnts(self,theDefl : float,theNUmin : int,theNVmin : int) -> None: 
        """
        Compute the sample-points for the intersections algorithms by adaptive algorithm for BSpline surfaces. For other surfaces algorithm is the same as in method ComputeSamplePoints(), but only fill arrays of U and V sample parameters;
        """
    def SamplePoint(self,Index : int,P2d : OCP.gp.gp_Pnt2d,P3d : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tol3d(self,V : Adaptor3d_HVertex) -> float: 
        """
        returns 3d tolerance of the arc C

        returns 3d tolerance of the vertex V
        """
    @overload
    def Tol3d(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: ...
    def UParameters(self,theArray : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        return the set of U parameters on the surface obtained by the method SamplePnts
        """
    def VParameters(self,theArray : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        return the set of V parameters on the surface obtained by the method SamplePnts
        """
    def Value(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        None
        """
    def Vertex(self) -> Adaptor3d_HVertex: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Surface : Adaptor3d_Surface) -> None: ...
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
