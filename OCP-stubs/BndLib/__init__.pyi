import OCP.BndLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.Geom2d
import OCP.Bnd
import OCP.gp
import OCP.Adaptor2d
__all__  = [
"BndLib",
"BndLib_Add2dCurve",
"BndLib_Add3dCurve",
"BndLib_AddSurface"
]
class BndLib():
    """
    The BndLib package provides functions to add a geometric primitive to a bounding box. Note: these functions work with gp objects, optionally limited by parameter values. If the curves and surfaces provided by the gp package are not explicitly parameterized, they still have an implicit parameterization, similar to that which they infer for the equivalent Geom or Geom2d objects. Add : Package to compute the bounding boxes for elementary objects from gp in 2d and 3d .
    """
    @staticmethod
    @overload
    def Add_s(C : OCP.gp.gp_Circ,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: 
        """
        Bounding box for a surface trimmed or not Adds the segment of the line L limited by the two parameter values P1 and P2, to the bounding box B, and then enlarges B by the tolerance value Tol. Tol is the tolerance value to enlarge the minimun and maximum dimension P1 and P2 may represent infinite values. Exceptions Standard_Failure if P1 and P2 are either two negative infinite real numbers, or two positive infinite real numbers.

        None

        None

        P2-P1 can be in [0,2*pi]

        None

        Adds the circle C, or the arc of the circle C limited by the two parameter values P1 and P2, to the bounding box B, and then enlarges B by the tolerance value Tol. P2-P1 can be in [0,2*pi]

        None

        P2-P1 can be in [0,2*pi]

        None

        Adds the ellipse E, or the arc of the ellipse E limited by the two parameter values P1 and P2, to the bounding box B, and then enlarges B by the tolerance value Tol. P2-P1 can be in [0,2*pi]

        None

        Adds the arc of the parabola P limited by the two parameter values P1 and P2, to the bounding box B, and then enlarges B by the tolerance value Tol. P1 and P2 may represent infinite values. Exceptions Standard_Failure if P1 and P2 are either two negative infinite real numbers, or two positive infinite real numbers.

        None

        Adds the arc of the branch of hyperbola H limited by the two parameter values P1 and P2, to the bounding box B, and then enlarges B by the tolerance value Tol. P1 and P2 may represent infinite values. Exceptions Standard_Failure if P1 and P2 are either two negative infinite real numbers, or two positive infinite real numbers.

        UMax -UMin can be in [0,2*pi]

        Adds to the bounding box B, the patch of the cylinder S limited - in the v parametric direction, by the two parameter values VMin and VMax - and optionally in the u parametric direction, by the two parameter values UMin and UMax. B is then enlarged by the tolerance value Tol. VMin and VMax may represent infinite values. Exceptions Standard_Failure if VMin and VMax are either two negative infinite real numbers, or two positive infinite real numbers.

        UMax-UMin can be in [0,2*pi]

        Adds to the bounding box B, the patch of the cone S limited - in the v parametric direction, by the two parameter values VMin and VMax - and optionally in the u parametric direction, by the two parameter values UMin and UMax, B is then enlarged by the tolerance value Tol. VMin and VMax may represent infinite values. Exceptions Standard_Failure if VMin and VMax are either two negative infinite real numbers, or two positive infinite real numbers.

        None

        Adds to the bounding box B the sphere S, or - the patch of the sphere S, limited in the u parametric direction, by the two parameter values UMin and UMax, and in the v parametric direction, by the two parameter values VMin and VMax. B is then enlarged by the tolerance value Tol. UMax-UMin can be in [0,2*pi] VMin,VMax can be [-pi/2,pi/2]

        None

        Adds to the bounding box B - the torus S, or - the patch of the torus S, limited in the u parametric direction, by the two parameter values UMin and UMax, and in the v parametric direction, by the two parameter values VMin and VMax. B is then enlarged by the tolerance value Tol. UMax-UMin can be in [0,2*pi], VMin,VMax can be [-pi/2,pi/2]
        """
    @staticmethod
    @overload
    def Add_s(S : OCP.gp.gp_Cone,VMin : float,VMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.gp.gp_Elips,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(L : OCP.gp.gp_Lin,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(S : OCP.gp.gp_Sphere,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(P : OCP.gp.gp_Parab2d,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.gp.gp_Elips,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(L : OCP.gp.gp_Lin2d,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def Add_s(S : OCP.gp.gp_Sphere,UMin : float,UMax : float,VMin : float,VMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(S : OCP.gp.gp_Cylinder,VMin : float,VMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(H : OCP.gp.gp_Hypr,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.gp.gp_Circ,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(S : OCP.gp.gp_Cylinder,UMin : float,UMax : float,VMin : float,VMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.gp.gp_Elips2d,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def Add_s(H : OCP.gp.gp_Hypr2d,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def Add_s(P : OCP.gp.gp_Torus,UMin : float,UMax : float,VMin : float,VMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.gp.gp_Circ2d,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.gp.gp_Circ2d,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.gp.gp_Elips2d,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def Add_s(P : OCP.gp.gp_Torus,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(S : OCP.gp.gp_Cone,UMin : float,UMax : float,VMin : float,VMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(P : OCP.gp.gp_Parab,P1 : float,P2 : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    def __init__(self) -> None: ...
    pass
class BndLib_Add2dCurve():
    """
    Computes the bounding box for a curve in 2d . Functions to add a 2D curve to a bounding box. The 2D curve is defined from a Geom2d curve.
    """
    @staticmethod
    def AddOptimal_s(C : OCP.Geom2d.Geom2d_Curve,U1 : float,U2 : float,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: 
        """
        Adds to the bounding box B the part of curve C B is then enlarged by the tolerance value Tol. U1, U2 - the parametric range to comute the bounding box; Note: depending on the type of curve, one of the following algorithms is used to include it in the bounding box B: - an exact analytical if C is built from a line, a circle or a conic curve, - numerical calculation of bounding box sizes, based on minimization algorithm, for other types of curve If Tol = < Precision::PConfusion(), Precision::PConfusion is used as tolerance for calculation
        """
    @staticmethod
    @overload
    def Add_s(C : OCP.Geom2d.Geom2d_Curve,Tol : float,Box : OCP.Bnd.Bnd_Box2d) -> None: 
        """
        Adds to the bounding box B the curve C B is then enlarged by the tolerance value Tol. Note: depending on the type of curve, one of the following representations of the curve C is used to include it in the bounding box B: - an exact representation if C is built from a line, a circle or a conic curve, - the poles of the curve if C is built from a Bezier curve or a BSpline curve, - if not, the points of an approximation of the curve C. Warning C is an adapted curve, that is, an object which is an interface between: - the services provided by a 2D curve from the package Geom2d - and those required of the curve by the computation algorithm. The adapted curve is created in the following way: Handle(Geom2d_Curve) mycurve = ... ; Geom2dAdaptor_Curve C(mycurve); The bounding box B is then enlarged by adding it: Bnd_Box2d B; // ... Standard_Real Tol = ... ; Add2dCurve::Add ( C, Tol, B ); Exceptions Standard_Failure if the curve is built from: - a Geom_Line, or - a Geom_Parabola, or - a Geom_Hyperbola, and P1 and P2 are either two negative infinite real numbers, or two positive infinite real numbers.

        Adds to the bounding box Bthe arc of the curve C limited by the two parameter values P1 and P2. B is then enlarged by the tolerance value Tol. Note: depending on the type of curve, one of the following representations of the curve C is used to include it in the bounding box B: - an exact representation if C is built from a line, a circle or a conic curve, - the poles of the curve if C is built from a Bezier curve or a BSpline curve, - if not, the points of an approximation of the curve C. Warning C is an adapted curve, that is, an object which is an interface between: - the services provided by a 2D curve from the package Geom2d - and those required of the curve by the computation algorithm. The adapted curve is created in the following way: Handle(Geom2d_Curve) mycurve = ... ; Geom2dAdaptor_Curve C(mycurve); The bounding box B is then enlarged by adding it: Bnd_Box2d B; // ... Standard_Real Tol = ... ; Add2dCurve::Add ( C, Tol, B ); Exceptions Standard_Failure if the curve is built from: - a Geom_Line, or - a Geom_Parabola, or - a Geom_Hyperbola, and P1 and P2 are either two negative infinite real numbers, or two positive infinite real numbers.

        Adds to the bounding box B the curve C B is then enlarged by the tolerance value Tol. Note: depending on the type of curve, one of the following representations of the curve C is used to include it in the bounding box B: - an exact representation if C is built from a line, a circle or a conic curve, - the poles of the curve if C is built from a Bezier curve or a BSpline curve, - if not, the points of an approximation of the curve C.

        Adds to the bounding box B the part of curve C B is then enlarged by the tolerance value Tol. U1, U2 - the parametric range to comute the bounding box; Note: depending on the type of curve, one of the following representations of the curve C is used to include it in the bounding box B: - an exact representation if C is built from a line, a circle or a conic curve, - the poles of the curve if C is built from a Bezier curve or a BSpline curve, - if not, the points of an approximation of the curve C.
        """
    @staticmethod
    @overload
    def Add_s(C : OCP.Geom2d.Geom2d_Curve,U1 : float,U2 : float,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U1 : float,U2 : float,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Tol : float,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    def __init__(self) -> None: ...
    pass
class BndLib_Add3dCurve():
    """
    Computes the bounding box for a curve in 3d. Functions to add a 3D curve to a bounding box. The 3D curve is defined from a Geom curve.
    """
    @staticmethod
    def AddGenCurv_s(C : OCP.Adaptor3d.Adaptor3d_Curve,UMin : float,UMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: 
        """
        Adds to the bounding box B the curve C using numerical minimization algorithms This method is used in AddOptimal for not analytical curves. if Tol < Precision::Confusion(), Precision:;Confusion is used as computation tolerance
        """
    @staticmethod
    @overload
    def AddOptimal_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: 
        """
        Adds to the bounding box B the curve C These methods use more precise algorithms for building bnd box then methods Add(...)

        None
        """
    @staticmethod
    @overload
    def AddOptimal_s(C : OCP.Adaptor3d.Adaptor3d_Curve,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: 
        """
        Adds to the bounding box B the curve C B is then enlarged by the tolerance value Tol. Note: depending on the type of curve, one of the following representations of the curve C is used to include it in the bounding box B: - an exact representation if C is built from a line, a circle or a conic curve, - the poles of the curve if C is built from a Bezier curve or a BSpline curve, if not, the points of an approximation of the curve C. Warning C is an adapted curve, that is, an object which is an interface between: - the services provided by a 3D curve from the package Geom - and those required of the curve by the computation algorithm. The adapted curve is created in the following way: Handle(Geom_Curve) mycurve = ... ; GeomAdaptor_Curve C(mycurve); The bounding box B is then enlarged by adding it: Bnd_Box B; // ... Standard_Real Tol = ... ; Add3dCurve::Add ( C, Tol, B ); Exceptions Standard_Failure if the curve is built from: - a Geom_Line, or - a Geom_Parabola, or - a Geom_Hyperbola, and P1 and P2 are either two negative infinite real numbers, or two positive infinite real numbers.

        Adds to the bounding box B the curve C the arc of the curve C limited by the two parameter values P1 and P2. Note: depending on the type of curve, one of the following representations of the curve C is used to include it in the bounding box B: - an exact representation if C is built from a line, a circle or a conic curve, - the poles of the curve if C is built from a Bezier curve or a BSpline curve, if not, the points of an approximation of the curve C. Warning C is an adapted curve, that is, an object which is an interface between: - the services provided by a 3D curve from the package Geom - and those required of the curve by the computation algorithm. The adapted curve is created in the following way: Handle(Geom_Curve) mycurve = ... ; GeomAdaptor_Curve C(mycurve); The bounding box B is then enlarged by adding it: Bnd_Box B; // ... Standard_Real Tol = ... ; Add3dCurve::Add ( C, Tol, B ); Exceptions Standard_Failure if the curve is built from: - a Geom_Line, or - a Geom_Parabola, or - a Geom_Hyperbola, and P1 and P2 are either two negative infinite real numbers, or two positive infinite real numbers.
        """
    @staticmethod
    @overload
    def Add_s(C : OCP.Adaptor3d.Adaptor3d_Curve,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    def __init__(self) -> None: ...
    pass
class BndLib_AddSurface():
    """
    computes the box from a surface Functions to add a surface to a bounding box. The surface is defined from a Geom surface.
    """
    @staticmethod
    def AddGenSurf_s(S : OCP.Adaptor3d.Adaptor3d_Surface,UMin : float,UMax : float,VMin : float,VMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: 
        """
        Adds to the bounding box B the surface S using numerical minimization algorithms This method is used in AddOptimal for not analytical surfaces and torus. if Tol < Precision::Confusion(), Precision::Confusion is used as computation tolerance
        """
    @staticmethod
    @overload
    def AddOptimal_s(S : OCP.Adaptor3d.Adaptor3d_Surface,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: 
        """
        Adds the surface S to the bounding box B. This algorith builds precise bounding box

        None
        """
    @staticmethod
    @overload
    def AddOptimal_s(S : OCP.Adaptor3d.Adaptor3d_Surface,UMin : float,UMax : float,VMin : float,VMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def Add_s(S : OCP.Adaptor3d.Adaptor3d_Surface,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: 
        """
        Adds to the bounding box B the surface S B is then enlarged by the tolerance value Tol. Note: depending on the type of curve, one of the following representations of the surface S is used to include it in the bounding box B: - an exact representation if S is built from a plane, a cylinder, a cone, a sphere or a torus, - the poles of the surface if S is built from a Bezier surface or a BSpline surface, - the points of an approximation of the surface S in cases other than offset surfaces; - in the case of an offset surface, the basis surface is first included according to the previous rules; then the bounding box is enlarged by the offset value. Warning Do not use these functions to add a non-finite surface to the bounding box B. If UMin, UMax, VMin or VMax is an infinite value B will become WholeSpace. S is an adapted surface, that is, an object which is an interface between: - the services provided by a surface from the package Geom - and those required of the surface by the computation algorithm. The adapted surface is created in the following way: Handle(Geom_Surface) mysurface = ... ; GeomAdaptor_Surface S(mysurface); The bounding box B is then enlarged by adding this surface: Bnd_Box B; // ... Standard_Real Tol = ... ; AddSurface::Add ( S, Tol, B );

        Adds to the bounding box B the surface S the patch of the surface S limited in the u parametric direction by the two parameter values UMin, UMax, and in the v parametric direction by the two parameter values VMin, VMax. Note: depending on the type of curve, one of the following representations of the surface S is used to include it in the bounding box B: - an exact representation if S is built from a plane, a cylinder, a cone, a sphere or a torus, - the poles of the surface if S is built from a Bezier surface or a BSpline surface, - the points of an approximation of the surface S in cases other than offset surfaces; - in the case of an offset surface, the basis surface is first included according to the previous rules; then the bounding box is enlarged by the offset value. Warning Do not use these functions to add a non-finite surface to the bounding box B. If UMin, UMax, VMin or VMax is an infinite value B will become WholeSpace. S is an adapted surface, that is, an object which is an interface between: - the services provided by a surface from the package Geom - and those required of the surface by the computation algorithm. The adapted surface is created in the following way: Handle(Geom_Surface) mysurface = ... ; GeomAdaptor_Surface S(mysurface); The bounding box B is then enlarged by adding this surface: Bnd_Box B; // ... Standard_Real Tol = ... ; AddSurface::Add ( S, Tol, B );
        """
    @staticmethod
    @overload
    def Add_s(S : OCP.Adaptor3d.Adaptor3d_Surface,UMin : float,UMax : float,VMin : float,VMax : float,Tol : float,B : OCP.Bnd.Bnd_Box) -> None: ...
    def __init__(self) -> None: ...
    pass
