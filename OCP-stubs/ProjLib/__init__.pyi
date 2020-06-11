import OCP.ProjLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.Adaptor3d
import OCP.Adaptor2d
import OCP.Geom2d
import OCP.Standard
import OCP.gp
import OCP.math
import OCP.TColgp
import OCP.Geom
import OCP.GeomAdaptor
import OCP.TColStd
import OCP.GeomAbs
import OCP.AppParCurves
__all__  = [
"ProjLib",
"ProjLib_CompProjectedCurve",
"ProjLib_ComputeApprox",
"ProjLib_ComputeApproxOnPolarSurface",
"ProjLib_Projector",
"ProjLib_Cylinder",
"ProjLib_HCompProjectedCurve",
"ProjLib_HProjectedCurve",
"ProjLib_SequenceOfHSequenceOfPnt",
"ProjLib_Plane",
"ProjLib_PrjFunc",
"ProjLib_PrjResolve",
"ProjLib_ProjectOnPlane",
"ProjLib_ProjectOnSurface",
"ProjLib_ProjectedCurve",
"ProjLib_Cone",
"ProjLib_HSequenceOfHSequenceOfPnt",
"ProjLib_Sphere",
"ProjLib_Torus"
]
class ProjLib():
    """
    The projLib package first provides projection of curves on a plane along a given Direction. The result will be a 3D curve. The ProjLib package provides projection of curves on surfaces to compute the curve in the parametric space.
    """
    @staticmethod
    def IsAnaSurf_s(theAS : OCP.Adaptor3d.Adaptor3d_HSurface) -> bool: 
        """
        Returns "true" if surface is analytical, that is it can be Plane, Cylinder, Cone, Sphere, Torus. For all other types of surface method returns "false".
        """
    @staticmethod
    def MakePCurveOfType_s(PC : ProjLib_ProjectedCurve,aC : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Make empty P-Curve <aC> of relevant to <PC> type
        """
    @staticmethod
    @overload
    def Project_s(Sp : OCP.gp.gp_Sphere,P : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def Project_s(Pl : OCP.gp.gp_Pln,L : OCP.gp.gp_Lin) -> OCP.gp.gp_Lin2d: ...
    @staticmethod
    @overload
    def Project_s(Cy : OCP.gp.gp_Cylinder,Ci : OCP.gp.gp_Circ) -> OCP.gp.gp_Lin2d: ...
    @staticmethod
    @overload
    def Project_s(To : OCP.gp.gp_Torus,P : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt2d: ...
    @staticmethod
    @overload
    def Project_s(Pl : OCP.gp.gp_Pln,H : OCP.gp.gp_Hypr) -> OCP.gp.gp_Hypr2d: ...
    @staticmethod
    @overload
    def Project_s(Pl : OCP.gp.gp_Pln,P : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt2d: ...
    @staticmethod
    @overload
    def Project_s(Cy : OCP.gp.gp_Cylinder,L : OCP.gp.gp_Lin) -> OCP.gp.gp_Lin2d: ...
    @staticmethod
    @overload
    def Project_s(Sp : OCP.gp.gp_Sphere,Ci : OCP.gp.gp_Circ) -> OCP.gp.gp_Lin2d: ...
    @staticmethod
    @overload
    def Project_s(Pl : OCP.gp.gp_Pln,E : OCP.gp.gp_Elips) -> OCP.gp.gp_Elips2d: ...
    @staticmethod
    @overload
    def Project_s(Pl : OCP.gp.gp_Pln,C : OCP.gp.gp_Circ) -> OCP.gp.gp_Circ2d: ...
    @staticmethod
    @overload
    def Project_s(Co : OCP.gp.gp_Cone,P : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt2d: ...
    @staticmethod
    @overload
    def Project_s(Cy : OCP.gp.gp_Cylinder,P : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt2d: ...
    @staticmethod
    @overload
    def Project_s(To : OCP.gp.gp_Torus,Ci : OCP.gp.gp_Circ) -> OCP.gp.gp_Lin2d: ...
    @staticmethod
    @overload
    def Project_s(Co : OCP.gp.gp_Cone,L : OCP.gp.gp_Lin) -> OCP.gp.gp_Lin2d: ...
    @staticmethod
    @overload
    def Project_s(Co : OCP.gp.gp_Cone,Ci : OCP.gp.gp_Circ) -> OCP.gp.gp_Lin2d: ...
    @staticmethod
    @overload
    def Project_s(Pl : OCP.gp.gp_Pln,P : OCP.gp.gp_Parab) -> OCP.gp.gp_Parab2d: ...
    def __init__(self) -> None: ...
    pass
class ProjLib_CompProjectedCurve(OCP.Adaptor2d.Adaptor2d_Curve2d):
    """
    None
    """
    def BSpline(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None
        """
    def Bounds(self,Index : int) -> Tuple[float, float]: 
        """
        returns the bounds of the continuous part corresponding to Index
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
        The returned vector gives the value of the derivative for the order of derivation N. Raised if N < 1. Raised if N > 2.
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
        Returns the first parameter of the curve C which has a projection on S.
        """
    def GetCurve(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def GetSequence(self) -> ProjLib_HSequenceOfHSequenceOfPnt: 
        """
        None
        """
    def GetSurface(self) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        None
        """
    def GetTolerance(self) -> Tuple[float, float]: 
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
    def Init(self) -> None: 
        """
        computes a set of projected point and determine the continuous parts of the projected curves. The points corresponding to a projection on the bounds of the surface are included in this set of points.
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Returns the parameters corresponding to S discontinuities.
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
    def IsSinglePnt(self,Index : int,P : OCP.gp.gp_Pnt2d) -> bool: 
        """
        returns True if part of projection with number Index is a single point and writes its coordinates in P
        """
    def IsUIso(self,Index : int,U : float) -> bool: 
        """
        returns True if part of projection with number Index is an u-isoparametric curve of input surface
        """
    def IsVIso(self,Index : int,V : float) -> bool: 
        """
        returns True if part of projection with number Index is an v-isoparametric curve of input surface
        """
    def LastParameter(self) -> float: 
        """
        Returns the last parameter of the curve C which has a projection on S.
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    @overload
    def Load(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        Changes the surface.

        Changes the curve.
        """
    @overload
    def Load(self,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: ...
    def MaxDistance(self,Index : int) -> float: 
        """
        returns the maximum distance between curve to project and surface
        """
    def NbCurves(self) -> int: 
        """
        returns the number of continuous part of the projected curve
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals which define an S continuous part of the projected curve
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
    def Trim(self,FirstParam : float,LastParam : float,Tol : float) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 2d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.
        """
    @overload
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve,TolU : float,TolV : float,MaxDist : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve,TolU : float,TolV : float) -> None: ...
    pass
class ProjLib_ComputeApprox():
    """
    Approximate the projection of a 3d curve on an analytic surface and stores the result in Approx. The result is a 2d curve. For approximation some parameters are used, including required tolerance of approximation. Tolerance is maximal possible value of 3d deviation of 3d projection of projected curve from "exact" 3d projection. Since algorithm searches 2d curve on surface, required 2d tolerance is computed from 3d tolerance with help of U,V resolutions of surface. 3d and 2d tolerances have sence only for curves on surface, it defines precision of projecting and approximation and have nothing to do with distance between the projected curve and the surface.
    """
    def BSpline(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None
        """
    def Perform(self,C : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: 
        """
        Performs projecting. In case of approximation current values of parameters are used: default values or set by corresponding methods Set...
        """
    def SetBndPnt(self,theBndPnt : OCP.AppParCurves.AppParCurves_Constraint) -> None: 
        """
        Set the parameter, which defines type of boundary condition between segments during approximation. It can be AppParCurves_PassPoint or AppParCurves_TangencyPoint. Default value is AppParCurves_TangencyPoint;
        """
    def SetDegree(self,theDegMin : int,theDegMax : int) -> None: 
        """
        Set min and max possible degree of result BSpline curve2d, which is got by approximation. If theDegMin/Max < 0, algorithm uses values that are chosen depending of types curve 3d and surface.
        """
    def SetMaxSegments(self,theMaxSegments : int) -> None: 
        """
        Set the parameter, which defines maximal value of parametric intervals the projected curve can be cut for approximation. If theMaxSegments < 0, algorithm uses default value = 1000.
        """
    def SetTolerance(self,theTolerance : float) -> None: 
        """
        Set tolerance of approximation. Default value is Precision::Confusion().
        """
    def Tolerance(self) -> float: 
        """
        returns the reached Tolerance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.Adaptor3d.Adaptor3d_HSurface,Tol : float) -> None: ...
    pass
class ProjLib_ComputeApproxOnPolarSurface():
    """
    Approximate the projection of a 3d curve on an polar surface and stores the result in Approx. The result is a 2d curve. The evaluation of the current point of the 2d curve is done with the evaluation of the extrema P3d - Surface. For approximation some parameters are used, including required tolerance of approximation. Tolerance is maximal possible value of 3d deviation of 3d projection of projected curve from "exact" 3d projection. Since algorithm searches 2d curve on surface, required 2d tolerance is computed from 3d tolerance with help of U,V resolutions of surface. 3d and 2d tolerances have sence only for curves on surface, it defines precision of projecting and approximation and have nothing to do with distance between the projected curve and the surface.
    """
    def BSpline(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns result curve 2d.
        """
    def BuildInitialCurve2d(self,Curve : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        Builds initial 2d curve as BSpline with degree = 1 using Extrema algoritm. Method is used in method Perform(...).
        """
    def Curve2d(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns second 2d curve.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    @overload
    def Perform(self,InitCurve2d : OCP.Adaptor2d.Adaptor2d_HCurve2d,C : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Method, which performs projecting, using default values of parameters or they must be set by corresponding methods before using.

        Method, which performs projecting, using default values of parameters or they must be set by corresponding methods before using. Parameter InitCurve2d is any rough estimation of 2d result curve.
        """
    @overload
    def Perform(self,C : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: ...
    def ProjectUsingInitialCurve2d(self,Curve : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.Adaptor3d.Adaptor3d_HSurface,InitCurve2d : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Method, which performs projecting. Method is used in method Perform(...).
        """
    def SetBndPnt(self,theBndPnt : OCP.AppParCurves.AppParCurves_Constraint) -> None: 
        """
        Set the parameter, which defines type of boundary condition between segments during approximation. It can be AppParCurves_PassPoint or AppParCurves_TangencyPoint. Default value is AppParCurves_TangencyPoint.
        """
    def SetDegree(self,theDegMin : int,theDegMax : int) -> None: 
        """
        Set min and max possible degree of result BSpline curve2d, which is got by approximation. If theDegMin/Max < 0, algorithm uses values min = 2, max = 8.
        """
    def SetMaxDist(self,theMaxDist : float) -> None: 
        """
        Set the parameter, which defines maximal possible distance between projected curve and surface. It is used only for projecting on not analytical surfaces. If theMaxDist < 0, algoritm uses default value 100.*Tolerance. If real distance between curve and surface more then theMaxDist, algorithm stops working.
        """
    def SetMaxSegments(self,theMaxSegments : int) -> None: 
        """
        Set the parameter, which defines maximal value of parametric intervals the projected curve can be cut for approximation. If theMaxSegments < 0, algorithm uses default value = 1000.
        """
    def SetTolerance(self,theTolerance : float) -> None: 
        """
        Set the tolerance used to project the curve on the surface. Default value is Precision::Approximation().
        """
    def Tolerance(self) -> float: 
        """
        returns the reached Tolerance.
        """
    @overload
    def __init__(self,InitCurve2d : OCP.Adaptor2d.Adaptor2d_HCurve2d,C : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.Adaptor3d.Adaptor3d_HSurface,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.Adaptor3d.Adaptor3d_HSurface,Tol : float=0.0001) -> None: ...
    @overload
    def __init__(self,InitCurve2d : OCP.Adaptor2d.Adaptor2d_HCurve2d,InitCurve2dBis : OCP.Adaptor2d.Adaptor2d_HCurve2d,C : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.Adaptor3d.Adaptor3d_HSurface,Tol : float) -> None: ...
    pass
class ProjLib_Projector():
    """
    Root class for projection algorithms, stores the result.
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
    def Done(self) -> None: 
        """
        Set isDone = Standard_True;
        """
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
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
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @overload
    def Project(self,C : OCP.gp.gp_Circ) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def Project(self,H : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def Project(self,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def Project(self,P : OCP.gp.gp_Parab) -> None: ...
    @overload
    def Project(self,E : OCP.gp.gp_Elips) -> None: ...
    def SetBSpline(self,C : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
        """
        None
        """
    def SetBezier(self,C : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
        """
        None
        """
    def SetPeriodic(self) -> None: 
        """
        None
        """
    def SetType(self,Type : OCP.GeomAbs.GeomAbs_CurveType) -> None: 
        """
        None
        """
    def UFrame(self,CFirst : float,CLast : float,UFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ UFirst, UFirst + Period [
        """
    def VFrame(self,CFirst : float,CLast : float,VFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ VFirst, VFirst + Period [
        """
    def __init__(self) -> None: ...
    pass
class ProjLib_Cylinder(ProjLib_Projector):
    """
    Projects elementary curves on a cylinder.
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
    def Done(self) -> None: 
        """
        Set isDone = Standard_True;
        """
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
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
    def Init(self,Cyl : OCP.gp.gp_Cylinder) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @overload
    def Project(self,L : OCP.gp.gp_Lin) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def Project(self,P : OCP.gp.gp_Parab) -> None: ...
    @overload
    def Project(self,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def Project(self,E : OCP.gp.gp_Elips) -> None: ...
    @overload
    def Project(self,H : OCP.gp.gp_Hypr) -> None: ...
    def SetBSpline(self,C : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
        """
        None
        """
    def SetBezier(self,C : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
        """
        None
        """
    def SetPeriodic(self) -> None: 
        """
        None
        """
    def SetType(self,Type : OCP.GeomAbs.GeomAbs_CurveType) -> None: 
        """
        None
        """
    def UFrame(self,CFirst : float,CLast : float,UFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ UFirst, UFirst + Period [
        """
    def VFrame(self,CFirst : float,CLast : float,VFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ VFirst, VFirst + Period [
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,E : OCP.gp.gp_Elips) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,L : OCP.gp.gp_Lin) -> None: ...
    pass
class ProjLib_HCompProjectedCurve(OCP.Adaptor2d.Adaptor2d_HCurve2d, OCP.Standard.Standard_Transient):
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
    def ChangeCurve2d(self) -> ProjLib_CompProjectedCurve: 
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
    def Set(self,C : ProjLib_CompProjectedCurve) -> None: 
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
    def __init__(self,C : ProjLib_CompProjectedCurve) -> None: ...
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
class ProjLib_HProjectedCurve(OCP.Adaptor2d.Adaptor2d_HCurve2d, OCP.Standard.Standard_Transient):
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
    def ChangeCurve2d(self) -> ProjLib_ProjectedCurve: 
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
    def Set(self,C : ProjLib_ProjectedCurve) -> None: 
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
    def __init__(self,C : ProjLib_ProjectedCurve) -> None: ...
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
class ProjLib_SequenceOfHSequenceOfPnt(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : ProjLib_SequenceOfHSequenceOfPnt) -> None: ...
    def Assign(self,theOther : ProjLib_SequenceOfHSequenceOfPnt) -> ProjLib_SequenceOfHSequenceOfPnt: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
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
    def First(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : ProjLib_SequenceOfHSequenceOfPnt) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ProjLib_SequenceOfHSequenceOfPnt) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
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
    def Prepend(self,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : ProjLib_SequenceOfHSequenceOfPnt) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ProjLib_SequenceOfHSequenceOfPnt) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : ProjLib_SequenceOfHSequenceOfPnt) -> None: ...
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
class ProjLib_Plane(ProjLib_Projector):
    """
    Projects elementary curves on a plane.
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
    def Done(self) -> None: 
        """
        Set isDone = Standard_True;
        """
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
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
    def Init(self,Pl : OCP.gp.gp_Pln) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @overload
    def Project(self,L : OCP.gp.gp_Lin) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def Project(self,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def Project(self,E : OCP.gp.gp_Elips) -> None: ...
    @overload
    def Project(self,H : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def Project(self,P : OCP.gp.gp_Parab) -> None: ...
    def SetBSpline(self,C : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
        """
        None
        """
    def SetBezier(self,C : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
        """
        None
        """
    def SetPeriodic(self) -> None: 
        """
        None
        """
    def SetType(self,Type : OCP.GeomAbs.GeomAbs_CurveType) -> None: 
        """
        None
        """
    def UFrame(self,CFirst : float,CLast : float,UFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ UFirst, UFirst + Period [
        """
    def VFrame(self,CFirst : float,CLast : float,VFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ VFirst, VFirst + Period [
        """
    @overload
    def __init__(self,Pl : OCP.gp.gp_Pln,P : OCP.gp.gp_Parab) -> None: ...
    @overload
    def __init__(self,Pl : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,Pl : OCP.gp.gp_Pln,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,Pl : OCP.gp.gp_Pln,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Pl : OCP.gp.gp_Pln,H : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def __init__(self,Pl : OCP.gp.gp_Pln,E : OCP.gp.gp_Elips) -> None: ...
    pass
class ProjLib_PrjFunc(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function.
        """
    def Solution(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns point on surface
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class ProjLib_PrjResolve():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def Perform(self,t : float,U : float,V : float,Tol : OCP.gp.gp_Pnt2d,Inf : OCP.gp.gp_Pnt2d,Sup : OCP.gp.gp_Pnt2d,FTol : float=-1.0,StrictInside : bool=False) -> None: 
        """
        Calculates the ort from C(t) to S with a close point. The close point is defined by the parameter values U0 and V0. The function F(u,v)=distance(S(u,v),C(t)) has an extremum when gradient(F)=0. The algorithm searchs a zero near the close point.
        """
    def Solution(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the point of the extremum distance.
        """
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface,Fix : int) -> None: ...
    pass
class ProjLib_ProjectOnPlane(OCP.Adaptor3d.Adaptor3d_Curve):
    """
    Class used to project a 3d curve on a plane. The result will be a 3d curve.
    """
    def BSpline(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        Warning ! this will NOT make a copy of the BSpline Curve : If you want to modify the Curve please make a copy yourself Also it will NOT trim the surface to myFirst/Last.
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierCurve: 
        """
        Warning ! this will NOT make a copy of the Bezier Curve : If you want to modify the Curve please make a copy yourself Also it will NOT trim the surface to myFirst/Last.
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
    def Degree(self) -> int: 
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
    def GetCurve(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def GetDirection(self) -> OCP.gp.gp_Dir: 
        """
        None
        """
    def GetPlane(self) -> OCP.gp.gp_Ax3: 
        """
        None
        """
    def GetResult(self) -> OCP.GeomAdaptor.GeomAdaptor_HCurve: 
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
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def Load(self,C : OCP.Adaptor3d.Adaptor3d_HCurve,Tolerance : float,KeepParametrization : bool=True) -> None: 
        """
        Sets the Curve and perform the projection. if <KeepParametrization> is true, the parametrization of the Projected Curve <PC> will be the same as the parametrization of the initial curve <C>. It meens: proj(C(u)) = PC(u) for each u. Otherwize, the parametrization may change.
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
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Pl : OCP.gp.gp_Ax3,D : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,Pl : OCP.gp.gp_Ax3) -> None: ...
    pass
class ProjLib_ProjectOnSurface():
    """
    Project a curve on a surface. The result ( a 3D Curve) will be an approximation
    """
    def BSpline(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Load(self,C : OCP.Adaptor3d.Adaptor3d_HCurve,Tolerance : float) -> None: 
        """
        Compute the projection of the curve <C> on the Surface.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: ...
    pass
class ProjLib_ProjectedCurve(OCP.Adaptor2d.Adaptor2d_Curve2d):
    """
    Compute the 2d-curve. Try to solve the particular case if possible. Otherwize, an approximation is done. For approximation some parameters are used, including required tolerance of approximation. Tolerance is maximal possible value of 3d deviation of 3d projection of projected curve from "exact" 3d projection. Since algorithm searches 2d curve on surface, required 2d tolerance is computed from 3d tolerance with help of U,V resolutions of surface. 3d and 2d tolerances have sence only for curves on surface, it defines precision of projecting and approximation and have nothing to do with distance between the projected curve and the surface.
    """
    def BSpline(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Warning ! This will NOT make a copy of the BSpline Curve - If you want to modify the Curve please make a copy yourself Also it will NOT trim the surface to myFirst/Last.
        """
    def Bezier(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Warning ! This will NOT make a copy of the -- Bezier Curve - If you want to modify -- the Curve please make a copy yourself -- Also it will NOT trim the surface to -- myFirst/Last.
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
    def GetCurve(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def GetSurface(self) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        None
        """
    def GetTolerance(self) -> float: 
        """
        returns the tolerance reached if an approximation is Done.
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
    @overload
    def Load(self,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: 
        """
        Changes the tolerance used to project the curve on the surface

        Changes the Surface.
        """
    @overload
    def Load(self,Tolerance : float) -> None: ...
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
    def Perform(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        Performs projecting for given curve. If projecting uses approximation, approximation parameters can be set before by corresponding methods SetDegree(...), SetMaxSegmets(...), SetBndPnt(...), SetMaxDist(...)
        """
    def Period(self) -> float: 
        """
        None
        """
    def Resolution(self,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    def SetBndPnt(self,theBndPnt : OCP.AppParCurves.AppParCurves_Constraint) -> None: 
        """
        Set the parameter, which defines type of boundary condition between segments during approximation. It can be AppParCurves_PassPoint or AppParCurves_TangencyPoint. Default value is AppParCurves_TangencyPoint;
        """
    def SetDegree(self,theDegMin : int,theDegMax : int) -> None: 
        """
        Set min and max possible degree of result BSpline curve2d, which is got by approximation. If theDegMin/Max < 0, algorithm uses values that are chosen depending of types curve 3d and surface.
        """
    def SetMaxDist(self,theMaxDist : float) -> None: 
        """
        Set the parameter, which degines maximal possible distance between projected curve and surface. It uses only for projecting on not analytical surfaces. If theMaxDist < 0, algoritm uses default value 100.*Tolerance. If real distance between curve and surface more then theMaxDist, algorithm stops working.
        """
    def SetMaxSegments(self,theMaxSegments : int) -> None: 
        """
        Set the parameter, which defines maximal value of parametric intervals the projected curve can be cut for approximation. If theMaxSegments < 0, algorithm uses default value = 1000.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.
        """
    @overload
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve,Tol : float) -> None: ...
    @overload
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: ...
    pass
class ProjLib_Cone(ProjLib_Projector):
    """
    Projects elementary curves on a cone.
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
    def Done(self) -> None: 
        """
        Set isDone = Standard_True;
        """
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
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
    def Init(self,Co : OCP.gp.gp_Cone) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @overload
    def Project(self,E : OCP.gp.gp_Elips) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def Project(self,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def Project(self,H : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def Project(self,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def Project(self,P : OCP.gp.gp_Parab) -> None: ...
    def SetBSpline(self,C : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
        """
        None
        """
    def SetBezier(self,C : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
        """
        None
        """
    def SetPeriodic(self) -> None: 
        """
        None
        """
    def SetType(self,Type : OCP.GeomAbs.GeomAbs_CurveType) -> None: 
        """
        None
        """
    def UFrame(self,CFirst : float,CLast : float,UFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ UFirst, UFirst + Period [
        """
    def VFrame(self,CFirst : float,CLast : float,VFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ VFirst, VFirst + Period [
        """
    @overload
    def __init__(self,Co : OCP.gp.gp_Cone,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Co : OCP.gp.gp_Cone,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def __init__(self,Co : OCP.gp.gp_Cone) -> None: ...
    pass
class ProjLib_HSequenceOfHSequenceOfPnt(ProjLib_SequenceOfHSequenceOfPnt, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : ProjLib_SequenceOfHSequenceOfPnt) -> None: ...
    def Assign(self,theOther : ProjLib_SequenceOfHSequenceOfPnt) -> ProjLib_SequenceOfHSequenceOfPnt: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        Last item access
        """
    def ChangeSequence(self) -> ProjLib_SequenceOfHSequenceOfPnt: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
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
    def First(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
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
    def InsertAfter(self,theIndex : int,theSeq : ProjLib_SequenceOfHSequenceOfPnt) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ProjLib_SequenceOfHSequenceOfPnt) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
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
    def Prepend(self,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : ProjLib_SequenceOfHSequenceOfPnt) -> None: ...
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
    def Sequence(self) -> ProjLib_SequenceOfHSequenceOfPnt: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ProjLib_SequenceOfHSequenceOfPnt) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : ProjLib_SequenceOfHSequenceOfPnt) -> None: ...
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
class ProjLib_Sphere(ProjLib_Projector):
    """
    Projects elementary curves on a sphere.
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
    def Done(self) -> None: 
        """
        Set isDone = Standard_True;
        """
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
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
    def Init(self,Sp : OCP.gp.gp_Sphere) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @overload
    def Project(self,P : OCP.gp.gp_Parab) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def Project(self,E : OCP.gp.gp_Elips) -> None: ...
    @overload
    def Project(self,H : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def Project(self,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def Project(self,L : OCP.gp.gp_Lin) -> None: ...
    def SetBSpline(self,C : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
        """
        None
        """
    def SetBezier(self,C : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
        """
        None
        """
    def SetInBounds(self,U : float) -> None: 
        """
        Set the point of parameter U on C in the natural restrictions of the sphere.
        """
    def SetPeriodic(self) -> None: 
        """
        None
        """
    def SetType(self,Type : OCP.GeomAbs.GeomAbs_CurveType) -> None: 
        """
        None
        """
    def UFrame(self,CFirst : float,CLast : float,UFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ UFirst, UFirst + Period [
        """
    def VFrame(self,CFirst : float,CLast : float,VFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ VFirst, VFirst + Period [
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Sp : OCP.gp.gp_Sphere,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,Sp : OCP.gp.gp_Sphere) -> None: ...
    pass
class ProjLib_Torus(ProjLib_Projector):
    """
    Projects elementary curves on a torus.
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
    def Done(self) -> None: 
        """
        Set isDone = Standard_True;
        """
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
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
    def Init(self,To : OCP.gp.gp_Torus) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @overload
    def Project(self,P : OCP.gp.gp_Parab) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def Project(self,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def Project(self,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def Project(self,H : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def Project(self,E : OCP.gp.gp_Elips) -> None: ...
    def SetBSpline(self,C : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
        """
        None
        """
    def SetBezier(self,C : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
        """
        None
        """
    def SetPeriodic(self) -> None: 
        """
        None
        """
    def SetType(self,Type : OCP.GeomAbs.GeomAbs_CurveType) -> None: 
        """
        None
        """
    def UFrame(self,CFirst : float,CLast : float,UFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ UFirst, UFirst + Period [
        """
    def VFrame(self,CFirst : float,CLast : float,VFirst : float,Period : float) -> None: 
        """
        Translates the 2d curve to set the part of the curve [CFirst, CLast] in the range [ VFirst, VFirst + Period [
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,To : OCP.gp.gp_Torus,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,To : OCP.gp.gp_Torus) -> None: ...
    pass
