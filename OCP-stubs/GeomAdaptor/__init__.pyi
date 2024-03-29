import OCP.GeomAdaptor
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.Adaptor3d
import OCP.gp
import OCP.GeomAbs
import OCP.Standard
import OCP.TColStd
__all__  = [
"GeomAdaptor",
"GeomAdaptor_Curve",
"GeomAdaptor_Surface",
"GeomAdaptor_SurfaceOfLinearExtrusion",
"GeomAdaptor_SurfaceOfRevolution"
]
class GeomAdaptor():
    """
    this package contains the geometric definition of curve and surface necessary to use algorithms.
    """
    @staticmethod
    def MakeCurve_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.Geom.Geom_Curve: 
        """
        Inherited from GHCurve. Provides a curve handled by reference. Build a Geom_Curve using the information from the Curve from Adaptor3d
        """
    @staticmethod
    def MakeSurface_s(theS : OCP.Adaptor3d.Adaptor3d_Surface,theTrimFlag : bool=True) -> OCP.Geom.Geom_Surface: 
        """
        Build a Geom_Surface using the information from the Surface from Adaptor3d
        """
    def __init__(self) -> None: ...
    pass
class GeomAdaptor_Curve(OCP.Adaptor3d.Adaptor3d_Curve, OCP.Standard.Standard_Transient):
    """
    This class provides an interface between the services provided by any curve from the package Geom and those required of the curve by algorithms which use it. Creation of the loaded curve the curve is C1 by piece.This class provides an interface between the services provided by any curve from the package Geom and those required of the curve by algorithms which use it. Creation of the loaded curve the curve is C1 by piece.
    """
    def BSpline(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        this will NOT make a copy of the BSpline Curve : If you want to modify the Curve please make a copy yourself Also it will NOT trim the surface to myFirst/Last.
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierCurve: 
        """
        this will NOT make a copy of the Bezier Curve : If you want to modify the Curve please make a copy yourself Also it will NOT trim the surface to myFirst/Last.
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def Curve(self) -> OCP.Geom.Geom_Curve: 
        """
        Provides a curve inherited from Hcurve from Adaptor. This is inherited to provide easy to use constructors.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Warning : On the specific case of BSplineCurve: if the curve is cut in interval of continuity CN, the derivatives are computed on the current interval. else the derivatives are computed on the basis curve. Raised if N < 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
        """
        this should NEVER make a copy of the underlying curve to read the relevant information
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
        this should NEVER make a copy of the underlying curve to read the relevant information
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
    def Load(self,theCurve : OCP.Geom.Geom_Curve,theUFirst : float,theULast : float) -> None: 
        """
        None

        Standard_ConstructionError is raised if theUFirst>theULast
        """
    @overload
    def Load(self,theCurve : OCP.Geom.Geom_Curve) -> None: ...
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbKnots(self) -> int: 
        """
        this should NEVER make a copy of the underlying curve to read the relevant information
        """
    def NbPoles(self) -> int: 
        """
        this should NEVER make a copy of the underlying curve to read the relevant information
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
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCurve : OCP.Geom.Geom_Curve,theUFirst : float,theULast : float) -> None: ...
    @overload
    def __init__(self,theCurve : OCP.Geom.Geom_Curve) -> None: ...
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
class GeomAdaptor_Surface(OCP.Adaptor3d.Adaptor3d_Surface, OCP.Standard.Standard_Transient):
    """
    An interface between the services provided by any surface from the package Geom and those required of the surface by algorithms which use it. Creation of the loaded surface the surface is C1 by pieceAn interface between the services provided by any surface from the package Geom and those required of the surface by algorithms which use it. Creation of the loaded surface the surface is C1 by piece
    """
    def AxeOfRevolution(self) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    def BSpline(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        This will NOT make a copy of the BSpline Surface : If you want to modify the Surface please make a copy yourself Also it will NOT trim the surface to myU/VFirst/Last.
        """
    def BasisCurve(self) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        None
        """
    def BasisSurface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierSurface: 
        """
        This will NOT make a copy of the Bezier Surface : If you want to modify the Surface please make a copy yourself Also it will NOT trim the surface to myU/VFirst/Last.
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
        Computes the point and the first derivatives on the surface.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first and second derivatives on the surface.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first, second and third derivatives on the surface.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V).
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
    @overload
    def Load(self,theSurf : OCP.Geom.Geom_Surface) -> None: 
        """
        None

        Standard_ConstructionError is raised if theUFirst>theULast or theVFirst>theVLast
        """
    @overload
    def Load(self,theSurf : OCP.Geom.Geom_Surface,theUFirst : float,theULast : float,theVFirst : float,theVLast : float,theTolU : float=0.0,theTolV : float=0.0) -> None: ...
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
    def ShallowCopy(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Shallow copy of adaptor
        """
    def Sphere(self) -> OCP.gp.gp_Sphere: 
        """
        None
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
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
    def VResolution(self,R3d : float) -> float: 
        """
        Returns the parametric V resolution corresponding to the real space resolution <R3d>.
        """
    def VTrim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns a surface trimmed in the V direction between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameters U,V on the surface.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theSurf : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def __init__(self,theSurf : OCP.Geom.Geom_Surface,theUFirst : float,theULast : float,theVFirst : float,theVLast : float,theTolU : float=0.0,theTolV : float=0.0) -> None: ...
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
class GeomAdaptor_SurfaceOfLinearExtrusion(GeomAdaptor_Surface, OCP.Adaptor3d.Adaptor3d_Surface, OCP.Standard.Standard_Transient):
    """
    Generalised cylinder. This surface is obtained by sweeping a curve in a given direction. The parametrization range for the parameter U is defined with referenced the curve. The parametrization range for the parameter V is ]-infinite,+infinite[ The position of the curve gives the origin for the parameter V. The continuity of the surface is CN in the V direction.Generalised cylinder. This surface is obtained by sweeping a curve in a given direction. The parametrization range for the parameter U is defined with referenced the curve. The parametrization range for the parameter V is ]-infinite,+infinite[ The position of the curve gives the origin for the parameter V. The continuity of the surface is CN in the V direction.
    """
    def AxeOfRevolution(self) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    def BSpline(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        None
        """
    def BasisCurve(self) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        None
        """
    def BasisSurface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
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
        Computes the point and the first derivatives on the surface.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first and second derivatives on the surface.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first, second and third derivatives on the surface.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V).
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
    @overload
    def Load(self,V : OCP.gp.gp_Dir) -> None: 
        """
        Changes the Curve

        Changes the Direction
        """
    @overload
    def Load(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
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
    def ShallowCopy(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Shallow copy of adaptor
        """
    def Sphere(self) -> OCP.gp.gp_Sphere: 
        """
        None
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
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
    def UTrim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns a surface trimmed in the U direction equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def VContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Return CN.
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
    def VTrim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns a surface trimmed in the V direction between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameters U,V on the surface.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,V : OCP.gp.gp_Dir) -> None: ...
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
class GeomAdaptor_SurfaceOfRevolution(GeomAdaptor_Surface, OCP.Adaptor3d.Adaptor3d_Surface, OCP.Standard.Standard_Transient):
    """
    This class defines a complete surface of revolution. The surface is obtained by rotating a curve a complete revolution about an axis. The curve and the axis must be in the same plane. If the curve and the axis are not in the same plane it is always possible to be in the previous case after a cylindrical projection of the curve in a referenced plane. For a complete surface of revolution the parametric range is 0 <= U <= 2*PI. -- The parametric range for V is defined with the revolved curve. The origin of the U parametrization is given by the position of the revolved curve (reference). The direction of the revolution axis defines the positive sense of rotation (trigonometric sense) corresponding to the increasing of the parametric value U. The derivatives are always defined for the u direction. For the v direction the definition of the derivatives depends on the degree of continuity of the referenced curve.This class defines a complete surface of revolution. The surface is obtained by rotating a curve a complete revolution about an axis. The curve and the axis must be in the same plane. If the curve and the axis are not in the same plane it is always possible to be in the previous case after a cylindrical projection of the curve in a referenced plane. For a complete surface of revolution the parametric range is 0 <= U <= 2*PI. -- The parametric range for V is defined with the revolved curve. The origin of the U parametrization is given by the position of the revolved curve (reference). The direction of the revolution axis defines the positive sense of rotation (trigonometric sense) corresponding to the increasing of the parametric value U. The derivatives are always defined for the u direction. For the v direction the definition of the derivatives depends on the degree of continuity of the referenced curve.
    """
    def AxeOfRevolution(self) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    def Axis(self) -> OCP.gp.gp_Ax3: 
        """
        None
        """
    def BSpline(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        None
        """
    def BasisCurve(self) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        None
        """
    def BasisSurface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierSurface: 
        """
        None
        """
    def Cone(self) -> OCP.gp.gp_Cone: 
        """
        Apex of the Cone = Cone.Position().Location() ==> ReferenceRadius = 0.
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
        Computes the point and the first derivatives on the surface.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first and second derivatives on the surface.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point, the first, second and third derivatives on the surface.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V).
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
    @overload
    def Load(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: 
        """
        Changes the Curve

        Changes the Direction
        """
    @overload
    def Load(self,V : OCP.gp.gp_Ax1) -> None: ...
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
    def ShallowCopy(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Shallow copy of adaptor
        """
    def Sphere(self) -> OCP.gp.gp_Sphere: 
        """
        None
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
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
    def UTrim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns a surface trimmed in the U direction equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def VContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Return CN.
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
    def VTrim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns a surface trimmed in the V direction between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameters U,V on the surface.
        """
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,V : OCP.gp.gp_Ax1) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
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
