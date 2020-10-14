import OCP.AdvApprox
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.GeomAbs
import OCP.TColgp
import OCP.PLib
__all__  = [
"AdvApprox_ApproxAFunction",
"AdvApprox_Cutting",
"AdvApprox_DichoCutting",
"AdvApprox_PrefAndRec",
"AdvApprox_PrefCutting",
"AdvApprox_SimpleApprox"
]
class AdvApprox_ApproxAFunction():
    """
    this approximate a given function
    """
    @staticmethod
    def Approximation_s(TotalDimension : int,TotalNumSS : int,LocalDimension : OCP.TColStd.TColStd_Array1OfInteger,First : float,Last : float,Evaluator : AdvApprox_EvaluatorFunction,CutTool : AdvApprox_Cutting,ContinuityOrder : int,NumMaxCoeffs : int,MaxSegments : int,TolerancesArray : OCP.TColStd.TColStd_Array1OfReal,code_precis : int,NumCoeffPerCurveArray : OCP.TColStd.TColStd_Array1OfInteger,LocalCoefficientArray : OCP.TColStd.TColStd_Array1OfReal,IntervalsArray : OCP.TColStd.TColStd_Array1OfReal,ErrorMaxArray : OCP.TColStd.TColStd_Array1OfReal,AverageErrorArray : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[int, int]: 
        """
        None
        """
    @overload
    def AverageError(self,Dimension : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns the error as is in the algorithms

        None
        """
    @overload
    def AverageError(self,Dimension : int,Index : int) -> float: ...
    def Degree(self) -> int: 
        """
        None

        None
        """
    def Dump(self,o : Any) -> None: 
        """
        diplay information on approximation.
        """
    def HasResult(self) -> bool: 
        """
        None

        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def Knots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None

        None
        """
    @overload
    def MaxError(self,Dimension : int,Index : int) -> float: 
        """
        returns the error as is in the algorithms

        None
        """
    @overload
    def MaxError(self,Dimension : int) -> OCP.TColStd.TColStd_HArray1OfReal: ...
    def Multiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None

        None
        """
    def NbKnots(self) -> int: 
        """
        None

        None
        """
    def NbPoles(self) -> int: 
        """
        as the name says
        """
    def NumSubSpaces(self,Dimension : int) -> int: 
        """
        None

        None
        """
    @overload
    def Poles(self,Index : int,P : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        -- returns the poles from the algorithms as is

        returns the poles at Index from the 3d subspace

        -- returns the poles from the algorithms as is
        """
    @overload
    def Poles(self) -> OCP.TColgp.TColgp_HArray2OfPnt: ...
    @overload
    def Poles1d(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        returns the poles from the algorithms as is

        returns the poles at Index from the 1d subspace

        returns the poles from the algorithms as is
        """
    @overload
    def Poles1d(self,Index : int,P : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Poles2d(self,Index : int,P : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        returns the poles from the algorithms as is

        returns the poles at Index from the 2d subspace

        returns the poles from the algorithms as is
        """
    @overload
    def Poles2d(self) -> OCP.TColgp.TColgp_HArray2OfPnt2d: ...
    @overload
    def __init__(self,Num1DSS : int,Num2DSS : int,Num3DSS : int,OneDTol : OCP.TColStd.TColStd_HArray1OfReal,TwoDTol : OCP.TColStd.TColStd_HArray1OfReal,ThreeDTol : OCP.TColStd.TColStd_HArray1OfReal,First : float,Last : float,Continuity : OCP.GeomAbs.GeomAbs_Shape,MaxDeg : int,MaxSeg : int,Func : AdvApprox_EvaluatorFunction,CutTool : AdvApprox_Cutting) -> None: ...
    @overload
    def __init__(self,Num1DSS : int,Num2DSS : int,Num3DSS : int,OneDTol : OCP.TColStd.TColStd_HArray1OfReal,TwoDTol : OCP.TColStd.TColStd_HArray1OfReal,ThreeDTol : OCP.TColStd.TColStd_HArray1OfReal,First : float,Last : float,Continuity : OCP.GeomAbs.GeomAbs_Shape,MaxDeg : int,MaxSeg : int,Func : AdvApprox_EvaluatorFunction) -> None: ...
    pass
class AdvApprox_Cutting():
    """
    to choose the way of cutting in approximation
    """
    def Value(self,a : float,b : float,cuttingvalue : float) -> bool: 
        """
        None
        """
    pass
class AdvApprox_DichoCutting(AdvApprox_Cutting):
    """
    if Cutting is necessary in [a,b], we cut at (a+b) / 2.
    """
    def Value(self,a : float,b : float,cuttingvalue : float) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class AdvApprox_PrefAndRec(AdvApprox_Cutting):
    """
    inherits class Cutting; contains a list of preferential points (pi)i and a list of Recommended points used in cutting management. if Cutting is necessary in [a,b], we cut at the di nearest from (a+b)/2
    """
    def Value(self,a : float,b : float,cuttingvalue : float) -> bool: 
        """
        cuting value is - the recommended point nerest of (a+b)/2 if pi is in ]a,b[ or else - the preferential point nearest of (a+b) / 2 if pi is in ](r*a+b)/(r+1) , (a+r*b)/(r+1)[ where r = Weight - or (a+b)/2 else.
        """
    def __init__(self,RecomendedCut : OCP.TColStd.TColStd_Array1OfReal,PrefferedCut : OCP.TColStd.TColStd_Array1OfReal,Weight : float=5.0) -> None: ...
    pass
class AdvApprox_PrefCutting(AdvApprox_Cutting):
    """
    inherits class Cutting; contains a list of preferential points (di)i if Cutting is necessary in [a,b], we cut at the di nearest from (a+b)/2.
    """
    def Value(self,a : float,b : float,cuttingvalue : float) -> bool: 
        """
        None
        """
    def __init__(self,CutPnts : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    pass
class AdvApprox_SimpleApprox():
    """
    Approximate a function on an intervall [First,Last] The result is a simple polynomial whose degree is as low as possible to satisfy the required tolerance and the maximum degree. The maximum error and the averrage error resulting from approximating the function by the polynomial are computed
    """
    def AverageError(self,Index : int) -> float: 
        """
        None
        """
    def Coefficients(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns the coefficients in the Jacobi Base
        """
    def Degree(self) -> int: 
        """
        None
        """
    def DifTab(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def Dump(self,o : Any) -> None: 
        """
        display information on approximation
        """
    def FirstConstr(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        returns the constraints at First
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastConstr(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        returns the constraints at Last
        """
    def MaxError(self,Index : int) -> float: 
        """
        None
        """
    def Perform(self,LocalDimension : OCP.TColStd.TColStd_Array1OfInteger,LocalTolerancesArray : OCP.TColStd.TColStd_Array1OfReal,First : float,Last : float,MaxDegree : int) -> None: 
        """
        Constructs approximator tool.
        """
    def SomTab(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def __init__(self,TotalDimension : int,TotalNumSS : int,Continuity : OCP.GeomAbs.GeomAbs_Shape,WorkDegree : int,NbGaussPoints : int,JacobiBase : OCP.PLib.PLib_JacobiPolynomial,Func : AdvApprox_EvaluatorFunction) -> None: ...
    pass
