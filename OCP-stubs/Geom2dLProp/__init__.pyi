import OCP.Geom2dLProp
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom2d
import OCP.math
import OCP.LProp
import OCP.gp
__all__  = [
"Geom2dLProp_CLProps2d",
"Geom2dLProp_CurAndInf2d",
"Geom2dLProp_Curve2dTool",
"Geom2dLProp_FuncCurExt",
"Geom2dLProp_FuncCurNul",
"Geom2dLProp_NumericCurInf2d"
]
class Geom2dLProp_CLProps2d():
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
    def SetCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Initializes the local properties of the curve for the new curve.
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
    @overload
    def __init__(self,N : int,Resolution : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Curve,U : float,N : int,Resolution : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Curve,N : int,Resolution : float) -> None: ...
    pass
class Geom2dLProp_CurAndInf2d(OCP.LProp.LProp_CurAndInf):
    """
    An algorithm for computing local properties of a curve. These properties include: - the maximum and minimum curvatures - the inflection points. A CurAndInf2d object provides the framework for: - defining the curve to be analyzed - implementing the computation algorithms - consulting the results.
    """
    def AddExtCur(self,Param : float,IsMin : bool) -> None: 
        """
        None
        """
    def AddInflection(self,Param : float) -> None: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        True if the solutions are found.
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points. The Points are stored to increasing parameter.
        """
    def Parameter(self,N : int) -> float: 
        """
        Returns the parameter of the Nth point. raises if N not in the range [1,NbPoints()]
        """
    def Perform(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        For the curve C, Computes both the inflection points and the maximum and minimum curvatures.
        """
    def PerformCurExt(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        For the curve C, Computes the locals extremas of curvature.
        """
    def PerformInf(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        For the curve C, Computes the inflections. After computation, the following functions can be used: - IsDone to check if the computation was successful - NbPoints to obtain the number of computed particular points - Parameter to obtain the parameter on the curve for each particular point - Type to check if the point is an inflection point or an extremum of curvature of the curve C. Warning These functions can be used to analyze a series of curves, however it is necessary to clear the table of results between each computation.
        """
    def Type(self,N : int) -> OCP.LProp.LProp_CIType: 
        """
        Returns - MinCur if the Nth parameter corresponds to a minimum of the radius of curvature. - MaxCur if the Nth parameter corresponds to a maximum of the radius of curvature. - Inflection if the parameter corresponds to a point of inflection. raises if N not in the range [1,NbPoints()]
        """
    def __init__(self) -> None: ...
    pass
class Geom2dLProp_Curve2dTool():
    """
    None
    """
    @staticmethod
    def Continuity_s(C : OCP.Geom2d.Geom2d_Curve) -> int: 
        """
        returns the order of continuity of the curve <C>. returns 1 : first derivative only is computable returns 2 : first and second derivative only are computable. returns 3 : first, second and third are computable.
        """
    @staticmethod
    def D1_s(C : OCP.Geom2d.Geom2d_Curve,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        Computes the point <P> and first derivative <V1> of parameter <U> on the curve <C>.
        """
    @staticmethod
    def D2_s(C : OCP.Geom2d.Geom2d_Curve,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Computes the point <P>, the first derivative <V1> and second derivative <V2> of parameter <U> on the curve <C>.
        """
    @staticmethod
    def D3_s(C : OCP.Geom2d.Geom2d_Curve,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Computes the point <P>, the first derivative <V1>, the second derivative <V2> and third derivative <V3> of parameter <U> on the curve <C>.
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Geom2d.Geom2d_Curve) -> float: 
        """
        returns the first parameter bound of the curve.
        """
    @staticmethod
    def LastParameter_s(C : OCP.Geom2d.Geom2d_Curve) -> float: 
        """
        returns the last parameter bound of the curve. FirstParameter must be less than LastParameter.
        """
    @staticmethod
    def Value_s(C : OCP.Geom2d.Geom2d_Curve,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Computes the point <P> of parameter <U> on the curve <C>.
        """
    def __init__(self) -> None: ...
    pass
class Geom2dLProp_FuncCurExt(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    Function used to find the extremas of curvature in 2d.
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        Returns the derivative for the variable <X>.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def IsMinKC(self,Param : float) -> bool: 
        """
        True if Param corresponds to a minus of the radius of curvature.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Returns the value for the variable <X>.
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        Returns the value of the function and the derivative for the variable <X>.
        """
    def __init__(self,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> None: ...
    pass
class Geom2dLProp_FuncCurNul(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    Function used to find the inflections in 2d.
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        Returns the derivative for the variable <X>
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Returns the value for the variable <X>.
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        Returns the value of the function and the derivative for the variable <X>.
        """
    def __init__(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    pass
class Geom2dLProp_NumericCurInf2d():
    """
    Computes the locals extremas of curvature and the inflections of a bounded curve in 2d.
    """
    def IsDone(self) -> bool: 
        """
        True if the solutions are found.
        """
    @overload
    def PerformCurExt(self,C : OCP.Geom2d.Geom2d_Curve,Result : OCP.LProp.LProp_CurAndInf) -> None: 
        """
        Computes the locals extremas of curvature.

        Computes the locals extremas of curvature. in the interval of parmeters [UMin,UMax].
        """
    @overload
    def PerformCurExt(self,C : OCP.Geom2d.Geom2d_Curve,UMin : float,UMax : float,Result : OCP.LProp.LProp_CurAndInf) -> None: ...
    @overload
    def PerformInf(self,C : OCP.Geom2d.Geom2d_Curve,UMin : float,UMax : float,Result : OCP.LProp.LProp_CurAndInf) -> None: 
        """
        Computes the inflections.

        Computes the inflections in the interval of parmeters [UMin,UMax].
        """
    @overload
    def PerformInf(self,C : OCP.Geom2d.Geom2d_Curve,Result : OCP.LProp.LProp_CurAndInf) -> None: ...
    def __init__(self) -> None: ...
    pass
