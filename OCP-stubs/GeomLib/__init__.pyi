import OCP.GeomLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.AdvApprox
import OCP.Geom2d
import OCP.gp
import OCP.TColgp
import OCP.Geom
import OCP.TColStd
import OCP.math
__all__  = [
"GeomLib",
"GeomLib_Array1OfMat",
"GeomLib_Check2dBSplineCurve",
"GeomLib_CheckBSplineCurve",
"GeomLib_CheckCurveOnSurface",
"GeomLib_DenominatorMultiplier",
"GeomLib_Interpolate",
"GeomLib_InterpolationErrors",
"GeomLib_IsPlanarSurface",
"GeomLib_LogSample",
"GeomLib_MakeCurvefromApprox",
"GeomLib_PolyFunc",
"GeomLib_Tool",
"GeomLib_DegreeSmallerThan3",
"GeomLib_InversionProblem",
"GeomLib_NoError",
"GeomLib_NotEnoughtPoints"
]
class GeomLib():
    """
    Geom Library. This package provides an implementation of functions for basic computation on geometric entity from packages Geom and Geom2d.
    """
    @staticmethod
    def AdjustExtremity_s(Curve : OCP.Geom.Geom_BoundedCurve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,T1 : OCP.gp.gp_Vec,T2 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def AxeOfInertia_s(Points : OCP.TColgp.TColgp_Array1OfPnt,Axe : OCP.gp.gp_Ax2,Tol : float=1e-07) -> Tuple[bool]: 
        """
        Compute axes of inertia, of some points -- -- -- <Axe>.Location() is the BaryCentre -- -- -- -- -- <Axe>.XDirection is the axe of upper inertia -- -- -- -- <Axe>.Direction is the Normal to the average plane -- -- -- IsSingular is True if points are on line -- Tol is used to determine singular cases.
        """
    @staticmethod
    def BuildCurve3d_s(Tolerance : float,CurvePtr : OCP.Adaptor3d.Adaptor3d_CurveOnSurface,FirstParameter : float,LastParameter : float,NewCurvePtr : OCP.Geom.Geom_Curve,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1,MaxDegree : int=14,MaxSegment : int=30) -> Tuple[float, float]: 
        """
        None
        """
    @staticmethod
    def CancelDenominatorDerivative_s(BSurf : OCP.Geom.Geom_BSplineSurface,UDirection : bool,VDirection : bool) -> None: 
        """
        Cancel,on the boudaries,the denominator first derivative in the directions wished by the user and set its value to 1.
        """
    @staticmethod
    def DensifyArray1OfReal_s(MinNumPoints : int,InParameters : OCP.TColStd.TColStd_Array1OfReal,OutParameters : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        this makes sure that there is at least MinNumPoints in OutParameters taking into account the parameters in the InParameters array provided those are in order, that is the sequence of real in the InParameter is strictly non decreasing
        """
    @staticmethod
    def EvalMaxDistanceAlongParameter_s(Curve : OCP.Adaptor3d.Adaptor3d_Curve,AReferenceCurve : OCP.Adaptor3d.Adaptor3d_Curve,Tolerance : float,Parameters : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float]: 
        """
        this will compute the maximum distancef at the parameters given in the Parameters array by projecting from the Curve to the reference curve and taking the minimum distance Than the maximum will be taken on those minimas.
        """
    @staticmethod
    def EvalMaxParametricDistance_s(Curve : OCP.Adaptor3d.Adaptor3d_Curve,AReferenceCurve : OCP.Adaptor3d.Adaptor3d_Curve,Tolerance : float,Parameters : OCP.TColStd.TColStd_Array1OfReal) -> Tuple[float]: 
        """
        this will compute the maximum distance at the parameters given in the Parameters array by evaluating each parameter the two curves and taking the maximum of the evaluated distance
        """
    @staticmethod
    def ExtendCurveToPoint_s(Curve : OCP.Geom.Geom_BoundedCurve,Point : OCP.gp.gp_Pnt,Cont : int,After : bool) -> None: 
        """
        Extends the bounded curve Curve to the point Point. The extension is built: - at the end of the curve if After equals true, or - at the beginning of the curve if After equals false. The extension is performed according to a degree of continuity equal to Cont, which in its turn must be equal to 1, 2 or 3. This function converts the bounded curve Curve into a BSpline curve. Warning - Nothing is done, and Curve is not modified if Cont is not equal to 1, 2 or 3. - It is recommended that the extension should not be too large with respect to the size of the bounded curve Curve: Point must not be located too far from one of the extremities of Curve.
        """
    @staticmethod
    def ExtendSurfByLength_s(Surf : OCP.Geom.Geom_BoundedSurface,Length : float,Cont : int,InU : bool,After : bool) -> None: 
        """
        Extends the bounded surface Surf along one of its boundaries. The chord length of the extension is equal to Length. The direction of the extension is given as: - the u parametric direction of Surf, if InU equals true, or - the v parametric direction of Surf, if InU equals false. In this parametric direction, the extension is built on the side of: - the last parameter of Surf, if After equals true, or - the first parameter of Surf, if After equals false. The extension is performed according to a degree of continuity equal to Cont, which in its turn must be equal to 1, 2 or 3. This function converts the bounded surface Surf into a BSpline surface. Warning - Nothing is done, and Surf is not modified if Cont is not equal to 1, 2 or 3. - It is recommended that Length, the size of the extension should not be too large with respect to the size of the bounded surface Surf. - Surf must not be a periodic BSpline surface in the parametric direction corresponding to the direction of extension.
        """
    @staticmethod
    def FuseIntervals_s(Interval1 : OCP.TColStd.TColStd_Array1OfReal,Interval2 : OCP.TColStd.TColStd_Array1OfReal,Fusion : OCP.TColStd.TColStd_SequenceOfReal,Confusion : float=1e-09) -> None: 
        """
        None
        """
    @staticmethod
    def GTransform_s(Curve : OCP.Geom2d.Geom2d_Curve,GTrsf : OCP.gp.gp_GTrsf2d) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Computes the curve 3d from package Geom corresponding to the curve 3d from package Geom, transformed with the transformation <GTrsf> WARNING : this method may return a null Handle if it's impossible to compute the transformation of a curve. It's not implemented when : 1) the curve is an infinite parabola or hyperbola 2) the curve is an offsetcurve
        """
    @staticmethod
    def Inertia_s(Points : OCP.TColgp.TColgp_Array1OfPnt,Bary : OCP.gp.gp_Pnt,XDir : OCP.gp.gp_Dir,YDir : OCP.gp.gp_Dir) -> Tuple[float, float, float]: 
        """
        Compute principale axes of inertia, and dispertion value of some points.
        """
    @staticmethod
    def IsBSplUClosed_s(S : OCP.Geom.Geom_BSplineSurface,U1 : float,U2 : float,Tol : float) -> bool: 
        """
        Returns true if the poles of U1 isoline and the poles of U2 isoline of surface are identical according to tolerance criterion. For rational surfaces Weights(i)*Poles(i) are checked.
        """
    @staticmethod
    def IsBSplVClosed_s(S : OCP.Geom.Geom_BSplineSurface,V1 : float,V2 : float,Tol : float) -> bool: 
        """
        Returns true if the poles of V1 isoline and the poles of V2 isoline of surface are identical according to tolerance criterion. For rational surfaces Weights(i)*Poles(i) are checked.
        """
    @staticmethod
    def IsBzUClosed_s(S : OCP.Geom.Geom_BezierSurface,U1 : float,U2 : float,Tol : float) -> bool: 
        """
        Returns true if the poles of U1 isoline and the poles of U2 isoline of surface are identical according to tolerance criterion.
        """
    @staticmethod
    def IsBzVClosed_s(S : OCP.Geom.Geom_BezierSurface,V1 : float,V2 : float,Tol : float) -> bool: 
        """
        Returns true if the poles of V1 isoline and the poles of V2 isoline of surface are identical according to tolerance criterion.
        """
    @staticmethod
    def IsClosed_s(S : OCP.Geom.Geom_Surface,Tol : float) -> Tuple[bool, bool]: 
        """
        This method defines if opposite boundaries of surface coincide with given tolerance
        """
    @staticmethod
    def NormEstim_s(S : OCP.Geom.Geom_Surface,UV : OCP.gp.gp_Pnt2d,Tol : float,N : OCP.gp.gp_Dir) -> int: 
        """
        None
        """
    @staticmethod
    def RemovePointsFromArray_s(NumPoints : int,InParameters : OCP.TColStd.TColStd_Array1OfReal,OutParameters : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Warning! This assume that the InParameter is an increasing sequence of real number and it will not check for that : Unpredictable result can happen if this is not satisfied. It is the caller responsability to check for that property.
        """
    @staticmethod
    def SameRange_s(Tolerance : float,Curve2dPtr : OCP.Geom2d.Geom2d_Curve,First : float,Last : float,RequestedFirst : float,RequestedLast : float,NewCurve2dPtr : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Make the curve Curve2dPtr have the imposed range First to List the most economic way, that is if it can change the range without changing the nature of the curve it will try to do that. Otherwise it will produce a Bspline curve that has the required range
        """
    @staticmethod
    def To3d_s(Position : OCP.gp.gp_Ax2,Curve2d : OCP.Geom2d.Geom2d_Curve) -> OCP.Geom.Geom_Curve: 
        """
        Computes the curve 3d from package Geom corresponding to curve 2d from package Geom2d, on the plan defined with the local coordinate system Position.
        """
    def __init__(self) -> None: ...
    pass
class GeomLib_Array1OfMat():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : GeomLib_Array1OfMat) -> GeomLib_Array1OfMat: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.gp.gp_Mat: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.gp.gp_Mat: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_Mat: 
        """
        Variable value access
        """
    def First(self) -> OCP.gp.gp_Mat: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.gp.gp_Mat) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> OCP.gp.gp_Mat: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : GeomLib_Array1OfMat) -> GeomLib_Array1OfMat: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_Mat) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> OCP.gp.gp_Mat: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : GeomLib_Array1OfMat) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.gp.gp_Mat,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class GeomLib_Check2dBSplineCurve():
    """
    Checks for the end tangents : wether or not those are reversed
    """
    def FixTangent(self,FirstFlag : bool,LastFlag : bool) -> None: 
        """
        None
        """
    def FixedTangent(self,FirstFlag : bool,LastFlag : bool) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        modifies the curve by fixing the first or the last tangencies
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def NeedTangentFix(self) -> Tuple[bool, bool]: 
        """
        None
        """
    def __init__(self,Curve : OCP.Geom2d.Geom2d_BSplineCurve,Tolerance : float,AngularTolerance : float) -> None: ...
    pass
class GeomLib_CheckBSplineCurve():
    """
    Checks for the end tangents : wether or not those are reversed regarding the third or n-3rd control
    """
    def FixTangent(self,FirstFlag : bool,LastFlag : bool) -> None: 
        """
        None
        """
    def FixedTangent(self,FirstFlag : bool,LastFlag : bool) -> OCP.Geom.Geom_BSplineCurve: 
        """
        modifies the curve by fixing the first or the last tangencies
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def NeedTangentFix(self) -> Tuple[bool, bool]: 
        """
        None
        """
    def __init__(self,Curve : OCP.Geom.Geom_BSplineCurve,Tolerance : float,AngularTolerance : float) -> None: ...
    pass
class GeomLib_CheckCurveOnSurface():
    """
    Computes the max distance between 3D-curve and 2D-curve in some surface.
    """
    def Curve(self) -> OCP.Geom.Geom_Curve: 
        """
        Returns my3DCurve
        """
    def ErrorStatus(self) -> int: 
        """
        Returns error status The possible values are: 0 - OK; 1 - null curve or surface or 2d curve; 2 - invalid parametric range; 3 - error in calculations.
        """
    @overload
    def Init(self,theCurve : OCP.Geom.Geom_Curve,theSurface : OCP.Geom.Geom_Surface,theFirst : float,theLast : float,theTolRange : float=9.999999999999999e-10) -> None: 
        """
        Sets the data for the algorithm

        Initializes all members by dafault values
        """
    @overload
    def Init(self) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the max distance has been found
        """
    def MaxDistance(self) -> float: 
        """
        Returns max distance
        """
    def MaxParameter(self) -> float: 
        """
        Returns parameter in which the distance is maximal
        """
    def Perform(self,thePCurve : OCP.Geom2d.Geom2d_Curve,isTheMultyTheradDisabled : bool=False) -> None: 
        """
        Computes the max distance for the 3d curve <myCurve> and 2d curve <thePCurve> If isTheMultyTheadDisabled == TRUE then computation will be made without any parallelization.
        """
    def Range(self) -> Tuple[float, float]: 
        """
        Returns first and last parameter of the curves (2D- and 3D-curves are considered to have same range)
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        Returns mySurface
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCurve : OCP.Geom.Geom_Curve,theSurface : OCP.Geom.Geom_Surface,theFirst : float,theLast : float,theTolRange : float=9.999999999999999e-10) -> None: ...
    pass
class GeomLib_DenominatorMultiplier():
    """
    this defines an evaluator for a function of 2 variables that will be used by CancelDenominatorDerivative in one direction.
    """
    def Value(self,UParameter : float,VParameter : float) -> float: 
        """
        Returns the value of a(UParameter,VParameter)=
        """
    def __init__(self,Surface : OCP.Geom.Geom_BSplineSurface,KnotVector : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    pass
class GeomLib_Interpolate():
    """
    this class is used to construct a BSpline curve by interpolation of points at given parameters The continuity of the curve is degree - 1 and the method used when boundary condition are not given is to use odd degrees and null the derivatives on both sides from degree -1 down to (degree+1) / 2 When even degree is given the returned curve is of degree - 1 so that the degree of the curve is odd
    """
    def Curve(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        returns the interpolated curve of the requested degree
        """
    def Error(self) -> GeomLib_InterpolationErrors: 
        """
        returns the error type if any

        returns the error type if any
        """
    def IsDone(self) -> bool: 
        """
        returns if everything went OK

        returns if everything went OK
        """
    def __init__(self,Degree : int,NumPoints : int,Points : OCP.TColgp.TColgp_Array1OfPnt,Parameters : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    pass
class GeomLib_InterpolationErrors():
    """
    in case the interpolation errors out, this tells what happened

    Members:

      GeomLib_NoError

      GeomLib_NotEnoughtPoints

      GeomLib_DegreeSmallerThan3

      GeomLib_InversionProblem
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    GeomLib_DegreeSmallerThan3: OCP.GeomLib.GeomLib_InterpolationErrors # value = GeomLib_InterpolationErrors.GeomLib_DegreeSmallerThan3
    GeomLib_InversionProblem: OCP.GeomLib.GeomLib_InterpolationErrors # value = GeomLib_InterpolationErrors.GeomLib_InversionProblem
    GeomLib_NoError: OCP.GeomLib.GeomLib_InterpolationErrors # value = GeomLib_InterpolationErrors.GeomLib_NoError
    GeomLib_NotEnoughtPoints: OCP.GeomLib.GeomLib_InterpolationErrors # value = GeomLib_InterpolationErrors.GeomLib_NotEnoughtPoints
    __entries: dict # value = {'GeomLib_NoError': (GeomLib_InterpolationErrors.GeomLib_NoError, None), 'GeomLib_NotEnoughtPoints': (GeomLib_InterpolationErrors.GeomLib_NotEnoughtPoints, None), 'GeomLib_DegreeSmallerThan3': (GeomLib_InterpolationErrors.GeomLib_DegreeSmallerThan3, None), 'GeomLib_InversionProblem': (GeomLib_InterpolationErrors.GeomLib_InversionProblem, None)}
    __members__: dict # value = {'GeomLib_NoError': GeomLib_InterpolationErrors.GeomLib_NoError, 'GeomLib_NotEnoughtPoints': GeomLib_InterpolationErrors.GeomLib_NotEnoughtPoints, 'GeomLib_DegreeSmallerThan3': GeomLib_InterpolationErrors.GeomLib_DegreeSmallerThan3, 'GeomLib_InversionProblem': GeomLib_InterpolationErrors.GeomLib_InversionProblem}
    pass
class GeomLib_IsPlanarSurface():
    """
    Find if a surface is a planar surface.
    """
    def IsPlanar(self) -> bool: 
        """
        Return if the Surface is a plan
        """
    def Plan(self) -> OCP.gp.gp_Pln: 
        """
        Return the plan definition
        """
    def __init__(self,S : OCP.Geom.Geom_Surface,Tol : float=1e-07) -> None: ...
    pass
class GeomLib_LogSample(OCP.math.math_FunctionSample):
    """
    None
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        Returns the bounds of parameters.
        """
    def GetParameter(self,Index : int) -> float: 
        """
        Returns the value of parameter of the point of range Index : A + ((Index-1)/(NbPoints-1))*B. An exception is raised if Index<=0 or Index>NbPoints.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of sample points.
        """
    def __init__(self,A : float,B : float,N : int) -> None: ...
    pass
class GeomLib_MakeCurvefromApprox():
    """
    this class is used to construct the BSpline curve from an Approximation ( ApproxAFunction from AdvApprox).
    """
    @overload
    def Curve(self,Index3d : int) -> OCP.Geom.Geom_BSplineCurve: 
        """
        returns a polynomial curve whose poles correspond to the Index3D 3D space if Index3D not in the Range [1,Nb3dSpaces] if the Approx is not Done

        returns a rational curve whose poles correspond to the index3D of the 3D space and whose weights correspond to the index1d 1D space. if Index1D not in the Range [1,Nb1dSpaces] if Index3D not in the Range [1,Nb3dSpaces] if the Approx is not Done
        """
    @overload
    def Curve(self,Index1D : int,Index3D : int) -> OCP.Geom.Geom_BSplineCurve: ...
    @overload
    def Curve2d(self,Index1d : int,Index2d : int) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        returns a polynomial curve whose poles correspond to the Index2d 2D space if Index2d not in the Range [1,Nb2dSpaces] if the Approx is not Done

        returns a rational curve whose poles correspond to the index2d of the 2D space and whose weights correspond to one dimensional space of index 1d if Index1d not in the Range [1,Nb1dSpaces] if Index2d not in the Range [1,Nb2dSpaces] if the Approx is not Done
        """
    @overload
    def Curve2d(self,Index2d : int) -> OCP.Geom2d.Geom2d_BSplineCurve: ...
    def Curve2dFromTwo1d(self,Index1d : int,Index2d : int) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        returns a 2D curve building it from the 1D curve in x at Index1d and y at Index2d amongst the 1D curves if Index1d not in the Range [1,Nb1dSpaces] if Index2d not in the Range [1,Nb1dSpaces] if the Approx is not Done
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def Nb1DSpaces(self) -> int: 
        """
        returns the number of 1D spaces of the Approx
        """
    def Nb2DSpaces(self) -> int: 
        """
        returns the number of 3D spaces of the Approx
        """
    def Nb3DSpaces(self) -> int: 
        """
        returns the number of 3D spaces of the Approx
        """
    def __init__(self,Approx : OCP.AdvApprox.AdvApprox_ApproxAFunction) -> None: ...
    pass
class GeomLib_PolyFunc(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    Polynomial Function
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        computes the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        computes the value <F>of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        computes the value <F> and the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def __init__(self,Coeffs : OCP.math.math_Vector) -> None: ...
    pass
class GeomLib_Tool():
    """
    Provides various methods with Geom2d and Geom curves and surfaces. The methods of this class compute the parameter(s) of a given point on a curve or a surface. To get the valid result the point must be located rather close to the curve (surface) or at least to allow getting unambiguous result (do not put point at center of circle...), but choice of "trust" distance between curve/surface and point is responcibility of user (parameter MaxDist). Return FALSE if the point is beyond the MaxDist limit or if computation fails.
    """
    @staticmethod
    @overload
    def Parameter_s(Curve : OCP.Geom.Geom_Curve,Point : OCP.gp.gp_Pnt,MaxDist : float,U : float) -> bool: 
        """
        Extracts the parameter of a 3D point lying on a 3D curve or at a distance less than the MaxDist value.

        Extracts the parameter of a 2D point lying on a 2D curve or at a distance less than the MaxDist value.
        """
    @staticmethod
    @overload
    def Parameter_s(Curve : OCP.Geom2d.Geom2d_Curve,Point : OCP.gp.gp_Pnt2d,MaxDist : float,U : float) -> bool: ...
    @staticmethod
    def Parameters_s(Surface : OCP.Geom.Geom_Surface,Point : OCP.gp.gp_Pnt,MaxDist : float,U : float,V : float) -> bool: 
        """
        Extracts the parameter of a 3D point lying on a surface or at a distance less than the MaxDist value.
        """
    def __init__(self) -> None: ...
    pass
GeomLib_DegreeSmallerThan3: OCP.GeomLib.GeomLib_InterpolationErrors # value = GeomLib_InterpolationErrors.GeomLib_DegreeSmallerThan3
GeomLib_InversionProblem: OCP.GeomLib.GeomLib_InterpolationErrors # value = GeomLib_InterpolationErrors.GeomLib_InversionProblem
GeomLib_NoError: OCP.GeomLib.GeomLib_InterpolationErrors # value = GeomLib_InterpolationErrors.GeomLib_NoError
GeomLib_NotEnoughtPoints: OCP.GeomLib.GeomLib_InterpolationErrors # value = GeomLib_InterpolationErrors.GeomLib_NotEnoughtPoints
