import OCP.AppBlend
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColgp
import OCP.TColStd
__all__  = [
"AppBlend_Approx"
]
class AppBlend_Approx():
    """
    Bspline approximation of a surface.
    """
    def Curve2d(self,Index : int,TPoles : OCP.TColgp.TColgp_Array1OfPnt2d,TKnots : OCP.TColStd.TColStd_Array1OfReal,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def Curve2dPoles(self,Index : int) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        None
        """
    def Curves2dDegree(self) -> int: 
        """
        None
        """
    def Curves2dKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def Curves2dMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def Curves2dShape(self) -> Tuple[int, int, int]: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbCurves2d(self) -> int: 
        """
        None
        """
    def SurfPoles(self) -> OCP.TColgp.TColgp_Array2OfPnt: 
        """
        None
        """
    def SurfShape(self) -> Tuple[int, int, int, int, int, int]: 
        """
        None
        """
    def SurfUKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def SurfUMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def SurfVKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def SurfVMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def SurfWeights(self) -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        None
        """
    def Surface(self,TPoles : OCP.TColgp.TColgp_Array2OfPnt,TWeights : OCP.TColStd.TColStd_Array2OfReal,TUKnots : OCP.TColStd.TColStd_Array1OfReal,TVKnots : OCP.TColStd.TColStd_Array1OfReal,TUMults : OCP.TColStd.TColStd_Array1OfInteger,TVMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def TolCurveOnSurf(self,Index : int) -> float: 
        """
        None
        """
    def TolReached(self) -> Tuple[float, float]: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    pass
