import OCP.GeomProjLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom2d
import OCP.Geom
import OCP.gp
__all__  = [
"GeomProjLib"
]
class GeomProjLib():
    """
    Projection of a curve on a surface.
    """
    @staticmethod
    @overload
    def Curve2d_s(C : OCP.Geom.Geom_Curve,First : float,Last : float,S : OCP.Geom.Geom_Surface,Tolerance : float) -> OCP.Geom2d.Geom2d_Curve: 
        """
        gives the 2d-curve of a 3d-curve lying on a surface ( uses GeomProjLib_ProjectedCurve ) The 3dCurve is taken between the parametrization range [First, Last] <Tolerance> is used as input if the projection needs an approximation. In this case, the reached tolerance is set in <Tolerance> as output. WARNING : if the projection has failed, this method returns a null Handle.

        gives the 2d-curve of a 3d-curve lying on a surface ( uses GeomProjLib_ProjectedCurve ) The 3dCurve is taken between the parametrization range [First, Last] <Tolerance> is used as input if the projection needs an approximation. In this case, the reached tolerance is set in <Tolerance> as output. WARNING : if the projection has failed, this method returns a null Handle.

        gives the 2d-curve of a 3d-curve lying on a surface ( uses GeomProjLib_ProjectedCurve ) The 3dCurve is taken between the parametrization range [First, Last] If the projection needs an approximation, Precision::PApproximation() is used. WARNING : if the projection has failed, this method returns a null Handle.

        gives the 2d-curve of a 3d-curve lying on a surface ( uses GeomProjLib_ProjectedCurve ). If the projection needs an approximation, Precision::PApproximation() is used. WARNING : if the projection has failed, this method returns a null Handle.

        gives the 2d-curve of a 3d-curve lying on a surface ( uses GeomProjLib_ProjectedCurve ). If the projection needs an approximation, Precision::PApproximation() is used. WARNING : if the projection has failed, this method returns a null Handle. can expand a little the bounds of surface

        gives the 2d-curve of a 3d-curve lying on a surface ( uses GeomProjLib_ProjectedCurve ). If the projection needs an approximation, Precision::PApproximation() is used. WARNING : if the projection has failed, this method returns a null Handle. can expand a little the bounds of surface
        """
    @staticmethod
    @overload
    def Curve2d_s(C : OCP.Geom.Geom_Curve,First : float,Last : float,S : OCP.Geom.Geom_Surface,UFirst : float,ULast : float,VFirst : float,VLast : float,Tolerance : float) -> OCP.Geom2d.Geom2d_Curve: ...
    @staticmethod
    @overload
    def Curve2d_s(C : OCP.Geom.Geom_Curve,S : OCP.Geom.Geom_Surface) -> OCP.Geom2d.Geom2d_Curve: ...
    @staticmethod
    @overload
    def Curve2d_s(C : OCP.Geom.Geom_Curve,First : float,Last : float,S : OCP.Geom.Geom_Surface) -> OCP.Geom2d.Geom2d_Curve: ...
    @staticmethod
    @overload
    def Curve2d_s(C : OCP.Geom.Geom_Curve,S : OCP.Geom.Geom_Surface,UDeb : float,UFin : float,VDeb : float,VFin : float,Tolerance : float) -> OCP.Geom2d.Geom2d_Curve: ...
    @staticmethod
    @overload
    def Curve2d_s(C : OCP.Geom.Geom_Curve,S : OCP.Geom.Geom_Surface,UDeb : float,UFin : float,VDeb : float,VFin : float) -> OCP.Geom2d.Geom2d_Curve: ...
    @staticmethod
    def ProjectOnPlane_s(Curve : OCP.Geom.Geom_Curve,Plane : OCP.Geom.Geom_Plane,Dir : OCP.gp.gp_Dir,KeepParametrization : bool) -> OCP.Geom.Geom_Curve: 
        """
        Constructs the 3d-curves from the projection of the curve <Curve> on the plane <Plane> along the direction <Dir>. If <KeepParametrization> is true, the parametrization of the Projected Curve <PC> will be the same as the parametrization of the initial curve <C>. It means: proj(C(u)) = PC(u) for each u. Otherwise, the parametrization may change.
        """
    @staticmethod
    def Project_s(C : OCP.Geom.Geom_Curve,S : OCP.Geom.Geom_Surface) -> OCP.Geom.Geom_Curve: 
        """
        Constructs the 3d-curve from the normal projection of the Curve <C> on the surface <S>. WARNING : if the projection has failed, returns a null Handle.
        """
    def __init__(self) -> None: ...
    pass
