import OCP.BSplCLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.GeomAbs
import OCP.TColgp
import OCP.math
import OCP.gp
import OCP.Standard
import OCP.TColStd
__all__  = [
"BSplCLib",
"BSplCLib_Cache",
"BSplCLib_CacheParams",
"BSplCLib_EvaluatorFunction",
"BSplCLib_KnotDistribution",
"BSplCLib_MultDistribution",
"BSplCLib_Constant",
"BSplCLib_NonConstant",
"BSplCLib_NonUniform",
"BSplCLib_QuasiConstant",
"BSplCLib_Uniform"
]
class BSplCLib():
    """
    BSplCLib B-spline curve Library.
    """
    @staticmethod
    def AntiBoorScheme_s(U : float,Degree : int,Knots : float,Dimension : int,Poles : float,Depth : int,Length : int,Tolerance : float) -> bool: 
        """
        Compute the content of Pole before the BoorScheme. This method is used to remove poles.
        """
    @staticmethod
    def Bohm_s(U : float,Degree : int,N : int,Dimension : int) -> Tuple[float, float]: 
        """
        Performs the Bohm Algorithm at parameter <U>. This algorithm computes the value and all the derivatives up to order N (N <= Degree).
        """
    @staticmethod
    def BoorIndex_s(Index : int,Length : int,Depth : int) -> int: 
        """
        Returns the index in the Boor result array of the poles <Index>. If the Boor algorithm was perform with <Length> and <Depth>.
        """
    @staticmethod
    def BoorScheme_s(U : float,Degree : int,Dimension : int,Depth : int,Length : int) -> Tuple[float, float]: 
        """
        Performs the Boor Algorithm at parameter <U> with the given <Degree> and the array of <Knots> on the poles <Poles> of dimension <Dimension>. The schema is computed until level <Depth> on a basis of <Length+1> poles.
        """
    @staticmethod
    def BuildBSpMatrix_s(Parameters : OCP.TColStd.TColStd_Array1OfReal,OrderArray : OCP.TColStd.TColStd_Array1OfInteger,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Degree : int,Matrix : OCP.math.math_Matrix,UpperBandWidth : int,LowerBandWidth : int) -> int: 
        """
        This Builds a fully blown Matrix of (ni) Bi (tj)
        """
    @staticmethod
    def BuildBoor_s(Index : int,Length : int,Dimension : int,Poles : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float]: 
        """
        Copy in <LP> poles for <Dimension> Boor scheme. Starting from <Index> * <Dimension>, copy <Length+1> poles.
        """
    @staticmethod
    @overload
    def BuildCache_s(theParameter : float,theSpanDomain : float,thePeriodicFlag : bool,theDegree : int,theSpanIndex : int,theFlatKnots : OCP.TColStd.TColStd_Array1OfReal,thePoles : OCP.TColgp.TColgp_Array1OfPnt,theWeights : OCP.TColStd.TColStd_Array1OfReal,theCacheArray : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        Perform the evaluation of the Taylor expansion of the Bspline normalized between 0 and 1. If rational computes the homogeneous Taylor expension for the numerator and stores it in CachePoles

        Perform the evaluation of the Taylor expansion of the Bspline normalized between 0 and 1. If rational computes the homogeneous Taylor expension for the numerator and stores it in CachePoles

        Perform the evaluation of the Taylor expansion of the Bspline normalized between 0 and 1. Structure of result optimized for BSplCLib_Cache.

        Perform the evaluation of the Taylor expansion of the Bspline normalized between 0 and 1. Structure of result optimized for BSplCLib_Cache.
        """
    @staticmethod
    @overload
    def BuildCache_s(U : float,InverseOfSpanDomain : float,PeriodicFlag : bool,Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,CachePoles : OCP.TColgp.TColgp_Array1OfPnt2d,CacheWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def BuildCache_s(theParameter : float,theSpanDomain : float,thePeriodicFlag : bool,theDegree : int,theSpanIndex : int,theFlatKnots : OCP.TColStd.TColStd_Array1OfReal,thePoles : OCP.TColgp.TColgp_Array1OfPnt2d,theWeights : OCP.TColStd.TColStd_Array1OfReal,theCacheArray : OCP.TColStd.TColStd_Array2OfReal) -> None: ...
    @staticmethod
    @overload
    def BuildCache_s(U : float,InverseOfSpanDomain : float,PeriodicFlag : bool,Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,CachePoles : OCP.TColgp.TColgp_Array1OfPnt,CacheWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def BuildEval_s(Degree : int,Index : int,Poles : OCP.TColStd.TColStd_Array1OfReal,Weights : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float]: 
        """
        None

        None

        Copy in <LP> the poles and weights for the Eval scheme. starting from Poles(Poles.Lower()+Index)
        """
    @staticmethod
    @overload
    def BuildEval_s(Degree : int,Index : int,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float]: ...
    @staticmethod
    @overload
    def BuildEval_s(Degree : int,Index : int,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float]: ...
    @staticmethod
    def BuildKnots_s(Degree : int,Index : int,Periodic : bool,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> Tuple[float]: 
        """
        Stores in LK the useful knots for the BoorSchem on the span Knots(Index) - Knots(Index+1)
        """
    @staticmethod
    def BuildSchoenbergPoints_s(Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Parameters : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        builds the Schoenberg points from the flat knot used to interpolate a BSpline since the BSpline matrix is invertible.
        """
    @staticmethod
    @overload
    def CacheD0_s(U : float,Degree : int,CacheParameter : float,SpanLenght : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt2d) -> None: 
        """
        Perform the evaluation of the of the cache the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights this just evaluates the current point the CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effects

        Perform the evaluation of the Bspline Basis and then multiplies by the weights this just evaluates the current point the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights ththe CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effectsis just evaluates the current point
        """
    @staticmethod
    @overload
    def CacheD0_s(U : float,Degree : int,CacheParameter : float,SpanLenght : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def CacheD1_s(U : float,Degree : int,CacheParameter : float,SpanLenght : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt2d,Vec : OCP.gp.gp_Vec2d) -> None: 
        """
        Perform the evaluation of the of the cache the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights this just evaluates the current point the CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effects

        Perform the evaluation of the Bspline Basis and then multiplies by the weights this just evaluates the current point the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights ththe CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effectsis just evaluates the current point
        """
    @staticmethod
    @overload
    def CacheD1_s(U : float,Degree : int,CacheParameter : float,SpanLenght : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt,Vec : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def CacheD2_s(U : float,Degree : int,CacheParameter : float,SpanLenght : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt,Vec1 : OCP.gp.gp_Vec,Vec2 : OCP.gp.gp_Vec) -> None: 
        """
        Perform the evaluation of the of the cache the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights this just evaluates the current point the CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effects

        Perform the evaluation of the Bspline Basis and then multiplies by the weights this just evaluates the current point the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights ththe CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effectsis just evaluates the current point
        """
    @staticmethod
    @overload
    def CacheD2_s(U : float,Degree : int,CacheParameter : float,SpanLenght : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt2d,Vec1 : OCP.gp.gp_Vec2d,Vec2 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def CacheD3_s(U : float,Degree : int,CacheParameter : float,SpanLenght : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt2d,Vec1 : OCP.gp.gp_Vec2d,Vec2 : OCP.gp.gp_Vec2d,Vec3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Perform the evaluation of the of the cache the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights this just evaluates the current point the CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effects

        Perform the evaluation of the Bspline Basis and then multiplies by the weights this just evaluates the current point the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights ththe CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effectsis just evaluates the current point
        """
    @staticmethod
    @overload
    def CacheD3_s(U : float,Degree : int,CacheParameter : float,SpanLenght : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt,Vec1 : OCP.gp.gp_Vec,Vec2 : OCP.gp.gp_Vec,Vec3 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def CoefsD0_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt2d) -> None: 
        """
        Calls CacheD0 for Bezier Curves Arrays computed with the method PolesCoefficients. Warning: To be used for Beziercurves ONLY!!!

        Calls CacheD0 for Bezier Curves Arrays computed with the method PolesCoefficients. Warning: To be used for Beziercurves ONLY!!!
        """
    @staticmethod
    @overload
    def CoefsD0_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def CoefsD1_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt,Vec : OCP.gp.gp_Vec) -> None: 
        """
        Calls CacheD1 for Bezier Curves Arrays computed with the method PolesCoefficients. Warning: To be used for Beziercurves ONLY!!!

        Calls CacheD1 for Bezier Curves Arrays computed with the method PolesCoefficients. Warning: To be used for Beziercurves ONLY!!!
        """
    @staticmethod
    @overload
    def CoefsD1_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt2d,Vec : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def CoefsD2_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt,Vec1 : OCP.gp.gp_Vec,Vec2 : OCP.gp.gp_Vec) -> None: 
        """
        Calls CacheD1 for Bezier Curves Arrays computed with the method PolesCoefficients. Warning: To be used for Beziercurves ONLY!!!

        Calls CacheD1 for Bezier Curves Arrays computed with the method PolesCoefficients. Warning: To be used for Beziercurves ONLY!!!
        """
    @staticmethod
    @overload
    def CoefsD2_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt2d,Vec1 : OCP.gp.gp_Vec2d,Vec2 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def CoefsD3_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt,Vec1 : OCP.gp.gp_Vec,Vec2 : OCP.gp.gp_Vec,Vec3 : OCP.gp.gp_Vec) -> None: 
        """
        Calls CacheD1 for Bezier Curves Arrays computed with the method PolesCoefficients. Warning: To be used for Beziercurves ONLY!!!

        Calls CacheD1 for Bezier Curves Arrays computed with the method PolesCoefficients. Warning: To be used for Beziercurves ONLY!!!
        """
    @staticmethod
    @overload
    def CoefsD3_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt2d,Vec1 : OCP.gp.gp_Vec2d,Vec2 : OCP.gp.gp_Vec2d,Vec3 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D0_s(U : float,UIndex : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def D0_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,P : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def D0_s(U : float,Index : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,P : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def D0_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,P : OCP.gp.gp_Pnt2d) -> None: ...
    @staticmethod
    @overload
    def D0_s(U : float,Index : int,Degree : int,Periodic : bool,Poles : OCP.TColStd.TColStd_Array1OfReal,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> Tuple[float]: ...
    @staticmethod
    @overload
    def D1_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def D1_s(U : float,UIndex : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,Index : int,Degree : int,Periodic : bool,Poles : OCP.TColStd.TColStd_Array1OfReal,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> Tuple[float, float]: ...
    @staticmethod
    @overload
    def D1_s(U : float,Index : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,Index : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def D2_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,UIndex : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,Index : int,Degree : int,Periodic : bool,Poles : OCP.TColStd.TColStd_Array1OfReal,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> Tuple[float, float, float]: ...
    @staticmethod
    @overload
    def D3_s(U : float,Index : int,Degree : int,Periodic : bool,Poles : OCP.TColStd.TColStd_Array1OfReal,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> Tuple[float, float, float, float]: 
        """
        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def D3_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,UIndex : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,Index : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    def Derivative_s(Degree : int,Dimension : int,Length : int,Order : int) -> Tuple[float, float]: 
        """
        Computes the poles of the BSpline giving the derivatives of order <Order>.
        """
    @staticmethod
    def EvalBsplineBasis_s(DerivativeOrder : int,Order : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Parameter : float,FirstNonZeroBsplineIndex : int,BsplineBasis : OCP.math.math_Matrix,isPeriodic : bool=False) -> int: 
        """
        This evaluates the Bspline Basis at a given parameter Parameter up to the requested DerivativeOrder and store the result in the array BsplineBasis in the following fashion BSplineBasis(1,1) = value of first non vanishing Bspline function which has Index FirstNonZeroBsplineIndex BsplineBasis(1,2) = value of second non vanishing Bspline function which has Index FirstNonZeroBsplineIndex + 1 BsplineBasis(1,n) = value of second non vanishing non vanishing Bspline function which has Index FirstNonZeroBsplineIndex + n (n <= Order) BSplineBasis(2,1) = value of derivative of first non vanishing Bspline function which has Index FirstNonZeroBsplineIndex BSplineBasis(N,1) = value of Nth derivative of first non vanishing Bspline function which has Index FirstNonZeroBsplineIndex if N <= DerivativeOrder + 1
        """
    @staticmethod
    @overload
    def Eval_s(U : float,Degree : int,Dimension : int) -> Tuple[float, float]: 
        """
        Perform the Boor algorithm to evaluate a point at parameter <U>, with <Degree> and <Dimension>.

        Perform the De Boor algorithm to evaluate a point at parameter <U>, with <Degree> and <Dimension>.

        Perform the De Boor algorithm to evaluate a point at parameter <U>, with <Degree> and <Dimension>. Evaluates by multiplying the Poles by the Weights and gives the homogeneous result in PolesResult that is the results of the evaluation of the numerator once it has been multiplied by the weights and in WeightsResult one has the result of the evaluation of the denominator

        Perform the evaluation of the Bspline Basis and then multiplies by the weights this just evaluates the current point

        Perform the evaluation of the Bspline Basis and then multiplies by the weights this just evaluates the current point
        """
    @staticmethod
    @overload
    def Eval_s(U : float,PeriodicFlag : bool,HomogeneousFlag : bool,Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt2d) -> Tuple[int, float]: ...
    @staticmethod
    @overload
    def Eval_s(U : float,PeriodicFlag : bool,DerivativeRequest : int,Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,ArrayDimension : int) -> Tuple[int, float, float, float, float]: ...
    @staticmethod
    @overload
    def Eval_s(U : float,PeriodicFlag : bool,DerivativeRequest : int,Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,ArrayDimension : int) -> Tuple[int, float, float]: ...
    @staticmethod
    @overload
    def Eval_s(U : float,PeriodicFlag : bool,HomogeneousFlag : bool,Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Point : OCP.gp.gp_Pnt) -> Tuple[int, float]: ...
    @staticmethod
    def FactorBandedMatrix_s(Matrix : OCP.math.math_Matrix,UpperBandWidth : int,LowerBandWidth : int,PivotIndexProblem : int) -> int: 
        """
        this factors the Banded Matrix in the LU form with a Banded storage of components of the L matrix WARNING : do not use if the Matrix is totally positive (It is the case for Bspline matrices build as above with parameters being the Schoenberg points
        """
    @staticmethod
    def FirstUKnotIndex_s(Degree : int,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> int: 
        """
        Computes the index of the knots value which gives the start point of the curve.
        """
    @staticmethod
    def FlatBezierKnots_s(Degree : int) -> float: 
        """
        Returns pointer to statically allocated array representing flat knots for bezier curve of the specified degree. Raises OutOfRange if Degree > MaxDegree()
        """
    @staticmethod
    def FlatIndex_s(Degree : int,Index : int,Mults : OCP.TColStd.TColStd_Array1OfInteger,Periodic : bool) -> int: 
        """
        Computes the index of the flats knots sequence corresponding to <Index> in the knots sequence which multiplicities are <Mults>.
        """
    @staticmethod
    @overload
    def FunctionMultiply_s(Function : BSplCLib_EvaluatorFunction,BSplineDegree : int,BSplineFlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColStd.TColStd_Array1OfReal,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewDegree : int,NewPoles : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[int]: 
        """
        this will multiply a given Vectorial BSpline F(t) defined by its BSplineDegree and BSplineFlatKnotsl, its Poles array which are coded as an array of Real of the form [1..NumPoles][1..PolesDimension] by a function a(t) which is assumed to satisfy the following : 1. a(t) * F(t) is a polynomial BSpline that can be expressed exactly as a BSpline of degree NewDegree on the knots FlatKnots 2. the range of a(t) is the same as the range of F(t) Warning: it is the caller's responsibility to insure that conditions 1. and 2. above are satisfied : no check whatsoever is made in this method theStatus will return 0 if OK else it will return the pivot index of the matrix that was inverted to compute the multiplied BSpline : the method used is interpolation at Schoenenberg points of a(t)*F(t)

        this will multiply a given Vectorial BSpline F(t) defined by its BSplineDegree and BSplineFlatKnotsl, its Poles array which are coded as an array of Real of the form [1..NumPoles][1..PolesDimension] by a function a(t) which is assumed to satisfy the following : 1. a(t) * F(t) is a polynomial BSpline that can be expressed exactly as a BSpline of degree NewDegree on the knots FlatKnots 2. the range of a(t) is the same as the range of F(t) Warning: it is the caller's responsibility to insure that conditions 1. and 2. above are satisfied : no check whatsoever is made in this method theStatus will return 0 if OK else it will return the pivot index of the matrix that was inverted to compute the multiplied BSpline : the method used is interpolation at Schoenenberg points of a(t)*F(t)

        this will multiply a given Vectorial BSpline F(t) defined by its BSplineDegree and BSplineFlatKnotsl, its Poles array which are coded as an array of Real of the form [1..NumPoles][1..PolesDimension] by a function a(t) which is assumed to satisfy the following : 1. a(t) * F(t) is a polynomial BSpline that can be expressed exactly as a BSpline of degree NewDegree on the knots FlatKnots 2. the range of a(t) is the same as the range of F(t) Warning: it is the caller's responsibility to insure that conditions 1. and 2. above are satisfied : no check whatsoever is made in this method theStatus will return 0 if OK else it will return the pivot index of the matrix that was inverted to compute the multiplied BSpline : the method used is interpolation at Schoenenberg points of a(t)*F(t)

        this will multiply a given Vectorial BSpline F(t) defined by its BSplineDegree and BSplineFlatKnotsl, its Poles array which are coded as an array of Real of the form [1..NumPoles][1..PolesDimension] by a function a(t) which is assumed to satisfy the following : 1. a(t) * F(t) is a polynomial BSpline that can be expressed exactly as a BSpline of degree NewDegree on the knots FlatKnots 2. the range of a(t) is the same as the range of F(t) Warning: it is the caller's responsibility to insure that conditions 1. and 2. above are satisfied : no check whatsoever is made in this method theStatus will return 0 if OK else it will return the pivot index of the matrix that was inverted to compute the multiplied BSpline : the method used is interpolation at Schoenenberg points of a(t)*F(t)
        """
    @staticmethod
    @overload
    def FunctionMultiply_s(Function : BSplCLib_EvaluatorFunction,BSplineDegree : int,BSplineFlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewDegree : int,NewPoles : OCP.TColgp.TColgp_Array1OfPnt) -> Tuple[int]: ...
    @staticmethod
    @overload
    def FunctionMultiply_s(Function : BSplCLib_EvaluatorFunction,BSplineDegree : int,BSplineFlatKnots : OCP.TColStd.TColStd_Array1OfReal,PolesDimension : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewDegree : int) -> Tuple[float, float, int]: ...
    @staticmethod
    @overload
    def FunctionMultiply_s(Function : BSplCLib_EvaluatorFunction,BSplineDegree : int,BSplineFlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewDegree : int,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d) -> Tuple[int]: ...
    @staticmethod
    @overload
    def FunctionReparameterise_s(Function : BSplCLib_EvaluatorFunction,BSplineDegree : int,BSplineFlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColStd.TColStd_Array1OfReal,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewDegree : int,NewPoles : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[int]: 
        """
        This function will compose a given Vectorial BSpline F(t) defined by its BSplineDegree and BSplineFlatKnotsl, its Poles array which are coded as an array of Real of the form [1..NumPoles][1..PolesDimension] with a function a(t) which is assumed to satisfy the following:

        This function will compose a given Vectorial BSpline F(t) defined by its BSplineDegree and BSplineFlatKnotsl, its Poles array which are coded as an array of Real of the form [1..NumPoles][1..PolesDimension] with a function a(t) which is assumed to satisfy the following:

        this will compose a given Vectorial BSpline F(t) defined by its BSplineDegree and BSplineFlatKnotsl, its Poles array which are coded as an array of Real of the form [1..NumPoles][1..PolesDimension] with a function a(t) which is assumed to satisfy the following : 1. F(a(t)) is a polynomial BSpline that can be expressed exactly as a BSpline of degree NewDegree on the knots FlatKnots 2. a(t) defines a differentiable isomorphism between the range of FlatKnots to the range of BSplineFlatKnots which is the same as the range of F(t) Warning: it is the caller's responsibility to insure that conditions 1. and 2. above are satisfied : no check whatsoever is made in this method theStatus will return 0 if OK else it will return the pivot index of the matrix that was inverted to compute the multiplied BSpline : the method used is interpolation at Schoenenberg points of F(a(t))

        this will compose a given Vectorial BSpline F(t) defined by its BSplineDegree and BSplineFlatKnotsl, its Poles array which are coded as an array of Real of the form [1..NumPoles][1..PolesDimension] with a function a(t) which is assumed to satisfy the following : 1. F(a(t)) is a polynomial BSpline that can be expressed exactly as a BSpline of degree NewDegree on the knots FlatKnots 2. a(t) defines a differentiable isomorphism between the range of FlatKnots to the range of BSplineFlatKnots which is the same as the range of F(t) Warning: it is the caller's responsibility to insure that conditions 1. and 2. above are satisfied : no check whatsoever is made in this method theStatus will return 0 if OK else it will return the pivot index of the matrix that was inverted to compute the multiplied BSpline : the method used is interpolation at Schoenenberg points of F(a(t))
        """
    @staticmethod
    @overload
    def FunctionReparameterise_s(Function : BSplCLib_EvaluatorFunction,BSplineDegree : int,BSplineFlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewDegree : int,NewPoles : OCP.TColgp.TColgp_Array1OfPnt) -> Tuple[int]: ...
    @staticmethod
    @overload
    def FunctionReparameterise_s(Function : BSplCLib_EvaluatorFunction,BSplineDegree : int,BSplineFlatKnots : OCP.TColStd.TColStd_Array1OfReal,PolesDimension : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewDegree : int) -> Tuple[float, float, int]: ...
    @staticmethod
    @overload
    def FunctionReparameterise_s(Function : BSplCLib_EvaluatorFunction,BSplineDegree : int,BSplineFlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewDegree : int,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d) -> Tuple[int]: ...
    @staticmethod
    def GetPole_s(Index : int,Length : int,Depth : int,Dimension : int,Pole : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float, int]: 
        """
        Copy the pole at position <Index> in the Boor scheme of dimension <Dimension> to <Position> in the array <Pole>. <Position> is updated.
        """
    @staticmethod
    def Hunt_s(theArray : OCP.TColStd.TColStd_Array1OfReal,theX : float) -> Tuple[int]: 
        """
        This routine searches the position of the real value theX in the monotonically increasing set of real values theArray using bisection algorithm.
        """
    @staticmethod
    def IncreaseDegreeCountKnots_s(Degree : int,NewDegree : int,Periodic : bool,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> int: 
        """
        Returns the number of knots of a curve with multiplicities <Mults> after elevating the degree from <Degree> to <NewDegree>. See the IncreaseDegree method for more comments.
        """
    @staticmethod
    @overload
    def IncreaseDegree_s(theNewDegree : int,thePoles : OCP.TColgp.TColgp_Array1OfPnt2d,theWeights : OCP.TColStd.TColStd_Array1OfReal,theNewPoles : OCP.TColgp.TColgp_Array1OfPnt2d,theNewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None

        None

        None

        Increase the degree of a bspline (or bezier) curve of dimension theDimension form theDegree to theNewDegree.
        """
    @staticmethod
    @overload
    def IncreaseDegree_s(NewDegree : int,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColgp.TColgp_Array1OfPnt,NewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def IncreaseDegree_s(Degree : int,NewDegree : int,Periodic : bool,Dimension : int,Poles : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColStd.TColStd_Array1OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
    @staticmethod
    @overload
    def IncreaseDegree_s(Degree : int,NewDegree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d,NewWeights : OCP.TColStd.TColStd_Array1OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
    @staticmethod
    @overload
    def IncreaseDegree_s(Degree : int,NewDegree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt,NewWeights : OCP.TColStd.TColStd_Array1OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
    @staticmethod
    @overload
    def InsertKnot_s(UIndex : int,U : float,UMult : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d,NewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        Insert a new knot U of multiplicity UMult in the knot sequence.
        """
    @staticmethod
    @overload
    def InsertKnot_s(UIndex : int,U : float,UMult : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt,NewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def InsertKnots_s(Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,AddKnots : OCP.TColStd.TColStd_Array1OfReal,AddMults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d,NewWeights : OCP.TColStd.TColStd_Array1OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,Epsilon : float,Add : bool=True) -> None: 
        """
        None

        None

        Insert a sequence of knots <AddKnots> with multiplicities <AddMults>. <AddKnots> must be a non decreasing sequence and verifies :
        """
    @staticmethod
    @overload
    def InsertKnots_s(Degree : int,Periodic : bool,Dimension : int,Poles : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,AddKnots : OCP.TColStd.TColStd_Array1OfReal,AddMults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColStd.TColStd_Array1OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,Epsilon : float,Add : bool=True) -> None: ...
    @staticmethod
    @overload
    def InsertKnots_s(Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,AddKnots : OCP.TColStd.TColStd_Array1OfReal,AddMults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt,NewWeights : OCP.TColStd.TColStd_Array1OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,Epsilon : float,Add : bool=True) -> None: ...
    @staticmethod
    @overload
    def Interpolate_s(Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Parameters : OCP.TColStd.TColStd_Array1OfReal,ContactOrderArray : OCP.TColStd.TColStd_Array1OfInteger,Poles : OCP.TColgp.TColgp_Array1OfPnt2d) -> Tuple[int]: 
        """
        Performs the interpolation of the data given in the Poles array according to the requests in ContactOrderArray that is : if ContactOrderArray(i) has value d it means that Poles(i) contains the dth derivative of the function to be interpolated. The length L of the following arrays must be the same : Parameters, ContactOrderArray, Poles, The length of FlatKnots is Degree + L + 1 Warning: the method used to do that interpolation is gauss elimination WITHOUT pivoting. Thus if the diagonal is not dominant there is no guarantee that the algorithm will work. Nevertheless for Cubic interpolation or interpolation at Scheonberg points the method will work The InversionProblem will report 0 if there was no problem else it will give the index of the faulty pivot

        Performs the interpolation of the data given in the Poles array according to the requests in ContactOrderArray that is : if ContactOrderArray(i) has value d it means that Poles(i) contains the dth derivative of the function to be interpolated. The length L of the following arrays must be the same : Parameters, ContactOrderArray, Poles, The length of FlatKnots is Degree + L + 1 Warning: the method used to do that interpolation is gauss elimination WITHOUT pivoting. Thus if the diagonal is not dominant there is no guarantee that the algorithm will work. Nevertheless for Cubic interpolation at knots or interpolation at Scheonberg points the method will work. The InversionProblem w ll report 0 if there was no problem else it will give the index of the faulty pivot

        Performs the interpolation of the data given in the Poles array according to the requests in ContactOrderArray that is : if ContactOrderArray(i) has value d it means that Poles(i) contains the dth derivative of the function to be interpolated. The length L of the following arrays must be the same : Parameters, ContactOrderArray, Poles, The length of FlatKnots is Degree + L + 1 Warning: the method used to do that interpolation is gauss elimination WITHOUT pivoting. Thus if the diagonal is not dominant there is no guarantee that the algorithm will work. Nevertheless for Cubic interpolation at knots or interpolation at Scheonberg points the method will work. The InversionProblem will report 0 if there was no problem else it will give the index of the faulty pivot

        Performs the interpolation of the data given in the Poles array according to the requests in ContactOrderArray that is : if ContactOrderArray(i) has value d it means that Poles(i) contains the dth derivative of the function to be interpolated. The length L of the following arrays must be the same : Parameters, ContactOrderArray, Poles, The length of FlatKnots is Degree + L + 1 Warning: the method used to do that interpolation is gauss elimination WITHOUT pivoting. Thus if the diagonal is not dominant there is no guarantee that the algorithm will work. Nevertheless for Cubic interpolation at knots or interpolation at Scheonberg points the method will work. The InversionProblem w ll report 0 if there was no problem else it will give the i

        Performs the interpolation of the data given in the Poles array according to the requests in ContactOrderArray that is : if ContactOrderArray(i) has value d it means that Poles(i) contains the dth derivative of the function to be interpolated. The length L of the following arrays must be the same : Parameters, ContactOrderArray The length of FlatKnots is Degree + L + 1 The PolesArray is an seen as an Array[1..N][1..ArrayDimension] with N = tge length of the parameters array Warning: the method used to do that interpolation is gauss elimination WITHOUT pivoting. Thus if the diagonal is not dominant there is no guarantee that the algorithm will work. Nevertheless for Cubic interpolation or interpolation at Scheonberg points the method will work The InversionProblem will report 0 if there was no problem else it will give the index of the faulty pivot

        None
        """
    @staticmethod
    @overload
    def Interpolate_s(Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Parameters : OCP.TColStd.TColStd_Array1OfReal,ContactOrderArray : OCP.TColStd.TColStd_Array1OfInteger,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[int]: ...
    @staticmethod
    @overload
    def Interpolate_s(Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Parameters : OCP.TColStd.TColStd_Array1OfReal,ContactOrderArray : OCP.TColStd.TColStd_Array1OfInteger,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[int]: ...
    @staticmethod
    @overload
    def Interpolate_s(Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Parameters : OCP.TColStd.TColStd_Array1OfReal,ContactOrderArray : OCP.TColStd.TColStd_Array1OfInteger,Poles : OCP.TColgp.TColgp_Array1OfPnt) -> Tuple[int]: ...
    @staticmethod
    @overload
    def Interpolate_s(Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Parameters : OCP.TColStd.TColStd_Array1OfReal,ContactOrderArray : OCP.TColStd.TColStd_Array1OfInteger,ArrayDimension : int) -> Tuple[float, int]: ...
    @staticmethod
    @overload
    def Interpolate_s(Degree : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Parameters : OCP.TColStd.TColStd_Array1OfReal,ContactOrderArray : OCP.TColStd.TColStd_Array1OfInteger,ArrayDimension : int) -> Tuple[float, float, int]: ...
    @staticmethod
    def IsRational_s(Weights : OCP.TColStd.TColStd_Array1OfReal,I1 : int,I2 : int,Epsilon : float=0.0) -> bool: 
        """
        Returns False if all the weights of the array <Weights> between I1 an I2 are identic. Epsilon is used for comparing weights. If Epsilon is 0. the Epsilon of the first weight is used.
        """
    @staticmethod
    def KnotAnalysis_s(Degree : int,Periodic : bool,CKnots : OCP.TColStd.TColStd_Array1OfReal,CMults : OCP.TColStd.TColStd_Array1OfInteger,KnotForm : OCP.GeomAbs.GeomAbs_BSplKnotDistribution) -> Tuple[int]: 
        """
        Analyzes the array of knots. Returns the form and the maximum knot multiplicity.
        """
    @staticmethod
    def KnotForm_s(Knots : OCP.TColStd.TColStd_Array1OfReal,FromK1 : int,ToK2 : int) -> BSplCLib_KnotDistribution: 
        """
        Analyses if the knots distribution is "Uniform" or "NonUniform" between the knot FromK1 and the knot ToK2. There is no repetition of knot in the knots'sequence <Knots>.
        """
    @staticmethod
    def KnotSequenceLength_s(Mults : OCP.TColStd.TColStd_Array1OfInteger,Degree : int,Periodic : bool) -> int: 
        """
        Returns the length of the sequence of knots with repetition.
        """
    @staticmethod
    @overload
    def KnotSequence_s(Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,KnotSeq : OCP.TColStd.TColStd_Array1OfReal,Periodic : bool=False) -> None: 
        """
        None

        Computes the sequence of knots KnotSeq with repetition of the knots of multiplicity greater than 1.
        """
    @staticmethod
    @overload
    def KnotSequence_s(Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Degree : int,Periodic : bool,KnotSeq : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    def KnotsLength_s(KnotSeq : OCP.TColStd.TColStd_Array1OfReal,Periodic : bool=False) -> int: 
        """
        Returns the length of the sequence of knots (and Mults) without repetition.
        """
    @staticmethod
    def Knots_s(KnotSeq : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Periodic : bool=False) -> None: 
        """
        Computes the sequence of knots Knots without repetition of the knots of multiplicity greater than 1.
        """
    @staticmethod
    def LastUKnotIndex_s(Degree : int,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> int: 
        """
        Computes the index of the knots value which gives the end point of the curve.
        """
    @staticmethod
    @overload
    def LocateParameter_s(Degree : int,Knots : OCP.TColStd.TColStd_Array1OfReal,U : float,IsPeriodic : bool,FromK1 : int,ToK2 : int) -> Tuple[int, float]: 
        """
        Locates the parametric value U in the knots sequence between the knot K1 and the knot K2. The value return in Index verifies.

        Locates the parametric value U in the knots sequence between the knot K1 and the knot K2. The value return in Index verifies.

        None
        """
    @staticmethod
    @overload
    def LocateParameter_s(Degree : int,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,U : float,Periodic : bool) -> Tuple[int, float]: ...
    @staticmethod
    @overload
    def LocateParameter_s(Degree : int,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,U : float,IsPeriodic : bool,FromK1 : int,ToK2 : int) -> Tuple[int, float]: ...
    @staticmethod
    def MaxDegree_s() -> int: 
        """
        returns the degree maxima for a BSplineCurve.
        """
    @staticmethod
    def MaxKnotMult_s(Mults : OCP.TColStd.TColStd_Array1OfInteger,K1 : int,K2 : int) -> int: 
        """
        Finds the greatest multiplicity in a set of knots between K1 and K2. Mults is the multiplicity associated with each knot value.
        """
    @staticmethod
    def MergeBSplineKnots_s(Tolerance : float,StartValue : float,EndValue : float,Degree1 : int,Knots1 : OCP.TColStd.TColStd_Array1OfReal,Mults1 : OCP.TColStd.TColStd_Array1OfInteger,Degree2 : int,Knots2 : OCP.TColStd.TColStd_Array1OfReal,Mults2 : OCP.TColStd.TColStd_Array1OfInteger,NewKnots : OCP.TColStd.TColStd_HArray1OfReal,NewMults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: 
        """
        Merges two knot vector by setting the starting and ending values to StartValue and EndValue
        """
    @staticmethod
    def MinKnotMult_s(Mults : OCP.TColStd.TColStd_Array1OfInteger,K1 : int,K2 : int) -> int: 
        """
        Finds the lowest multiplicity in a set of knots between K1 and K2. Mults is the multiplicity associated with each knot value.
        """
    @staticmethod
    @overload
    def MovePointAndTangent_s(U : float,Delta : OCP.gp.gp_Vec2d,DeltaDerivative : OCP.gp.gp_Vec2d,Tolerance : float,Degree : int,StartingCondition : int,EndingCondition : int,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d) -> Tuple[int]: 
        """
        This is the dimension free version of the utility U is the parameter must be within the first FlatKnots and the last FlatKnots Delta is the amount the curve has to be moved DeltaDerivative is the amount the derivative has to be moved. Delta and DeltaDerivative must be array of dimension ArrayDimension Degree is the degree of the BSpline and the FlatKnots are the knots of the BSpline Starting Condition if = -1 means the starting point of the curve can move = 0 means the starting point of the curve cannot move but tangent starting point of the curve cannot move = 1 means the starting point and tangents cannot move = 2 means the starting point tangent and curvature cannot move = ... Same holds for EndingCondition Poles are the poles of the curve Weights are the weights of the curve if not NULL NewPoles are the poles of the deformed curve ErrorStatus will be 0 if no error happened 1 if there are not enough knots/poles the imposed conditions The way to solve this problem is to add knots to the BSpline If StartCondition = 1 and EndCondition = 1 then you need at least 4 + 2 = 6 poles so for example to have a C1 cubic you will need have at least 2 internal knots.

        This is the dimension free version of the utility U is the parameter must be within the first FlatKnots and the last FlatKnots Delta is the amount the curve has to be moved DeltaDerivative is the amount the derivative has to be moved. Delta and DeltaDerivative must be array of dimension ArrayDimension Degree is the degree of the BSpline and the FlatKnots are the knots of the BSpline Starting Condition if = -1 means the starting point of the curve can move = 0 means the starting point of the curve cannot move but tangent starting point of the curve cannot move = 1 means the starting point and tangents cannot move = 2 means the starting point tangent and curvature cannot move = ... Same holds for EndingCondition Poles are the poles of the curve Weights are the weights of the curve if not NULL NewPoles are the poles of the deformed curve ErrorStatus will be 0 if no error happened 1 if there are not enough knots/poles the imposed conditions The way to solve this problem is to add knots to the BSpline If StartCondition = 1 and EndCondition = 1 then you need at least 4 + 2 = 6 poles so for example to have a C1 cubic you will need have at least 2 internal knots.

        This is the dimension free version of the utility U is the parameter must be within the first FlatKnots and the last FlatKnots Delta is the amount the curve has to be moved DeltaDerivative is the amount the derivative has to be moved. Delta and DeltaDerivative must be array of dimension ArrayDimension Degree is the degree of the BSpline and the FlatKnots are the knots of the BSpline Starting Condition if = -1 means the starting point of the curve can move = 0 means the starting point of the curve cannot move but tangent starting point of the curve cannot move = 1 means the starting point and tangents cannot move = 2 means the starting point tangent and curvature cannot move = ... Same holds for EndingCondition Poles are the poles of the curve Weights are the weights of the curve if not NULL NewPoles are the poles of the deformed curve ErrorStatus will be 0 if no error happened 1 if there are not enough knots/poles the imposed conditions The way to solve this problem is to add knots to the BSpline If StartCondition = 1 and EndCondition = 1 then you need at least 4 + 2 = 6 poles so for example to have a C1 cubic you will need have at least 2 internal knots.
        """
    @staticmethod
    @overload
    def MovePointAndTangent_s(U : float,Delta : OCP.gp.gp_Vec,DeltaDerivative : OCP.gp.gp_Vec,Tolerance : float,Degree : int,StartingCondition : int,EndingCondition : int,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColgp.TColgp_Array1OfPnt) -> Tuple[int]: ...
    @staticmethod
    @overload
    def MovePointAndTangent_s(U : float,ArrayDimension : int,Tolerance : float,Degree : int,StartingCondition : int,EndingCondition : int,Weights : OCP.TColStd.TColStd_Array1OfReal,FlatKnots : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float, float, float, float, int]: ...
    @staticmethod
    @overload
    def MovePoint_s(U : float,Displ : OCP.gp.gp_Vec2d,Index1 : int,Index2 : int,Degree : int,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d) -> Tuple[int, int]: 
        """
        Find the new poles which allows an old point (with a given u as parameter) to reach a new position Index1 and Index2 indicate the range of poles we can move (1, NbPoles-1) or (2, NbPoles) -> no constraint for one side don't enter (1,NbPoles) -> error: rigid move (2, NbPoles-1) -> the ends are enforced (3, NbPoles-2) -> the ends and the tangency are enforced if Problem in BSplineBasis calculation, no change for the curve and FirstIndex, LastIndex = 0

        Find the new poles which allows an old point (with a given u as parameter) to reach a new position Index1 and Index2 indicate the range of poles we can move (1, NbPoles-1) or (2, NbPoles) -> no constraint for one side don't enter (1,NbPoles) -> error: rigid move (2, NbPoles-1) -> the ends are enforced (3, NbPoles-2) -> the ends and the tangency are enforced if Problem in BSplineBasis calculation, no change for the curve and FirstIndex, LastIndex = 0
        """
    @staticmethod
    @overload
    def MovePoint_s(U : float,Displ : OCP.gp.gp_Vec,Index1 : int,Index2 : int,Degree : int,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColgp.TColgp_Array1OfPnt) -> Tuple[int, int]: ...
    @staticmethod
    def MultForm_s(Mults : OCP.TColStd.TColStd_Array1OfInteger,FromK1 : int,ToK2 : int) -> BSplCLib_MultDistribution: 
        """
        Analyses the distribution of multiplicities between the knot FromK1 and the Knot ToK2.
        """
    @staticmethod
    def NbPoles_s(Degree : int,Periodic : bool,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> int: 
        """
        Returns the number of poles of the curve. Returns 0 if one of the multiplicities is incorrect.
        """
    @staticmethod
    def NoMults_s() -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        Used as argument for a flatknots evaluation.
        """
    @staticmethod
    def NoWeights_s() -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Used as argument for a non rational curve.
        """
    @staticmethod
    def PoleIndex_s(Degree : int,Index : int,Periodic : bool,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> int: 
        """
        Return the index of the first Pole to use on the span Mults(Index) - Mults(Index+1). This index must be added to Poles.Lower().
        """
    @staticmethod
    @overload
    def PolesCoefficients_s(Poles : OCP.TColgp.TColgp_Array1OfPnt,CachePoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        None

        None

        None

        Encapsulation of BuildCache to perform the evaluation of the Taylor expansion for beziercurves at parameter 0. Warning: To be used for Beziercurves ONLY!!!
        """
    @staticmethod
    @overload
    def PolesCoefficients_s(Poles : OCP.TColgp.TColgp_Array1OfPnt2d,CachePoles : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @staticmethod
    @overload
    def PolesCoefficients_s(Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,CachePoles : OCP.TColgp.TColgp_Array1OfPnt2d,CacheWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def PolesCoefficients_s(Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,CachePoles : OCP.TColgp.TColgp_Array1OfPnt,CacheWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    def PrepareInsertKnots_s(Degree : int,Periodic : bool,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,AddKnots : OCP.TColStd.TColStd_Array1OfReal,AddMults : OCP.TColStd.TColStd_Array1OfInteger,NbPoles : int,NbKnots : int,Epsilon : float,Add : bool=True) -> bool: 
        """
        Returns in <NbPoles, NbKnots> the new number of poles and knots if the sequence of knots <AddKnots, AddMults> is inserted in the sequence <Knots, Mults>.
        """
    @staticmethod
    def PrepareTrimming_s(Degree : int,Periodic : bool,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,U1 : float,U2 : float) -> Tuple[int, int]: 
        """
        Set in <NbKnots> and <NbPoles> the number of Knots and Poles of the curve resulting from the trimming of the BSplinecurve defined with <degree>, <knots>, <mults>
        """
    @staticmethod
    def PrepareUnperiodize_s(Degree : int,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> Tuple[int, int]: 
        """
        Set in <NbKnots> and <NbPolesToAdd> the number of Knots and Poles of the NotPeriodic Curve identical at the periodic curve with a degree <Degree> , a knots-distribution with Multiplicities <Mults>.
        """
    @staticmethod
    @overload
    def RaiseMultiplicity_s(KnotIndex : int,Mult : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt,NewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        Raise the multiplicity of knot to <UMult>.
        """
    @staticmethod
    @overload
    def RaiseMultiplicity_s(KnotIndex : int,Mult : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d,NewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def RemoveKnot_s(Index : int,Mult : int,Degree : int,Periodic : bool,Dimension : int,Poles : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColStd.TColStd_Array1OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,Tolerance : float) -> bool: 
        """
        None

        None

        Decrement the multiplicity of <Knots(Index)> to <Mult>. If <Mult> is null the knot is removed.
        """
    @staticmethod
    @overload
    def RemoveKnot_s(Index : int,Mult : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt,NewWeights : OCP.TColStd.TColStd_Array1OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,Tolerance : float) -> bool: ...
    @staticmethod
    @overload
    def RemoveKnot_s(Index : int,Mult : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d,NewWeights : OCP.TColStd.TColStd_Array1OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,Tolerance : float) -> bool: ...
    @staticmethod
    def Reparametrize_s(U1 : float,U2 : float,Knots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Reparametrizes a B-spline curve to [U1, U2]. The knot values are recomputed such that Knots (Lower) = U1 and Knots (Upper) = U2 but the knot form is not modified. Warnings : In the array Knots the values must be in ascending order. U1 must not be equal to U2 to avoid division by zero.
        """
    @staticmethod
    @overload
    def Resolution_s(Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,NumPoles : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Degree : int,Tolerance3D : float) -> Tuple[float]: 
        """
        given a tolerance in 3D space returns a tolerance in U parameter space such that all u1 and u0 in the domain of the curve f(u) | u1 - u0 | < UTolerance and we have |f (u1) - f (u0)| < Tolerance3D

        given a tolerance in 3D space returns a tolerance in U parameter space such that all u1 and u0 in the domain of the curve f(u) | u1 - u0 | < UTolerance and we have |f (u1) - f (u0)| < Tolerance3D

        given a tolerance in 3D space returns a tolerance in U parameter space such that all u1 and u0 in the domain of the curve f(u) | u1 - u0 | < UTolerance and we have |f (u1) - f (u0)| < Tolerance3D
        """
    @staticmethod
    @overload
    def Resolution_s(ArrayDimension : int,NumPoles : int,Weights : OCP.TColStd.TColStd_Array1OfReal,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Degree : int,Tolerance3D : float) -> Tuple[float, float]: ...
    @staticmethod
    @overload
    def Resolution_s(Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,NumPoles : int,FlatKnots : OCP.TColStd.TColStd_Array1OfReal,Degree : int,Tolerance3D : float) -> Tuple[float]: ...
    @staticmethod
    @overload
    def Reverse_s(Knots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Reverses the array knots to become the knots sequence of the reversed curve.

        Reverses the array of multiplicities.

        Reverses the array of poles. Last is the index of the new first pole. On a non periodic curve last is Poles.Upper(). On a periodic curve last is

        Reverses the array of poles.

        Reverses the array of poles.
        """
    @staticmethod
    @overload
    def Reverse_s(Mults : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
    @staticmethod
    @overload
    def Reverse_s(Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Last : int) -> None: ...
    @staticmethod
    @overload
    def Reverse_s(Weights : OCP.TColStd.TColStd_Array1OfReal,Last : int) -> None: ...
    @staticmethod
    @overload
    def Reverse_s(Poles : OCP.TColgp.TColgp_Array1OfPnt,Last : int) -> None: ...
    @staticmethod
    @overload
    def SolveBandedSystem_s(Matrix : OCP.math.math_Matrix,UpperBandWidth : int,LowerBandWidth : int,ArrayDimension : int,Array : float) -> int: 
        """
        This solves the system Matrix.X = B with when Matrix is factored in LU form The Array is an seen as an Array[1..N][1..ArrayDimension] with N = the rank of the matrix Matrix. The result is stored in Array when each coordinate is solved that is B is the array whose values are B[i] = Array[i][p] for each p in 1..ArrayDimension

        This solves the system Matrix.X = B with when Matrix is factored in LU form The Array has the length of the rank of the matrix Matrix. The result is stored in Array when each coordinate is solved that is B is the array whose values are B[i] = Array[i][p] for each p in 1..ArrayDimension

        This solves the system Matrix.X = B with when Matrix is factored in LU form The Array has the length of the rank of the matrix Matrix. The result is stored in Array when each coordinate is solved that is B is the array whose values are B[i] = Array[i][p] for each p in 1..ArrayDimension

        None

        This solves the system Matrix.X = B with when Matrix is factored in LU form The Array is an seen as an Array[1..N][1..ArrayDimension] with N = the rank of the matrix Matrix. The result is stored in Array when each coordinate is solved that is B is the array whose values are B[i] = Array[i][p] for each p in 1..ArrayDimension. If HomogeneousFlag == 0 the Poles are multiplied by the Weights upon Entry and once interpolation is carried over the result of the poles are divided by the result of the interpolation of the weights. Otherwise if HomogenousFlag == 1 the Poles and Weigths are treated homogeneously that is that those are interpolated as they are and result is returned without division by the interpolated weigths.

        This solves the system Matrix.X = B with when Matrix is factored in LU form The Array is an seen as an Array[1..N][1..ArrayDimension] with N = the rank of the matrix Matrix. The result is stored in Array when each coordinate is solved that is B is the array whose values are B[i] = Array[i][p] for each p in 1..ArrayDimension If HomogeneousFlag == 0 the Poles are multiplied by the Weights upon Entry and once interpolation is carried over the result of the poles are divided by the result of the interpolation of the weights. Otherwise if HomogenousFlag == 1 the Poles and Weigths are treated homogeneously that is that those are interpolated as they are and result is returned without division by the interpolated weigths.
        """
    @staticmethod
    @overload
    def SolveBandedSystem_s(Matrix : OCP.math.math_Matrix,UpperBandWidth : int,LowerBandWidth : int,Array : OCP.TColgp.TColgp_Array1OfPnt2d) -> int: ...
    @staticmethod
    @overload
    def SolveBandedSystem_s(Matrix : OCP.math.math_Matrix,UpperBandWidth : int,LowerBandWidth : int,HomogeneousFlag : bool,Array : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal) -> int: ...
    @staticmethod
    @overload
    def SolveBandedSystem_s(Matrix : OCP.math.math_Matrix,UpperBandWidth : int,LowerBandWidth : int,HomogenousFlag : bool,Array : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal) -> int: ...
    @staticmethod
    @overload
    def SolveBandedSystem_s(Matrix : OCP.math.math_Matrix,UpperBandWidth : int,LowerBandWidth : int,HomogenousFlag : bool,ArrayDimension : int,Array : float,Weights : float) -> int: ...
    @staticmethod
    @overload
    def SolveBandedSystem_s(Matrix : OCP.math.math_Matrix,UpperBandWidth : int,LowerBandWidth : int,Array : OCP.TColgp.TColgp_Array1OfPnt) -> int: ...
    @staticmethod
    def TangExtendToConstraint_s(FlatKnots : OCP.TColStd.TColStd_Array1OfReal,C1Coefficient : float,NumPoles : int,Dimension : int,Degree : int,ConstraintPoint : OCP.TColStd.TColStd_Array1OfReal,Continuity : int,After : bool) -> Tuple[float, int, int, float, float]: 
        """
        Extend a BSpline nD using the tangency map <C1Coefficient> is the coefficient of reparametrisation <Continuity> must be equal to 1, 2 or 3. <Degree> must be greater or equal than <Continuity> + 1.
        """
    @staticmethod
    @overload
    def Trimming_s(Degree : int,Periodic : bool,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,U1 : float,U2 : float,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt,NewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None

        None
        """
    @staticmethod
    @overload
    def Trimming_s(Degree : int,Periodic : bool,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,U1 : float,U2 : float,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d,NewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def Trimming_s(Degree : int,Periodic : bool,Dimension : int,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Poles : OCP.TColStd.TColStd_Array1OfReal,U1 : float,U2 : float,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def Unperiodize_s(Degree : int,Mults : OCP.TColStd.TColStd_Array1OfInteger,Knots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColgp.TColgp_Array1OfPnt2d,NewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None

        None
        """
    @staticmethod
    @overload
    def Unperiodize_s(Degree : int,Mults : OCP.TColStd.TColStd_Array1OfInteger,Knots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColgp.TColgp_Array1OfPnt,NewWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def Unperiodize_s(Degree : int,Dimension : int,Mults : OCP.TColStd.TColStd_Array1OfInteger,Knots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    def __init__(self) -> None: ...
    pass
class BSplCLib_Cache(OCP.Standard.Standard_Transient):
    """
    A cache class for Bezier and B-spline curves.A cache class for Bezier and B-spline curves.
    """
    @overload
    def BuildCache(self,theParameter : float,theFlatKnots : OCP.TColStd.TColStd_Array1OfReal,thePoles : OCP.TColgp.TColgp_Array1OfPnt,theWeights : OCP.TColStd.TColStd_Array1OfReal=None) -> None: 
        """
        Recomputes the cache data for 2D curves. Does not verify validity of the cache

        Recomputes the cache data for 3D curves. Does not verify validity of the cache
        """
    @overload
    def BuildCache(self,theParameter : float,theFlatKnots : OCP.TColStd.TColStd_Array1OfReal,thePoles2d : OCP.TColgp.TColgp_Array1OfPnt2d,theWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def D0(self,theParameter : float,thePoint : OCP.gp.gp_Pnt) -> None: 
        """
        Calculates the point on the curve in the specified parameter

        None
        """
    @overload
    def D0(self,theParameter : float,thePoint : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def D1(self,theParameter : float,thePoint : OCP.gp.gp_Pnt2d,theTangent : OCP.gp.gp_Vec2d) -> None: 
        """
        Calculates the point on the curve and its first derivative in the specified parameter

        None
        """
    @overload
    def D1(self,theParameter : float,thePoint : OCP.gp.gp_Pnt,theTangent : OCP.gp.gp_Vec) -> None: ...
    @overload
    def D2(self,theParameter : float,thePoint : OCP.gp.gp_Pnt,theTangent : OCP.gp.gp_Vec,theCurvature : OCP.gp.gp_Vec) -> None: 
        """
        Calculates the point on the curve and two derivatives in the specified parameter

        None
        """
    @overload
    def D2(self,theParameter : float,thePoint : OCP.gp.gp_Pnt2d,theTangent : OCP.gp.gp_Vec2d,theCurvature : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def D3(self,theParameter : float,thePoint : OCP.gp.gp_Pnt,theTangent : OCP.gp.gp_Vec,theCurvature : OCP.gp.gp_Vec,theTorsion : OCP.gp.gp_Vec) -> None: 
        """
        Calculates the point on the curve and three derivatives in the specified parameter

        None
        """
    @overload
    def D3(self,theParameter : float,thePoint : OCP.gp.gp_Pnt2d,theTangent : OCP.gp.gp_Vec2d,theCurvature : OCP.gp.gp_Vec2d,theTorsion : OCP.gp.gp_Vec2d) -> None: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCacheValid(self,theParameter : float) -> bool: 
        """
        Verifies validity of the cache using flat parameter of the point
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theDegree : int,thePeriodic : bool,theFlatKnots : OCP.TColStd.TColStd_Array1OfReal,thePoles : OCP.TColgp.TColgp_Array1OfPnt,theWeights : OCP.TColStd.TColStd_Array1OfReal=None) -> None: ...
    @overload
    def __init__(self,theDegree : int,thePeriodic : bool,theFlatKnots : OCP.TColStd.TColStd_Array1OfReal,thePoles2d : OCP.TColgp.TColgp_Array1OfPnt2d,theWeights : OCP.TColStd.TColStd_Array1OfReal=None) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class BSplCLib_CacheParams():
    """
    Simple structure containing parameters describing parameterization of a B-spline curve or a surface in one direction (U or V), and data of the current span for its caching
    """
    def IsCacheValid(self,theParameter : float) -> bool: 
        """
        Verifies validity of the cache using flat parameter of the point
        """
    def LocateParameter(self,theFlatKnots : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float]: 
        """
        Computes span for the specified parameter
        """
    def PeriodicNormalization(self,theParameter : float) -> float: 
        """
        Normalizes the parameter for periodic B-splines
        """
    def __init__(self,theDegree : int,thePeriodic : bool,theFlatKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @property
    def SpanIndex(self) -> int:
        """
        :type: int
        """
    @SpanIndex.setter
    def SpanIndex(self, arg0: int) -> None:
        pass
    @property
    def SpanLength(self) -> float:
        """
        :type: float
        """
    @SpanLength.setter
    def SpanLength(self, arg0: float) -> None:
        pass
    @property
    def SpanStart(self) -> float:
        """
        :type: float
        """
    @SpanStart.setter
    def SpanStart(self, arg0: float) -> None:
        pass
    pass
class BSplCLib_EvaluatorFunction():
    """
    None
    """
    def Evaluate(self,theDerivativeRequest : int,theStartEnd : float,theParameter : float) -> Tuple[float, int]: 
        """
        Function evaluation method to be defined by descendant
        """
    def __init__(self) -> None: ...
    pass
class BSplCLib_KnotDistribution():
    """
    This enumeration describes the repartition of the knots sequence. If all the knots differ by the same positive constant from the preceding knot the "KnotDistribution" is <Uniform> else it is <NonUniform>

    Members:

      BSplCLib_NonUniform

      BSplCLib_Uniform
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
    BSplCLib_NonUniform: OCP.BSplCLib.BSplCLib_KnotDistribution # value = <BSplCLib_KnotDistribution.BSplCLib_NonUniform: 0>
    BSplCLib_Uniform: OCP.BSplCLib.BSplCLib_KnotDistribution # value = <BSplCLib_KnotDistribution.BSplCLib_Uniform: 1>
    __entries: dict # value = {'BSplCLib_NonUniform': (<BSplCLib_KnotDistribution.BSplCLib_NonUniform: 0>, None), 'BSplCLib_Uniform': (<BSplCLib_KnotDistribution.BSplCLib_Uniform: 1>, None)}
    __members__: dict # value = {'BSplCLib_NonUniform': <BSplCLib_KnotDistribution.BSplCLib_NonUniform: 0>, 'BSplCLib_Uniform': <BSplCLib_KnotDistribution.BSplCLib_Uniform: 1>}
    pass
class BSplCLib_MultDistribution():
    """
    This enumeration describes the form of the sequence of mutiplicities. MultDistribution is :

    Members:

      BSplCLib_NonConstant

      BSplCLib_Constant

      BSplCLib_QuasiConstant
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
    BSplCLib_Constant: OCP.BSplCLib.BSplCLib_MultDistribution # value = <BSplCLib_MultDistribution.BSplCLib_Constant: 1>
    BSplCLib_NonConstant: OCP.BSplCLib.BSplCLib_MultDistribution # value = <BSplCLib_MultDistribution.BSplCLib_NonConstant: 0>
    BSplCLib_QuasiConstant: OCP.BSplCLib.BSplCLib_MultDistribution # value = <BSplCLib_MultDistribution.BSplCLib_QuasiConstant: 2>
    __entries: dict # value = {'BSplCLib_NonConstant': (<BSplCLib_MultDistribution.BSplCLib_NonConstant: 0>, None), 'BSplCLib_Constant': (<BSplCLib_MultDistribution.BSplCLib_Constant: 1>, None), 'BSplCLib_QuasiConstant': (<BSplCLib_MultDistribution.BSplCLib_QuasiConstant: 2>, None)}
    __members__: dict # value = {'BSplCLib_NonConstant': <BSplCLib_MultDistribution.BSplCLib_NonConstant: 0>, 'BSplCLib_Constant': <BSplCLib_MultDistribution.BSplCLib_Constant: 1>, 'BSplCLib_QuasiConstant': <BSplCLib_MultDistribution.BSplCLib_QuasiConstant: 2>}
    pass
BSplCLib_Constant: OCP.BSplCLib.BSplCLib_MultDistribution # value = <BSplCLib_MultDistribution.BSplCLib_Constant: 1>
BSplCLib_NonConstant: OCP.BSplCLib.BSplCLib_MultDistribution # value = <BSplCLib_MultDistribution.BSplCLib_NonConstant: 0>
BSplCLib_NonUniform: OCP.BSplCLib.BSplCLib_KnotDistribution # value = <BSplCLib_KnotDistribution.BSplCLib_NonUniform: 0>
BSplCLib_QuasiConstant: OCP.BSplCLib.BSplCLib_MultDistribution # value = <BSplCLib_MultDistribution.BSplCLib_QuasiConstant: 2>
BSplCLib_Uniform: OCP.BSplCLib.BSplCLib_KnotDistribution # value = <BSplCLib_KnotDistribution.BSplCLib_Uniform: 1>
