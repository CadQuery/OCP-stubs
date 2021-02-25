import OCP.GeomAbs
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
__all__  = [
"GeomAbs_BSplKnotDistribution",
"GeomAbs_CurveType",
"GeomAbs_IsoType",
"GeomAbs_JoinType",
"GeomAbs_Shape",
"GeomAbs_SurfaceType",
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
"GeomAbs_Cone",
"GeomAbs_Cylinder",
"GeomAbs_Ellipse",
"GeomAbs_G1",
"GeomAbs_G2",
"GeomAbs_Hyperbola",
"GeomAbs_Intersection",
"GeomAbs_IsoU",
"GeomAbs_IsoV",
"GeomAbs_Line",
"GeomAbs_NonUniform",
"GeomAbs_NoneIso",
"GeomAbs_OffsetCurve",
"GeomAbs_OffsetSurface",
"GeomAbs_OtherCurve",
"GeomAbs_OtherSurface",
"GeomAbs_Parabola",
"GeomAbs_PiecewiseBezier",
"GeomAbs_Plane",
"GeomAbs_QuasiUniform",
"GeomAbs_Sphere",
"GeomAbs_SurfaceOfExtrusion",
"GeomAbs_SurfaceOfRevolution",
"GeomAbs_Tangent",
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
    GeomAbs_NonUniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = <GeomAbs_BSplKnotDistribution.GeomAbs_NonUniform: 0>
    GeomAbs_PiecewiseBezier: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = <GeomAbs_BSplKnotDistribution.GeomAbs_PiecewiseBezier: 3>
    GeomAbs_QuasiUniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = <GeomAbs_BSplKnotDistribution.GeomAbs_QuasiUniform: 2>
    GeomAbs_Uniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = <GeomAbs_BSplKnotDistribution.GeomAbs_Uniform: 1>
    __entries: dict # value = {'GeomAbs_NonUniform': (<GeomAbs_BSplKnotDistribution.GeomAbs_NonUniform: 0>, None), 'GeomAbs_Uniform': (<GeomAbs_BSplKnotDistribution.GeomAbs_Uniform: 1>, None), 'GeomAbs_QuasiUniform': (<GeomAbs_BSplKnotDistribution.GeomAbs_QuasiUniform: 2>, None), 'GeomAbs_PiecewiseBezier': (<GeomAbs_BSplKnotDistribution.GeomAbs_PiecewiseBezier: 3>, None)}
    __members__: dict # value = {'GeomAbs_NonUniform': <GeomAbs_BSplKnotDistribution.GeomAbs_NonUniform: 0>, 'GeomAbs_Uniform': <GeomAbs_BSplKnotDistribution.GeomAbs_Uniform: 1>, 'GeomAbs_QuasiUniform': <GeomAbs_BSplKnotDistribution.GeomAbs_QuasiUniform: 2>, 'GeomAbs_PiecewiseBezier': <GeomAbs_BSplKnotDistribution.GeomAbs_PiecewiseBezier: 3>}
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
    GeomAbs_BSplineCurve: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_BSplineCurve: 6>
    GeomAbs_BezierCurve: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_BezierCurve: 5>
    GeomAbs_Circle: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Circle: 1>
    GeomAbs_Ellipse: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Ellipse: 2>
    GeomAbs_Hyperbola: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Hyperbola: 3>
    GeomAbs_Line: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Line: 0>
    GeomAbs_OffsetCurve: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_OffsetCurve: 7>
    GeomAbs_OtherCurve: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_OtherCurve: 8>
    GeomAbs_Parabola: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Parabola: 4>
    __entries: dict # value = {'GeomAbs_Line': (<GeomAbs_CurveType.GeomAbs_Line: 0>, None), 'GeomAbs_Circle': (<GeomAbs_CurveType.GeomAbs_Circle: 1>, None), 'GeomAbs_Ellipse': (<GeomAbs_CurveType.GeomAbs_Ellipse: 2>, None), 'GeomAbs_Hyperbola': (<GeomAbs_CurveType.GeomAbs_Hyperbola: 3>, None), 'GeomAbs_Parabola': (<GeomAbs_CurveType.GeomAbs_Parabola: 4>, None), 'GeomAbs_BezierCurve': (<GeomAbs_CurveType.GeomAbs_BezierCurve: 5>, None), 'GeomAbs_BSplineCurve': (<GeomAbs_CurveType.GeomAbs_BSplineCurve: 6>, None), 'GeomAbs_OffsetCurve': (<GeomAbs_CurveType.GeomAbs_OffsetCurve: 7>, None), 'GeomAbs_OtherCurve': (<GeomAbs_CurveType.GeomAbs_OtherCurve: 8>, None)}
    __members__: dict # value = {'GeomAbs_Line': <GeomAbs_CurveType.GeomAbs_Line: 0>, 'GeomAbs_Circle': <GeomAbs_CurveType.GeomAbs_Circle: 1>, 'GeomAbs_Ellipse': <GeomAbs_CurveType.GeomAbs_Ellipse: 2>, 'GeomAbs_Hyperbola': <GeomAbs_CurveType.GeomAbs_Hyperbola: 3>, 'GeomAbs_Parabola': <GeomAbs_CurveType.GeomAbs_Parabola: 4>, 'GeomAbs_BezierCurve': <GeomAbs_CurveType.GeomAbs_BezierCurve: 5>, 'GeomAbs_BSplineCurve': <GeomAbs_CurveType.GeomAbs_BSplineCurve: 6>, 'GeomAbs_OffsetCurve': <GeomAbs_CurveType.GeomAbs_OffsetCurve: 7>, 'GeomAbs_OtherCurve': <GeomAbs_CurveType.GeomAbs_OtherCurve: 8>}
    pass
class GeomAbs_IsoType():
    """
    this enumeration describes if a curve is an U isoparaetric or V isoparametric

    Members:

      GeomAbs_IsoU

      GeomAbs_IsoV

      GeomAbs_NoneIso
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
    GeomAbs_IsoU: OCP.GeomAbs.GeomAbs_IsoType # value = <GeomAbs_IsoType.GeomAbs_IsoU: 0>
    GeomAbs_IsoV: OCP.GeomAbs.GeomAbs_IsoType # value = <GeomAbs_IsoType.GeomAbs_IsoV: 1>
    GeomAbs_NoneIso: OCP.GeomAbs.GeomAbs_IsoType # value = <GeomAbs_IsoType.GeomAbs_NoneIso: 2>
    __entries: dict # value = {'GeomAbs_IsoU': (<GeomAbs_IsoType.GeomAbs_IsoU: 0>, None), 'GeomAbs_IsoV': (<GeomAbs_IsoType.GeomAbs_IsoV: 1>, None), 'GeomAbs_NoneIso': (<GeomAbs_IsoType.GeomAbs_NoneIso: 2>, None)}
    __members__: dict # value = {'GeomAbs_IsoU': <GeomAbs_IsoType.GeomAbs_IsoU: 0>, 'GeomAbs_IsoV': <GeomAbs_IsoType.GeomAbs_IsoV: 1>, 'GeomAbs_NoneIso': <GeomAbs_IsoType.GeomAbs_NoneIso: 2>}
    pass
class GeomAbs_JoinType():
    """
    Characterizes the type of a join, built by an algorithm for constructing parallel curves, between two consecutive arcs of a contour parallel to a given contour.

    Members:

      GeomAbs_Arc

      GeomAbs_Tangent

      GeomAbs_Intersection
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
    GeomAbs_Arc: OCP.GeomAbs.GeomAbs_JoinType # value = <GeomAbs_JoinType.GeomAbs_Arc: 0>
    GeomAbs_Intersection: OCP.GeomAbs.GeomAbs_JoinType # value = <GeomAbs_JoinType.GeomAbs_Intersection: 2>
    GeomAbs_Tangent: OCP.GeomAbs.GeomAbs_JoinType # value = <GeomAbs_JoinType.GeomAbs_Tangent: 1>
    __entries: dict # value = {'GeomAbs_Arc': (<GeomAbs_JoinType.GeomAbs_Arc: 0>, None), 'GeomAbs_Tangent': (<GeomAbs_JoinType.GeomAbs_Tangent: 1>, None), 'GeomAbs_Intersection': (<GeomAbs_JoinType.GeomAbs_Intersection: 2>, None)}
    __members__: dict # value = {'GeomAbs_Arc': <GeomAbs_JoinType.GeomAbs_Arc: 0>, 'GeomAbs_Tangent': <GeomAbs_JoinType.GeomAbs_Tangent: 1>, 'GeomAbs_Intersection': <GeomAbs_JoinType.GeomAbs_Intersection: 2>}
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
    GeomAbs_C0: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_C0: 0>
    GeomAbs_C1: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_C1: 2>
    GeomAbs_C2: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_C2: 4>
    GeomAbs_C3: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_C3: 5>
    GeomAbs_CN: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_CN: 6>
    GeomAbs_G1: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_G1: 1>
    GeomAbs_G2: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_G2: 3>
    __entries: dict # value = {'GeomAbs_C0': (<GeomAbs_Shape.GeomAbs_C0: 0>, None), 'GeomAbs_G1': (<GeomAbs_Shape.GeomAbs_G1: 1>, None), 'GeomAbs_C1': (<GeomAbs_Shape.GeomAbs_C1: 2>, None), 'GeomAbs_G2': (<GeomAbs_Shape.GeomAbs_G2: 3>, None), 'GeomAbs_C2': (<GeomAbs_Shape.GeomAbs_C2: 4>, None), 'GeomAbs_C3': (<GeomAbs_Shape.GeomAbs_C3: 5>, None), 'GeomAbs_CN': (<GeomAbs_Shape.GeomAbs_CN: 6>, None)}
    __members__: dict # value = {'GeomAbs_C0': <GeomAbs_Shape.GeomAbs_C0: 0>, 'GeomAbs_G1': <GeomAbs_Shape.GeomAbs_G1: 1>, 'GeomAbs_C1': <GeomAbs_Shape.GeomAbs_C1: 2>, 'GeomAbs_G2': <GeomAbs_Shape.GeomAbs_G2: 3>, 'GeomAbs_C2': <GeomAbs_Shape.GeomAbs_C2: 4>, 'GeomAbs_C3': <GeomAbs_Shape.GeomAbs_C3: 5>, 'GeomAbs_CN': <GeomAbs_Shape.GeomAbs_CN: 6>}
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
    GeomAbs_BSplineSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_BSplineSurface: 6>
    GeomAbs_BezierSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_BezierSurface: 5>
    GeomAbs_Cone: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Cone: 2>
    GeomAbs_Cylinder: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Cylinder: 1>
    GeomAbs_OffsetSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_OffsetSurface: 9>
    GeomAbs_OtherSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_OtherSurface: 10>
    GeomAbs_Plane: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Plane: 0>
    GeomAbs_Sphere: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Sphere: 3>
    GeomAbs_SurfaceOfExtrusion: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_SurfaceOfExtrusion: 8>
    GeomAbs_SurfaceOfRevolution: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_SurfaceOfRevolution: 7>
    GeomAbs_Torus: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Torus: 4>
    __entries: dict # value = {'GeomAbs_Plane': (<GeomAbs_SurfaceType.GeomAbs_Plane: 0>, None), 'GeomAbs_Cylinder': (<GeomAbs_SurfaceType.GeomAbs_Cylinder: 1>, None), 'GeomAbs_Cone': (<GeomAbs_SurfaceType.GeomAbs_Cone: 2>, None), 'GeomAbs_Sphere': (<GeomAbs_SurfaceType.GeomAbs_Sphere: 3>, None), 'GeomAbs_Torus': (<GeomAbs_SurfaceType.GeomAbs_Torus: 4>, None), 'GeomAbs_BezierSurface': (<GeomAbs_SurfaceType.GeomAbs_BezierSurface: 5>, None), 'GeomAbs_BSplineSurface': (<GeomAbs_SurfaceType.GeomAbs_BSplineSurface: 6>, None), 'GeomAbs_SurfaceOfRevolution': (<GeomAbs_SurfaceType.GeomAbs_SurfaceOfRevolution: 7>, None), 'GeomAbs_SurfaceOfExtrusion': (<GeomAbs_SurfaceType.GeomAbs_SurfaceOfExtrusion: 8>, None), 'GeomAbs_OffsetSurface': (<GeomAbs_SurfaceType.GeomAbs_OffsetSurface: 9>, None), 'GeomAbs_OtherSurface': (<GeomAbs_SurfaceType.GeomAbs_OtherSurface: 10>, None)}
    __members__: dict # value = {'GeomAbs_Plane': <GeomAbs_SurfaceType.GeomAbs_Plane: 0>, 'GeomAbs_Cylinder': <GeomAbs_SurfaceType.GeomAbs_Cylinder: 1>, 'GeomAbs_Cone': <GeomAbs_SurfaceType.GeomAbs_Cone: 2>, 'GeomAbs_Sphere': <GeomAbs_SurfaceType.GeomAbs_Sphere: 3>, 'GeomAbs_Torus': <GeomAbs_SurfaceType.GeomAbs_Torus: 4>, 'GeomAbs_BezierSurface': <GeomAbs_SurfaceType.GeomAbs_BezierSurface: 5>, 'GeomAbs_BSplineSurface': <GeomAbs_SurfaceType.GeomAbs_BSplineSurface: 6>, 'GeomAbs_SurfaceOfRevolution': <GeomAbs_SurfaceType.GeomAbs_SurfaceOfRevolution: 7>, 'GeomAbs_SurfaceOfExtrusion': <GeomAbs_SurfaceType.GeomAbs_SurfaceOfExtrusion: 8>, 'GeomAbs_OffsetSurface': <GeomAbs_SurfaceType.GeomAbs_OffsetSurface: 9>, 'GeomAbs_OtherSurface': <GeomAbs_SurfaceType.GeomAbs_OtherSurface: 10>}
    pass
GeomAbs_Arc: OCP.GeomAbs.GeomAbs_JoinType # value = <GeomAbs_JoinType.GeomAbs_Arc: 0>
GeomAbs_BSplineCurve: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_BSplineCurve: 6>
GeomAbs_BSplineSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_BSplineSurface: 6>
GeomAbs_BezierCurve: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_BezierCurve: 5>
GeomAbs_BezierSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_BezierSurface: 5>
GeomAbs_C0: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_C0: 0>
GeomAbs_C1: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_C1: 2>
GeomAbs_C2: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_C2: 4>
GeomAbs_C3: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_C3: 5>
GeomAbs_CN: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_CN: 6>
GeomAbs_Circle: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Circle: 1>
GeomAbs_Cone: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Cone: 2>
GeomAbs_Cylinder: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Cylinder: 1>
GeomAbs_Ellipse: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Ellipse: 2>
GeomAbs_G1: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_G1: 1>
GeomAbs_G2: OCP.GeomAbs.GeomAbs_Shape # value = <GeomAbs_Shape.GeomAbs_G2: 3>
GeomAbs_Hyperbola: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Hyperbola: 3>
GeomAbs_Intersection: OCP.GeomAbs.GeomAbs_JoinType # value = <GeomAbs_JoinType.GeomAbs_Intersection: 2>
GeomAbs_IsoU: OCP.GeomAbs.GeomAbs_IsoType # value = <GeomAbs_IsoType.GeomAbs_IsoU: 0>
GeomAbs_IsoV: OCP.GeomAbs.GeomAbs_IsoType # value = <GeomAbs_IsoType.GeomAbs_IsoV: 1>
GeomAbs_Line: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Line: 0>
GeomAbs_NonUniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = <GeomAbs_BSplKnotDistribution.GeomAbs_NonUniform: 0>
GeomAbs_NoneIso: OCP.GeomAbs.GeomAbs_IsoType # value = <GeomAbs_IsoType.GeomAbs_NoneIso: 2>
GeomAbs_OffsetCurve: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_OffsetCurve: 7>
GeomAbs_OffsetSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_OffsetSurface: 9>
GeomAbs_OtherCurve: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_OtherCurve: 8>
GeomAbs_OtherSurface: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_OtherSurface: 10>
GeomAbs_Parabola: OCP.GeomAbs.GeomAbs_CurveType # value = <GeomAbs_CurveType.GeomAbs_Parabola: 4>
GeomAbs_PiecewiseBezier: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = <GeomAbs_BSplKnotDistribution.GeomAbs_PiecewiseBezier: 3>
GeomAbs_Plane: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Plane: 0>
GeomAbs_QuasiUniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = <GeomAbs_BSplKnotDistribution.GeomAbs_QuasiUniform: 2>
GeomAbs_Sphere: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Sphere: 3>
GeomAbs_SurfaceOfExtrusion: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_SurfaceOfExtrusion: 8>
GeomAbs_SurfaceOfRevolution: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_SurfaceOfRevolution: 7>
GeomAbs_Tangent: OCP.GeomAbs.GeomAbs_JoinType # value = <GeomAbs_JoinType.GeomAbs_Tangent: 1>
GeomAbs_Torus: OCP.GeomAbs.GeomAbs_SurfaceType # value = <GeomAbs_SurfaceType.GeomAbs_Torus: 4>
GeomAbs_Uniform: OCP.GeomAbs.GeomAbs_BSplKnotDistribution # value = <GeomAbs_BSplKnotDistribution.GeomAbs_Uniform: 1>
