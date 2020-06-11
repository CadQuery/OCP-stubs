import OCP.CPnts
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64

_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.Adaptor2d
import OCP.math
import OCP.gp

__all__ = [
    "CPnts_AbscissaPoint",
    "CPnts_MyGaussFunction",
    "CPnts_MyRootFunction",
    "CPnts_UniformDeflection",
]

class CPnts_AbscissaPoint:
    """
    the algorithm computes a point on a curve at a given distance from another point on the curve
    """

    def AdvPerform(
        self, Abscissa: float, U0: float, Ui: float, Resolution: float
    ) -> None:
        """
        Computes the point at the distance <Abscissa> of the curve; performs more appropriate tolerance managment; to use this method in right way it is necessary to call empty consructor. then call method Init with Tolerance = Resolution, then call AdvPermorm. U0 is the parameter of the point from which the distance is measured and Ui is the starting value for the iterative process (should be close to the final solution).
        """
    @overload
    def Init(self, C: OCP.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """
        Initializes the resolution function with <C>.

        Initializes the resolution function with <C>.

        Initializes the resolution function with <C>.

        Initializes the resolution function with <C>.

        Initializes the resolution function with <C> between U1 and U2.

        Initializes the resolution function with <C> between U1 and U2.

        Initializes the resolution function with <C> between U1 and U2.

        Initializes the resolution function with <C> between U1 and U2.
        """
    @overload
    def Init(self, C: OCP.Adaptor2d.Adaptor2d_Curve2d, Tol: float) -> None: ...
    @overload
    def Init(self, C: OCP.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float) -> None: ...
    @overload
    def Init(self, C: OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    @overload
    def Init(
        self, C: OCP.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float
    ) -> None: ...
    @overload
    def Init(
        self, C: OCP.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float, Tol: float
    ) -> None: ...
    @overload
    def Init(
        self, C: OCP.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, Tol: float
    ) -> None: ...
    @overload
    def Init(self, C: OCP.Adaptor3d.Adaptor3d_Curve, Tol: float) -> None: ...
    def IsDone(self) -> bool:
        """
        True if the computation was successful, False otherwise.

        True if the computation was successful, False otherwise.
        """
    @staticmethod
    @overload
    def Length_s(C: OCP.Adaptor3d.Adaptor3d_Curve) -> float:
        """
        Computes the length of the Curve <C>.

        Computes the length of the Curve <C>.

        Computes the length of the Curve <C> with the given tolerance.

        Computes the length of the Curve <C> with the given tolerance.

        Computes the length of the Curve <C> between <U1> and <U2>.

        Computes the length of the Curve <C> between <U1> and <U2>.

        Computes the length of the Curve <C> between <U1> and <U2> with the given tolerance.

        Computes the length of the Curve <C> between <U1> and <U2> with the given tolerance. creation of a indefinite AbscissaPoint.
        """
    @staticmethod
    @overload
    def Length_s(C: OCP.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float) -> float: ...
    @staticmethod
    @overload
    def Length_s(C: OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: ...
    @staticmethod
    @overload
    def Length_s(C: OCP.Adaptor3d.Adaptor3d_Curve, Tol: float) -> float: ...
    @staticmethod
    @overload
    def Length_s(
        C: OCP.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, Tol: float
    ) -> float: ...
    @staticmethod
    @overload
    def Length_s(C: OCP.Adaptor2d.Adaptor2d_Curve2d, Tol: float) -> float: ...
    @staticmethod
    @overload
    def Length_s(
        C: OCP.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float, Tol: float
    ) -> float: ...
    @staticmethod
    @overload
    def Length_s(C: OCP.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float) -> float: ...
    def Parameter(self) -> float:
        """
        Returns the parameter of the solution.

        Returns the parameter of the solution.
        """
    @overload
    def Perform(self, Abscissa: float, U0: float, Ui: float, Resolution: float) -> None:
        """
        Computes the point at the distance <Abscissa> of the curve. U0 is the parameter of the point from which the distance is measured.

        Computes the point at the distance <Abscissa> of the curve. U0 is the parameter of the point from which the distance is measured and Ui is the starting value for the iterative process (should be close to the final solution).
        """
    @overload
    def Perform(self, Abscissa: float, U0: float, Resolution: float) -> None: ...
    def SetParameter(self, P: float) -> None:
        """
        Enforce the solution, used by GCPnts.

        Enforce the solution, used by GCPnts.
        """
    @overload
    def __init__(
        self,
        C: OCP.Adaptor3d.Adaptor3d_Curve,
        Abscissa: float,
        U0: float,
        Resolution: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C: OCP.Adaptor2d.Adaptor2d_Curve2d,
        Abscissa: float,
        U0: float,
        Ui: float,
        Resolution: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C: OCP.Adaptor2d.Adaptor2d_Curve2d,
        Abscissa: float,
        U0: float,
        Resolution: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C: OCP.Adaptor3d.Adaptor3d_Curve,
        Abscissa: float,
        U0: float,
        Ui: float,
        Resolution: float,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass

class CPnts_MyGaussFunction(OCP.math.math_Function):
    """
    for implementation, compute values for Gauss
    """

    def GetStateNumber(self) -> int:
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self, X: float, F: float) -> bool:
        """
        None
        """
    def __init__(self) -> None: ...
    pass

class CPnts_MyRootFunction(
    OCP.math.math_FunctionWithDerivative, OCP.math.math_Function
):
    """
    Implements a function for the Newton algorithm to find the solution of Integral(F) = L (compute Length and Derivative of the curve for Newton)
    """

    def Derivative(self, X: float, Df: float) -> bool:
        """
        This is F(X,D)
        """
    def GetStateNumber(self) -> int:
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def Init(self, X0: float, L: float) -> None:
        """
        We want to solve Integral(X0,X,F(X,D)) = L

        We want to solve Integral(X0,X,F(X,D)) = L with given tolerance
        """
    @overload
    def Init(self, X0: float, L: float, Tol: float) -> None: ...
    def Value(self, X: float, F: float) -> bool:
        """
        This is Integral(X0,X,F(X,D)) - L
        """
    def Values(self, X: float, F: float, Df: float) -> bool:
        """
        None
        """
    def __init__(self) -> None: ...
    pass

class CPnts_UniformDeflection:
    """
    This class defines an algorithm to create a set of points (with a given chordal deviation) at the positions of constant deflection of a given parametrized curve or a trimmed circle. The continuity of the curve must be at least C2.
    """

    @overload
    def Initialize(
        self,
        C: OCP.Adaptor2d.Adaptor2d_Curve2d,
        Deflection: float,
        U1: float,
        U2: float,
        Resolution: float,
        WithControl: bool,
    ) -> None:
        """
        Initialize the algoritms with <C>, <Deflection>, <UStep>, <Resolution> and <WithControl>

        Initialize the algoritms with <C>, <Deflection>, <UStep>, <Resolution> and <WithControl>

        Initialize the algoritms with <C>, <Deflection>, <UStep>, <U1>, <U2> and <WithControl>

        Initialize the algoritms with <C>, <Deflection>, <UStep>, <U1>, <U2> and <WithControl>
        """
    @overload
    def Initialize(
        self,
        C: OCP.Adaptor3d.Adaptor3d_Curve,
        Deflection: float,
        Resolution: float,
        WithControl: bool,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        C: OCP.Adaptor2d.Adaptor2d_Curve2d,
        Deflection: float,
        Resolution: float,
        WithControl: bool,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        C: OCP.Adaptor3d.Adaptor3d_Curve,
        Deflection: float,
        U1: float,
        U2: float,
        Resolution: float,
        WithControl: bool,
    ) -> None: ...
    def IsAllDone(self) -> bool:
        """
        To know if all the calculus were done successfully (ie all the points have been computed). The calculus can fail if the Curve is not C1 in the considered domain. Returns True if the calculus was successful.

        To know if all the calculus were done successfully (ie all the points have been computed). The calculus can fail if the Curve is not C1 in the considered domain. Returns True if the calculus was successful.
        """
    def More(self) -> bool:
        """
        returns True if it exists a next Point.
        """
    def Next(self) -> None:
        """
        go to the next Point.

        go to the next Point.
        """
    def Point(self) -> OCP.gp.gp_Pnt:
        """
        return the computed parameter

        return the computed parameter
        """
    def Value(self) -> float:
        """
        return the computed parameter

        return the computed parameter
        """
    @overload
    def __init__(
        self,
        C: OCP.Adaptor3d.Adaptor3d_Curve,
        Deflection: float,
        Resolution: float,
        WithControl: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C: OCP.Adaptor3d.Adaptor3d_Curve,
        Deflection: float,
        U1: float,
        U2: float,
        Resolution: float,
        WithControl: bool,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        C: OCP.Adaptor2d.Adaptor2d_Curve2d,
        Deflection: float,
        U1: float,
        U2: float,
        Resolution: float,
        WithControl: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C: OCP.Adaptor2d.Adaptor2d_Curve2d,
        Deflection: float,
        Resolution: float,
        WithControl: bool,
    ) -> None: ...
    pass
