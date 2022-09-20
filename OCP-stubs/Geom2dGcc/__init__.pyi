import OCP.Geom2dGcc
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom2dAdaptor
import OCP.math
import OCP.gp
import OCP.Geom2d
import OCP.GccAna
import OCP.GccEnt
__all__  = [
"Geom2dGcc",
"Geom2dGcc_Circ2d2TanOn",
"Geom2dGcc_Circ2d2TanOnGeo",
"Geom2dGcc_Circ2d2TanOnIter",
"Geom2dGcc_Circ2d2TanRad",
"Geom2dGcc_Circ2d2TanRadGeo",
"Geom2dGcc_Circ2d3Tan",
"Geom2dGcc_Circ2d3TanIter",
"Geom2dGcc_Circ2dTanCen",
"Geom2dGcc_Circ2dTanCenGeo",
"Geom2dGcc_Circ2dTanOnRad",
"Geom2dGcc_Circ2dTanOnRadGeo",
"Geom2dGcc_CurveTool",
"Geom2dGcc_FunctionTanCirCu",
"Geom2dGcc_FunctionTanCuCu",
"Geom2dGcc_FunctionTanCuCuCu",
"Geom2dGcc_FunctionTanCuCuOnCu",
"Geom2dGcc_FunctionTanCuPnt",
"Geom2dGcc_FunctionTanObl",
"Geom2dGcc_IsParallel",
"Geom2dGcc_Lin2d2Tan",
"Geom2dGcc_Lin2d2TanIter",
"Geom2dGcc_Lin2dTanObl",
"Geom2dGcc_Lin2dTanOblIter",
"Geom2dGcc_QCurve",
"Geom2dGcc_QualifiedCurve",
"Geom2dGcc_Type1",
"Geom2dGcc_Type2",
"Geom2dGcc_Type3",
"Geom2dGcc_CiCiCu",
"Geom2dGcc_CiCu",
"Geom2dGcc_CiCuCu",
"Geom2dGcc_CiCuOnCi",
"Geom2dGcc_CiCuOnCu",
"Geom2dGcc_CiCuOnLi",
"Geom2dGcc_CiLiCu",
"Geom2dGcc_CuCu",
"Geom2dGcc_CuCuCu",
"Geom2dGcc_CuCuOnCi",
"Geom2dGcc_CuCuOnCu",
"Geom2dGcc_CuCuOnLi",
"Geom2dGcc_CuPtOnCi",
"Geom2dGcc_CuPtOnCu",
"Geom2dGcc_CuPtOnLi",
"Geom2dGcc_LiCuCu",
"Geom2dGcc_LiCuOnCi",
"Geom2dGcc_LiCuOnCu",
"Geom2dGcc_LiCuOnLi",
"Geom2dGcc_LiLiCu"
]
class Geom2dGcc():
    """
    The Geom2dGcc package describes qualified 2D curves used in the construction of constrained geometric objects by an algorithm provided by the Geom2dGcc package. A qualified 2D curve is a curve with a qualifier which specifies whether the solution of a construction algorithm using the qualified curve (as an argument): - encloses the curve, or - is enclosed by the curve, or - is built so that both the curve and this solution are external to one another, or - is undefined (all solutions apply). These package methods provide simpler functions to construct a qualified curve. Note: the interior of a curve is defined as the left-hand side of the curve in relation to its orientation.
    """
    @staticmethod
    def Enclosed_s(Obj : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve: 
        """
        Constructs such a qualified curve that the solution computed by a construction algorithm using the qualified curve is enclosed by the curve. Warning Obj is an adapted curve, i.e. an object which is an interface between: - the services provided by a 2D curve from the package Geom2d, - and those required on the curve by a computation algorithm. The adapted curve is created in the following way: Handle(Geom2d_Curve) mycurve = ... ; Geom2dAdaptor_Curve Obj ( mycurve ) ; The qualified curve is then constructed with this object: Geom2dGcc_QualifiedCurve myQCurve = Geom2dGcc::Enclosed(Obj);
        """
    @staticmethod
    def Enclosing_s(Obj : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve: 
        """
        Constructs such a qualified curve that the solution computed by a construction algorithm using the qualified curve encloses the curve. Warning Obj is an adapted curve, i.e. an object which is an interface between: - the services provided by a 2D curve from the package Geom2d, - and those required on the curve by a computation algorithm. The adapted curve is created in the following way: Handle(Geom2d_Curve) mycurve = ... ; Geom2dAdaptor_Curve Obj ( mycurve ) ; The qualified curve is then constructed with this object: Geom2dGcc_QualifiedCurve myQCurve = Geom2dGcc::Enclosing(Obj);
        """
    @staticmethod
    def Outside_s(Obj : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve: 
        """
        Constructs such a qualified curve that the solution computed by a construction algorithm using the qualified curve and the curve are external to one another. Warning Obj is an adapted curve, i.e. an object which is an interface between: - the services provided by a 2D curve from the package Geom2d, - and those required on the curve by a computation algorithm. The adapted curve is created in the following way: Handle(Geom2d_Curve) mycurve = ... ; Geom2dAdaptor_Curve Obj ( mycurve ) ; The qualified curve is then constructed with this object: Geom2dGcc_QualifiedCurve myQCurve = Geom2dGcc::Outside(Obj);
        """
    @staticmethod
    def Unqualified_s(Obj : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve: 
        """
        Constructs such a qualified curve that the relative position of the solution computed by a construction algorithm using the qualified curve to the circle or line is not qualified, i.e. all solutions apply. Warning Obj is an adapted curve, i.e. an object which is an interface between: - the services provided by a 2D curve from the package Geom2d, - and those required on the curve by a computation algorithm. The adapted curve is created in the following way: Handle(Geom2d_Curve) mycurve = ... ; Geom2dAdaptor_Curve Obj ( mycurve ) ; The qualified curve is then constructed with this object: Geom2dGcc_QualifiedCurve myQCurve = Geom2dGcc::Unqualified(Obj);
        """
    def __init__(self) -> None: ...
    pass
class Geom2dGcc_Circ2d2TanOn():
    """
    This class implements the algorithms used to create 2d circles TANgent to 2 entities and having the center ON a curve. The order of the tangency argument is always QualifiedCirc, QualifiedLin, QualifiedCurv, Pnt2d. the arguments are : - The two tangency arguments. - The center line. - The parameter for each tangency argument which is a curve. - The tolerance.
    """
    def CenterOn3(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float]: 
        """
        Returns the center PntSol of the solution of index Index computed by this algorithm. ParArg is the parameter of the point PntSol on the third argument. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction algorithm does not fail (even if it finds no solution). Note: IsDone protects against a failure arising from a more internal intersection algorithm, which has reached its numeric limits.
        """
    def IsTheSame1(self,Index : int) -> bool: 
        """
        Returns true if the solution of index Index and, respectively, the first or second argument of this algorithm are the same (i.e. there are 2 identical circles). If Rarg is the radius of the first or second argument, Rsol is the radius of the solution and dist is the distance between the two centers, we consider the two circles to be identical if |Rarg - Rsol| and dist are less than or equal to the tolerance criterion given at the time of construction of this algorithm. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def IsTheSame2(self,Index : int) -> bool: 
        """
        Returns true if the solution of index Index and, respectively, the first or second argument of this algorithm are the same (i.e. there are 2 identical circles). If Rarg is the radius of the first or second argument, Rsol is the radius of the solution and dist is the distance between the two centers, we consider the two circles to be identical if |Rarg - Rsol| and dist are less than or equal to the tolerance criterion given at the time of construction of this algorithm. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def NbSolutions(self) -> int: 
        """
        This method returns the number of solutions. NotDone is raised if the algorithm failed.
        """
    @overload
    def Results(self,Circ : Geom2dGcc_Circ2d2TanOnGeo) -> None: 
        """
        None

        None
        """
    @overload
    def Results(self,Circ : OCP.GccAna.GccAna_Circ2d2TanOn) -> None: ...
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """
    def Tangency2(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the second argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution number Index and raises OutOfRange exception if Index is greater than the number of solutions. Be careful: the Index is only a way to get all the solutions, but is not associated to these outside the context of the algorithm-object. Exceptions Standard_OutOfRange if Index is less than or equal to zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position,Qualif2 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        It returns the information about the qualifiers of the tangency arguments concerning the solution number Index. It returns the real qualifiers (the qualifiers given to the constructor method in case of enclosed, enclosing and outside and the qualifiers computedin case of unqualified). Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Point : OCP.Geom2d.Geom2d_Point,OnCurve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tolerance : float,Param1 : float,ParamOn : float) -> None: ...
    @overload
    def __init__(self,Point1 : OCP.Geom2d.Geom2d_Point,Point2 : OCP.Geom2d.Geom2d_Point,OnCurve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Qualified2 : Geom2dGcc_QualifiedCurve,OnCurve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tolerance : float,Param1 : float,Param2 : float,ParamOn : float) -> None: ...
    pass
class Geom2dGcc_Circ2d2TanOnGeo():
    """
    This class implements the algorithms used to create 2d circles TANgent to 2 entities and having the center ON a curve. The order of the tangency argument is always QualifiedCirc, QualifiedLin, QualifiedCurv, Pnt2d. the arguments are : - The two tangency arguments (lines, circles or points). - The center line (a curve). - The parameter for each tangency argument which is a curve. - The tolerance.
    """
    def CenterOn3(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float]: 
        """
        Returns information about the center (on the curv) of the result. ParArg is the intrinsic parameter of the point on the argument curv. PntSol is the center point of the solution curv. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def IsDone(self) -> bool: 
        """
        This method returns True if the construction algorithm succeeded.
        """
    def IsTheSame1(self,Index : int) -> bool: 
        """
        Returns True if the solution number Index is equal to the first argument and False in the other cases. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def IsTheSame2(self,Index : int) -> bool: 
        """
        Returns True if the solution number Index is equal to the second argument and False in the other cases. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def NbSolutions(self) -> int: 
        """
        This method returns the number of solutions. It raises NotDone if the construction algorithm didn't succeed.
        """
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the first argument. ParSol is the intrinsic parameter of the point on the solution curv. ParArg is the intrinsic parameter of the point on the argument curv. PntSol is the tangency point on the solution curv. PntArg is the tangency point on the argument curv. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def Tangency2(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the second argument. ParSol is the intrinsic parameter of the point on the solution curv. ParArg is the intrinsic parameter of the point on the argument curv. PntSol is the tangency point on the solution curv. PntArg is the tangency point on the argument curv. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution number Index and raises OutOfRange exception if Index is greater than the number of solutions. Be careful: the Index is only a way to get all the solutions, but is not associated to those outside the context of the algorithm-object. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position,Qualif2 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        It returns the information about the qualifiers of the tangency arguments concerning the solution number Index. It returns the real qualifiers (the qualifiers given to the constructor method in case of enclosed, enclosing and outside and the qualifiers computedin case of unqualified).
        """
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : OCP.GccEnt.GccEnt_QualifiedLin,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : OCP.GccEnt.GccEnt_QualifiedCirc,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified2 : OCP.GccEnt.GccEnt_QualifiedLin,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Point2 : OCP.gp.gp_Pnt2d,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified2 : OCP.gp.gp_Pnt2d,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Point1 : OCP.gp.gp_Pnt2d,Point2 : OCP.gp.gp_Pnt2d,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_Circ2d2TanOnIter():
    """
    This class implements the algorithms used to create 2d circles TANgent to 2 entities and having the center ON a curv. The order of the tangency argument is always QualifiedCirc, QualifiedLin, QualifiedCurv, Pnt2d. the arguments are : - The two tangency arguments. - The center line. - The parameter for each tangency argument which is a curve. - The tolerance.
    """
    def CenterOn3(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float]: 
        """
        Returns information about the center (on the curv) of the result and the third argument. It raises NotDone if the construction algorithm didn't succeed.
        """
    def IsDone(self) -> bool: 
        """
        This method returns True if the construction algorithm succeeded.
        """
    def IsTheSame1(self) -> bool: 
        """
        It raises NotDone if the construction algorithm didn't succeed.
        """
    def IsTheSame2(self) -> bool: 
        """
        It raises NotDone if the construction algorithm didn't succeed.
        """
    def Tangency1(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. It raises NotDone if the construction algorithm didn't succeed.
        """
    def Tangency2(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the second argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. It raises NotDone if the construction algorithm didn't succeed.
        """
    def ThisSolution(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution. It raises NotDone if the construction algorithm didn't succeed.
        """
    def WhichQualifier(self,Qualif1 : OCP.GccEnt.GccEnt_Position,Qualif2 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Qualified2 : Geom2dGcc_QCurve,OnLine : OCP.gp.gp_Lin2d,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : Geom2dGcc_QCurve,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Param1 : float,Param2 : float,ParamOn : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Point2 : OCP.gp.gp_Pnt2d,OnCurve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Param1 : float,ParamOn : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Qualified2 : Geom2dGcc_QCurve,OnCirc : OCP.gp.gp_Circ2d,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified2 : Geom2dGcc_QCurve,OnCirc : OCP.gp.gp_Circ2d,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified2 : Geom2dGcc_QCurve,OnLine : OCP.gp.gp_Lin2d,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Point2 : OCP.gp.gp_Pnt2d,OnLine : OCP.gp.gp_Lin2d,Param1 : float,Param2 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Qualified2 : Geom2dGcc_QCurve,OnCurve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Param1 : float,Param2 : float,ParamOn : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified2 : Geom2dGcc_QCurve,OnCurve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Param1 : float,Param2 : float,ParamOn : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : Geom2dGcc_QCurve,OnLine : OCP.gp.gp_Lin2d,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : Geom2dGcc_QCurve,OnCirc : OCP.gp.gp_Circ2d,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Point2 : OCP.gp.gp_Pnt2d,OnCirc : OCP.gp.gp_Circ2d,Param1 : float,Param2 : float,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_Circ2d2TanRad():
    """
    This class implements the algorithms used to create 2d circles tangent to one curve and a point/line/circle/curv and with a given radius. For each construction methods arguments are: - Two Qualified elements for tangency constrains. (for example EnclosedCirc if we want the solution inside the argument EnclosedCirc). - Two Reals. One (Radius) for the radius and the other (Tolerance) for the tolerance. Tolerance is only used for the limit cases. For example : We want to create a circle inside a circle C1 and inside a curve Cu2 with a radius Radius and a tolerance Tolerance. If we did not used Tolerance it is impossible to find a solution in the following case : Cu2 is inside C1 and there is no intersection point between the two elements. with Tolerance we will give a solution if the lowest distance between C1 and Cu2 is lower than or equal Tolerance.
    """
    def IsDone(self) -> bool: 
        """
        This method returns True if the algorithm succeeded. Note: IsDone protects against a failure arising from a more internal intersection algorithm, which has reached its numeric limits.
        """
    def IsTheSame1(self,Index : int) -> bool: 
        """
        Returns true if the solution of index Index and, respectively, the first or second argument of this algorithm are the same (i.e. there are 2 identical circles). If Rarg is the radius of the first or second argument, Rsol is the radius of the solution and dist is the distance between the two centers, we consider the two circles to be identical if |Rarg - Rsol| and dist are less than or equal to the tolerance criterion given at the time of construction of this algorithm. OutOfRange is raised if Index is greater than the number of solutions. notDone is raised if the construction algorithm did not succeed.
        """
    def IsTheSame2(self,Index : int) -> bool: 
        """
        Returns true if the solution of index Index and, respectively, the first or second argument of this algorithm are the same (i.e. there are 2 identical circles). If Rarg is the radius of the first or second argument, Rsol is the radius of the solution and dist is the distance between the two centers, we consider the two circles to be identical if |Rarg - Rsol| and dist are less than or equal to the tolerance criterion given at the time of construction of this algorithm. OutOfRange is raised if Index is greater than the number of solutions. notDone is raised if the construction algorithm did not succeed.
        """
    def NbSolutions(self) -> int: 
        """
        This method returns the number of solutions. NotDone is raised if the algorithm failed. Exceptions StdFail_NotDone if the construction fails.
        """
    @overload
    def Results(self,Circ : Geom2dGcc_Circ2d2TanRadGeo) -> None: 
        """
        None

        None
        """
    @overload
    def Results(self,Circ : OCP.GccAna.GccAna_Circ2d2TanRad) -> None: ...
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. OutOfRange is raised if Index is greater than the number of solutions. notDone is raised if the construction algorithm did not succeed.
        """
    def Tangency2(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the second argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. OutOfRange is raised if Index is greater than the number of solutions. notDone is raised if the construction algorithm did not succeed.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution number Index and raises OutOfRange exception if Index is greater than the number of solutions. Be careful: the Index is only a way to get all the solutions, but is not associated to these outside the context of the algorithm-object. Warning This indexing simply provides a means of consulting the solutions. The index values are not associated with these solutions outside the context of the algorithm object. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position,Qualif2 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        Returns the qualifiers Qualif1 and Qualif2 of the tangency arguments for the solution of index Index computed by this algorithm. The returned qualifiers are: - those specified at the start of construction when the solutions are defined as enclosed, enclosing or outside with respect to the arguments, or - those computed during construction (i.e. enclosed, enclosing or outside) when the solutions are defined as unqualified with respect to the arguments, or - GccEnt_noqualifier if the tangency argument is a point, or - GccEnt_unqualified in certain limit cases where it is impossible to qualify the solution as enclosed, enclosing or outside. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Point : OCP.Geom2d.Geom2d_Point,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Qualified2 : Geom2dGcc_QualifiedCurve,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Point1 : OCP.Geom2d.Geom2d_Point,Point2 : OCP.Geom2d.Geom2d_Point,Radius : float,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_Circ2d2TanRadGeo():
    """
    This class implements the algorithms used to create 2d circles tangent to one curve and a point/line/circle/curv and with a given radius. For each construction methods arguments are: - Two Qualified elements for tangency constrains. (for example EnclosedCirc if we want the solution inside the argument EnclosedCirc). - Two Reals. One (Radius) for the radius and the other (Tolerance) for the tolerance. Tolerance is only used for the limit cases. For example : We want to create a circle inside a circle C1 and inside a curve Cu2 with a radius Radius and a tolerance Tolerance. If we did not used Tolerance it is impossible to find a solution in the following case : Cu2 is inside C1 and there is no intersection point between the two elements. With Tolerance we will get a solution if the lowest distance between C1 and Cu2 is lower than or equal Tolerance.
    """
    def IsDone(self) -> bool: 
        """
        This method returns True if the algorithm succeeded.
        """
    def IsTheSame1(self,Index : int) -> bool: 
        """
        Returns True if the solution number Index is equal to the first argument. It raises OutOfRange if Index is greater than the number of solutions. It raises NotDone if the construction algorithm did not succeed.
        """
    def IsTheSame2(self,Index : int) -> bool: 
        """
        Returns True if the solution number Index is equal to the second argument. It raises OutOfRange if Index is greater than the number of solutions. It raises NotDone if the construction algorithm did not succeed.
        """
    def NbSolutions(self) -> int: 
        """
        This method returns the number of solutions. It raises NotDone if the algorithm failed.
        """
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution. ParArg is the intrinsic parameter of the point PntSol on the first argument. It raises OutOfRange if Index is greater than the number of solutions. It raises NotDone if the construction algorithm did not succeed.
        """
    def Tangency2(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the second argument. ParSol is the intrinsic parameter of the point PntSol on the solution. ParArg is the intrinsic parameter of the point PntArg on the second argument. It raises OutOfRange if Index is greater than the number of solutions. It raises NotDone if the construction algorithm did not succeed.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution number Index. Be careful: the Index is only a way to get all the solutions, but is not associated to those outside the context of the algorithm-object. It raises OutOfRange exception if Index is greater than the number of solutions. It raises NotDone if the construction algorithm did not succeed.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position,Qualif2 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        It returns the information about the qualifiers of the tangency arguments concerning the solution number Index. It returns the real qualifiers (the qualifiers given to the constructor method in case of enclosed, enclosing and outside and the qualifiers computedin case of unqualified).
        """
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : Geom2dGcc_QCurve,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Qualified2 : Geom2dGcc_QCurve,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Point2 : OCP.gp.gp_Pnt2d,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified2 : Geom2dGcc_QCurve,Radius : float,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_Circ2d3Tan():
    """
    This class implements the algorithms used to create 2d circles tangent to 3 points/lines/circles/ curves with one curve or more. The arguments of all construction methods are : - The three qualifiied elements for the tangency constrains (QualifiedCirc, QualifiedLine, Qualifiedcurv, Points). - A parameter for each QualifiedCurv. Describes functions for building a 2D circle: - tangential to 3 curves, or - tangential to 2 curves and passing through a point, or - tangential to a curve and passing through 2 points, or - passing through 3 points. A Circ2d3Tan object provides a framework for: - defining the construction of 2D circles(s), - implementing the construction algorithm, and - consulting the result(s).
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction algorithm does not fail (even if it finds no solution). Note: IsDone protects against a failure arising from a more internal intersection algorithm, which has reached its numeric limits.
        """
    def IsTheSame1(self,Index : int) -> bool: 
        """
        Returns True if the solution is equal to the first argument.
        """
    def IsTheSame2(self,Index : int) -> bool: 
        """
        Returns True if the solution is equal to the second argument.
        """
    def IsTheSame3(self,Index : int) -> bool: 
        """
        Returns True if the solution is equal to the third argument. If Rarg is the radius of the first, second or third argument, Rsol is the radius of the solution and dist is the distance between the two centers, we consider the two circles to be identical if |Rarg - Rsol| and dist are less than or equal to the tolerance criterion given at the time of construction of this algorithm. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def NbSolutions(self) -> int: 
        """
        This method returns the number of solutions. NotDone is raised if the algorithm failed.
        """
    def Results(self,Circ : OCP.GccAna.GccAna_Circ2d3Tan,Rank1 : int,Rank2 : int,Rank3 : int) -> None: 
        """
        None
        """
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """
    def Tangency2(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the second argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """
    def Tangency3(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the third argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution number Index and raises OutOfRange exception if Index is greater than the number of solutions. Be careful: the Index is only a way to get all the solutions, but is not associated to these outside the context of the algorithm-object.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position,Qualif2 : OCP.GccEnt.GccEnt_Position,Qualif3 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        It returns the information about the qualifiers of the tangency arguments concerning the solution number Index. It returns the real qualifiers (the qualifiers given to the constructor method in case of enclosed, enclosing and outside and the qualifiers computedin case of unqualified).
        """
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Qualified2 : Geom2dGcc_QualifiedCurve,Qualified3 : Geom2dGcc_QualifiedCurve,Tolerance : float,Param1 : float,Param2 : float,Param3 : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Point1 : OCP.Geom2d.Geom2d_Point,Point2 : OCP.Geom2d.Geom2d_Point,Tolerance : float,Param1 : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Qualified2 : Geom2dGcc_QualifiedCurve,Point : OCP.Geom2d.Geom2d_Point,Tolerance : float,Param1 : float,Param2 : float) -> None: ...
    @overload
    def __init__(self,Point1 : OCP.Geom2d.Geom2d_Point,Point2 : OCP.Geom2d.Geom2d_Point,Point3 : OCP.Geom2d.Geom2d_Point,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_Circ2d3TanIter():
    """
    This class implements the algorithms used to create 2d circles tangent to 3 points/lines/circles/ curves with one curve or more. The arguments of all construction methods are : - The three qualifiied elements for the tangency constrains (QualifiedCirc, QualifiedLine, Qualifiedcurv, Points). - A parameter for each QualifiedCurv.
    """
    def IsDone(self) -> bool: 
        """
        This method returns True if the construction algorithm succeeded.
        """
    def IsTheSame1(self) -> bool: 
        """
        It raises NotDone if the construction algorithm didn't succeed.
        """
    def IsTheSame2(self) -> bool: 
        """
        It raises NotDone if the construction algorithm didn't succeed.
        """
    def IsTheSame3(self) -> bool: 
        """
        It raises NotDone if the construction algorithm didn't succeed.
        """
    def Tangency1(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. It raises NotDone if the construction algorithm didn't succeed.
        """
    def Tangency2(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the second argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. It raises NotDone if the construction algorithm didn't succeed.
        """
    def Tangency3(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the third argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. It raises NotDone if the construction algorithm didn't succeed.
        """
    def ThisSolution(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution. It raises NotDone if the construction algorithm didn't succeed.
        """
    def WhichQualifier(self,Qualif1 : OCP.GccEnt.GccEnt_Position,Qualif2 : OCP.GccEnt.GccEnt_Position,Qualif3 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified3 : Geom2dGcc_QCurve,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : Geom2dGcc_QCurve,Point3 : OCP.gp.gp_Pnt2d,Param1 : float,Param2 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified2 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified3 : Geom2dGcc_QCurve,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Point1 : OCP.gp.gp_Pnt2d,Point2 : OCP.gp.gp_Pnt2d,Param1 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : Geom2dGcc_QCurve,Qualified3 : Geom2dGcc_QCurve,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified3 : Geom2dGcc_QCurve,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Qualified2 : Geom2dGcc_QCurve,Qualified3 : Geom2dGcc_QCurve,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified2 : Geom2dGcc_QCurve,Qualified3 : Geom2dGcc_QCurve,Param1 : float,Param2 : float,Param3 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,Qualified2 : Geom2dGcc_QCurve,Point3 : OCP.gp.gp_Pnt2d,Param1 : float,Param2 : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Qualified2 : Geom2dGcc_QCurve,Point2 : OCP.gp.gp_Pnt2d,Param1 : float,Param2 : float,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_Circ2dTanCen():
    """
    This class implements the algorithms used to create 2d circles tangent to a curve and centered on a point. The arguments of all construction methods are : - The qualified element for the tangency constrains (QualifiedCurv). -The center point Pcenter. - A real Tolerance. Tolerance is only used in the limits cases. For example : We want to create a circle tangent to an EnclosedCurv C1 with a tolerance Tolerance. If we did not used Tolerance it is impossible to find a solution in the following case : Pcenter is outside C1. With Tolerance we will give a solution if the distance between C1 and Pcenter is lower than or equal Tolerance/2.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction algorithm does not fail (even if it finds no solution). Note: IsDone protects against a failure arising from a more internal intersection algorithm, which has reached its numeric limits.
        """
    def IsTheSame1(self,Index : int) -> bool: 
        """
        Returns true if the solution of index Index and the first argument of this algorithm are the same (i.e. there are 2 identical circles). If Rarg is the radius of the first argument, Rsol is the radius of the solution and dist is the distance between the two centers, we consider the two circles to be identical if |Rarg - Rsol| and dist are less than or equal to the tolerance criterion given at the time of construction of this algorithm. NotDone is raised if the construction algorithm didn't succeed. OutOfRange is raised if Index is greater than the number of solutions.
        """
    def NbSolutions(self) -> int: 
        """
        Returns the number of circles, representing solutions computed by this algorithm. Exceptions StdFail_NotDone if the construction fails.
        """
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Circ2d: 
        """
        Returns a circle, representing the solution of index Index computed by this algorithm. Warning This indexing simply provides a means of consulting the solutions. The index values are not associated with these solutions outside the context of the algorithm object. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        Returns the qualifier Qualif1 of the tangency argument for the solution of index Index computed by this algorithm. The returned qualifier is: - that specified at the start of construction when the solutions are defined as enclosed, enclosing or outside with respect to the argument, or - that computed during construction (i.e. enclosed, enclosing or outside) when the solutions are defined as unqualified with respect to the argument. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Pcenter : OCP.Geom2d.Geom2d_Point,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_Circ2dTanCenGeo():
    """
    This class implements the algorithms used to create 2d circles tangent to a curve and centered on a point. The arguments of all construction methods are : - The qualified element for the tangency constrains (QualifiedCurv). -The center point Pcenter. - A real Tolerance. Tolerance is only used in the limits cases. For example : We want to create a circle tangent to an EnclosedCurv C1 with a tolerance Tolerance. If we did not use Tolerance it is impossible to find a solution in the following case : Pcenter is outside C1. With Tolerance we will give a solution if the distance between C1 and Pcenter is lower than or equal Tolerance/2.
    """
    def IsDone(self) -> bool: 
        """
        This method returns True if the construction algorithm succeeded.
        """
    def NbSolutions(self) -> int: 
        """
        Returns the number of solutions and raises NotDone exception if the algorithm didn't succeed. It raises NotDone if the construction algorithm didn't succeed.
        """
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntArg on the argument curv. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions or less than zero.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution number Index and raises OutOfRange exception if Index is greater than the number of solutions. Be careful: the Index is only a way to get all the solutions, but is not associated to these outside the context of the algorithm-object. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions or less than zero.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        None
        """
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Pcenter : OCP.gp.gp_Pnt2d,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_Circ2dTanOnRad():
    """
    This class implements the algorithms used to create a 2d circle tangent to a 2d entity, centered on a 2d entity and with a given radius. More than one argument must be a curve. The arguments of all construction methods are : - The qualified element for the tangency constrains (QualifiedCirc, QualifiedLin, QualifiedCurvPoints). - The Center element (circle, line, curve). - A real Tolerance. Tolerance is only used in the limits cases. For example : We want to create a circle tangent to an OutsideCurv Cu1 centered on a line OnLine with a radius Radius and with a tolerance Tolerance. If we did not used Tolerance it is impossible to find a solution in the following case : OnLine is outside Cu1. There is no intersection point between Cu1 and OnLine. The distance between the line and the circle is greater than Radius. With Tolerance we will give a solution if the distance between Cu1 and OnLine is lower than or equal Tolerance.
    """
    def CenterOn3(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float]: 
        """
        Returns the center PntSol on the second argument (i.e. line or circle) of the solution of index Index computed by this algorithm. ParArg is the intrinsic parameter of the point on the argument curv. PntSol is the center point of the solution curv. PntArg is the projection of PntSol on the argument curv. Exceptions: Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction algorithm does not fail (even if it finds no solution). Note: IsDone protects against a failure arising from a more internal intersection algorithm which has reached its numeric limits.
        """
    def IsTheSame1(self,Index : int) -> bool: 
        """
        Returns true if the solution of index Index and the first argument of this algorithm are the same (i.e. there are 2 identical circles). If Rarg is the radius of the first argument, Rsol is the radius of the solution and dist is the distance between the two centers, we consider the two circles to be identical if |Rarg - Rsol| and dist are less than or equal to the tolerance criterion given at the time of construction of this algorithm. OutOfRange is raised if Index is greater than the number of solutions. notDone is raised if the construction algorithm did not succeed.
        """
    def NbSolutions(self) -> int: 
        """
        Returns the number of circles, representing solutions computed by this algorithm. Exceptions: StdFail_NotDone if the construction fails.
        """
    @overload
    def Results(self,Circ : OCP.GccAna.GccAna_Circ2dTanOnRad) -> None: 
        """
        None

        None
        """
    @overload
    def Results(self,Circ : Geom2dGcc_Circ2dTanOnRadGeo) -> None: ...
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the first argument. ParSol is the intrinsic parameter of the point on the solution curv. ParArg is the intrinsic parameter of the point on the argument curv. PntSol is the tangency point on the solution curv. PntArg is the tangency point on the argument curv. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution number Index and raises OutOfRange exception if Index is greater than the number of solutions. Be careful: the Index is only a way to get all the solutions, but is not associated to these outside the context of the algorithm-object. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        Returns the qualifier Qualif1 of the tangency argument for the solution of index Index computed by this algorithm. The returned qualifier is: - that specified at the start of construction when the solutions are defined as enclosed, enclosing or outside with respect to the arguments, or - that computed during construction (i.e. enclosed, enclosing or outside) when the solutions are defined as unqualified with respect to the arguments, or - GccEnt_noqualifier if the tangency argument is a point. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Point1 : OCP.Geom2d.Geom2d_Point,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Radius : float,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_Circ2dTanOnRadGeo():
    """
    This class implements the algorithms used to create a 2d circle tangent to a 2d entity, centered on a 2d entity and with a given radius. More than one argument must be a curve. The arguments of all construction methods are : - The qualified element for the tangency constrains (QualifiedCirc, QualifiedLin, QualifiedCurvPoints). - The Center element (circle, line, curve). - A real Tolerance. Tolerance is only used in the limits cases. For example : We want to create a circle tangent to an OutsideCurv Cu1 centered on a line OnLine with a radius Radius and with a tolerance Tolerance. If we did not use Tolerance it is impossible to find a solution in the following case : OnLine is outside Cu1. There is no intersection point between Cu1 and OnLine. The distance between the line and the circle is greater than Radius. With Tolerance we will give a solution if the distance between Cu1 and OnLine is lower than or equal Tolerance.
    """
    def CenterOn3(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float]: 
        """
        Returns information about the center (on the curv) of the result. ParArg is the intrinsic parameter of the point on the argument curv. PntSol is the center point of the solution curv. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def IsDone(self) -> bool: 
        """
        This method returns True if the construction algorithm succeeded.
        """
    def IsTheSame1(self,Index : int) -> bool: 
        """
        Returns True if the solution number Index is equal to the first argument and False in the other cases. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def NbSolutions(self) -> int: 
        """
        This method returns the number of solutions. It raises NotDone if the construction algorithm didn't succeed.
        """
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result number Index and the first argument. ParSol is the intrinsic parameter of the point on the solution curv. ParArg is the intrinsic parameter of the point on the argument curv. PntSol is the tangency point on the solution curv. PntArg is the tangency point on the argument curv. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Circ2d: 
        """
        Returns the solution number Index and raises OutOfRange exception if Index is greater than the number of solutions. Be careful: the Index is only a way to get all the solutions, but is not associated to these outside the context of the algorithm-object. It raises NotDone if the construction algorithm didn't succeed. It raises OutOfRange if Index is greater than the number of solutions.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedLin,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Point1 : OCP.gp.gp_Pnt2d,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,OnLine : OCP.gp.gp_Lin2d,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,OnCirc : OCP.gp.gp_Circ2d,Radius : float,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,OnCurv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Radius : float,Tolerance : float) -> None: ...
    pass
class Geom2dGcc_CurveTool():
    """
    None
    """
    @staticmethod
    def D1_s(C : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    @staticmethod
    def D2_s(C : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d,N : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    @staticmethod
    def D3_s(C : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,U : float,P : OCP.gp.gp_Pnt2d,T : OCP.gp.gp_Vec2d,N : OCP.gp.gp_Vec2d,dN : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    @staticmethod
    def EpsX_s(C : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Tol : float) -> float: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def NbSamples_s(C : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> int: 
        """
        None
        """
    @staticmethod
    def Value_s(C : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,X : float) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Geom2dGcc_FunctionTanCirCu(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    This abstract class describes a Function of 1 Variable used to find a line tangent to a curve and a circle.
    """
    def Derivative(self,X : float,Deriv : float) -> bool: 
        """
        Computes the derivative of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Computes the value of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def Values(self,X : float,F : float,Deriv : float) -> bool: 
        """
        Computes the value and the derivative of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def __init__(self,Circ : OCP.gp.gp_Circ2d,Curv : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    pass
class Geom2dGcc_FunctionTanCuCu(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    This abstract class describes a Function of 1 Variable used to find a line tangent to two curves.
    """
    def Derivatives(self,X : OCP.math.math_Vector,Deriv : OCP.math.math_Matrix) -> bool: 
        """
        Computes the derivative of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def InitDerivative(self,X : OCP.math.math_Vector,Point1 : OCP.gp.gp_Pnt2d,Point2 : OCP.gp.gp_Pnt2d,Tan1 : OCP.gp.gp_Vec2d,Tan2 : OCP.gp.gp_Vec2d,D21 : OCP.gp.gp_Vec2d,D22 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        Computes the value of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,Deriv : OCP.math.math_Matrix) -> bool: 
        """
        Computes the value and the derivative of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    @overload
    def __init__(self,Circ1 : OCP.gp.gp_Circ2d,Curv2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    @overload
    def __init__(self,Curv1 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Curv2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    pass
class Geom2dGcc_FunctionTanCuCuCu(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    This abstract class describes a set on N Functions of M independent variables.
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        Returns the values of the derivatives for the variable <X>.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def InitDerivative(self,X : OCP.math.math_Vector,Point1 : OCP.gp.gp_Pnt2d,Point2 : OCP.gp.gp_Pnt2d,Point3 : OCP.gp.gp_Pnt2d,Tan1 : OCP.gp.gp_Vec2d,Tan2 : OCP.gp.gp_Vec2d,Tan3 : OCP.gp.gp_Vec2d,D21 : OCP.gp.gp_Vec2d,D22 : OCP.gp.gp_Vec2d,D23 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        Returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns the number of variables of the function.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        Computes the values of the Functions for the variable <X>.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        Returns the values of the functions and the derivatives for the variable <X>.
        """
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.gp.gp_Circ2d,C3 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,C3 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,C3 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    @overload
    def __init__(self,L1 : OCP.gp.gp_Lin2d,L2 : OCP.gp.gp_Lin2d,C3 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,L2 : OCP.gp.gp_Lin2d,C3 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    @overload
    def __init__(self,L1 : OCP.gp.gp_Lin2d,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,C3 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    pass
class Geom2dGcc_FunctionTanCuCuOnCu(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    This abstract class describes a set on N Functions of M independent variables.
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        Returns the values of the derivatives for the variable <X>.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def InitDerivative(self,X : OCP.math.math_Vector,Point1 : OCP.gp.gp_Pnt2d,Point2 : OCP.gp.gp_Pnt2d,Point3 : OCP.gp.gp_Pnt2d,Tan1 : OCP.gp.gp_Vec2d,Tan2 : OCP.gp.gp_Vec2d,Tan3 : OCP.gp.gp_Vec2d,D21 : OCP.gp.gp_Vec2d,D22 : OCP.gp.gp_Vec2d,D23 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        Returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns the number of variables of the function.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        Computes the values of the Functions for the variable <X>.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        Returns the values of the functions and the derivatives for the variable <X>.
        """
    @overload
    def __init__(self,L1 : OCP.gp.gp_Lin2d,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,OnCu : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Rad : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,OnCu : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Rad : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,OnCi : OCP.gp.gp_Circ2d,Rad : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,OnLi : OCP.gp.gp_Lin2d,Rad : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,P1 : OCP.gp.gp_Pnt2d,OnCu : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Rad : float) -> None: ...
    @overload
    def __init__(self,L1 : OCP.gp.gp_Lin2d,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,OnLi : OCP.gp.gp_Lin2d,Rad : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,P2 : OCP.gp.gp_Pnt2d,OnLi : OCP.gp.gp_Lin2d,Rad : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,OnCu : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Rad : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,P2 : OCP.gp.gp_Pnt2d,OnCi : OCP.gp.gp_Circ2d,Rad : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,OnCi : OCP.gp.gp_Circ2d,Rad : float) -> None: ...
    @overload
    def __init__(self,L1 : OCP.gp.gp_Lin2d,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,OnCi : OCP.gp.gp_Circ2d,Rad : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,OnLi : OCP.gp.gp_Lin2d,Rad : float) -> None: ...
    pass
class Geom2dGcc_FunctionTanCuPnt(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    This abstract class describes a Function of 1 Variable used to find a line tangent to a curve and passing through a point.
    """
    def Derivative(self,X : float,Deriv : float) -> bool: 
        """
        Computes the derivative of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Computes the value of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def Values(self,X : float,F : float,Deriv : float) -> bool: 
        """
        Computes the value and the derivative of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def __init__(self,C : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Point : OCP.gp.gp_Pnt2d) -> None: ...
    pass
class Geom2dGcc_FunctionTanObl(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    This class describe a function of a single variable.
    """
    def Derivative(self,X : float,Deriv : float) -> bool: 
        """
        Computes the derivative of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Computes the value of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def Values(self,X : float,F : float,Deriv : float) -> bool: 
        """
        Computes the value and the derivative of the function F for the variable X. It returns True if the computation is successfully done, False otherwise.
        """
    def __init__(self,Curve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Dir : OCP.gp.gp_Dir2d) -> None: ...
    pass
class Geom2dGcc_IsParallel(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Geom2dGcc', '__weakref__': <attribute '__weakref__' of 'Geom2dGcc_IsParallel' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Geom2dGcc_IsParallel' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Geom2dGcc_Lin2d2Tan():
    """
    This class implements the algorithms used to create 2d lines tangent to 2 other elements which can be circles, curves or points. More than one argument must be a curve. Describes functions for building a 2D line: - tangential to 2 curves, or - tangential to a curve and passing through a point. A Lin2d2Tan object provides a framework for: - defining the construction of 2D line(s), - implementing the construction algorithm, and - consulting the result(s).
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction algorithm does not fail (even if it finds no solution). Note: IsDone protects against a failure arising from a more internal intersection algorithm, which has reached its numeric limits.
        """
    def NbSolutions(self) -> int: 
        """
        Returns the number of lines, representing solutions computed by this algorithm. Exceptions StdFail_NotDone if the construction fails.R
        """
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def Tangency2(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Lin2d: 
        """
        Returns a line, representing the solution of index Index computed by this algorithm. Warning This indexing simply provides a means of consulting the solutions. The index values are not associated with these solutions outside the context of the algorithm object. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position,Qualif2 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        Returns the qualifiers Qualif1 and Qualif2 of the tangency arguments for the solution of index Index computed by this algorithm. The returned qualifiers are: - those specified at the start of construction when the solutions are defined as enclosing or outside with respect to the arguments, or - those computed during construction (i.e. enclosing or outside) when the solutions are defined as unqualified with respect to the arguments, or - GccEnt_noqualifier if the tangency argument is a point. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,ThePoint : OCP.gp.gp_Pnt2d,Tolang : float,Param1 : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,ThePoint : OCP.gp.gp_Pnt2d,Tolang : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Qualified2 : Geom2dGcc_QualifiedCurve,Tolang : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,Qualified2 : Geom2dGcc_QualifiedCurve,Tolang : float,Param1 : float,Param2 : float) -> None: ...
    pass
class Geom2dGcc_Lin2d2TanIter():
    """
    This class implements the algorithms used to create 2d lines tangent to 2 other elements which can be circles, curves or points. More than one argument must be a curve.
    """
    def IsDone(self) -> bool: 
        """
        This methode returns true when there is a solution and false in the other cases.
        """
    def Tangency1(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """
    def Tangency2(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        None
        """
    def ThisSolution(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns the solution.
        """
    def WhichQualifier(self,Qualif1 : OCP.GccEnt.GccEnt_Position,Qualif2 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,ThePoint : OCP.gp.gp_Pnt2d,Param1 : float,Tolang : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : OCP.GccEnt.GccEnt_QualifiedCirc,Qualified2 : Geom2dGcc_QCurve,Param2 : float,Tolang : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,Qualified2 : Geom2dGcc_QCurve,Param1 : float,Param2 : float,Tolang : float) -> None: ...
    pass
class Geom2dGcc_Lin2dTanObl():
    """
    This class implements the algorithms used to create 2d line tangent to a curve QualifiedCurv and doing an angle Angle with a line TheLin. The angle must be in Radian. Describes functions for building a 2D line making a given angle with a line and tangential to a curve. A Lin2dTanObl object provides a framework for: - defining the construction of 2D line(s), - implementing the construction algorithm, and - consulting the result(s).
    """
    def Intersection2(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns the point of intersection PntSol between the solution of index Index and the second argument (the line) of this algorithm. ParSol is the parameter of the point PntSol on the solution. ParArg is the parameter of the point PntSol on the second argument (the line). Exceptions StdFail_NotDone if the construction fails. Geom2dGcc_IsParallel if the solution and the second argument (the line) are parallel. Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the construction algorithm does not fail (even if it finds no solution). Note: IsDone protects against a failure arising from a more internal intersection algorithm, which has reached its numeric limits.
        """
    def NbSolutions(self) -> int: 
        """
        Returns the number of lines, representing solutions computed by this algorithm. Exceptions StdFail_NotDone if the construction fails.
        """
    def Tangency1(self,Index : int,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        Returns information about the tangency point between the result and the first argument. ParSol is the intrinsic parameter of the point PntSol on the solution curv. ParArg is the intrinsic parameter of the point PntSol on the argument curv.
        """
    def ThisSolution(self,Index : int) -> OCP.gp.gp_Lin2d: 
        """
        Returns a line, representing the solution of index Index computed by this algorithm. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    def WhichQualifier(self,Index : int,Qualif1 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        Returns the qualifier Qualif1 of the tangency argument for the solution of index Index computed by this algorithm. The returned qualifier is: - that specified at the start of construction when the solutions are defined as enclosing or outside with respect to the argument, or - that computed during construction (i.e. enclosing or outside) when the solutions are defined as unqualified with respect to the argument, or - GccEnt_noqualifier if the tangency argument is a point. Exceptions Standard_OutOfRange if Index is less than zero or greater than the number of solutions computed by this algorithm. StdFail_NotDone if the construction fails.
        """
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,TheLin : OCP.gp.gp_Lin2d,TolAng : float,Angle : float) -> None: ...
    @overload
    def __init__(self,Qualified1 : Geom2dGcc_QualifiedCurve,TheLin : OCP.gp.gp_Lin2d,TolAng : float,Param1 : float,Angle : float) -> None: ...
    pass
class Geom2dGcc_Lin2dTanOblIter():
    """
    This class implements the algorithms used to create 2d line tangent to a curve QualifiedCurv and doing an angle Angle with a line TheLin. The angle must be in Radian.
    """
    def Intersection2(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        This method returns true when there is a solution and false in the other cases.
        """
    def IsParallel2(self) -> bool: 
        """
        None
        """
    def Tangency1(self,PntSol : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        None
        """
    def ThisSolution(self) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    def WhichQualifier(self,Qualif1 : OCP.GccEnt.GccEnt_Position) -> None: 
        """
        None
        """
    def __init__(self,Qualified1 : Geom2dGcc_QCurve,TheLin : OCP.gp.gp_Lin2d,Param1 : float,TolAng : float,Angle : float=0.0) -> None: ...
    pass
class Geom2dGcc_QCurve():
    """
    Creates a qualified 2d line.
    """
    def IsEnclosed(self) -> bool: 
        """
        Returns true if the solution is Enclosed in the Curv and false in the other cases.
        """
    def IsEnclosing(self) -> bool: 
        """
        Returns true if the solution is Enclosing the Curv and false in the other cases.
        """
    def IsOutside(self) -> bool: 
        """
        Returns true if the solution is Outside the Curv and false in the other cases.
        """
    def IsUnqualified(self) -> bool: 
        """
        Returns true if the solution is unqualified and false in the other cases.
        """
    def Qualified(self) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        None
        """
    def Qualifier(self) -> OCP.GccEnt.GccEnt_Position: 
        """
        None
        """
    def __init__(self,Curve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Qualifier : OCP.GccEnt.GccEnt_Position) -> None: ...
    pass
class Geom2dGcc_QualifiedCurve():
    """
    Describes functions for building a qualified 2D curve. A qualified 2D curve is a curve with a qualifier which specifies whether the solution of a construction algorithm using the qualified curve (as an argument): - encloses the curve, or - is enclosed by the curve, or - is built so that both the curve and it are external to one another, or - is undefined (all solutions apply).
    """
    def IsEnclosed(self) -> bool: 
        """
        It returns true if the solution is Enclosed in the Curv and false in the other cases.
        """
    def IsEnclosing(self) -> bool: 
        """
        It returns true if the solution is Enclosing the Curv and false in the other cases.
        """
    def IsOutside(self) -> bool: 
        """
        It returns true if the solution is Outside the Curv and false in the other cases.
        """
    def IsUnqualified(self) -> bool: 
        """
        Returns true if the solution is unqualified and false in the other cases.
        """
    def Qualified(self) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        Returns a 2D curve to which the qualifier is assigned. Warning The returned curve is an adapted curve, i.e. an object which is an interface between: - the services provided by a 2D curve from the package Geom2d, - and those required on the curve by a computation algorithm. The Geom2d curve on which the adapted curve is based can be obtained in the following way: myQualifiedCurve = ... ; Geom2dAdaptor_Curve myAdaptedCurve = myQualifiedCurve.Qualified(); Handle(Geom2d_Curve) = myAdaptedCurve.Curve();
        """
    def Qualifier(self) -> OCP.GccEnt.GccEnt_Position: 
        """
        Returns - the qualifier of this qualified curve if it is enclosing, enclosed or outside, or - GccEnt_noqualifier if it is unqualified.
        """
    def __init__(self,Curve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Qualifier : OCP.GccEnt.GccEnt_Position) -> None: ...
    pass
class Geom2dGcc_Type1():
    """
    None

    Members:

      Geom2dGcc_CuCuCu

      Geom2dGcc_CiCuCu

      Geom2dGcc_CiCiCu

      Geom2dGcc_CiLiCu

      Geom2dGcc_LiLiCu

      Geom2dGcc_LiCuCu
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
    Geom2dGcc_CiCiCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_CiCiCu: 2>
    Geom2dGcc_CiCuCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_CiCuCu: 1>
    Geom2dGcc_CiLiCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_CiLiCu: 3>
    Geom2dGcc_CuCuCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_CuCuCu: 0>
    Geom2dGcc_LiCuCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_LiCuCu: 5>
    Geom2dGcc_LiLiCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_LiLiCu: 4>
    __entries: dict # value = {'Geom2dGcc_CuCuCu': (<Geom2dGcc_Type1.Geom2dGcc_CuCuCu: 0>, None), 'Geom2dGcc_CiCuCu': (<Geom2dGcc_Type1.Geom2dGcc_CiCuCu: 1>, None), 'Geom2dGcc_CiCiCu': (<Geom2dGcc_Type1.Geom2dGcc_CiCiCu: 2>, None), 'Geom2dGcc_CiLiCu': (<Geom2dGcc_Type1.Geom2dGcc_CiLiCu: 3>, None), 'Geom2dGcc_LiLiCu': (<Geom2dGcc_Type1.Geom2dGcc_LiLiCu: 4>, None), 'Geom2dGcc_LiCuCu': (<Geom2dGcc_Type1.Geom2dGcc_LiCuCu: 5>, None)}
    __members__: dict # value = {'Geom2dGcc_CuCuCu': <Geom2dGcc_Type1.Geom2dGcc_CuCuCu: 0>, 'Geom2dGcc_CiCuCu': <Geom2dGcc_Type1.Geom2dGcc_CiCuCu: 1>, 'Geom2dGcc_CiCiCu': <Geom2dGcc_Type1.Geom2dGcc_CiCiCu: 2>, 'Geom2dGcc_CiLiCu': <Geom2dGcc_Type1.Geom2dGcc_CiLiCu: 3>, 'Geom2dGcc_LiLiCu': <Geom2dGcc_Type1.Geom2dGcc_LiLiCu: 4>, 'Geom2dGcc_LiCuCu': <Geom2dGcc_Type1.Geom2dGcc_LiCuCu: 5>}
    pass
class Geom2dGcc_Type2():
    """
    None

    Members:

      Geom2dGcc_CuCuOnCu

      Geom2dGcc_CiCuOnCu

      Geom2dGcc_LiCuOnCu

      Geom2dGcc_CuPtOnCu

      Geom2dGcc_CuCuOnLi

      Geom2dGcc_CiCuOnLi

      Geom2dGcc_LiCuOnLi

      Geom2dGcc_CuPtOnLi

      Geom2dGcc_CuCuOnCi

      Geom2dGcc_CiCuOnCi

      Geom2dGcc_LiCuOnCi

      Geom2dGcc_CuPtOnCi
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
    Geom2dGcc_CiCuOnCi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CiCuOnCi: 9>
    Geom2dGcc_CiCuOnCu: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CiCuOnCu: 1>
    Geom2dGcc_CiCuOnLi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CiCuOnLi: 5>
    Geom2dGcc_CuCuOnCi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuCuOnCi: 8>
    Geom2dGcc_CuCuOnCu: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuCuOnCu: 0>
    Geom2dGcc_CuCuOnLi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuCuOnLi: 4>
    Geom2dGcc_CuPtOnCi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuPtOnCi: 11>
    Geom2dGcc_CuPtOnCu: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuPtOnCu: 3>
    Geom2dGcc_CuPtOnLi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuPtOnLi: 7>
    Geom2dGcc_LiCuOnCi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_LiCuOnCi: 10>
    Geom2dGcc_LiCuOnCu: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_LiCuOnCu: 2>
    Geom2dGcc_LiCuOnLi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_LiCuOnLi: 6>
    __entries: dict # value = {'Geom2dGcc_CuCuOnCu': (<Geom2dGcc_Type2.Geom2dGcc_CuCuOnCu: 0>, None), 'Geom2dGcc_CiCuOnCu': (<Geom2dGcc_Type2.Geom2dGcc_CiCuOnCu: 1>, None), 'Geom2dGcc_LiCuOnCu': (<Geom2dGcc_Type2.Geom2dGcc_LiCuOnCu: 2>, None), 'Geom2dGcc_CuPtOnCu': (<Geom2dGcc_Type2.Geom2dGcc_CuPtOnCu: 3>, None), 'Geom2dGcc_CuCuOnLi': (<Geom2dGcc_Type2.Geom2dGcc_CuCuOnLi: 4>, None), 'Geom2dGcc_CiCuOnLi': (<Geom2dGcc_Type2.Geom2dGcc_CiCuOnLi: 5>, None), 'Geom2dGcc_LiCuOnLi': (<Geom2dGcc_Type2.Geom2dGcc_LiCuOnLi: 6>, None), 'Geom2dGcc_CuPtOnLi': (<Geom2dGcc_Type2.Geom2dGcc_CuPtOnLi: 7>, None), 'Geom2dGcc_CuCuOnCi': (<Geom2dGcc_Type2.Geom2dGcc_CuCuOnCi: 8>, None), 'Geom2dGcc_CiCuOnCi': (<Geom2dGcc_Type2.Geom2dGcc_CiCuOnCi: 9>, None), 'Geom2dGcc_LiCuOnCi': (<Geom2dGcc_Type2.Geom2dGcc_LiCuOnCi: 10>, None), 'Geom2dGcc_CuPtOnCi': (<Geom2dGcc_Type2.Geom2dGcc_CuPtOnCi: 11>, None)}
    __members__: dict # value = {'Geom2dGcc_CuCuOnCu': <Geom2dGcc_Type2.Geom2dGcc_CuCuOnCu: 0>, 'Geom2dGcc_CiCuOnCu': <Geom2dGcc_Type2.Geom2dGcc_CiCuOnCu: 1>, 'Geom2dGcc_LiCuOnCu': <Geom2dGcc_Type2.Geom2dGcc_LiCuOnCu: 2>, 'Geom2dGcc_CuPtOnCu': <Geom2dGcc_Type2.Geom2dGcc_CuPtOnCu: 3>, 'Geom2dGcc_CuCuOnLi': <Geom2dGcc_Type2.Geom2dGcc_CuCuOnLi: 4>, 'Geom2dGcc_CiCuOnLi': <Geom2dGcc_Type2.Geom2dGcc_CiCuOnLi: 5>, 'Geom2dGcc_LiCuOnLi': <Geom2dGcc_Type2.Geom2dGcc_LiCuOnLi: 6>, 'Geom2dGcc_CuPtOnLi': <Geom2dGcc_Type2.Geom2dGcc_CuPtOnLi: 7>, 'Geom2dGcc_CuCuOnCi': <Geom2dGcc_Type2.Geom2dGcc_CuCuOnCi: 8>, 'Geom2dGcc_CiCuOnCi': <Geom2dGcc_Type2.Geom2dGcc_CiCuOnCi: 9>, 'Geom2dGcc_LiCuOnCi': <Geom2dGcc_Type2.Geom2dGcc_LiCuOnCi: 10>, 'Geom2dGcc_CuPtOnCi': <Geom2dGcc_Type2.Geom2dGcc_CuPtOnCi: 11>}
    pass
class Geom2dGcc_Type3():
    """
    None

    Members:

      Geom2dGcc_CuCu

      Geom2dGcc_CiCu
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
    Geom2dGcc_CiCu: OCP.Geom2dGcc.Geom2dGcc_Type3 # value = <Geom2dGcc_Type3.Geom2dGcc_CiCu: 1>
    Geom2dGcc_CuCu: OCP.Geom2dGcc.Geom2dGcc_Type3 # value = <Geom2dGcc_Type3.Geom2dGcc_CuCu: 0>
    __entries: dict # value = {'Geom2dGcc_CuCu': (<Geom2dGcc_Type3.Geom2dGcc_CuCu: 0>, None), 'Geom2dGcc_CiCu': (<Geom2dGcc_Type3.Geom2dGcc_CiCu: 1>, None)}
    __members__: dict # value = {'Geom2dGcc_CuCu': <Geom2dGcc_Type3.Geom2dGcc_CuCu: 0>, 'Geom2dGcc_CiCu': <Geom2dGcc_Type3.Geom2dGcc_CiCu: 1>}
    pass
Geom2dGcc_CiCiCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_CiCiCu: 2>
Geom2dGcc_CiCu: OCP.Geom2dGcc.Geom2dGcc_Type3 # value = <Geom2dGcc_Type3.Geom2dGcc_CiCu: 1>
Geom2dGcc_CiCuCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_CiCuCu: 1>
Geom2dGcc_CiCuOnCi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CiCuOnCi: 9>
Geom2dGcc_CiCuOnCu: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CiCuOnCu: 1>
Geom2dGcc_CiCuOnLi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CiCuOnLi: 5>
Geom2dGcc_CiLiCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_CiLiCu: 3>
Geom2dGcc_CuCu: OCP.Geom2dGcc.Geom2dGcc_Type3 # value = <Geom2dGcc_Type3.Geom2dGcc_CuCu: 0>
Geom2dGcc_CuCuCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_CuCuCu: 0>
Geom2dGcc_CuCuOnCi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuCuOnCi: 8>
Geom2dGcc_CuCuOnCu: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuCuOnCu: 0>
Geom2dGcc_CuCuOnLi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuCuOnLi: 4>
Geom2dGcc_CuPtOnCi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuPtOnCi: 11>
Geom2dGcc_CuPtOnCu: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuPtOnCu: 3>
Geom2dGcc_CuPtOnLi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_CuPtOnLi: 7>
Geom2dGcc_LiCuCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_LiCuCu: 5>
Geom2dGcc_LiCuOnCi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_LiCuOnCi: 10>
Geom2dGcc_LiCuOnCu: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_LiCuOnCu: 2>
Geom2dGcc_LiCuOnLi: OCP.Geom2dGcc.Geom2dGcc_Type2 # value = <Geom2dGcc_Type2.Geom2dGcc_LiCuOnLi: 6>
Geom2dGcc_LiLiCu: OCP.Geom2dGcc.Geom2dGcc_Type1 # value = <Geom2dGcc_Type1.Geom2dGcc_LiLiCu: 4>
