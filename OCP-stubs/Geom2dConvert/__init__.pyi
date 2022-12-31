import OCP.Geom2dConvert
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.gp
import OCP.Geom2d
import OCP.GeomAbs
import io
import OCP.TColGeom2d
import OCP.TColStd
import OCP.Adaptor2d
__all__  = [
"Geom2dConvert",
"Geom2dConvert_ApproxArcsSegments",
"Geom2dConvert_ApproxCurve",
"Geom2dConvert_BSplineCurveKnotSplitting",
"Geom2dConvert_BSplineCurveToBezierCurve",
"Geom2dConvert_CompCurveToBSplineCurve",
"Geom2dConvert_PPoint",
"Geom2dConvert_SequenceOfPPoint"
]
class Geom2dConvert():
    """
    This package provides an implementation of algorithms to do the conversion between equivalent geometric entities from package Geom2d. It gives the possibility : . to obtain the B-spline representation of bounded curves. . to split a B-spline curve into several B-spline curves with some constraints of continuity, . to convert a B-spline curve into several Bezier curves or surfaces. All the geometric entities used in this package are bounded. References : . Generating the Bezier Points of B-spline curves and surfaces (Wolfgang Bohm) CAGD volume 13 number 6 november 1981 . On NURBS: A Survey (Leslie Piegl) IEEE Computer Graphics and Application January 1991 . Curve and surface construction using rational B-splines (Leslie Piegl and Wayne Tiller) CAD Volume 19 number 9 november 1987 . A survey of curve and surface methods in CAGD (Wolfgang BOHM) CAGD 1 1984
    """
    @staticmethod
    @overload
    def C0BSplineToArrayOfC1BSplineCurve_s(BS : OCP.Geom2d.Geom2d_BSplineCurve,tabBS : OCP.TColGeom2d.TColGeom2d_HArray1OfBSplineCurve,AngularTolerance : float,Tolerance : float) -> None: 
        """
        This Method reduces as far as it is possible the multiplicities of the knots of the BSpline BS.(keeping the geometry). It returns an array of BSpline C1. Tolerance is a geometrical tolerance

        This Method reduces as far as it is possible the multiplicities of the knots of the BSpline BS.(keeping the geometry). It returns an array of BSpline C1. tolerance is a geometrical tolerance
        """
    @staticmethod
    @overload
    def C0BSplineToArrayOfC1BSplineCurve_s(BS : OCP.Geom2d.Geom2d_BSplineCurve,tabBS : OCP.TColGeom2d.TColGeom2d_HArray1OfBSplineCurve,Tolerance : float) -> None: ...
    @staticmethod
    def C0BSplineToC1BSplineCurve_s(BS : OCP.Geom2d.Geom2d_BSplineCurve,Tolerance : float) -> None: 
        """
        This Method reduces as far as it is possible the multiplicities of the knots of the BSpline BS.(keeping the geometry). It returns a new BSpline which could still be C0. tolerance is a geometrical tolerance
        """
    @staticmethod
    @overload
    def ConcatC1_s(ArrayOfCurves : OCP.TColGeom2d.TColGeom2d_Array1OfBSplineCurve,ArrayOfToler : OCP.TColStd.TColStd_Array1OfReal,ArrayOfIndices : OCP.TColStd.TColStd_HArray1OfInteger,ArrayOfConcatenated : OCP.TColGeom2d.TColGeom2d_HArray1OfBSplineCurve,ClosedTolerance : float) -> Tuple[bool]: 
        """
        This Method concatenates C1 the ArrayOfCurves as far as it is possible. ArrayOfCurves[0..N-1] ArrayOfToler contains the biggest tolerance of the two points shared by two consecutives curves. Its dimension: [0..N-2] ClosedFlag indicates if the ArrayOfCurves is closed. In this case ClosedTolerance contains the biggest tolerance of the two points which are at the closure. Otherwise its value is 0.0 ClosedFlag becomes False on the output if it is impossible to build closed curve.

        This Method concatenates C1 the ArrayOfCurves as far as it is possible. ArrayOfCurves[0..N-1] ArrayOfToler contains the biggest tolerance of the two points shared by two consecutives curves. Its dimension: [0..N-2] ClosedFlag indicates if the ArrayOfCurves is closed. In this case ClosedTolerance contains the biggest tolerance of the two points which are at the closure. Otherwise its value is 0.0 ClosedFlag becomes False on the output if it is impossible to build closed curve.
        """
    @staticmethod
    @overload
    def ConcatC1_s(ArrayOfCurves : OCP.TColGeom2d.TColGeom2d_Array1OfBSplineCurve,ArrayOfToler : OCP.TColStd.TColStd_Array1OfReal,ArrayOfIndices : OCP.TColStd.TColStd_HArray1OfInteger,ArrayOfConcatenated : OCP.TColGeom2d.TColGeom2d_HArray1OfBSplineCurve,ClosedTolerance : float,AngularTolerance : float) -> Tuple[bool]: ...
    @staticmethod
    def ConcatG1_s(ArrayOfCurves : OCP.TColGeom2d.TColGeom2d_Array1OfBSplineCurve,ArrayOfToler : OCP.TColStd.TColStd_Array1OfReal,ArrayOfConcatenated : OCP.TColGeom2d.TColGeom2d_HArray1OfBSplineCurve,ClosedTolerance : float) -> Tuple[bool]: 
        """
        This Method concatenates G1 the ArrayOfCurves as far as it is possible. ArrayOfCurves[0..N-1] ArrayOfToler contains the biggest tolerance of the two points shared by two consecutives curves. Its dimension: [0..N-2] ClosedFlag indicates if the ArrayOfCurves is closed. In this case ClosedTolerance contains the biggest tolerance of the two points which are at the closure. Otherwise its value is 0.0 ClosedFlag becomes False on the output if it is impossible to build closed curve.
        """
    @staticmethod
    def CurveToBSplineCurve_s(C : OCP.Geom2d.Geom2d_Curve,Parameterisation : OCP.Convert.Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        This function converts a non infinite curve from Geom into a B-spline curve. C must be an ellipse or a circle or a trimmed conic or a trimmed line or a Bezier curve or a trimmed Bezier curve or a BSpline curve or a trimmed BSpline curve or an Offset curve or a trimmed Offset curve. The returned B-spline is not periodic except if C is a Circle or an Ellipse. ParameterisationType applies only if the curve is a Circle or an ellipse : TgtThetaOver2, TgtThetaOver2_1, TgtThetaOver2_2, TgtThetaOver2_3, TgtThetaOver2_4, Purpose: this is the classical rational parameterisation 2 1 - t cos(theta) = ------ 2 1 + t
        """
    @staticmethod
    @overload
    def SplitBSplineCurve_s(C : OCP.Geom2d.Geom2d_BSplineCurve,FromK1 : int,ToK2 : int,SameOrientation : bool=True) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        -- Convert a curve to BSpline by Approximation

        This function computes the segment of B-spline curve between the parametric values FromU1, ToU2. If C is periodic the arc has the same orientation as C if SameOrientation = True. If C is not periodic SameOrientation is not used for the computation and C is oriented fromU1 toU2. If U1 and U2 and two parametric values we consider that U1 = U2 if Abs (U1 - U2) <= ParametricTolerance and ParametricTolerance must be greater or equal to Resolution from package gp.
        """
    @staticmethod
    @overload
    def SplitBSplineCurve_s(C : OCP.Geom2d.Geom2d_BSplineCurve,FromU1 : float,ToU2 : float,ParametricTolerance : float,SameOrientation : bool=True) -> OCP.Geom2d.Geom2d_BSplineCurve: ...
    def __init__(self) -> None: ...
    pass
class Geom2dConvert_ApproxArcsSegments():
    """
    Approximation of a free-form curve by a sequence of arcs+segments.
    """
    class Status_e():
        """
        None

        Members:

          StatusOK

          StatusNotDone

          StatusError
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
        StatusError: OCP.Geom2dConvert.Status_e # value = <Status_e.StatusError: 2>
        StatusNotDone: OCP.Geom2dConvert.Status_e # value = <Status_e.StatusNotDone: 1>
        StatusOK: OCP.Geom2dConvert.Status_e # value = <Status_e.StatusOK: 0>
        __entries: dict # value = {'StatusOK': (<Status_e.StatusOK: 0>, None), 'StatusNotDone': (<Status_e.StatusNotDone: 1>, None), 'StatusError': (<Status_e.StatusError: 2>, None)}
        __members__: dict # value = {'StatusOK': <Status_e.StatusOK: 0>, 'StatusNotDone': <Status_e.StatusNotDone: 1>, 'StatusError': <Status_e.StatusError: 2>}
        pass
    def GetResult(self) -> OCP.TColGeom2d.TColGeom2d_SequenceOfCurve: 
        """
        Get the result curve after approximation.
        """
    def __init__(self,theCurve : OCP.Adaptor2d.Adaptor2d_Curve2d,theTolerance : float,theAngleTol : float) -> None: ...
    StatusError: OCP.Geom2dConvert.Status_e # value = <Status_e.StatusError: 2>
    StatusNotDone: OCP.Geom2dConvert.Status_e # value = <Status_e.StatusNotDone: 1>
    StatusOK: OCP.Geom2dConvert.Status_e # value = <Status_e.StatusOK: 0>
    pass
class Geom2dConvert_ApproxCurve():
    """
    A framework to convert a 2D curve to a BSpline. This is done by approximation within a given tolerance.
    """
    def Curve(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns the 2D BSpline curve resulting from the approximation algorithm.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Print on the stream o information about the object
        """
    def HasResult(self) -> bool: 
        """
        returns Standard_True if the approximation did come out with a result that is not NECESSARELY within the required tolerance
        """
    def IsDone(self) -> bool: 
        """
        returns Standard_True if the approximation has been done with within required tolerance
        """
    def MaxError(self) -> float: 
        """
        Returns the greatest distance between a point on the source conic and the BSpline curve resulting from the approximation. (>0 when an approximation has been done, 0 if no approximation)
        """
    @overload
    def __init__(self,Curve : OCP.Geom2d.Geom2d_Curve,Tol2d : float,Order : OCP.GeomAbs.GeomAbs_Shape,MaxSegments : int,MaxDegree : int) -> None: ...
    @overload
    def __init__(self,Curve : OCP.Adaptor2d.Adaptor2d_Curve2d,Tol2d : float,Order : OCP.GeomAbs.GeomAbs_Shape,MaxSegments : int,MaxDegree : int) -> None: ...
    pass
class Geom2dConvert_BSplineCurveKnotSplitting():
    """
    An algorithm to determine points at which a BSpline curve should be split in order to obtain arcs of the same continuity. If you require curves with a minimum continuity for your computation, it is useful to know the points between which an arc has a continuity of a given order. The continuity order is given at the construction time. For a BSpline curve, the discontinuities are localized at the knot values. Between two knot values the BSpline is infinitely and continuously differentiable. At a given knot, the continuity is equal to: Degree - Mult, where Degree is the degree of the BSpline curve and Mult is the multiplicity of the knot. It is possible to compute the arcs which correspond to this splitting using the global function SplitBSplineCurve provided by the package Geom2dConvert. A BSplineCurveKnotSplitting object provides a framework for: - defining the curve to be analysed and the required degree of continuity, - implementing the computation algorithm, and - consulting the results.
    """
    def NbSplits(self) -> int: 
        """
        Returns the number of points at which the analysed BSpline curve should be split, in order to obtain arcs with the continuity required by this framework. All these points correspond to knot values. Note that the first and last points of the curve, which bound the first and last arcs, are counted among these splitting points.
        """
    def SplitValue(self,Index : int) -> int: 
        """
        Returns the split knot of index Index to the split knots table computed in this framework. The returned value is an index in the knots table of the BSpline curve analysed by this algorithm. Notes: - If Index is equal to 1, the corresponding knot gives the first point of the curve. - If Index is equal to the number of split knots computed in this framework, the corresponding point is the last point of the curve. Exceptions Standard_RangeError if Index is less than 1 or greater than the number of split knots computed in this framework.
        """
    def Splitting(self,SplitValues : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Loads the SplitValues table with the split knots values computed in this framework. Each value in the table is an index in the knots table of the BSpline curve analysed by this algorithm. The values in SplitValues are given in ascending order and comprise the indices of the knots which give the first and last points of the curve. Use two consecutive values from the table as arguments of the global function SplitBSplineCurve (provided by the package Geom2dConvert) to split the curve. Exceptions Standard_DimensionError if the array SplitValues was not created with the following bounds: - 1, and - the number of split points computed in this framework (as given by the function NbSplits).
        """
    def __init__(self,BasisCurve : OCP.Geom2d.Geom2d_BSplineCurve,ContinuityRange : int) -> None: ...
    pass
class Geom2dConvert_BSplineCurveToBezierCurve():
    """
    An algorithm to convert a BSpline curve into a series of adjacent Bezier curves. A BSplineCurveToBezierCurve object provides a framework for: - defining the BSpline curve to be converted - implementing the construction algorithm, and - consulting the results. References : Generating the Bezier points of B-spline curves and surfaces (Wolfgang Bohm) CAD volume 13 number 6 november 1981
    """
    def Arc(self,Index : int) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Constructs and returns the Bezier curve of index Index to the table of adjacent Bezier arcs computed by this algorithm. This Bezier curve has the same orientation as the BSpline curve analyzed in this framework. Exceptions Standard_OutOfRange if Index is less than 1 or greater than the number of adjacent Bezier arcs computed by this algorithm.
        """
    def Arcs(self,Curves : OCP.TColGeom2d.TColGeom2d_Array1OfBezierCurve) -> None: 
        """
        Constructs all the Bezier curves whose data is computed by this algorithm and loads these curves into the Curves table. The Bezier curves have the same orientation as the BSpline curve analyzed in this framework. Exceptions Standard_DimensionError if the Curves array was not created with the following bounds: - 1 , and - the number of adjacent Bezier arcs computed by this algorithm (as given by the function NbArcs).
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        This methode returns the bspline's knots associated to the converted arcs Raises DimensionError if the length of Curves is not equal to NbArcs + 1
        """
    def NbArcs(self) -> int: 
        """
        Returns the number of BezierCurve arcs. If at the creation time you have decomposed the basis curve between the parametric values UFirst, ULast the number of BezierCurve arcs depends on the number of knots included inside the interval [UFirst, ULast]. If you have decomposed the whole basis B-spline curve the number of BezierCurve arcs NbArcs is equal to the number of knots less one.
        """
    @overload
    def __init__(self,BasisCurve : OCP.Geom2d.Geom2d_BSplineCurve,U1 : float,U2 : float,ParametricTolerance : float) -> None: ...
    @overload
    def __init__(self,BasisCurve : OCP.Geom2d.Geom2d_BSplineCurve) -> None: ...
    pass
class Geom2dConvert_CompCurveToBSplineCurve():
    """
    This algorithm converts and concat several curve in an BSplineCurve
    """
    def Add(self,NewCurve : OCP.Geom2d.Geom2d_BoundedCurve,Tolerance : float,After : bool=False) -> bool: 
        """
        Append a curve in the BSpline Return False if the curve is not G0 with the BSplineCurve. Tolerance is used to check continuity and decrease Multiplicty at the common Knot After is useful if BasisCurve is a closed curve .
        """
    def BSplineCurve(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Clear result curve
        """
    @overload
    def __init__(self,Parameterisation : OCP.Convert.Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> None: ...
    @overload
    def __init__(self,BasisCurve : OCP.Geom2d.Geom2d_BoundedCurve,Parameterisation : OCP.Convert.Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> None: ...
    pass
class Geom2dConvert_PPoint():
    """
    Class representing a point on curve, with 2D coordinate and the tangent
    """
    def D1(self) -> OCP.gp.gp_XY: 
        """
        Query the first derivatives.
        """
    def Dist(self,theOth : Geom2dConvert_PPoint) -> float: 
        """
        Compute the distance betwwen two 2d points.
        """
    def Parameter(self) -> float: 
        """
        Query the parmeter value.
        """
    def Point(self) -> OCP.gp.gp_XY: 
        """
        Query the point location.
        """
    def SetD1(self,theD1 : OCP.gp.gp_XY) -> None: 
        """
        Change the value of the derivative at the point.
        """
    @overload
    def __init__(self,theParameter : float,thePoint : OCP.gp.gp_XY,theD1 : OCP.gp.gp_XY) -> None: ...
    @overload
    def __init__(self,theParameter : float,theAdaptor : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Geom2dConvert_SequenceOfPPoint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Geom2dConvert_PPoint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Geom2dConvert_SequenceOfPPoint) -> None: ...
    def Assign(self,theOther : Geom2dConvert_SequenceOfPPoint) -> Geom2dConvert_SequenceOfPPoint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Geom2dConvert_PPoint: 
        """
        First item access
        """
    def ChangeLast(self) -> Geom2dConvert_PPoint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Geom2dConvert_PPoint: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> Geom2dConvert_PPoint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Geom2dConvert_PPoint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Geom2dConvert_SequenceOfPPoint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Geom2dConvert_SequenceOfPPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Geom2dConvert_PPoint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Geom2dConvert_PPoint: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : Geom2dConvert_PPoint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Geom2dConvert_SequenceOfPPoint) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Geom2dConvert_PPoint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Geom2dConvert_SequenceOfPPoint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Geom2dConvert_PPoint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Geom2dConvert_SequenceOfPPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
