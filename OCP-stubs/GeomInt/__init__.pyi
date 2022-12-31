import OCP.GeomInt
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.Adaptor3d
import OCP.GeomAdaptor
import OCP.Geom2d
import OCP.IntImp
import OCP.TColStd
import OCP.IntPatch
import OCP.IntSurf
import OCP.math
import OCP.AppParCurves
import OCP.NCollection
import OCP.gp
import OCP.TopAbs
import OCP.TColgp
import OCP.Bnd
import OCP.Approx
import io
__all__  = [
"GeomInt",
"GeomInt_BSpGradient_BFGSOfMyBSplGradientOfTheComputeLineOfWLApprox",
"GeomInt_BSpParFunctionOfMyBSplGradientOfTheComputeLineOfWLApprox",
"GeomInt_BSpParLeastSquareOfMyBSplGradientOfTheComputeLineOfWLApprox",
"GeomInt_Gradient_BFGSOfMyGradientOfTheComputeLineBezierOfWLApprox",
"GeomInt_Gradient_BFGSOfMyGradientbisOfTheComputeLineOfWLApprox",
"GeomInt_IntSS",
"GeomInt_LineConstructor",
"GeomInt_LineTool",
"GeomInt_MyBSplGradientOfTheComputeLineOfWLApprox",
"GeomInt_MyGradientOfTheComputeLineBezierOfWLApprox",
"GeomInt_MyGradientbisOfTheComputeLineOfWLApprox",
"GeomInt_ParFunctionOfMyGradientOfTheComputeLineBezierOfWLApprox",
"GeomInt_ParFunctionOfMyGradientbisOfTheComputeLineOfWLApprox",
"GeomInt_ParLeastSquareOfMyGradientOfTheComputeLineBezierOfWLApprox",
"GeomInt_ParLeastSquareOfMyGradientbisOfTheComputeLineOfWLApprox",
"GeomInt_ParameterAndOrientation",
"GeomInt_ResConstraintOfMyGradientOfTheComputeLineBezierOfWLApprox",
"GeomInt_ResConstraintOfMyGradientbisOfTheComputeLineOfWLApprox",
"GeomInt_SequenceOfParameterAndOrientation",
"GeomInt_TheComputeLineBezierOfWLApprox",
"GeomInt_TheComputeLineOfWLApprox",
"GeomInt_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfWLApprox",
"GeomInt_TheImpPrmSvSurfacesOfWLApprox",
"GeomInt_TheInt2SOfThePrmPrmSvSurfacesOfWLApprox",
"GeomInt_TheMultiLineOfWLApprox",
"GeomInt_TheMultiLineToolOfWLApprox",
"GeomInt_ThePrmPrmSvSurfacesOfWLApprox",
"GeomInt_TheZerImpFuncOfTheImpPrmSvSurfacesOfWLApprox",
"GeomInt_VectorOfReal",
"GeomInt_WLApprox"
]
class GeomInt():
    """
    Provides intersections on between two surfaces of Geom. The result are curves from Geom.
    """
    @staticmethod
    def AdjustPeriodic_s(thePar : float,theParMin : float,theParMax : float,thePeriod : float,theNewPar : float,theOffset : float,theEps : float=0.0) -> bool: 
        """
        Adjusts the parameter <thePar> to the range [theParMin, theParMax]
        """
    def __init__(self) -> None: ...
    pass
class GeomInt_BSpGradient_BFGSOfMyBSplGradientOfTheComputeLineOfWLApprox(OCP.math.math_BFGS):
    """
    None
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    @overload
    def Gradient(self,Grad : OCP.math.math_Vector) -> None: 
        """
        Returns the value of the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        Returns the value of the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        Returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.

        Returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Gradient(self) -> OCP.math.math_Vector: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def IsSolutionReached(self,F : OCP.math.math_MultipleVarFunctionWithGradient) -> bool: 
        """
        None
        """
    @overload
    def Location(self,Loc : OCP.math.math_Vector) -> None: 
        """
        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Location(self) -> OCP.math.math_Vector: ...
    def Minimum(self) -> float: 
        """
        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def NbIterations(self) -> int: 
        """
        Returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if the minimum was not found.

        Returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if the minimum was not found.
        """
    def Perform(self,F : OCP.math.math_MultipleVarFunctionWithGradient,StartingPoint : OCP.math.math_Vector) -> None: 
        """
        Given the starting point StartingPoint, minimization is done on the function F. The solution F = Fi is found when : 2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1) + ZEPS). Tolerance, ZEPS and maximum number of iterations are given in the constructor.
        """
    def SetBoundary(self,theLeftBorder : OCP.math.math_Vector,theRightBorder : OCP.math.math_Vector) -> None: 
        """
        Set boundaries for conditional optimization. The expected indices range of vectors is [1, NbVariables].
        """
    def __init__(self,F : OCP.math.math_MultipleVarFunctionWithGradient,StartingPoint : OCP.math.math_Vector,Tolerance3d : float,Tolerance2d : float,Eps : float,NbIterations : int=200) -> None: ...
    pass
class GeomInt_BSpParFunctionOfMyBSplGradientOfTheComputeLineOfWLApprox(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    None
    """
    def CurveValue(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        returns the MultiBSpCurve approximating the set after computing the value F or Grad(F).
        """
    def DerivativeFunctionMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the derivative function matrix used to approximate the multiline.
        """
    def Error(self,IPoint : int,CurveIndex : int) -> float: 
        """
        returns the distance between the MultiPoint of range IPoint and the curve CurveIndex.
        """
    def FirstConstraint(self,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,FirstPoint : int) -> OCP.AppParCurves.AppParCurves_Constraint: 
        """
        None
        """
    def FunctionMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the function matrix used to approximate the multiline.
        """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : OCP.math.math_Vector,G : OCP.math.math_Vector) -> bool: 
        """
        returns the gradient G of the sum above for the parameters Xi.
        """
    def Index(self) -> OCP.math.math_IntegerVector: 
        """
        Returns the indexes of the first non null values of A and DA. The values are non null from Index(ieme point) +1 to Index(ieme point) + degree +1.
        """
    def LastConstraint(self,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,LastPoint : int) -> OCP.AppParCurves.AppParCurves_Constraint: 
        """
        None
        """
    def MaxError2d(self) -> float: 
        """
        returns the maximum distance between the points and the MultiBSpCurve.
        """
    def MaxError3d(self) -> float: 
        """
        returns the maximum distance between the points and the MultiBSpCurve.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function. It corresponds to the number of MultiPoints.
        """
    def NewParameters(self) -> OCP.math.math_Vector: 
        """
        returns the new parameters of the MultiLine.
        """
    def SetFirstLambda(self,l1 : float) -> None: 
        """
        None
        """
    def SetLastLambda(self,l2 : float) -> None: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : float) -> bool: 
        """
        this method computes the new approximation of the MultiLine SSP and calculates F = sum (||Pui - Bi*Pi||2) for each point of the MultiLine.
        """
    def Values(self,X : OCP.math.math_Vector,F : float,G : OCP.math.math_Vector) -> bool: 
        """
        returns the value F=sum(||Pui - Bi*Pi||)2. returns the value G = grad(F) for the parameters Xi.
        """
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NbPol : int) -> None: ...
    pass
class GeomInt_BSpParLeastSquareOfMyBSplGradientOfTheComputeLineOfWLApprox():
    """
    None
    """
    def BSplineValue(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        returns the result of the approximation, i.e. all the Curves. An exception is raised if NotDone.
        """
    def BezierValue(self) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the result of the approximation, i.e. all the Curves. An exception is raised if NotDone.
        """
    def DerivativeFunctionMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the derivative function matrix used to approximate the set.
        """
    def Distance(self) -> OCP.math.math_Matrix: 
        """
        returns the distances between the points of the multiline and the approximation curves.
        """
    def Error(self) -> Tuple[float, float, float]: 
        """
        returns the maximum errors between the MultiLine and the approximation curves. F is the sum of the square distances.
        """
    def ErrorGradient(self,Grad : OCP.math.math_Vector) -> Tuple[float, float, float]: 
        """
        returns the maximum errors between the MultiLine and the approximation curves. F is the sum of the square distances. Grad is the derivative vector of the function F.
        """
    def FirstLambda(self) -> float: 
        """
        returns the value (P2 - P1)/ V1 if the first point was a tangency point.
        """
    def FunctionMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the function matrix used to approximate the set.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    def KIndex(self) -> OCP.math.math_IntegerVector: 
        """
        Returns the indexes of the first non null values of A and DA. The values are non null from Index(ieme point) +1 to Index(ieme point) + degree +1.
        """
    def LastLambda(self) -> float: 
        """
        returns the value (PN - PN-1)/ VN if the last point was a tangency point.
        """
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector) -> None: 
        """
        Is used after having initialized the fields. The case "CurvaturePoint" is not treated in this method.

        Is used after having initialized the fields.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point. <V1c> is the tangent vector at the first point. <V2c> is the tangent vector at the last point.
        """
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,V1t : OCP.math.math_Vector,V2t : OCP.math.math_Vector,V1c : OCP.math.math_Vector,V2c : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,V1t : OCP.math.math_Vector,V2t : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    def Points(self) -> OCP.math.math_Matrix: 
        """
        returns the matrix of points value.
        """
    def Poles(self) -> OCP.math.math_Matrix: 
        """
        returns the matrix of resulting control points value.
        """
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    pass
class GeomInt_Gradient_BFGSOfMyGradientOfTheComputeLineBezierOfWLApprox(OCP.math.math_BFGS):
    """
    None
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    @overload
    def Gradient(self,Grad : OCP.math.math_Vector) -> None: 
        """
        Returns the value of the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        Returns the value of the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        Returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.

        Returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Gradient(self) -> OCP.math.math_Vector: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def IsSolutionReached(self,F : OCP.math.math_MultipleVarFunctionWithGradient) -> bool: 
        """
        None
        """
    @overload
    def Location(self,Loc : OCP.math.math_Vector) -> None: 
        """
        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Location(self) -> OCP.math.math_Vector: ...
    def Minimum(self) -> float: 
        """
        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def NbIterations(self) -> int: 
        """
        Returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if the minimum was not found.

        Returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if the minimum was not found.
        """
    def Perform(self,F : OCP.math.math_MultipleVarFunctionWithGradient,StartingPoint : OCP.math.math_Vector) -> None: 
        """
        Given the starting point StartingPoint, minimization is done on the function F. The solution F = Fi is found when : 2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1) + ZEPS). Tolerance, ZEPS and maximum number of iterations are given in the constructor.
        """
    def SetBoundary(self,theLeftBorder : OCP.math.math_Vector,theRightBorder : OCP.math.math_Vector) -> None: 
        """
        Set boundaries for conditional optimization. The expected indices range of vectors is [1, NbVariables].
        """
    def __init__(self,F : OCP.math.math_MultipleVarFunctionWithGradient,StartingPoint : OCP.math.math_Vector,Tolerance3d : float,Tolerance2d : float,Eps : float,NbIterations : int=200) -> None: ...
    pass
class GeomInt_Gradient_BFGSOfMyGradientbisOfTheComputeLineOfWLApprox(OCP.math.math_BFGS):
    """
    None
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    @overload
    def Gradient(self,Grad : OCP.math.math_Vector) -> None: 
        """
        Returns the value of the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        Returns the value of the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        Returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.

        Returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Gradient(self) -> OCP.math.math_Vector: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def IsSolutionReached(self,F : OCP.math.math_MultipleVarFunctionWithGradient) -> bool: 
        """
        None
        """
    @overload
    def Location(self,Loc : OCP.math.math_Vector) -> None: 
        """
        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Location(self) -> OCP.math.math_Vector: ...
    def Minimum(self) -> float: 
        """
        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def NbIterations(self) -> int: 
        """
        Returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if the minimum was not found.

        Returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if the minimum was not found.
        """
    def Perform(self,F : OCP.math.math_MultipleVarFunctionWithGradient,StartingPoint : OCP.math.math_Vector) -> None: 
        """
        Given the starting point StartingPoint, minimization is done on the function F. The solution F = Fi is found when : 2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1) + ZEPS). Tolerance, ZEPS and maximum number of iterations are given in the constructor.
        """
    def SetBoundary(self,theLeftBorder : OCP.math.math_Vector,theRightBorder : OCP.math.math_Vector) -> None: 
        """
        Set boundaries for conditional optimization. The expected indices range of vectors is [1, NbVariables].
        """
    def __init__(self,F : OCP.math.math_MultipleVarFunctionWithGradient,StartingPoint : OCP.math.math_Vector,Tolerance3d : float,Tolerance2d : float,Eps : float,NbIterations : int=200) -> None: ...
    pass
class GeomInt_IntSS():
    """
    None
    """
    def Boundary(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    @staticmethod
    def BuildPCurves_s(f : float,l : float,S : OCP.Geom.Geom_Surface,C : OCP.Geom.Geom_Curve,C2d : OCP.Geom2d.Geom2d_Curve) -> Tuple[float]: 
        """
        creates 2D-curve on given surface from given 3D-curve
        """
    def HasLineOnS1(self,Index : int) -> bool: 
        """
        None
        """
    def HasLineOnS2(self,Index : int) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def Line(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def LineOnS1(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def LineOnS2(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    @staticmethod
    def MakeBSpline2d_s(theWLine : OCP.IntPatch.IntPatch_WLine,ideb : int,ifin : int,onFirst : bool) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def MakeBSpline_s(WL : OCP.IntPatch.IntPatch_WLine,ideb : int,ifin : int) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def NbBoundaries(self) -> int: 
        """
        None

        None
        """
    def NbLines(self) -> int: 
        """
        None

        None
        """
    def NbPoints(self) -> int: 
        """
        None

        None
        """
    @overload
    def Perform(self,HS1 : OCP.GeomAdaptor.GeomAdaptor_Surface,HS2 : OCP.GeomAdaptor.GeomAdaptor_Surface,Tol : float,Approx : bool=True,ApproxS1 : bool=False,ApproxS2 : bool=False) -> None: 
        """
        general intersection of two surfaces

        intersection of adapted surfaces

        general intersection using a starting point

        intersection of adapted surfaces using a starting point

        intersection of adapted surfaces

        intersection of adapted surfaces using a starting point
        """
    @overload
    def Perform(self,HS1 : OCP.GeomAdaptor.GeomAdaptor_Surface,HS2 : OCP.GeomAdaptor.GeomAdaptor_Surface,Tol : float,Approx : bool,ApproxS1 : bool,ApproxS2 : bool) -> None: ...
    @overload
    def Perform(self,HS1 : OCP.GeomAdaptor.GeomAdaptor_Surface,HS2 : OCP.GeomAdaptor.GeomAdaptor_Surface,Tol : float,U1 : float,V1 : float,U2 : float,V2 : float,Approx : bool=True,ApproxS1 : bool=False,ApproxS2 : bool=False) -> None: ...
    @overload
    def Perform(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,Tol : float,Approx : bool=True,ApproxS1 : bool=False,ApproxS2 : bool=False) -> None: ...
    @overload
    def Perform(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,Tol : float,U1 : float,V1 : float,U2 : float,V2 : float,Approx : bool=True,ApproxS1 : bool=False,ApproxS2 : bool=False) -> None: ...
    @overload
    def Perform(self,HS1 : OCP.GeomAdaptor.GeomAdaptor_Surface,HS2 : OCP.GeomAdaptor.GeomAdaptor_Surface,Tol : float,U1 : float,V1 : float,U2 : float,V2 : float,Approx : bool,ApproxS1 : bool,ApproxS2 : bool) -> None: ...
    def Pnt2d(self,Index : int,OnFirst : bool) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def TolReached2d(self) -> float: 
        """
        None

        None
        """
    def TolReached3d(self) -> float: 
        """
        None

        None
        """
    @staticmethod
    def TreatRLine_s(theRL : OCP.IntPatch.IntPatch_RLine,theHS1 : OCP.GeomAdaptor.GeomAdaptor_Surface,theHS2 : OCP.GeomAdaptor.GeomAdaptor_Surface,theC3d : OCP.Geom.Geom_Curve,theC2d1 : OCP.Geom2d.Geom2d_Curve,theC2d2 : OCP.Geom2d.Geom2d_Curve) -> Tuple[float]: 
        """
        converts RLine to Geom(2d)_Curve.
        """
    @staticmethod
    def TrimILineOnSurfBoundaries_s(theC2d1 : OCP.Geom2d.Geom2d_Curve,theC2d2 : OCP.Geom2d.Geom2d_Curve,theBound1 : OCP.Bnd.Bnd_Box2d,theBound2 : OCP.Bnd.Bnd_Box2d,theArrayOfParameters : GeomInt_VectorOfReal) -> None: 
        """
        puts into theArrayOfParameters the parameters of intersection points of given theC2d1 and theC2d2 curves with the boundaries of the source surface.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,Tol : float,Approx : bool=True,ApproxS1 : bool=False,ApproxS2 : bool=False) -> None: ...
    pass
class GeomInt_LineConstructor():
    """
    Splits given Line.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if splitting was successful

        Returns True if splitting was successful
        """
    def Load(self,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,S1 : OCP.GeomAdaptor.GeomAdaptor_Surface,S2 : OCP.GeomAdaptor.GeomAdaptor_Surface) -> None: 
        """
        Initializes me by two surfaces and corresponding tools which represent boundaries of surfaces

        Initializes me by two surfaces and corresponding tools which represent boundaries of surfaces
        """
    def NbParts(self) -> int: 
        """
        Returns number of splits

        Returns number of splits
        """
    def Part(self,I : int) -> Tuple[float, float]: 
        """
        Return first and last parameters for given index of split

        Return first and last parameters for given index of split
        """
    def Perform(self,L : OCP.IntPatch.IntPatch_Line) -> None: 
        """
        Splits line
        """
    def __init__(self) -> None: ...
    pass
class GeomInt_LineTool():
    """
    None
    """
    @staticmethod
    def DecompositionOfWLine_s(theWLine : OCP.IntPatch.IntPatch_WLine,theSurface1 : OCP.GeomAdaptor.GeomAdaptor_Surface,theSurface2 : OCP.GeomAdaptor.GeomAdaptor_Surface,aTolSum : float,theLConstructor : GeomInt_LineConstructor,theNewLines : OCP.IntPatch.IntPatch_SequenceOfLine) -> bool: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(L : OCP.IntPatch.IntPatch_Line) -> float: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(L : OCP.IntPatch.IntPatch_Line) -> float: 
        """
        None
        """
    @staticmethod
    def NbVertex_s(L : OCP.IntPatch.IntPatch_Line) -> int: 
        """
        None
        """
    @staticmethod
    def Vertex_s(L : OCP.IntPatch.IntPatch_Line,I : int) -> OCP.IntPatch.IntPatch_Point: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class GeomInt_MyBSplGradientOfTheComputeLineOfWLApprox():
    """
    None
    """
    def AverageError(self) -> float: 
        """
        returns the average error between the old and the new approximation.
        """
    def Error(self,Index : int) -> float: 
        """
        returns the difference between the old and the new approximation. An exception is raised if NotDone. An exception is raised if Index<1 or Index>NbParameters.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    def MaxError2d(self) -> float: 
        """
        returns the maximum difference between the old and the new approximation.
        """
    def MaxError3d(self) -> float: 
        """
        returns the maximum difference between the old and the new approximation.
        """
    def Value(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        returns all the BSpline curves approximating the MultiLine SSP after minimization of the parameter.
        """
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Deg : int,Tol3d : float,Tol2d : float,NbIterations : int=1) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Deg : int,Tol3d : float,Tol2d : float,NbIterations : int,lambda1 : float,lambda2 : float) -> None: ...
    pass
class GeomInt_MyGradientOfTheComputeLineBezierOfWLApprox():
    """
    None
    """
    def AverageError(self) -> float: 
        """
        returns the average error between the old and the new approximation.
        """
    def Error(self,Index : int) -> float: 
        """
        returns the difference between the old and the new approximation. An exception is raised if NotDone. An exception is raised if Index<1 or Index>NbParameters.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    def MaxError2d(self) -> float: 
        """
        returns the maximum difference between the old and the new approximation.
        """
    def MaxError3d(self) -> float: 
        """
        returns the maximum difference between the old and the new approximation.
        """
    def Value(self) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns all the Bezier curves approximating the MultiLine SSP after minimization of the parameter.
        """
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int,Tol3d : float,Tol2d : float,NbIterations : int=200) -> None: ...
    pass
class GeomInt_MyGradientbisOfTheComputeLineOfWLApprox():
    """
    None
    """
    def AverageError(self) -> float: 
        """
        returns the average error between the old and the new approximation.
        """
    def Error(self,Index : int) -> float: 
        """
        returns the difference between the old and the new approximation. An exception is raised if NotDone. An exception is raised if Index<1 or Index>NbParameters.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    def MaxError2d(self) -> float: 
        """
        returns the maximum difference between the old and the new approximation.
        """
    def MaxError3d(self) -> float: 
        """
        returns the maximum difference between the old and the new approximation.
        """
    def Value(self) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns all the Bezier curves approximating the MultiLine SSP after minimization of the parameter.
        """
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int,Tol3d : float,Tol2d : float,NbIterations : int=200) -> None: ...
    pass
class GeomInt_ParFunctionOfMyGradientOfTheComputeLineBezierOfWLApprox(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    None
    """
    def CurveValue(self) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the MultiCurve approximating the set after computing the value F or Grad(F).
        """
    def Error(self,IPoint : int,CurveIndex : int) -> float: 
        """
        returns the distance between the MultiPoint of range IPoint and the curve CurveIndex.
        """
    def FirstConstraint(self,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,FirstPoint : int) -> OCP.AppParCurves.AppParCurves_Constraint: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : OCP.math.math_Vector,G : OCP.math.math_Vector) -> bool: 
        """
        returns the gradient G of the sum above for the parameters Xi.
        """
    def LastConstraint(self,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,LastPoint : int) -> OCP.AppParCurves.AppParCurves_Constraint: 
        """
        None
        """
    def MaxError2d(self) -> float: 
        """
        returns the maximum distance between the points and the MultiCurve.
        """
    def MaxError3d(self) -> float: 
        """
        returns the maximum distance between the points and the MultiCurve.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function. It corresponds to the number of MultiPoints.
        """
    def NewParameters(self) -> OCP.math.math_Vector: 
        """
        returns the new parameters of the MultiLine.
        """
    def Value(self,X : OCP.math.math_Vector,F : float) -> bool: 
        """
        this method computes the new approximation of the MultiLine SSP and calculates F = sum (||Pui - Bi*Pi||2) for each point of the MultiLine.
        """
    def Values(self,X : OCP.math.math_Vector,F : float,G : OCP.math.math_Vector) -> bool: 
        """
        returns the value F=sum(||Pui - Bi*Pi||)2. returns the value G = grad(F) for the parameters Xi.
        """
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int) -> None: ...
    pass
class GeomInt_ParFunctionOfMyGradientbisOfTheComputeLineOfWLApprox(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    None
    """
    def CurveValue(self) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the MultiCurve approximating the set after computing the value F or Grad(F).
        """
    def Error(self,IPoint : int,CurveIndex : int) -> float: 
        """
        returns the distance between the MultiPoint of range IPoint and the curve CurveIndex.
        """
    def FirstConstraint(self,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,FirstPoint : int) -> OCP.AppParCurves.AppParCurves_Constraint: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : OCP.math.math_Vector,G : OCP.math.math_Vector) -> bool: 
        """
        returns the gradient G of the sum above for the parameters Xi.
        """
    def LastConstraint(self,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,LastPoint : int) -> OCP.AppParCurves.AppParCurves_Constraint: 
        """
        None
        """
    def MaxError2d(self) -> float: 
        """
        returns the maximum distance between the points and the MultiCurve.
        """
    def MaxError3d(self) -> float: 
        """
        returns the maximum distance between the points and the MultiCurve.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function. It corresponds to the number of MultiPoints.
        """
    def NewParameters(self) -> OCP.math.math_Vector: 
        """
        returns the new parameters of the MultiLine.
        """
    def Value(self,X : OCP.math.math_Vector,F : float) -> bool: 
        """
        this method computes the new approximation of the MultiLine SSP and calculates F = sum (||Pui - Bi*Pi||2) for each point of the MultiLine.
        """
    def Values(self,X : OCP.math.math_Vector,F : float,G : OCP.math.math_Vector) -> bool: 
        """
        returns the value F=sum(||Pui - Bi*Pi||)2. returns the value G = grad(F) for the parameters Xi.
        """
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int) -> None: ...
    pass
class GeomInt_ParLeastSquareOfMyGradientOfTheComputeLineBezierOfWLApprox():
    """
    None
    """
    def BSplineValue(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        returns the result of the approximation, i.e. all the Curves. An exception is raised if NotDone.
        """
    def BezierValue(self) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the result of the approximation, i.e. all the Curves. An exception is raised if NotDone.
        """
    def DerivativeFunctionMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the derivative function matrix used to approximate the set.
        """
    def Distance(self) -> OCP.math.math_Matrix: 
        """
        returns the distances between the points of the multiline and the approximation curves.
        """
    def Error(self) -> Tuple[float, float, float]: 
        """
        returns the maximum errors between the MultiLine and the approximation curves. F is the sum of the square distances.
        """
    def ErrorGradient(self,Grad : OCP.math.math_Vector) -> Tuple[float, float, float]: 
        """
        returns the maximum errors between the MultiLine and the approximation curves. F is the sum of the square distances. Grad is the derivative vector of the function F.
        """
    def FirstLambda(self) -> float: 
        """
        returns the value (P2 - P1)/ V1 if the first point was a tangency point.
        """
    def FunctionMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the function matrix used to approximate the set.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    def KIndex(self) -> OCP.math.math_IntegerVector: 
        """
        Returns the indexes of the first non null values of A and DA. The values are non null from Index(ieme point) +1 to Index(ieme point) + degree +1.
        """
    def LastLambda(self) -> float: 
        """
        returns the value (PN - PN-1)/ VN if the last point was a tangency point.
        """
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector) -> None: 
        """
        Is used after having initialized the fields. The case "CurvaturePoint" is not treated in this method.

        Is used after having initialized the fields.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point. <V1c> is the tangent vector at the first point. <V2c> is the tangent vector at the last point.
        """
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,V1t : OCP.math.math_Vector,V2t : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,V1t : OCP.math.math_Vector,V2t : OCP.math.math_Vector,V1c : OCP.math.math_Vector,V2c : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    def Points(self) -> OCP.math.math_Matrix: 
        """
        returns the matrix of points value.
        """
    def Poles(self) -> OCP.math.math_Matrix: 
        """
        returns the matrix of resulting control points value.
        """
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    pass
class GeomInt_ParLeastSquareOfMyGradientbisOfTheComputeLineOfWLApprox():
    """
    None
    """
    def BSplineValue(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        returns the result of the approximation, i.e. all the Curves. An exception is raised if NotDone.
        """
    def BezierValue(self) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the result of the approximation, i.e. all the Curves. An exception is raised if NotDone.
        """
    def DerivativeFunctionMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the derivative function matrix used to approximate the set.
        """
    def Distance(self) -> OCP.math.math_Matrix: 
        """
        returns the distances between the points of the multiline and the approximation curves.
        """
    def Error(self) -> Tuple[float, float, float]: 
        """
        returns the maximum errors between the MultiLine and the approximation curves. F is the sum of the square distances.
        """
    def ErrorGradient(self,Grad : OCP.math.math_Vector) -> Tuple[float, float, float]: 
        """
        returns the maximum errors between the MultiLine and the approximation curves. F is the sum of the square distances. Grad is the derivative vector of the function F.
        """
    def FirstLambda(self) -> float: 
        """
        returns the value (P2 - P1)/ V1 if the first point was a tangency point.
        """
    def FunctionMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the function matrix used to approximate the set.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    def KIndex(self) -> OCP.math.math_IntegerVector: 
        """
        Returns the indexes of the first non null values of A and DA. The values are non null from Index(ieme point) +1 to Index(ieme point) + degree +1.
        """
    def LastLambda(self) -> float: 
        """
        returns the value (PN - PN-1)/ VN if the last point was a tangency point.
        """
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,V1t : OCP.math.math_Vector,V2t : OCP.math.math_Vector,l1 : float,l2 : float) -> None: 
        """
        Is used after having initialized the fields. The case "CurvaturePoint" is not treated in this method.

        Is used after having initialized the fields.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point. <V1c> is the tangent vector at the first point. <V2c> is the tangent vector at the last point.
        """
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,V1t : OCP.math.math_Vector,V2t : OCP.math.math_Vector,V1c : OCP.math.math_Vector,V2c : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector) -> None: ...
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    def Points(self) -> OCP.math.math_Matrix: 
        """
        returns the matrix of points value.
        """
    def Poles(self) -> OCP.math.math_Matrix: 
        """
        returns the matrix of resulting control points value.
        """
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    pass
class GeomInt_ParameterAndOrientation():
    """
    None
    """
    def Orientation1(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Orientation2(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Parameter(self) -> float: 
        """
        None
        """
    def SetOrientation1(self,Or : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        None
        """
    def SetOrientation2(self,Or : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : float,Or1 : OCP.TopAbs.TopAbs_Orientation,Or2 : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    pass
class GeomInt_ResConstraintOfMyGradientOfTheComputeLineBezierOfWLApprox():
    """
    None
    """
    def ConstraintDerivative(self,SSP : GeomInt_TheMultiLineOfWLApprox,Parameters : OCP.math.math_Vector,Deg : int,DA : OCP.math.math_Matrix) -> OCP.math.math_Matrix: 
        """
        Returns the derivative of the constraint matrix.
        """
    def ConstraintMatrix(self) -> OCP.math.math_Matrix: 
        """
        None
        """
    def Duale(self) -> OCP.math.math_Vector: 
        """
        returns the duale variables of the system.
        """
    def InverseMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the Inverse of Cont*Transposed(Cont), where Cont is the constraint matrix for the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,SCurv : OCP.AppParCurves.AppParCurves_MultiCurve,FirstPoint : int,LastPoint : int,Constraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Bern : OCP.math.math_Matrix,DerivativeBern : OCP.math.math_Matrix,Tolerance : float=1e-10) -> None: ...
    pass
class GeomInt_ResConstraintOfMyGradientbisOfTheComputeLineOfWLApprox():
    """
    None
    """
    def ConstraintDerivative(self,SSP : GeomInt_TheMultiLineOfWLApprox,Parameters : OCP.math.math_Vector,Deg : int,DA : OCP.math.math_Matrix) -> OCP.math.math_Matrix: 
        """
        Returns the derivative of the constraint matrix.
        """
    def ConstraintMatrix(self) -> OCP.math.math_Matrix: 
        """
        None
        """
    def Duale(self) -> OCP.math.math_Vector: 
        """
        returns the duale variables of the system.
        """
    def InverseMatrix(self) -> OCP.math.math_Matrix: 
        """
        returns the Inverse of Cont*Transposed(Cont), where Cont is the constraint matrix for the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    def __init__(self,SSP : GeomInt_TheMultiLineOfWLApprox,SCurv : OCP.AppParCurves.AppParCurves_MultiCurve,FirstPoint : int,LastPoint : int,Constraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Bern : OCP.math.math_Matrix,DerivativeBern : OCP.math.math_Matrix,Tolerance : float=1e-10) -> None: ...
    pass
class GeomInt_SequenceOfParameterAndOrientation(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : GeomInt_ParameterAndOrientation) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : GeomInt_SequenceOfParameterAndOrientation) -> None: ...
    def Assign(self,theOther : GeomInt_SequenceOfParameterAndOrientation) -> GeomInt_SequenceOfParameterAndOrientation: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> GeomInt_ParameterAndOrientation: 
        """
        First item access
        """
    def ChangeLast(self) -> GeomInt_ParameterAndOrientation: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> GeomInt_ParameterAndOrientation: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> GeomInt_ParameterAndOrientation: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : GeomInt_ParameterAndOrientation) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : GeomInt_SequenceOfParameterAndOrientation) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : GeomInt_SequenceOfParameterAndOrientation) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : GeomInt_ParameterAndOrientation) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> GeomInt_ParameterAndOrientation: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : GeomInt_ParameterAndOrientation) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : GeomInt_SequenceOfParameterAndOrientation) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : GeomInt_ParameterAndOrientation) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : GeomInt_SequenceOfParameterAndOrientation) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> GeomInt_ParameterAndOrientation: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : GeomInt_SequenceOfParameterAndOrientation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class GeomInt_TheComputeLineBezierOfWLApprox():
    """
    None
    """
    def ChangeValue(self,Index : int=1) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the result of the approximation.
        """
    def Error(self,Index : int) -> Tuple[float, float]: 
        """
        returns the tolerances 2d and 3d of the <Index> MultiCurve.
        """
    def Init(self,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: 
        """
        Initializes the fields of the algorithm.
        """
    def IsAllApproximated(self) -> bool: 
        """
        returns False if at a moment of the approximation, the status NoApproximation has been sent by the user when more points were needed.
        """
    def IsToleranceReached(self) -> bool: 
        """
        returns False if the status NoPointsAdded has been sent.
        """
    def NbMultiCurves(self) -> int: 
        """
        Returns the number of MultiCurve doing the approximation of the MultiLine.
        """
    def Parameters(self,Index : int=1) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        returns the new parameters of the approximation corresponding to the points of the multicurve <Index>.
        """
    def Parametrization(self) -> OCP.Approx.Approx_ParametrizationType: 
        """
        returns the type of parametrization
        """
    def Perform(self,Line : GeomInt_TheMultiLineOfWLApprox) -> None: 
        """
        runs the algorithm after having initialized the fields.
        """
    def SetConstraints(self,firstC : OCP.AppParCurves.AppParCurves_Constraint,lastC : OCP.AppParCurves.AppParCurves_Constraint) -> None: 
        """
        changes the first and the last constraint points.
        """
    def SetDegrees(self,degreemin : int,degreemax : int) -> None: 
        """
        changes the degrees of the approximation.
        """
    def SetTolerances(self,Tolerance3d : float,Tolerance2d : float) -> None: 
        """
        Changes the tolerances of the approximation.
        """
    def SplineValue(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        returns the result of the approximation.
        """
    def Value(self,Index : int=1) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the result of the approximation.
        """
    @overload
    def __init__(self,Parameters : OCP.math.math_Vector,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,Line : GeomInt_TheMultiLineOfWLApprox,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,Line : GeomInt_TheMultiLineOfWLApprox,Parameters : OCP.math.math_Vector,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,Squares : bool=False) -> None: ...
    pass
class GeomInt_TheComputeLineOfWLApprox():
    """
    None
    """
    def ChangeValue(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        returns the result of the approximation.
        """
    def Error(self) -> Tuple[float, float]: 
        """
        returns the tolerances 2d and 3d of the MultiBSpCurve.
        """
    def Init(self,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: 
        """
        Initializes the fields of the algorithm.
        """
    def Interpol(self,Line : GeomInt_TheMultiLineOfWLApprox) -> None: 
        """
        Constructs an interpolation of the MultiLine <Line> The result will be a C2 curve of degree 3.
        """
    def IsAllApproximated(self) -> bool: 
        """
        returns False if at a moment of the approximation, the status NoApproximation has been sent by the user when more points were needed.
        """
    def IsToleranceReached(self) -> bool: 
        """
        returns False if the status NoPointsAdded has been sent.
        """
    def Parameters(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        returns the new parameters of the approximation corresponding to the points of the MultiBSpCurve.
        """
    def Perform(self,Line : GeomInt_TheMultiLineOfWLApprox) -> None: 
        """
        runs the algorithm after having initialized the fields.
        """
    def SetConstraints(self,firstC : OCP.AppParCurves.AppParCurves_Constraint,lastC : OCP.AppParCurves.AppParCurves_Constraint) -> None: 
        """
        changes the first and the last constraint points.
        """
    def SetContinuity(self,C : int) -> None: 
        """
        sets the continuity of the spline. if C = 2, the spline will be C2.
        """
    def SetDegrees(self,degreemin : int,degreemax : int) -> None: 
        """
        changes the degrees of the approximation.
        """
    def SetKnots(self,Knots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        The approximation will be done with the set of knots <Knots>. The multiplicities will be set with the degree and the desired continuity.
        """
    def SetKnotsAndMultiplicities(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        The approximation will be done with the set of knots <Knots> and the multiplicities <Mults>.
        """
    def SetParameters(self,ThePar : OCP.math.math_Vector) -> None: 
        """
        The approximation will begin with the set of parameters <ThePar>.
        """
    def SetPeriodic(self,thePeriodic : bool) -> None: 
        """
        Sets periodic flag. If thePeriodic = Standard_True, algorithm tries to build periodic multicurve using corresponding C1 boundary condition for first and last multipoints. Multiline must be closed.
        """
    def SetTolerances(self,Tolerance3d : float,Tolerance2d : float) -> None: 
        """
        Changes the tolerances of the approximation.
        """
    def Value(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        returns the result of the approximation.
        """
    @overload
    def __init__(self,Line : GeomInt_TheMultiLineOfWLApprox,Parameters : OCP.math.math_Vector,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,Line : GeomInt_TheMultiLineOfWLApprox,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,Parameters : OCP.math.math_Vector,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,Squares : bool=False) -> None: ...
    pass
class GeomInt_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfWLApprox(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def AuxillarSurface1(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def AuxillarSurface2(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def ComputeParameters(self,ChoixIso : OCP.IntImp.IntImp_ConstIsoparametric,Param : OCP.TColStd.TColStd_Array1OfReal,UVap : OCP.math.math_Vector,BornInf : OCP.math.math_Vector,BornSup : OCP.math.math_Vector,Tolerance : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        None
        """
    def DirectionOnS1(self) -> OCP.gp.gp_Dir2d: 
        """
        None
        """
    def DirectionOnS2(self) -> OCP.gp.gp_Dir2d: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def IsTangent(self,UVap : OCP.math.math_Vector,Param : OCP.TColStd.TColStd_Array1OfReal,BestChoix : OCP.IntImp.IntImp_ConstIsoparametric) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Root(self) -> float: 
        """
        returns somme des fi*fi
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    pass
class GeomInt_TheImpPrmSvSurfacesOfWLApprox():
    """
    None
    """
    def Compute(self,u1 : float,v1 : float,u2 : float,v2 : float,Pt : OCP.gp.gp_Pnt,Tg : OCP.gp.gp_Vec,Tguv1 : OCP.gp.gp_Vec2d,Tguv2 : OCP.gp.gp_Vec2d) -> bool: 
        """
        returns True if Tg,Tguv1 Tguv2 can be computed.
        """
    def Pnt(self,u1 : float,v1 : float,u2 : float,v2 : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def SeekPoint(self,u1 : float,v1 : float,u2 : float,v2 : float,Point : OCP.IntSurf.IntSurf_PntOn2S) -> bool: 
        """
        None
        """
    def Tangency(self,u1 : float,v1 : float,u2 : float,v2 : float,Tg : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    def TangencyOnSurf1(self,u1 : float,v1 : float,u2 : float,v2 : float,Tg : OCP.gp.gp_Vec2d) -> bool: 
        """
        None
        """
    def TangencyOnSurf2(self,u1 : float,v1 : float,u2 : float,v2 : float,Tg : OCP.gp.gp_Vec2d) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,Surf1 : OCP.Adaptor3d.Adaptor3d_Surface,Surf2 : OCP.IntSurf.IntSurf_Quadric) -> None: ...
    @overload
    def __init__(self,Surf1 : OCP.IntSurf.IntSurf_Quadric,Surf2 : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    pass
class GeomInt_TheInt2SOfThePrmPrmSvSurfacesOfWLApprox():
    """
    None
    """
    def ChangePoint(self) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        return the intersection point which is enable for changing.
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns the tangent at the intersection line.
        """
    def DirectionOnS1(self) -> OCP.gp.gp_Dir2d: 
        """
        Returns the tangent at the intersection line in the parametric space of the first surface.
        """
    def DirectionOnS2(self) -> OCP.gp.gp_Dir2d: 
        """
        Returns the tangent at the intersection line in the parametric space of the second surface.
        """
    def Function(self) -> GeomInt_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfWLApprox: 
        """
        return the math function which is used to compute the intersection
        """
    def IsDone(self) -> bool: 
        """
        Returns TRUE if the creation completed without failure.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE when there is no solution to the problem.
        """
    def IsTangent(self) -> bool: 
        """
        Returns True if the surfaces are tangent at the intersection point.
        """
    @overload
    def Perform(self,Param : OCP.TColStd.TColStd_Array1OfReal,Rsnld : OCP.math.math_FunctionSetRoot) -> OCP.IntImp.IntImp_ConstIsoparametric: 
        """
        returns the best constant isoparametric to find the next intersection's point +stores the solution point (the solution point is found with the close point to intersect the isoparametric with the other patch; the choice of the isoparametic is calculated)

        returns the best constant isoparametric to find the next intersection's point +stores the solution point (the solution point is found with the close point to intersect the isoparametric with the other patch; the choice of the isoparametic is given by ChoixIso)
        """
    @overload
    def Perform(self,Param : OCP.TColStd.TColStd_Array1OfReal,Rsnld : OCP.math.math_FunctionSetRoot,ChoixIso : OCP.IntImp.IntImp_ConstIsoparametric) -> OCP.IntImp.IntImp_ConstIsoparametric: ...
    def Point(self) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        Returns the intersection point.
        """
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,TolTangency : float) -> None: ...
    @overload
    def __init__(self,Param : OCP.TColStd.TColStd_Array1OfReal,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,TolTangency : float) -> None: ...
    pass
class GeomInt_TheMultiLineOfWLApprox():
    """
    None
    """
    def Dump(self) -> None: 
        """
        Dump of the current multi-line.
        """
    def FirstPoint(self) -> int: 
        """
        None
        """
    def LastPoint(self) -> int: 
        """
        None
        """
    def MakeMLBetween(self,Low : int,High : int,NbPointsToInsert : int) -> GeomInt_TheMultiLineOfWLApprox: 
        """
        Tries to make a sub-line between <Low> and <High> points of this line by adding <NbPointsToInsert> new points
        """
    def MakeMLOneMorePoint(self,Low : int,High : int,indbad : int,OtherLine : GeomInt_TheMultiLineOfWLApprox) -> bool: 
        """
        Tries to make a sub-line between <Low> and <High> points of this line by adding one more point between (indbad-1)-th and indbad-th points
        """
    def NbP2d(self) -> int: 
        """
        Returns the number of 2d points of a TheLine.
        """
    def NbP3d(self) -> int: 
        """
        Returns the number of 3d points of a TheLine.
        """
    @overload
    def Tangency(self,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec) -> bool: 
        """
        Returns the 3d tangency points of the multipoint <MPointIndex> only when 3d points exist.

        Returns the 2d tangency points of the multipoint <MPointIndex> only when 2d points exist.

        Returns the 3d and 2d points of the multipoint <MPointIndex>.
        """
    @overload
    def Tangency(self,MPointIndex : int,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: ...
    @overload
    def Tangency(self,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: ...
    @overload
    def Value(self,MPointIndex : int,tabPt : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        Returns the 3d points of the multipoint <MPointIndex> when only 3d points exist.

        Returns the 2d points of the multipoint <MPointIndex> when only 2d points exist.

        returns the 3d and 2d points of the multipoint <MPointIndex>.
        """
    @overload
    def Value(self,MPointIndex : int,tabPt2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @overload
    def Value(self,MPointIndex : int,tabPt : OCP.TColgp.TColgp_Array1OfPnt,tabPt2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    def WhatStatus(self) -> OCP.Approx.Approx_Status: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,line : OCP.IntPatch.IntPatch_WLine,PtrSvSurfaces : capsule,NbP3d : int,NbP2d : int,ApproxU1V1 : bool,ApproxU2V2 : bool,xo : float,yo : float,zo : float,u1o : float,v1o : float,u2o : float,v2o : float,P2DOnFirst : bool,IndMin : int=0,IndMax : int=0) -> None: ...
    @overload
    def __init__(self,line : OCP.IntPatch.IntPatch_WLine,NbP3d : int,NbP2d : int,ApproxU1V1 : bool,ApproxU2V2 : bool,xo : float,yo : float,zo : float,u1o : float,v1o : float,u2o : float,v2o : float,P2DOnFirst : bool,IndMin : int=0,IndMax : int=0) -> None: ...
    pass
class GeomInt_TheMultiLineToolOfWLApprox():
    """
    None
    """
    @staticmethod
    @overload
    def Curvature_s(ML : GeomInt_TheMultiLineOfWLApprox,MPointIndex : int,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        returns the 3d curvature of the multipoint <MPointIndex> when only 3d points exist.

        returns the 2d curvature points of the multipoint <MPointIndex> only when 2d points exist.

        returns the 3d and 2d curvature of the multipoint <MPointIndex>.
        """
    @staticmethod
    @overload
    def Curvature_s(ML : GeomInt_TheMultiLineOfWLApprox,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: ...
    @staticmethod
    @overload
    def Curvature_s(ML : GeomInt_TheMultiLineOfWLApprox,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec) -> bool: ...
    @staticmethod
    def Dump_s(ML : GeomInt_TheMultiLineOfWLApprox) -> None: 
        """
        Dump of the current multi-line.
        """
    @staticmethod
    def FirstPoint_s(ML : GeomInt_TheMultiLineOfWLApprox) -> int: 
        """
        Returns the number of multipoints of the TheMultiLine.
        """
    @staticmethod
    def LastPoint_s(ML : GeomInt_TheMultiLineOfWLApprox) -> int: 
        """
        Returns the number of multipoints of the TheMultiLine.
        """
    @staticmethod
    def MakeMLBetween_s(ML : GeomInt_TheMultiLineOfWLApprox,I1 : int,I2 : int,NbPMin : int) -> GeomInt_TheMultiLineOfWLApprox: 
        """
        Is called if WhatStatus returned "PointsAdded".
        """
    @staticmethod
    def MakeMLOneMorePoint_s(ML : GeomInt_TheMultiLineOfWLApprox,I1 : int,I2 : int,indbad : int,OtherLine : GeomInt_TheMultiLineOfWLApprox) -> bool: 
        """
        Is called when the Bezier curve contains a loop
        """
    @staticmethod
    def NbP2d_s(ML : GeomInt_TheMultiLineOfWLApprox) -> int: 
        """
        Returns the number of 2d points of a TheMultiLine.
        """
    @staticmethod
    def NbP3d_s(ML : GeomInt_TheMultiLineOfWLApprox) -> int: 
        """
        Returns the number of 3d points of a TheMultiLine.
        """
    @staticmethod
    @overload
    def Tangency_s(ML : GeomInt_TheMultiLineOfWLApprox,MPointIndex : int,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        returns the 3d points of the multipoint <MPointIndex> when only 3d points exist.

        returns the 2d tangency points of the multipoint <MPointIndex> only when 2d points exist.

        returns the 3d and 2d points of the multipoint <MPointIndex>.
        """
    @staticmethod
    @overload
    def Tangency_s(ML : GeomInt_TheMultiLineOfWLApprox,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: ...
    @staticmethod
    @overload
    def Tangency_s(ML : GeomInt_TheMultiLineOfWLApprox,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec) -> bool: ...
    @staticmethod
    @overload
    def Value_s(ML : GeomInt_TheMultiLineOfWLApprox,MPointIndex : int,tabPt2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        returns the 3d points of the multipoint <MPointIndex> when only 3d points exist.

        returns the 2d points of the multipoint <MPointIndex> when only 2d points exist.

        returns the 3d and 2d points of the multipoint <MPointIndex>.
        """
    @staticmethod
    @overload
    def Value_s(ML : GeomInt_TheMultiLineOfWLApprox,MPointIndex : int,tabPt : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @staticmethod
    @overload
    def Value_s(ML : GeomInt_TheMultiLineOfWLApprox,MPointIndex : int,tabPt : OCP.TColgp.TColgp_Array1OfPnt,tabPt2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @staticmethod
    def WhatStatus_s(ML : GeomInt_TheMultiLineOfWLApprox,I1 : int,I2 : int) -> OCP.Approx.Approx_Status: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class GeomInt_ThePrmPrmSvSurfacesOfWLApprox():
    """
    None
    """
    def Compute(self,u1 : float,v1 : float,u2 : float,v2 : float,Pt : OCP.gp.gp_Pnt,Tg : OCP.gp.gp_Vec,Tguv1 : OCP.gp.gp_Vec2d,Tguv2 : OCP.gp.gp_Vec2d) -> bool: 
        """
        returns True if Tg,Tguv1 Tguv2 can be computed.
        """
    def Pnt(self,u1 : float,v1 : float,u2 : float,v2 : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def SeekPoint(self,u1 : float,v1 : float,u2 : float,v2 : float,Point : OCP.IntSurf.IntSurf_PntOn2S) -> bool: 
        """
        None
        """
    def Tangency(self,u1 : float,v1 : float,u2 : float,v2 : float,Tg : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    def TangencyOnSurf1(self,u1 : float,v1 : float,u2 : float,v2 : float,Tg : OCP.gp.gp_Vec2d) -> bool: 
        """
        None
        """
    def TangencyOnSurf2(self,u1 : float,v1 : float,u2 : float,v2 : float,Tg : OCP.gp.gp_Vec2d) -> bool: 
        """
        None
        """
    def __init__(self,Surf1 : OCP.Adaptor3d.Adaptor3d_Surface,Surf2 : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    pass
class GeomInt_TheZerImpFuncOfTheImpPrmSvSurfacesOfWLApprox(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def Direction2d(self) -> OCP.gp.gp_Dir2d: 
        """
        None
        """
    def Direction3d(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def ISurface(self) -> OCP.IntSurf.IntSurf_Quadric: 
        """
        None
        """
    def IsTangent(self) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def PSurface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Root(self) -> float: 
        """
        None
        """
    @overload
    def Set(self,Tolerance : float) -> None: 
        """
        None

        None
        """
    @overload
    def Set(self,PS : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    def SetImplicitSurface(self,IS : OCP.IntSurf.IntSurf_Quadric) -> None: 
        """
        None
        """
    def Tolerance(self) -> float: 
        """
        Returns the value Tol so that if Abs(Func.Root())<Tol the function is considered null.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,IS : OCP.IntSurf.IntSurf_Quadric) -> None: ...
    @overload
    def __init__(self,PS : OCP.Adaptor3d.Adaptor3d_Surface,IS : OCP.IntSurf.IntSurf_Quadric) -> None: ...
    pass
class GeomInt_VectorOfReal(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : float) -> float: 
        """
        Append
        """
    def Appended(self) -> float: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : GeomInt_VectorOfReal,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> float: 
        """
        Returns first element
        """
    def ChangeLast(self) -> float: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> float: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> float: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> float: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : float) -> float: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> float: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : GeomInt_VectorOfReal) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class GeomInt_WLApprox():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbMultiCurves(self) -> int: 
        """
        None
        """
    @staticmethod
    def Parameters_s(Line : GeomInt_TheMultiLineOfWLApprox,firstP : int,lastP : int,Par : OCP.Approx.Approx_ParametrizationType,TheParameters : OCP.math.math_Vector) -> None: 
        """
        None
        """
    @overload
    def Perform(self,Surf1 : OCP.Adaptor3d.Adaptor3d_Surface,Surf2 : OCP.Adaptor3d.Adaptor3d_Surface,aLine : OCP.IntPatch.IntPatch_WLine,ApproxXYZ : bool=True,ApproxU1V1 : bool=True,ApproxU2V2 : bool=True,indicemin : int=0,indicemax : int=0) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,aLine : OCP.IntPatch.IntPatch_WLine,ApproxXYZ : bool=True,ApproxU1V1 : bool=True,ApproxU2V2 : bool=True,indicemin : int=0,indicemax : int=0) -> None: ...
    def SetParameters(self,Tol3d : float,Tol2d : float,DegMin : int,DegMax : int,NbIterMax : int,NbPntMax : int=30,ApproxWithTangency : bool=True,Parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength) -> None: 
        """
        None
        """
    def TolReached2d(self) -> float: 
        """
        None
        """
    def TolReached3d(self) -> float: 
        """
        None
        """
    def Value(self,Index : int) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
