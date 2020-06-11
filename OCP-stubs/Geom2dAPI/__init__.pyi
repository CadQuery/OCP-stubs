import OCP.Geom2dAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom2dInt
import OCP.Geom2d
import OCP.Approx
import OCP.gp
import OCP.TColgp
import OCP.Extrema
import OCP.TColStd
__all__  = [
"Geom2dAPI_ExtremaCurveCurve",
"Geom2dAPI_InterCurveCurve",
"Geom2dAPI_Interpolate",
"Geom2dAPI_PointsToBSpline",
"Geom2dAPI_ProjectPointOnCurve"
]
class Geom2dAPI_ExtremaCurveCurve():
    """
    Describes functions for computing all the extrema between two 2D curves. An ExtremaCurveCurve algorithm minimizes or maximizes the distance between a point on the first curve and a point on the second curve. Thus, it computes the start point and end point of perpendiculars common to the two curves (an intersection point is not an extremum except where the two curves are tangential at this point). Solutions consist of pairs of points, and an extremum is considered to be a segment joining the two points of a solution. An ExtremaCurveCurve object provides a framework for: - defining the construction of the extrema, - implementing the construction algorithm, and - consulting the results. Warning In some cases, the nearest points between two curves do not correspond to one of the computed extrema. Instead, they may be given by: - a limit point of one curve and one of the following: - its orthogonal projection on the other curve, - a limit point of the other curve; or - an intersection point between the two curves.
    """
    def Distance(self,Index : int) -> float: 
        """
        Computes the distance between the end points of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def Extrema(self) -> OCP.Extrema.Extrema_ExtCC2d: 
        """
        None

        None
        """
    def LowerDistance(self) -> float: 
        """
        Computes the distance between the end points of the shortest extremum computed by this algorithm. Exceptions - StdFail_NotDone if this algorithm fails.
        """
    def LowerDistanceParameters(self) -> Tuple[float, float]: 
        """
        Returns the parameters U1 of the point on the first curve and U2 of the point on the second curve, which are the ends of the shortest extremum computed by this algorithm. Exceptions StdFail_NotDone if this algorithm fails.
        """
    def NbExtrema(self) -> int: 
        """
        Returns the number of extrema computed by this algorithm. Note: if this algorithm fails, NbExtrema returns 0.
        """
    def NearestPoints(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns the points P1 on the first curve and P2 on the second curve, which are the ends of the shortest extremum computed by this algorithm. Exceptions StdFail_NotDone if this algorithm fails.
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        Returns the parameters U1 of the point on the first curve and U2 of the point on the second curve, which are the ends of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def Points(self,Index : int,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns the points P1 on the first curve and P2 on the second curve, which are the ends of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def __init__(self,C1 : OCP.Geom2d.Geom2d_Curve,C2 : OCP.Geom2d.Geom2d_Curve,U1min : float,U1max : float,U2min : float,U2max : float) -> None: ...
    pass
class Geom2dAPI_InterCurveCurve():
    """
    This class implements methods for computing - the intersections between two 2D curves, - the self-intersections of a 2D curve. Using the InterCurveCurve algorithm allows to get the following results: - intersection points in the case of cross intersections, - intersection segments in the case of tangential intersections, - nothing in the case of no intersections.
    """
    @overload
    def Init(self,C1 : OCP.Geom2d.Geom2d_Curve,Tol : float=1e-06) -> None: 
        """
        Initializes an algorithm with the given arguments and computes the intersections between the curves C1. and C2.

        Initializes an algorithm with the given arguments and computes the self-intersections of the curve C1. Tolerance value Tol, defaulted to 1.0e-6, defines the precision of computing the intersection points. In case of a tangential intersection, Tol also defines the size of intersection segments (limited portions of the curves) where the distance between all points from two curves (or a curve in case of self-intersection) is less than Tol. Warning Use functions NbPoints and NbSegments to obtain the number of solutions. If the algorithm finds no intersections NbPoints and NbSegments return 0.
        """
    @overload
    def Init(self,C1 : OCP.Geom2d.Geom2d_Curve,C2 : OCP.Geom2d.Geom2d_Curve,Tol : float=1e-06) -> None: ...
    def Intersector(self) -> OCP.Geom2dInt.Geom2dInt_GInter: 
        """
        return the algorithmic object from Intersection.

        return the algorithmic object from Intersection.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of intersection-points in case of cross intersections. NbPoints returns 0 if no intersections were found.
        """
    def NbSegments(self) -> int: 
        """
        Returns the number of tangential intersections. NbSegments returns 0 if no intersections were found
        """
    def Point(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the intersection point of index Index. Intersection points are computed in case of cross intersections with a precision equal to the tolerance value assigned at the time of construction or in the function Init (this value is defaulted to 1.0e-6). Exceptions Standard_OutOfRange if index is not in the range [ 1,NbPoints ], where NbPoints is the number of computed intersection points
        """
    def Segment(self,Index : int,Curve1 : OCP.Geom2d.Geom2d_Curve,Curve2 : OCP.Geom2d.Geom2d_Curve) -> Any: 
        """
        Use this syntax only to get solutions of tangential intersection between two curves. Output values Curve1 and Curve2 are the intersection segments on the first curve and on the second curve accordingly. Parameter Index defines a number of computed solution. An intersection segment is a portion of an initial curve limited by two points. The distance from each point of this segment to the other curve is less or equal to the tolerance value assigned at the time of construction or in function Init (this value is defaulted to 1.0e-6). Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbSegments ], where NbSegments is the number of computed tangential intersections. Standard_NullObject if the algorithm is initialized for the computing of self-intersections on a curve.
        """
    @overload
    def __init__(self,C1 : OCP.Geom2d.Geom2d_Curve,Tol : float=1e-06) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom2d.Geom2d_Curve,C2 : OCP.Geom2d.Geom2d_Curve,Tol : float=1e-06) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Geom2dAPI_Interpolate():
    """
    This class is used to interpolate a BsplineCurve passing through an array of points, with a C2 Continuity if tangency is not requested at the point. If tangency is requested at the point the continuity will be C1. If Perodicity is requested the curve will be closed and the junction will be the first point given. The curve will than be only C1 The curve is defined by a table of points through which it passes, and if required by a parallel table of reals which gives the value of the parameter of each point through which the resulting BSpline curve passes, and by vectors tangential to these points. An Interpolate object provides a framework for: defining the constraints of the BSpline curve, - implementing the interpolation algorithm, and consulting the results.
    """
    def Curve(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns the computed BSpline curve. Raises StdFail_NotDone if the interpolation fails.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the constrained BSpline curve is successfully constructed. Note: in this case, the result is given by the function Curve.
        """
    @overload
    def Load(self,InitialTangent : OCP.gp.gp_Vec2d,FinalTangent : OCP.gp.gp_Vec2d,Scale : bool=True) -> None: 
        """
        Assigns this constrained BSpline curve to be tangential to vectors InitialTangent and FinalTangent at its first and last points respectively (i.e. the first and last points of the table of points through which the curve passes, as defined at the time of initialization). <Scale> - boolean flag defining whether tangent vectors are to be scaled according to derivatives of lagrange interpolation.

        Assigns this constrained BSpline curve to be tangential to vectors defined in the table Tangents, which is parallel to the table of points through which the curve passes, as defined at the time of initialization. Vectors in the table Tangents are defined only if the flag given in the parallel table TangentFlags is true: only these vectors are set as tangency constraints. <Scale> - boolean flag defining whether tangent vectors are to be scaled according to derivatives of lagrange interpolation.
        """
    @overload
    def Load(self,Tangents : OCP.TColgp.TColgp_Array1OfVec2d,TangentFlags : OCP.TColStd.TColStd_HArray1OfBoolean,Scale : bool=True) -> None: ...
    def Perform(self) -> None: 
        """
        Computes the constrained BSpline curve. Use the function IsDone to verify that the computation is successful, and then the function Curve to obtain the result.
        """
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_HArray1OfPnt2d,PeriodicFlag : bool,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_HArray1OfPnt2d,Parameters : OCP.TColStd.TColStd_HArray1OfReal,PeriodicFlag : bool,Tolerance : float) -> None: ...
    pass
class Geom2dAPI_PointsToBSpline():
    """
    This class is used to approximate a BsplineCurve passing through an array of points, with a given Continuity. Describes functions for building a 2D BSpline curve which approximates a set of points. A PointsToBSpline object provides a framework for: - defining the data of the BSpline curve to be built, - implementing the approximation algorithm, and - consulting the results
    """
    def Curve(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns the approximate BSpline Curve
        """
    @overload
    def Init(self,YValues : OCP.TColStd.TColStd_Array1OfReal,X0 : float,DX : float,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol2D : float=1e-06) -> None: 
        """
        Approximate a BSpline Curve passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol2D

        Approximate a BSpline Curve passing through an array of Point. Of coordinates :

        Approximate a BSpline Curve passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol2D

        Approximate a BSpline Curve passing through an array of Point, which parameters are given by the array <Parameters>. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol2D

        Approximate a BSpline Curve passing through an array of Point using variational smoothing algorithm, which tries to minimize additional criterium: Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion
        """
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array1OfPnt2d,Weight1 : float,Weight2 : float,Weight3 : float,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol2D : float=0.001) -> None: ...
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array1OfPnt2d,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol2D : float=1e-06) -> None: ...
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array1OfPnt2d,ParType : OCP.Approx.Approx_ParametrizationType,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol2D : float=0.001) -> None: ...
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array1OfPnt2d,Parameters : OCP.TColStd.TColStd_Array1OfReal,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol2D : float=0.001) -> None: ...
    def IsDone(self) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array1OfPnt2d,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol2D : float=1e-06) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array1OfPnt2d,Weight1 : float,Weight2 : float,Weight3 : float,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array1OfPnt2d,Parameters : OCP.TColStd.TColStd_Array1OfReal,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol2D : float=0.001) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array1OfPnt2d,ParType : OCP.Approx.Approx_ParametrizationType,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol2D : float=0.001) -> None: ...
    @overload
    def __init__(self,YValues : OCP.TColStd.TColStd_Array1OfReal,X0 : float,DX : float,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol2D : float=1e-06) -> None: ...
    pass
class Geom2dAPI_ProjectPointOnCurve():
    """
    This class implements methods for computing all the orthogonal projections of a 2D point onto a 2D curve.
    """
    def Distance(self,Index : int) -> float: 
        """
        Computes the distance between the point and its computed orthogonal projection on the curve. Index is a number of computed projected point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.
        """
    def Extrema(self) -> OCP.Extrema.Extrema_ExtPC2d: 
        """
        return the algorithmic object from Extrema

        return the algorithmic object from Extrema
        """
    @overload
    def Init(self,P : OCP.gp.gp_Pnt2d,Curve : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Initializes this algorithm with the given arguments, and computes the orthogonal projections of a point <P> on a curve <Curve>

        Initializes this algorithm with the given arguments, and computes the orthogonal projections of the point P onto the portion of the curve Curve limited by the two points of parameter Umin and Usup.
        """
    @overload
    def Init(self,P : OCP.gp.gp_Pnt2d,Curve : OCP.Geom2d.Geom2d_Curve,Umin : float,Usup : float) -> None: ...
    def LowerDistance(self) -> float: 
        """
        Computes the distance between the point and its nearest orthogonal projection on the curve. Exceptions StdFail_NotDone if this algorithm fails.
        """
    def LowerDistanceParameter(self) -> float: 
        """
        Returns the parameter on the curve of the nearest orthogonal projection of the point. Exceptions StdFail_NotDone if this algorithm fails.
        """
    def NbPoints(self) -> int: 
        """
        return the number of of computed orthogonal projectionn points.
        """
    def NearestPoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the nearest orthogonal projection of the point on the curve. Exceptions StdFail_NotDone if this algorithm fails.
        """
    @overload
    def Parameter(self,Index : int) -> Tuple[float]: 
        """
        Returns the parameter on the curve of a point which is the orthogonal projection. Index is a number of a computed projected point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.

        Returns the parameter on the curve of a point which is the orthogonal projection. Index is a number of a computed projected point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points
        """
    @overload
    def Parameter(self,Index : int) -> float: ...
    def Point(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the orthogonal projection on the curve. Index is a number of a computed point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,Curve : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,Curve : OCP.Geom2d.Geom2d_Curve,Umin : float,Usup : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
