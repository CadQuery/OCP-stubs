import OCP.BSplSLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.TColgp
import OCP.Standard
import OCP.TColStd
__all__  = [
"BSplSLib",
"BSplSLib_Cache",
"BSplSLib_EvaluatorFunction"
]
class BSplSLib():
    """
    BSplSLib B-spline surface Library This package provides an implementation of geometric functions for rational and non rational, periodic and non periodic B-spline surface computation.
    """
    @staticmethod
    @overload
    def BuildCache_s(theU : float,theV : float,theUSpanDomain : float,theVSpanDomain : float,theUPeriodic : bool,theVPeriodic : bool,theUDegree : int,theVDegree : int,theUIndex : int,theVIndex : int,theUFlatKnots : OCP.TColStd.TColStd_Array1OfReal,theVFlatKnots : OCP.TColStd.TColStd_Array1OfReal,thePoles : OCP.TColgp.TColgp_Array2OfPnt,theWeights : OCP.TColStd.TColStd_Array2OfReal,theCacheArray : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        Perform the evaluation of the Taylor expansion of the Bspline normalized between 0 and 1. If rational computes the homogeneous Taylor expension for the numerator and stores it in CachePoles

        Perform the evaluation of the Taylor expansion of the Bspline normalized between 0 and 1. Structure of result optimized for BSplSLib_Cache.
        """
    @staticmethod
    @overload
    def BuildCache_s(U : float,V : float,USpanDomain : float,VSpanDomain : float,UPeriodicFlag : bool,VPeriodicFlag : bool,UDegree : int,VDegree : int,UIndex : int,VIndex : int,UFlatKnots : OCP.TColStd.TColStd_Array1OfReal,VFlatKnots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,CachePoles : OCP.TColgp.TColgp_Array2OfPnt,CacheWeights : OCP.TColStd.TColStd_Array2OfReal) -> None: ...
    @staticmethod
    def CacheD0_s(U : float,V : float,UDegree : int,VDegree : int,UCacheParameter : float,VCacheParameter : float,USpanLenght : float,VSpanLength : float,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Point : OCP.gp.gp_Pnt) -> None: 
        """
        Perform the evaluation of the of the cache the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights this just evaluates the current point the CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effects
        """
    @staticmethod
    def CacheD1_s(U : float,V : float,UDegree : int,VDegree : int,UCacheParameter : float,VCacheParameter : float,USpanLenght : float,VSpanLength : float,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Point : OCP.gp.gp_Pnt,VecU : OCP.gp.gp_Vec,VecV : OCP.gp.gp_Vec) -> None: 
        """
        Perform the evaluation of the of the cache the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights this just evaluates the current point the CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effects
        """
    @staticmethod
    def CacheD2_s(U : float,V : float,UDegree : int,VDegree : int,UCacheParameter : float,VCacheParameter : float,USpanLenght : float,VSpanLength : float,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Point : OCP.gp.gp_Pnt,VecU : OCP.gp.gp_Vec,VecV : OCP.gp.gp_Vec,VecUU : OCP.gp.gp_Vec,VecUV : OCP.gp.gp_Vec,VecVV : OCP.gp.gp_Vec) -> None: 
        """
        Perform the evaluation of the of the cache the parameter must be normalized between the 0 and 1 for the span. The Cache must be valid when calling this routine. Geom Package will insure that. and then multiplies by the weights this just evaluates the current point the CacheParameter is where the Cache was constructed the SpanLength is to normalize the polynomial in the cache to avoid bad conditioning effects
        """
    @staticmethod
    def CoefsD0_s(U : float,V : float,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Point : OCP.gp.gp_Pnt) -> None: 
        """
        Calls CacheD0 for Bezier Surfaces Arrays computed with the method PolesCoefficients. Warning: To be used for BezierSurfaces ONLY!!!
        """
    @staticmethod
    def CoefsD1_s(U : float,V : float,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Point : OCP.gp.gp_Pnt,VecU : OCP.gp.gp_Vec,VecV : OCP.gp.gp_Vec) -> None: 
        """
        Calls CacheD0 for Bezier Surfaces Arrays computed with the method PolesCoefficients. Warning: To be used for BezierSurfaces ONLY!!!
        """
    @staticmethod
    def CoefsD2_s(U : float,V : float,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Point : OCP.gp.gp_Pnt,VecU : OCP.gp.gp_Vec,VecV : OCP.gp.gp_Vec,VecUU : OCP.gp.gp_Vec,VecUV : OCP.gp.gp_Vec,VecVV : OCP.gp.gp_Vec) -> None: 
        """
        Calls CacheD0 for Bezier Surfaces Arrays computed with the method PolesCoefficients. Warning: To be used for BezierSurfaces ONLY!!!
        """
    @staticmethod
    def D0_s(U : float,V : float,UIndex : int,VIndex : int,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,UDegree : int,VDegree : int,URat : bool,VRat : bool,UPer : bool,VPer : bool,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def D1_s(U : float,V : float,UIndex : int,VIndex : int,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,Degree : int,VDegree : int,URat : bool,VRat : bool,UPer : bool,VPer : bool,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D2_s(U : float,V : float,UIndex : int,VIndex : int,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,UDegree : int,VDegree : int,URat : bool,VRat : bool,UPer : bool,VPer : bool,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D3_s(U : float,V : float,UIndex : int,VIndex : int,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,UDegree : int,VDegree : int,URat : bool,VRat : bool,UPer : bool,VPer : bool,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec,Vuuu : OCP.gp.gp_Vec,Vvvv : OCP.gp.gp_Vec,Vuuv : OCP.gp.gp_Vec,Vuvv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def DN_s(U : float,V : float,Nu : int,Nv : int,UIndex : int,VIndex : int,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,UDegree : int,VDegree : int,URat : bool,VRat : bool,UPer : bool,VPer : bool,Vn : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def FunctionMultiply_s(Function : BSplSLib_EvaluatorFunction,UBSplineDegree : int,VBSplineDegree : int,UBSplineKnots : OCP.TColStd.TColStd_Array1OfReal,VBSplineKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UFlatKnots : OCP.TColStd.TColStd_Array1OfReal,VFlatKnots : OCP.TColStd.TColStd_Array1OfReal,UNewDegree : int,VNewDegree : int,NewNumerator : OCP.TColgp.TColgp_Array2OfPnt,NewDenominator : OCP.TColStd.TColStd_Array2OfReal) -> Tuple[int]: 
        """
        this will multiply a given BSpline numerator N(u,v) and denominator D(u,v) defined by its U/VBSplineDegree and U/VBSplineKnots, and U/VMults. Its Poles and Weights are arrays which are coded as array2 of the form [1..UNumPoles][1..VNumPoles] by a function a(u,v) which is assumed to satisfy the following : 1. a(u,v) * N(u,v) and a(u,v) * D(u,v) is a polynomial BSpline that can be expressed exactly as a BSpline of degree U/VNewDegree on the knots U/VFlatKnots 2. the range of a(u,v) is the same as the range of N(u,v) or D(u,v) ---Warning: it is the caller's responsability to insure that conditions 1. and 2. above are satisfied : no check whatsoever is made in this method -- theStatus will return 0 if OK else it will return the pivot index -- of the matrix that was inverted to compute the multiplied -- BSpline : the method used is interpolation at Schoenenberg -- points of a(u,v)* N(u,v) and a(u,v) * D(u,v) theStatus will return 0 if OK else it will return the pivot index of the matrix that was inverted to compute the multiplied BSpline : the method used is interpolation at Schoenenberg points of a(u,v)*F(u,v) --
        """
    @staticmethod
    @overload
    def GetPoles_s(FP : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array2OfPnt,UDirection : bool) -> None: 
        """
        Get from FP the coordinates of the poles.

        Get from FP the coordinates of the poles.
        """
    @staticmethod
    @overload
    def GetPoles_s(FP : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UDirection : bool) -> None: ...
    @staticmethod
    def HomogeneousD0_s(U : float,V : float,UIndex : int,VIndex : int,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,UDegree : int,VDegree : int,URat : bool,VRat : bool,UPer : bool,VPer : bool,P : OCP.gp.gp_Pnt) -> Tuple[float]: 
        """
        Makes an homogeneous evaluation of Poles and Weights any and returns in P the Numerator value and in W the Denominator value if Weights are present otherwise returns 1.0e0
        """
    @staticmethod
    def HomogeneousD1_s(U : float,V : float,UIndex : int,VIndex : int,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,UDegree : int,VDegree : int,URat : bool,VRat : bool,UPer : bool,VPer : bool,N : OCP.gp.gp_Pnt,Nu : OCP.gp.gp_Vec,Nv : OCP.gp.gp_Vec) -> Tuple[float, float, float]: 
        """
        Makes an homogeneous evaluation of Poles and Weights any and returns in P the Numerator value and in W the Denominator value if Weights are present otherwise returns 1.0e0
        """
    @staticmethod
    def IncreaseDegree_s(UDirection : bool,Degree : int,NewDegree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array2OfPnt,NewWeights : OCP.TColStd.TColStd_Array2OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    @staticmethod
    def InsertKnots_s(UDirection : bool,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,AddKnots : OCP.TColStd.TColStd_Array1OfReal,AddMults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array2OfPnt,NewWeights : OCP.TColStd.TColStd_Array2OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,Epsilon : float,Add : bool=True) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def Interpolate_s(UDegree : int,VDegree : int,UFlatKnots : OCP.TColStd.TColStd_Array1OfReal,VFlatKnots : OCP.TColStd.TColStd_Array1OfReal,UParameters : OCP.TColStd.TColStd_Array1OfReal,VParameters : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array2OfPnt) -> Tuple[int]: 
        """
        Performs the interpolation of the data points given in the Poles array in the form [1,...,RL][1,...,RC][1...PolesDimension] . The ColLength CL and the Length of UParameters must be the same. The length of VFlatKnots is VDegree + CL + 1.

        Performs the interpolation of the data points given in the Poles array. The ColLength CL and the Length of UParameters must be the same. The length of VFlatKnots is VDegree + CL + 1.
        """
    @staticmethod
    @overload
    def Interpolate_s(UDegree : int,VDegree : int,UFlatKnots : OCP.TColStd.TColStd_Array1OfReal,VFlatKnots : OCP.TColStd.TColStd_Array1OfReal,UParameters : OCP.TColStd.TColStd_Array1OfReal,VParameters : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal) -> Tuple[int]: ...
    @staticmethod
    def IsRational_s(Weights : OCP.TColStd.TColStd_Array2OfReal,I1 : int,I2 : int,J1 : int,J2 : int,Epsilon : float=0.0) -> bool: 
        """
        Returns False if all the weights of the array <Weights> in the area [I1,I2] * [J1,J2] are identic. Epsilon is used for comparing weights. If Epsilon is 0. the Epsilon of the first weight is used.
        """
    @staticmethod
    def Iso_s(Param : float,IsU : bool,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Degree : int,Periodic : bool,CPoles : OCP.TColgp.TColgp_Array1OfPnt,CWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Computes the poles and weights of an isoparametric curve at parameter <Param> (UIso if <IsU> is True, VIso else).
        """
    @staticmethod
    def MovePoint_s(U : float,V : float,Displ : OCP.gp.gp_Vec,UIndex1 : int,UIndex2 : int,VIndex1 : int,VIndex2 : int,UDegree : int,VDegree : int,Rational : bool,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UFlatKnots : OCP.TColStd.TColStd_Array1OfReal,VFlatKnots : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColgp.TColgp_Array2OfPnt) -> Tuple[int, int, int, int]: 
        """
        Find the new poles which allows an old point (with a given u,v as parameters) to reach a new position UIndex1,UIndex2 indicate the range of poles we can move for U (1, UNbPoles-1) or (2, UNbPoles) -> no constraint for one side in U (2, UNbPoles-1) -> the ends are enforced for U don't enter (1,NbPoles) and (1,VNbPoles) -> error: rigid move if problem in BSplineBasis calculation, no change for the curve and UFirstIndex, VLastIndex = 0 VFirstIndex, VLastIndex = 0
        """
    @staticmethod
    def NoWeights_s() -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        Used as argument for a non rational curve.
        """
    @staticmethod
    @overload
    def PolesCoefficients_s(Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,CachePoles : OCP.TColgp.TColgp_Array2OfPnt,CacheWeights : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        Warning! To be used for BezierSurfaces ONLY!!!

        Encapsulation of BuildCache to perform the evaluation of the Taylor expansion for beziersurfaces at parameters 0.,0.; Warning: To be used for BezierSurfaces ONLY!!!
        """
    @staticmethod
    @overload
    def PolesCoefficients_s(Poles : OCP.TColgp.TColgp_Array2OfPnt,CachePoles : OCP.TColgp.TColgp_Array2OfPnt) -> None: ...
    @staticmethod
    def RationalDerivative_s(UDeg : int,VDeg : int,N : int,M : int,All : bool=True) -> Tuple[float, float]: 
        """
        this is a one dimensional function typedef void (*EvaluatorFunction) ( Standard_Integer // Derivative Request Standard_Real * // StartEnd[2][2] // [0] = U // [1] = V // [0] = start // [1] = end Standard_Real // UParameter Standard_Real // VParamerer Standard_Real & // Result Standard_Integer &) ;// Error Code serves to multiply a given vectorial BSpline by a function Computes the derivatives of a ratio of two-variables functions x(u,v) / w(u,v) at orders <N,M>, x(u,v) is a vector in dimension <3>.
        """
    @staticmethod
    def RemoveKnot_s(UDirection : bool,Index : int,Mult : int,Degree : int,Periodic : bool,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NewPoles : OCP.TColgp.TColgp_Array2OfPnt,NewWeights : OCP.TColStd.TColStd_Array2OfReal,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,Tolerance : float) -> bool: 
        """
        None
        """
    @staticmethod
    def Resolution_s(Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,UDegree : int,VDegree : int,URat : bool,VRat : bool,UPer : bool,VPer : bool,Tolerance3D : float) -> Tuple[float, float]: 
        """
        Given a tolerance in 3D space returns two tolerances, one in U one in V such that for all (u1,v1) and (u0,v0) in the domain of the surface f(u,v) we have : | u1 - u0 | < UTolerance and | v1 - v0 | < VTolerance we have |f (u1,v1) - f (u0,v0)| < Tolerance3D
        """
    @staticmethod
    @overload
    def Reverse_s(Poles : OCP.TColgp.TColgp_Array2OfPnt,Last : int,UDirection : bool) -> None: 
        """
        Reverses the array of poles. Last is the Index of the new first Row( Col) of Poles. On a non periodic surface Last is Poles.Upper(). On a periodic curve last is (number of flat knots - degree - 1) or (sum of multiplicities(but for the last) + degree - 1)

        Reverses the array of weights.
        """
    @staticmethod
    @overload
    def Reverse_s(Weights : OCP.TColStd.TColStd_Array2OfReal,Last : int,UDirection : bool) -> None: ...
    @staticmethod
    @overload
    def SetPoles_s(Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,FP : OCP.TColStd.TColStd_Array1OfReal,UDirection : bool) -> None: 
        """
        Copy in FP the coordinates of the poles.

        Copy in FP the coordinates of the poles.
        """
    @staticmethod
    @overload
    def SetPoles_s(Poles : OCP.TColgp.TColgp_Array2OfPnt,FP : OCP.TColStd.TColStd_Array1OfReal,UDirection : bool) -> None: ...
    @staticmethod
    def Unperiodize_s(UDirection : bool,Degree : int,Mults : OCP.TColStd.TColStd_Array1OfInteger,Knots : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,NewMults : OCP.TColStd.TColStd_Array1OfInteger,NewKnots : OCP.TColStd.TColStd_Array1OfReal,NewPoles : OCP.TColgp.TColgp_Array2OfPnt,NewWeights : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BSplSLib_Cache(OCP.Standard.Standard_Transient):
    """
    A cache class for Bezier and B-spline surfaces.A cache class for Bezier and B-spline surfaces.
    """
    def BuildCache(self,theParameterU : float,theParameterV : float,theFlatKnotsU : OCP.TColStd.TColStd_Array1OfReal,theFlatKnotsV : OCP.TColStd.TColStd_Array1OfReal,thePoles : OCP.TColgp.TColgp_Array2OfPnt,theWeights : OCP.TColStd.TColStd_Array2OfReal=None) -> None: 
        """
        Recomputes the cache data. Does not verify validity of the cache
        """
    def D0(self,theU : float,theV : float,thePoint : OCP.gp.gp_Pnt) -> None: 
        """
        Calculates the point on the surface for specified parameters
        """
    def D1(self,theU : float,theV : float,thePoint : OCP.gp.gp_Pnt,theTangentU : OCP.gp.gp_Vec,theTangentV : OCP.gp.gp_Vec) -> None: 
        """
        Calculates the point on the surface and its first derivative
        """
    def D2(self,theU : float,theV : float,thePoint : OCP.gp.gp_Pnt,theTangentU : OCP.gp.gp_Vec,theTangentV : OCP.gp.gp_Vec,theCurvatureU : OCP.gp.gp_Vec,theCurvatureV : OCP.gp.gp_Vec,theCurvatureUV : OCP.gp.gp_Vec) -> None: 
        """
        Calculates the point on the surface and derivatives till second order
        """
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
    def IsCacheValid(self,theParameterU : float,theParameterV : float) -> bool: 
        """
        Verifies validity of the cache using parameters of the point
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theDegreeU : int,thePeriodicU : bool,theFlatKnotsU : OCP.TColStd.TColStd_Array1OfReal,theDegreeV : int,thePeriodicV : bool,theFlatKnotsV : OCP.TColStd.TColStd_Array1OfReal,theWeights : OCP.TColStd.TColStd_Array2OfReal=None) -> None: ...
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
class BSplSLib_EvaluatorFunction():
    """
    None
    """
    def Evaluate(self,theDerivativeRequest : int,theUParameter : float,theVParameter : float) -> Tuple[float, int]: 
        """
        Function evaluation method to be defined by descendant
        """
    def __init__(self) -> None: ...
    pass
