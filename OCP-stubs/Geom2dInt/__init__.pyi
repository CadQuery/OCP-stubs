import OCP.Geom2dInt
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IntCurve
import OCP.IntRes2d
import OCP.Bnd
import OCP.gp
import OCP.Intf
import OCP.GeomAbs
import OCP.Extrema
import OCP.TColStd
import OCP.Adaptor2d
import OCP.math
__all__  = [
"Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter",
"Geom2dInt_GInter",
"Geom2dInt_Geom2dCurveTool",
"Geom2dInt_IntConicCurveOfGInter",
"Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter",
"Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter",
"Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter",
"Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter",
"Geom2dInt_TheIntConicCurveOfGInter",
"Geom2dInt_TheIntPCurvePCurveOfGInter",
"Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter",
"Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter",
"Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter",
"Geom2dInt_TheProjPCurOfGInter"
]
class Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter():
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
    def Perform(self,Poly1 : Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter,Poly2 : Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter) -> Tuple[int, int, float, float]: 
        """
        None

        None
        """
    @overload
    def Perform(self,Uo : float,Vo : float,UInf : float,VInf : float,USup : float,VSup : float) -> None: ...
    def Roots(self) -> Tuple[float, float]: 
        """
        None
        """
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,Tol : float) -> None: ...
    pass
class Geom2dInt_GInter(OCP.IntRes2d.IntRes2d_Intersection):
    """
    None
    """
    def ComputeDomain(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,TolDomain : float) -> OCP.IntRes2d.IntRes2d_Domain: 
        """
        Create a domain from a curve
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
    @overload
    def Perform(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,D1 : OCP.IntRes2d.IntRes2d_Domain,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,TolConf : float,Tol : float) -> None: 
        """
        Intersection between 2 curves.

        Intersection between 2 curves.

        Intersection between 2 curves.

        Intersection between 2 curves.

        Intersection between 2 curves.

        Intersection between 2 curves.
        """
    @overload
    def Perform(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,D1 : OCP.IntRes2d.IntRes2d_Domain,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,D1 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,TolConf : float,Tol : float) -> None: ...
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
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,D : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,D1 : OCP.IntRes2d.IntRes2d_Domain,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,D1 : OCP.IntRes2d.IntRes2d_Domain,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,TolConf : float,Tol : float) -> None: ...
    pass
class Geom2dInt_Geom2dCurveTool():
    """
    This class provides a Geom2dCurveTool as < Geom2dCurveTool from IntCurve > from a Tool as < Geom2dCurveTool from Adaptor3d > .
    """
    @staticmethod
    def Circle_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Circ2d: 
        """
        Returns the Circ2d from gp corresponding to the curve C. This method is called only when TheType returns GeomAbs_Circle.
        """
    @staticmethod
    def D0_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    @staticmethod
    def D1_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    @staticmethod
    def D2_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d,N : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    @staticmethod
    def D3_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d,N : OCP.gp.gp_Vec2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    @staticmethod
    def DN_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    @staticmethod
    def Degree_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> int: 
        """
        None
        """
    @staticmethod
    def Ellipse_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Elips2d: 
        """
        Returns the Elips2d from gp corresponding to the curve C. This method is called only when TheType returns GeomAbs_Ellipse.
        """
    @staticmethod
    @overload
    def EpsX_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Eps_XYZ : float) -> float: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def EpsX_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: ...
    @staticmethod
    def FirstParameter_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    @staticmethod
    def GetInterval_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Index : int,Tab : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float, float]: 
        """
        output the bounds of interval of index <Index> used if Type == Composite.
        """
    @staticmethod
    def GetType_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        None
        """
    @staticmethod
    def Hyperbola_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Hypr2d: 
        """
        Returns the Hypr2d from gp corresponding to the curve C. This method is called only when TheType returns GeomAbs_Hyperbola.
        """
    @staticmethod
    def Intervals_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Tab : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        compute Tab.
        """
    @staticmethod
    def LastParameter_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Lin2d: 
        """
        Returns the Lin2d from gp corresponding to the curve C. This method is called only when TheType returns GeomAbs_Line.
        """
    @staticmethod
    def NbIntervals_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> int: 
        """
        output the number of interval of continuity C2 of the curve
        """
    @staticmethod
    @overload
    def NbSamples_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,U1 : float) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbSamples_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> int: ...
    @staticmethod
    def Parabola_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Parab2d: 
        """
        Returns the Parab2d from gp corresponding to the curve C. This method is called only when TheType returns GeomAbs_Parabola.
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,X : float) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Geom2dInt_IntConicCurveOfGInter(OCP.IntRes2d.IntRes2d_Intersection):
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
    @overload
    def Perform(self,C : OCP.gp.gp_Circ2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: 
        """
        Intersection between a line and a parametric curve.

        Intersection between a line and a parametric curve.

        Intersection between an ellipse and a parametric curve.

        Intersection between a parabola and a parametric curve.

        Intersection between the main branch of an hyperbola and a parametric curve.
        """
    @overload
    def Perform(self,L : OCP.gp.gp_Lin2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,H : OCP.gp.gp_Hypr2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,Prb : OCP.gp.gp_Parab2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,E : OCP.gp.gp_Elips2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
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
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,Prb : OCP.gp.gp_Parab2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    pass
class Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
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
    def __init__(self,IT : OCP.IntCurve.IntCurve_IConicTool,PC : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    pass
class Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
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
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        sets the field mycurve of the function.
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
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter():
    """
    None
    """
    @staticmethod
    @overload
    def Locate_s(P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,Papp : OCP.Extrema.Extrema_POnCurv2d) -> None: 
        """
        Among a set of points {C(ui),i=1,NbU}, locate the point P=C(uj) such that: distance(P,C) = Min{distance(P,C(ui))}

        Among a set of points {C(ui),i=1,NbU}, locate the point P=C(uj) such that: distance(P,C) = Min{distance(P,C(ui))} The research is done between umin and usup.
        """
    @staticmethod
    @overload
    def Locate_s(P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,Umin : float,Usup : float,Papp : OCP.Extrema.Extrema_POnCurv2d) -> None: ...
    def __init__(self) -> None: ...
    pass
class Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
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
    def __init__(self,curve1 : OCP.Adaptor2d.Adaptor2d_Curve2d,curve2 : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    pass
class Geom2dInt_TheIntConicCurveOfGInter(OCP.IntRes2d.IntRes2d_Intersection):
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
    @overload
    def Perform(self,H : OCP.gp.gp_Hypr2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: 
        """
        Intersection between a line and a parametric curve.

        Intersection between a line and a parametric curve.

        Intersection between an ellipse and a parametric curve.

        Intersection between a parabola and a parametric curve.

        Intersection between the main branch of an hyperbola and a parametric curve.
        """
    @overload
    def Perform(self,E : OCP.gp.gp_Elips2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,Prb : OCP.gp.gp_Parab2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,L : OCP.gp.gp_Lin2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
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
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,Prb : OCP.gp.gp_Parab2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d,D1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    pass
class Geom2dInt_TheIntPCurvePCurveOfGInter(OCP.IntRes2d.IntRes2d_Intersection):
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
    @overload
    def Perform(self,Curve1 : OCP.Adaptor2d.Adaptor2d_Curve2d,Domain1 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,Curve1 : OCP.Adaptor2d.Adaptor2d_Curve2d,Domain1 : OCP.IntRes2d.IntRes2d_Domain,Curve2 : OCP.Adaptor2d.Adaptor2d_Curve2d,Domain2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
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
class Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter(OCP.IntRes2d.IntRes2d_Intersection):
    """
    None
    """
    def And_Domaine_Objet1_Intersections(self,TheImpTool : OCP.IntCurve.IntCurve_IConicTool,TheParCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,TheImpCurveDomain : OCP.IntRes2d.IntRes2d_Domain,TheParCurveDomain : OCP.IntRes2d.IntRes2d_Domain,Inter2_And_Domain2 : OCP.TColStd.TColStd_Array1OfReal,Inter1 : OCP.TColStd.TColStd_Array1OfReal,Resultat1 : OCP.TColStd.TColStd_Array1OfReal,Resultat2 : OCP.TColStd.TColStd_Array1OfReal,EpsNul : float) -> Tuple[int]: 
        """
        None
        """
    def FindU(self,parameter : float,point : OCP.gp.gp_Pnt2d,TheParCurev : OCP.Adaptor2d.Adaptor2d_Curve2d,TheImpTool : OCP.IntCurve.IntCurve_IConicTool) -> float: 
        """
        None
        """
    def FindV(self,parameter : float,point : OCP.gp.gp_Pnt2d,TheImpTool : OCP.IntCurve.IntCurve_IConicTool,ParCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,TheParCurveDomain : OCP.IntRes2d.IntRes2d_Domain,V0 : float,V1 : float,Tolerance : float) -> float: 
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
    def Perform(self,ITool : OCP.IntCurve.IntCurve_IConicTool,Dom1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,Dom2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: 
        """
        Intersection between an implicit curve and a parametrised curve. The exception ConstructionError is raised if the domain of the parametrised curve does not verify HasFirstPoint and HasLastPoint return True.
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
    @overload
    def __init__(self,ITool : OCP.IntCurve.IntCurve_IConicTool,Dom1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,Dom2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter():
    """
    None
    """
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Umin : float,Usup : float,TolU : float) -> None: 
        """
        sets the fields of the algorithm.
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
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,TolU : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,Umin : float,Usup : float,TolU : float) -> None: ...
    pass
class Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter(OCP.Intf.Intf_Polygon2d):
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
    def ComputeWithBox(self,Curve : OCP.Adaptor2d.Adaptor2d_Curve2d,OtherBox : OCP.Bnd.Bnd_Box2d) -> None: 
        """
        The current polygon is modified if most of the points of the polygon are are outside the box <OtherBox>. In this situation, bounds are computed to build a polygon inside or near the OtherBox.
        """
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
    def __init__(self,Curve : OCP.Adaptor2d.Adaptor2d_Curve2d,NbPnt : int,Domain : OCP.IntRes2d.IntRes2d_Domain,Tol : float) -> None: ...
    pass
class Geom2dInt_TheProjPCurOfGInter():
    """
    None
    """
    @staticmethod
    @overload
    def FindParameter_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Pnt : OCP.gp.gp_Pnt2d,LowParameter : float,HighParameter : float,Tol : float) -> float: 
        """
        Returns the parameter V of the point on the parametric curve corresponding to the Point Pnt. The Correspondance between Pnt and the point P(V) on the parametric curve must be coherent with the way of determination of the signed distance between a point and the implicit curve. Tol is the tolerance on the distance between a point and the parametrised curve. In that case, no bounds are given. The research of the rigth parameter has to be made on the natural parametric domain of the curve.

        Returns the parameter V of the point on the parametric curve corresponding to the Point Pnt. The Correspondance between Pnt and the point P(V) on the parametric curve must be coherent with the way of determination of the signed distance between a point and the implicit curve. Tol is the tolerance on the distance between a point and the parametrised curve. LowParameter and HighParameter give the boundaries of the interval in wich the parameter certainly lies. These parameters are given to implement a more efficient algoritm. So, it is not necessary to check that the returned value verifies LowParameter <= Value <= HighParameter.
        """
    @staticmethod
    @overload
    def FindParameter_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Pnt : OCP.gp.gp_Pnt2d,Tol : float) -> float: ...
    def __init__(self) -> None: ...
    pass
