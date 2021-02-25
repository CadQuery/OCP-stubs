import OCP.GCPnts
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.gp
import OCP.math
import OCP.Adaptor2d
__all__  = [
"GCPnts_AbscissaPoint",
"GCPnts_AbscissaType",
"GCPnts_DeflectionType",
"GCPnts_DistFunction",
"GCPnts_DistFunction2d",
"GCPnts_DistFunction2dMV",
"GCPnts_DistFunctionMV",
"GCPnts_QuasiUniformAbscissa",
"GCPnts_QuasiUniformDeflection",
"GCPnts_TangentialDeflection",
"GCPnts_UniformAbscissa",
"GCPnts_UniformDeflection",
"GCPnts_AbsComposite",
"GCPnts_Circular",
"GCPnts_Curved",
"GCPnts_DefComposite",
"GCPnts_LengthParametrized",
"GCPnts_Linear",
"GCPnts_Parametrized"
]
class GCPnts_AbscissaPoint():
    """
    Provides an algorithm to compute a point on a curve situated at a given distance from another point on the curve, the distance being measured along the curve (curvilinear abscissa on the curve). This algorithm is also used to compute the length of a curve. An AbscissaPoint object provides a framework for: - defining the point to compute - implementing the construction algorithm - consulting the result.
    """
    def IsDone(self) -> bool: 
        """
        True if the computation was successful, False otherwise. IsDone is a protection against: - non-convergence of the algorithm - querying the results before computation.
        """
    @staticmethod
    @overload
    def Length_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float) -> float: 
        """
        Computes the length of the Curve <C>.

        Computes the length of the Curve <C>.

        Computes the length of the Curve <C> with the given tolerance.

        Computes the length of the Curve <C> with the given tolerance.

        Computes the length of the Curve <C>.

        Computes the length of the Curve <C>.

        Computes the length of the Curve <C> with the given tolerance.

        Computes the length of the Curve <C> with the given tolerance. Constructs an empty algorithm. This function is used only for initializing a framework to compute the length of a curve (or a series of curves). Warning The function IsDone will return the value false after the use of this function.
        """
    @staticmethod
    @overload
    def Length_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> float: ...
    @staticmethod
    @overload
    def Length_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: ...
    @staticmethod
    @overload
    def Length_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,Tol : float) -> float: ...
    @staticmethod
    @overload
    def Length_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U1 : float,U2 : float,Tol : float) -> float: ...
    @staticmethod
    @overload
    def Length_s(C : OCP.Adaptor3d.Adaptor3d_Curve,Tol : float) -> float: ...
    @staticmethod
    @overload
    def Length_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Tol : float) -> float: ...
    @staticmethod
    @overload
    def Length_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U1 : float,U2 : float) -> float: ...
    def Parameter(self) -> float: 
        """
        Returns the parameter on the curve of the point solution of this algorithm. Exceptions StdFail_NotDone if the computation was not successful, or was not done.
        """
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Abscissa : float,U0 : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Tol : float,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Abscissa : float,U0 : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Abscissa : float,U0 : float,Ui : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Abscissa : float,U0 : float,Ui : float,Tol : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Abscissa : float,U0 : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Abscissa : float,U0 : float,Ui : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Abscissa : float,U0 : float,Ui : float) -> None: ...
    @overload
    def __init__(self,Tol : float,C : OCP.Adaptor3d.Adaptor3d_Curve,Abscissa : float,U0 : float) -> None: ...
    pass
class GCPnts_AbscissaType():
    """
    None

    Members:

      GCPnts_LengthParametrized

      GCPnts_Parametrized

      GCPnts_AbsComposite
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __init__(self,value : int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self,other : object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self,state : int) -> None: ...
    @property
    def name(self) -> None:
        """
        :type: None
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    GCPnts_AbsComposite: OCP.GCPnts.GCPnts_AbscissaType # value = <GCPnts_AbscissaType.GCPnts_AbsComposite: 2>
    GCPnts_LengthParametrized: OCP.GCPnts.GCPnts_AbscissaType # value = <GCPnts_AbscissaType.GCPnts_LengthParametrized: 0>
    GCPnts_Parametrized: OCP.GCPnts.GCPnts_AbscissaType # value = <GCPnts_AbscissaType.GCPnts_Parametrized: 1>
    __entries: dict # value = {'GCPnts_LengthParametrized': (<GCPnts_AbscissaType.GCPnts_LengthParametrized: 0>, None), 'GCPnts_Parametrized': (<GCPnts_AbscissaType.GCPnts_Parametrized: 1>, None), 'GCPnts_AbsComposite': (<GCPnts_AbscissaType.GCPnts_AbsComposite: 2>, None)}
    __members__: dict # value = {'GCPnts_LengthParametrized': <GCPnts_AbscissaType.GCPnts_LengthParametrized: 0>, 'GCPnts_Parametrized': <GCPnts_AbscissaType.GCPnts_Parametrized: 1>, 'GCPnts_AbsComposite': <GCPnts_AbscissaType.GCPnts_AbsComposite: 2>}
    pass
class GCPnts_DeflectionType():
    """
    None

    Members:

      GCPnts_Linear

      GCPnts_Circular

      GCPnts_Curved

      GCPnts_DefComposite
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __init__(self,value : int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self,other : object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self,state : int) -> None: ...
    @property
    def name(self) -> None:
        """
        :type: None
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    GCPnts_Circular: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_Circular: 1>
    GCPnts_Curved: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_Curved: 2>
    GCPnts_DefComposite: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_DefComposite: 3>
    GCPnts_Linear: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_Linear: 0>
    __entries: dict # value = {'GCPnts_Linear': (<GCPnts_DeflectionType.GCPnts_Linear: 0>, None), 'GCPnts_Circular': (<GCPnts_DeflectionType.GCPnts_Circular: 1>, None), 'GCPnts_Curved': (<GCPnts_DeflectionType.GCPnts_Curved: 2>, None), 'GCPnts_DefComposite': (<GCPnts_DeflectionType.GCPnts_DefComposite: 3>, None)}
    __members__: dict # value = {'GCPnts_Linear': <GCPnts_DeflectionType.GCPnts_Linear: 0>, 'GCPnts_Circular': <GCPnts_DeflectionType.GCPnts_Circular: 1>, 'GCPnts_Curved': <GCPnts_DeflectionType.GCPnts_Curved: 2>, 'GCPnts_DefComposite': <GCPnts_DeflectionType.GCPnts_DefComposite: 3>}
    pass
class GCPnts_DistFunction(OCP.math.math_Function):
    """
    Class to define function, which calculates square distance between point on curve C(u), U1 <= u <= U2 and line passing through points C(U1) and C(U2) This function is used in any minimisation algorithm to define maximal deviation between curve and line, which required one variable function without derivative (for ex. math_BrentMinimum)
    """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        None
        """
    def __init__(self,theCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float) -> None: ...
    pass
class GCPnts_DistFunction2d(OCP.math.math_Function):
    """
    Class to define function, which calculates square distance between point on curve C(u), U1 <= u <= U2 and line passing through points C(U1) and C(U2) This function is used in any minimisation algorithm to define maximal deviation between curve and line, which required one variable function without derivative (for ex. math_BrentMinimum)
    """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        None
        """
    def __init__(self,theCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,U1 : float,U2 : float) -> None: ...
    pass
class GCPnts_DistFunction2dMV(OCP.math.math_MultipleVarFunction):
    """
    The same as class GCPnts_DistFunction2d, but it can be used in minimization algorithms that requires multi variable function
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : float) -> bool: 
        """
        None
        """
    def __init__(self,theCurvLinDist : GCPnts_DistFunction2d) -> None: ...
    pass
class GCPnts_DistFunctionMV(OCP.math.math_MultipleVarFunction):
    """
    The same as class GCPnts_DistFunction, but it can be used in minimization algorithms that requires multi variable function
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : float) -> bool: 
        """
        None
        """
    def __init__(self,theCurvLinDist : GCPnts_DistFunction) -> None: ...
    pass
class GCPnts_QuasiUniformAbscissa():
    """
    This class provides an algorithm to compute a uniform abscissa distribution of points on a curve, i.e. a sequence of equidistant points. The distance between two consecutive points is measured along the curve. The distribution is defined: - either by the curvilinear distance between two consecutive points - or by a number of points.
    """
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbPoints : int,U1 : float,U2 : float) -> None: 
        """
        Initialize the algoritms with <C>, <NbPoints> and

        Initialize the algoritms with <C>, <Abscissa>, <U1>, <U2>.

        Initialize the algoritms with <C>, <NbPoints> and

        Initialize the algoritms with <C>, <Abscissa>, <U1>, <U2>.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbPoints : int) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbPoints : int) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbPoints : int,U1 : float,U2 : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the computation was successful. IsDone is a protection against: - non-convergence of the algorithm - querying the results before computation.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points of the distribution computed by this algorithm. This value is either: - the one imposed on the algorithm at the time of construction (or initialization), or - the one computed by the algorithm when the curvilinear distance between two consecutive points of the distribution is imposed on the algorithm at the time of construction (or initialization). Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    def Parameter(self,Index : int) -> float: 
        """
        Returns the parameter of the point of index Index in the distribution computed by this algorithm. Warning Index must be greater than or equal to 1, and less than or equal to the number of points of the distribution. However, pay particular attention as this condition is not checked by this function. Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbPoints : int) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbPoints : int,U1 : float,U2 : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbPoints : int) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbPoints : int,U1 : float,U2 : float) -> None: ...
    pass
class GCPnts_QuasiUniformDeflection():
    """
    This class computes a distribution of points on a curve. The points may respect the deflection. The algorithm is not based on the classical prediction (with second derivative of curve), but either on the evaluation of the distance between the mid point and the point of mid parameter of the two points, or the distance between the mid point and the point at parameter 0.5 on the cubic interpolation of the two points and their tangents. Note: this algorithm is faster than a GCPnts_UniformDeflection algorithm, and is able to work with non-"C2" continuous curves. However, it generates more points in the distribution.
    """
    def Deflection(self) -> float: 
        """
        Returns the deflection between the curve and the polygon resulting from the points of the distribution computed by this algorithm. This is the value given to the algorithm at the time of construction (or initialization). Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Deflection : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: 
        """
        Initialize the algoritms with <C>, <Deflection>

        Initialize the algoritms with <C>, <Deflection>

        Initialize the algoritms with <C>, <Deflection>, <U1>,<U2>

        Initialize the algoritms with <C>, <Deflection>, -- <U1>,<U2> This and the above algorithms initialize (or reinitialize) this algorithm and compute a distribution of points: - on the curve C, or - on the part of curve C limited by the two parameter values U1 and U2, where the deflection resulting from the distributed points is not greater than Deflection. The first point of the distribution is either the origin of curve C or the point of parameter U1. The last point of the distribution is either the end point of curve C or the point of parameter U2. Intermediate points of the distribution are built in such a way that the deflection is not greater than Deflection. Using the following evaluation of the deflection: if Pi and Pj are two consecutive points of the distribution, respectively of parameter ui and uj on the curve, the deflection is the distance between: - the mid-point of Pi and Pj (the center of the chord joining these two points) - and the point of mid-parameter of these two points (the point of parameter [(ui+uj) / 2 ] on curve C). Continuity, defaulted to GeomAbs_C1, gives the degree of continuity of the curve C. (Note that C is an Adaptor3d_Curve or an Adaptor2d_Curve2d object, and does not know the degree of continuity of the underlying curve). Use the function IsDone to verify that the computation was successful, the function NbPoints to obtain the number of points of the computed distribution, and the function Parameter to read the parameter of each point. Warning - The roles of U1 and U2 are inverted if U1 > U2. - Derivative functions on the curve are called according to Continuity. An error may occur if Continuity is greater than the real degree of continuity of the curve. Warning C is an adapted curve, i.e. an object which is an interface between: - the services provided by either a 2D curve from the package Geom2d (in the case of an Adaptor2d_Curve2d curve) or a 3D curve from the package Geom (in the case of an Adaptor3d_Curve curve), and those required on the curve by the computation algorithm.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Deflection : float,U1 : float,U2 : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Deflection : float,U1 : float,U2 : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Deflection : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the computation was successful. IsDone is a protection against: - non-convergence of the algorithm - querying the results before computation.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points of the distribution computed by this algorithm. Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    def Parameter(self,Index : int) -> float: 
        """
        Returns the parameter of the point of index Index in the distribution computed by this algorithm. Warning Index must be greater than or equal to 1, and less than or equal to the number of points of the distribution. However, pay particular attention as this condition is not checked by this function. Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    def Value(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the point of index Index in the distribution computed by this algorithm. Warning Index must be greater than or equal to 1, and less than or equal to the number of points of the distribution. However, pay particular attention as this condition is not checked by this function. Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Deflection : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Deflection : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Deflection : float,U1 : float,U2 : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Deflection : float,U1 : float,U2 : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    pass
class GCPnts_TangentialDeflection():
    """
    Computes a set of points on a curve from package Adaptor3d such as between two successive points P1(u1)and P2(u2) :
    """
    def AddPoint(self,thePnt : OCP.gp.gp_Pnt,theParam : float,theIsReplace : bool=True) -> int: 
        """
        Add point to already calculated points (or replace existing) Returns index of new added point or founded with parametric tolerance (replaced if theIsReplace is true)
        """
    @staticmethod
    def ArcAngularStep_s(theRadius : float,theLinearDeflection : float,theAngularDeflection : float,theMinLength : float) -> float: 
        """
        Computes angular step for the arc using the given parameters.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,FirstParameter : float,LastParameter : float,AngularDeflection : float,CurvatureDeflection : float,MinimumOfPoints : int=2,UTol : float=1e-09,theMinLen : float=1e-07) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,FirstParameter : float,LastParameter : float,AngularDeflection : float,CurvatureDeflection : float,MinimumOfPoints : int=2,UTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,AngularDeflection : float,CurvatureDeflection : float,MinimumOfPoints : int=2,UTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,AngularDeflection : float,CurvatureDeflection : float,MinimumOfPoints : int=2,UTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    def NbPoints(self) -> int: 
        """
        None
        """
    def Parameter(self,I : int) -> float: 
        """
        None
        """
    def Value(self,I : int) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,FirstParameter : float,LastParameter : float,AngularDeflection : float,CurvatureDeflection : float,MinimumOfPoints : int=2,UTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,AngularDeflection : float,CurvatureDeflection : float,MinimumOfPoints : int=2,UTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,FirstParameter : float,LastParameter : float,AngularDeflection : float,CurvatureDeflection : float,MinimumOfPoints : int=2,UTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,AngularDeflection : float,CurvatureDeflection : float,MinimumOfPoints : int=2,UTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    pass
class GCPnts_UniformAbscissa():
    """
    This class allows to compute a uniform distribution of points on a curve (ie the points will all be equally distant).
    """
    def Abscissa(self) -> float: 
        """
        returne the current abscissa ie the distance between two consecutive points
        """
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Abscissa : float,Toler : float=-1.0) -> None: 
        """
        Initialize the algoritms with <C>, <Abscissa>, <Toler>

        Initialize the algoritms with <C>, <Abscissa>, <U1>, <U2>, <Toler>

        Initialize the algoritms with <C>, <NbPoints>, <Toler> and

        Initialize the algoritms with <C>, <Abscissa>, <U1>, <U2>, <Toler>.

        Initialize the algoritms with <C>, <Abscissa>, <Toler>

        Initialize the algoritms with <C>, <Abscissa>, <U1>, <U2>, <Toler>

        Initialize the algoritms with <C>, <NbPoints>, <Toler> and

        Initialize the algoritms with <C>, <Abscissa>, <U1>, <U2>, <Toler>.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Abscissa : float,Toler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbPoints : int,Toler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbPoints : int,Toler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Abscissa : float,U1 : float,U2 : float,Toler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbPoints : int,U1 : float,U2 : float,Toler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbPoints : int,U1 : float,U2 : float,Toler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Abscissa : float,U1 : float,U2 : float,Toler : float=-1.0) -> None: ...
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        None
        """
    def Parameter(self,Index : int) -> float: 
        """
        returns the computed Parameter of index <Index>.
        """
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbPoints : int,U1 : float,U2 : float,Toler : float=-1.0) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbPoints : int,Toler : float=-1.0) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbPoints : int,Toler : float=-1.0) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbPoints : int,U1 : float,U2 : float,Toler : float=-1.0) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Abscissa : float,Toler : float=-1.0) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Abscissa : float,Toler : float=-1.0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Abscissa : float,U1 : float,U2 : float,Toler : float=-1.0) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Abscissa : float,U1 : float,U2 : float,Toler : float=-1.0) -> None: ...
    pass
class GCPnts_UniformDeflection():
    """
    Provides an algorithm to compute a distribution of points on a 'C2' continuous curve. The algorithm respects a criterion of maximum deflection between the curve and the polygon that results from the computed points. Note: This algorithm is relatively time consuming. A GCPnts_QuasiUniformDeflection algorithm is quicker; it can also work with non-'C2' continuous curves, but it generates more points in the distribution.
    """
    def Deflection(self) -> float: 
        """
        Returns the deflection between the curve and the polygon resulting from the points of the distribution computed by this algorithm. This value is the one given to the algorithm at the time of construction (or initialization). Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Deflection : float,WithControl : bool=True) -> None: 
        """
        Initialize the algoritms with <C>, <Deflection>

        Initialize the algoritms with <C>, <Deflection>

        Initialize the algoritms with <C>, <Deflection>, <U1>,<U2>

        Initialize the algoritms with <C>, <Deflection>, <U1>,<U2> This and the above methods initialize (or reinitialize) this algorithm and compute a distribution of points: - on the curve C, or - on the part of curve C limited by the two parameter values U1 and U2, where the maximum distance between C and the polygon that results from the points of the distribution is not greater than Deflection. The first point of the distribution is either the origin of curve C or the point of parameter U1. The last point of the distribution is either the end point of curve C or the point of parameter U2. Intermediate points of the distribution are built using interpolations of segments of the curve limited at the 2nd degree. The construction ensures, in a first step, that the chordal deviation for this interpolation of the curve is less than or equal to Deflection. However, it does not ensure that the chordal deviation for the curve itself is less than or equal to Deflection. To do this a check is necessary, which may generate (second step) additional intermediate points. This check is time consuming, and can be avoided by setting WithControl to false. Note that by default WithControl is true and check is performed. Use the function IsDone to verify that the computation was successful, the function NbPoints to obtain the number of points of the computed distribution, and the function Parameter to read the parameter of each point. Warning - C is necessary, 'C2' continuous. This property is not checked at construction time. - The roles of U1 and U2 are inverted if U1 > U2. Warning C is an adapted curve, i.e. an object which is an interface between: - the services provided by either a 2D curve from the package Geom2d (in the case of an Adaptor2d_Curve2d curve) or a 3D curve from the package Geom (in the case of an Adaptor3d_Curve curve), - and those required on the curve by the computation algorithm.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Deflection : float,U1 : float,U2 : float,WithControl : bool=True) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Deflection : float,U1 : float,U2 : float,WithControl : bool=True) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Deflection : float,WithControl : bool=True) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the computation was successful. IsDone is a protection against: - non-convergence of the algorithm - querying the results before computation.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points of the distribution computed by this algorithm. Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    def Parameter(self,Index : int) -> float: 
        """
        Returns the parameter of the point of index Index in the distribution computed by this algorithm. Warning Index must be greater than or equal to 1, and less than or equal to the number of points of the distribution. However, pay particular attention as this condition is not checked by this function. Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    def Value(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the point of index Index in the distribution computed by this algorithm. Warning Index must be greater than or equal to 1, and less than or equal to the number of points of the distribution. However, pay particular attention as this condition is not checked by this function. Exceptions StdFAil_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Deflection : float,U1 : float,U2 : float,WithControl : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Deflection : float,WithControl : bool=True) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Deflection : float,WithControl : bool=True) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Deflection : float,U1 : float,U2 : float,WithControl : bool=True) -> None: ...
    pass
GCPnts_AbsComposite: OCP.GCPnts.GCPnts_AbscissaType # value = <GCPnts_AbscissaType.GCPnts_AbsComposite: 2>
GCPnts_Circular: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_Circular: 1>
GCPnts_Curved: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_Curved: 2>
GCPnts_DefComposite: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_DefComposite: 3>
GCPnts_LengthParametrized: OCP.GCPnts.GCPnts_AbscissaType # value = <GCPnts_AbscissaType.GCPnts_LengthParametrized: 0>
GCPnts_Linear: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_Linear: 0>
GCPnts_Parametrized: OCP.GCPnts.GCPnts_AbscissaType # value = <GCPnts_AbscissaType.GCPnts_Parametrized: 1>
