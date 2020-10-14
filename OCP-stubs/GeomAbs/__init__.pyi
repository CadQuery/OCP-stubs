import OCP.GeomAbs
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
__all__  = [
"GeomAbs_BSplKnotDistribution",
"GeomAbs_CurveForm",
"GeomAbs_CurveType",
"GeomAbs_IsoType",
"GeomAbs_JoinType",
"GeomAbs_Shape",
"GeomAbs_SurfaceForm",
"GeomAbs_SurfaceType",
"GeomAbs_UVSense",
"GeomAbs_Arc",
"GeomAbs_BSplineCurve",
"GeomAbs_BSplineSurface",
"GeomAbs_BezierCurve",
"GeomAbs_BezierSurface",
"GeomAbs_C0",
"GeomAbs_C1",
"GeomAbs_C2",
"GeomAbs_C3",
"GeomAbs_CN",
"GeomAbs_Circle",
"GeomAbs_CircularForm",
"GeomAbs_Cone",
"GeomAbs_ConicalForm",
"GeomAbs_Cylinder",
"GeomAbs_CylindricalForm",
"GeomAbs_Ellipse",
"GeomAbs_EllipticForm",
"GeomAbs_G1",
"GeomAbs_G2",
"GeomAbs_Hyperbola",
"GeomAbs_HyperbolicForm",
"GeomAbs_Intersection",
"GeomAbs_IsoU",
"GeomAbs_IsoV",
"GeomAbs_Line",
"GeomAbs_NonUniform",
"GeomAbs_NoneIso",
"GeomAbs_OffsetCurve",
"GeomAbs_OffsetSurface",
"GeomAbs_OppositeUV",
"GeomAbs_OtherCurve",
"GeomAbs_OtherCurveForm",
"GeomAbs_OtherSurface",
"GeomAbs_OtherSurfaceForm",
"GeomAbs_Parabola",
"GeomAbs_ParabolicForm",
"GeomAbs_PiecewiseBezier",
"GeomAbs_PlanarForm",
"GeomAbs_Plane",
"GeomAbs_PolylineForm",
"GeomAbs_QuadricForm",
"GeomAbs_QuasiUniform",
"GeomAbs_RevolutionForm",
"GeomAbs_RuledForm",
"GeomAbs_SameU",
"GeomAbs_SameUV",
"GeomAbs_SameV",
"GeomAbs_Sphere",
"GeomAbs_SphericalForm",
"GeomAbs_SurfaceOfExtrusion",
"GeomAbs_SurfaceOfRevolution",
"GeomAbs_Tangent",
"GeomAbs_ToroidalForm",
"GeomAbs_Torus",
"GeomAbs_Uniform"
]
class GeomAbs_BSplKnotDistribution():
    """
    This enumeration is used in the classes BSplineCurve and BSplineSurface to describe the repartition of set of knots. (comments in classes BSplineCurve and BSplineSurface)

    Members:

      GeomAbs_NonUniform

      GeomAbs_Uniform

      GeomAbs_QuasiUniform

      GeomAbs_PiecewiseBezier
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
    GeomAbs_NonUniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = GeomAbs_BSplKnotDistribution.GeomAbs_NonUniform
    GeomAbs_PiecewiseBezier: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = GeomAbs_BSplKnotDistribution.GeomAbs_PiecewiseBezier
    GeomAbs_QuasiUniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = GeomAbs_BSplKnotDistribution.GeomAbs_QuasiUniform
    GeomAbs_Uniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = GeomAbs_BSplKnotDistribution.GeomAbs_Uniform
    __entries: dict # value = {'GeomAbs_NonUniform': (GeomAbs_BSplKnotDistribution.GeomAbs_NonUniform, None), 'GeomAbs_Uniform': (GeomAbs_BSplKnotDistribution.GeomAbs_Uniform, None), 'GeomAbs_QuasiUniform': (GeomAbs_BSplKnotDistribution.GeomAbs_QuasiUniform, None), 'GeomAbs_PiecewiseBezier': (GeomAbs_BSplKnotDistribution.GeomAbs_PiecewiseBezier, None)}
    __members__: dict # value = {'GeomAbs_NonUniform': GeomAbs_BSplKnotDistribution.GeomAbs_NonUniform, 'GeomAbs_Uniform': GeomAbs_BSplKnotDistribution.GeomAbs_Uniform, 'GeomAbs_QuasiUniform': GeomAbs_BSplKnotDistribution.GeomAbs_QuasiUniform, 'GeomAbs_PiecewiseBezier': GeomAbs_BSplKnotDistribution.GeomAbs_PiecewiseBezier}
    pass
class GeomAbs_CurveForm():
    """
    This enumeration is used to note specific curve form.

    Members:

      GeomAbs_PolylineForm

      GeomAbs_CircularForm

      GeomAbs_EllipticForm

      GeomAbs_HyperbolicForm

      GeomAbs_ParabolicForm

      GeomAbs_OtherCurveForm
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
    GeomAbs_CircularForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_CircularForm
    GeomAbs_EllipticForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_EllipticForm
    GeomAbs_HyperbolicForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_HyperbolicForm
    GeomAbs_OtherCurveForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_OtherCurveForm
    GeomAbs_ParabolicForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_ParabolicForm
    GeomAbs_PolylineForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_PolylineForm
    __entries: dict # value = {'GeomAbs_PolylineForm': (GeomAbs_CurveForm.GeomAbs_PolylineForm, None), 'GeomAbs_CircularForm': (GeomAbs_CurveForm.GeomAbs_CircularForm, None), 'GeomAbs_EllipticForm': (GeomAbs_CurveForm.GeomAbs_EllipticForm, None), 'GeomAbs_HyperbolicForm': (GeomAbs_CurveForm.GeomAbs_HyperbolicForm, None), 'GeomAbs_ParabolicForm': (GeomAbs_CurveForm.GeomAbs_ParabolicForm, None), 'GeomAbs_OtherCurveForm': (GeomAbs_CurveForm.GeomAbs_OtherCurveForm, None)}
    __members__: dict # value = {'GeomAbs_PolylineForm': GeomAbs_CurveForm.GeomAbs_PolylineForm, 'GeomAbs_CircularForm': GeomAbs_CurveForm.GeomAbs_CircularForm, 'GeomAbs_EllipticForm': GeomAbs_CurveForm.GeomAbs_EllipticForm, 'GeomAbs_HyperbolicForm': GeomAbs_CurveForm.GeomAbs_HyperbolicForm, 'GeomAbs_ParabolicForm': GeomAbs_CurveForm.GeomAbs_ParabolicForm, 'GeomAbs_OtherCurveForm': GeomAbs_CurveForm.GeomAbs_OtherCurveForm}
    pass
class GeomAbs_CurveType():
    """
    Identifies the type of a curve.

    Members:

      GeomAbs_Line

      GeomAbs_Circle

      GeomAbs_Ellipse

      GeomAbs_Hyperbola

      GeomAbs_Parabola

      GeomAbs_BezierCurve

      GeomAbs_BSplineCurve

      GeomAbs_OffsetCurve

      GeomAbs_OtherCurve
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
    GeomAbs_BSplineCurve: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_BSplineCurve
    GeomAbs_BezierCurve: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_BezierCurve
    GeomAbs_Circle: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Circle
    GeomAbs_Ellipse: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Ellipse
    GeomAbs_Hyperbola: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Hyperbola
    GeomAbs_Line: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Line
    GeomAbs_OffsetCurve: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_OffsetCurve
    GeomAbs_OtherCurve: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_OtherCurve
    GeomAbs_Parabola: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Parabola
    __entries: dict # value = {'GeomAbs_Line': (GeomAbs_CurveType.GeomAbs_Line, None), 'GeomAbs_Circle': (GeomAbs_CurveType.GeomAbs_Circle, None), 'GeomAbs_Ellipse': (GeomAbs_CurveType.GeomAbs_Ellipse, None), 'GeomAbs_Hyperbola': (GeomAbs_CurveType.GeomAbs_Hyperbola, None), 'GeomAbs_Parabola': (GeomAbs_CurveType.GeomAbs_Parabola, None), 'GeomAbs_BezierCurve': (GeomAbs_CurveType.GeomAbs_BezierCurve, None), 'GeomAbs_BSplineCurve': (GeomAbs_CurveType.GeomAbs_BSplineCurve, None), 'GeomAbs_OffsetCurve': (GeomAbs_CurveType.GeomAbs_OffsetCurve, None), 'GeomAbs_OtherCurve': (GeomAbs_CurveType.GeomAbs_OtherCurve, None)}
    __members__: dict # value = {'GeomAbs_Line': GeomAbs_CurveType.GeomAbs_Line, 'GeomAbs_Circle': GeomAbs_CurveType.GeomAbs_Circle, 'GeomAbs_Ellipse': GeomAbs_CurveType.GeomAbs_Ellipse, 'GeomAbs_Hyperbola': GeomAbs_CurveType.GeomAbs_Hyperbola, 'GeomAbs_Parabola': GeomAbs_CurveType.GeomAbs_Parabola, 'GeomAbs_BezierCurve': GeomAbs_CurveType.GeomAbs_BezierCurve, 'GeomAbs_BSplineCurve': GeomAbs_CurveType.GeomAbs_BSplineCurve, 'GeomAbs_OffsetCurve': GeomAbs_CurveType.GeomAbs_OffsetCurve, 'GeomAbs_OtherCurve': GeomAbs_CurveType.GeomAbs_OtherCurve}
    pass
class GeomAbs_IsoType():
    """
    this enumeration describes if a curve is an U isoparaetric or V isoparametric

    Members:

      GeomAbs_IsoU

      GeomAbs_IsoV

      GeomAbs_NoneIso
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
    GeomAbs_IsoU: OCP.GeomAbs.GeomAbs_IsoType # value = GeomAbs_IsoType.GeomAbs_IsoU
    GeomAbs_IsoV: OCP.GeomAbs.GeomAbs_IsoType # value = GeomAbs_IsoType.GeomAbs_IsoV
    GeomAbs_NoneIso: OCP.GeomAbs.GeomAbs_IsoType # value = GeomAbs_IsoType.GeomAbs_NoneIso
    __entries: dict # value = {'GeomAbs_IsoU': (GeomAbs_IsoType.GeomAbs_IsoU, None), 'GeomAbs_IsoV': (GeomAbs_IsoType.GeomAbs_IsoV, None), 'GeomAbs_NoneIso': (GeomAbs_IsoType.GeomAbs_NoneIso, None)}
    __members__: dict # value = {'GeomAbs_IsoU': GeomAbs_IsoType.GeomAbs_IsoU, 'GeomAbs_IsoV': GeomAbs_IsoType.GeomAbs_IsoV, 'GeomAbs_NoneIso': GeomAbs_IsoType.GeomAbs_NoneIso}
    pass
class GeomAbs_JoinType():
    """
    Characterizes the type of a join, built by an algorithm for constructing parallel curves, between two consecutive arcs of a contour parallel to a given contour.

    Members:

      GeomAbs_Arc

      GeomAbs_Tangent

      GeomAbs_Intersection
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
    GeomAbs_Arc: OCP.GeomAbs.GeomAbs_JoinType # value = GeomAbs_JoinType.GeomAbs_Arc
    GeomAbs_Intersection: OCP.GeomAbs.GeomAbs_JoinType # value = GeomAbs_JoinType.GeomAbs_Intersection
    GeomAbs_Tangent: OCP.GeomAbs.GeomAbs_JoinType # value = GeomAbs_JoinType.GeomAbs_Tangent
    __entries: dict # value = {'GeomAbs_Arc': (GeomAbs_JoinType.GeomAbs_Arc, None), 'GeomAbs_Tangent': (GeomAbs_JoinType.GeomAbs_Tangent, None), 'GeomAbs_Intersection': (GeomAbs_JoinType.GeomAbs_Intersection, None)}
    __members__: dict # value = {'GeomAbs_Arc': GeomAbs_JoinType.GeomAbs_Arc, 'GeomAbs_Tangent': GeomAbs_JoinType.GeomAbs_Tangent, 'GeomAbs_Intersection': GeomAbs_JoinType.GeomAbs_Intersection}
    pass
class GeomAbs_Shape():
    """
    Provides information about the continuity of a curve: - C0: only geometric continuity. - G1: for each point on the curve, the tangent vectors "on the right" and "on the left" are collinear with the same orientation. - C1: continuity of the first derivative. The "C1" curve is also "G1" but, in addition, the tangent vectors " on the right" and "on the left" are equal. - G2: for each point on the curve, the normalized normal vectors "on the right" and "on the left" are equal. - C2: continuity of the second derivative. - C3: continuity of the third derivative. - CN: continuity of the N-th derivative, whatever is the value given for N (infinite order of continuity). Also provides information about the continuity of a surface: - C0: only geometric continuity. - C1: continuity of the first derivatives; any isoparametric (in U or V) of a surface "C1" is also "C1". - G2: for BSpline curves only; "on the right" and "on the left" of a knot the computation of the "main curvature radii" and the "main directions" (when they exist) gives the same result. - C2: continuity of the second derivative. - C3: continuity of the third derivative. - CN: continuity of any N-th derivative, whatever is the value given for N (infinite order of continuity). We may also say that a surface is "Ci" in u, and "Cj" in v to indicate the continuity of its derivatives up to the order i in the u parametric direction, and j in the v parametric direction.

    Members:

      GeomAbs_C0

      GeomAbs_G1

      GeomAbs_C1

      GeomAbs_G2

      GeomAbs_C2

      GeomAbs_C3

      GeomAbs_CN
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
    GeomAbs_C0: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_C0
    GeomAbs_C1: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_C1
    GeomAbs_C2: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_C2
    GeomAbs_C3: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_C3
    GeomAbs_CN: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_CN
    GeomAbs_G1: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_G1
    GeomAbs_G2: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_G2
    __entries: dict # value = {'GeomAbs_C0': (GeomAbs_Shape.GeomAbs_C0, None), 'GeomAbs_G1': (GeomAbs_Shape.GeomAbs_G1, None), 'GeomAbs_C1': (GeomAbs_Shape.GeomAbs_C1, None), 'GeomAbs_G2': (GeomAbs_Shape.GeomAbs_G2, None), 'GeomAbs_C2': (GeomAbs_Shape.GeomAbs_C2, None), 'GeomAbs_C3': (GeomAbs_Shape.GeomAbs_C3, None), 'GeomAbs_CN': (GeomAbs_Shape.GeomAbs_CN, None)}
    __members__: dict # value = {'GeomAbs_C0': GeomAbs_Shape.GeomAbs_C0, 'GeomAbs_G1': GeomAbs_Shape.GeomAbs_G1, 'GeomAbs_C1': GeomAbs_Shape.GeomAbs_C1, 'GeomAbs_G2': GeomAbs_Shape.GeomAbs_G2, 'GeomAbs_C2': GeomAbs_Shape.GeomAbs_C2, 'GeomAbs_C3': GeomAbs_Shape.GeomAbs_C3, 'GeomAbs_CN': GeomAbs_Shape.GeomAbs_CN}
    pass
class GeomAbs_SurfaceForm():
    """
    This enumeration is used to note specific surface form.

    Members:

      GeomAbs_PlanarForm

      GeomAbs_ConicalForm

      GeomAbs_CylindricalForm

      GeomAbs_ToroidalForm

      GeomAbs_SphericalForm

      GeomAbs_RevolutionForm

      GeomAbs_RuledForm

      GeomAbs_QuadricForm

      GeomAbs_OtherSurfaceForm
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
    GeomAbs_ConicalForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_ConicalForm
    GeomAbs_CylindricalForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_CylindricalForm
    GeomAbs_OtherSurfaceForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_OtherSurfaceForm
    GeomAbs_PlanarForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_PlanarForm
    GeomAbs_QuadricForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_QuadricForm
    GeomAbs_RevolutionForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_RevolutionForm
    GeomAbs_RuledForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_RuledForm
    GeomAbs_SphericalForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_SphericalForm
    GeomAbs_ToroidalForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_ToroidalForm
    __entries: dict # value = {'GeomAbs_PlanarForm': (GeomAbs_SurfaceForm.GeomAbs_PlanarForm, None), 'GeomAbs_ConicalForm': (GeomAbs_SurfaceForm.GeomAbs_ConicalForm, None), 'GeomAbs_CylindricalForm': (GeomAbs_SurfaceForm.GeomAbs_CylindricalForm, None), 'GeomAbs_ToroidalForm': (GeomAbs_SurfaceForm.GeomAbs_ToroidalForm, None), 'GeomAbs_SphericalForm': (GeomAbs_SurfaceForm.GeomAbs_SphericalForm, None), 'GeomAbs_RevolutionForm': (GeomAbs_SurfaceForm.GeomAbs_RevolutionForm, None), 'GeomAbs_RuledForm': (GeomAbs_SurfaceForm.GeomAbs_RuledForm, None), 'GeomAbs_QuadricForm': (GeomAbs_SurfaceForm.GeomAbs_QuadricForm, None), 'GeomAbs_OtherSurfaceForm': (GeomAbs_SurfaceForm.GeomAbs_OtherSurfaceForm, None)}
    __members__: dict # value = {'GeomAbs_PlanarForm': GeomAbs_SurfaceForm.GeomAbs_PlanarForm, 'GeomAbs_ConicalForm': GeomAbs_SurfaceForm.GeomAbs_ConicalForm, 'GeomAbs_CylindricalForm': GeomAbs_SurfaceForm.GeomAbs_CylindricalForm, 'GeomAbs_ToroidalForm': GeomAbs_SurfaceForm.GeomAbs_ToroidalForm, 'GeomAbs_SphericalForm': GeomAbs_SurfaceForm.GeomAbs_SphericalForm, 'GeomAbs_RevolutionForm': GeomAbs_SurfaceForm.GeomAbs_RevolutionForm, 'GeomAbs_RuledForm': GeomAbs_SurfaceForm.GeomAbs_RuledForm, 'GeomAbs_QuadricForm': GeomAbs_SurfaceForm.GeomAbs_QuadricForm, 'GeomAbs_OtherSurfaceForm': GeomAbs_SurfaceForm.GeomAbs_OtherSurfaceForm}
    pass
class GeomAbs_SurfaceType():
    """
    None

    Members:

      GeomAbs_Plane

      GeomAbs_Cylinder

      GeomAbs_Cone

      GeomAbs_Sphere

      GeomAbs_Torus

      GeomAbs_BezierSurface

      GeomAbs_BSplineSurface

      GeomAbs_SurfaceOfRevolution

      GeomAbs_SurfaceOfExtrusion

      GeomAbs_OffsetSurface

      GeomAbs_OtherSurface
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
    GeomAbs_BSplineSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_BSplineSurface
    GeomAbs_BezierSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_BezierSurface
    GeomAbs_Cone: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Cone
    GeomAbs_Cylinder: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Cylinder
    GeomAbs_OffsetSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_OffsetSurface
    GeomAbs_OtherSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_OtherSurface
    GeomAbs_Plane: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Plane
    GeomAbs_Sphere: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Sphere
    GeomAbs_SurfaceOfExtrusion: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_SurfaceOfExtrusion
    GeomAbs_SurfaceOfRevolution: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_SurfaceOfRevolution
    GeomAbs_Torus: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Torus
    __entries: dict # value = {'GeomAbs_Plane': (GeomAbs_SurfaceType.GeomAbs_Plane, None), 'GeomAbs_Cylinder': (GeomAbs_SurfaceType.GeomAbs_Cylinder, None), 'GeomAbs_Cone': (GeomAbs_SurfaceType.GeomAbs_Cone, None), 'GeomAbs_Sphere': (GeomAbs_SurfaceType.GeomAbs_Sphere, None), 'GeomAbs_Torus': (GeomAbs_SurfaceType.GeomAbs_Torus, None), 'GeomAbs_BezierSurface': (GeomAbs_SurfaceType.GeomAbs_BezierSurface, None), 'GeomAbs_BSplineSurface': (GeomAbs_SurfaceType.GeomAbs_BSplineSurface, None), 'GeomAbs_SurfaceOfRevolution': (GeomAbs_SurfaceType.GeomAbs_SurfaceOfRevolution, None), 'GeomAbs_SurfaceOfExtrusion': (GeomAbs_SurfaceType.GeomAbs_SurfaceOfExtrusion, None), 'GeomAbs_OffsetSurface': (GeomAbs_SurfaceType.GeomAbs_OffsetSurface, None), 'GeomAbs_OtherSurface': (GeomAbs_SurfaceType.GeomAbs_OtherSurface, None)}
    __members__: dict # value = {'GeomAbs_Plane': GeomAbs_SurfaceType.GeomAbs_Plane, 'GeomAbs_Cylinder': GeomAbs_SurfaceType.GeomAbs_Cylinder, 'GeomAbs_Cone': GeomAbs_SurfaceType.GeomAbs_Cone, 'GeomAbs_Sphere': GeomAbs_SurfaceType.GeomAbs_Sphere, 'GeomAbs_Torus': GeomAbs_SurfaceType.GeomAbs_Torus, 'GeomAbs_BezierSurface': GeomAbs_SurfaceType.GeomAbs_BezierSurface, 'GeomAbs_BSplineSurface': GeomAbs_SurfaceType.GeomAbs_BSplineSurface, 'GeomAbs_SurfaceOfRevolution': GeomAbs_SurfaceType.GeomAbs_SurfaceOfRevolution, 'GeomAbs_SurfaceOfExtrusion': GeomAbs_SurfaceType.GeomAbs_SurfaceOfExtrusion, 'GeomAbs_OffsetSurface': GeomAbs_SurfaceType.GeomAbs_OffsetSurface, 'GeomAbs_OtherSurface': GeomAbs_SurfaceType.GeomAbs_OtherSurface}
    pass
class GeomAbs_UVSense():
    """
    This enumeration is used in the class RectangularTrimmedSurface to compare the orientation of the basic surface and the orientation of the trimmed surface and in the class ElementarySurface to know the direction of parametrization by comparison with the default construction mode.

    Members:

      GeomAbs_SameUV

      GeomAbs_SameU

      GeomAbs_SameV

      GeomAbs_OppositeUV
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
    GeomAbs_OppositeUV: OCP.GeomAbs.GeomAbs_UVSense # value = GeomAbs_UVSense.GeomAbs_OppositeUV
    GeomAbs_SameU: OCP.GeomAbs.GeomAbs_UVSense # value = GeomAbs_UVSense.GeomAbs_SameU
    GeomAbs_SameUV: OCP.GeomAbs.GeomAbs_UVSense # value = GeomAbs_UVSense.GeomAbs_SameUV
    GeomAbs_SameV: OCP.GeomAbs.GeomAbs_UVSense # value = GeomAbs_UVSense.GeomAbs_SameV
    __entries: dict # value = {'GeomAbs_SameUV': (GeomAbs_UVSense.GeomAbs_SameUV, None), 'GeomAbs_SameU': (GeomAbs_UVSense.GeomAbs_SameU, None), 'GeomAbs_SameV': (GeomAbs_UVSense.GeomAbs_SameV, None), 'GeomAbs_OppositeUV': (GeomAbs_UVSense.GeomAbs_OppositeUV, None)}
    __members__: dict # value = {'GeomAbs_SameUV': GeomAbs_UVSense.GeomAbs_SameUV, 'GeomAbs_SameU': GeomAbs_UVSense.GeomAbs_SameU, 'GeomAbs_SameV': GeomAbs_UVSense.GeomAbs_SameV, 'GeomAbs_OppositeUV': GeomAbs_UVSense.GeomAbs_OppositeUV}
    pass
GeomAbs_Arc: OCP.GeomAbs.GeomAbs_JoinType # value = GeomAbs_JoinType.GeomAbs_Arc
GeomAbs_BSplineCurve: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_BSplineCurve
GeomAbs_BSplineSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_BSplineSurface
GeomAbs_BezierCurve: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_BezierCurve
GeomAbs_BezierSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_BezierSurface
GeomAbs_C0: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_C0
GeomAbs_C1: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_C1
GeomAbs_C2: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_C2
GeomAbs_C3: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_C3
GeomAbs_CN: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_CN
GeomAbs_Circle: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Circle
GeomAbs_CircularForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_CircularForm
GeomAbs_Cone: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Cone
GeomAbs_ConicalForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_ConicalForm
GeomAbs_Cylinder: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Cylinder
GeomAbs_CylindricalForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_CylindricalForm
GeomAbs_Ellipse: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Ellipse
GeomAbs_EllipticForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_EllipticForm
GeomAbs_G1: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_G1
GeomAbs_G2: OCP.GeomAbs.GeomAbs_Shape # value = GeomAbs_Shape.GeomAbs_G2
GeomAbs_Hyperbola: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Hyperbola
GeomAbs_HyperbolicForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_HyperbolicForm
GeomAbs_Intersection: OCP.GeomAbs.GeomAbs_JoinType # value = GeomAbs_JoinType.GeomAbs_Intersection
GeomAbs_IsoU: OCP.GeomAbs.GeomAbs_IsoType # value = GeomAbs_IsoType.GeomAbs_IsoU
GeomAbs_IsoV: OCP.GeomAbs.GeomAbs_IsoType # value = GeomAbs_IsoType.GeomAbs_IsoV
GeomAbs_Line: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Line
GeomAbs_NonUniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = GeomAbs_BSplKnotDistribution.GeomAbs_NonUniform
GeomAbs_NoneIso: OCP.GeomAbs.GeomAbs_IsoType # value = GeomAbs_IsoType.GeomAbs_NoneIso
GeomAbs_OffsetCurve: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_OffsetCurve
GeomAbs_OffsetSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_OffsetSurface
GeomAbs_OppositeUV: OCP.GeomAbs.GeomAbs_UVSense # value = GeomAbs_UVSense.GeomAbs_OppositeUV
GeomAbs_OtherCurve: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_OtherCurve
GeomAbs_OtherCurveForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_OtherCurveForm
GeomAbs_OtherSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_OtherSurface
GeomAbs_OtherSurfaceForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_OtherSurfaceForm
GeomAbs_Parabola: OCP.GeomAbs.GeomAbs_CurveType # value = GeomAbs_CurveType.GeomAbs_Parabola
GeomAbs_ParabolicForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_ParabolicForm
GeomAbs_PiecewiseBezier: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = GeomAbs_BSplKnotDistribution.GeomAbs_PiecewiseBezier
GeomAbs_PlanarForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_PlanarForm
GeomAbs_Plane: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Plane
GeomAbs_PolylineForm: OCP.GeomAbs.GeomAbs_CurveForm # value = GeomAbs_CurveForm.GeomAbs_PolylineForm
GeomAbs_QuadricForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_QuadricForm
GeomAbs_QuasiUniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = GeomAbs_BSplKnotDistribution.GeomAbs_QuasiUniform
GeomAbs_RevolutionForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_RevolutionForm
GeomAbs_RuledForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_RuledForm
GeomAbs_SameU: OCP.GeomAbs.GeomAbs_UVSense # value = GeomAbs_UVSense.GeomAbs_SameU
GeomAbs_SameUV: OCP.GeomAbs.GeomAbs_UVSense # value = GeomAbs_UVSense.GeomAbs_SameUV
GeomAbs_SameV: OCP.GeomAbs.GeomAbs_UVSense # value = GeomAbs_UVSense.GeomAbs_SameV
GeomAbs_Sphere: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Sphere
GeomAbs_SphericalForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_SphericalForm
GeomAbs_SurfaceOfExtrusion: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_SurfaceOfExtrusion
GeomAbs_SurfaceOfRevolution: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_SurfaceOfRevolution
GeomAbs_Tangent: OCP.GeomAbs.GeomAbs_JoinType # value = GeomAbs_JoinType.GeomAbs_Tangent
GeomAbs_ToroidalForm: OCP.GeomAbs.GeomAbs_SurfaceForm # value = GeomAbs_SurfaceForm.GeomAbs_ToroidalForm
GeomAbs_Torus: OCP.GeomAbs.GeomAbs_SurfaceType # value = GeomAbs_SurfaceType.GeomAbs_Torus
GeomAbs_Uniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = GeomAbs_BSplKnotDistribution.GeomAbs_Uniform
