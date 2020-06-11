import OCP.ElCLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
__all__  = [
"ElCLib"
]
class ElCLib():
    """
    Provides functions for basic geometric computations on elementary curves such as conics and lines in 2D and 3D space. This includes: - calculation of a point or derived vector on a 2D or 3D curve where: - the curve is provided by the gp package, or defined in reference form (as in the gp package), and - the point is defined by a parameter, - evaluation of the parameter corresponding to a point on a 2D or 3D curve from gp, - various elementary computations which allow you to position parameterized values within the period of a curve. Notes: - ElCLib stands for Elementary Curves Library. - If the curves provided by the gp package are not explicitly parameterized, they still have an implicit parameterization, analogous to that which they infer for the equivalent Geom or Geom2d curves.
    """
    @staticmethod
    def AdjustPeriodic_s(UFirst : float,ULast : float,Precision : float) -> Tuple[float, float]: 
        """
        Adjust U1 and U2 in the parametric range UFirst Ulast of a periodic curve, where ULast - UFirst is its period. To do this, this function: - sets U1 in the range [ UFirst, ULast ] by adding/removing the period to/from the value U1, then - sets U2 in the range [ U1, U1 + period ] by adding/removing the period to/from the value U2. Precision is used to test the equalities.
        """
    @staticmethod
    @overload
    def CircleD1_s(U : float,Pos : OCP.gp.gp_Ax2,Radius : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def CircleD1_s(U : float,Pos : OCP.gp.gp_Ax22d,Radius : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def CircleD2_s(U : float,Pos : OCP.gp.gp_Ax22d,Radius : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def CircleD2_s(U : float,Pos : OCP.gp.gp_Ax2,Radius : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def CircleD3_s(U : float,Pos : OCP.gp.gp_Ax22d,Radius : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def CircleD3_s(U : float,Pos : OCP.gp.gp_Ax2,Radius : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def CircleDN_s(U : float,Pos : OCP.gp.gp_Ax2,Radius : float,N : int) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def CircleDN_s(U : float,Pos : OCP.gp.gp_Ax22d,Radius : float,N : int) -> OCP.gp.gp_Vec2d: ...
    @staticmethod
    @overload
    def CircleParameter_s(Pos : OCP.gp.gp_Ax22d,P : OCP.gp.gp_Pnt2d) -> float: 
        """
        None

        Pos is the Axis of the Circle parametrization In the local coordinate system of the circle X (U) = Radius * Cos (U) Y (U) = Radius * Sin (U)
        """
    @staticmethod
    @overload
    def CircleParameter_s(Pos : OCP.gp.gp_Ax2,P : OCP.gp.gp_Pnt) -> float: ...
    @staticmethod
    @overload
    def CircleValue_s(U : float,Pos : OCP.gp.gp_Ax22d,Radius : float) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def CircleValue_s(U : float,Pos : OCP.gp.gp_Ax2,Radius : float) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def D1_s(U : float,E : OCP.gp.gp_Elips,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        For elementary curves (lines, circles and conics) from the gp package, computes: - the point P of parameter U, and - the first derivative vector V1 at this point. The results P and V1 are either: - a gp_Pnt point and a gp_Vec vector, for a curve in 3D space, or - a gp_Pnt2d point and a gp_Vec2d vector, for a curve in 2D space.

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def D1_s(U : float,H : OCP.gp.gp_Hypr2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,L : OCP.gp.gp_Lin,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,L : OCP.gp.gp_Lin2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,C : OCP.gp.gp_Circ2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,Prb : OCP.gp.gp_Parab2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,C : OCP.gp.gp_Circ,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,H : OCP.gp.gp_Hypr,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,E : OCP.gp.gp_Elips2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D1_s(U : float,Prb : OCP.gp.gp_Parab,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,E : OCP.gp.gp_Elips2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        For elementary curves (circles and conics) from the gp package, computes: - the point P of parameter U, and - the first and second derivative vectors V1 and V2 at this point. The results, P, V1 and V2, are either: - a gp_Pnt point and two gp_Vec vectors, for a curve in 3D space, or - a gp_Pnt2d point and two gp_Vec2d vectors, for a curve in 2D space.

        None

        None

        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def D2_s(U : float,C : OCP.gp.gp_Circ,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,E : OCP.gp.gp_Elips,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,Prb : OCP.gp.gp_Parab,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,H : OCP.gp.gp_Hypr2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,H : OCP.gp.gp_Hypr,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,C : OCP.gp.gp_Circ2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D2_s(U : float,Prb : OCP.gp.gp_Parab2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,H : OCP.gp.gp_Hypr2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        For elementary curves (circles, ellipses and hyperbolae) from the gp package, computes: - the point P of parameter U, and - the first, second and third derivative vectors V1, V2 and V3 at this point. The results, P, V1, V2 and V3, are either: - a gp_Pnt point and three gp_Vec vectors, for a curve in 3D space, or - a gp_Pnt2d point and three gp_Vec2d vectors, for a curve in 2D space.

        None

        None

        None

        None

        In the following functions N is the order of derivation and should be greater than 0
        """
    @staticmethod
    @overload
    def D3_s(U : float,C : OCP.gp.gp_Circ2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,E : OCP.gp.gp_Elips2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,E : OCP.gp.gp_Elips,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,C : OCP.gp.gp_Circ,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def D3_s(U : float,H : OCP.gp.gp_Hypr,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def DN_s(U : float,Prb : OCP.gp.gp_Parab,N : int) -> OCP.gp.gp_Vec: 
        """
        For elementary curves (lines, circles and conics) from the gp package, computes the vector corresponding to the Nth derivative at the point of parameter U. The result is either: - a gp_Vec vector for a curve in 3D space, or - a gp_Vec2d vector for a curve in 2D space. In the following functions N is the order of derivation and should be greater than 0

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def DN_s(U : float,C : OCP.gp.gp_Circ,N : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def DN_s(U : float,H : OCP.gp.gp_Hypr2d,N : int) -> OCP.gp.gp_Vec2d: ...
    @staticmethod
    @overload
    def DN_s(U : float,H : OCP.gp.gp_Hypr,N : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def DN_s(U : float,L : OCP.gp.gp_Lin,N : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def DN_s(U : float,E : OCP.gp.gp_Elips,N : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def DN_s(U : float,Prb : OCP.gp.gp_Parab2d,N : int) -> OCP.gp.gp_Vec2d: ...
    @staticmethod
    @overload
    def DN_s(U : float,L : OCP.gp.gp_Lin2d,N : int) -> OCP.gp.gp_Vec2d: ...
    @staticmethod
    @overload
    def DN_s(U : float,C : OCP.gp.gp_Circ2d,N : int) -> OCP.gp.gp_Vec2d: ...
    @staticmethod
    @overload
    def DN_s(U : float,E : OCP.gp.gp_Elips2d,N : int) -> OCP.gp.gp_Vec2d: ...
    @staticmethod
    @overload
    def EllipseD1_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def EllipseD1_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def EllipseD2_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def EllipseD2_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def EllipseD3_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def EllipseD3_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: ...
    @staticmethod
    @overload
    def EllipseDN_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,N : int) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def EllipseDN_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,N : int) -> OCP.gp.gp_Vec2d: ...
    @staticmethod
    @overload
    def EllipseParameter_s(Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt) -> float: 
        """
        None

        Pos is the Axis of the Ellipse parametrization In the local coordinate system of the Ellipse X (U) = MajorRadius * Cos (U) Y (U) = MinorRadius * Sin (U)
        """
    @staticmethod
    @overload
    def EllipseParameter_s(Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt2d) -> float: ...
    @staticmethod
    @overload
    def EllipseValue_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def EllipseValue_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def HyperbolaD1_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def HyperbolaD1_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def HyperbolaD2_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def HyperbolaD2_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def HyperbolaD3_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        In the following functions N is the order of derivation and should be greater than 0
        """
    @staticmethod
    @overload
    def HyperbolaD3_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def HyperbolaDN_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,N : int) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def HyperbolaDN_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,N : int) -> OCP.gp.gp_Vec2d: ...
    @staticmethod
    @overload
    def HyperbolaParameter_s(Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt) -> float: 
        """
        None

        Pos is the Axis of the Hyperbola parametrization In the local coordinate system of the Hyperbola X (U) = MajorRadius * Ch (U) Y (U) = MinorRadius * Sh (U)
        """
    @staticmethod
    @overload
    def HyperbolaParameter_s(Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float,P : OCP.gp.gp_Pnt2d) -> float: ...
    @staticmethod
    @overload
    def HyperbolaValue_s(U : float,Pos : OCP.gp.gp_Ax22d,MajorRadius : float,MinorRadius : float) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def HyperbolaValue_s(U : float,Pos : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    def InPeriod_s(U : float,UFirst : float,ULast : float) -> float: 
        """
        Return a value in the range <UFirst, ULast> by adding or removing the period <ULast - UFirst> to <U>. ATTENTION!!! It is expected but not checked that (ULast > UFirst)
        """
    @staticmethod
    @overload
    def LineD1_s(U : float,Pos : OCP.gp.gp_Ax2d,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def LineD1_s(U : float,Pos : OCP.gp.gp_Ax1,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def LineDN_s(U : float,Pos : OCP.gp.gp_Ax2d,N : int) -> OCP.gp.gp_Vec2d: 
        """
        In the following functions N is the order of derivation and should be greater than 0

        None
        """
    @staticmethod
    @overload
    def LineDN_s(U : float,Pos : OCP.gp.gp_Ax1,N : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def LineParameter_s(Pos : OCP.gp.gp_Ax2d,P : OCP.gp.gp_Pnt2d) -> float: 
        """
        None

        parametrization P (U) = L.Location() + U * L.Direction()
        """
    @staticmethod
    @overload
    def LineParameter_s(Pos : OCP.gp.gp_Ax1,P : OCP.gp.gp_Pnt) -> float: ...
    @staticmethod
    @overload
    def LineValue_s(U : float,Pos : OCP.gp.gp_Ax2d) -> OCP.gp.gp_Pnt2d: 
        """
        Curve evaluation The following basis functions compute the derivatives on elementary curves defined by their geometric characteristics. These functions can be called without constructing a conic from package gp. They are called by the previous functions. Example : A circle is defined by its position and its radius.

        None
        """
    @staticmethod
    @overload
    def LineValue_s(U : float,Pos : OCP.gp.gp_Ax1) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def ParabolaD1_s(U : float,Pos : OCP.gp.gp_Ax22d,Focal : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def ParabolaD1_s(U : float,Pos : OCP.gp.gp_Ax2,Focal : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def ParabolaD2_s(U : float,Pos : OCP.gp.gp_Ax22d,Focal : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def ParabolaD2_s(U : float,Pos : OCP.gp.gp_Ax2,Focal : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    @overload
    def ParabolaDN_s(U : float,Pos : OCP.gp.gp_Ax22d,Focal : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        None

        The following functions compute the parametric value corresponding to a given point on a elementary curve. The point should be on the curve.
        """
    @staticmethod
    @overload
    def ParabolaDN_s(U : float,Pos : OCP.gp.gp_Ax2,Focal : float,N : int) -> OCP.gp.gp_Vec: ...
    @staticmethod
    @overload
    def ParabolaParameter_s(Pos : OCP.gp.gp_Ax2,P : OCP.gp.gp_Pnt) -> float: 
        """
        None

        Pos is the mirror axis of the parabola parametrization In the local coordinate system of the parabola Y**2 = (2*P) * X where P is the distance between the focus and the directrix. The following functions build a 3d curve from a 2d curve at a given position defined with an Ax2.
        """
    @staticmethod
    @overload
    def ParabolaParameter_s(Pos : OCP.gp.gp_Ax22d,P : OCP.gp.gp_Pnt2d) -> float: ...
    @staticmethod
    @overload
    def ParabolaValue_s(U : float,Pos : OCP.gp.gp_Ax22d,Focal : float) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def ParabolaValue_s(U : float,Pos : OCP.gp.gp_Ax2,Focal : float) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def Parameter_s(L : OCP.gp.gp_Lin,P : OCP.gp.gp_Pnt) -> float: 
        """
        Computes the parameter value of the point P on the given curve. Note: In its local coordinate system, the parametric equation of the curve is given by the following: - for the line L: P(U) = Po + U*Vo where Po is the origin and Vo the unit vector of its positioning axis. - for the circle C: X(U) = Radius*Cos(U), Y(U) = Radius*Sin(U) - for the ellipse E: X(U) = MajorRadius*Cos(U). Y(U) = MinorRadius*Sin(U) - for the hyperbola H: X(U) = MajorRadius*Ch(U), Y(U) = MinorRadius*Sh(U) - for the parabola Prb: X(U) = U**2 / (2*p) Y(U) = U where p is the distance between the focus and the directrix. Warning The point P must be on the curve. These functions are not protected, however, and if point P is not on the curve, an exception may be raised.

        parametrization P (U) = L.Location() + U * L.Direction()

        None

        parametrization In the local coordinate system of the circle X (U) = Radius * Cos (U) Y (U) = Radius * Sin (U)

        None

        parametrization In the local coordinate system of the Ellipse X (U) = MajorRadius * Cos (U) Y (U) = MinorRadius * Sin (U)

        None

        parametrization In the local coordinate system of the Hyperbola X (U) = MajorRadius * Ch (U) Y (U) = MinorRadius * Sh (U)

        None

        parametrization In the local coordinate system of the parabola Y**2 = (2*P) * X where P is the distance between the focus and the directrix.
        """
    @staticmethod
    @overload
    def Parameter_s(E : OCP.gp.gp_Elips,P : OCP.gp.gp_Pnt) -> float: ...
    @staticmethod
    @overload
    def Parameter_s(H : OCP.gp.gp_Hypr2d,P : OCP.gp.gp_Pnt2d) -> float: ...
    @staticmethod
    @overload
    def Parameter_s(E : OCP.gp.gp_Elips2d,P : OCP.gp.gp_Pnt2d) -> float: ...
    @staticmethod
    @overload
    def Parameter_s(Prb : OCP.gp.gp_Parab,P : OCP.gp.gp_Pnt) -> float: ...
    @staticmethod
    @overload
    def Parameter_s(Prb : OCP.gp.gp_Parab2d,P : OCP.gp.gp_Pnt2d) -> float: ...
    @staticmethod
    @overload
    def Parameter_s(L : OCP.gp.gp_Lin2d,P : OCP.gp.gp_Pnt2d) -> float: ...
    @staticmethod
    @overload
    def Parameter_s(H : OCP.gp.gp_Hypr,P : OCP.gp.gp_Pnt) -> float: ...
    @staticmethod
    @overload
    def Parameter_s(C : OCP.gp.gp_Circ2d,P : OCP.gp.gp_Pnt2d) -> float: ...
    @staticmethod
    @overload
    def Parameter_s(C : OCP.gp.gp_Circ,P : OCP.gp.gp_Pnt) -> float: ...
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,V : OCP.gp.gp_Vec2d) -> OCP.gp.gp_Vec: 
        """
        None

        None

        None

        None

        None

        None

        None

        None

        None

        These functions build a 3D geometric entity from a 2D geometric entity. The "X Axis" and the "Y Axis" of the global coordinate system (i.e. 2D space) are lined up respectively with the "X Axis" and "Y Axis" of the 3D coordinate system, Pos.
        """
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,C : OCP.gp.gp_Circ2d) -> OCP.gp.gp_Circ: ...
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,L : OCP.gp.gp_Lin2d) -> OCP.gp.gp_Lin: ...
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,H : OCP.gp.gp_Hypr2d) -> OCP.gp.gp_Hypr: ...
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,A : OCP.gp.gp_Ax2d) -> OCP.gp.gp_Ax1: ...
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,P : OCP.gp.gp_Pnt2d) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,Prb : OCP.gp.gp_Parab2d) -> OCP.gp.gp_Parab: ...
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,A : OCP.gp.gp_Ax22d) -> OCP.gp.gp_Ax2: ...
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,E : OCP.gp.gp_Elips2d) -> OCP.gp.gp_Elips: ...
    @staticmethod
    @overload
    def To3d_s(Pos : OCP.gp.gp_Ax2,V : OCP.gp.gp_Dir2d) -> OCP.gp.gp_Dir: ...
    @staticmethod
    @overload
    def Value_s(U : float,C : OCP.gp.gp_Circ2d) -> OCP.gp.gp_Pnt2d: 
        """
        For elementary curves (lines, circles and conics) from the gp package, computes the point of parameter U. The result is either: - a gp_Pnt point for a curve in 3D space, or - a gp_Pnt2d point for a curve in 2D space.

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def Value_s(U : float,Prb : OCP.gp.gp_Parab) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def Value_s(U : float,Prb : OCP.gp.gp_Parab2d) -> OCP.gp.gp_Pnt2d: ...
    @staticmethod
    @overload
    def Value_s(U : float,H : OCP.gp.gp_Hypr) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def Value_s(U : float,L : OCP.gp.gp_Lin) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def Value_s(U : float,H : OCP.gp.gp_Hypr2d) -> OCP.gp.gp_Pnt2d: ...
    @staticmethod
    @overload
    def Value_s(U : float,C : OCP.gp.gp_Circ) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def Value_s(U : float,E : OCP.gp.gp_Elips2d) -> OCP.gp.gp_Pnt2d: ...
    @staticmethod
    @overload
    def Value_s(U : float,L : OCP.gp.gp_Lin2d) -> OCP.gp.gp_Pnt2d: ...
    @staticmethod
    @overload
    def Value_s(U : float,E : OCP.gp.gp_Elips) -> OCP.gp.gp_Pnt: ...
    def __init__(self) -> None: ...
    pass
