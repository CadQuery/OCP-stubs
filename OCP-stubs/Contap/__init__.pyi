import OCP.Contap
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.TColStd
import OCP.math
import OCP.NCollection
import OCP.Adaptor2d
import OCP.gp
import OCP.GeomAbs
import OCP.IntSurf
import OCP.Geom2d
import OCP.Standard
__all__  = [
"Contap_ArcFunction",
"Contap_ContAna",
"Contap_Contour",
"Contap_HContTool",
"Contap_HCurve2dTool",
"Contap_IType",
"Contap_Line",
"Contap_Point",
"Contap_SequenceOfIWLineOfTheIWalking",
"Contap_SequenceOfPathPointOfTheSearch",
"Contap_SequenceOfSegmentOfTheSearch",
"Contap_SurfFunction",
"Contap_SurfProps",
"Contap_TFunction",
"Contap_TheSequenceOfPoint",
"Contap_TheIWLineOfTheIWalking",
"Contap_TheIWalking",
"Contap_ThePathPointOfTheSearch",
"Contap_TheSearch",
"Contap_TheSearchInside",
"Contap_TheSegmentOfTheSearch",
"Contap_TheSequenceOfLine",
"Contap_TheHSequenceOfPoint",
"Contap_Circle",
"Contap_ContourPrs",
"Contap_ContourStd",
"Contap_DraftPrs",
"Contap_DraftStd",
"Contap_Lin",
"Contap_Restriction",
"Contap_Walking"
]
class Contap_ArcFunction(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        None
        """
    def LastComputedPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point, which has been computed while the last calling Value() method

        Returns the point, which has been computed while the last calling Value() method
        """
    def NbSamples(self) -> int: 
        """
        None
        """
    def Quadric(self) -> OCP.IntSurf.IntSurf_Quadric: 
        """
        None
        """
    @overload
    def Set(self,Direction : OCP.gp.gp_Dir) -> None: 
        """
        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @overload
    def Set(self,Eye : OCP.gp.gp_Pnt,Angle : float) -> None: ...
    @overload
    def Set(self,A : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> None: ...
    @overload
    def Set(self,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: ...
    @overload
    def Set(self,Direction : OCP.gp.gp_Dir,Angle : float) -> None: ...
    @overload
    def Set(self,Eye : OCP.gp.gp_Pnt) -> None: ...
    def Surface(self) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        Returns mySurf field

        Returns mySurf field
        """
    def Valpoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        None
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Contap_ContAna():
    """
    This class provides the computation of the contours for quadric surfaces.
    """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None

        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def Line(self,Index : int) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def NbContours(self) -> int: 
        """
        None

        None
        """
    @overload
    def Perform(self,C : OCP.gp.gp_Cone,Eye : OCP.gp.gp_Pnt) -> None: 
        """
        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @overload
    def Perform(self,C : OCP.gp.gp_Cylinder,D : OCP.gp.gp_Dir,Ang : float) -> None: ...
    @overload
    def Perform(self,S : OCP.gp.gp_Sphere,D : OCP.gp.gp_Dir,Ang : float) -> None: ...
    @overload
    def Perform(self,S : OCP.gp.gp_Sphere,Eye : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Cone,D : OCP.gp.gp_Dir) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Cylinder,Eye : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Cylinder,D : OCP.gp.gp_Dir) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Cone,D : OCP.gp.gp_Dir,Ang : float) -> None: ...
    @overload
    def Perform(self,S : OCP.gp.gp_Sphere,D : OCP.gp.gp_Dir) -> None: ...
    def TypeContour(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns GeomAbs_Line or GeomAbs_Circle, when IsDone() returns True.

        Returns GeomAbs_Line or GeomAbs_Circle, when IsDone() returns True.
        """
    def __init__(self) -> None: ...
    pass
class Contap_Contour():
    """
    None
    """
    @overload
    def Init(self,Direction : OCP.gp.gp_Vec) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Init(self,Eye : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Init(self,Direction : OCP.gp.gp_Vec,Angle : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if the is no line.

        Returns true if the is no line.
        """
    def Line(self,Index : int) -> Contap_Line: 
        """
        None

        None
        """
    def NbLines(self) -> int: 
        """
        None

        None
        """
    @overload
    def Perform(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool,Eye : OCP.gp.gp_Pnt) -> None: 
        """
        Creates the contour in a given direction.

        Creates the contour in a given direction.

        Creates the contour in a given direction.

        Creates the contour for a perspective view.
        """
    @overload
    def Perform(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool,Direction : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Perform(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool) -> None: ...
    @overload
    def Perform(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool,Direction : OCP.gp.gp_Vec,Angle : float) -> None: ...
    def SurfaceFunction(self) -> Contap_SurfFunction: 
        """
        Returns a reference on the internal SurfaceFunction. This is used to compute tangents on the lines.

        Returns a reference on the internal SurfaceFunction. This is used to compute tangents on the lines.
        """
    @overload
    def __init__(self,Eye : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool,Direction : OCP.gp.gp_Vec,Angle : float) -> None: ...
    @overload
    def __init__(self,Direction : OCP.gp.gp_Vec,Angle : float) -> None: ...
    @overload
    def __init__(self,Direction : OCP.gp.gp_Vec) -> None: ...
    @overload
    def __init__(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool,Eye : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool,Direction : OCP.gp.gp_Vec) -> None: ...
    pass
class Contap_HContTool():
    """
    Tool for the intersection between 2 surfaces. Regroupe pour l instant les methodes hors Adaptor3d...
    """
    @staticmethod
    def Bounds_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> Tuple[float, float]: 
        """
        Returns the parametric limits on the arc C. These limits must be finite : they are either the real limits of the arc, for a finite arc, or a bounding box for an infinite arc.
        """
    @staticmethod
    def HasBeenSeen_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> bool: 
        """
        Returns True if all the intersection point and edges are known on the Arc. The intersection point are given as vertices. The intersection edges are given as intervals between two vertices.
        """
    @staticmethod
    def HasFirstPoint_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,Index : int,IndFirst : int) -> bool: 
        """
        Returns True when the segment of range Index is not open at the left side. In that case, IndFirst is the range in the list intersection points (see NbPoints) of the one which defines the left bound of the segment. Otherwise, the method has to return False, and IndFirst has no meaning.
        """
    @staticmethod
    def HasLastPoint_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,Index : int,IndLast : int) -> bool: 
        """
        Returns True when the segment of range Index is not open at the right side. In that case, IndLast is the range in the list intersection points (see NbPoints) of the one which defines the right bound of the segment. Otherwise, the method has to return False, and IndLast has no meaning.
        """
    @staticmethod
    def IsAllSolution_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> bool: 
        """
        Returns True when the whole restriction is solution of the intersection problem.
        """
    @staticmethod
    def IsVertex_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,Index : int) -> bool: 
        """
        Returns True if the intersection point of range Index corresponds with a vertex on the arc A.
        """
    @staticmethod
    def NbPoints_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> int: 
        """
        Returns the number of intersection points on the arc A.
        """
    @staticmethod
    def NbSamplePoints_s(S : OCP.Adaptor3d.Adaptor3d_HSurface) -> int: 
        """
        None
        """
    @staticmethod
    def NbSamplesOnArc_s(A : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> int: 
        """
        returns the number of points which is used to make a sample on the arc. this number is a function of the Surface and the CurveOnSurface complexity.
        """
    @staticmethod
    def NbSamplesU_s(S : OCP.Adaptor3d.Adaptor3d_HSurface,u1 : float,u2 : float) -> int: 
        """
        None
        """
    @staticmethod
    def NbSamplesV_s(S : OCP.Adaptor3d.Adaptor3d_HSurface,v1 : float,v2 : float) -> int: 
        """
        None
        """
    @staticmethod
    def NbSegments_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> int: 
        """
        returns the number of part of A solution of the of intersection problem.
        """
    @staticmethod
    def Parameter_s(V : OCP.Adaptor3d.Adaptor3d_HVertex,C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        Returns the parameter of the vertex V on the arc A.
        """
    @staticmethod
    def Project_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,P : OCP.gp.gp_Pnt2d,Paramproj : float,Ptproj : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Projects the point P on the arc C. If the methods returns Standard_True, the projection is successful, and Paramproj is the parameter on the arc of the projected point, Ptproj is the projected Point. If the method returns Standard_False, Param proj and Ptproj are not significant.
        """
    @staticmethod
    def SamplePoint_s(S : OCP.Adaptor3d.Adaptor3d_HSurface,Index : int) -> Tuple[float, float]: 
        """
        None
        """
    @staticmethod
    def Tolerance_s(V : OCP.Adaptor3d.Adaptor3d_HVertex,C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        Returns the parametric tolerance used to consider that the vertex and another point meet, i-e if Abs(parameter(Vertex) - parameter(OtherPnt))<= Tolerance, the points are "merged".
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,Index : int,Pt : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        Returns the value (Pt), the tolerance (Tol), and the parameter (U) on the arc A , of the intersection point of range Index.
        """
    @staticmethod
    def Vertex_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,Index : int,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> None: 
        """
        When IsVertex returns True, this method returns the vertex on the arc A.
        """
    def __init__(self) -> None: ...
    pass
class Contap_HCurve2dTool():
    """
    None
    """
    @staticmethod
    def BSpline_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Circ2d: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Computes the point of parameter U on the curve.
        """
    @staticmethod
    def D1_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    @staticmethod
    def D2_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    @staticmethod
    def D3_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    @staticmethod
    def DN_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    @staticmethod
    def Ellipse_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Elips2d: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Hyperbola_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Hypr2d: 
        """
        None
        """
    @staticmethod
    def Intervals_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def IsClosed_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPeriodic_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> bool: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(myclass) >= <S>
        """
    @staticmethod
    def NbSamples_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U0 : float,U1 : float) -> int: 
        """
        None
        """
    @staticmethod
    def Parabola_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @staticmethod
    def Period_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self) -> None: ...
    pass
class Contap_IType():
    """
    None

    Members:

      Contap_Lin

      Contap_Circle

      Contap_Walking

      Contap_Restriction
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
    Contap_Circle: OCP.Contap.Contap_IType # value = <Contap_IType.Contap_Circle: 1>
    Contap_Lin: OCP.Contap.Contap_IType # value = <Contap_IType.Contap_Lin: 0>
    Contap_Restriction: OCP.Contap.Contap_IType # value = <Contap_IType.Contap_Restriction: 3>
    Contap_Walking: OCP.Contap.Contap_IType # value = <Contap_IType.Contap_Walking: 2>
    __entries: dict # value = {'Contap_Lin': (<Contap_IType.Contap_Lin: 0>, None), 'Contap_Circle': (<Contap_IType.Contap_Circle: 1>, None), 'Contap_Walking': (<Contap_IType.Contap_Walking: 2>, None), 'Contap_Restriction': (<Contap_IType.Contap_Restriction: 3>, None)}
    __members__: dict # value = {'Contap_Lin': <Contap_IType.Contap_Lin: 0>, 'Contap_Circle': <Contap_IType.Contap_Circle: 1>, 'Contap_Walking': <Contap_IType.Contap_Walking: 2>, 'Contap_Restriction': <Contap_IType.Contap_Restriction: 3>}
    pass
class Contap_Line():
    """
    None
    """
    @overload
    def Add(self,POn2S : OCP.IntSurf.IntSurf_PntOn2S) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Add(self,P : OCP.IntSurf.IntSurf_PntOn2S) -> None: ...
    @overload
    def Add(self,P : Contap_Point) -> None: ...
    def Arc(self) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        None
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None

        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None

        None
        """
    def LineOn2S(self) -> OCP.IntSurf.IntSurf_LineOn2S: 
        """
        None

        None
        """
    def NbPnts(self) -> int: 
        """
        None

        None
        """
    def NbVertex(self) -> int: 
        """
        None

        None
        """
    def Point(self,Index : int) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        None

        None
        """
    def ResetSeqOfVertex(self) -> None: 
        """
        None
        """
    def SetLineOn2S(self,L : OCP.IntSurf.IntSurf_LineOn2S) -> None: 
        """
        None
        """
    def SetTransitionOnS(self,T : OCP.IntSurf.IntSurf_TypeTrans) -> None: 
        """
        Set The Tansition of the line.
        """
    @overload
    def SetValue(self,C : OCP.gp.gp_Circ) -> None: 
        """
        None

        None

        None
        """
    @overload
    def SetValue(self,A : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> None: ...
    @overload
    def SetValue(self,L : OCP.gp.gp_Lin) -> None: ...
    def TransitionOnS(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        returns IN if at the "left" of the line, the normale of the surface is oriented to the observator.
        """
    def TypeContour(self) -> Contap_IType: 
        """
        Returns Contap_Lin for a line, Contap_Circle for a circle, and Contap_Walking for a Walking line, Contap_Restriction for a part of boundarie.

        Returns Contap_Lin for a line, Contap_Circle for a circle, and Contap_Walking for a Walking line, Contap_Restriction for a part of boundarie.
        """
    def Vertex(self,Index : int) -> Contap_Point: 
        """
        None

        None
        """
    def __init__(self) -> None: ...
    pass
class Contap_Point():
    """
    Definition of a vertex on the contour line. Most of the time, such a point is an intersection between the contour and a restriction of the surface. When it is not tyhe method IsOnArc return False. Such a point is contains geometrical informations (see the Value method) and logical informations.
    """
    def Arc(self) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        Returns the arc of restriction containing the vertex.

        Returns the arc of restriction containing the vertex.
        """
    def IsInternal(self) -> bool: 
        """
        Returns True if the point is an internal one, i.e if the tangent to the line on the point and the eye direction are parallel.

        Returns True if the point is an internal one, i.e if the tangent to the line on the point and the eye direction are parallel.
        """
    def IsMultiple(self) -> bool: 
        """
        Returns True if the point belongs to several lines.

        Returns True if the point belongs to several lines.
        """
    def IsOnArc(self) -> bool: 
        """
        Returns True when the point is an intersection between the contour and a restriction.

        Returns True when the point is an intersection between the contour and a restriction.
        """
    def IsVertex(self) -> bool: 
        """
        Returns TRUE if the point is a vertex on the initial restriction facet of the surface.

        Returns TRUE if the point is a vertex on the initial restriction facet of the surface.
        """
    def ParameterOnArc(self) -> float: 
        """
        Returns the parameter of the point on the arc returned by the method Arc().

        Returns the parameter of the point on the arc returned by the method Arc().
        """
    def ParameterOnLine(self) -> float: 
        """
        This method returns the parameter of the point on the intersection line. If the points does not belong to an intersection line, the value returned does not have any sens.

        This method returns the parameter of the point on the intersection line. If the points does not belong to an intersection line, the value returned does not have any sens.
        """
    def Parameters(self) -> Tuple[float, float]: 
        """
        Returns the parameters on the surface of the point.

        Returns the parameters on the surface of the point.
        """
    def SetArc(self,A : OCP.Adaptor2d.Adaptor2d_HCurve2d,Param : float,TLine : OCP.IntSurf.IntSurf_Transition,TArc : OCP.IntSurf.IntSurf_Transition) -> None: 
        """
        Sets the value of the arc and of the parameter on this arc of the point.

        Sets the value of the arc and of the parameter on this arc of the point.
        """
    def SetInternal(self) -> None: 
        """
        None

        None
        """
    def SetMultiple(self) -> None: 
        """
        None

        None
        """
    def SetParameter(self,Para : float) -> None: 
        """
        Set the value of the parameter on the intersection line.

        Set the value of the parameter on the intersection line.
        """
    def SetValue(self,Pt : OCP.gp.gp_Pnt,U : float,V : float) -> None: 
        """
        Sets the values for a point.

        Sets the values for a point.
        """
    def SetVertex(self,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> None: 
        """
        Sets the values of a point which is a vertex on the initial facet of restriction of one of the surface.

        Sets the values of a point which is a vertex on the initial facet of restriction of one of the surface.
        """
    def TransitionOnArc(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        Returns the transition of the point on the arc.

        Returns the transition of the point on the arc.
        """
    def TransitionOnLine(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        Returns the transition of the point on the contour.

        Returns the transition of the point on the contour.
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the intersection point (geometric information).

        Returns the intersection point (geometric information).
        """
    def Vertex(self) -> OCP.Adaptor3d.Adaptor3d_HVertex: 
        """
        Returns the information about the point when it is on the domain of the patch, i-e when the function IsVertex returns True. Otherwise, an exception is raised.

        Returns the information about the point when it is on the domain of the patch, i-e when the function IsVertex returns True. Otherwise, an exception is raised.
        """
    @overload
    def __init__(self,Pt : OCP.gp.gp_Pnt,U : float,V : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Contap_SequenceOfIWLineOfTheIWalking(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Contap_SequenceOfIWLineOfTheIWalking) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Contap_TheIWLineOfTheIWalking) -> None: ...
    def Assign(self,theOther : Contap_SequenceOfIWLineOfTheIWalking) -> Contap_SequenceOfIWLineOfTheIWalking: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Contap_TheIWLineOfTheIWalking: 
        """
        First item access
        """
    def ChangeLast(self) -> Contap_TheIWLineOfTheIWalking: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Contap_TheIWLineOfTheIWalking: 
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
    def First(self) -> Contap_TheIWLineOfTheIWalking: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Contap_SequenceOfIWLineOfTheIWalking) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Contap_TheIWLineOfTheIWalking) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Contap_TheIWLineOfTheIWalking) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Contap_SequenceOfIWLineOfTheIWalking) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Contap_TheIWLineOfTheIWalking: 
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
    def Prepend(self,theItem : Contap_TheIWLineOfTheIWalking) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Contap_SequenceOfIWLineOfTheIWalking) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Contap_TheIWLineOfTheIWalking) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Contap_SequenceOfIWLineOfTheIWalking) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Contap_TheIWLineOfTheIWalking: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Contap_SequenceOfIWLineOfTheIWalking) -> None: ...
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
class Contap_SequenceOfPathPointOfTheSearch(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Contap_SequenceOfPathPointOfTheSearch) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Contap_ThePathPointOfTheSearch) -> None: ...
    def Assign(self,theOther : Contap_SequenceOfPathPointOfTheSearch) -> Contap_SequenceOfPathPointOfTheSearch: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Contap_ThePathPointOfTheSearch: 
        """
        First item access
        """
    def ChangeLast(self) -> Contap_ThePathPointOfTheSearch: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Contap_ThePathPointOfTheSearch: 
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
    def First(self) -> Contap_ThePathPointOfTheSearch: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Contap_SequenceOfPathPointOfTheSearch) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Contap_ThePathPointOfTheSearch) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Contap_ThePathPointOfTheSearch) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Contap_SequenceOfPathPointOfTheSearch) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Contap_ThePathPointOfTheSearch: 
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
    def Prepend(self,theItem : Contap_ThePathPointOfTheSearch) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Contap_SequenceOfPathPointOfTheSearch) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Contap_ThePathPointOfTheSearch) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Contap_SequenceOfPathPointOfTheSearch) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Contap_ThePathPointOfTheSearch: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Contap_SequenceOfPathPointOfTheSearch) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Contap_SequenceOfSegmentOfTheSearch(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Contap_TheSegmentOfTheSearch) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Contap_SequenceOfSegmentOfTheSearch) -> None: ...
    def Assign(self,theOther : Contap_SequenceOfSegmentOfTheSearch) -> Contap_SequenceOfSegmentOfTheSearch: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Contap_TheSegmentOfTheSearch: 
        """
        First item access
        """
    def ChangeLast(self) -> Contap_TheSegmentOfTheSearch: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Contap_TheSegmentOfTheSearch: 
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
    def First(self) -> Contap_TheSegmentOfTheSearch: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Contap_SequenceOfSegmentOfTheSearch) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Contap_TheSegmentOfTheSearch) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Contap_TheSegmentOfTheSearch) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Contap_SequenceOfSegmentOfTheSearch) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Contap_TheSegmentOfTheSearch: 
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
    def Prepend(self,theItem : Contap_TheSegmentOfTheSearch) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Contap_SequenceOfSegmentOfTheSearch) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Contap_TheSegmentOfTheSearch) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Contap_SequenceOfSegmentOfTheSearch) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Contap_TheSegmentOfTheSearch: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Contap_SequenceOfSegmentOfTheSearch) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Contap_SurfFunction(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    This class describes the function on a parametric surface. the form of the function is F(u,v) = 0 where u and v are the parameteric coordinates of a point on the surface, to compute the contours of the surface.
    """
    def Angle(self) -> float: 
        """
        None

        None
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        The dimension of D is (1,2).
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        None

        None
        """
    def Direction2d(self) -> OCP.gp.gp_Dir2d: 
        """
        None

        None
        """
    def Direction3d(self) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    def Eye(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def FunctionType(self) -> Contap_TFunction: 
        """
        None

        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def IsTangent(self) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        This method has to return 1.
        """
    def NbVariables(self) -> int: 
        """
        This method has to return 2.
        """
    def PSurface(self) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        Method is entered for compatibility with IntPatch_TheSurfFunction.
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the value of the solution point on the surface.

        Returns the value of the solution point on the surface.
        """
    def Root(self) -> float: 
        """
        Root is the value of the function at the solution. It is a vector of dimension 1, i-e a real.

        Root is the value of the function at the solution. It is a vector of dimension 1, i-e a real.
        """
    @overload
    def Set(self,Eye : OCP.gp.gp_Pnt,Angle : float) -> None: 
        """
        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @overload
    def Set(self,Dir : OCP.gp.gp_Dir) -> None: ...
    @overload
    def Set(self,Eye : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Set(self,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: ...
    @overload
    def Set(self,Tolerance : float) -> None: ...
    @overload
    def Set(self,Direction : OCP.gp.gp_Dir,Angle : float) -> None: ...
    @overload
    def Set(self,Direction : OCP.gp.gp_Dir) -> None: ...
    @overload
    def Set(self,Dir : OCP.gp.gp_Dir,Angle : float) -> None: ...
    def Surface(self) -> OCP.Adaptor3d.Adaptor3d_HSurface: 
        """
        None

        None
        """
    def Tolerance(self) -> float: 
        """
        Returns the value Tol so that if Abs(Func.Root())<Tol the function is considered null.

        Returns the value Tol so that if Abs(Func.Root())<Tol the function is considered null.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        The dimension of F is 1.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Contap_SurfProps():
    """
    Internal tool used to compute the normal and its derivatives.
    """
    @staticmethod
    def DerivAndNorm_s(S : OCP.Adaptor3d.Adaptor3d_HSurface,U : float,V : float,P : OCP.gp.gp_Pnt,d1u : OCP.gp.gp_Vec,d1v : OCP.gp.gp_Vec,N : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P>, and normal vector <N> on <S> at parameters U,V.
        """
    @staticmethod
    def NormAndDn_s(S : OCP.Adaptor3d.Adaptor3d_HSurface,U : float,V : float,P : OCP.gp.gp_Pnt,N : OCP.gp.gp_Vec,Dnu : OCP.gp.gp_Vec,Dnv : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P>, normal vector <N>, and its derivatives <Dnu> and <Dnv> on <S> at parameters U,V.
        """
    @staticmethod
    def Normale_s(S : OCP.Adaptor3d.Adaptor3d_HSurface,U : float,V : float,P : OCP.gp.gp_Pnt,N : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P>, and normal vector <N> on <S> at parameters U,V.
        """
    def __init__(self) -> None: ...
    pass
class Contap_TFunction():
    """
    None

    Members:

      Contap_ContourStd

      Contap_ContourPrs

      Contap_DraftStd

      Contap_DraftPrs
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
    Contap_ContourPrs: OCP.Contap.Contap_TFunction # value = <Contap_TFunction.Contap_ContourPrs: 1>
    Contap_ContourStd: OCP.Contap.Contap_TFunction # value = <Contap_TFunction.Contap_ContourStd: 0>
    Contap_DraftPrs: OCP.Contap.Contap_TFunction # value = <Contap_TFunction.Contap_DraftPrs: 3>
    Contap_DraftStd: OCP.Contap.Contap_TFunction # value = <Contap_TFunction.Contap_DraftStd: 2>
    __entries: dict # value = {'Contap_ContourStd': (<Contap_TFunction.Contap_ContourStd: 0>, None), 'Contap_ContourPrs': (<Contap_TFunction.Contap_ContourPrs: 1>, None), 'Contap_DraftStd': (<Contap_TFunction.Contap_DraftStd: 2>, None), 'Contap_DraftPrs': (<Contap_TFunction.Contap_DraftPrs: 3>, None)}
    __members__: dict # value = {'Contap_ContourStd': <Contap_TFunction.Contap_ContourStd: 0>, 'Contap_ContourPrs': <Contap_TFunction.Contap_ContourPrs: 1>, 'Contap_DraftStd': <Contap_TFunction.Contap_DraftStd: 2>, 'Contap_DraftPrs': <Contap_TFunction.Contap_DraftPrs: 3>}
    pass
class Contap_TheSequenceOfPoint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Contap_Point) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Contap_TheSequenceOfPoint) -> None: ...
    def Assign(self,theOther : Contap_TheSequenceOfPoint) -> Contap_TheSequenceOfPoint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Contap_Point: 
        """
        First item access
        """
    def ChangeLast(self) -> Contap_Point: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Contap_Point: 
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
    def First(self) -> Contap_Point: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Contap_Point) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Contap_TheSequenceOfPoint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Contap_TheSequenceOfPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Contap_Point) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Contap_Point: 
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
    def Prepend(self,theItem : Contap_Point) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Contap_TheSequenceOfPoint) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Contap_Point) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Contap_TheSequenceOfPoint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Contap_Point: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Contap_TheSequenceOfPoint) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Contap_TheIWLineOfTheIWalking(OCP.Standard.Standard_Transient):
    def AddIndexPassing(self,Index : int) -> None: 
        """
        associer a l 'indice du point sur la ligne l'indice du point passant dans l'iterateur de depart
        """
    def AddPoint(self,P : OCP.IntSurf.IntSurf_PntOn2S) -> None: 
        """
        Add a point in the line.
        """
    @overload
    def AddStatusFirst(self,Closed : bool,HasFirst : bool) -> None: 
        """
        None

        None
        """
    @overload
    def AddStatusFirst(self,Closed : bool,HasLast : bool,Index : int,P : OCP.IntSurf.IntSurf_PathPoint) -> None: ...
    def AddStatusFirstLast(self,Closed : bool,HasFirst : bool,HasLast : bool) -> None: 
        """
        None
        """
    @overload
    def AddStatusLast(self,HasLast : bool) -> None: 
        """
        None

        None
        """
    @overload
    def AddStatusLast(self,HasLast : bool,Index : int,P : OCP.IntSurf.IntSurf_PathPoint) -> None: ...
    def Cut(self,Index : int) -> None: 
        """
        Cut the line at the point of rank Index.
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
    def FirstPoint(self) -> OCP.IntSurf.IntSurf_PathPoint: 
        """
        Returns the first point of the line when it is a marching point. An exception is raised if HasFirstPoint returns False.
        """
    def FirstPointIndex(self) -> int: 
        """
        Returns the Index of first point of the line when it is a marching point.This index is the index in the PointStartIterator. An exception is raised if HasFirstPoint returns False.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if the first point of the line is a marching point . when is HasFirstPoint==False ,the line begins on the natural bound of the surface.the line can be too long
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if the end point of the line is a marching point (Point from IntWS). when is HasFirstPoint==False ,the line ends on the natural bound of the surface.the line can be too long.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsClosed(self) -> bool: 
        """
        Returns True if the line is closed.
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
    def IsTangentAtBegining(self) -> bool: 
        """
        None
        """
    def IsTangentAtEnd(self) -> bool: 
        """
        None
        """
    def LastPoint(self) -> OCP.IntSurf.IntSurf_PathPoint: 
        """
        Returns the last point of the line when it is a marching point. An exception is raised if HasLastPoint returns False.
        """
    def LastPointIndex(self) -> int: 
        """
        Returns the index of last point of the line when it is a marching point.This index is the index in the PointStartIterator. An exception is raised if HasLastPoint returns False.
        """
    def Line(self) -> OCP.IntSurf.IntSurf_LineOn2S: 
        """
        Returns the LineOn2S contained in the walking line.
        """
    def NbPassingPoint(self) -> int: 
        """
        returns the number of points belonging to Pnts1 which are passing point.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points of the line (including first point and end point : see HasLastPoint and HasFirstPoint).
        """
    def PassingPoint(self,Index : int) -> Tuple[int, int]: 
        """
        returns the index of the point belonging to the line which is associated to the passing point belonging to Pnts1 an exception is raised if Index > NbPassingPoint()
        """
    def Reverse(self) -> None: 
        """
        reverse the points in the line. Hasfirst, HasLast are kept.
        """
    def SetTangencyAtBegining(self,IsTangent : bool) -> None: 
        """
        None
        """
    def SetTangencyAtEnd(self,IsTangent : bool) -> None: 
        """
        None
        """
    def SetTangentVector(self,V : OCP.gp.gp_Vec,Index : int) -> None: 
        """
        None
        """
    def TangentVector(self,Index : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,Index : int) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        Returns the point of range Index. If index <= 0 or Index > NbPoints, an exception is raised.
        """
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
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
class Contap_TheIWalking():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the calculus was successful.
        """
    def NbLines(self) -> int: 
        """
        Returns the number of resulting polylines. An exception is raised if IsDone returns False.
        """
    def NbSinglePnts(self) -> int: 
        """
        Returns the number of points belonging to Pnts on which no line starts or ends. An exception is raised if IsDone returns False.
        """
    @overload
    def Perform(self,Pnts1 : OCP.IntSurf.IntSurf_SequenceOfPathPoint,Func : Contap_SurfFunction,S : OCP.Adaptor3d.Adaptor3d_HSurface,Reversed : bool=False) -> None: 
        """
        Searches a set of polylines starting on a point of Pnts1 or Pnts2. Each point on a resulting polyline verifies F(u,v)=0

        Searches a set of polylines starting on a point of Pnts1. Each point on a resulting polyline verifies F(u,v)=0
        """
    @overload
    def Perform(self,Pnts1 : OCP.IntSurf.IntSurf_SequenceOfPathPoint,Pnts2 : OCP.IntSurf.IntSurf_SequenceOfInteriorPoint,Func : Contap_SurfFunction,S : OCP.Adaptor3d.Adaptor3d_HSurface,Reversed : bool=False) -> None: ...
    def SetTolerance(self,Epsilon : float,Deflection : float,Step : float) -> None: 
        """
        Deflection is the maximum deflection admitted between two consecutive points on a resulting polyline. Step is the maximum increment admitted between two consecutive points (in 2d space). Epsilon is the tolerance beyond which 2 points are confused
        """
    def SinglePnt(self,Index : int) -> OCP.IntSurf.IntSurf_PathPoint: 
        """
        Returns the point of range Index . An exception is raised if IsDone returns False. An exception is raised if Index<=0 or Index > NbSinglePnts.
        """
    def Value(self,Index : int) -> Contap_TheIWLineOfTheIWalking: 
        """
        Returns the polyline of range Index. An exception is raised if IsDone is False. An exception is raised if Index<=0 or Index>NbLines.
        """
    def __init__(self,Epsilon : float,Deflection : float,Step : float,theToFillHoles : bool=False) -> None: ...
    pass
class Contap_ThePathPointOfTheSearch():
    """
    None
    """
    def Arc(self) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        None
        """
    def IsNew(self) -> bool: 
        """
        None
        """
    def Parameter(self) -> float: 
        """
        None
        """
    @overload
    def SetValue(self,P : OCP.gp.gp_Pnt,Tol : float,V : OCP.Adaptor3d.Adaptor3d_HVertex,A : OCP.Adaptor2d.Adaptor2d_HCurve2d,Parameter : float) -> None: 
        """
        None

        None
        """
    @overload
    def SetValue(self,P : OCP.gp.gp_Pnt,Tol : float,A : OCP.Adaptor2d.Adaptor2d_HCurve2d,Parameter : float) -> None: ...
    def Tolerance(self) -> float: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Vertex(self) -> OCP.Adaptor3d.Adaptor3d_HVertex: 
        """
        None
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Tol : float,A : OCP.Adaptor2d.Adaptor2d_HCurve2d,Parameter : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Tol : float,V : OCP.Adaptor3d.Adaptor3d_HVertex,A : OCP.Adaptor2d.Adaptor2d_HCurve2d,Parameter : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Contap_TheSearch():
    """
    None
    """
    def AllArcSolution(self) -> bool: 
        """
        Returns true if all arc of the Arcs are solution (inside the surface). An exception is raised if IsDone returns False.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the calculus was successful.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of resulting points. An exception is raised if IsDone returns False (NotDone).
        """
    def NbSegments(self) -> int: 
        """
        Returns the number of the resulting segments. An exception is raised if IsDone returns False (NotDone).
        """
    def Perform(self,F : Contap_ArcFunction,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool,TolBoundary : float,TolTangency : float,RecheckOnRegularity : bool=False) -> None: 
        """
        Algorithm to find the points and parts of curves of Domain (domain of of restriction of a surface) which verify F = 0. TolBoundary defines if a curve is on Q. TolTangency defines if a point is on Q.
        """
    def Point(self,Index : int) -> Contap_ThePathPointOfTheSearch: 
        """
        Returns the resulting point of range Index. The exception NotDone is raised if IsDone() returns False. The exception OutOfRange is raised if Index <= 0 or Index > NbPoints.
        """
    def Segment(self,Index : int) -> Contap_TheSegmentOfTheSearch: 
        """
        Returns the resulting segment of range Index. The exception NotDone is raised if IsDone() returns False. The exception OutOfRange is raised if Index <= 0 or Index > NbPoints.
        """
    def __init__(self) -> None: ...
    pass
class Contap_TheSearchInside():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points. The exception NotDone if raised if IsDone returns False.
        """
    @overload
    def Perform(self,F : Contap_SurfFunction,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,T : OCP.Adaptor3d.Adaptor3d_TopolTool,Epsilon : float) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,F : Contap_SurfFunction,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,UStart : float,VStart : float) -> None: ...
    def Value(self,Index : int) -> OCP.IntSurf.IntSurf_InteriorPoint: 
        """
        Returns the point of range Index. The exception NotDone if raised if IsDone returns False. The exception OutOfRange if raised if Index <= 0 or Index > NbPoints.
        """
    @overload
    def __init__(self,F : Contap_SurfFunction,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,T : OCP.Adaptor3d.Adaptor3d_TopolTool,Epsilon : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Contap_TheSegmentOfTheSearch():
    """
    None
    """
    def Curve(self) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        Returns the geometric curve on the surface 's domain which is solution.
        """
    def FirstPoint(self) -> Contap_ThePathPointOfTheSearch: 
        """
        Returns the first point.
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if there is a vertex (ThePathPoint) defining the lowest valid parameter on the arc.
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if there is a vertex (ThePathPoint) defining the greatest valid parameter on the arc.
        """
    def LastPoint(self) -> Contap_ThePathPointOfTheSearch: 
        """
        Returns the last point.
        """
    def SetLimitPoint(self,V : Contap_ThePathPointOfTheSearch,First : bool) -> None: 
        """
        Defines the first point or the last point, depending on the value of the boolean First.
        """
    def SetValue(self,A : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> None: 
        """
        Defines the concerned arc.
        """
    def __init__(self) -> None: ...
    pass
class Contap_TheSequenceOfLine(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Contap_TheSequenceOfLine) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Contap_Line) -> None: ...
    def Assign(self,theOther : Contap_TheSequenceOfLine) -> Contap_TheSequenceOfLine: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Contap_Line: 
        """
        First item access
        """
    def ChangeLast(self) -> Contap_Line: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Contap_Line: 
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
    def First(self) -> Contap_Line: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Contap_TheSequenceOfLine) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Contap_Line) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Contap_Line) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Contap_TheSequenceOfLine) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Contap_Line: 
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
    def Prepend(self,theItem : Contap_Line) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Contap_TheSequenceOfLine) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Contap_Line) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Contap_TheSequenceOfLine) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Contap_Line: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Contap_TheSequenceOfLine) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Contap_TheHSequenceOfPoint(Contap_TheSequenceOfPoint, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Contap_Point) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : Contap_TheSequenceOfPoint) -> None: ...
    def Assign(self,theOther : Contap_TheSequenceOfPoint) -> Contap_TheSequenceOfPoint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Contap_Point: 
        """
        First item access
        """
    def ChangeLast(self) -> Contap_Point: 
        """
        Last item access
        """
    def ChangeSequence(self) -> Contap_TheSequenceOfPoint: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> Contap_Point: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
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
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> Contap_Point: 
        """
        First item access
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Contap_Point) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Contap_TheSequenceOfPoint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Contap_TheSequenceOfPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Contap_Point) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> Contap_Point: 
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
    def Prepend(self,theItem : Contap_Point) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Contap_TheSequenceOfPoint) -> None: ...
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
    def Sequence(self) -> Contap_TheSequenceOfPoint: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : Contap_Point) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Contap_TheSequenceOfPoint) -> None: 
        """
        Split in two sequences
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Contap_Point: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Contap_TheSequenceOfPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
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
Contap_Circle: OCP.Contap.Contap_IType # value = <Contap_IType.Contap_Circle: 1>
Contap_ContourPrs: OCP.Contap.Contap_TFunction # value = <Contap_TFunction.Contap_ContourPrs: 1>
Contap_ContourStd: OCP.Contap.Contap_TFunction # value = <Contap_TFunction.Contap_ContourStd: 0>
Contap_DraftPrs: OCP.Contap.Contap_TFunction # value = <Contap_TFunction.Contap_DraftPrs: 3>
Contap_DraftStd: OCP.Contap.Contap_TFunction # value = <Contap_TFunction.Contap_DraftStd: 2>
Contap_Lin: OCP.Contap.Contap_IType # value = <Contap_IType.Contap_Lin: 0>
Contap_Restriction: OCP.Contap.Contap_IType # value = <Contap_IType.Contap_Restriction: 3>
Contap_Walking: OCP.Contap.Contap_IType # value = <Contap_IType.Contap_Walking: 2>
