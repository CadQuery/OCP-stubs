import OCP.GC
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gce
import OCP.Geom
import OCP.gp
__all__  = [
"GC_Root",
"GC_MakeArcOfEllipse",
"GC_MakeArcOfHyperbola",
"GC_MakeArcOfParabola",
"GC_MakeCircle",
"GC_MakeConicalSurface",
"GC_MakeCylindricalSurface",
"GC_MakeEllipse",
"GC_MakeHyperbola",
"GC_MakeLine",
"GC_MakeMirror",
"GC_MakePlane",
"GC_MakeRotation",
"GC_MakeScale",
"GC_MakeSegment",
"GC_MakeTranslation",
"GC_MakeTrimmedCone",
"GC_MakeTrimmedCylinder",
"GC_MakeArcOfCircle"
]
class GC_Root():
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
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def __init__(self) -> None: ...
    pass
class GC_MakeArcOfEllipse(GC_Root):
    """
    Implements construction algorithms for an arc of ellipse in 3D space. The result is a Geom_TrimmedCurve curve. A MakeArcOfEllipse object provides a framework for: - defining the construction of the arc of ellipse, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed arc of ellipse.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_TrimmedCurve: 
        """
        Returns the constructed arc of ellipse.
        """
    @overload
    def __init__(self,Elips : OCP.gp.gp_Elips,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,Sense : bool) -> None: ...
    @overload
    def __init__(self,Elips : OCP.gp.gp_Elips,P : OCP.gp.gp_Pnt,Alpha : float,Sense : bool) -> None: ...
    @overload
    def __init__(self,Elips : OCP.gp.gp_Elips,Alpha1 : float,Alpha2 : float,Sense : bool) -> None: ...
    pass
class GC_MakeArcOfHyperbola(GC_Root):
    """
    Implements construction algorithms for an arc of hyperbola in 3D space. The result is a Geom_TrimmedCurve curve. A MakeArcOfHyperbola object provides a framework for: - defining the construction of the arc of hyperbola, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed arc of hyperbola.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_TrimmedCurve: 
        """
        Returns the constructed arc of hyperbola.
        """
    @overload
    def __init__(self,Hypr : OCP.gp.gp_Hypr,Alpha1 : float,Alpha2 : float,Sense : bool) -> None: ...
    @overload
    def __init__(self,Hypr : OCP.gp.gp_Hypr,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,Sense : bool) -> None: ...
    @overload
    def __init__(self,Hypr : OCP.gp.gp_Hypr,P : OCP.gp.gp_Pnt,Alpha : float,Sense : bool) -> None: ...
    pass
class GC_MakeArcOfParabola(GC_Root):
    """
    Implements construction algorithms for an arc of parabola in 3D space. The result is a Geom_TrimmedCurve curve. A MakeArcOfParabola object provides a framework for: - defining the construction of the arc of parabola, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed arc of parabola.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_TrimmedCurve: 
        """
        Returns the constructed arc of parabola.
        """
    @overload
    def __init__(self,Parab : OCP.gp.gp_Parab,Alpha1 : float,Alpha2 : float,Sense : bool) -> None: ...
    @overload
    def __init__(self,Parab : OCP.gp.gp_Parab,P : OCP.gp.gp_Pnt,Alpha : float,Sense : bool) -> None: ...
    @overload
    def __init__(self,Parab : OCP.gp.gp_Parab,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,Sense : bool) -> None: ...
    pass
class GC_MakeCircle(GC_Root):
    """
    This class implements the following algorithms used to create Cirlec from Geom.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_Circle: 
        """
        Returns the constructed circle. Exceptions StdFail_NotDone if no circle is constructed.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,Norm : OCP.gp.gp_Dir,Radius : float) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ,Point : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1,Radius : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,PtAxis : OCP.gp.gp_Pnt,Radius : float) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,Radius : float) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ,Dist : float) -> None: ...
    pass
class GC_MakeConicalSurface(GC_Root):
    """
    This class implements the following algorithms used to create a ConicalSurface from Geom. * Create a ConicalSurface parallel to another and passing through a point. * Create a ConicalSurface parallel to another at a distance <Dist>. * Create a ConicalSurface by 4 points. * Create a ConicalSurface by its axis and 2 points. * Create a ConicalSurface by 2 points and 2 radius. The local coordinate system of the ConicalSurface is defined with an axis placement (see class ElementarySurface).
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_ConicalSurface: 
        """
        Returns the constructed cone. Exceptions StdFail_NotDone if no cone is constructed.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,R1 : float,R2 : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cone) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,Ang : float,Radius : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt,P4 : OCP.gp.gp_Pnt) -> None: ...
    pass
class GC_MakeCylindricalSurface(GC_Root):
    """
    This class implements the following algorithms used to create a CylindricalSurface from Geom. * Create a CylindricalSurface parallel to another and passing through a point. * Create a CylindricalSurface parallel to another at a distance <Dist>. * Create a CylindricalSurface passing through 3 points. * Create a CylindricalSurface by its axis and radius. * Create a cylindricalSurface by its circular base. The local coordinate system of the CylindricalSurface is defined with an axis placement (see class ElementarySurface).
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_CylindricalSurface: 
        """
        Returns the constructed cylinder. Exceptions StdFail_NotDone if no cylinder is constructed.
        """
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1,Radius : float) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,Radius : float) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,Point : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,Dist : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt) -> None: ...
    pass
class GC_MakeEllipse(GC_Root):
    """
    This class implements construction algorithms for an ellipse in 3D space. The result is a Geom_Ellipse ellipse. A MakeEllipse object provides a framework for: - defining the construction of the ellipse, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed ellipse.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_Ellipse: 
        """
        Returns the constructed ellipse. Exceptions StdFail_NotDone if no ellipse is constructed.
        """
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt,S2 : OCP.gp.gp_Pnt,Center : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips) -> None: ...
    pass
class GC_MakeHyperbola(GC_Root):
    """
    This class implements construction algorithms for a hyperbola in 3D space. The result is a Geom_Hyperbola hyperbola. A MakeHyperbola object provides a framework for: - defining the construction of the hyperbola, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed hyperbola. To define the main branch of an hyperbola. The parameterization range is ]-infinite,+infinite[ It is possible to get the other branch and the two conjugate branches of the main branch.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_Hyperbola: 
        """
        Returns the constructed hyperbola. Exceptions StdFail_NotDone if no hyperbola is constructed.
        """
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt,S2 : OCP.gp.gp_Pnt,Center : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr) -> None: ...
    pass
class GC_MakeLine(GC_Root):
    """
    This class implements the following algorithms used to create a Line from Geom. * Create a Line parallel to another and passing through a point. * Create a Line passing through 2 points. A MakeLine object provides a framework for: - defining the construction of the line, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed line.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_Line: 
        """
        Returns the constructed line. Exceptions StdFail_NotDone if no line is constructed.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def __init__(self,A1 : OCP.gp.gp_Ax1) -> None: ...
    @overload
    def __init__(self,Lin : OCP.gp.gp_Lin,Point : OCP.gp.gp_Pnt) -> None: ...
    pass
class GC_MakeMirror():
    """
    This class implements elementary construction algorithms for a symmetrical transformation in 3D space about a point, axis or plane. The result is a Geom_Transformation transformation. A MakeMirror object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Value(self) -> OCP.Geom.Geom_Transformation: 
        """
        Returns the constructed transformation.
        """
    @overload
    def __init__(self,Point : OCP.gp.gp_Pnt,Direc : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin) -> None: ...
    @overload
    def __init__(self,Point : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Plane : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def __init__(self,Plane : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1) -> None: ...
    pass
class GC_MakePlane(GC_Root):
    """
    This class implements the following algorithms used to create a Plane from gp. * Create a Plane parallel to another and passing through a point. * Create a Plane passing through 3 points. * Create a Plane by its normal A MakePlane object provides a framework for: - defining the construction of the plane, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed plane.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_Plane: 
        """
        Returns the constructed plane. Exceptions StdFail_NotDone if no plane is constructed.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Pl : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,Pln : OCP.gp.gp_Pln,Point : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,Pln : OCP.gp.gp_Pln,Dist : float) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1) -> None: ...
    @overload
    def __init__(self,A : float,B : float,C : float,D : float) -> None: ...
    pass
class GC_MakeRotation():
    """
    This class implements elementary construction algorithms for a rotation in 3D space. The result is a Geom_Transformation transformation. A MakeRotation object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Value(self) -> OCP.Geom.Geom_Transformation: 
        """
        Returns the constructed transformation.
        """
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin,Angle : float) -> None: ...
    @overload
    def __init__(self,Point : OCP.gp.gp_Pnt,Direc : OCP.gp.gp_Dir,Angle : float) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1,Angle : float) -> None: ...
    pass
class GC_MakeScale():
    """
    This class implements an elementary construction algorithm for a scaling transformation in 3D space. The result is a Geom_Transformation transformation (a scaling transformation with the center point <Point> and the scaling value <Scale>). A MakeScale object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Value(self) -> OCP.Geom.Geom_Transformation: 
        """
        Returns the constructed transformation.
        """
    def __init__(self,Point : OCP.gp.gp_Pnt,Scale : float) -> None: ...
    pass
class GC_MakeSegment(GC_Root):
    """
    Implements construction algorithms for a line segment in 3D space. Makes a segment of Line from the 2 points <P1> and <P2>. The result is a Geom_TrimmedCurve curve. A MakeSegment object provides a framework for: - defining the construction of the line segment, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed line segment.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_TrimmedCurve: 
        """
        Returns the constructed line segment.
        """
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin,U1 : float,U2 : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin,Point : OCP.gp.gp_Pnt,Ulast : float) -> None: ...
    pass
class GC_MakeTranslation():
    """
    This class implements elementary construction algorithms for a translation in 3D space. The result is a Geom_Transformation transformation. A MakeTranslation object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Value(self) -> OCP.Geom.Geom_Transformation: 
        """
        Returns the constructed transformation.
        """
    @overload
    def __init__(self,Point1 : OCP.gp.gp_Pnt,Point2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Vect : OCP.gp.gp_Vec) -> None: ...
    pass
class GC_MakeTrimmedCone(GC_Root):
    """
    Implements construction algorithms for a trimmed cone limited by two planes orthogonal to its axis. The result is a Geom_RectangularTrimmedSurface surface. A MakeTrimmedCone provides a framework for: - defining the construction of the trimmed cone, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed trimmed cone.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_RectangularTrimmedSurface: 
        """
        Returns the constructed trimmed cone. StdFail_NotDone if no trimmed cone is constructed.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,R1 : float,R2 : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt,P4 : OCP.gp.gp_Pnt) -> None: ...
    pass
class GC_MakeTrimmedCylinder(GC_Root):
    """
    Implements construction algorithms for a trimmed cylinder limited by two planes orthogonal to its axis. The result is a Geom_RectangularTrimmedSurface surface. A MakeTrimmedCylinder provides a framework for: - defining the construction of the trimmed cylinder, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed trimmed cylinder.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_RectangularTrimmedSurface: 
        """
        Returns the constructed trimmed cylinder. Exceptions StdFail_NotDone if no trimmed cylinder is constructed.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,A1 : OCP.gp.gp_Ax1,Radius : float,Height : float) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ,Height : float) -> None: ...
    pass
class GC_MakeArcOfCircle(GC_Root):
    """
    Implements construction algorithms for an arc of circle in 3D space. The result is a Geom_TrimmedCurve curve. A MakeArcOfCircle object provides a framework for: - defining the construction of the arc of circle, - implementing the construction algorithm, and - consulting the results. In particular, the Value function returns the constructed arc of circle.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> OCP.gce.gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.Geom.Geom_TrimmedCurve: 
        """
        Returns the constructed arc of circle. Exceptions StdFail_NotDone if no arc of circle is constructed.
        """
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,Sense : bool) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ,Alpha1 : float,Alpha2 : float,Sense : bool) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ,P : OCP.gp.gp_Pnt,Alpha : float,Sense : bool) -> None: ...
    pass
