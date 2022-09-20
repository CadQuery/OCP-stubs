import OCP.gce
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
__all__  = [
"gce_ErrorType",
"gce_Root",
"gce_MakeCirc2d",
"gce_MakeCone",
"gce_MakeCylinder",
"gce_MakeDir",
"gce_MakeDir2d",
"gce_MakeElips",
"gce_MakeElips2d",
"gce_MakeHypr",
"gce_MakeHypr2d",
"gce_MakeLin",
"gce_MakeLin2d",
"gce_MakeMirror",
"gce_MakeMirror2d",
"gce_MakeParab",
"gce_MakeParab2d",
"gce_MakePln",
"gce_MakeRotation",
"gce_MakeRotation2d",
"gce_MakeScale",
"gce_MakeScale2d",
"gce_MakeTranslation",
"gce_MakeTranslation2d",
"gce_MakeCirc",
"gce_BadAngle",
"gce_BadEquation",
"gce_ColinearPoints",
"gce_ConfusedPoints",
"gce_Done",
"gce_IntersectionError",
"gce_InvertAxis",
"gce_InvertRadius",
"gce_NegativeRadius",
"gce_NullAngle",
"gce_NullAxis",
"gce_NullFocusLength",
"gce_NullRadius",
"gce_NullVector"
]
class gce_ErrorType():
    """
    Indicates the outcome of a construction, i.e. whether it is successful or not, as explained below. gce_Done: Construction was successful. gce_ConfusedPoints: Two points are coincident. gce_NegativeRadius: Radius value is negative. gce_ColinearPoints: Three points are collinear. gce_IntersectionError: Intersection cannot be computed. gce_NullAxis: Axis is undefined. gce_NullAngle: Angle value is invalid (usually null). gce_NullRadius: Radius is null. gce_InvertAxis: Axis value is invalid. gce_BadAngle: Angle value is invalid. gce_InvertRadius: Radius value is incorrect (usually with respect to another radius). gce_NullFocusLength: Focal distance is null. gce_NullVector: Vector is null. gce_BadEquation: Coefficients are incorrect (applies to the equation of a geometric object).

    Members:

      gce_Done

      gce_ConfusedPoints

      gce_NegativeRadius

      gce_ColinearPoints

      gce_IntersectionError

      gce_NullAxis

      gce_NullAngle

      gce_NullRadius

      gce_InvertAxis

      gce_BadAngle

      gce_InvertRadius

      gce_NullFocusLength

      gce_NullVector

      gce_BadEquation
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
    __entries: dict # value = {'gce_Done': (<gce_ErrorType.gce_Done: 0>, None), 'gce_ConfusedPoints': (<gce_ErrorType.gce_ConfusedPoints: 1>, None), 'gce_NegativeRadius': (<gce_ErrorType.gce_NegativeRadius: 2>, None), 'gce_ColinearPoints': (<gce_ErrorType.gce_ColinearPoints: 3>, None), 'gce_IntersectionError': (<gce_ErrorType.gce_IntersectionError: 4>, None), 'gce_NullAxis': (<gce_ErrorType.gce_NullAxis: 5>, None), 'gce_NullAngle': (<gce_ErrorType.gce_NullAngle: 6>, None), 'gce_NullRadius': (<gce_ErrorType.gce_NullRadius: 7>, None), 'gce_InvertAxis': (<gce_ErrorType.gce_InvertAxis: 8>, None), 'gce_BadAngle': (<gce_ErrorType.gce_BadAngle: 9>, None), 'gce_InvertRadius': (<gce_ErrorType.gce_InvertRadius: 10>, None), 'gce_NullFocusLength': (<gce_ErrorType.gce_NullFocusLength: 11>, None), 'gce_NullVector': (<gce_ErrorType.gce_NullVector: 12>, None), 'gce_BadEquation': (<gce_ErrorType.gce_BadEquation: 13>, None)}
    __members__: dict # value = {'gce_Done': <gce_ErrorType.gce_Done: 0>, 'gce_ConfusedPoints': <gce_ErrorType.gce_ConfusedPoints: 1>, 'gce_NegativeRadius': <gce_ErrorType.gce_NegativeRadius: 2>, 'gce_ColinearPoints': <gce_ErrorType.gce_ColinearPoints: 3>, 'gce_IntersectionError': <gce_ErrorType.gce_IntersectionError: 4>, 'gce_NullAxis': <gce_ErrorType.gce_NullAxis: 5>, 'gce_NullAngle': <gce_ErrorType.gce_NullAngle: 6>, 'gce_NullRadius': <gce_ErrorType.gce_NullRadius: 7>, 'gce_InvertAxis': <gce_ErrorType.gce_InvertAxis: 8>, 'gce_BadAngle': <gce_ErrorType.gce_BadAngle: 9>, 'gce_InvertRadius': <gce_ErrorType.gce_InvertRadius: 10>, 'gce_NullFocusLength': <gce_ErrorType.gce_NullFocusLength: 11>, 'gce_NullVector': <gce_ErrorType.gce_NullVector: 12>, 'gce_BadEquation': <gce_ErrorType.gce_BadEquation: 13>}
    gce_BadAngle: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_BadAngle: 9>
    gce_BadEquation: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_BadEquation: 13>
    gce_ColinearPoints: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_ColinearPoints: 3>
    gce_ConfusedPoints: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_ConfusedPoints: 1>
    gce_Done: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_Done: 0>
    gce_IntersectionError: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_IntersectionError: 4>
    gce_InvertAxis: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_InvertAxis: 8>
    gce_InvertRadius: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_InvertRadius: 10>
    gce_NegativeRadius: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NegativeRadius: 2>
    gce_NullAngle: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullAngle: 6>
    gce_NullAxis: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullAxis: 5>
    gce_NullFocusLength: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullFocusLength: 11>
    gce_NullRadius: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullRadius: 7>
    gce_NullVector: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullVector: 12>
    pass
class gce_Root():
    """
    This class implements the common services for all classes of gce which report error.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def __init__(self) -> None: ...
    pass
class gce_MakeCirc2d(gce_Root):
    """
    This class implements the following algorithms used to create Circ2d from gp.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Circ2d: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns the constructed circle. Exceptions StdFail_NotDone if no circle is constructed.
        """
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt2d,Point : OCP.gp.gp_Pnt2d,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ2d,Point : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax22d,Radius : float) -> None: ...
    @overload
    def __init__(self,XAxis : OCP.gp.gp_Ax2d,Radius : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt2d,Radius : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,P3 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ2d,Dist : float) -> None: ...
    pass
class gce_MakeCone(gce_Root):
    """
    This class implements the following algorithms used to create a Cone from gp. * Create a Cone coaxial to another and passing through a point. * Create a Cone coaxial to another at a distance <Dist>. * Create a Cone by 4 points. * Create a Cone by its axis and 2 points. * Create a Cone by 2 points and 2 radius. * Create a Cone by an Ax2 an angle and the radius of its reference section.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Cone: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Cone: 
        """
        Returns the constructed cone. Exceptions StdFail_NotDone if no cone is constructed.
        """
    @overload
    def __init__(self,Cone : OCP.gp.gp_Cone,Point : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt,P4 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Cone : OCP.gp.gp_Cone,Dist : float) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,Ang : float,Radius : float) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Lin,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,R1 : float,R2 : float) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    pass
class gce_MakeCylinder(gce_Root):
    """
    This class implements the following algorithms used to create a Cylinder from gp. * Create a Cylinder coaxial to another and passing through a point. * Create a Cylinder coaxial to another at a distance <Dist>. * Create a Cylinder with 3 points. * Create a Cylinder by its axis and radius. * Create a cylinder by its circular base.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Cylinder: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Cylinder: 
        """
        Returns the constructed cylinder. Exceptions StdFail_NotDone if no cylinder is constructed.
        """
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,Point : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1,Radius : float) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,Dist : float) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,Radius : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt) -> None: ...
    pass
class gce_MakeDir(gce_Root):
    """
    This class implements the following algorithms used to create a Dir from gp. * Create a Dir parallel to another and passing through a point. * Create a Dir passing through 2 points. * Create a Dir from its axis (Ax1 from gp). * Create a Dir from a point and a direction.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Dir: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Dir: 
        """
        Returns the constructed unit vector. Exceptions StdFail_NotDone if no unit vector is constructed.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def __init__(self,Coord : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self,Xv : float,Yv : float,Zv : float) -> None: ...
    pass
class gce_MakeDir2d(gce_Root):
    """
    This class implements the following algorithms used to create a Dir2d from gp. * Create a Dir2d with 2 points. * Create a Dir2d with a Vec2d. * Create a Dir2d with a XY from gp. * Create a Dir2d with a 2 Reals (Coordinates).
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Dir2d: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Dir2d: 
        """
        Returns the constructed unit vector. Exceptions StdFail_NotDone if no unit vector is constructed.
        """
    @overload
    def __init__(self,V : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def __init__(self,Xv : float,Yv : float) -> None: ...
    @overload
    def __init__(self,Coord : OCP.gp.gp_XY) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    pass
class gce_MakeElips(gce_Root):
    """
    This class implements the following algorithms used to create an ellipse from gp.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Elips: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Elips: 
        """
        Returns the constructed ellipse. Exceptions StdFail_NotDone if no ellipse is constructed.
        """
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt,S2 : OCP.gp.gp_Pnt,Center : OCP.gp.gp_Pnt) -> None: ...
    pass
class gce_MakeElips2d(gce_Root):
    """
    This class implements the following algorithms used to create Elips2d from gp.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Elips2d: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Elips2d: 
        """
        Returns the constructed ellipse. Exceptions StdFail_NotDone if no ellipse is constructed.
        """
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt2d,S2 : OCP.gp.gp_Pnt2d,Center : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,MajorAxis : OCP.gp.gp_Ax2d,MajorRadius : float,MinorRadius : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,A : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float) -> None: ...
    pass
class gce_MakeHypr(gce_Root):
    """
    This class implements the following algorithms used to create Hyperbola from gp. * Create an Hyperbola from its center, and two points: one on its axis of symmetry giving the major radius, the other giving the value of the small radius. The three points give the plane of the hyperbola. * Create an hyperbola from its axisplacement and its MajorRadius and its MinorRadius.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Hypr: 
        """
        Returns the constructed hyperbola. Exceptions StdFail_NotDone if no hyperbola is constructed.
        """
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt,S2 : OCP.gp.gp_Pnt,Center : OCP.gp.gp_Pnt) -> None: ...
    pass
class gce_MakeHypr2d(gce_Root):
    """
    This class implements the following algorithms used to create a 2d Hyperbola from gp. * Create a 2d Hyperbola from its center and two points: one on its axis of symmetry giving the major radius, the other giving the value of the small radius. * Create a 2d Hyperbola from its major axis and its major radius and its minor radius.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Hypr2d: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Hypr2d: 
        """
        Returns the constructed hyperbola. Exceptions StdFail_NotDone if no hyperbola is constructed.
        """
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt2d,S2 : OCP.gp.gp_Pnt2d,Center : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,MajorAxis : OCP.gp.gp_Ax2d,MajorRadius : float,MinorRadius : float,Sense : bool) -> None: ...
    @overload
    def __init__(self,A : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float) -> None: ...
    pass
class gce_MakeLin(gce_Root):
    """
    This class implements the following algorithms used to create a Lin from gp. * Create a Lin parallel to another and passing through a point. * Create a Lin passing through 2 points. * Create a lin from its axis (Ax1 from gp). * Create a lin from a point and a direction.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Lin: 
        """
        Returns the constructed line. Exceptions StdFail_NotDone is raised if no line is constructed.
        """
    @overload
    def __init__(self,A1 : OCP.gp.gp_Ax1) -> None: ...
    @overload
    def __init__(self,Lin : OCP.gp.gp_Lin,Point : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    pass
class gce_MakeLin2d(gce_Root):
    """
    This class implements the following algorithms used to create Lin2d from gp.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns the constructed line. Exceptions StdFail_NotDone if no line is constructed.
        """
    @overload
    def __init__(self,Lin : OCP.gp.gp_Lin2d,Dist : float) -> None: ...
    @overload
    def __init__(self,Lin : OCP.gp.gp_Lin2d,Point : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,A : OCP.gp.gp_Ax2d) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Dir2d) -> None: ...
    @overload
    def __init__(self,A : float,B : float,C : float) -> None: ...
    pass
class gce_MakeMirror():
    """
    This class mplements elementary construction algorithms for a symmetrical transformation in 3D space about a point, axis or plane. The result is a gp_Trsf transformation. A MakeMirror object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Operator(self) -> OCP.gp.gp_Trsf: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the constructed transformation.
        """
    @overload
    def __init__(self,Plane : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,Point : OCP.gp.gp_Pnt,Direc : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,Point : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Line : OCP.gp.gp_Lin) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1) -> None: ...
    @overload
    def __init__(self,Plane : OCP.gp.gp_Ax2) -> None: ...
    pass
class gce_MakeMirror2d():
    """
    This class implements elementary construction algorithms for a symmetrical transformation in 2D space about a point or axis. The result is a gp_Trsf2d transformation. A MakeMirror2d object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and consulting the result.
    """
    def Operator(self) -> OCP.gp.gp_Trsf2d: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Trsf2d: 
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
class gce_MakeParab(gce_Root):
    """
    This class implements the following algorithms used to create Parab from gp. Defines the parabola in the parameterization range : ]-infinite, +infinite[ The vertex of the parabola is the "Location" point of the local coordinate system (axis placement) of the parabola.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Parab: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Parab: 
        """
        Returns the constructed parabola. Exceptions StdFail_NotDone if no parabola is constructed.
        """
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,Focal : float) -> None: ...
    @overload
    def __init__(self,D : OCP.gp.gp_Ax1,F : OCP.gp.gp_Pnt) -> None: ...
    pass
class gce_MakeParab2d(gce_Root):
    """
    This class implements the following algorithms used to create Parab2d from gp. Defines an infinite parabola. An axis placement one axis defines the local cartesian coordinate system ("XAxis") of the parabola. The vertex of the parabola is the "Location" point of the local coordinate system of the parabola. The "XAxis" of the parabola is its axis of symmetry. The "XAxis" is oriented from the vertex of the parabola to the Focus of the parabola. The "YAxis" is parallel to the directrix of the parabola and its "Location" point is the vertex of the parabola. The equation of the parabola in the local coordinate system is Y**2 = (2*P) * X P is the distance between the focus and the directrix of the parabola called Parameter). The focal length F = P/2 is the distance between the vertex and the focus of the parabola.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Parab2d: 
        """
        Returns the constructed parabola. Exceptions StdFail_NotDone if no parabola is constructed.
        """
    @overload
    def __init__(self,D : OCP.gp.gp_Ax2d,F : OCP.gp.gp_Pnt2d,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,A : OCP.gp.gp_Ax22d,Focal : float) -> None: ...
    @overload
    def __init__(self,MirrorAxis : OCP.gp.gp_Ax2d,Focal : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pnt2d,Center : OCP.gp.gp_Pnt2d,Sense : bool=True) -> None: ...
    pass
class gce_MakePln(gce_Root):
    """
    This class implements the following algorithms used to create a Plane from gp. * Create a Pln parallel to another and passing through a point. * Create a Pln passing through 3 points. * Create a Pln by its normal. Defines a non-persistent plane. The plane is located in 3D space with an axis placement two axis. It is the local coordinate system of the plane.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Pln: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Pln: 
        """
        Returns the constructed plane. Exceptions StdFail_NotDone if no plane is constructed.
        """
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1) -> None: ...
    @overload
    def __init__(self,A : float,B : float,C : float,D : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,Pln : OCP.gp.gp_Pln,Dist : float) -> None: ...
    @overload
    def __init__(self,Pln : OCP.gp.gp_Pln,Point : OCP.gp.gp_Pnt) -> None: ...
    pass
class gce_MakeRotation():
    """
    This class implements elementary construction algorithms for a rotation in 3D space. The result is a gp_Trsf transformation. A MakeRotation object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Operator(self) -> OCP.gp.gp_Trsf: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Trsf: 
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
class gce_MakeRotation2d():
    """
    Implements an elementary construction algorithm for a rotation in 2D space. The result is a gp_Trsf2d transformation. A MakeRotation2d object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Operator(self) -> OCP.gp.gp_Trsf2d: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Trsf2d: 
        """
        Returns the constructed transformation.
        """
    def __init__(self,Point : OCP.gp.gp_Pnt2d,Angle : float) -> None: ...
    pass
class gce_MakeScale():
    """
    Implements an elementary construction algorithm for a scaling transformation in 3D space. The result is a gp_Trsf transformation. A MakeScale object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Operator(self) -> OCP.gp.gp_Trsf: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the constructed transformation.
        """
    def __init__(self,Point : OCP.gp.gp_Pnt,Scale : float) -> None: ...
    pass
class gce_MakeScale2d():
    """
    This class implements an elementary construction algorithm for a scaling transformation in 2D space. The result is a gp_Trsf2d transformation. A MakeScale2d object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Operator(self) -> OCP.gp.gp_Trsf2d: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Trsf2d: 
        """
        Returns the constructed transformation.
        """
    def __init__(self,Point : OCP.gp.gp_Pnt2d,Scale : float) -> None: ...
    pass
class gce_MakeTranslation():
    """
    This class implements elementary construction algorithms for a translation in 3D space. The result is a gp_Trsf transformation. A MakeTranslation object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Operator(self) -> OCP.gp.gp_Trsf: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the constructed transformation.
        """
    @overload
    def __init__(self,Point1 : OCP.gp.gp_Pnt,Point2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Vect : OCP.gp.gp_Vec) -> None: ...
    pass
class gce_MakeTranslation2d():
    """
    This class implements elementary construction algorithms for a translation in 2D space. The result is a gp_Trsf2d transformation. A MakeTranslation2d object provides a framework for: - defining the construction of the transformation, - implementing the construction algorithm, and - consulting the result.
    """
    def Operator(self) -> OCP.gp.gp_Trsf2d: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Trsf2d: 
        """
        Returns the constructed transformation.
        """
    @overload
    def __init__(self,Vect : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def __init__(self,Point1 : OCP.gp.gp_Pnt2d,Point2 : OCP.gp.gp_Pnt2d) -> None: ...
    pass
class gce_MakeCirc(gce_Root):
    """
    This class implements the following algorithms used to create Circ from gp.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction is successful.

        Returns true if the construction is successful.
        """
    def Operator(self) -> OCP.gp.gp_Circ: 
        """
        None
        """
    def Status(self) -> gce_ErrorType: 
        """
        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.

        Returns the status of the construction: - gce_Done, if the construction is successful, or - another value of the gce_ErrorType enumeration indicating why the construction failed.
        """
    def Value(self) -> OCP.gp.gp_Circ: 
        """
        Returns the constructed circle. Exceptions StdFail_NotDone if no circle is constructed.
        """
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,Radius : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,Norm : OCP.gp.gp_Dir,Radius : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,Plane : OCP.gp.gp_Pln,Radius : float) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ,Dist : float) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax1,Radius : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,Ptaxis : OCP.gp.gp_Pnt,Radius : float) -> None: ...
    @overload
    def __init__(self,Circ : OCP.gp.gp_Circ,Point : OCP.gp.gp_Pnt) -> None: ...
    pass
gce_BadAngle: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_BadAngle: 9>
gce_BadEquation: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_BadEquation: 13>
gce_ColinearPoints: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_ColinearPoints: 3>
gce_ConfusedPoints: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_ConfusedPoints: 1>
gce_Done: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_Done: 0>
gce_IntersectionError: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_IntersectionError: 4>
gce_InvertAxis: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_InvertAxis: 8>
gce_InvertRadius: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_InvertRadius: 10>
gce_NegativeRadius: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NegativeRadius: 2>
gce_NullAngle: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullAngle: 6>
gce_NullAxis: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullAxis: 5>
gce_NullFocusLength: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullFocusLength: 11>
gce_NullRadius: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullRadius: 7>
gce_NullVector: OCP.gce.gce_ErrorType # value = <gce_ErrorType.gce_NullVector: 12>
