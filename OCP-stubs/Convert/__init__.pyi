import OCP.Convert
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TColStd
import OCP.TColgp
import OCP.gp
__all__  = [
"Convert_ConicToBSplineCurve",
"Convert_CompBezierCurves2dToBSplineCurve2d",
"Convert_CompBezierCurvesToBSplineCurve",
"Convert_CompPolynomialToPoles",
"Convert_ElementarySurfaceToBSplineSurface",
"Convert_CircleToBSplineCurve",
"Convert_CylinderToBSplineSurface",
"Convert_ConeToBSplineSurface",
"Convert_EllipseToBSplineCurve",
"Convert_GridPolynomialToPoles",
"Convert_HyperbolaToBSplineCurve",
"Convert_ParabolaToBSplineCurve",
"Convert_ParameterisationType",
"Convert_SequenceOfArray1OfPoles",
"Convert_SphereToBSplineSurface",
"Convert_TorusToBSplineSurface",
"BuildPolynomialCosAndSin",
"Convert_Polynomial",
"Convert_QuasiAngular",
"Convert_RationalC1",
"Convert_TgtThetaOver2",
"Convert_TgtThetaOver2_1",
"Convert_TgtThetaOver2_2",
"Convert_TgtThetaOver2_3",
"Convert_TgtThetaOver2_4"
]
class Convert_ConicToBSplineCurve():
    """
    Root class for algorithms which convert a conic curve into a BSpline curve (CircleToBSplineCurve, EllipseToBSplineCurve, HyperbolaToBSplineCurve, ParabolaToBSplineCurve). These algorithms all work on 2D curves from the gp package and compute all the data needed to construct a BSpline curve equivalent to the conic curve. This data consists of: - the degree of the curve, - the periodic characteristics of the curve, - a poles table with associated weights, - a knots table with associated multiplicities. The abstract class ConicToBSplineCurve provides a framework for storing and consulting this computed data. The data may then be used to construct a Geom2d_BSplineCurve curvSuper class of the following classes : This abstract class implements the methods to get the geometric representation of the B-spline curve equivalent to the conic. The B-spline is computed at the creation time in the sub classes. The B-spline curve is defined with its degree, its control points (Poles), its weights, its knots and their multiplicity. All the geometric entities used in this package are defined in 2D space. KeyWords : Convert, Conic, BSplineCurve, 2D.
    """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: 
        """
        None

        None
        """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,UFirst : float,ULast : float,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: ...
    def Degree(self) -> int: 
        """
        Returns the degree of the BSpline curve whose data is computed in this framework.
        """
    def IsPeriodic(self) -> bool: 
        """
        Returns true if the BSpline curve whose data is computed in this framework is periodic.
        """
    def Knot(self,Index : int) -> float: 
        """
        Returns the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def Multiplicity(self,Index : int) -> int: 
        """
        Returns the multiplicity of the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def NbKnots(self) -> int: 
        """
        Returns the number of knots of the BSpline curve whose data is computed in this framework.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles of the BSpline curve whose data is computed in this framework.
        """
    def Pole(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    def Weight(self,Index : int) -> float: 
        """
        Returns the weight of the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    pass
class Convert_CompBezierCurves2dToBSplineCurve2d():
    """
    Converts a list of connecting Bezier Curves 2d to a BSplineCurve 2d. if possible, the continuity of the BSpline will be increased to more than C0.
    """
    def AddCurve(self,Poles : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        Adds the Bezier curve defined by the table of poles Poles, to the sequence (still contained in this framework) of adjacent Bezier curves to be converted into a BSpline curve. Only polynomial (i.e. non-rational) Bezier curves are converted using this framework. If this is not the first call to the function (i.e. if this framework still contains data in its sequence of Bezier curves), the degree of continuity of the BSpline curve will be increased at the time of computation at the first point of the added Bezier curve (i.e. the first point of the Poles table). This will be the case if the tangent vector of the curve at this point is parallel to the tangent vector at the end point of the preceding Bezier curve in the sequence of Bezier curves still contained in this framework. An angular tolerance given at the time of construction of this framework, will be used to check the parallelism of the two tangent vectors. This checking procedure, and all the relative computations will be performed by the function Perform. When the sequence of adjacent Bezier curves is complete, use the following functions: - Perform to compute the data needed to build the BSpline curve, - and the available consultation functions to access the computed data. This data may be used to construct the BSpline curve. Warning The sequence of Bezier curves treated by this framework is automatically initialized with the first Bezier curve when the function is first called. During subsequent use of this function, ensure that the first point of the added Bezier curve (i.e. the first point of the Poles table) is coincident with the last point of the sequence (i.e. the last point of the preceding Bezier curve in the sequence) of Bezier curves still contained in this framework. An error may occur at the time of computation if this condition is not satisfied. Particular care must be taken with respect to the above, as this condition is not checked either when defining the sequence of Bezier curves or at the time of computation.
        """
    def Degree(self) -> int: 
        """
        Returns the degree of the BSpline curve whose data is computed in this framework. Warning Take particular care not to use this function before the computation is performed (Perform function), as this condition is not checked and an error may therefore occur.
        """
    def KnotsAndMults(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Loads the Knots table with the knots and the Mults table with the corresponding multiplicities of the BSpline curve whose data is computed in this framework. Warning - Do not use this function before the computation is performed (Perform function). - The length of the Knots and Mults arrays must be equal to the number of knots in the BSpline curve whose data is computed in this framework. Particular care must be taken with respect to the above as these conditions are not checked, and an error may occur.
        """
    def NbKnots(self) -> int: 
        """
        Returns the number of knots of the BSpline curve whose data is computed in this framework. Warning Take particular care not to use this function before the computation is performed (Perform function), as this condition is not checked and an error may therefore occur.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles of the BSpline curve whose data is computed in this framework. Warning Take particular care not to use this function before the computation is performed (Perform function), as this condition is not checked and an error may therefore occur.
        """
    def Perform(self) -> None: 
        """
        Computes all the data needed to build a BSpline curve equivalent to the sequence of adjacent Bezier curves still contained in this framework. A knot is inserted on the computed BSpline curve at the junction point of two consecutive Bezier curves. The degree of continuity of the BSpline curve will be increased at the junction point of two consecutive Bezier curves if their tangent vectors at this point are parallel. An angular tolerance given at the time of construction of this framework is used to check the parallelism of the two tangent vectors. Use the available consultation functions to access the computed data. This data may then be used to construct the BSpline curve. Warning Ensure that the curves in the sequence of Bezier curves contained in this framework are adjacent. An error may occur at the time of computation if this condition is not satisfied. Particular care must be taken with respect to the above as this condition is not checked, either when defining the Bezier curve sequence or at the time of computation.
        """
    def Poles(self,Poles : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        Loads the Poles table with the poles of the BSpline curve whose data is computed in this framework. Warning - Do not use this function before the computation is performed (Perform function). - The length of the Poles array must be equal to the number of poles of the BSpline curve whose data is computed in this framework. Particular care must be taken with respect to the above, as these conditions are not checked, and an error may occur.
        """
    def __init__(self,AngularTolerance : float=0.0001) -> None: ...
    pass
class Convert_CompBezierCurvesToBSplineCurve():
    """
    An algorithm to convert a sequence of adjacent non-rational Bezier curves into a BSpline curve. A CompBezierCurvesToBSplineCurve object provides a framework for: - defining the sequence of adjacent non-rational Bezier curves to be converted into a BSpline curve, - implementing the computation algorithm, and - consulting the results. Warning Do not attempt to convert rational Bezier curves using this type of algorithm.
    """
    def AddCurve(self,Poles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        Adds the Bezier curve defined by the table of poles Poles, to the sequence (still contained in this framework) of adjacent Bezier curves to be converted into a BSpline curve. Only polynomial (i.e. non-rational) Bezier curves are converted using this framework. If this is not the first call to the function (i.e. if this framework still contains data in its Bezier curve sequence), the degree of continuity of the BSpline curve will be increased at the time of computation at the first point of the added Bezier curve (i.e. the first point of the Poles table). This will be the case if the tangent vector of the curve at this point is parallel to the tangent vector at the end point of the preceding Bezier curve in the Bezier curve sequence still contained in this framework. An angular tolerance given at the time of construction of this framework will be used to check the parallelism of the two tangent vectors. This checking procedure and all related computations will be performed by the Perform function. When the adjacent Bezier curve sequence is complete, use the following functions: - Perform to compute the data needed to build the BSpline curve, - and the available consultation functions to access the computed data. This data may be used to construct the BSpline curve. Warning The Bezier curve sequence treated by this framework is automatically initialized with the first Bezier curve when the function is first called. During subsequent use of this function, ensure that the first point of the added Bezier curve (i.e. the first point of the Poles table) is coincident with the last point of the Bezier curve sequence (i.e. the last point of the preceding Bezier curve in the sequence) still contained in this framework. An error may occur at the time of computation if this condition is not satisfied. Particular care must be taken with respect to the above, as this condition is not checked either when defining the Bezier curve sequence or at the time of computation.
        """
    def Degree(self) -> int: 
        """
        Returns the degree of the BSpline curve whose data is computed in this framework. Warning Take particular care not to use this function before the computation is performed (Perform function), as this condition is not checked and an error may therefore occur.
        """
    def KnotsAndMults(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        - loads the Knots table with the knots, - and loads the Mults table with the corresponding multiplicities of the BSpline curve whose data is computed in this framework. Warning - Do not use this function before the computation is performed (Perform function). - The length of the Knots and Mults arrays must be equal to the number of knots in the BSpline curve whose data is computed in this framework. Particular care must be taken with respect to the above as these conditions are not checked, and an error may occur.
        """
    def NbKnots(self) -> int: 
        """
        Returns the number of knots of the BSpline curve whose data is computed in this framework. Warning Take particular care not to use this function before the computation is performed (Perform function), as this condition is not checked and an error may therefore occur.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles of the BSpline curve whose data is computed in this framework. Warning Take particular care not to use this function before the computation is performed (Perform function), as this condition is not checked and an error may therefore occur.
        """
    def Perform(self) -> None: 
        """
        Computes all the data needed to build a BSpline curve equivalent to the adjacent Bezier curve sequence still contained in this framework. A knot is inserted on the computed BSpline curve at the junction point of two consecutive Bezier curves. The degree of continuity of the BSpline curve will be increased at the junction point of two consecutive Bezier curves if their tangent vectors at this point are parallel. An angular tolerance given at the time of construction of this framework is used to check the parallelism of the two tangent vectors. Use the available consultation functions to access the computed data. This data may then be used to construct the BSpline curve. Warning Make sure that the curves in the Bezier curve sequence contained in this framework are adjacent. An error may occur at the time of computation if this condition is not satisfied. Particular care must be taken with respect to the above as this condition is not checked, either when defining the Bezier curve sequence or at the time of computation.
        """
    def Poles(self,Poles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        Loads the Poles table with the poles of the BSpline curve whose data is computed in this framework. Warning - Do not use this function before the computation is performed (Perform function). - The length of the Poles array must be equal to the number of poles of the BSpline curve whose data is computed in this framework. Particular care must be taken with respect to the above, as these conditions are not checked, and an error may occur.
        """
    def __init__(self,AngularTolerance : float=0.0001) -> None: ...
    pass
class Convert_CompPolynomialToPoles():
    """
    Convert a serie of Polynomial N-Dimensional Curves that are have continuity CM to an N-Dimensional Bspline Curve that has continuity CM. (to convert an function (curve) polynomial by span in a BSpline) This class uses the following arguments : NumCurves : the number of Polynomial Curves Continuity: the requested continuity for the n-dimensional Spline Dimension : the dimension of the Spline MaxDegree : maximum allowed degree for each composite polynomial segment. NumCoeffPerCurve : the number of coefficient per segments = degree - 1 Coefficients : the coefficients organized in the following way [1..<myNumPolynomials>][1..myMaxDegree +1][1..myDimension] that is : index [n,d,i] is at slot (n-1) * (myMaxDegree + 1) * myDimension + (d-1) * myDimension + i PolynomialIntervals : nth polynomial represents a polynomial between myPolynomialIntervals->Value(n,0) and myPolynomialIntervals->Value(n,1) TrueIntervals : the nth polynomial has to be mapped linearly to be defined on the following interval : myTrueIntervals->Value(n) and myTrueIntervals->Value(n+1) so that it represent adequatly the function with the required continuity
    """
    def Degree(self) -> int: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Knots(self,K : OCP.TColStd.TColStd_HArray1OfReal) -> Any: 
        """
        Knots of the n-dimensional Bspline
        """
    def Multiplicities(self,M : OCP.TColStd.TColStd_HArray1OfInteger) -> Any: 
        """
        Multiplicities of the knots in the BSpline
        """
    def NbKnots(self) -> int: 
        """
        Degree of the n-dimensional Bspline
        """
    def NbPoles(self) -> int: 
        """
        number of poles of the n-dimensional BSpline
        """
    def Poles(self,Poles : OCP.TColStd.TColStd_HArray2OfReal) -> Any: 
        """
        returns the poles of the n-dimensional BSpline in the following format : [1..NumPoles][1..Dimension]
        """
    @overload
    def __init__(self,Dimension : int,MaxDegree : int,Degree : int,Coefficients : OCP.TColStd.TColStd_Array1OfReal,PolynomialIntervals : OCP.TColStd.TColStd_Array1OfReal,TrueIntervals : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,NumCurves : int,Continuity : int,Dimension : int,MaxDegree : int,NumCoeffPerCurve : OCP.TColStd.TColStd_HArray1OfInteger,Coefficients : OCP.TColStd.TColStd_HArray1OfReal,PolynomialIntervals : OCP.TColStd.TColStd_HArray2OfReal,TrueIntervals : OCP.TColStd.TColStd_HArray1OfReal) -> None: ...
    @overload
    def __init__(self,NumCurves : int,Dimension : int,MaxDegree : int,Continuity : OCP.TColStd.TColStd_Array1OfInteger,NumCoeffPerCurve : OCP.TColStd.TColStd_Array1OfInteger,Coefficients : OCP.TColStd.TColStd_Array1OfReal,PolynomialIntervals : OCP.TColStd.TColStd_Array2OfReal,TrueIntervals : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    pass
class Convert_ElementarySurfaceToBSplineSurface():
    """
    Root class for algorithms which convert an elementary surface (cylinder, cone, sphere or torus) into a BSpline surface (CylinderToBSplineSurface, ConeToBSplineSurface, SphereToBSplineSurface, TorusToBSplineSurface). These algorithms all work on elementary surfaces from the gp package and compute all the data needed to construct a BSpline surface equivalent to the cylinder, cone, sphere or torus. This data consists of the following: - degrees in the u and v parametric directions, - periodic characteristics in the u and v parametric directions, - a poles table with associated weights, - a knots table (for the u and v parametric directions) with associated multiplicities. The abstract class ElementarySurfaceToBSplineSurface provides a framework for storing and consulting this computed data. This data may then be used to construct a Geom_BSplineSurface surface, for example. All those classes define algorithmes to convert an ElementarySurface into a B-spline surface. This abstract class implements the methods to get the geometric representation of the B-spline surface. The B-spline representation is computed at the creation time in the sub classes. The B-spline surface is defined with its degree in the parametric U and V directions, its control points (Poles), its weights, its knots and their multiplicity. KeyWords : Convert, ElementarySurface, BSplineSurface.
    """
    def IsUPeriodic(self) -> bool: 
        """
        None
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns true if the BSpline surface whose data is computed in this framework is periodic in the u or v parametric direction.
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVKnots(self) -> int: 
        """
        Returns the number of knots for the u or v parametric direction of the BSpline surface whose data is computed in this framework .
        """
    def NbVPoles(self) -> int: 
        """
        Returns the number of poles for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def Pole(self,UIndex : int,VIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UKnot(self,UIndex : int) -> float: 
        """
        Returns the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def UMultiplicity(self,UIndex : int) -> int: 
        """
        Returns the multiplicity of the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def VDegree(self) -> int: 
        """
        Returns the degree for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def VKnot(self,UIndex : int) -> float: 
        """
        Returns the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def VMultiplicity(self,VIndex : int) -> int: 
        """
        Returns the multiplicity of the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def Weight(self,UIndex : int,VIndex : int) -> float: 
        """
        Returns the weight of the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    pass
class Convert_CircleToBSplineCurve(Convert_ConicToBSplineCurve):
    """
    This algorithm converts a circle into a rational B-spline curve. The circle is a Circ2d from package gp and its parametrization is : P (U) = Loc + R * (Cos(U) * Xdir + Sin(U) * YDir) where Loc is the center of the circle Xdir and Ydir are the normalized directions of the local cartesian coordinate system of the circle. The parametrization range for the circle is U [0, 2Pi].
    """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: 
        """
        None

        None
        """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,UFirst : float,ULast : float,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: ...
    def Degree(self) -> int: 
        """
        Returns the degree of the BSpline curve whose data is computed in this framework.
        """
    def IsPeriodic(self) -> bool: 
        """
        Returns true if the BSpline curve whose data is computed in this framework is periodic.
        """
    def Knot(self,Index : int) -> float: 
        """
        Returns the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def Multiplicity(self,Index : int) -> int: 
        """
        Returns the multiplicity of the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def NbKnots(self) -> int: 
        """
        Returns the number of knots of the BSpline curve whose data is computed in this framework.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles of the BSpline curve whose data is computed in this framework.
        """
    def Pole(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    def Weight(self,Index : int) -> float: 
        """
        Returns the weight of the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d,U1 : float,U2 : float,Parameterisation : Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d,Parameterisation : Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> None: ...
    pass
class Convert_CylinderToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    """
    This algorithm converts a bounded cylinder into a rational B-spline surface. The cylinder is a Cylinder from package gp. The parametrization of the cylinder is : P (U, V) = Loc + V * Zdir + Radius * (Xdir*Cos(U) + Ydir*Sin(U)) where Loc is the location point of the cylinder, Xdir, Ydir and Zdir are the normalized directions of the local cartesian coordinate system of the cylinder (Zdir is the direction of the cylinder's axis). The U parametrization range is U [0, 2PI]. KeyWords : Convert, Cylinder, BSplineSurface.
    """
    def IsUPeriodic(self) -> bool: 
        """
        None
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns true if the BSpline surface whose data is computed in this framework is periodic in the u or v parametric direction.
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVKnots(self) -> int: 
        """
        Returns the number of knots for the u or v parametric direction of the BSpline surface whose data is computed in this framework .
        """
    def NbVPoles(self) -> int: 
        """
        Returns the number of poles for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def Pole(self,UIndex : int,VIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UKnot(self,UIndex : int) -> float: 
        """
        Returns the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def UMultiplicity(self,UIndex : int) -> int: 
        """
        Returns the multiplicity of the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def VDegree(self) -> int: 
        """
        Returns the degree for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def VKnot(self,UIndex : int) -> float: 
        """
        Returns the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def VMultiplicity(self,VIndex : int) -> int: 
        """
        Returns the multiplicity of the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def Weight(self,UIndex : int,VIndex : int) -> float: 
        """
        Returns the weight of the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,U1 : float,U2 : float,V1 : float,V2 : float) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,V1 : float,V2 : float) -> None: ...
    pass
class Convert_ConeToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    """
    This algorithm converts a bounded Cone into a rational B-spline surface. The cone a Cone from package gp. Its parametrization is : P (U, V) = Loc + V * Zdir + (R + V*Tan(Ang)) * (Cos(U)*Xdir + Sin(U)*Ydir) where Loc is the location point of the cone, Xdir, Ydir and Zdir are the normalized directions of the local cartesian coordinate system of the cone (Zdir is the direction of the Cone's axis) , Ang is the cone semi-angle. The U parametrization range is [0, 2PI]. KeyWords : Convert, Cone, BSplineSurface.
    """
    def IsUPeriodic(self) -> bool: 
        """
        None
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns true if the BSpline surface whose data is computed in this framework is periodic in the u or v parametric direction.
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVKnots(self) -> int: 
        """
        Returns the number of knots for the u or v parametric direction of the BSpline surface whose data is computed in this framework .
        """
    def NbVPoles(self) -> int: 
        """
        Returns the number of poles for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def Pole(self,UIndex : int,VIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UKnot(self,UIndex : int) -> float: 
        """
        Returns the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def UMultiplicity(self,UIndex : int) -> int: 
        """
        Returns the multiplicity of the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def VDegree(self) -> int: 
        """
        Returns the degree for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def VKnot(self,UIndex : int) -> float: 
        """
        Returns the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def VMultiplicity(self,VIndex : int) -> int: 
        """
        Returns the multiplicity of the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def Weight(self,UIndex : int,VIndex : int) -> float: 
        """
        Returns the weight of the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    @overload
    def __init__(self,C : OCP.gp.gp_Cone,V1 : float,V2 : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cone,U1 : float,U2 : float,V1 : float,V2 : float) -> None: ...
    pass
class Convert_EllipseToBSplineCurve(Convert_ConicToBSplineCurve):
    """
    This algorithm converts a ellipse into a rational B-spline curve. The ellipse is represented an Elips2d from package gp with the parametrization : P (U) = Loc + (MajorRadius * Cos(U) * Xdir + MinorRadius * Sin(U) * Ydir) where Loc is the center of the ellipse, Xdir and Ydir are the normalized directions of the local cartesian coordinate system of the ellipse. The parametrization range is U [0, 2PI]. KeyWords : Convert, Ellipse, BSplineCurve, 2D .
    """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: 
        """
        None

        None
        """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,UFirst : float,ULast : float,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: ...
    def Degree(self) -> int: 
        """
        Returns the degree of the BSpline curve whose data is computed in this framework.
        """
    def IsPeriodic(self) -> bool: 
        """
        Returns true if the BSpline curve whose data is computed in this framework is periodic.
        """
    def Knot(self,Index : int) -> float: 
        """
        Returns the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def Multiplicity(self,Index : int) -> int: 
        """
        Returns the multiplicity of the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def NbKnots(self) -> int: 
        """
        Returns the number of knots of the BSpline curve whose data is computed in this framework.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles of the BSpline curve whose data is computed in this framework.
        """
    def Pole(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    def Weight(self,Index : int) -> float: 
        """
        Returns the weight of the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d,Parameterisation : Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d,U1 : float,U2 : float,Parameterisation : Convert_ParameterisationType=Convert_ParameterisationType.Convert_TgtThetaOver2) -> None: ...
    pass
class Convert_GridPolynomialToPoles():
    """
    Convert a grid of Polynomial Surfaces that are have continuity CM to an Bspline Surface that has continuity CM
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVKnots(self) -> int: 
        """
        None
        """
    def NbVPoles(self) -> int: 
        """
        None
        """
    def Perform(self,UContinuity : int,VContinuity : int,MaxUDegree : int,MaxVDegree : int,NumCoeffPerSurface : OCP.TColStd.TColStd_HArray2OfInteger,Coefficients : OCP.TColStd.TColStd_HArray1OfReal,PolynomialUIntervals : OCP.TColStd.TColStd_HArray1OfReal,PolynomialVIntervals : OCP.TColStd.TColStd_HArray1OfReal,TrueUIntervals : OCP.TColStd.TColStd_HArray1OfReal,TrueVIntervals : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def Poles(self) -> OCP.TColgp.TColgp_HArray2OfPnt: 
        """
        returns the poles of the BSpline Surface
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UKnots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Knots in the U direction
        """
    def UMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Multiplicities of the knots in the U direction
        """
    def VDegree(self) -> int: 
        """
        None
        """
    def VKnots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Knots in the V direction
        """
    def VMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Multiplicities of the knots in the V direction
        """
    @overload
    def __init__(self,NbUSurfaces : int,NBVSurfaces : int,UContinuity : int,VContinuity : int,MaxUDegree : int,MaxVDegree : int,NumCoeffPerSurface : OCP.TColStd.TColStd_HArray2OfInteger,Coefficients : OCP.TColStd.TColStd_HArray1OfReal,PolynomialUIntervals : OCP.TColStd.TColStd_HArray1OfReal,PolynomialVIntervals : OCP.TColStd.TColStd_HArray1OfReal,TrueUIntervals : OCP.TColStd.TColStd_HArray1OfReal,TrueVIntervals : OCP.TColStd.TColStd_HArray1OfReal) -> None: ...
    @overload
    def __init__(self,MaxUDegree : int,MaxVDegree : int,NumCoeff : OCP.TColStd.TColStd_HArray1OfInteger,Coefficients : OCP.TColStd.TColStd_HArray1OfReal,PolynomialUIntervals : OCP.TColStd.TColStd_HArray1OfReal,PolynomialVIntervals : OCP.TColStd.TColStd_HArray1OfReal) -> None: ...
    pass
class Convert_HyperbolaToBSplineCurve(Convert_ConicToBSplineCurve):
    """
    This algorithm converts a hyperbola into a rational B-spline curve. The hyperbola is an Hypr2d from package gp with the parametrization : P (U) = Loc + (MajorRadius * Cosh(U) * Xdir + MinorRadius * Sinh(U) * Ydir) where Loc is the location point of the hyperbola, Xdir and Ydir are the normalized directions of the local cartesian coordinate system of the hyperbola. KeyWords : Convert, Hyperbola, BSplineCurve, 2D .
    """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: 
        """
        None

        None
        """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,UFirst : float,ULast : float,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: ...
    def Degree(self) -> int: 
        """
        Returns the degree of the BSpline curve whose data is computed in this framework.
        """
    def IsPeriodic(self) -> bool: 
        """
        Returns true if the BSpline curve whose data is computed in this framework is periodic.
        """
    def Knot(self,Index : int) -> float: 
        """
        Returns the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def Multiplicity(self,Index : int) -> int: 
        """
        Returns the multiplicity of the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def NbKnots(self) -> int: 
        """
        Returns the number of knots of the BSpline curve whose data is computed in this framework.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles of the BSpline curve whose data is computed in this framework.
        """
    def Pole(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    def Weight(self,Index : int) -> float: 
        """
        Returns the weight of the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    def __init__(self,H : OCP.gp.gp_Hypr2d,U1 : float,U2 : float) -> None: ...
    pass
class Convert_ParabolaToBSplineCurve(Convert_ConicToBSplineCurve):
    """
    This algorithm converts a parabola into a non rational B-spline curve. The parabola is a Parab2d from package gp with the parametrization P (U) = Loc + F * (U*U * Xdir + 2 * U * Ydir) where Loc is the apex of the parabola, Xdir is the normalized direction of the symmetry axis of the parabola, Ydir is the normalized direction of the directrix and F is the focal length. KeyWords : Convert, Parabola, BSplineCurve, 2D .
    """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: 
        """
        None

        None
        """
    @overload
    def BuildCosAndSin(self,Parametrisation : Convert_ParameterisationType,UFirst : float,ULast : float,CosNumerator : OCP.TColStd.TColStd_HArray1OfReal,SinNumerator : OCP.TColStd.TColStd_HArray1OfReal,Denominator : OCP.TColStd.TColStd_HArray1OfReal,Knots : OCP.TColStd.TColStd_HArray1OfReal,Mults : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: ...
    def Degree(self) -> int: 
        """
        Returns the degree of the BSpline curve whose data is computed in this framework.
        """
    def IsPeriodic(self) -> bool: 
        """
        Returns true if the BSpline curve whose data is computed in this framework is periodic.
        """
    def Knot(self,Index : int) -> float: 
        """
        Returns the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def Multiplicity(self,Index : int) -> int: 
        """
        Returns the multiplicity of the knot of index Index to the knots table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of the BSpline curve whose data is computed in this framework.
        """
    def NbKnots(self) -> int: 
        """
        Returns the number of knots of the BSpline curve whose data is computed in this framework.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles of the BSpline curve whose data is computed in this framework.
        """
    def Pole(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    def Weight(self,Index : int) -> float: 
        """
        Returns the weight of the pole of index Index to the poles table of the BSpline curve whose data is computed in this framework. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table of the BSpline curve whose data is computed in this framework.
        """
    def __init__(self,Prb : OCP.gp.gp_Parab2d,U1 : float,U2 : float) -> None: ...
    pass
class Convert_ParameterisationType():
    """
    Identifies a type of parameterization of a circle or ellipse represented as a BSpline curve. For a circle with a center C and a radius R (for example a Geom2d_Circle or a Geom_Circle), the natural parameterization is angular. It uses the angle Theta made by the vector CM with the 'X Axis' of the circle's local coordinate system as parameter for the current point M. The coordinates of the point M are as follows: X = R *cos ( Theta ) y = R * sin ( Theta ) Similarly, for an ellipse with a center C, a major radius R and a minor radius r, the circle Circ with center C and radius R (and located in the same plane as the ellipse) lends its natural angular parameterization to the ellipse. This is achieved by an affine transformation in the plane of the ellipse, in the ratio r / R, about the 'X Axis' of its local coordinate system. The coordinates of the current point M are as follows: X = R * cos ( Theta ) y = r * sin ( Theta ) The process of converting a circle or an ellipse into a rational or non-rational BSpline curve transforms the Theta angular parameter into a parameter t. This ensures the rational or polynomial parameterization of the resulting BSpline curve. Several types of parametric transformations are available. TgtThetaOver2 The most usual method is Convert_TgtThetaOver2 where the parameter t on the BSpline curve is obtained by means of transformation of the following type: t = tan ( Theta / 2 ) The result of this definition is: cos ( Theta ) = ( 1. - t**2 ) / ( 1. + t**2 ) sin ( Theta ) = 2. * t / ( 1. + t**2 ) which ensures the rational parameterization of the circle or the ellipse. However, this is not the most suitable parameterization method where the arc of the circle or ellipse has a large opening angle. In such cases, the curve will be represented by a BSpline with intermediate knots. Each span, i.e. each portion of curve between two different knot values, will use parameterization of this type. The number of spans is calculated using the following rule: ( 1.2 * Delta / Pi ) + 1 where Delta is equal to the opening angle (in radians) of the arc of the circle (Delta is equal to 2.* Pi in the case of a complete circle). The resulting BSpline curve is "exact", i.e. computing any point of parameter t on the BSpline curve gives an exact point on the circle or the ellipse. TgtThetaOver2_N Where N is equal to 1, 2, 3 or 4, this ensures the same type of parameterization as Convert_TgtThetaOver2 but sets the number of spans in the resulting BSpline curve to N rather than allowing the algorithm to make this calculation. However, the opening angle Delta (parametric angle, given in radians) of the arc of the circle (or of the ellipse) must comply with the following: - Delta <= 0.9999 * Pi for the Convert_TgtThetaOver2_1 method, or - Delta <= 1.9999 * Pi for the Convert_TgtThetaOver2_2 method. QuasiAngular The Convert_QuasiAngular method of parameterization uses a different type of rational parameterization. This method ensures that the parameter t along the resulting BSpline curve is very close to the natural parameterization angle Theta of the circle or ellipse (i.e. which uses the functions sin ( Theta ) and cos ( Theta ). The resulting BSpline curve is "exact", i.e. computing any point of parameter t on the BSpline curve gives an exact point on the circle or the ellipse. RationalC1 The Convert_RationalC1 method of parameterization uses a further type of rational parameterization. This method ensures that the equation relating to the resulting BSpline curve has a "C1" continuous denominator, which is not the case with the above methods. RationalC1 enhances the degree of continuity at the junction point of the different spans of the curve. The resulting BSpline curve is "exact", i.e. computing any point of parameter t on the BSpline curve gives an exact point on the circle or the ellipse. Polynomial The Convert_Polynomial method is used to produce polynomial (i.e. non-rational) parameterization of the resulting BSpline curve with 8 poles (i.e. a polynomial degree equal to 7). However, the result is an approximation of the circle or ellipse (i.e. computing the point of parameter t on the BSpline curve does not give an exact point on the circle or the ellipse).

    Members:

      Convert_TgtThetaOver2

      Convert_TgtThetaOver2_1

      Convert_TgtThetaOver2_2

      Convert_TgtThetaOver2_3

      Convert_TgtThetaOver2_4

      Convert_QuasiAngular

      Convert_RationalC1

      Convert_Polynomial
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Convert_Polynomial: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_Polynomial
    Convert_QuasiAngular: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_QuasiAngular
    Convert_RationalC1: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_RationalC1
    Convert_TgtThetaOver2: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2
    Convert_TgtThetaOver2_1: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2_1
    Convert_TgtThetaOver2_2: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2_2
    Convert_TgtThetaOver2_3: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2_3
    Convert_TgtThetaOver2_4: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2_4
    __entries: dict # value = {'Convert_TgtThetaOver2': (Convert_ParameterisationType.Convert_TgtThetaOver2, None), 'Convert_TgtThetaOver2_1': (Convert_ParameterisationType.Convert_TgtThetaOver2_1, None), 'Convert_TgtThetaOver2_2': (Convert_ParameterisationType.Convert_TgtThetaOver2_2, None), 'Convert_TgtThetaOver2_3': (Convert_ParameterisationType.Convert_TgtThetaOver2_3, None), 'Convert_TgtThetaOver2_4': (Convert_ParameterisationType.Convert_TgtThetaOver2_4, None), 'Convert_QuasiAngular': (Convert_ParameterisationType.Convert_QuasiAngular, None), 'Convert_RationalC1': (Convert_ParameterisationType.Convert_RationalC1, None), 'Convert_Polynomial': (Convert_ParameterisationType.Convert_Polynomial, None)}
    __members__: dict # value = {'Convert_TgtThetaOver2': Convert_ParameterisationType.Convert_TgtThetaOver2, 'Convert_TgtThetaOver2_1': Convert_ParameterisationType.Convert_TgtThetaOver2_1, 'Convert_TgtThetaOver2_2': Convert_ParameterisationType.Convert_TgtThetaOver2_2, 'Convert_TgtThetaOver2_3': Convert_ParameterisationType.Convert_TgtThetaOver2_3, 'Convert_TgtThetaOver2_4': Convert_ParameterisationType.Convert_TgtThetaOver2_4, 'Convert_QuasiAngular': Convert_ParameterisationType.Convert_QuasiAngular, 'Convert_RationalC1': Convert_ParameterisationType.Convert_RationalC1, 'Convert_Polynomial': Convert_ParameterisationType.Convert_Polynomial}
    pass
class Convert_SequenceOfArray1OfPoles(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Convert_SequenceOfArray1OfPoles) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OCP.TColgp.TColgp_HArray1OfPnt) -> None: ...
    def Assign(self,theOther : Convert_SequenceOfArray1OfPoles) -> Convert_SequenceOfArray1OfPoles: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TColgp.TColgp_HArray1OfPnt: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TColgp.TColgp_HArray1OfPnt: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColgp.TColgp_HArray1OfPnt: 
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
    def First(self) -> OCP.TColgp.TColgp_HArray1OfPnt: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TColgp.TColgp_HArray1OfPnt) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Convert_SequenceOfArray1OfPoles) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TColgp.TColgp_HArray1OfPnt) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Convert_SequenceOfArray1OfPoles) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TColgp.TColgp_HArray1OfPnt: 
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
    def Prepend(self,theSeq : Convert_SequenceOfArray1OfPoles) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.TColgp.TColgp_HArray1OfPnt) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : OCP.TColgp.TColgp_HArray1OfPnt) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Convert_SequenceOfArray1OfPoles) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TColgp.TColgp_HArray1OfPnt: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Convert_SequenceOfArray1OfPoles) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Convert_SphereToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    """
    This algorithm converts a bounded Sphere into a rational B-spline surface. The sphere is a Sphere from package gp. The parametrization of the sphere is P (U, V) = Loc + Radius * Sin(V) * Zdir + Radius * Cos(V) * (Cos(U)*Xdir + Sin(U)*Ydir) where Loc is the center of the sphere Xdir, Ydir and Zdir are the normalized directions of the local cartesian coordinate system of the sphere. The parametrization range is U [0, 2PI] and V [-PI/2, PI/2]. KeyWords : Convert, Sphere, BSplineSurface.
    """
    def IsUPeriodic(self) -> bool: 
        """
        None
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns true if the BSpline surface whose data is computed in this framework is periodic in the u or v parametric direction.
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVKnots(self) -> int: 
        """
        Returns the number of knots for the u or v parametric direction of the BSpline surface whose data is computed in this framework .
        """
    def NbVPoles(self) -> int: 
        """
        Returns the number of poles for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def Pole(self,UIndex : int,VIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UKnot(self,UIndex : int) -> float: 
        """
        Returns the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def UMultiplicity(self,UIndex : int) -> int: 
        """
        Returns the multiplicity of the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def VDegree(self) -> int: 
        """
        Returns the degree for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def VKnot(self,UIndex : int) -> float: 
        """
        Returns the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def VMultiplicity(self,VIndex : int) -> int: 
        """
        Returns the multiplicity of the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def Weight(self,UIndex : int,VIndex : int) -> float: 
        """
        Returns the weight of the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    @overload
    def __init__(self,Sph : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def __init__(self,Sph : OCP.gp.gp_Sphere,Param1 : float,Param2 : float,UTrim : bool=True) -> None: ...
    @overload
    def __init__(self,Sph : OCP.gp.gp_Sphere,U1 : float,U2 : float,V1 : float,V2 : float) -> None: ...
    pass
class Convert_TorusToBSplineSurface(Convert_ElementarySurfaceToBSplineSurface):
    """
    This algorithm converts a bounded Torus into a rational B-spline surface. The torus is a Torus from package gp. The parametrization of the torus is : P (U, V) = Loc + MinorRadius * Sin(V) * Zdir + (MajorRadius+MinorRadius*Cos(V)) * (Cos(U)*Xdir + Sin(U)*Ydir) where Loc is the center of the torus, Xdir, Ydir and Zdir are the normalized directions of the local cartesian coordinate system of the Torus. The parametrization range is U [0, 2PI], V [0, 2PI]. KeyWords : Convert, Torus, BSplineSurface.
    """
    def IsUPeriodic(self) -> bool: 
        """
        None
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns true if the BSpline surface whose data is computed in this framework is periodic in the u or v parametric direction.
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVKnots(self) -> int: 
        """
        Returns the number of knots for the u or v parametric direction of the BSpline surface whose data is computed in this framework .
        """
    def NbVPoles(self) -> int: 
        """
        Returns the number of poles for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def Pole(self,UIndex : int,VIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UKnot(self,UIndex : int) -> float: 
        """
        Returns the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def UMultiplicity(self,UIndex : int) -> int: 
        """
        Returns the multiplicity of the U-knot of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def VDegree(self) -> int: 
        """
        Returns the degree for the u or v parametric direction of the BSpline surface whose data is computed in this framework.
        """
    def VKnot(self,UIndex : int) -> float: 
        """
        Returns the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def VMultiplicity(self,VIndex : int) -> int: 
        """
        Returns the multiplicity of the V-knot of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots.
        """
    def Weight(self,UIndex : int,VIndex : int) -> float: 
        """
        Returns the weight of the pole of index (UIndex,VIndex) to the poles table of the BSpline surface whose data is computed in this framework. Exceptions Standard_OutOfRange if, for the BSpline surface whose data is computed in this framework: - UIndex is outside the bounds of the poles table in the u parametric direction, or - VIndex is outside the bounds of the poles table in the v parametric direction.
        """
    @overload
    def __init__(self,T : OCP.gp.gp_Torus) -> None: ...
    @overload
    def __init__(self,T : OCP.gp.gp_Torus,U1 : float,U2 : float,V1 : float,V2 : float) -> None: ...
    @overload
    def __init__(self,T : OCP.gp.gp_Torus,Param1 : float,Param2 : float,UTrim : bool=True) -> None: ...
    pass
def BuildPolynomialCosAndSin(arg0 : float,arg1 : float,arg2 : int,arg3 : OCP.TColStd.TColStd_HArray1OfReal,arg4 : OCP.TColStd.TColStd_HArray1OfReal,arg5 : OCP.TColStd.TColStd_HArray1OfReal) -> None:
    """
    None
    """
Convert_Polynomial: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_Polynomial
Convert_QuasiAngular: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_QuasiAngular
Convert_RationalC1: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_RationalC1
Convert_TgtThetaOver2: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2
Convert_TgtThetaOver2_1: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2_1
Convert_TgtThetaOver2_2: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2_2
Convert_TgtThetaOver2_3: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2_3
Convert_TgtThetaOver2_4: OCP.Convert.Convert_ParameterisationType # value = Convert_ParameterisationType.Convert_TgtThetaOver2_4
