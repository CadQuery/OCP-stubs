import OCP.IntAna2d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
__all__  = [
"IntAna2d_AnaIntersection",
"IntAna2d_Conic",
"IntAna2d_IntPoint",
"MyDirectPolynomialRoots",
"Coord_Ancien_Repere",
"Points_Confondus",
"Traitement_Points_Confondus"
]
class IntAna2d_AnaIntersection():
    """
    Implementation of the analytical intersection between: - two Lin2d, - two Circ2d, - a Lin2d and a Circ2d, - an element of gp (Lin2d, Circ2d, Elips2d, Parab2d, Hypr2d) and another conic. No tolerance is given for all the intersections: the tolerance will be the "precision machine".
    """
    def IdenticalElements(self) -> bool: 
        """
        For the intersection between an element of gp and a conic known by an implicit equation, the result will be TRUE if the element of gp verifies the implicit equation. For the intersection between two Lin2d or two Circ2d, the result will be TRUE if the elements are identical. The function returns FALSE in all the other cases.

        For the intersection between an element of gp and a conic known by an implicit equation, the result will be TRUE if the element of gp verifies the implicit equation. For the intersection between two Lin2d or two Circ2d, the result will be TRUE if the elements are identical. The function returns FALSE in all the other cases.
        """
    def IsDone(self) -> bool: 
        """
        Returns TRUE if the computation was succesfull.

        Returns TRUE if the computation was succesfull.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE when there is no intersection, i-e - no intersection point - the elements are not identical. The element may be parallel in this case.

        Returns TRUE when there is no intersection, i-e - no intersection point - the elements are not identical. The element may be parallel in this case.
        """
    def NbPoints(self) -> int: 
        """
        returns the number of IntPoint between the 2 curves.

        returns the number of IntPoint between the 2 curves.
        """
    def ParallelElements(self) -> bool: 
        """
        For the intersection between two Lin2d or two Circ2d, the function returns TRUE if the elements are parallel. The function returns FALSE in all the other cases.

        For the intersection between two Lin2d or two Circ2d, the function returns TRUE if the elements are parallel. The function returns FALSE in all the other cases.
        """
    @overload
    def Perform(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.gp.gp_Circ2d) -> None: 
        """
        Intersection between two lines.

        Intersection between two circles.

        Intersection between a line and a circle.

        Intersection between a line and a conic.

        Intersection between a circle and another conic.

        Intersection between an ellipse and another conic.

        Intersection between a parabola and another conic.

        Intersection between an hyperbola and another conic.
        """
    @overload
    def Perform(self,L1 : OCP.gp.gp_Lin2d,L2 : OCP.gp.gp_Lin2d) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ2d,Co : IntAna2d_Conic) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Parab2d,C : IntAna2d_Conic) -> None: ...
    @overload
    def Perform(self,L : OCP.gp.gp_Lin2d,C : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def Perform(self,H : OCP.gp.gp_Hypr2d,C : IntAna2d_Conic) -> None: ...
    @overload
    def Perform(self,E : OCP.gp.gp_Elips2d,C : IntAna2d_Conic) -> None: ...
    @overload
    def Perform(self,L : OCP.gp.gp_Lin2d,C : IntAna2d_Conic) -> None: ...
    def Point(self,N : int) -> IntAna2d_IntPoint: 
        """
        returns the intersection point of range N; If (N<=0) or (N>NbPoints), an exception is raised.

        returns the intersection point of range N; If (N<=0) or (N>NbPoints), an exception is raised.
        """
    @overload
    def __init__(self,E : OCP.gp.gp_Elips2d,C : IntAna2d_Conic) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Parab2d,C : IntAna2d_Conic) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr2d,C : IntAna2d_Conic) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,C : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d,Co : IntAna2d_Conic) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,C : IntAna2d_Conic) -> None: ...
    @overload
    def __init__(self,L1 : OCP.gp.gp_Lin2d,L2 : OCP.gp.gp_Lin2d) -> None: ...
    pass
class IntAna2d_Conic():
    """
    Definition of a conic by its implicit quadaratic equation: A.X**2 + B.Y**2 + 2.C.X*Y + 2.D.X + 2.E.Y + F = 0.
    """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float]: 
        """
        returns the coefficients of the polynomial equation wich defines the conic: A.X**2 + B.Y**2 + 2.C.X*Y + 2.D.X + 2.E.Y + F = 0.
        """
    def Grad(self,X : float,Y : float) -> OCP.gp.gp_XY: 
        """
        returns the value of the gradient of F at the point X,Y.
        """
    def NewCoefficients(self,Axis : OCP.gp.gp_Ax2d) -> Tuple[float, float, float, float, float, float]: 
        """
        Returns the coefficients of the polynomial equation ( written in the natural coordinates system ) A x x + B y y + 2 C x y + 2 D x + 2 E y + F in the local coordinates system defined by Axis
        """
    def ValAndGrad(self,X : float,Y : float,Grd : OCP.gp.gp_XY) -> Tuple[float]: 
        """
        Returns the value of the function and its gradient at the point X,Y.
        """
    def Value(self,X : float,Y : float) -> float: 
        """
        value of the function F at the point X,Y.
        """
    @overload
    def __init__(self,C : OCP.gp.gp_Hypr2d) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Parab2d) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Elips2d) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Lin2d) -> None: ...
    pass
class IntAna2d_IntPoint():
    """
    Geometrical intersection between two 2d elements.
    """
    def ParamOnFirst(self) -> float: 
        """
        Returns the parameter on the first element.

        Returns the parameter on the first element.
        """
    def ParamOnSecond(self) -> float: 
        """
        Returns the parameter on the second element. If the second element is an implicit curve, an exception is raised.

        Returns the parameter on the second element. If the second element is an implicit curve, an exception is raised.
        """
    def SecondIsImplicit(self) -> bool: 
        """
        Returns True if the second curve is implicit.

        Returns True if the second curve is implicit.
        """
    @overload
    def SetValue(self,X : float,Y : float,U1 : float,U2 : float) -> None: 
        """
        Set the values for a "non-implicit" point.

        Set the values for an "implicit" point.
        """
    @overload
    def SetValue(self,X : float,Y : float,U1 : float) -> None: ...
    def Value(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the geometric point.

        Returns the geometric point.
        """
    @overload
    def __init__(self,X : float,Y : float,U1 : float) -> None: ...
    @overload
    def __init__(self,X : float,Y : float,U1 : float,U2 : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class MyDirectPolynomialRoots():
    """
    None
    """
    def InfiniteRoots(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> float: 
        """
        None
        """
    def NbSolutions(self) -> int: 
        """
        None
        """
    def Value(self,i : int) -> float: 
        """
        None
        """
    @overload
    def __init__(self,A4 : float,A3 : float,A2 : float,A1 : float,A0 : float) -> None: ...
    @overload
    def __init__(self,A2 : float,A1 : float,A0 : float) -> None: ...
    pass
def Coord_Ancien_Repere(Ancien_X : float,Ancien_Y : float,Axe_Nouveau_Repere : OCP.gp.gp_Ax2d) -> None:
    """
    None
    """
def Points_Confondus(xa : float,ya : float,xb : float,yb : float) -> bool:
    """
    None
    """
def Traitement_Points_Confondus(nb_pts : int,pts : IntAna2d_IntPoint) -> None:
    """
    None
    """
