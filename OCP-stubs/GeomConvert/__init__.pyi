import OCP.GeomConvert
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.TColgp
import OCP.Geom
import OCP.TColStd
import OCP.GeomAbs
import OCP.TColGeom
__all__  = [
"GeomConvert",
"GeomConvert_ApproxCurve",
"GeomConvert_ApproxSurface",
"GeomConvert_BSplineCurveKnotSplitting",
"GeomConvert_BSplineCurveToBezierCurve",
"GeomConvert_BSplineSurfaceKnotSplitting",
"GeomConvert_BSplineSurfaceToBezierSurface",
"GeomConvert_CompBezierSurfacesToBSplineSurface",
"GeomConvert_CompCurveToBSplineCurve"
]
class GeomConvert():
    """
    The GeomConvert package provides some global functions as follows - converting classical Geom curves into BSpline curves, - segmenting BSpline curves, particularly at knots values: this function may be used in conjunction with the GeomConvert_BSplineCurveKnotSplitting class to segment a BSpline curve into arcs which comply with required continuity levels, - converting classical Geom surfaces into BSpline surfaces, and - segmenting BSpline surfaces, particularly at knots values: this function may be used in conjunction with the GeomConvert_BSplineSurfaceKnotSplitting class to segment a BSpline surface into patches which comply with required continuity levels. All geometric entities used in this package are bounded.
    """
    @staticmethod
    @overload
    def C0BSplineToArrayOfC1BSplineCurve_s(BS : OCP.Geom.Geom_BSplineCurve,tabBS : OCP.TColGeom.TColGeom_HArray1OfBSplineCurve,tolerance : float) -> None: 
        """
        This Method reduces as far as it is possible the multiplicities of the knots of the BSpline BS.(keeping the geometry). It returns an array of BSpline C1. tolerance is a geometrical tolerance.

        This Method reduces as far as it is possible the multiplicities of the knots of the BSpline BS.(keeping the geometry). It returns an array of BSpline C1. tolerance is a geometrical tolerance : it allows for the maximum deformation The Angular tolerance is in radians and mesures the angle of the tangents on the left and on the right to decide if the curve is C1 or not at a given point
        """
    @staticmethod
    @overload
    def C0BSplineToArrayOfC1BSplineCurve_s(BS : OCP.Geom.Geom_BSplineCurve,tabBS : OCP.TColGeom.TColGeom_HArray1OfBSplineCurve,AngularTolerance : float,tolerance : float) -> None: ...
    @staticmethod
    def C0BSplineToC1BSplineCurve_s(BS : OCP.Geom.Geom_BSplineCurve,tolerance : float,AngularTolerance : float=1e-07) -> None: 
        """
        This Method reduces as far as it is possible the multiplicities of the knots of the BSpline BS.(keeping the geometry). It returns a new BSpline which could still be C0. tolerance is a geometrical tolerance. The Angular toleranceis in radians and mesures the angle of the tangents on the left and on the right to decide if the curve is G1 or not at a given point
        """
    @staticmethod
    @overload
    def ConcatC1_s(ArrayOfCurves : OCP.TColGeom.TColGeom_Array1OfBSplineCurve,ArrayOfToler : OCP.TColStd.TColStd_Array1OfReal,ArrayOfIndices : OCP.TColStd.TColStd_HArray1OfInteger,ArrayOfConcatenated : OCP.TColGeom.TColGeom_HArray1OfBSplineCurve,ClosedTolerance : float,AngularTolerance : float) -> Tuple[bool]: 
        """
        This Method concatenates C1 the ArrayOfCurves as far as it is possible. ArrayOfCurves[0..N-1] ArrayOfToler contains the biggest tolerance of the two points shared by two consecutives curves. Its dimension: [0..N-2] ClosedFlag indicates if the ArrayOfCurves is closed. In this case ClosedTolerance contains the biggest tolerance of the two points which are at the closure. Otherwise its value is 0.0 ClosedFlag becomes False on the output if it is impossible to build closed curve.

        This Method concatenates C1 the ArrayOfCurves as far as it is possible. ArrayOfCurves[0..N-1] ArrayOfToler contains the biggest tolerance of the two points shared by two consecutives curves. Its dimension: [0..N-2] ClosedFlag indicates if the ArrayOfCurves is closed. In this case ClosedTolerance contains the biggest tolerance of the two points which are at the closure. Otherwise its value is 0.0 ClosedFlag becomes False on the output if it is impossible to build closed curve.
        """
    @staticmethod
    @overload
    def ConcatC1_s(ArrayOfCurves : OCP.TColGeom.TColGeom_Array1OfBSplineCurve,ArrayOfToler : OCP.TColStd.TColStd_Array1OfReal,ArrayOfIndices : OCP.TColStd.TColStd_HArray1OfInteger,ArrayOfConcatenated : OCP.TColGeom.TColGeom_HArray1OfBSplineCurve,ClosedTolerance : float) -> Tuple[bool]: ...
    @staticmethod
    def ConcatG1_s(ArrayOfCurves : OCP.TColGeom.TColGeom_Array1OfBSplineCurve,ArrayOfToler : OCP.TColStd.TColStd_Array1OfReal,ArrayOfConcatenated : OCP.TColGeom.TColGeom_HArray1OfBSplineCurve,ClosedTolerance : float) -> Tuple[bool]: 
        """
        This Method concatenates G1 the ArrayOfCurves as far as it is possible. ArrayOfCurves[0..N-1] ArrayOfToler contains the biggest tolerance of the two points shared by two consecutives curves. Its dimension: [0..N-2] ClosedFlag indicates if the ArrayOfCurves is closed. In this case ClosedTolerance contains the biggest tolerance of the two points which are at the closure. Otherwise its value is 0.0 ClosedFlag becomes False on the output if it is impossible to build closed curve.
        """
    @staticmethod
    def CurveToBSplineCurve_s(C : OCP.Geom.Geom_Curve,Parameterisation : OCP.Convert.Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> OCP.Geom.Geom_BSplineCurve: 
        """
        This function converts a non infinite curve from Geom into a B-spline curve. C must be an ellipse or a circle or a trimmed conic or a trimmed line or a Bezier curve or a trimmed Bezier curve or a BSpline curve or a trimmed BSpline curve or an OffsetCurve. The returned B-spline is not periodic except if C is a Circle or an Ellipse. If the Parameterisation is QuasiAngular than the returned curve is NOT periodic in case a periodic Geom_Circle or Geom_Ellipse. For TgtThetaOver2_1 and TgtThetaOver2_2 the method raises an exception in case of a periodic Geom_Circle or a Geom_Ellipse ParameterisationType applies only if the curve is a Circle or an ellipse : TgtThetaOver2, -- TgtThetaOver2_1, -- TgtThetaOver2_2, -- TgtThetaOver2_3, -- TgtThetaOver2_4,
        """
    @staticmethod
    @overload
    def SplitBSplineCurve_s(C : OCP.Geom.Geom_BSplineCurve,FromK1 : int,ToK2 : int,SameOrientation : bool=True) -> OCP.Geom.Geom_BSplineCurve: 
        """
        Convert a curve from Geom by an approximation method

        This function computes the segment of B-spline curve between the parametric values FromU1, ToU2. If C is periodic the arc has the same orientation as C if SameOrientation = True. If C is not periodic SameOrientation is not used for the computation and C is oriented fromU1 toU2. If U1 and U2 and two parametric values we consider that U1 = U2 if Abs (U1 - U2) <= ParametricTolerance and ParametricTolerance must be greater or equal to Resolution from package gp.
        """
    @staticmethod
    @overload
    def SplitBSplineCurve_s(C : OCP.Geom.Geom_BSplineCurve,FromU1 : float,ToU2 : float,ParametricTolerance : float,SameOrientation : bool=True) -> OCP.Geom.Geom_BSplineCurve: ...
    @staticmethod
    @overload
    def SplitBSplineSurface_s(S : OCP.Geom.Geom_BSplineSurface,FromUK1 : int,ToUK2 : int,FromVK1 : int,ToVK2 : int,SameUOrientation : bool=True,SameVOrientation : bool=True) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Computes the B-spline surface patche between the knots values FromUK1, ToUK2, FromVK1, ToVK2. If S is periodic in one direction the patche has the same orientation as S in this direction if the flag is true in this direction (SameUOrientation, SameVOrientation). If S is not periodic SameUOrientation and SameVOrientation are not used for the computation and S is oriented FromUK1 ToUK2 and FromVK1 ToVK2. Raised if FromUK1 = ToUK2 or FromVK1 = ToVK2 FromUK1 or ToUK2 are out of the bounds [FirstUKnotIndex, LastUKnotIndex] FromVK1 or ToVK2 are out of the bounds [FirstVKnotIndex, LastVKnotIndex]

        This method splits a B-spline surface patche between the knots values FromK1, ToK2 in one direction. If USplit = True then the splitting direction is the U parametric direction else it is the V parametric direction. If S is periodic in the considered direction the patche has the same orientation as S in this direction if SameOrientation is True If S is not periodic in this direction SameOrientation is not used for the computation and S is oriented FromK1 ToK2. Raised if FromK1 = ToK2 or if FromK1 or ToK2 are out of the bounds [FirstUKnotIndex, LastUKnotIndex] in the considered parametric direction.

        This method computes the B-spline surface patche between the parametric values FromU1, ToU2, FromV1, ToV2. If S is periodic in one direction the patche has the same orientation as S in this direction if the flag is True in this direction (SameUOrientation, SameVOrientation). If S is not periodic SameUOrientation and SameVOrientation are not used for the computation and S is oriented FromU1 ToU2 and FromV1 ToV2. If U1 and U2 and two parametric values we consider that U1 = U2 if Abs (U1 - U2) <= ParametricTolerance and ParametricTolerance must be greater or equal to Resolution from package gp.

        This method splits the B-spline surface S in one direction between the parametric values FromParam1, ToParam2. If USplit = True then the Splitting direction is the U parametric direction else it is the V parametric direction. If S is periodic in the considered direction the patche has the same orientation as S in this direction if SameOrientation is true. If S is not periodic in the considered direction SameOrientation is not used for the computation and S is oriented FromParam1 ToParam2. If U1 and U2 and two parametric values we consider that U1 = U2 if Abs (U1 - U2) <= ParametricTolerance and ParametricTolerance must be greater or equal to Resolution from package gp.
        """
    @staticmethod
    @overload
    def SplitBSplineSurface_s(S : OCP.Geom.Geom_BSplineSurface,FromParam1 : float,ToParam2 : float,USplit : bool,ParametricTolerance : float,SameOrientation : bool=True) -> OCP.Geom.Geom_BSplineSurface: ...
    @staticmethod
    @overload
    def SplitBSplineSurface_s(S : OCP.Geom.Geom_BSplineSurface,FromU1 : float,ToU2 : float,FromV1 : float,ToV2 : float,ParametricTolerance : float,SameUOrientation : bool=True,SameVOrientation : bool=True) -> OCP.Geom.Geom_BSplineSurface: ...
    @staticmethod
    @overload
    def SplitBSplineSurface_s(S : OCP.Geom.Geom_BSplineSurface,FromK1 : int,ToK2 : int,USplit : bool,SameOrientation : bool=True) -> OCP.Geom.Geom_BSplineSurface: ...
    @staticmethod
    def SurfaceToBSplineSurface_s(S : OCP.Geom.Geom_Surface) -> OCP.Geom.Geom_BSplineSurface: 
        """
        This algorithm converts a non infinite surface from Geom into a B-spline surface. S must be a trimmed plane or a trimmed cylinder or a trimmed cone or a trimmed sphere or a trimmed torus or a sphere or a torus or a Bezier surface of a trimmed Bezier surface or a trimmed swept surface with a corresponding basis curve which can be turned into a B-spline curve (see the method CurveToBSplineCurve). Raises DomainError if the type of the surface is not previously defined.
        """
    def __init__(self) -> None: ...
    pass
class GeomConvert_ApproxCurve():
    """
    A framework to convert a 3D curve to a 3D BSpline. This is done by approximation to a BSpline curve within a given tolerance.
    """
    def Curve(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        Returns the BSpline curve resulting from the approximation algorithm.
        """
    def Dump(self,o : Any) -> None: 
        """
        Print on the stream o information about the object
        """
    def HasResult(self) -> bool: 
        """
        Returns Standard_True if the approximation did come out with a result that is not NECESSARELY within the required tolerance
        """
    def IsDone(self) -> bool: 
        """
        returns Standard_True if the approximation has been done within requiered tolerance
        """
    def MaxError(self) -> float: 
        """
        Returns the greatest distance between a point on the source conic and the BSpline curve resulting from the approximation. (>0 when an approximation has been done, 0 if no approximation)
        """
    @overload
    def __init__(self,Curve : OCP.Geom.Geom_Curve,Tol3d : float,Order : OCP.GeomAbs.GeomAbs_Shape,MaxSegments : int,MaxDegree : int) -> None: ...
    @overload
    def __init__(self,Curve : OCP.Adaptor3d.Adaptor3d_HCurve,Tol3d : float,Order : OCP.GeomAbs.GeomAbs_Shape,MaxSegments : int,MaxDegree : int) -> None: ...
    pass
class GeomConvert_ApproxSurface():
    """
    A framework to convert a surface to a BSpline surface. This is done by approximation to a BSpline surface within a given tolerance.
    """
    def Dump(self,o : Any) -> None: 
        """
        Prints on the stream o informations on the current state of the object.
        """
    def HasResult(self) -> bool: 
        """
        Returns true if the approximation did come out with a result that is not NECESSARILY within the required tolerance or a result that is not recognized with the wished continuities.
        """
    def IsDone(self) -> bool: 
        """
        Returns Standard_True if the approximation has be done
        """
    def MaxError(self) -> float: 
        """
        Returns the greatest distance between a point on the source conic surface and the BSpline surface resulting from the approximation (>0 when an approximation has been done, 0 if no approximation )
        """
    def Surface(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Returns the BSpline surface resulting from the approximation algorithm.
        """
    @overload
    def __init__(self,Surf : OCP.Geom.Geom_Surface,Tol3d : float,UContinuity : OCP.GeomAbs.GeomAbs_Shape,VContinuity : OCP.GeomAbs.GeomAbs_Shape,MaxDegU : int,MaxDegV : int,MaxSegments : int,PrecisCode : int) -> None: ...
    @overload
    def __init__(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,Tol3d : float,UContinuity : OCP.GeomAbs.GeomAbs_Shape,VContinuity : OCP.GeomAbs.GeomAbs_Shape,MaxDegU : int,MaxDegV : int,MaxSegments : int,PrecisCode : int) -> None: ...
    pass
class GeomConvert_BSplineCurveKnotSplitting():
    """
    An algorithm to determine points at which a BSpline curve should be split in order to obtain arcs of the same continuity. If you require curves with a minimum continuity for your computation, it is useful to know the points between which an arc has a continuity of a given order. The continuity order is given at the construction time. For a BSpline curve, the discontinuities are localized at the knot values. Between two knot values the BSpline is infinitely and continuously differentiable. At a given knot, the continuity is equal to: Degree - Mult, where Degree is the degree of the BSpline curve and Mult is the multiplicity of the knot. It is possible to compute the arcs which correspond to this splitting using the global function SplitBSplineCurve provided by the package GeomConvert. A BSplineCurveKnotSplitting object provides a framework for: - defining the curve to be analyzed and the required degree of continuity, - implementing the computation algorithm, and - consulting the results.
    """
    def NbSplits(self) -> int: 
        """
        Returns the number of points at which the analyzed BSpline curve should be split, in order to obtain arcs with the continuity required by this framework. All these points correspond to knot values. Note that the first and last points of the curve, which bound the first and last arcs, are counted among these splitting points.
        """
    def SplitValue(self,Index : int) -> int: 
        """
        Returns the split knot of index Index to the split knots table computed in this framework. The returned value is an index in the knots table of the BSpline curve analyzed by this algorithm. Notes: - If Index is equal to 1, the corresponding knot gives the first point of the curve. - If Index is equal to the number of split knots computed in this framework, the corresponding point is the last point of the curve. Exceptions Standard_RangeError if Index is less than 1 or greater than the number of split knots computed in this framework.
        """
    def Splitting(self,SplitValues : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Loads the SplitValues table with the split knots values computed in this framework. Each value in the table is an index in the knots table of the BSpline curve analyzed by this algorithm. The values in SplitValues are given in ascending order and comprise the indices of the knots which give the first and last points of the curve. Use two consecutive values from the table as arguments of the global function SplitBSplineCurve (provided by the package GeomConvert) to split the curve. Exceptions Standard_DimensionError if the array SplitValues was not created with the following bounds: - 1, and - the number of split points computed in this framework (as given by the function NbSplits).
        """
    def __init__(self,BasisCurve : OCP.Geom.Geom_BSplineCurve,ContinuityRange : int) -> None: ...
    pass
class GeomConvert_BSplineCurveToBezierCurve():
    """
    An algorithm to convert a BSpline curve into a series of adjacent Bezier curves. A BSplineCurveToBezierCurve object provides a framework for: - defining the BSpline curve to be converted - implementing the construction algorithm, and - consulting the results. References : Generating the Bezier points of B-spline curves and surfaces (Wolfgang Bohm) CAD volume 13 number 6 november 1981
    """
    def Arc(self,Index : int) -> OCP.Geom.Geom_BezierCurve: 
        """
        Constructs and returns the Bezier curve of index Index to the table of adjacent Bezier arcs computed by this algorithm. This Bezier curve has the same orientation as the BSpline curve analyzed in this framework. Exceptions Standard_OutOfRange if Index is less than 1 or greater than the number of adjacent Bezier arcs computed by this algorithm.
        """
    def Arcs(self,Curves : OCP.TColGeom.TColGeom_Array1OfBezierCurve) -> None: 
        """
        Constructs all the Bezier curves whose data is computed by this algorithm and loads these curves into the Curves table. The Bezier curves have the same orientation as the BSpline curve analyzed in this framework. Exceptions Standard_DimensionError if the Curves array was not created with the following bounds: - 1 , and - the number of adjacent Bezier arcs computed by this algorithm (as given by the function NbArcs).
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        This methode returns the bspline's knots associated to the converted arcs Raised if the length of Curves is not equal to NbArcs + 1.
        """
    def NbArcs(self) -> int: 
        """
        Returns the number of BezierCurve arcs. If at the creation time you have decomposed the basis curve between the parametric values UFirst, ULast the number of BezierCurve arcs depends on the number of knots included inside the interval [UFirst, ULast]. If you have decomposed the whole basis B-spline curve the number of BezierCurve arcs NbArcs is equal to the number of knots less one.
        """
    @overload
    def __init__(self,BasisCurve : OCP.Geom.Geom_BSplineCurve) -> None: ...
    @overload
    def __init__(self,BasisCurve : OCP.Geom.Geom_BSplineCurve,U1 : float,U2 : float,ParametricTolerance : float) -> None: ...
    pass
class GeomConvert_BSplineSurfaceKnotSplitting():
    """
    An algorithm to determine isoparametric curves along which a BSpline surface should be split in order to obtain patches of the same continuity. The continuity order is given at the construction time. It is possible to compute the surface patches corresponding to the splitting with the method of package SplitBSplineSurface. For a B-spline surface the discontinuities are localised at the knot values. Between two knots values the B-spline is infinitely continuously differentiable. For each parametric direction at a knot of range index the continuity in this direction is equal to : Degree - Mult (Index) where Degree is the degree of the basis B-spline functions and Mult the multiplicity of the knot of range Index in the given direction. If for your computation you need to have B-spline surface with a minima of continuity it can be interesting to know between which knot values, a B-spline patch, has a continuity of given order. This algorithm computes the indexes of the knots where you should split the surface, to obtain patches with a constant continuity given at the construction time. If you just want to compute the local derivatives on the surface you don't need to create the BSpline patches, you can use the functions LocalD1, LocalD2, LocalD3, LocalDN of the class BSplineSurface from package Geom.
    """
    def NbUSplits(self) -> int: 
        """
        Returns the number of u-isoparametric curves along which the analysed BSpline surface should be split in order to obtain patches with the continuity required by this framework. The parameters which define these curves are knot values in the corresponding parametric direction. Note that the four curves which bound the surface are counted among these splitting curves.
        """
    def NbVSplits(self) -> int: 
        """
        Returns the number of v-isoparametric curves along which the analysed BSpline surface should be split in order to obtain patches with the continuity required by this framework. The parameters which define these curves are knot values in the corresponding parametric direction. Note that the four curves which bound the surface are counted among these splitting curves.
        """
    def Splitting(self,USplit : OCP.TColStd.TColStd_Array1OfInteger,VSplit : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Loads the USplit and VSplit tables with the split knots values computed in this framework. Each value in these tables is an index in the knots table corresponding to the u or v parametric direction of the BSpline surface analysed by this algorithm. The USplit and VSplit values are given in ascending order and comprise the indices of the knots which give the first and last isoparametric curves of the surface in the corresponding parametric direction. Use two consecutive values from the USplit table and two consecutive values from the VSplit table as arguments of the global function SplitBSplineSurface (provided by the package GeomConvert) to split the surface. Exceptions Standard_DimensionError if: - the array USplit was not created with the following bounds: - 1 , and - the number of split knots in the u parametric direction computed in this framework (as given by the function NbUSplits); or - the array VSplit was not created with the following bounds: - 1 , and - the number of split knots in the v parametric direction computed in this framework (as given by the function NbVSplits).
        """
    def USplitValue(self,UIndex : int) -> int: 
        """
        Returns the split knot of index UIndex to the split knots table for the u parametric direction computed in this framework. The returned value is an index in the knots table relative to the u parametric direction of the BSpline surface analysed by this algorithm. Note: If UIndex is equal to 1, or to the number of split knots for the u parametric direction computed in this framework, the corresponding knot gives the parameter of one of the bounding curves of the surface. Exceptions Standard_RangeError if UIndex is less than 1 or greater than the number of split knots for the u parametric direction computed in this framework.
        """
    def VSplitValue(self,VIndex : int) -> int: 
        """
        Returns the split knot of index VIndex to the split knots table for the v parametric direction computed in this framework. The returned value is an index in the knots table relative to the v parametric direction of the BSpline surface analysed by this algorithm. Note: If UIndex is equal to 1, or to the number of split knots for the v parametric direction computed in this framework, the corresponding knot gives the parameter of one of the bounding curves of the surface. Exceptions Standard_RangeError if VIndex is less than 1 or greater than the number of split knots for the v parametric direction computed in this framework.
        """
    def __init__(self,BasisSurface : OCP.Geom.Geom_BSplineSurface,UContinuityRange : int,VContinuityRange : int) -> None: ...
    pass
class GeomConvert_BSplineSurfaceToBezierSurface():
    """
    This algorithm converts a B-spline surface into several Bezier surfaces. It uses an algorithm of knot insertion. A BSplineSurfaceToBezierSurface object provides a framework for: - defining the BSpline surface to be converted, - implementing the construction algorithm, and - consulting the results. References : Generating the Bezier points of B-spline curves and surfaces (Wolfgang Bohm) CAD volume 13 number 6 november 1981
    """
    def NbUPatches(self) -> int: 
        """
        Returns the number of Bezier surfaces in the U direction. If at the creation time you have decomposed the basis Surface between the parametric values UFirst, ULast the number of Bezier surfaces in the U direction depends on the number of knots included inside the interval [UFirst, ULast]. If you have decomposed the whole basis B-spline surface the number of Bezier surfaces NbUPatches is equal to the number of UKnots less one.
        """
    def NbVPatches(self) -> int: 
        """
        Returns the number of Bezier surfaces in the V direction. If at the creation time you have decomposed the basis surface between the parametric values VFirst, VLast the number of Bezier surfaces in the V direction depends on the number of knots included inside the interval [VFirst, VLast]. If you have decomposed the whole basis B-spline surface the number of Bezier surfaces NbVPatches is equal to the number of VKnots less one.
        """
    def Patch(self,UIndex : int,VIndex : int) -> OCP.Geom.Geom_BezierSurface: 
        """
        Constructs and returns the Bezier surface of indices (UIndex, VIndex) to the patch grid computed on the BSpline surface analyzed by this algorithm. This Bezier surface has the same orientation as the BSpline surface analyzed in this framework. UIndex is an index common to a row in the patch grid. A row in the grid corresponds to a series of adjacent patches, all limited by the same two u-isoparametric curves of the surface. VIndex is an index common to a column in the patch grid. A column in the grid corresponds to a series of adjacent patches, all limited by the same two v-isoparametric curves of the surface. Exceptions Standard_OutOfRange if: - UIndex is less than 1 or greater than the number of rows in the patch grid computed on the BSpline surface analyzed by this algorithm (as returned by the function NbUPatches); or if - VIndex is less than 1 or greater than the number of columns in the patch grid computed on the BSpline surface analyzed by this algorithm (as returned by the function NbVPatches).
        """
    def Patches(self,Surfaces : OCP.TColGeom.TColGeom_Array2OfBezierSurface) -> None: 
        """
        Constructs all the Bezier surfaces whose data is computed by this algorithm, and loads them into the Surfaces table. These Bezier surfaces have the same orientation as the BSpline surface analyzed in this framework. The Surfaces array is organised in the same way as the patch grid computed on the BSpline surface analyzed by this algorithm. A row in the array corresponds to a series of adjacent patches, all limited by the same two u-isoparametric curves of the surface. A column in the array corresponds to a series of adjacent patches, all limited by the same two v-isoparametric curves of the surface. Exceptions Standard_DimensionError if the Surfaces array was not created with the following bounds: - 1, and the number of adjacent patch series in the u parametric direction of the patch grid computed on the BSpline surface, analyzed by this algorithm (as given by the function NbUPatches) as row bounds, - 1, and the number of adjacent patch series in the v parametric direction of the patch grid computed on the BSpline surface, analyzed by this algorithm (as given by the function NbVPatches) as column bounds.
        """
    def UKnots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        This methode returns the bspline's u-knots associated to the converted Patches Raised if the length of Curves is not equal to NbUPatches + 1.
        """
    def VKnots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        This methode returns the bspline's v-knots associated to the converted Patches Raised if the length of Curves is not equal to NbVPatches + 1.
        """
    @overload
    def __init__(self,BasisSurface : OCP.Geom.Geom_BSplineSurface) -> None: ...
    @overload
    def __init__(self,BasisSurface : OCP.Geom.Geom_BSplineSurface,U1 : float,U2 : float,V1 : float,V2 : float,ParametricTolerance : float) -> None: ...
    pass
class GeomConvert_CompBezierSurfacesToBSplineSurface():
    """
    An algorithm to convert a grid of adjacent non-rational Bezier surfaces (with continuity CM) into a BSpline surface (with continuity CM). A CompBezierSurfacesToBSplineSurface object provides a framework for: - defining the grid of adjacent Bezier surfaces which is to be converted into a BSpline surface, - implementing the computation algorithm, and - consulting the results. Warning Do not attempt to convert rational Bezier surfaces using such an algorithm. Input is array of Bezier patch 1 2 3 4 -> VIndex [1, NbVPatches] -> VDirection ----------------------- 1 | | | | | ----------------------- 2 | | | | | ----------------------- 3 | | | | | ----------------------- UIndex [1, NbUPatches] Udirection
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the conversion was successful. Unless an exception was raised at the time of construction, the conversion of the Bezier surface grid assigned to this algorithm is always carried out. IsDone returns false if the constraints defined at the time of construction cannot be respected. This occurs when there is an incompatibility between a required degree of continuity on the BSpline surface, and the maximum tolerance accepted for local deformations of the surface. In such a case the computed data does not satisfy all the initial constraints.
        """
    def NbUKnots(self) -> int: 
        """
        Returns the number of knots in the U direction of the BSpline surface whose data is computed in this framework.

        Returns the number of knots in the U direction of the BSpline surface whose data is computed in this framework.
        """
    def NbUPoles(self) -> int: 
        """
        Returns number of poles in the U direction of the BSpline surface whose data is computed in this framework.

        Returns number of poles in the U direction of the BSpline surface whose data is computed in this framework.
        """
    def NbVKnots(self) -> int: 
        """
        Returns the number of knots in the V direction of the BSpline surface whose data is computed in this framework.

        Returns the number of knots in the V direction of the BSpline surface whose data is computed in this framework.
        """
    def NbVPoles(self) -> int: 
        """
        Returns the number of poles in the V direction of the BSpline surface whose data is computed in this framework.

        Returns the number of poles in the V direction of the BSpline surface whose data is computed in this framework.
        """
    def Poles(self) -> OCP.TColgp.TColgp_HArray2OfPnt: 
        """
        Returns the table of poles of the BSpline surface whose data is computed in this framework.

        Returns the table of poles of the BSpline surface whose data is computed in this framework.
        """
    def UDegree(self) -> int: 
        """
        Returns the degree for the u parametric direction of the BSpline surface whose data is computed in this framework.

        Returns the degree for the u parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def UKnots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the knots table for the u parametric direction of the BSpline surface whose data is computed in this framework.

        Returns the knots table for the u parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def UMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Returns the multiplicities table for the u parametric direction of the knots of the BSpline surface whose data is computed in this framework.

        Returns the multiplicities table for the u parametric direction of the knots of the BSpline surface whose data is computed in this framework.
        """
    def VDegree(self) -> int: 
        """
        Returns the degree for the v parametric direction of the BSpline surface whose data is computed in this framework.

        Returns the degree for the v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def VKnots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the knots table for the v parametric direction of the BSpline surface whose data is computed in this framework.

        Returns the knots table for the v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def VMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        -- Returns the multiplicities table for the v parametric direction of the knots of the BSpline surface whose data is computed in this framework.

        -- Returns the multiplicities table for the v parametric direction of the knots of the BSpline surface whose data is computed in this framework.
        """
    @overload
    def __init__(self,Beziers : OCP.TColGeom.TColGeom_Array2OfBezierSurface) -> None: ...
    @overload
    def __init__(self,Beziers : OCP.TColGeom.TColGeom_Array2OfBezierSurface,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C0,VContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C0,Tolerance : float=0.0001) -> None: ...
    @overload
    def __init__(self,Beziers : OCP.TColGeom.TColGeom_Array2OfBezierSurface,Tolerance : float,RemoveKnots : bool=True) -> None: ...
    pass
class GeomConvert_CompCurveToBSplineCurve():
    """
    Algorithm converts and concat several curve in an BSplineCurve
    """
    def Add(self,NewCurve : OCP.Geom.Geom_BoundedCurve,Tolerance : float,After : bool=False,WithRatio : bool=True,MinM : int=0) -> bool: 
        """
        Append a curve in the BSpline Return False if the curve is not G0 with the BSplineCurve. Tolerance is used to check continuity and decrease Multiplicity at the common Knot until MinM if MinM = 0, the common Knot can be removed
        """
    def BSplineCurve(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Clear a result curve
        """
    @overload
    def __init__(self,BasisCurve : OCP.Geom.Geom_BoundedCurve,Parameterisation : OCP.Convert.Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> None: ...
    @overload
    def __init__(self,Parameterisation : OCP.Convert.Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> None: ...
    pass
