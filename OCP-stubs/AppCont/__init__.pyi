import OCP.AppCont
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64

_Shape = Tuple[int, ...]
import OCP.TColgp
import OCP.AppParCurves

__all__ = ["AppCont_Function", "AppCont_LeastSquare", "PeriodicityInfo"]

class AppCont_Function:
    """
    Class describing a continous 3d and/or function f(u). This class must be provided by the user to use the approximation algorithm FittingCurve.
    """

    def D1(
        self,
        theU: float,
        theVec2d: OCP.TColgp.TColgp_Array1OfVec2d,
        theVec: OCP.TColgp.TColgp_Array1OfVec,
    ) -> bool:
        """
        Returns the derivative at parameter <theU>.
        """
    def FirstParameter(self) -> float:
        """
        Returns the first parameter of the function.
        """
    def GetNbOf2dPoints(self) -> int:
        """
        Get number of 2d points returned by "Value" and "D1" functions.
        """
    def GetNbOf3dPoints(self) -> int:
        """
        Get number of 3d points returned by "Value" and "D1" functions.
        """
    def GetNumberOfPoints(self) -> Tuple[int, int]:
        """
        Get number of 3d and 2d points returned by "Value" and "D1" functions.
        """
    def LastParameter(self) -> float:
        """
        Returns the last parameter of the function.
        """
    def Value(
        self,
        theU: float,
        thePnt2d: OCP.TColgp.TColgp_Array1OfPnt2d,
        thePnt: OCP.TColgp.TColgp_Array1OfPnt,
    ) -> bool:
        """
        Returns the point at parameter <theU>.
        """
    def __init__(self) -> None: ...
    pass

class AppCont_LeastSquare:
    """
    None
    """

    def Error(self) -> Tuple[float, float, float]:
        """
        None
        """
    def IsDone(self) -> bool:
        """
        None
        """
    def Value(self) -> OCP.AppParCurves.AppParCurves_MultiCurve:
        """
        None
        """
    def __init__(
        self,
        SSP: AppCont_Function,
        U0: float,
        U1: float,
        FirstCons: OCP.AppParCurves.AppParCurves_Constraint,
        LastCons: OCP.AppParCurves.AppParCurves_Constraint,
        Deg: int,
        NbPoints: int,
    ) -> None: ...
    pass

class PeriodicityInfo:
    """
    None
    """

    def __init__(self) -> None: ...
    @property
    def isPeriodic(self) -> bool:
        """
        :type: bool
        """
    @isPeriodic.setter
    def isPeriodic(self, arg0: bool) -> None:
        pass
    @property
    def myPeriod(self) -> float:
        """
        :type: float
        """
    @myPeriod.setter
    def myPeriod(self, arg0: float) -> None:
        pass
    pass
