import OCP.GCE2d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom2d
import OCP.gce
import OCP.gp
__all__  = [
"GCE2d_Root",
"GCE2d_MakeArcOfEllipse",
"GCE2d_MakeArcOfHyperbola",
"GCE2d_MakeArcOfParabola",
"GCE2d_MakeCircle",
"GCE2d_MakeEllipse",
"GCE2d_MakeHyperbola",
"GCE2d_MakeLine",
"GCE2d_MakeMirror",
"GCE2d_MakeParabola",
"GCE2d_MakeRotation",
"GCE2d_MakeScale",
"GCE2d_MakeSegment",
"GCE2d_MakeTranslation",
"GCE2d_MakeArcOfCircle"
]
class GCE2d_Root():
    """
    This class implements the common services for all classes of gce which report error.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def __init__(self) -> None: ...
    pass
class GCE2d_MakeArcOfEllipse(GCE2d_Root):
    """
    Implements construction algorithms for an arc of ellipse in the plane. The result is a Geom2d_TrimmedCurve curve. A MakeArcOfEllipse object provides a framework for: - defining the construction of the arc of ellipse, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed arc of ellipse.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_TrimmedCurve: 
        """
        Returns the constructed arc of ellipse.
        """
    @overload
    def __init__(self,Elips : OCP.gp.gp_Elips2d,P : OCP.gp.gp_Pnt2d,Alpha : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Elips : OCP.gp.gp_Elips2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Elips : OCP.gp.gp_Elips2d,Alpha1 : float,Alpha2 : float,Sense : bool=True) -> None: ...
    pass
class GCE2d_MakeArcOfHyperbola(GCE2d_Root):
    """
    Implements construction algorithms for an arc of hyperbola in the plane. The result is a Geom2d_TrimmedCurve curve. A MakeArcOfHyperbola object provides a framework for: - defining the construction of the arc of hyperbola, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed arc of hyperbola.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_TrimmedCurve: 
        """
        Returns the constructed arc of hyperbola.
        """
    @overload
    def __init__(self,Hypr : OCP.gp.gp_Hypr2d,Alpha1 : float,Alpha2 : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Hypr : OCP.gp.gp_Hypr2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Hypr : OCP.gp.gp_Hypr2d,P : OCP.gp.gp_Pnt2d,Alpha : float,Sense : bool=True) -> None: ...
    pass
class GCE2d_MakeArcOfParabola(GCE2d_Root):
    """
    Implements construction algorithms for an arc of parabola in the plane. The result is a Geom2d_TrimmedCurve curve. A MakeArcOfParabola object provides a framework for: - defining the construction of the arc of parabola, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed arc of parabola.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_TrimmedCurve: 
        """
        Returns the constructed arc of parabola.
        """
    @overload
    def __init__(self,Parab : OCP.gp.gp_Parab2d,Alpha1 : float,Alpha2 : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Parab : OCP.gp.gp_Parab2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Parab : OCP.gp.gp_Parab2d,P : OCP.gp.gp_Pnt2d,Alpha : float,Sense : bool=True) -> None: ...
    pass
class GCE2d_MakeCircle(GCE2d_Root):
    """
    This class implements the following algorithms used to create Circle from Geom2d.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_Circle: 
        """
        Returns the constructed circle. Exceptions StdFail_NotDone if no circle is constructed.
        """
    @overload
    def __init__(self,A : OCP.gp.gp_Ax22d,Radius : float) -> None: ...
    @overload
    def __init__(self,A : OCP.gp.gp_Ax2d,Radius : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ2d,Dist : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,P3 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,Radius : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ2d,Point : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt2d,Point : OCP.gp.gp_Pnt2d,Sense : bool=True) -> None: ...
    pass
class GCE2d_MakeEllipse(GCE2d_Root):
    """
    This class implements the following algorithms used to create Ellipse from Geom2d. * Create an Ellipse from two apex and the center. Defines an ellipse in 2D space. The parametrization range is [0,2*PI]. The ellipse is a closed and periodic curve. The center of the ellipse is the "Location" point of its axis placement "XAxis". The "XAxis" of the ellipse defines the origin of the parametrization, it is the major axis of the ellipse. The YAxis is the minor axis of the ellipse.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_Ellipse: 
        """
        Returns the constructed ellipse. Exceptions StdFail_NotDone if no ellipse is constructed.
        """
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d) -> None: ...
    @overload
    def __init__(self,MajorAxis : OCP.gp.gp_Ax2d,MajorRadius : float,MinorRadius : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt2d,S2 : OCP.gp.gp_Pnt2d,Center : OCP.gp.gp_Pnt2d) -> None: ...
    pass
class GCE2d_MakeHyperbola(GCE2d_Root):
    """
    This class implements the following algorithms used to create Hyperbola from Geom2d. * Create an Hyperbola from two apex and the center. Defines the main branch of an hyperbola. The parameterization range is ]-infinite,+infinite[ It is possible to get the other branch and the two conjugate branches of the main branch.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_Hyperbola: 
        """
        Returns the constructed hyperbola. Exceptions: StdFail_NotDone if no hyperbola is constructed.
        """
    @overload
    def __init__(self,MajorAxis : OCP.gp.gp_Ax2d,MajorRadius : float,MinorRadius : float,Sense : bool) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr2d) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt2d,S2 : OCP.gp.gp_Pnt2d,Center : OCP.gp.gp_Pnt2d) -> None: ...
    pass
class GCE2d_MakeLine(GCE2d_Root):
    """
    This class implements the following algorithms used to create a Line from Geom2d. * Create a Line parallel to another and passing through a point. * Create a Line passing through 2 points.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_Line: 
        """
        Returns the constructed line. Exceptions StdFail_NotDone if no line is constructed.
        """
    @overload
    def __init__(self,Lin : OCP.gp.gp_Lin2d,Dist : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Dir2d) -> None: ...
    @overload
    def __init__(self,A : OCP.gp.gp_Ax2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Lin : OCP.gp.gp_Lin2d,Point : OCP.gp.gp_Pnt2d) -> None: ...
    pass
class GCE2d_MakeMirror():
    """
    This class implements elementary construction algorithms for a symmetrical transformation in 2D space about a point or axis. The result is a Geom2d_Transformation transformation. A MakeMirror object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Value(self) -> OCP.Geom2d.Geom2d_Transformation: 
        """
        Returns the constructed transformation.
        """
    @overload
    def __init__(self,Point : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax2d) -> None: ...
    @overload
    def __init__(self,Point : OCP.gp.gp_Pnt2d,Direc : OCP.gp.gp_Dir2d) -> None: ...
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin2d) -> None: ...
    pass
class GCE2d_MakeParabola(GCE2d_Root):
    """
    This class implements the following algorithms used to create Parabola from Geom2d. * Create an Parabola from two apex and the center. Defines the parabola in the parameterization range : ]-infinite,+infinite[ The vertex of the parabola is the "Location" point of the local coordinate system "XAxis" of the parabola. The "XAxis" of the parabola is its axis of symmetry. The "Xaxis" is oriented from the vertex of the parabola to the Focus of the parabola. The equation of the parabola in the local coordinate system is Y**2 = (2*P) * X P is the distance between the focus and the directrix of the parabola called Parameter). The focal length F = P/2 is the distance between the vertex and the focus of the parabola.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_Parabola: 
        """
        Returns the constructed parabola. Exceptions StdFail_NotDone if no parabola is constructed.
        """
    @overload
    def __init__(self,D : OCP.gp.gp_Ax2d,F : OCP.gp.gp_Pnt2d,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax22d,Focal : float) -> None: ...
    @overload
    def __init__(self,Prb : OCP.gp.gp_Parab2d) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt2d,O : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,MirrorAxis : OCP.gp.gp_Ax2d,Focal : float,Sense : bool) -> None: ...
    pass
class GCE2d_MakeRotation():
    """
    This class implements an elementary construction algorithm for a rotation in 2D space. The result is a Geom2d_Transformation transformation. A MakeRotation object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Value(self) -> OCP.Geom2d.Geom2d_Transformation: 
        """
        Returns the constructed transformation.
        """
    def __init__(self,Point : OCP.gp.gp_Pnt2d,Angle : float) -> None: ...
    pass
class GCE2d_MakeScale():
    """
    This class implements an elementary construction algorithm for a scaling transformation in 2D space. The result is a Geom2d_Transformation transformation. A MakeScale object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Value(self) -> OCP.Geom2d.Geom2d_Transformation: 
        """
        Returns the constructed transformation.
        """
    def __init__(self,Point : OCP.gp.gp_Pnt2d,Scale : float) -> None: ...
    pass
class GCE2d_MakeSegment(GCE2d_Root):
    """
    Implements construction algorithms for a line segment in the plane. The result is a Geom2d_TrimmedCurve curve. A MakeSegment object provides a framework for: - defining the construction of the line segment, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed line segment.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_TrimmedCurve: 
        """
        Returns the constructed line segment. Exceptions StdFail_NotDone if no line segment is constructed.
        """
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin2d,U1 : float,U2 : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Dir2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin2d,Point : OCP.gp.gp_Pnt2d,Ulast : float) -> None: ...
    pass
class GCE2d_MakeTranslation():
    """
    This class implements elementary construction algorithms for a translation in 2D space. The result is a Geom2d_Transformation transformation. A MakeTranslation object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Value(self) -> OCP.Geom2d.Geom2d_Transformation: 
        """
        Returns the constructed transformation.
        """
    @overload
    def __init__(self,Point1 : OCP.gp.gp_Pnt2d,Point2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Vect : OCP.gp.gp_Vec2d) -> None: ...
    pass
class GCE2d_MakeArcOfCircle(GCE2d_Root):
    """
    Implements construction algorithms for an arc of circle in the plane. The result is a Geom2d_TrimmedCurve curve. A MakeArcOfCircle object provides a framework for: - defining the construction of the arc of circle, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed arc of circle.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom2d.Geom2d_TrimmedCurve: 
        """
        Returns the constructed arc of circle. Exceptions StdFail_NotDone if no arc of circle is constructed.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ2d,P : OCP.gp.gp_Pnt2d,Alpha : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,P3 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ2d,Alpha1 : float,Alpha2 : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,Sense : bool=True) -> None: ...
    pass
