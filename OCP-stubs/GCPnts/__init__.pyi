import OCP.GCPnts
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.math
import OCP.Adaptor2d
import OCP.gp
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
"GCPnts_TCurveTypes_Adaptor2d_Curve2d",
"GCPnts_TCurveTypes_Adaptor3d_Curve",
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
    def Length_s(theC : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        Computes the length of the 3D Curve.

        Computes the length of the 2D Curve.

        Computes the length of the 3D Curve with the given tolerance.

        Computes the length of the 2D Curve with the given tolerance.

        Computes the length of the 3D Curve.

        Computes the length of the 2D Curve.

        Computes the length of the 3D Curve with the given tolerance.

        Computes the length of the Curve with the given tolerance.
        """
    @staticmethod
    @overload
    def Length_s(theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theU1 : float,theU2 : float,theTol : float) -> float: ...
    @staticmethod
    @overload
    def Length_s(theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theTol : float) -> float: ...
    @staticmethod
    @overload
    def Length_s(theC : OCP.Adaptor3d.Adaptor3d_Curve) -> float: ...
    @staticmethod
    @overload
    def Length_s(theC : OCP.Adaptor3d.Adaptor3d_Curve,theTol : float) -> float: ...
    @staticmethod
    @overload
    def Length_s(theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theU1 : float,theU2 : float) -> float: ...
    @staticmethod
    @overload
    def Length_s(theC : OCP.Adaptor3d.Adaptor3d_Curve,theU1 : float,theU2 : float) -> float: ...
    @staticmethod
    @overload
    def Length_s(theC : OCP.Adaptor3d.Adaptor3d_Curve,theU1 : float,theU2 : float,theTol : float) -> float: ...
    def Parameter(self) -> float: 
        """
        Returns the parameter on the curve of the point solution of this algorithm. Exceptions StdFail_NotDone if the computation was not successful, or was not done.
        """
    @overload
    def __init__(self,theTol : float,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAbscissa : float,theU0 : float) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAbscissa : float,theU0 : float) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAbscissa : float,theU0 : float,theUi : float) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAbscissa : float,theU0 : float,theUi : float,theTol : float) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAbscissa : float,theU0 : float) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAbscissa : float,theU0 : float,theUi : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theTol : float,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAbscissa : float,theU0 : float) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAbscissa : float,theU0 : float,theUi : float,theTol : float) -> None: ...
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
    def __index__(self) -> int: ...
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
    def __index__(self) -> int: ...
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
    Class to define function, which calculates square distance between point on curve C(u), U1 <= u <= U2 and line passing through points C(U1) and C(U2) This function is used in any minimization algorithm to define maximal deviation between curve and line, which required one variable function without derivative (for ex. math_BrentMinimum)
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
    This class provides an algorithm to compute a uniform abscissa distribution of points on a curve, i.e. a sequence of equidistant points. The distance between two consecutive points is measured along the curve.
    """
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theNbPoints : int) -> None: 
        """
        Initialize the algorithms with 3D curve and target number of points.

        Initialize the algorithms with 3D curve, target number of points and curve parameter range.

        Initialize the algorithms with 2D curve and target number of points.

        Initialize the algorithms with 2D curve, target number of points and curve parameter range.
        """
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theNbPoints : int) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theNbPoints : int,theU1 : float,theU2 : float) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theNbPoints : int,theU1 : float,theU2 : float) -> None: ...
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
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theNbPoints : int,theU1 : float,theU2 : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theNbPoints : int) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theNbPoints : int) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theNbPoints : int,theU1 : float,theU2 : float) -> None: ...
    pass
class GCPnts_QuasiUniformDeflection():
    """
    This class computes a distribution of points on a curve. The points may respect the deflection. The algorithm is not based on the classical prediction (with second derivative of curve), but either on the evaluation of the distance between the mid point and the point of mid parameter of the two points, or the distance between the mid point and the point at parameter 0.5 on the cubic interpolation of the two points and their tangents.
    """
    def Deflection(self) -> float: 
        """
        Returns the deflection between the curve and the polygon resulting from the points of the distribution computed by this algorithm. This is the value given to the algorithm at the time of construction (or initialization). Exceptions StdFail_NotDone if this algorithm has not been initialized, or if the computation was not successful.
        """
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theDeflection : float,theContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: 
        """
        Initialize the algorithms with 3D curve and deflection.

        Initialize the algorithms with 2D curve and deflection.

        Initialize the algorithms with 3D curve, deflection and parameter range.

        Initialize the algorithms with theC, theDeflection, theU1, theU2. This and the above algorithms initialize (or reinitialize) this algorithm and compute a distribution of points: - on the curve theC, or - on the part of curve theC limited by the two parameter values theU1 and theU2, where the deflection resulting from the distributed points is not greater than theDeflection.
        """
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theDeflection : float,theU1 : float,theU2 : float,theContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theU1 : float,theU2 : float,theContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
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
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theDeflection : float,theU1 : float,theU2 : float,theContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theU1 : float,theU2 : float,theContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theDeflection : float,theContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    pass
class GCPnts_TCurveTypes_Adaptor2d_Curve2d():
    """
    Auxiliary tool to resolve 2D curve classes.
    """
    def __init__(self) -> None: ...
    pass
class GCPnts_TCurveTypes_Adaptor3d_Curve():
    """
    Auxiliary tool to resolve 3D curve classes.
    """
    def __init__(self) -> None: ...
    pass
class GCPnts_TangentialDeflection():
    """
    Computes a set of points on a curve from package Adaptor3d such as between two successive points P1(u1)and P2(u2) : where P3 is the point of abscissa ((u1+u2)/2), with u1 the abscissa of the point P1 and u2 the abscissa of the point P2.
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
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theFirstParameter : float,theLastParameter : float,theAngularDeflection : float,theCurvatureDeflection : float,theMinimumOfPoints : int=2,theUTol : float=1e-09,theMinLen : float=1e-07) -> None: 
        """
        Initialize algorithm for 3D curve.

        Initialize algorithm for 3D curve with restricted range.

        Initialize algorithm for 2D curve.

        Initialize algorithm for 2D curve with restricted range.
        """
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAngularDeflection : float,theCurvatureDeflection : float,theMinimumOfPoints : int=2,theUTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theFirstParameter : float,theLastParameter : float,theAngularDeflection : float,theCurvatureDeflection : float,theMinimumOfPoints : int=2,theUTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAngularDeflection : float,theCurvatureDeflection : float,theMinimumOfPoints : int=2,theUTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
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
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theFirstParameter : float,theLastParameter : float,theAngularDeflection : float,theCurvatureDeflection : float,theMinimumOfPoints : int=2,theUTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAngularDeflection : float,theCurvatureDeflection : float,theMinimumOfPoints : int=2,theUTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theFirstParameter : float,theLastParameter : float,theAngularDeflection : float,theCurvatureDeflection : float,theMinimumOfPoints : int=2,theUTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAngularDeflection : float,theCurvatureDeflection : float,theMinimumOfPoints : int=2,theUTol : float=1e-09,theMinLen : float=1e-07) -> None: ...
    pass
class GCPnts_UniformAbscissa():
    """
    This class allows to compute a uniform distribution of points on a curve (i.e. the points will all be equally distant).
    """
    def Abscissa(self) -> float: 
        """
        Returns the current abscissa, i.e. the distance between two consecutive points.
        """
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAbscissa : float,theToler : float=-1.0) -> None: 
        """
        Initialize the algorithms with 3D curve, Abscissa, and Tolerance.

        Initialize the algorithms with 3D curve, Abscissa, Tolerance, and parameter range.

        Initialize the algorithms with 3D curve, number of points, and Tolerance.

        Initialize the algorithms with 3D curve, number of points, Tolerance, and parameter range.

        Initialize the algorithms with 2D curve, Abscissa, and Tolerance.

        Initialize the algorithms with 2D curve, Abscissa, Tolerance, and parameter range.

        Initialize the algorithms with 2D curve, number of points, and Tolerance.

        Initialize the algorithms with 2D curve, number of points, Tolerance, and parameter range.
        """
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theNbPoints : int,theU1 : float,theU2 : float,theToler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAbscissa : float,theU1 : float,theU2 : float,theToler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAbscissa : float,theU1 : float,theU2 : float,theToler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theNbPoints : int,theToler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theNbPoints : int,theU1 : float,theU2 : float,theToler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theNbPoints : int,theToler : float=-1.0) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAbscissa : float,theToler : float=-1.0) -> None: ...
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
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theNbPoints : int,theToler : float=-1.0) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theNbPoints : int,theU1 : float,theU2 : float,theToler : float=-1.0) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAbscissa : float,theToler : float=-1.0) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theAbscissa : float,theU1 : float,theU2 : float,theToler : float=-1.0) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAbscissa : float,theU1 : float,theU2 : float,theToler : float=-1.0) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theNbPoints : int,theToler : float=-1.0) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theAbscissa : float,theToler : float=-1.0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theNbPoints : int,theU1 : float,theU2 : float,theToler : float=-1.0) -> None: ...
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
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theWithControl : bool=True) -> None: 
        """
        Initialize the algorithms with 3D curve and deflection.

        Initialize the algorithms with 2D curve and deflection.

        Initialize the algorithms with 3D curve, deflection, parameter range.

        Initialize the algorithms with curve, deflection, parameter range. This and the above methods initialize (or reinitialize) this algorithm and compute a distribution of points: - on the curve theC, or - on the part of curve theC limited by the two parameter values theU1 and theU2, where the maximum distance between theC and the polygon that results from the points of the distribution is not greater than theDeflection. The first point of the distribution is either the origin of curve theC or the point of parameter theU1. The last point of the distribution is either the end point of curve theC or the point of parameter theU2. Intermediate points of the distribution are built using interpolations of segments of the curve limited at the 2nd degree. The construction ensures, in a first step, that the chordal deviation for this interpolation of the curve is less than or equal to theDeflection. However, it does not ensure that the chordal deviation for the curve itself is less than or equal to theDeflection. To do this a check is necessary, which may generate (second step) additional intermediate points. This check is time consuming, and can be avoided by setting theWithControl to false. Note that by default theWithControl is true and check is performed. Use the function IsDone to verify that the computation was successful, the function NbPoints() to obtain the number of points of the computed distribution, and the function Parameter to read the parameter of each point.
        """
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theDeflection : float,theU1 : float,theU2 : float,theWithControl : bool=True) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theDeflection : float,theWithControl : bool=True) -> None: ...
    @overload
    def Initialize(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theU1 : float,theU2 : float,theWithControl : bool=True) -> None: ...
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
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theDeflection : float,theU1 : float,theU2 : float,theWithControl : bool=True) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theU1 : float,theU2 : float,theWithControl : bool=True) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor2d.Adaptor2d_Curve2d,theDeflection : float,theWithControl : bool=True) -> None: ...
    @overload
    def __init__(self,theC : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theWithControl : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
GCPnts_AbsComposite: OCP.GCPnts.GCPnts_AbscissaType # value = <GCPnts_AbscissaType.GCPnts_AbsComposite: 2>
GCPnts_Circular: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_Circular: 1>
GCPnts_Curved: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_Curved: 2>
GCPnts_DefComposite: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_DefComposite: 3>
GCPnts_LengthParametrized: OCP.GCPnts.GCPnts_AbscissaType # value = <GCPnts_AbscissaType.GCPnts_LengthParametrized: 0>
GCPnts_Linear: OCP.GCPnts.GCPnts_DeflectionType # value = <GCPnts_DeflectionType.GCPnts_Linear: 0>
GCPnts_Parametrized: OCP.GCPnts.GCPnts_AbscissaType # value = <GCPnts_AbscissaType.GCPnts_Parametrized: 1>
