import OCP.LocalAnalysis
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import io
import OCP.GeomAbs
import OCP.Geom
import OCP.GeomLProp
import OCP.Geom2d
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
    def Dump_s(surfconti : LocalAnalysis_SurfaceContinuity,o : io.BytesIO) -> None: 
        """
        This class compute s and gives tools to check the local continuity between two points situated on 2 curves)

        This fonction gives informations about a variable SurfaceContinuity
        """
    @staticmethod
    @overload
    def Dump_s(curvconti : LocalAnalysis_CurveContinuity,o : io.BytesIO) -> None: ...
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
    LocalAnalysis_CurvatureNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined: 4>
    LocalAnalysis_NormalNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined: 3>
    LocalAnalysis_NullFirstDerivative: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative: 0>
    LocalAnalysis_NullSecondDerivative: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative: 1>
    LocalAnalysis_TangentNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined: 2>
    __entries: dict # value = {'LocalAnalysis_NullFirstDerivative': (<LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative: 0>, None), 'LocalAnalysis_NullSecondDerivative': (<LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative: 1>, None), 'LocalAnalysis_TangentNotDefined': (<LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined: 2>, None), 'LocalAnalysis_NormalNotDefined': (<LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined: 3>, None), 'LocalAnalysis_CurvatureNotDefined': (<LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined: 4>, None)}
    __members__: dict # value = {'LocalAnalysis_NullFirstDerivative': <LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative: 0>, 'LocalAnalysis_NullSecondDerivative': <LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative: 1>, 'LocalAnalysis_TangentNotDefined': <LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined: 2>, 'LocalAnalysis_NormalNotDefined': <LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined: 3>, 'LocalAnalysis_CurvatureNotDefined': <LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined: 4>}
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
    def __init__(self,EpsNul : float=0.001,EpsC0 : float=0.001,EpsC1 : float=0.001,EpsC2 : float=0.001,EpsG1 : float=0.001,Percent : float=0.01,Maxlen : float=10000.0) -> None: ...
    @overload
    def __init__(self,curv1 : OCP.Geom2d.Geom2d_Curve,curv2 : OCP.Geom2d.Geom2d_Curve,U : float,Surf1 : OCP.Geom.Geom_Surface,Surf2 : OCP.Geom.Geom_Surface,Order : OCP.GeomAbs.GeomAbs_Shape,EpsNul : float=0.001,EpsC0 : float=0.001,EpsC1 : float=0.001,EpsC2 : float=0.001,EpsG1 : float=0.001,Percent : float=0.01,Maxlen : float=10000.0) -> None: ...
    @overload
    def __init__(self,Surf1 : OCP.Geom.Geom_Surface,u1 : float,v1 : float,Surf2 : OCP.Geom.Geom_Surface,u2 : float,v2 : float,Order : OCP.GeomAbs.GeomAbs_Shape,EpsNul : float=0.001,EpsC0 : float=0.001,EpsC1 : float=0.001,EpsC2 : float=0.001,EpsG1 : float=0.001,Percent : float=0.01,Maxlen : float=10000.0) -> None: ...
    pass
LocalAnalysis_CurvatureNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_CurvatureNotDefined: 4>
LocalAnalysis_NormalNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_NormalNotDefined: 3>
LocalAnalysis_NullFirstDerivative: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_NullFirstDerivative: 0>
LocalAnalysis_NullSecondDerivative: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_NullSecondDerivative: 1>
LocalAnalysis_TangentNotDefined: OCP.LocalAnalysis.LocalAnalysis_StatusErrorType # value = <LocalAnalysis_StatusErrorType.LocalAnalysis_TangentNotDefined: 2>
