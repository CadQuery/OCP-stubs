import OCP.LocalAnalysis
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom2d
import OCP.GeomLProp
import OCP.Geom
import OCP.GeomAbs
__all__  = [
"LocalAnalysis",
"LocalAnalysis_CurveContinuity",
"LocalAnalysis_StatusErrorType",
"LocalAnalysis_SurfaceContinuity",
"LocalAnalysis_CurvatureNotDefined",
"LocalAnalysis_NormalNotDefined",
"LocalAnalysis_NullFirstDerivative",
"LocalAnalysis_NullSecondDerivative",
"LocalAnalysis_TangentNotDefined"
]
class LocalAnalysis():
    """
    This package gives tools to check the local continuity between two points situated on two curves or two surfaces.
    """
    @staticmethod
    @overload
    def Dump_s(curvconti : LocalAnalysis_CurveContinuity,o : Any) -> None: 
        """
        This class compute s and gives tools to check the local continuity between two points situated on 2 curves)

        This fonction gives informations about a variable SurfaceContinuity
        """
    @staticmethod
    @overload
    def Dump_s(surfconti : LocalAnalysis_SurfaceContinuity,o : Any) -> None: ...
    def __init__(self) -> None: ...
    pass
class LocalAnalysis_CurveContinuity():
    """
    This class gives tools to check local continuity C0 C1 C2 G1 G2 between two points situated on two curves
    """
    def C0Value(self) -> float: 
        """
        None
        """
    def C1Angle(self) -> float: 
        """
        None
        """
    def C1Ratio(self) -> float: 
        """
        None
        """
    def C2Angle(self) -> float: 
        """
        None
        """
    def C2Ratio(self) -> float: 
        """
        None
        """
    def ContinuityStatus(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def G1Angle(self) -> float: 
        """
        None
        """
    def G2Angle(self) -> float: 
        """
        None
        """
    def G2CurvatureVariation(self) -> float: 
        """
        None
        """
    def IsC0(self) -> bool: 
        """
        None
        """
    def IsC1(self) -> bool: 
        """
        None
        """
    def IsC2(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsG1(self) -> bool: 
        """
        None
        """
    def IsG2(self) -> bool: 
        """
        None
        """
    def StatusError(self) -> LocalAnalysis_StatusErrorType: 
        """
        None
        """
    def __init__(self,Curv1 : OCP.Geom.Geom_Curve,u1 : float,Curv2 : OCP.Geom.Geom_Curve,u2 : float,Order : OCP.GeomAbs.GeomAbs_Shape,EpsNul : float=0.001,EpsC0 : float=0.001,EpsC1 : float=0.001,EpsC2 : float=0.001,EpsG1 : float=0.001,EpsG2 : float=0.001,Percent : float=0.01,Maxlen : float=10000.0) -> None: ...
    pass
class LocalAnalysis_StatusErrorType():
    """
    None

    Members:

      LocalAnalysis_NullFirstDerivative

      LocalAnalysis_NullSecondDerivative

      LocalAnalysis_TangentNotDefined

      LocalAnalysis_NormalNotDefined

      LocalAnalysis_CurvatureNotDefined
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    LocalAnalysis_CurvatureNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined
    LocalAnalysis_NormalNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined
    LocalAnalysis_NullFirstDerivative: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative
    LocalAnalysis_NullSecondDerivative: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative
    LocalAnalysis_TangentNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined
    __entries: dict # value = {'LocalAnalysis_NullFirstDerivative': (LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative, None), 'LocalAnalysis_NullSecondDerivative': (LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative, None), 'LocalAnalysis_TangentNotDefined': (LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined, None), 'LocalAnalysis_NormalNotDefined': (LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined, None), 'LocalAnalysis_CurvatureNotDefined': (LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined, None)}
    __members__: dict # value = {'LocalAnalysis_NullFirstDerivative': LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative, 'LocalAnalysis_NullSecondDerivative': LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative, 'LocalAnalysis_TangentNotDefined': LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined, 'LocalAnalysis_NormalNotDefined': LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined, 'LocalAnalysis_CurvatureNotDefined': LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined}
    pass
class LocalAnalysis_SurfaceContinuity():
    """
    This class gives tools to check local continuity C0 C1 C2 G1 G2 between two points situated on two surfaces
    """
    def C0Value(self) -> float: 
        """
        None
        """
    def C1UAngle(self) -> float: 
        """
        None
        """
    def C1URatio(self) -> float: 
        """
        None
        """
    def C1VAngle(self) -> float: 
        """
        None
        """
    def C1VRatio(self) -> float: 
        """
        None
        """
    def C2UAngle(self) -> float: 
        """
        None
        """
    def C2URatio(self) -> float: 
        """
        None
        """
    def C2VAngle(self) -> float: 
        """
        None
        """
    def C2VRatio(self) -> float: 
        """
        None
        """
    def ComputeAnalysis(self,Surf1 : OCP.GeomLProp.GeomLProp_SLProps,Surf2 : OCP.GeomLProp.GeomLProp_SLProps,Order : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        None
        """
    def ContinuityStatus(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def G1Angle(self) -> float: 
        """
        None
        """
    def G2CurvatureGap(self) -> float: 
        """
        None
        """
    def IsC0(self) -> bool: 
        """
        None
        """
    def IsC1(self) -> bool: 
        """
        None
        """
    def IsC2(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsG1(self) -> bool: 
        """
        None
        """
    def IsG2(self) -> bool: 
        """
        None
        """
    def StatusError(self) -> LocalAnalysis_StatusErrorType: 
        """
        None
        """
    @overload
    def __init__(self,curv1 : OCP.Geom2d.Geom2d_Curve,curv2 : OCP.Geom2d.Geom2d_Curve,U : float,Surf1 : OCP.Geom.Geom_Surface,Surf2 : OCP.Geom.Geom_Surface,Order : OCP.GeomAbs.GeomAbs_Shape,EpsNul : float=0.001,EpsC0 : float=0.001,EpsC1 : float=0.001,EpsC2 : float=0.001,EpsG1 : float=0.001,Percent : float=0.01,Maxlen : float=10000.0) -> None: ...
    @overload
    def __init__(self,EpsNul : float=0.001,EpsC0 : float=0.001,EpsC1 : float=0.001,EpsC2 : float=0.001,EpsG1 : float=0.001,Percent : float=0.01,Maxlen : float=10000.0) -> None: ...
    @overload
    def __init__(self,Surf1 : OCP.Geom.Geom_Surface,u1 : float,v1 : float,Surf2 : OCP.Geom.Geom_Surface,u2 : float,v2 : float,Order : OCP.GeomAbs.GeomAbs_Shape,EpsNul : float=0.001,EpsC0 : float=0.001,EpsC1 : float=0.001,EpsC2 : float=0.001,EpsG1 : float=0.001,Percent : float=0.01,Maxlen : float=10000.0) -> None: ...
    pass
LocalAnalysis_CurvatureNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined
LocalAnalysis_NormalNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined
LocalAnalysis_NullFirstDerivative: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative
LocalAnalysis_NullSecondDerivative: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative
LocalAnalysis_TangentNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined
