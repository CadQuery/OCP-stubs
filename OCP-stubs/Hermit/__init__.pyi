import OCP.Hermit
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom2d
import OCP.Geom
__all__  = [
"Hermit"
]
class Hermit():
    """
    This is used to reparameterize Rational BSpline Curves so that we can concatenate them later to build C1 Curves It builds and 1D-reparameterizing function starting from an Hermite interpolation and adding knots and modifying poles of the 1D BSpline obtained that way. The goal is to build a(u) so that if we consider a BSpline curve N(u) f(u) = ----- D(u)
    """
    @staticmethod
    @overload
    def Solution_s(BS : OCP.Geom2d.Geom2d_BSplineCurve,TolPoles : float=1e-06,TolKnots : float=1e-06) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        returns the correct spline a(u) which will be multiplicated with BS later.

        returns the correct spline a(u) which will be multiplicated with BS later.
        """
    @staticmethod
    @overload
    def Solution_s(BS : OCP.Geom.Geom_BSplineCurve,TolPoles : float=1e-06,TolKnots : float=1e-06) -> OCP.Geom2d.Geom2d_BSplineCurve: ...
    @staticmethod
    def Solutionbis_s(BS : OCP.Geom.Geom_BSplineCurve,TolPoles : float=1e-06,TolKnots : float=1e-06) -> Tuple[float, float]: 
        """
        returns the knots to insert to a(u) to stay with a constant sign and in the tolerances.
        """
    def __init__(self) -> None: ...
    pass
