import OCP.GeomAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom2d
import OCP.Approx
import OCP.gp
import OCP.TColgp
import OCP.Geom
import OCP.Extrema
import OCP.TColStd
__all__  = [
"GeomAPI",
"GeomAPI_ExtremaCurveCurve",
"GeomAPI_ExtremaCurveSurface",
"GeomAPI_ExtremaSurfaceSurface",
"GeomAPI_IntCS",
"GeomAPI_IntSS",
"GeomAPI_Interpolate",
"GeomAPI_PointsToBSpline",
"GeomAPI_PointsToBSplineSurface",
"GeomAPI_ProjectPointOnCurve",
"GeomAPI_ProjectPointOnSurf"
]
class GeomAPI():
    """
    The GeomAPI package provides an Application Programming Interface for the Geometry.
    """
    @staticmethod
    def To2d_s(C : OCP.Geom.Geom_Curve,P : OCP.gp.gp_Pln) -> OCP.Geom2d.Geom2d_Curve: 
        """
        This function builds (in the parametric space of the plane P) a 2D curve equivalent to the 3D curve C. The 3D curve C is considered to be located in the plane P. Warning The 3D curve C must be of one of the following types: - a line - a circle - an ellipse - a hyperbola - a parabola - a Bezier curve - a BSpline curve Exceptions Standard_NoSuchObject if C is not a defined type curve.
        """
    @staticmethod
    def To3d_s(C : OCP.Geom2d.Geom2d_Curve,P : OCP.gp.gp_Pln) -> OCP.Geom.Geom_Curve: 
        """
        Builds a 3D curve equivalent to the 2D curve C described in the parametric space defined by the local coordinate system of plane P. The resulting 3D curve is of the same nature as that of the curve C.
        """
    def __init__(self) -> None: ...
    pass
class GeomAPI_ExtremaCurveCurve():
    """
    Describes functions for computing all the extrema between two 3D curves. An ExtremaCurveCurve algorithm minimizes or maximizes the distance between a point on the first curve and a point on the second curve. Thus, it computes start and end points of perpendiculars common to the two curves (an intersection point is not an extremum unless the two curves are tangential at this point). Solutions consist of pairs of points, and an extremum is considered to be a segment joining the two points of a solution. An ExtremaCurveCurve object provides a framework for: - defining the construction of the extrema, - implementing the construction algorithm, and - consulting the results. Warning In some cases, the nearest points between two curves do not correspond to one of the computed extrema. Instead, they may be given by: - a limit point of one curve and one of the following: - its orthogonal projection on the other curve, - a limit point of the other curve; or - an intersection point between the two curves.
    """
    def Distance(self,Index : int) -> float: 
        """
        Computes the distance between the end points of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def Extrema(self) -> OCP.Extrema.Extrema_ExtCC: 
        """
        return the algorithmic object from Extrema

        return the algorithmic object from Extrema
        """
    @overload
    def Init(self,C1 : OCP.Geom.Geom_Curve,C2 : OCP.Geom.Geom_Curve) -> None: 
        """
        Initializes this algorithm with the given arguments and computes the extrema between the curves C1 and C2

        Initializes this algorithm with the given arguments and computes the extrema between : - the portion of the curve C1 limited by the two points of parameter (U1min,U1max), and - the portion of the curve C2 limited by the two points of parameter (U2min,U2max). Warning Use the function NbExtrema to obtain the number of solutions. If this algorithm fails, NbExtrema returns 0.
        """
    @overload
    def Init(self,C1 : OCP.Geom.Geom_Curve,C2 : OCP.Geom.Geom_Curve,U1min : float,U1max : float,U2min : float,U2max : float) -> None: ...
    def LowerDistance(self) -> float: 
        """
        Computes the distance between the end points of the shortest extremum computed by this algorithm. Exceptions StdFail_NotDone if this algorithm fails.
        """
    def LowerDistanceParameters(self) -> Tuple[float, float]: 
        """
        Returns the parameters U1 of the point on the first curve and U2 of the point on the second curve, which are the ends of the shortest extremum computed by this algorithm. Exceptions StdFail_NotDone if this algorithm fails.
        """
    def NbExtrema(self) -> int: 
        """
        Returns the number of extrema computed by this algorithm. Note: if this algorithm fails, NbExtrema returns 0.
        """
    def NearestPoints(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Returns the points P1 on the first curve and P2 on the second curve, which are the ends of the shortest extremum computed by this algorithm. Exceptions StdFail_NotDone if this algorithm fails.
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        Returns the parameters U1 of the point on the first curve and U2 of the point on the second curve, which are the ends of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def Points(self,Index : int,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Returns the points P1 on the first curve and P2 on the second curve, which are the ends of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def TotalLowerDistance(self) -> float: 
        """
        return the distance of the total nearest couple solution point. if <myExtCC> is not done
        """
    def TotalLowerDistanceParameters(self,U1 : float,U2 : float) -> bool: 
        """
        set in <U1> and <U2> the parameters of the couple solution points which represents the total nearest solution.
        """
    def TotalNearestPoints(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> bool: 
        """
        set in <P1> and <P2> the couple solution points such a the distance [P1,P2] is the minimum. taking in account extremity points of curves.
        """
    @overload
    def __init__(self,C1 : OCP.Geom.Geom_Curve,C2 : OCP.Geom.Geom_Curve,U1min : float,U1max : float,U2min : float,U2max : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom.Geom_Curve,C2 : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomAPI_ExtremaCurveSurface():
    """
    Describes functions for computing all the extrema between a curve and a surface. An ExtremaCurveSurface algorithm minimizes or maximizes the distance between a point on the curve and a point on the surface. Thus, it computes start and end points of perpendiculars common to the curve and the surface (an intersection point is not an extremum except where the curve and the surface are tangential at this point). Solutions consist of pairs of points, and an extremum is considered to be a segment joining the two points of a solution. An ExtremaCurveSurface object provides a framework for: - defining the construction of the extrema, - implementing the construction algorithm, and - consulting the results. Warning In some cases, the nearest points between a curve and a surface do not correspond to one of the computed extrema. Instead, they may be given by: - a point of a bounding curve of the surface and one of the following: - its orthogonal projection on the curve, - a limit point of the curve; or - a limit point of the curve and its projection on the surface; or - an intersection point between the curve and the surface.
    """
    def Distance(self,Index : int) -> float: 
        """
        Computes the distance between the end points of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def Extrema(self) -> OCP.Extrema.Extrema_ExtCS: 
        """
        Returns the algorithmic object from Extrema

        Returns the algorithmic object from Extrema
        """
    @overload
    def Init(self,Curve : OCP.Geom.Geom_Curve,Surface : OCP.Geom.Geom_Surface) -> None: 
        """
        Computes the extrema distances between the curve <C> and the surface <S>.

        Computes the extrema distances between the curve <C> and the surface <S>. The solution point are computed in the domain [Wmin,Wmax] of the curve and in the domain [Umin,Umax] [Vmin,Vmax] of the surface. Warning Use the function NbExtrema to obtain the number of solutions. If this algorithm fails, NbExtrema returns 0.
        """
    @overload
    def Init(self,Curve : OCP.Geom.Geom_Curve,Surface : OCP.Geom.Geom_Surface,Wmin : float,Wmax : float,Umin : float,Umax : float,Vmin : float,Vmax : float) -> None: ...
    def LowerDistance(self) -> float: 
        """
        Computes the distance between the end points of the shortest extremum computed by this algorithm. Exceptions - StdFail_NotDone if this algorithm fails.
        """
    def LowerDistanceParameters(self) -> Tuple[float, float, float]: 
        """
        Returns the parameters W of the point on the curve and (U,V) of the point on the surface, which are the ends of the shortest extremum computed by this algorithm. Exceptions - StdFail_NotDone if this algorithm fails.
        """
    def NbExtrema(self) -> int: 
        """
        Returns the number of extrema computed by this algorithm. Note: if this algorithm fails, NbExtrema returns 0.
        """
    def NearestPoints(self,PC : OCP.gp.gp_Pnt,PS : OCP.gp.gp_Pnt) -> None: 
        """
        Returns the points PC on the curve and PS on the surface, which are the ends of the shortest extremum computed by this algorithm. Exceptions - StdFail_NotDone if this algorithm fails.
        """
    def Parameters(self,Index : int) -> Tuple[float, float, float]: 
        """
        Returns the parameters W of the point on the curve, and (U,V) of the point on the surface, which are the ends of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def Points(self,Index : int,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Returns the points P1 on the curve and P2 on the surface, which are the ends of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    @overload
    def __init__(self,Curve : OCP.Geom.Geom_Curve,Surface : OCP.Geom.Geom_Surface,Wmin : float,Wmax : float,Umin : float,Umax : float,Vmin : float,Vmax : float) -> None: ...
    @overload
    def __init__(self,Curve : OCP.Geom.Geom_Curve,Surface : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomAPI_ExtremaSurfaceSurface():
    """
    Describes functions for computing all the extrema between two surfaces. An ExtremaSurfaceSurface algorithm minimizes or maximizes the distance between a point on the first surface and a point on the second surface. Results are start and end points of perpendiculars common to the two surfaces. Solutions consist of pairs of points, and an extremum is considered to be a segment joining the two points of a solution. An ExtremaSurfaceSurface object provides a framework for: - defining the construction of the extrema, - implementing the construction algorithm, and - consulting the results. Warning In some cases, the nearest points between the two surfaces do not correspond to one of the computed extrema. Instead, they may be given by: - a point of a bounding curve of one surface and one of the following: - its orthogonal projection on the other surface, - a point of a bounding curve of the other surface; or - any point on intersection curves between the two surfaces.
    """
    def Distance(self,Index : int) -> float: 
        """
        Computes the distance between the end points of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def Extrema(self) -> OCP.Extrema.Extrema_ExtSS: 
        """
        return the algorithmic object from Extrema

        return the algorithmic object from Extrema
        """
    @overload
    def Init(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface) -> None: 
        """
        Initializes this algorithm with the given arguments and computes the extrema distances between the surfaces <S1> and <S2>

        Initializes this algorithm with the given arguments and computes the extrema distances between - the portion of the surface S1 limited by the two values of parameter (U1min,U1max) in the u parametric direction, and by the two values of parameter (V1min,V1max) in the v parametric direction, and - the portion of the surface S2 limited by the two values of parameter (U2min,U2max) in the u parametric direction, and by the two values of parameter (V2min,V2max) in the v parametric direction.
        """
    @overload
    def Init(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,U1min : float,U1max : float,V1min : float,V1max : float,U2min : float,U2max : float,V2min : float,V2max : float) -> None: ...
    def LowerDistance(self) -> float: 
        """
        Computes the distance between the end points of the shortest extremum computed by this algorithm. Exceptions StdFail_NotDone if this algorithm fails.
        """
    def LowerDistanceParameters(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parameters (U1,V1) of the point on the first surface and (U2,V2) of the point on the second surface, which are the ends of the shortest extremum computed by this algorithm. Exceptions - StdFail_NotDone if this algorithm fails.
        """
    def NbExtrema(self) -> int: 
        """
        Returns the number of extrema computed by this algorithm. Note: if this algorithm fails, NbExtrema returns 0.
        """
    def NearestPoints(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Returns the points P1 on the first surface and P2 on the second surface, which are the ends of the shortest extremum computed by this algorithm. Exceptions StdFail_NotDone if this algorithm fails.
        """
    def Parameters(self,Index : int) -> Tuple[float, float, float, float]: 
        """
        Returns the parameters (U1,V1) of the point on the first surface, and (U2,V2) of the point on the second surface, which are the ends of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    def Points(self,Index : int,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Returns the points P1 on the first surface and P2 on the second surface, which are the ends of the extremum of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbExtrema ], where NbExtrema is the number of extrema computed by this algorithm.
        """
    @overload
    def __init__(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,U1min : float,U1max : float,V1min : float,V1max : float,U2min : float,U2max : float,V2min : float,V2max : float) -> None: ...
    pass
class GeomAPI_IntCS():
    """
    This class implements methods for computing intersection points and segments between a
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the intersections are successfully computed.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of Intersection Points if IsDone returns True. else NotDone is raised.
        """
    def NbSegments(self) -> int: 
        """
        Returns the number of computed intersection segments in case of tangential intersection. Exceptions StdFail_NotDone if the intersection algorithm fails or is not initialized.
        """
    @overload
    def Parameters(self,Index : int) -> Tuple[float, float, float, float]: 
        """
        Returns parameter W on the curve and (parameters U,V) on the surface of the computed intersection point of index Index in case of cross intersection. Exceptions StdFail_NotDone if intersection algorithm fails or is not initialized. Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of computed intersection points.

        Returns the parameters of the first (U1,V1) and the last (U2,V2) points of curve's segment on the surface in case of tangential intersection. Index is the number of computed intersection segments. Exceptions StdFail_NotDone if intersection algorithm fails or is not initialized. Standard_OutOfRange if Index is not in the range [ 1,NbSegments ], where NbSegments is the number of computed intersection segments.
        """
    @overload
    def Parameters(self,Index : int) -> Tuple[float, float, float]: ...
    def Perform(self,C : OCP.Geom.Geom_Curve,S : OCP.Geom.Geom_Surface) -> None: 
        """
        This function Initializes an algorithm with the curve C and the surface S and computes the intersections between C and S. Warning Use function IsDone to verify that the intersections are computed successfully.
        """
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Intersection Point of range <Index>in case of cross intersection. Raises NotDone if the computation has failed or if the computation has not been done raises OutOfRange if Index is not in the range <1..NbPoints>
        """
    def Segment(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        Returns the computed intersection segment of index Index in case of tangential intersection. Intersection segment is a portion of the initial curve tangent to surface. Exceptions StdFail_NotDone if intersection algorithm fails or is not initialized. Standard_OutOfRange if Index is not in the range [ 1,NbSegments ], where NbSegments is the number of computed intersection segments.
        """
    @overload
    def __init__(self,C : OCP.Geom.Geom_Curve,S : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomAPI_IntSS():
    """
    This class implements methods for computing the intersection curves between two surfaces. The result is curves from Geom. The "domain" used for a surface is the natural parametric domain unless the surface is a RectangularTrimmedSurface from Geom.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the intersection was successful.

        Returns True if the intersection was successful.
        """
    @overload
    def Line(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        Returns the computed intersection curve of index Index. Exceptions StdFail_NotDone if the computation fails. Standard_OutOfRange if Index is out of range [1, NbLines] where NbLines is the number of computed intersection curves.

        Returns the computed intersection curve of index Index. Exceptions StdFail_NotDone if the computation fails. Standard_OutOfRange if Index is out of range [1, NbLines] where NbLines is the number of computed intersection curves.
        """
    @overload
    def Line(self,I : int) -> OCP.Geom.Geom_Curve: ...
    def NbLines(self) -> int: 
        """
        Returns the number of computed intersection curves. Exceptions StdFail_NotDone if the computation fails.

        Returns the number of computed intersection curves. Exceptions StdFail_NotDone if the computation fails.
        """
    def Perform(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,Tol : float) -> None: 
        """
        Initializes an algorithm with the given arguments and computes the intersection curves between the two surfaces S1 and S2. Parameter Tol defines the precision of curves computation. For most cases the value 1.0e-7 is recommended to use. Warning Use function IsDone to verify that the intersections are successfully computed.

        Initializes an algorithm with the given arguments and computes the intersection curves between the two surfaces S1 and S2. Parameter Tol defines the precision of curves computation. For most cases the value 1.0e-7 is recommended to use. Warning Use function IsDone to verify that the intersections are successfully computed.
        """
    @overload
    def __init__(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomAPI_Interpolate():
    """
    This class is used to interpolate a BsplineCurve passing through an array of points, with a C2 Continuity if tangency is not requested at the point. If tangency is requested at the point the continuity will be C1. If Perodicity is requested the curve will be closed and the junction will be the first point given. The curve will than be only C1 Describes functions for building a constrained 3D BSpline curve. The curve is defined by a table of points through which it passes, and if required: - by a parallel table of reals which gives the value of the parameter of each point through which the resulting BSpline curve passes, and - by vectors tangential to these points. An Interpolate object provides a framework for: - defining the constraints of the BSpline curve, - implementing the interpolation algorithm, and - consulting the results.
    """
    def Curve(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        Returns the computed BSpline curve. Raises StdFail_NotDone if the interpolation fails.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the constrained BSpline curve is successfully constructed. Note: in this case, the result is given by the function Curve.
        """
    @overload
    def Load(self,InitialTangent : OCP.gp.gp_Vec,FinalTangent : OCP.gp.gp_Vec,Scale : bool=True) -> None: 
        """
        Assigns this constrained BSpline curve to be tangential to vectors InitialTangent and FinalTangent at its first and last points respectively (i.e. the first and last points of the table of points through which the curve passes, as defined at the time of initialization).

        Assigns this constrained BSpline curve to be tangential to vectors defined in the table Tangents, which is parallel to the table of points through which the curve passes, as defined at the time of initialization. Vectors in the table Tangents are defined only if the flag given in the parallel table TangentFlags is true: only these vectors are set as tangency constraints.
        """
    @overload
    def Load(self,Tangents : OCP.TColgp.TColgp_Array1OfVec,TangentFlags : OCP.TColStd.TColStd_HArray1OfBoolean,Scale : bool=True) -> None: ...
    def Perform(self) -> None: 
        """
        Computes the constrained BSpline curve. Use the function IsDone to verify that the computation is successful, and then the function Curve to obtain the result.
        """
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_HArray1OfPnt,Parameters : OCP.TColStd.TColStd_HArray1OfReal,PeriodicFlag : bool,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_HArray1OfPnt,PeriodicFlag : bool,Tolerance : float) -> None: ...
    pass
class GeomAPI_PointsToBSpline():
    """
    This class is used to approximate a BsplineCurve passing through an array of points, with a given Continuity. Describes functions for building a 3D BSpline curve which approximates a set of points. A PointsToBSpline object provides a framework for: - defining the data of the BSpline curve to be built, - implementing the approximation algorithm, and consulting the results.
    """
    def Curve(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        Returns the computed BSpline curve. Raises StdFail_NotDone if the curve is not built.
        """
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array1OfPnt,Parameters : OCP.TColStd.TColStd_Array1OfReal,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: 
        """
        Approximate a BSpline Curve passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol3D

        Approximate a BSpline Curve passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol3D

        Approximate a BSpline Curve passing through an array of Point, which parameters are given by the array <Parameters>. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol3D

        Approximate a BSpline Curve passing through an array of Point using variational smoothing algorithm, which tries to minimize additional criterium: Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion
        """
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array1OfPnt,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array1OfPnt,Weight1 : float,Weight2 : float,Weight3 : float,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array1OfPnt,ParType : OCP.Approx.Approx_ParametrizationType,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    def IsDone(self) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array1OfPnt,ParType : OCP.Approx.Approx_ParametrizationType,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array1OfPnt,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array1OfPnt,Weight1 : float,Weight2 : float,Weight3 : float,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array1OfPnt,Parameters : OCP.TColStd.TColStd_Array1OfReal,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    pass
class GeomAPI_PointsToBSplineSurface():
    """
    This class is used to approximate or interpolate a BSplineSurface passing through an Array2 of points, with a given continuity. Describes functions for building a BSpline surface which approximates or interpolates a set of points. A PointsToBSplineSurface object provides a framework for: - defining the data of the BSpline surface to be built, - implementing the approximation algorithm or the interpolation algorithm, and consulting the results. In fact, class contains 3 algorithms, 2 for approximation and 1 for interpolation. First approximation algorithm is based on usual least square criterium: minimization of square distance between samplimg points and result surface. Second approximation algorithm uses least square criterium and additional minimization of some local characteristic of surface (first, second and third partial derivative), which allows managing shape of surface. Interpolation algorithm produces surface, which passes through sampling points.
    """
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array2OfPnt,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: 
        """
        Approximates a BSpline Surface passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol3D.

        Approximates a BSpline Surface passing through an array of Points.

        Approximates a BSpline Surface passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be in the range [Degmin,Degmax] 2- his continuity will be at least <Continuity> 3- the distance from the point <Points> to the BSpline will be lower to Tol3D.

        Approximates a BSpline Surface passing through an array of point using variational smoothing algorithm, which tries to minimize additional criterium: Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion.
        """
    @overload
    def Init(self,ZPoints : OCP.TColStd.TColStd_Array2OfReal,X0 : float,dX : float,Y0 : float,dY : float,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array2OfPnt,Weight1 : float,Weight2 : float,Weight3 : float,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def Init(self,Points : OCP.TColgp.TColgp_Array2OfPnt,ParType : OCP.Approx.Approx_ParametrizationType,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001,thePeriodic : bool=False) -> None: ...
    @overload
    def Interpolate(self,Points : OCP.TColgp.TColgp_Array2OfPnt,thePeriodic : bool=False) -> None: 
        """
        Interpolates a BSpline Surface passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be 3. 2- his continuity will be C2.

        Interpolates a BSpline Surface passing through an array of Point. The resulting BSpline will have the following properties: 1- his degree will be 3. 2- his continuity will be C2.

        Interpolates a BSpline Surface passing through an array of Points.
        """
    @overload
    def Interpolate(self,ZPoints : OCP.TColStd.TColStd_Array2OfReal,X0 : float,dX : float,Y0 : float,dY : float) -> None: ...
    @overload
    def Interpolate(self,Points : OCP.TColgp.TColgp_Array2OfPnt,ParType : OCP.Approx.Approx_ParametrizationType,thePeriodic : bool=False) -> None: ...
    def IsDone(self) -> bool: 
        """
        None
        """
    def Surface(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Returns the approximate BSpline Surface
        """
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array2OfPnt,Weight1 : float,Weight2 : float,Weight3 : float,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array2OfPnt,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def __init__(self,ZPoints : OCP.TColStd.TColStd_Array2OfReal,X0 : float,dX : float,Y0 : float,dY : float,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColgp.TColgp_Array2OfPnt,ParType : OCP.Approx.Approx_ParametrizationType,DegMin : int=3,DegMax : int=8,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Tol3D : float=0.001) -> None: ...
    pass
class GeomAPI_ProjectPointOnCurve():
    """
    This class implements methods for computing all the orthogonal projections of a 3D point onto a 3D curve.
    """
    def Distance(self,Index : int) -> float: 
        """
        Computes the distance between the point and its orthogonal projection on the curve. Index is a number of a computed point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.
        """
    def Extrema(self) -> OCP.Extrema.Extrema_ExtPC: 
        """
        return the algorithmic object from Extrema

        return the algorithmic object from Extrema
        """
    @overload
    def Init(self,P : OCP.gp.gp_Pnt,Curve : OCP.Geom.Geom_Curve,Umin : float,Usup : float) -> None: 
        """
        Init the projection of a point <P> on a curve <Curve>

        Init the projection of a point <P> on a curve <Curve> limited by the two points of parameter Umin and Usup.

        Init the projection of a point <P> on a curve <Curve> limited by the two points of parameter Umin and Usup.
        """
    @overload
    def Init(self,P : OCP.gp.gp_Pnt,Curve : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def Init(self,Curve : OCP.Geom.Geom_Curve,Umin : float,Usup : float) -> None: ...
    def LowerDistance(self) -> float: 
        """
        Computes the distance between the point and its nearest orthogonal projection on the curve. Exceptions: StdFail_NotDone if this algorithm fails.
        """
    def LowerDistanceParameter(self) -> float: 
        """
        Returns the parameter on the curve of the nearest orthogonal projection of the point. Exceptions: StdFail_NotDone if this algorithm fails.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of computed orthogonal projection points. Note: if this algorithm fails, NbPoints returns 0.
        """
    def NearestPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the nearest orthogonal projection of the point on the curve. Exceptions: StdFail_NotDone if this algorithm fails.
        """
    @overload
    def Parameter(self,Index : int) -> Tuple[float]: 
        """
        Returns the parameter on the curve of the point, which is the orthogonal projection. Index is a number of a computed point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.

        Returns the parameter on the curve of the point, which is the orthogonal projection. Index is a number of a computed point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.-
        """
    @overload
    def Parameter(self,Index : int) -> float: ...
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Performs the projection of a point on the current curve.
        """
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the orthogonal projection on the curve. Index is a number of a computed point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Curve : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Curve : OCP.Geom.Geom_Curve,Umin : float,Usup : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomAPI_ProjectPointOnSurf():
    """
    This class implements methods for computing all the orthogonal projections of a point onto a surface.
    """
    def Distance(self,Index : int) -> float: 
        """
        Computes the distance between the point and its orthogonal projection on the surface. Index is a number of a computed point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.
        """
    def Extrema(self) -> OCP.Extrema.Extrema_ExtPS: 
        """
        return the algorithmic object from Extrema

        return the algorithmic object from Extrema
        """
    @overload
    def Init(self,P : OCP.gp.gp_Pnt,Surface : OCP.Geom.Geom_Surface,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: 
        """
        None

        Init the projection of a point <P> on a surface <Surface>. The solution are computed in the domain [Umin,Usup] [Vmin,Vsup] of the surface.

        None

        Init the projection for many points on a surface <Surface>. The solutions will be computed in the domain [Umin,Usup] [Vmin,Vsup] of the surface.

        None

        None
        """
    @overload
    def Init(self,P : OCP.gp.gp_Pnt,Surface : OCP.Geom.Geom_Surface,Tolerance : float,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def Init(self,Surface : OCP.Geom.Geom_Surface,Umin : float,Usup : float,Vmin : float,Vsup : float,Tolerance : float,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def Init(self,Surface : OCP.Geom.Geom_Surface,Umin : float,Usup : float,Vmin : float,Vsup : float,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def Init(self,P : OCP.gp.gp_Pnt,Surface : OCP.Geom.Geom_Surface,Umin : float,Usup : float,Vmin : float,Vsup : float,Tolerance : float,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def Init(self,P : OCP.gp.gp_Pnt,Surface : OCP.Geom.Geom_Surface,Umin : float,Usup : float,Vmin : float,Vsup : float,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    def IsDone(self) -> bool: 
        """
        None
        """
    def LowerDistance(self) -> float: 
        """
        Computes the distance between the point and its nearest orthogonal projection on the surface. Exceptions StdFail_NotDone if projection fails.
        """
    def LowerDistanceParameters(self) -> Tuple[float, float]: 
        """
        Returns the parameters (U,V) on the surface of the nearest computed orthogonal projection of the point. Exceptions StdFail_NotDone if projection fails.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of computed orthogonal projection points. Note: if projection fails, NbPoints returns 0.
        """
    def NearestPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the nearest orthogonal projection of the point on the surface. Exceptions StdFail_NotDone if projection fails.
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        Returns the parameters (U,V) on the surface of the orthogonal projection. Index is a number of a computed point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.
        """
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Performs the projection of a point on the current surface.
        """
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the orthogonal projection on the surface. Index is a number of a computed point. Exceptions Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where NbPoints is the number of solution points.
        """
    def SetExtremaAlgo(self,theAlgo : OCP.Extrema.Extrema_ExtAlgo) -> None: 
        """
        Sets the Extrema search algorithm - Grad or Tree. By default the Extrema is initialized with Grad algorithm.
        """
    def SetExtremaFlag(self,theExtFlag : OCP.Extrema.Extrema_ExtFlag) -> None: 
        """
        Sets the Extrema search flag - MIN or MAX or MINMAX. By default the Extrema is set to search the MinMax solutions.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Surface : OCP.Geom.Geom_Surface,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Surface : OCP.Geom.Geom_Surface,Umin : float,Usup : float,Vmin : float,Vsup : float,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Surface : OCP.Geom.Geom_Surface,Tolerance : float,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Surface : OCP.Geom.Geom_Surface,Umin : float,Usup : float,Vmin : float,Vsup : float,Tolerance : float,Algo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    pass
