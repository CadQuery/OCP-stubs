import OCP.ElSLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
__all__  = [
"ElSLib"
]
class ElSLib():
    """
    Provides functions for basic geometric computation on elementary surfaces. This includes: - calculation of a point or derived vector on a surface where the surface is provided by the gp package, or defined in canonical form (as in the gp package), and the point is defined with a parameter, - evaluation of the parameters corresponding to a point on an elementary surface from gp, - calculation of isoparametric curves on an elementary surface defined in canonical form (as in the gp package). Notes: - ElSLib stands for Elementary Surfaces Library. - If the surfaces provided by the gp package are not explicitly parameterized, they still have an implicit parameterization, similar to that which they infer on the equivalent Geom surfaces. Note: ElSLib stands for Elementary Surfaces Library.
    """
    @staticmethod
    def ConeD0_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,SAngle : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def ConeD1_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,SAngle : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def ConeD2_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,SAngle : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def ConeD3_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,SAngle : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec,Vuuu : OCP.gp.gp_Vec,Vvvv : OCP.gp.gp_Vec,Vuuv : OCP.gp.gp_Vec,Vuvv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def ConeDN_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,SAngle : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def ConeParameters_s(Pos : OCP.gp.gp_Ax3,Radius : float,SAngle : float,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        parametrization P (U, V) = Location + V * ZDirection + (Radius + V * Tan (SemiAngle)) * (Cos(U) * XDirection + Sin(U) * YDirection)
        """
    @staticmethod
    def ConeUIso_s(Pos : OCP.gp.gp_Ax3,Radius : float,SAngle : float,U : float) -> OCP.gp.gp_Lin: 
        """
        compute the U Isoparametric gp_Lin of the cone.
        """
    @staticmethod
    def ConeVIso_s(Pos : OCP.gp.gp_Ax3,Radius : float,SAngle : float,V : float) -> OCP.gp.gp_Circ: 
        """
        compute the V Isoparametric gp_Circ of the cone.
        """
    @staticmethod
    def ConeValue_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,SAngle : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @staticmethod
    def CylinderD0_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def CylinderD1_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def CylinderD2_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def CylinderD3_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec,Vuuu : OCP.gp.gp_Vec,Vvvv : OCP.gp.gp_Vec,Vuuv : OCP.gp.gp_Vec,Vuvv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def CylinderDN_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def CylinderParameters_s(Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        parametrization P (U, V) = Location + V * ZDirection + Radius * (Cos(U) * XDirection + Sin (U) * YDirection)
        """
    @staticmethod
    def CylinderUIso_s(Pos : OCP.gp.gp_Ax3,Radius : float,U : float) -> OCP.gp.gp_Lin: 
        """
        compute the U Isoparametric gp_Lin of the cylinder.
        """
    @staticmethod
    def CylinderVIso_s(Pos : OCP.gp.gp_Ax3,Radius : float,V : float) -> OCP.gp.gp_Circ: 
        """
        compute the V Isoparametric gp_Circ of the cylinder.
        """
    @staticmethod
    def CylinderValue_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @staticmethod
    @overload
    def D0_s(U : float,V : float,Pl : OCP.gp.gp_Pln,P : OCP.gp.gp_Pnt) -> None: 
        """
        For elementary surfaces from the gp package (planes, cones, cylinders, spheres and tori), computes the point P of parameters (U, V).inline

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def D0_s(U : float,V : float,C : OCP.gp.gp_Cone,P : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def D0_s(U : float,V : float,C : OCP.gp.gp_Cylinder,P : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def D0_s(U : float,V : float,S : OCP.gp.gp_Sphere,P : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def D0_s(U : float,V : float,T : OCP.gp.gp_Torus,P : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,V : float,Pl : OCP.gp.gp_Pln,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: 
        """
        For elementary surfaces from the gp package (planes, cones, cylinders, spheres and tori), computes: - the point P of parameters (U, V), and - the first derivative vectors Vu and Vv at this point in the u and v parametric directions respectively.

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def D1_s(U : float,V : float,T : OCP.gp.gp_Torus,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,V : float,C : OCP.gp.gp_Cone,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,V : float,S : OCP.gp.gp_Sphere,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,V : float,C : OCP.gp.gp_Cylinder,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,V : float,C : OCP.gp.gp_Cone,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec) -> None: 
        """
        For elementary surfaces from the gp package (cones, cylinders, spheres and tori), computes: - the point P of parameters (U, V), and - the first derivative vectors Vu and Vv at this point in the u and v parametric directions respectively, and - the second derivative vectors Vuu, Vvv and Vuv at this point.

        None

        None

        None
        """
    @staticmethod
    @overload
    def D2_s(U : float,V : float,T : OCP.gp.gp_Torus,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,V : float,C : OCP.gp.gp_Cylinder,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,V : float,S : OCP.gp.gp_Sphere,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,V : float,C : OCP.gp.gp_Cylinder,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec,Vuuu : OCP.gp.gp_Vec,Vvvv : OCP.gp.gp_Vec,Vuuv : OCP.gp.gp_Vec,Vuvv : OCP.gp.gp_Vec) -> None: 
        """
        For elementary surfaces from the gp package (cones, cylinders, spheres and tori), computes: - the point P of parameters (U,V), and - the first derivative vectors Vu and Vv at this point in the u and v parametric directions respectively, and - the second derivative vectors Vuu, Vvv and Vuv at this point, and - the third derivative vectors Vuuu, Vvvv, Vuuv and Vuvv at this point.

        None

        None

        Surface evaluation The following functions compute the point and the derivatives on elementary surfaces defined with their geometric characterisitics. You don't need to create the surface to use these functions. These functions are called by the previous ones. Example : A cylinder is defined with its position and its radius.
        """
    @staticmethod
    @overload
    def D3_s(U : float,V : float,C : OCP.gp.gp_Cone,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec,Vuuu : OCP.gp.gp_Vec,Vvvv : OCP.gp.gp_Vec,Vuuv : OCP.gp.gp_Vec,Vuvv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,V : float,S : OCP.gp.gp_Sphere,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec,Vuuu : OCP.gp.gp_Vec,Vvvv : OCP.gp.gp_Vec,Vuuv : OCP.gp.gp_Vec,Vuvv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,V : float,T : OCP.gp.gp_Torus,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec,Vuuu : OCP.gp.gp_Vec,Vvvv : OCP.gp.gp_Vec,Vuuv : OCP.gp.gp_Vec,Vuvv : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def DN_s(U : float,V : float,S : OCP.gp.gp_Sphere,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        For elementary surfaces from the gp package (planes, cones, cylinders, spheres and tori), computes the derivative vector of order Nu and Nv in the u and v parametric directions respectively, at the point of parameters (U, V).

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def DN_s(U : float,V : float,C : OCP.gp.gp_Cone,Nu : int,Nv : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def DN_s(U : float,V : float,T : OCP.gp.gp_Torus,Nu : int,Nv : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def DN_s(U : float,V : float,C : OCP.gp.gp_Cylinder,Nu : int,Nv : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def DN_s(U : float,V : float,Pl : OCP.gp.gp_Pln,Nu : int,Nv : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def Parameters_s(T : OCP.gp.gp_Torus,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        parametrization P (U, V) = Pl.Location() + U * Pl.XDirection() + V * Pl.YDirection()

        parametrization P (U, V) = Location + V * ZDirection + Radius * (Cos(U) * XDirection + Sin (U) * YDirection)

        parametrization P (U, V) = Location + V * ZDirection + (Radius + V * Tan (SemiAngle)) * (Cos(U) * XDirection + Sin(U) * YDirection)

        parametrization P (U, V) = Location + Radius * Cos (V) * (Cos (U) * XDirection + Sin (U) * YDirection) + Radius * Sin (V) * ZDirection

        parametrization P (U, V) = Location + (MajorRadius + MinorRadius * Cos(U)) * (Cos(V) * XDirection - Sin(V) * YDirection) + MinorRadius * Sin(U) * ZDirection
        """
    @staticmethod
    @overload
    def Parameters_s(Pl : OCP.gp.gp_Pln,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: ...
    @staticmethod
    @overload
    def Parameters_s(C : OCP.gp.gp_Cylinder,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: ...
    @staticmethod
    @overload
    def Parameters_s(C : OCP.gp.gp_Cone,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: ...
    @staticmethod
    @overload
    def Parameters_s(S : OCP.gp.gp_Sphere,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: ...
    @staticmethod
    def PlaneD0_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def PlaneD1_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def PlaneDN_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def PlaneParameters_s(Pos : OCP.gp.gp_Ax3,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        parametrization P (U, V) = Pl.Location() + U * Pl.XDirection() + V * Pl.YDirection()
        """
    @staticmethod
    def PlaneUIso_s(Pos : OCP.gp.gp_Ax3,U : float) -> OCP.gp.gp_Lin: 
        """
        compute the U Isoparametric gp_Lin of the plane.
        """
    @staticmethod
    def PlaneVIso_s(Pos : OCP.gp.gp_Ax3,V : float) -> OCP.gp.gp_Lin: 
        """
        compute the V Isoparametric gp_Lin of the plane.
        """
    @staticmethod
    def PlaneValue_s(U : float,V : float,Pos : OCP.gp.gp_Ax3) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @staticmethod
    def SphereD0_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def SphereD1_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def SphereD2_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def SphereD3_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec,Vuuu : OCP.gp.gp_Vec,Vvvv : OCP.gp.gp_Vec,Vuuv : OCP.gp.gp_Vec,Vuvv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def SphereDN_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def SphereParameters_s(Pos : OCP.gp.gp_Ax3,Radius : float,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        parametrization P (U, V) = Location + Radius * Cos (V) * (Cos (U) * XDirection + Sin (U) * YDirection) + Radius * Sin (V) * ZDirection
        """
    @staticmethod
    def SphereUIso_s(Pos : OCP.gp.gp_Ax3,Radius : float,U : float) -> OCP.gp.gp_Circ: 
        """
        compute the U Isoparametric gp_Circ of the sphere, (the meridian is not trimmed).
        """
    @staticmethod
    def SphereVIso_s(Pos : OCP.gp.gp_Ax3,Radius : float,V : float) -> OCP.gp.gp_Circ: 
        """
        compute the V Isoparametric gp_Circ of the sphere, (the meridian is not trimmed).
        """
    @staticmethod
    def SphereValue_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,Radius : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @staticmethod
    def TorusD0_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def TorusD1_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def TorusD2_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def TorusD3_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt,Vu : OCP.gp.gp_Vec,Vv : OCP.gp.gp_Vec,Vuu : OCP.gp.gp_Vec,Vvv : OCP.gp.gp_Vec,Vuv : OCP.gp.gp_Vec,Vuuu : OCP.gp.gp_Vec,Vvvv : OCP.gp.gp_Vec,Vuuv : OCP.gp.gp_Vec,Vuvv : OCP.gp.gp_Vec) -> None: 
        """
        The following functions compute the parametric values corresponding to a given point on a elementary surface. The point should be on the surface.
        """
    @staticmethod
    def TorusDN_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def TorusParameters_s(Pos : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        parametrization P (U, V) = Location + (MajorRadius + MinorRadius * Cos(U)) * (Cos(V) * XDirection - Sin(V) * YDirection) + MinorRadius * Sin(U) * ZDirection
        """
    @staticmethod
    def TorusUIso_s(Pos : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float,U : float) -> OCP.gp.gp_Circ: 
        """
        compute the U Isoparametric gp_Circ of the torus.
        """
    @staticmethod
    def TorusVIso_s(Pos : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float,V : float) -> OCP.gp.gp_Circ: 
        """
        compute the V Isoparametric gp_Circ of the torus.
        """
    @staticmethod
    def TorusValue_s(U : float,V : float,Pos : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @staticmethod
    @overload
    def Value_s(U : float,V : float,T : OCP.gp.gp_Torus) -> OCP.gp.gp_Pnt: 
        """
        For elementary surfaces from the gp package (planes, cones, cylinders, spheres and tori), computes the point of parameters (U, V).

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def Value_s(U : float,V : float,S : OCP.gp.gp_Sphere) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def Value_s(U : float,V : float,C : OCP.gp.gp_Cylinder) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def Value_s(U : float,V : float,C : OCP.gp.gp_Cone) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def Value_s(U : float,V : float,Pl : OCP.gp.gp_Pln) -> OCP.gp.gp_Pnt: ...
    def __init__(self) -> None: ...
    pass
