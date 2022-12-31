import OCP.GeomToStep
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.gp
import OCP.Geom2d
import OCP.TColgp
import OCP.StepGeom
__all__  = [
"GeomToStep_Root",
"GeomToStep_MakeAxis2Placement2d",
"GeomToStep_MakeAxis2Placement3d",
"GeomToStep_MakeBSplineCurveWithKnots",
"GeomToStep_MakeBSplineCurveWithKnotsAndRationalBSplineCurve",
"GeomToStep_MakeBSplineSurfaceWithKnots",
"GeomToStep_MakeBSplineSurfaceWithKnotsAndRationalBSplineSurface",
"GeomToStep_MakeBoundedCurve",
"GeomToStep_MakeBoundedSurface",
"GeomToStep_MakeCartesianPoint",
"GeomToStep_MakeCircle",
"GeomToStep_MakeConic",
"GeomToStep_MakeConicalSurface",
"GeomToStep_MakeCurve",
"GeomToStep_MakeCylindricalSurface",
"GeomToStep_MakeDirection",
"GeomToStep_MakeElementarySurface",
"GeomToStep_MakeEllipse",
"GeomToStep_MakeHyperbola",
"GeomToStep_MakeLine",
"GeomToStep_MakeParabola",
"GeomToStep_MakePlane",
"GeomToStep_MakePolyline",
"GeomToStep_MakeRectangularTrimmedSurface",
"GeomToStep_MakeSphericalSurface",
"GeomToStep_MakeSurface",
"GeomToStep_MakeSurfaceOfLinearExtrusion",
"GeomToStep_MakeSurfaceOfRevolution",
"GeomToStep_MakeSweptSurface",
"GeomToStep_MakeToroidalSurface",
"GeomToStep_MakeVector",
"GeomToStep_MakeAxis1Placement"
]
class GeomToStep_Root():
    """
    This class implements the common services for all classes of GeomToStep which report error.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class GeomToStep_MakeAxis2Placement2d(GeomToStep_Root):
    """
    This class implements the mapping between classes Axis2Placement from Geom and Ax2, Ax22d from gp, and the class Axis2Placement2d from StepGeom which describes an axis2_placement_2d from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Axis2Placement2d: 
        """
        None
        """
    @overload
    def __init__(self,A : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def __init__(self,A : OCP.gp.gp_Ax22d) -> None: ...
    pass
class GeomToStep_MakeAxis2Placement3d(GeomToStep_Root):
    """
    This class implements the mapping between classes Axis2Placement from Geom and Ax2, Ax3 from gp, and the class Axis2Placement3d from StepGeom which describes an axis2_placement_3d from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Axis2Placement3d: 
        """
        None
        """
    @overload
    def __init__(self,A : OCP.gp.gp_Ax3) -> None: ...
    @overload
    def __init__(self,A : OCP.Geom.Geom_Axis2Placement) -> None: ...
    @overload
    def __init__(self,A : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def __init__(self,T : OCP.gp.gp_Trsf) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomToStep_MakeBSplineCurveWithKnots(GeomToStep_Root):
    """
    This class implements the mapping between classes BSplineCurve from Geom, Geom2d and the class BSplineCurveWithKnots from StepGeom which describes a bspline_curve_with_knots from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_BSplineCurveWithKnots: 
        """
        None
        """
    @overload
    def __init__(self,Bsplin : OCP.Geom.Geom_BSplineCurve) -> None: ...
    @overload
    def __init__(self,Bsplin : OCP.Geom2d.Geom2d_BSplineCurve) -> None: ...
    pass
class GeomToStep_MakeBSplineCurveWithKnotsAndRationalBSplineCurve(GeomToStep_Root):
    """
    This class implements the mapping between classes BSplineCurve from Geom, Geom2d and the class BSplineCurveWithKnotsAndRationalBSplineCurve from StepGeom which describes a rational_bspline_curve_with_knots from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve: 
        """
        None
        """
    @overload
    def __init__(self,Bsplin : OCP.Geom.Geom_BSplineCurve) -> None: ...
    @overload
    def __init__(self,Bsplin : OCP.Geom2d.Geom2d_BSplineCurve) -> None: ...
    pass
class GeomToStep_MakeBSplineSurfaceWithKnots(GeomToStep_Root):
    """
    This class implements the mapping between class BSplineSurface from Geom and the class BSplineSurfaceWithKnots from StepGeom which describes a bspline_Surface_with_knots from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_BSplineSurfaceWithKnots: 
        """
        None
        """
    def __init__(self,Bsplin : OCP.Geom.Geom_BSplineSurface) -> None: ...
    pass
class GeomToStep_MakeBSplineSurfaceWithKnotsAndRationalBSplineSurface(GeomToStep_Root):
    """
    This class implements the mapping between class BSplineSurface from Geom and the class BSplineSurfaceWithKnotsAndRationalBSplineSurface from StepGeom which describes a rational_bspline_Surface_with_knots from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface: 
        """
        None
        """
    def __init__(self,Bsplin : OCP.Geom.Geom_BSplineSurface) -> None: ...
    pass
class GeomToStep_MakeBoundedCurve(GeomToStep_Root):
    """
    This class implements the mapping between classes BoundedCurve from Geom, Geom2d and the class BoundedCurve from StepGeom which describes a BoundedCurve from prostep. As BoundedCurve is an abstract BoundedCurve this class is an access to the sub-class required.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_BoundedCurve: 
        """
        None
        """
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_BoundedCurve) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom.Geom_BoundedCurve) -> None: ...
    pass
class GeomToStep_MakeBoundedSurface(GeomToStep_Root):
    """
    This class implements the mapping between classes BoundedSurface from Geom and the class BoundedSurface from StepGeom which describes a BoundedSurface from prostep. As BoundedSurface is an abstract BoundedSurface this class is an access to the sub-class required.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_BoundedSurface: 
        """
        None
        """
    def __init__(self,C : OCP.Geom.Geom_BoundedSurface) -> None: ...
    pass
class GeomToStep_MakeCartesianPoint(GeomToStep_Root):
    """
    This class implements the mapping between classes CartesianPoint from Geom and Pnt from gp, and the class CartesianPoint from StepGeom which describes a point from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_CartesianPoint: 
        """
        None
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,P : OCP.Geom.Geom_CartesianPoint) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,P : OCP.Geom2d.Geom2d_CartesianPoint) -> None: ...
    pass
class GeomToStep_MakeCircle(GeomToStep_Root):
    """
    This class implements the mapping between classes Circle from Geom, and Circ from gp, and the class Circle from StepGeom which describes a circle from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Circle: 
        """
        None
        """
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Circle) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom.Geom_Circle) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ) -> None: ...
    pass
class GeomToStep_MakeConic(GeomToStep_Root):
    """
    This class implements the mapping between classes Conic from Geom and the class Conic from StepGeom which describes a Conic from prostep. As Conic is an abstract Conic this class is an access to the sub-class required.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Conic: 
        """
        None
        """
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Conic) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom.Geom_Conic) -> None: ...
    pass
class GeomToStep_MakeConicalSurface(GeomToStep_Root):
    """
    This class implements the mapping between class ConicalSurface from Geom and the class ConicalSurface from StepGeom which describes a conical_surface from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_ConicalSurface: 
        """
        None
        """
    def __init__(self,CSurf : OCP.Geom.Geom_ConicalSurface) -> None: ...
    pass
class GeomToStep_MakeCurve(GeomToStep_Root):
    """
    This class implements the mapping between classes Curve from Geom and the class Curve from StepGeom which describes a Curve from prostep. As Curve is an abstract curve this class an access to the sub-class required.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Curve: 
        """
        None
        """
    @overload
    def __init__(self,C : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    pass
class GeomToStep_MakeCylindricalSurface(GeomToStep_Root):
    """
    This class implements the mapping between class CylindricalSurface from Geom and the class CylindricalSurface from StepGeom which describes a cylindrical_surface from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_CylindricalSurface: 
        """
        None
        """
    def __init__(self,CSurf : OCP.Geom.Geom_CylindricalSurface) -> None: ...
    pass
class GeomToStep_MakeDirection(GeomToStep_Root):
    """
    This class implements the mapping between classes Direction from Geom, Geom2d and Dir, Dir2d from gp, and the class Direction from StepGeom which describes a direction from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Direction: 
        """
        None
        """
    @overload
    def __init__(self,D : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,D : OCP.Geom2d.Geom2d_Direction) -> None: ...
    @overload
    def __init__(self,D : OCP.gp.gp_Dir2d) -> None: ...
    @overload
    def __init__(self,D : OCP.Geom.Geom_Direction) -> None: ...
    pass
class GeomToStep_MakeElementarySurface(GeomToStep_Root):
    """
    This class implements the mapping between classes ElementarySurface from Geom and the class ElementarySurface from StepGeom which describes a ElementarySurface from prostep. As ElementarySurface is an abstract Surface this class is an access to the sub-class required.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_ElementarySurface: 
        """
        None
        """
    def __init__(self,S : OCP.Geom.Geom_ElementarySurface) -> None: ...
    pass
class GeomToStep_MakeEllipse(GeomToStep_Root):
    """
    This class implements the mapping between classes Ellipse from Geom, and Circ from gp, and the class Ellipse from StepGeom which describes a Ellipse from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Ellipse: 
        """
        None
        """
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Ellipse) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom.Geom_Ellipse) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Elips) -> None: ...
    pass
class GeomToStep_MakeHyperbola(GeomToStep_Root):
    """
    This class implements the mapping between the class Hyperbola from Geom and the class Hyperbola from StepGeom which describes a Hyperbola from ProSTEP
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Hyperbola: 
        """
        None
        """
    @overload
    def __init__(self,C : OCP.Geom.Geom_Hyperbola) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Hyperbola) -> None: ...
    pass
class GeomToStep_MakeLine(GeomToStep_Root):
    """
    This class implements the mapping between classes Line from Geom and Lin from gp, and the class Line from StepGeom which describes a line from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Line: 
        """
        None
        """
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Line) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom.Geom_Line) -> None: ...
    pass
class GeomToStep_MakeParabola(GeomToStep_Root):
    """
    This class implements the mapping between the class Parabola from Geom and the class Parabola from StepGeom which describes a Parabola from ProSTEP
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Parabola: 
        """
        None
        """
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Parabola) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom.Geom_Parabola) -> None: ...
    pass
class GeomToStep_MakePlane(GeomToStep_Root):
    """
    This class implements the mapping between classes Plane from Geom and Pln from gp, and the class Plane from StepGeom which describes a plane from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Plane: 
        """
        None
        """
    @overload
    def __init__(self,P : OCP.Geom.Geom_Plane) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln) -> None: ...
    pass
class GeomToStep_MakePolyline(GeomToStep_Root):
    """
    This class implements the mapping between an Array1 of points from gp and a Polyline from StepGeom.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Polyline: 
        """
        None
        """
    @overload
    def __init__(self,P : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @overload
    def __init__(self,P : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    pass
class GeomToStep_MakeRectangularTrimmedSurface(GeomToStep_Root):
    """
    This class implements the mapping between class RectangularTrimmedSurface from Geom and the class RectangularTrimmedSurface from StepGeom which describes a rectangular_trimmed_surface from ISO-IS 10303-42
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_RectangularTrimmedSurface: 
        """
        None
        """
    def __init__(self,RTSurf : OCP.Geom.Geom_RectangularTrimmedSurface) -> None: ...
    pass
class GeomToStep_MakeSphericalSurface(GeomToStep_Root):
    """
    This class implements the mapping between class SphericalSurface from Geom and the class SphericalSurface from StepGeom which describes a spherical_surface from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_SphericalSurface: 
        """
        None
        """
    def __init__(self,CSurf : OCP.Geom.Geom_SphericalSurface) -> None: ...
    pass
class GeomToStep_MakeSurface(GeomToStep_Root):
    """
    This class implements the mapping between classes Surface from Geom and the class Surface from StepGeom which describes a Surface from prostep. As Surface is an abstract Surface this class is an access to the sub-class required.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Surface: 
        """
        None
        """
    def __init__(self,C : OCP.Geom.Geom_Surface) -> None: ...
    pass
class GeomToStep_MakeSurfaceOfLinearExtrusion(GeomToStep_Root):
    """
    This class implements the mapping between class SurfaceOfLinearExtrusion from Geom and the class SurfaceOfLinearExtrusion from StepGeom which describes a surface_of_linear_extrusion from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_SurfaceOfLinearExtrusion: 
        """
        None
        """
    def __init__(self,CSurf : OCP.Geom.Geom_SurfaceOfLinearExtrusion) -> None: ...
    pass
class GeomToStep_MakeSurfaceOfRevolution(GeomToStep_Root):
    """
    This class implements the mapping between class SurfaceOfRevolution from Geom and the class SurfaceOfRevolution from StepGeom which describes a surface_of_revolution from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_SurfaceOfRevolution: 
        """
        None
        """
    def __init__(self,RevSurf : OCP.Geom.Geom_SurfaceOfRevolution) -> None: ...
    pass
class GeomToStep_MakeSweptSurface(GeomToStep_Root):
    """
    This class implements the mapping between classes SweptSurface from Geom and the class SweptSurface from StepGeom which describes a SweptSurface from prostep. As SweptSurface is an abstract SweptSurface this class is an access to the sub-class required.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_SweptSurface: 
        """
        None
        """
    def __init__(self,S : OCP.Geom.Geom_SweptSurface) -> None: ...
    pass
class GeomToStep_MakeToroidalSurface(GeomToStep_Root):
    """
    This class implements the mapping between class ToroidalSurface from Geom and the class ToroidalSurface from StepGeom which describes a toroidal_surface from Prostep
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_ToroidalSurface: 
        """
        None
        """
    def __init__(self,TorSurf : OCP.Geom.Geom_ToroidalSurface) -> None: ...
    pass
class GeomToStep_MakeVector(GeomToStep_Root):
    """
    This class implements the mapping between classes Vector from Geom, Geom2d and Vec, Vec2d from gp, and the class Vector from StepGeom which describes a Vector from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Vector: 
        """
        None
        """
    @overload
    def __init__(self,V : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def __init__(self,V : OCP.Geom2d.Geom2d_Vector) -> None: ...
    @overload
    def __init__(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def __init__(self,V : OCP.Geom.Geom_Vector) -> None: ...
    pass
class GeomToStep_MakeAxis1Placement(GeomToStep_Root):
    """
    This class implements the mapping between classes Axis1Placement from Geom and Ax1 from gp, and the class Axis1Placement from StepGeom which describes an Axis1Placement from Prostep.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepGeom.StepGeom_Axis1Placement: 
        """
        None
        """
    @overload
    def __init__(self,A : OCP.gp.gp_Ax2d) -> None: ...
    @overload
    def __init__(self,A : OCP.Geom.Geom_Axis1Placement) -> None: ...
    @overload
    def __init__(self,A : OCP.Geom2d.Geom2d_AxisPlacement) -> None: ...
    @overload
    def __init__(self,A : OCP.gp.gp_Ax1) -> None: ...
    pass
