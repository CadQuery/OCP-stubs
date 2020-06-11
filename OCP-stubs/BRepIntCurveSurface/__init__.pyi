import OCP.BRepIntCurveSurface
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64

_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.IntCurveSurface
import OCP.gp
import OCP.GeomAdaptor
import OCP.TopoDS

__all__ = ["BRepIntCurveSurface_Inter"]

class BRepIntCurveSurface_Inter:
    """
    Computes the intersection between a face and a curve. To intersect one curve with shape method Init(Shape, curve, tTol) should be used. To intersect a few curves with specified shape it is necessary to load shape one time using method Load(shape, tol) and find intersection points for each curve using method Init(curve). For iteration by intersection points method More() and Next() should be used.
    """

    def Face(self) -> OCP.TopoDS.TopoDS_Face:
        """
        returns the current face.
        """
    @overload
    def Init(
        self,
        theShape: OCP.TopoDS.TopoDS_Shape,
        theCurve: OCP.GeomAdaptor.GeomAdaptor_Curve,
        theTol: float,
    ) -> None:
        """
        Load the Shape, the curve and initialize the tolerance used for the classification.

        Load the Shape, the curve and initialize the tolerance used for the classification.

        Method to find intersections of specified curve with loaded shape.
        """
    @overload
    def Init(
        self, theShape: OCP.TopoDS.TopoDS_Shape, theLine: OCP.gp.gp_Lin, theTol: float
    ) -> None: ...
    @overload
    def Init(self, theCurve: OCP.GeomAdaptor.GeomAdaptor_Curve) -> None: ...
    def Load(self, theShape: OCP.TopoDS.TopoDS_Shape, theTol: float) -> None:
        """
        Load the Shape, and initialize the tolerance used for the classification.
        """
    def More(self) -> bool:
        """
        returns True if there is a current face.
        """
    def Next(self) -> None:
        """
        Sets the next intersection point to check.
        """
    def Pnt(self) -> OCP.gp.gp_Pnt:
        """
        returns the current geometric Point
        """
    def Point(self) -> OCP.IntCurveSurface.IntCurveSurface_IntersectionPoint:
        """
        returns the current Intersection point.
        """
    def State(self) -> OCP.TopAbs.TopAbs_State:
        """
        returns the current state (IN or ON)
        """
    def Transition(self) -> OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve:
        """
        returns the transition of the line on the surface (IN or OUT or UNKNOWN)
        """
    def U(self) -> float:
        """
        returns the U parameter of the current point on the current face.
        """
    def V(self) -> float:
        """
        returns the V parameter of the current point on the current face.
        """
    def W(self) -> float:
        """
        returns the parameter of the current point on the curve.
        """
    def __init__(self) -> None: ...
    pass
