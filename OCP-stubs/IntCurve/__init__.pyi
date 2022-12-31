import OCP.IntCurve
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.math
import OCP.gp
import OCP.IntRes2d
import OCP.GeomAbs
import OCP.TColStd
__all__  = [
"IntCurve_IConicTool",
"IntCurve_IntConicConic",
"IntCurve_IntImpConicParConic",
"IntCurve_MyImpParToolOfIntImpConicParConic",
"IntCurve_PConic",
"IntCurve_PConicTool",
"IntCurve_ProjectOnPConicTool",
"Interval",
"PeriodicInterval"
]
class IntCurve_IConicTool():
    """
    Implementation of the ImpTool from IntImpParGen for conics of gp.
    """
    def D1(self,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d,N : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def Distance(self,P : OCP.gp.gp_Pnt2d) -> float: 
        """
        Computes the value of the signed distance between the point P and the implicit curve.
        """
    def FindParameter(self,P : OCP.gp.gp_Pnt2d) -> float: 
        """
        Returns the parameter U of the point on the implicit curve corresponding to the point P. The correspondence between P and the point P(U) on the implicit curve must be coherent with the way of determination of the signed distance.
        """
    def GradDistance(self,P : OCP.gp.gp_Pnt2d) -> OCP.gp.gp_Vec2d: 
        """
        Computes the Gradient of the Signed Distance between a point and the implicit curve, at the point P.
        """
    def Value(self,X : float) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Parab2d) -> None: ...
    @overload
    def __init__(self,IT : IntCurve_IConicTool) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntCurve_IntConicConic(OCP.IntRes2d.IntRes2d_Intersection):
    """
    Provides methods to intersect two conics. The exception ConstructionError is raised in constructors or in Perform methods when a domain (Domain from IntRes2d) is not correct, i-e when a Circle (Circ2d from gp) or an Ellipse (i-e Elips2d from gp) do not have a closed domain (use the SetEquivalentParameters method for a domain on a circle or an ellipse).
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
    def Perform(self,C : OCP.gp.gp_Circ2d,DC : OCP.IntRes2d.IntRes2d_Domain,H : OCP.gp.gp_Hypr2d,DH : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: 
        """
        Intersection between 2 lines from gp.

        Intersection between a line and a circle. The exception ConstructionError is raised if the method IsClosed of the domain of the circle returns False.

        Intersection between a line and an ellipse. The exception ConstructionError is raised if the method IsClosed of the domain of the ellipse returns False.

        Intersection between a line and a parabola from gp.

        Intersection between a line and an hyperbola.

        Intersection between 2 circles from gp. The exception ConstructionError is raised if the method IsClosed of the domain of one of the circle returns False.

        Intersection between a circle and an ellipse. The exception ConstructionError is raised if the method IsClosed of one the domain returns False.

        Intersection between a circle and a parabola. The exception ConstructionError is raised if the method IsClosed of the domain of the circle returns False.

        Intersection between a circle and an hyperbola. The exception ConstructionError is raised if the method IsClosed of the domain of the circle returns False.

        Intersection between 2 ellipses. The exception ConstructionError is raised if the method IsClosed of one of the domain returns False.

        Intersection between an ellipse and a parabola. The exception ConstructionError is raised if the method IsClosed of the domain of the ellipse returns False.

        Intersection between an ellipse and an hyperbola. The exception ConstructionError is raised if the method IsClosed of the domain of the ellipse returns False.

        Intersection between 2 parabolas.

        Intersection between a parabola and an hyperbola.

        Intersection between 2 hyperbolas.
        """
    @overload
    def Perform(self,L : OCP.gp.gp_Lin2d,DL : OCP.IntRes2d.IntRes2d_Domain,H : OCP.gp.gp_Hypr2d,DH : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,C1 : OCP.gp.gp_Circ2d,D1 : OCP.IntRes2d.IntRes2d_Domain,C2 : OCP.gp.gp_Circ2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,E1 : OCP.gp.gp_Elips2d,D1 : OCP.IntRes2d.IntRes2d_Domain,E2 : OCP.gp.gp_Elips2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,E : OCP.gp.gp_Elips2d,DE : OCP.IntRes2d.IntRes2d_Domain,P : OCP.gp.gp_Parab2d,DP : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,L : OCP.gp.gp_Lin2d,DL : OCP.IntRes2d.IntRes2d_Domain,P : OCP.gp.gp_Parab2d,DP : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,P1 : OCP.gp.gp_Parab2d,D1 : OCP.IntRes2d.IntRes2d_Domain,P2 : OCP.gp.gp_Parab2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ2d,DC : OCP.IntRes2d.IntRes2d_Domain,P : OCP.gp.gp_Parab2d,DP : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,L1 : OCP.gp.gp_Lin2d,D1 : OCP.IntRes2d.IntRes2d_Domain,L2 : OCP.gp.gp_Lin2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Parab2d,DP : OCP.IntRes2d.IntRes2d_Domain,H : OCP.gp.gp_Hypr2d,DH : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,H1 : OCP.gp.gp_Hypr2d,D1 : OCP.IntRes2d.IntRes2d_Domain,H2 : OCP.gp.gp_Hypr2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,L : OCP.gp.gp_Lin2d,DL : OCP.IntRes2d.IntRes2d_Domain,C : OCP.gp.gp_Circ2d,DC : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,E : OCP.gp.gp_Elips2d,DE : OCP.IntRes2d.IntRes2d_Domain,H : OCP.gp.gp_Hypr2d,DH : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,L : OCP.gp.gp_Lin2d,DL : OCP.IntRes2d.IntRes2d_Domain,E : OCP.gp.gp_Elips2d,DE : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ2d,DC : OCP.IntRes2d.IntRes2d_Domain,E : OCP.gp.gp_Elips2d,DE : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
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
    def __init__(self,C : OCP.gp.gp_Circ2d,DC : OCP.IntRes2d.IntRes2d_Domain,H : OCP.gp.gp_Hypr2d,DH : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,DL : OCP.IntRes2d.IntRes2d_Domain,H : OCP.gp.gp_Hypr2d,DH : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Parab2d,D1 : OCP.IntRes2d.IntRes2d_Domain,P2 : OCP.gp.gp_Parab2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d,DE : OCP.IntRes2d.IntRes2d_Domain,P : OCP.gp.gp_Parab2d,DP : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,L1 : OCP.gp.gp_Lin2d,D1 : OCP.IntRes2d.IntRes2d_Domain,L2 : OCP.gp.gp_Lin2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,DL : OCP.IntRes2d.IntRes2d_Domain,C : OCP.gp.gp_Circ2d,DC : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,DL : OCP.IntRes2d.IntRes2d_Domain,P : OCP.gp.gp_Parab2d,DP : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,H1 : OCP.gp.gp_Hypr2d,D1 : OCP.IntRes2d.IntRes2d_Domain,H2 : OCP.gp.gp_Hypr2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,D1 : OCP.IntRes2d.IntRes2d_Domain,C2 : OCP.gp.gp_Circ2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E1 : OCP.gp.gp_Elips2d,D1 : OCP.IntRes2d.IntRes2d_Domain,E2 : OCP.gp.gp_Elips2d,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Parab2d,DP : OCP.IntRes2d.IntRes2d_Domain,H : OCP.gp.gp_Hypr2d,DH : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d,DE : OCP.IntRes2d.IntRes2d_Domain,H : OCP.gp.gp_Hypr2d,DH : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d,DC : OCP.IntRes2d.IntRes2d_Domain,P : OCP.gp.gp_Parab2d,DP : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,DL : OCP.IntRes2d.IntRes2d_Domain,E : OCP.gp.gp_Elips2d,DE : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d,DC : OCP.IntRes2d.IntRes2d_Domain,E : OCP.gp.gp_Elips2d,DE : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    pass
class IntCurve_IntImpConicParConic(OCP.IntRes2d.IntRes2d_Intersection):
    """
    None
    """
    def And_Domaine_Objet1_Intersections(self,TheImpTool : IntCurve_IConicTool,TheParCurve : IntCurve_PConic,TheImpCurveDomain : OCP.IntRes2d.IntRes2d_Domain,TheParCurveDomain : OCP.IntRes2d.IntRes2d_Domain,Inter2_And_Domain2 : OCP.TColStd.TColStd_Array1OfReal,Inter1 : OCP.TColStd.TColStd_Array1OfReal,Resultat1 : OCP.TColStd.TColStd_Array1OfReal,Resultat2 : OCP.TColStd.TColStd_Array1OfReal,EpsNul : float) -> Tuple[int]: 
        """
        None
        """
    def FindU(self,parameter : float,point : OCP.gp.gp_Pnt2d,TheParCurev : IntCurve_PConic,TheImpTool : IntCurve_IConicTool) -> float: 
        """
        None
        """
    def FindV(self,parameter : float,point : OCP.gp.gp_Pnt2d,TheImpTool : IntCurve_IConicTool,ParCurve : IntCurve_PConic,TheParCurveDomain : OCP.IntRes2d.IntRes2d_Domain,V0 : float,V1 : float,Tolerance : float) -> float: 
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
    def Perform(self,ITool : IntCurve_IConicTool,Dom1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : IntCurve_PConic,Dom2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: 
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,ITool : IntCurve_IConicTool,Dom1 : OCP.IntRes2d.IntRes2d_Domain,PCurve : IntCurve_PConic,Dom2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float) -> None: ...
    pass
class IntCurve_MyImpParToolOfIntImpConicParConic(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
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
    def __init__(self,IT : IntCurve_IConicTool,PC : IntCurve_PConic) -> None: ...
    pass
class IntCurve_PConic():
    """
    This class represents a conic from gp as a parametric curve ( in order to be used by the class PConicTool from IntCurve).
    """
    def Accuracy(self) -> int: 
        """
        None

        None
        """
    def Axis2(self) -> OCP.gp.gp_Ax22d: 
        """
        None

        None
        """
    def EpsX(self) -> float: 
        """
        None

        None
        """
    def Param1(self) -> float: 
        """
        None

        None
        """
    def Param2(self) -> float: 
        """
        None

        None
        """
    def SetAccuracy(self,Nb : int) -> None: 
        """
        Accuracy is the number of samples used to approximate the parametric curve on its domain.
        """
    def SetEpsX(self,EpsDist : float) -> None: 
        """
        EpsX is a internal tolerance used in math algorithms, usually about 1e-10 (See FunctionAllRoots for more details)
        """
    def TypeCurve(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        The Conics are manipulated as objects which only depend on three parameters : Axis and two Real from Standards. Type Curve is used to select the correct Conic.

        The Conics are manipulated as objects which only depend on three parameters : Axis and two Real from Standards. Type Curve is used to select the correct Conic.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Parab2d) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr2d) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d) -> None: ...
    @overload
    def __init__(self,PC : IntCurve_PConic) -> None: ...
    pass
class IntCurve_PConicTool():
    """
    Implementation of the ParTool from IntImpParGen for conics of gp, using the class PConic from IntCurve.
    """
    @staticmethod
    def D1_s(C : IntCurve_PConic,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    @staticmethod
    def D2_s(C : IntCurve_PConic,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d,N : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    @staticmethod
    def EpsX_s(C : IntCurve_PConic) -> float: 
        """
        None
        """
    @staticmethod
    @overload
    def NbSamples_s(C : IntCurve_PConic) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbSamples_s(C : IntCurve_PConic,U0 : float,U1 : float) -> int: ...
    @staticmethod
    def Value_s(C : IntCurve_PConic,X : float) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IntCurve_ProjectOnPConicTool():
    """
    This class provides a tool which computes the parameter of a point near a parametric conic.
    """
    @staticmethod
    @overload
    def FindParameter_s(C : IntCurve_PConic,Pnt : OCP.gp.gp_Pnt2d,Tol : float) -> float: 
        """
        Returns the parameter V of the point on the parametric curve corresponding to the Point Pnt. The Correspondence between Pnt and the point P(V) on the parametric curve must be coherent with the way of determination of the signed distance between a point and the implicit curve. Tol is the tolerance on the distance between a point and the parametrised curve. In that case, no bounds are given. The research of the right parameter has to be made on the natural parametric domain of the curve.

        Returns the parameter V of the point on the parametric curve corresponding to the Point Pnt. The Correspondence between Pnt and the point P(V) on the parametric curve must be coherent with the way of determination of the signed distance between a point and the implicit curve. Tol is the tolerance on the distance between a point and the parametrised curve. LowParameter and HighParameter give the boundaries of the interval in which the parameter certainly lies. These parameters are given to implement a more efficient algorithm. So, it is not necessary to check that the returned value verifies LowParameter <= Value <= HighParameter.
        """
    @staticmethod
    @overload
    def FindParameter_s(C : IntCurve_PConic,Pnt : OCP.gp.gp_Pnt2d,LowParameter : float,HighParameter : float,Tol : float) -> float: ...
    def __init__(self) -> None: ...
    pass
class Interval():
    """
    None
    """
    @property
    def Binf(self) -> float:
        """
        :type: float
        """
    @Binf.setter
    def Binf(self, arg0: float) -> None:
        pass
    @property
    def Bsup(self) -> float:
        """
        :type: float
        """
    @Bsup.setter
    def Bsup(self, arg0: float) -> None:
        pass
    @property
    def HasFirstBound(self) -> bool:
        """
        :type: bool
        """
    @HasFirstBound.setter
    def HasFirstBound(self, arg0: bool) -> None:
        pass
    @property
    def HasLastBound(self) -> bool:
        """
        :type: bool
        """
    @HasLastBound.setter
    def HasLastBound(self, arg0: bool) -> None:
        pass
    @property
    def IsNull(self) -> bool:
        """
        :type: bool
        """
    @IsNull.setter
    def IsNull(self, arg0: bool) -> None:
        pass
    pass
class PeriodicInterval():
    """
    None
    """
    def Complement(self) -> None: 
        """
        None
        """
    def IsNull(self) -> bool: 
        """
        None
        """
    def Length(self) -> float: 
        """
        None
        """
    def Normalize(self) -> None: 
        """
        None
        """
    def SetNull(self) -> None: 
        """
        None
        """
    def SetValues(self,a : float,b : float) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,a : float,b : float) -> None: ...
    @overload
    def __init__(self,Domain : OCP.IntRes2d.IntRes2d_Domain) -> None: ...
    @property
    def Binf(self) -> float:
        """
        :type: float
        """
    @Binf.setter
    def Binf(self, arg0: float) -> None:
        pass
    @property
    def Bsup(self) -> float:
        """
        :type: float
        """
    @Bsup.setter
    def Bsup(self, arg0: float) -> None:
        pass
    @property
    def isnull(self) -> bool:
        """
        :type: bool
        """
    @isnull.setter
    def isnull(self, arg0: bool) -> None:
        pass
    pass
