import OCP.AppDef
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.math
import OCP.AppParCurves
import OCP.gp
import OCP.FEmTool
import OCP.TColgp
import OCP.Approx
import OCP.GeomAbs
import OCP.Standard
import OCP.TColStd
import io
__all__  = [
"AppDef_Array1OfMultiPointConstraint",
"AppDef_BSpGradient_BFGSOfMyBSplGradientOfBSplineCompute",
"AppDef_BSpParFunctionOfMyBSplGradientOfBSplineCompute",
"AppDef_BSpParLeastSquareOfMyBSplGradientOfBSplineCompute",
"AppDef_BSplineCompute",
"AppDef_Compute",
"AppDef_Gradient_BFGSOfMyGradientOfCompute",
"AppDef_Gradient_BFGSOfMyGradientbisOfBSplineCompute",
"AppDef_Gradient_BFGSOfTheGradient",
"AppDef_HArray1OfMultiPointConstraint",
"AppDef_SmoothCriterion",
"AppDef_MultiLine",
"AppDef_MultiPointConstraint",
"AppDef_MyBSplGradientOfBSplineCompute",
"AppDef_MyGradientOfCompute",
"AppDef_MyGradientbisOfBSplineCompute",
"AppDef_MyLineTool",
"AppDef_ParFunctionOfMyGradientOfCompute",
"AppDef_ParFunctionOfMyGradientbisOfBSplineCompute",
"AppDef_ParFunctionOfTheGradient",
"AppDef_ParLeastSquareOfMyGradientOfCompute",
"AppDef_ParLeastSquareOfMyGradientbisOfBSplineCompute",
"AppDef_ParLeastSquareOfTheGradient",
"AppDef_ResConstraintOfMyGradientOfCompute",
"AppDef_ResConstraintOfMyGradientbisOfBSplineCompute",
"AppDef_ResConstraintOfTheGradient",
"AppDef_LinearCriteria",
"AppDef_TheFunction",
"AppDef_TheGradient",
"AppDef_TheLeastSquares",
"AppDef_TheResol",
"AppDef_Variational"
]
class AppDef_Array1OfMultiPointConstraint():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : AppDef_Array1OfMultiPointConstraint) -> AppDef_Array1OfMultiPointConstraint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> AppDef_MultiPointConstraint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppDef_MultiPointConstraint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppDef_MultiPointConstraint: 
        """
        Variable value access
        """
    def First(self) -> AppDef_MultiPointConstraint: 
        """
        Returns first element
        """
    def Init(self,theValue : AppDef_MultiPointConstraint) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> AppDef_MultiPointConstraint: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : AppDef_Array1OfMultiPointConstraint) -> AppDef_Array1OfMultiPointConstraint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppDef_MultiPointConstraint) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> AppDef_MultiPointConstraint: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : AppDef_MultiPointConstraint,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : AppDef_Array1OfMultiPointConstraint) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class AppDef_BSpGradient_BFGSOfMyBSplGradientOfBSplineCompute(OCP.math.math_BFGS):
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
class AppDef_BSpParFunctionOfMyBSplGradientOfBSplineCompute(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NbPol : int) -> None: ...
    pass
class AppDef_BSpParLeastSquareOfMyBSplGradientOfBSplineCompute():
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    pass
class AppDef_BSplineCompute():
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
    def Interpol(self,Line : AppDef_MultiLine) -> None: 
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
    def Perform(self,Line : AppDef_MultiLine) -> None: 
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
    def __init__(self,Parameters : OCP.math.math_Vector,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,Line : AppDef_MultiLine,Parameters : OCP.math.math_Vector,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,Line : AppDef_MultiLine,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: ...
    pass
class AppDef_Compute():
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
    def Perform(self,Line : AppDef_MultiLine) -> None: 
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
    def __init__(self,Line : AppDef_MultiLine,Parameters : OCP.math.math_Vector,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,Line : AppDef_MultiLine,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: ...
    @overload
    def __init__(self,degreemin : int=4,degreemax : int=8,Tolerance3d : float=0.001,Tolerance2d : float=1e-06,NbIterations : int=5,cutting : bool=True,parametrization : OCP.Approx.Approx_ParametrizationType=Approx_ParametrizationType.Approx_ChordLength,Squares : bool=False) -> None: ...
    pass
class AppDef_Gradient_BFGSOfMyGradientOfCompute(OCP.math.math_BFGS):
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
class AppDef_Gradient_BFGSOfMyGradientbisOfBSplineCompute(OCP.math.math_BFGS):
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
class AppDef_Gradient_BFGSOfTheGradient(OCP.math.math_BFGS):
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
class AppDef_HArray1OfMultiPointConstraint(AppDef_Array1OfMultiPointConstraint, OCP.Standard.Standard_Transient):
    def Array1(self) -> AppDef_Array1OfMultiPointConstraint: 
        """
        None
        """
    def Assign(self,theOther : AppDef_Array1OfMultiPointConstraint) -> AppDef_Array1OfMultiPointConstraint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> AppDef_Array1OfMultiPointConstraint: 
        """
        None
        """
    def ChangeFirst(self) -> AppDef_MultiPointConstraint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppDef_MultiPointConstraint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppDef_MultiPointConstraint: 
        """
        Variable value access
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def First(self) -> AppDef_MultiPointConstraint: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : AppDef_MultiPointConstraint) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> AppDef_MultiPointConstraint: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : AppDef_Array1OfMultiPointConstraint) -> AppDef_Array1OfMultiPointConstraint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppDef_MultiPointConstraint) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> AppDef_MultiPointConstraint: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : AppDef_Array1OfMultiPointConstraint) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : AppDef_MultiPointConstraint) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class AppDef_SmoothCriterion(OCP.Standard.Standard_Transient):
    """
    defined criterion to smooth points in curvedefined criterion to smooth points in curvedefined criterion to smooth points in curve
    """
    def AssemblyTable(self) -> OCP.FEmTool.FEmTool_HAssemblyTable: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DependenceTable(self) -> OCP.TColStd.TColStd_HArray2OfInteger: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ErrorValues(self) -> Tuple[float, float, float]: 
        """
        None
        """
    def EstLength(self) -> float: 
        """
        None
        """
    def GetCurve(self,C : OCP.FEmTool.FEmTool_Curve) -> Any: 
        """
        None
        """
    def GetEstimation(self) -> Tuple[float, float, float]: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetWeight(self) -> Tuple[float, float]: 
        """
        None
        """
    def Gradient(self,Element : int,Dimension : int,G : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def Hessian(self,Element : int,Dimension1 : int,Dimension2 : int,H : OCP.math.math_Matrix) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InputVector(self,X : OCP.math.math_Vector,AssTable : OCP.FEmTool.FEmTool_HAssemblyTable) -> None: 
        """
        Convert the assembly Vector in an Curve;
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def QualityValues(self,J1min : float,J2min : float,J3min : float,J1 : float,J2 : float,J3 : float) -> int: 
        """
        None
        """
    def SetCurve(self,C : OCP.FEmTool.FEmTool_Curve) -> None: 
        """
        None
        """
    def SetEstimation(self,E1 : float,E2 : float,E3 : float) -> None: 
        """
        None
        """
    def SetParameters(self,Parameters : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    @overload
    def SetWeight(self,Weight : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None
        """
    @overload
    def SetWeight(self,QuadraticWeight : float,QualityWeight : float,percentJ1 : float,percentJ2 : float,percentJ3 : float) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class AppDef_MultiLine():
    """
    This class describes the organized set of points used in the approximations. A MultiLine is composed of n MultiPointConstraints. The approximation of the MultiLine will be done in the order of the given n MultiPointConstraints.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def NbMultiPoints(self) -> int: 
        """
        returns the number of MultiPointConstraints of the MultiLine.
        """
    def NbPoints(self) -> int: 
        """
        returns the number of Points from MultiPoints composing the MultiLine.
        """
    def SetValue(self,Index : int,MPoint : AppDef_MultiPointConstraint) -> None: 
        """
        It sets the MultiPointConstraint of range Index to the value MPoint. An exception is raised if Index < 0 or Index> MPoint. An exception is raised if the dimensions of the MultiPoints are different.
        """
    def Value(self,Index : int) -> AppDef_MultiPointConstraint: 
        """
        returns the MultiPointConstraint of range Index An exception is raised if Index<0 or Index>MPoint.
        """
    @overload
    def __init__(self,tabP3d : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,tabP2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @overload
    def __init__(self,NbMult : int) -> None: ...
    @overload
    def __init__(self,tabMultiP : AppDef_Array1OfMultiPointConstraint) -> None: ...
    pass
class AppDef_MultiPointConstraint(OCP.AppParCurves.AppParCurves_MultiPoint):
    """
    Describes a MultiPointConstraint used in a Multiline. MultiPointConstraints are composed of several two or three-dimensional points. The purpose is to define the corresponding points that share a common constraint in order to compute the approximation of several lines in parallel. Notes: - The order of points of a MultiPointConstraints is very important. Users must give 3D points first, and then 2D points. - The constraints for the points included in a MultiPointConstraint are always identical for all points, including the parameter. - If a MultiPointConstraint is a "tangency" point, the point is also a "passing" point.
    """
    def Curv(self,Index : int) -> OCP.gp.gp_Vec: 
        """
        returns the normal vector at the point of range Index. An exception is raised if Index < 0 or if Index > number of 3d points.
        """
    def Curv2d(self,Index : int) -> OCP.gp.gp_Vec2d: 
        """
        returns the normal vector at the point of range Index. An exception is raised if Index < 0 or if Index > number of 3d points.
        """
    def Dimension(self,Index : int) -> int: 
        """
        returns the dimension of the point of range Index. An exception is raised if Index <0 or Index > NbCurves.

        returns the dimension of the point of range Index. An exception is raised if Index <0 or Index > NbCurves.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def IsCurvaturePoint(self) -> bool: 
        """
        returns True if the MultiPoint has a curvature value.
        """
    def IsTangencyPoint(self) -> bool: 
        """
        returns True if the MultiPoint has a tangency value.
        """
    def NbPoints(self) -> int: 
        """
        returns the number of points of dimension 3D.

        returns the number of points of dimension 3D.
        """
    def NbPoints2d(self) -> int: 
        """
        returns the number of points of dimension 2D.

        returns the number of points of dimension 2D.
        """
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns the 3d Point of range Index. An exception is raised if Index < 0 or Index < number of 3d Points.
        """
    def Point2d(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        returns the 2d Point of range Index. An exception is raised if index <= number of 3d Points or Index > total number of Points.
        """
    def SetCurv(self,Index : int,Curv : OCP.gp.gp_Vec) -> None: 
        """
        Vec sets the value of the normal vector at the point of index Index. The norm of the normal vector at the point of position Index is set to the normal curvature. An exception is raised if Index <0 or if Index > number of 3d points. An exception is raised if Curv has an incorrect number of dimensions.
        """
    def SetCurv2d(self,Index : int,Curv2d : OCP.gp.gp_Vec2d) -> None: 
        """
        Vec sets the value of the normal vector at the point of index Index. The norm of the normal vector at the point of position Index is set to the normal curvature. An exception is raised if Index <0 or if Index > number of 3d points. An exception is raised if Curv has an incorrect number of dimensions.
        """
    def SetPoint(self,Index : int,Point : OCP.gp.gp_Pnt) -> None: 
        """
        the 3d Point of range Index of this MultiPoint is set to <Point>. An exception is raised if Index < 0 or Index > number of 3d Points.
        """
    def SetPoint2d(self,Index : int,Point : OCP.gp.gp_Pnt2d) -> None: 
        """
        The 2d Point of range Index is set to <Point>. An exception is raised if Index > 3d Points or Index > total number of Points.
        """
    def SetTang(self,Index : int,Tang : OCP.gp.gp_Vec) -> None: 
        """
        sets the value of the tangency of the point of range Index. An exception is raised if Index <0 or if Index > number of 3d points. An exception is raised if Tang has an incorrect number of dimensions.
        """
    def SetTang2d(self,Index : int,Tang2d : OCP.gp.gp_Vec2d) -> None: 
        """
        sets the value of the tangency of the point of range Index. An exception is raised if Index <number of 3d points or if Index > total number of Points An exception is raised if Tang has an incorrect number of dimensions.
        """
    def Tang(self,Index : int) -> OCP.gp.gp_Vec: 
        """
        returns the tangency value of the point of range Index. An exception is raised if Index < 0 or if Index > number of 3d points.
        """
    def Tang2d(self,Index : int) -> OCP.gp.gp_Vec2d: 
        """
        returns the tangency value of the point of range Index. An exception is raised if Index < number of 3d points or if Index > total number of points.
        """
    def Transform(self,CuIndex : int,x : float,dx : float,y : float,dy : float,z : float,dz : float) -> None: 
        """
        Applies a transformation to the curve of range <CuIndex>. newx = x + dx*oldx newy = y + dy*oldy for all points of the curve. newz = z + dz*oldz
        """
    def Transform2d(self,CuIndex : int,x : float,dx : float,y : float,dy : float) -> None: 
        """
        Applies a transformation to the Curve of range <CuIndex>. newx = x + dx*oldx newy = y + dy*oldy for all points of the curve.
        """
    @overload
    def __init__(self,tabP : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @overload
    def __init__(self,tabP : OCP.TColgp.TColgp_Array1OfPnt,tabP2d : OCP.TColgp.TColgp_Array1OfPnt2d,tabVec : OCP.TColgp.TColgp_Array1OfVec,tabVec2d : OCP.TColgp.TColgp_Array1OfVec2d,tabCur : OCP.TColgp.TColgp_Array1OfVec,tabCur2d : OCP.TColgp.TColgp_Array1OfVec2d) -> None: ...
    @overload
    def __init__(self,tabP2d : OCP.TColgp.TColgp_Array1OfPnt2d,tabVec2d : OCP.TColgp.TColgp_Array1OfVec2d,tabCur2d : OCP.TColgp.TColgp_Array1OfVec2d) -> None: ...
    @overload
    def __init__(self,tabP : OCP.TColgp.TColgp_Array1OfPnt,tabP2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @overload
    def __init__(self,tabP2d : OCP.TColgp.TColgp_Array1OfPnt2d,tabVec2d : OCP.TColgp.TColgp_Array1OfVec2d) -> None: ...
    @overload
    def __init__(self,tabP : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self,tabP : OCP.TColgp.TColgp_Array1OfPnt,tabP2d : OCP.TColgp.TColgp_Array1OfPnt2d,tabVec : OCP.TColgp.TColgp_Array1OfVec,tabVec2d : OCP.TColgp.TColgp_Array1OfVec2d) -> None: ...
    @overload
    def __init__(self,tabP : OCP.TColgp.TColgp_Array1OfPnt,tabVec : OCP.TColgp.TColgp_Array1OfVec,tabCur : OCP.TColgp.TColgp_Array1OfVec) -> None: ...
    @overload
    def __init__(self,NbPoints : int,NbPoints2d : int) -> None: ...
    @overload
    def __init__(self,tabP : OCP.TColgp.TColgp_Array1OfPnt,tabVec : OCP.TColgp.TColgp_Array1OfVec) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class AppDef_MyBSplGradientOfBSplineCompute():
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Deg : int,Tol3d : float,Tol2d : float,NbIterations : int=1) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Deg : int,Tol3d : float,Tol2d : float,NbIterations : int,lambda1 : float,lambda2 : float) -> None: ...
    pass
class AppDef_MyGradientOfCompute():
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int,Tol3d : float,Tol2d : float,NbIterations : int=200) -> None: ...
    pass
class AppDef_MyGradientbisOfBSplineCompute():
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int,Tol3d : float,Tol2d : float,NbIterations : int=200) -> None: ...
    pass
class AppDef_MyLineTool():
    """
    Example of MultiLine tool corresponding to the tools of the packages AppParCurves and Approx. For Approx, the tool will not add points if the algorithms want some.
    """
    @staticmethod
    @overload
    def Curvature_s(ML : AppDef_MultiLine,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        returns the 3d curvatures of the multipoint <MPointIndex> when only 3d points exist.

        returns the 2d curvatures of the multipoint <MPointIndex> only when 2d points exist.

        returns the 3d and 2d curvatures of the multipoint <MPointIndex>.
        """
    @staticmethod
    @overload
    def Curvature_s(ML : AppDef_MultiLine,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec) -> bool: ...
    @staticmethod
    @overload
    def Curvature_s(ML : AppDef_MultiLine,MPointIndex : int,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: ...
    @staticmethod
    def FirstPoint_s(ML : AppDef_MultiLine) -> int: 
        """
        Returns the first index of multipoints of the MultiLine.
        """
    @staticmethod
    def LastPoint_s(ML : AppDef_MultiLine) -> int: 
        """
        Returns the last index of multipoints of the MultiLine.
        """
    @staticmethod
    def MakeMLBetween_s(ML : AppDef_MultiLine,I1 : int,I2 : int,NbPMin : int) -> AppDef_MultiLine: 
        """
        Is never called in the algorithms. Nothing is done.
        """
    @staticmethod
    def MakeMLOneMorePoint_s(ML : AppDef_MultiLine,I1 : int,I2 : int,indbad : int,OtherLine : AppDef_MultiLine) -> bool: 
        """
        Is never called in the algorithms. Nothing is done.
        """
    @staticmethod
    def NbP2d_s(ML : AppDef_MultiLine) -> int: 
        """
        Returns the number of 2d points of a MultiLine.
        """
    @staticmethod
    def NbP3d_s(ML : AppDef_MultiLine) -> int: 
        """
        Returns the number of 3d points of a MultiLine.
        """
    @staticmethod
    @overload
    def Tangency_s(ML : AppDef_MultiLine,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        returns the 3d points of the multipoint <MPointIndex> when only 3d points exist.

        returns the 2d tangency points of the multipoint <MPointIndex> only when 2d points exist.

        returns the 3d and 2d points of the multipoint <MPointIndex>.
        """
    @staticmethod
    @overload
    def Tangency_s(ML : AppDef_MultiLine,MPointIndex : int,tabV : OCP.TColgp.TColgp_Array1OfVec) -> bool: ...
    @staticmethod
    @overload
    def Tangency_s(ML : AppDef_MultiLine,MPointIndex : int,tabV2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: ...
    @staticmethod
    @overload
    def Value_s(ML : AppDef_MultiLine,MPointIndex : int,tabPt2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        returns the 3d points of the multipoint <MPointIndex> when only 3d points exist.

        returns the 2d points of the multipoint <MPointIndex> when only 2d points exist.

        returns the 3d and 2d points of the multipoint <MPointIndex>.
        """
    @staticmethod
    @overload
    def Value_s(ML : AppDef_MultiLine,MPointIndex : int,tabPt : OCP.TColgp.TColgp_Array1OfPnt,tabPt2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @staticmethod
    @overload
    def Value_s(ML : AppDef_MultiLine,MPointIndex : int,tabPt : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @staticmethod
    def WhatStatus_s(ML : AppDef_MultiLine,I1 : int,I2 : int) -> OCP.Approx.Approx_Status: 
        """
        returns NoPointsAdded
        """
    def __init__(self) -> None: ...
    pass
class AppDef_ParFunctionOfMyGradientOfCompute(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int) -> None: ...
    pass
class AppDef_ParFunctionOfMyGradientbisOfBSplineCompute(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int) -> None: ...
    pass
class AppDef_ParFunctionOfTheGradient(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int) -> None: ...
    pass
class AppDef_ParLeastSquareOfMyGradientOfCompute():
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
    def Perform(self,Parameters : OCP.math.math_Vector,l1 : float,l2 : float) -> None: 
        """
        Is used after having initialized the fields. The case "CurvaturePoint" is not treated in this method.

        Is used after having initialized the fields.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point. <V1c> is the tangent vector at the first point. <V2c> is the tangent vector at the last point.
        """
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,V1t : OCP.math.math_Vector,V2t : OCP.math.math_Vector,V1c : OCP.math.math_Vector,V2c : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,V1t : OCP.math.math_Vector,V2t : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector) -> None: ...
    def Points(self) -> OCP.math.math_Matrix: 
        """
        returns the matrix of points value.
        """
    def Poles(self) -> OCP.math.math_Matrix: 
        """
        returns the matrix of resulting control points value.
        """
    @overload
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    pass
class AppDef_ParLeastSquareOfMyGradientbisOfBSplineCompute():
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
    def Perform(self,Parameters : OCP.math.math_Vector,l1 : float,l2 : float) -> None: 
        """
        Is used after having initialized the fields. The case "CurvaturePoint" is not treated in this method.

        Is used after having initialized the fields.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point.

        Is used after having initialized the fields. <V1t> is the tangent vector at the first point. <V2t> is the tangent vector at the last point. <V1c> is the tangent vector at the first point. <V2c> is the tangent vector at the last point.
        """
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector,V1t : OCP.math.math_Vector,V2t : OCP.math.math_Vector,l1 : float,l2 : float) -> None: ...
    @overload
    def Perform(self,Parameters : OCP.math.math_Vector) -> None: ...
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
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    pass
class AppDef_ParLeastSquareOfTheGradient():
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
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    pass
class AppDef_ResConstraintOfMyGradientOfCompute():
    """
    None
    """
    def ConstraintDerivative(self,SSP : AppDef_MultiLine,Parameters : OCP.math.math_Vector,Deg : int,DA : OCP.math.math_Matrix) -> OCP.math.math_Matrix: 
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
    def __init__(self,SSP : AppDef_MultiLine,SCurv : OCP.AppParCurves.AppParCurves_MultiCurve,FirstPoint : int,LastPoint : int,Constraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Bern : OCP.math.math_Matrix,DerivativeBern : OCP.math.math_Matrix,Tolerance : float=1e-10) -> None: ...
    pass
class AppDef_ResConstraintOfMyGradientbisOfBSplineCompute():
    """
    None
    """
    def ConstraintDerivative(self,SSP : AppDef_MultiLine,Parameters : OCP.math.math_Vector,Deg : int,DA : OCP.math.math_Matrix) -> OCP.math.math_Matrix: 
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
    def __init__(self,SSP : AppDef_MultiLine,SCurv : OCP.AppParCurves.AppParCurves_MultiCurve,FirstPoint : int,LastPoint : int,Constraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Bern : OCP.math.math_Matrix,DerivativeBern : OCP.math.math_Matrix,Tolerance : float=1e-10) -> None: ...
    pass
class AppDef_ResConstraintOfTheGradient():
    """
    None
    """
    def ConstraintDerivative(self,SSP : AppDef_MultiLine,Parameters : OCP.math.math_Vector,Deg : int,DA : OCP.math.math_Matrix) -> OCP.math.math_Matrix: 
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
    def __init__(self,SSP : AppDef_MultiLine,SCurv : OCP.AppParCurves.AppParCurves_MultiCurve,FirstPoint : int,LastPoint : int,Constraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Bern : OCP.math.math_Matrix,DerivativeBern : OCP.math.math_Matrix,Tolerance : float=1e-10) -> None: ...
    pass
class AppDef_LinearCriteria(AppDef_SmoothCriterion, OCP.Standard.Standard_Transient):
    """
    defined an Linear Criteria to used in variational Smoothing of points.defined an Linear Criteria to used in variational Smoothing of points.defined an Linear Criteria to used in variational Smoothing of points.
    """
    def AssemblyTable(self) -> OCP.FEmTool.FEmTool_HAssemblyTable: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DependenceTable(self) -> OCP.TColStd.TColStd_HArray2OfInteger: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ErrorValues(self) -> Tuple[float, float, float]: 
        """
        None
        """
    def GetCurve(self,C : OCP.FEmTool.FEmTool_Curve) -> Any: 
        """
        None
        """
    def GetEstimation(self) -> Tuple[float, float, float]: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetWeight(self) -> Tuple[float, float]: 
        """
        None
        """
    def Gradient(self,Element : int,Dimension : int,G : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def Hessian(self,Element : int,Dimension1 : int,Dimension2 : int,H : OCP.math.math_Matrix) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InputVector(self,X : OCP.math.math_Vector,AssTable : OCP.FEmTool.FEmTool_HAssemblyTable) -> None: 
        """
        Convert the assembly Vector in an Curve;
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def QualityValues(self,J1min : float,J2min : float,J3min : float,J1 : float,J2 : float,J3 : float) -> int: 
        """
        None
        """
    def SetCurve(self,C : OCP.FEmTool.FEmTool_Curve) -> None: 
        """
        None
        """
    def SetEstimation(self,E1 : float,E2 : float,E3 : float) -> None: 
        """
        None
        """
    def SetParameters(self,Parameters : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    @overload
    def SetWeight(self,Weight : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None
        """
    @overload
    def SetWeight(self,QuadraticWeight : float,QualityWeight : float,percentJ1 : float,percentJ2 : float,percentJ3 : float) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    @property
    def EstLength(self) -> float:
        """
        None

        :type: float
        """
    @EstLength.setter
    def EstLength(self, arg1: float) -> None:
        """
        None
        """
    pass
class AppDef_TheFunction(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int) -> None: ...
    pass
class AppDef_TheGradient():
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Parameters : OCP.math.math_Vector,Deg : int,Tol3d : float,Tol2d : float,NbIterations : int=200) -> None: ...
    pass
class AppDef_TheLeastSquares():
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
    def Perform(self,Parameters : OCP.math.math_Vector,l1 : float,l2 : float) -> None: 
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
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    @overload
    def __init__(self,SSP : AppDef_MultiLine,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,FirstPoint : int,LastPoint : int,FirstCons : OCP.AppParCurves.AppParCurves_Constraint,LastCons : OCP.AppParCurves.AppParCurves_Constraint,Parameters : OCP.math.math_Vector,NbPol : int) -> None: ...
    pass
class AppDef_TheResol():
    """
    None
    """
    def ConstraintDerivative(self,SSP : AppDef_MultiLine,Parameters : OCP.math.math_Vector,Deg : int,DA : OCP.math.math_Matrix) -> OCP.math.math_Matrix: 
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
    def __init__(self,SSP : AppDef_MultiLine,SCurv : OCP.AppParCurves.AppParCurves_MultiCurve,FirstPoint : int,LastPoint : int,Constraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,Bern : OCP.math.math_Matrix,DerivativeBern : OCP.math.math_Matrix,Tolerance : float=1e-10) -> None: ...
    pass
class AppDef_Variational():
    """
    This class is used to smooth N points with constraints by minimization of quadratic criterium but also variational criterium in order to obtain " fair Curve " Computes the approximation of a Multiline by Variational optimization.
    """
    def Approximate(self) -> None: 
        """
        Makes the approximation with the current fields.
        """
    def AverageError(self) -> float: 
        """
        returns the average error between the MultiLine from AppDef and the approximation.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        returns the Continuity used in the approximation
        """
    def Criterium(self) -> Tuple[float, float, float]: 
        """
        returns the values of the quality criterium.
        """
    def CriteriumWeight(self) -> Tuple[float, float, float]: 
        """
        returns the Weights (as percent) associed to the criterium used in the optimization.
        """
    def Distance(self,mat : OCP.math.math_Matrix) -> None: 
        """
        returns the distances between the points of the multiline and the approximation curves.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. MaxError,MaxErrorIndex,AverageError,QuadraticError,Criterium Distances,Degre,Nombre de poles, parametres, noeuds
        """
    def IsCreated(self) -> bool: 
        """
        returns True if the creation is done and correspond to the current fields.
        """
    def IsDone(self) -> bool: 
        """
        returns True if the approximation is ok and correspond to the current fields.
        """
    def IsOverConstrained(self) -> bool: 
        """
        returns True if the problem is overconstrained in this case, approximation cannot be done.
        """
    def Knots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns the knots uses to the approximations
        """
    def MaxDegree(self) -> int: 
        """
        returns the Maximum Degree used in the approximation
        """
    def MaxError(self) -> float: 
        """
        returns the maximum of the distances between the points of the multiline and the approximation curves.
        """
    def MaxErrorIndex(self) -> int: 
        """
        returns the index of the MultiPoint of ErrorMax
        """
    def MaxSegment(self) -> int: 
        """
        returns the Maximum of segment used in the approximation
        """
    def NbIterations(self) -> int: 
        """
        returns the number of iterations used in the approximation.
        """
    def Parameters(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns the parameters uses to the approximations
        """
    def QuadraticError(self) -> float: 
        """
        returns the quadratic average of the distances between the points of the multiline and the approximation curves.
        """
    def SetConstraints(self,aConstrainst : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple) -> bool: 
        """
        Define the constraints to approximate If this value is incompatible with the others fields this method modify nothing and returns false
        """
    def SetContinuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> bool: 
        """
        Define the Continuity used in the approximation If this value is incompatible with the others fields this method modify nothing and returns false
        """
    @overload
    def SetCriteriumWeight(self,Order : int,Percent : float) -> None: 
        """
        define the Weights (as percent) associed to the criterium used in the optimization.

        define the Weight (as percent) associed to the criterium Order used in the optimization : Others weights are updated. if Percent < 0 if Order < 1 or Order > 3
        """
    @overload
    def SetCriteriumWeight(self,Percent1 : float,Percent2 : float,Percent3 : float) -> None: ...
    def SetKnots(self,knots : OCP.TColStd.TColStd_HArray1OfReal) -> bool: 
        """
        Defines the knots used by the approximations If this value is incompatible with the others fields this method modify nothing and returns false
        """
    def SetMaxDegree(self,Degree : int) -> bool: 
        """
        Define the Maximum Degree used in the approximation If this value is incompatible with the others fields this method modify nothing and returns false
        """
    def SetMaxSegment(self,NbSegment : int) -> bool: 
        """
        Define the maximum number of segments used in the approximation If this value is incompatible with the others fields this method modify nothing and returns false
        """
    def SetNbIterations(self,Iter : int) -> None: 
        """
        define the number of iterations used in the approximation. if Iter < 1
        """
    def SetParameters(self,param : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Defines the parameters used by the approximations.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        define the tolerance used in the approximation.
        """
    def SetWithCutting(self,Cutting : bool) -> bool: 
        """
        Define if the approximation can insert new Knots or not. If this value is incompatible with the others fields this method modify nothing and returns false
        """
    def SetWithMinMax(self,MinMax : bool) -> None: 
        """
        Define if the approximation search to minimize the maximum Error or not.
        """
    def Tolerance(self) -> float: 
        """
        returns the tolerance used in the approximation.
        """
    def Value(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        returns all the BSpline curves approximating the MultiLine from AppDef SSP after minimization of the parameter.
        """
    def WithCutting(self) -> bool: 
        """
        returns if the approximation can insert new Knots or not.
        """
    def WithMinMax(self) -> bool: 
        """
        returns if the approximation search to minimize the maximum Error or not.
        """
    def __init__(self,SSP : AppDef_MultiLine,FirstPoint : int,LastPoint : int,TheConstraints : OCP.AppParCurves.AppParCurves_HArray1OfConstraintCouple,MaxDegree : int=14,MaxSegment : int=100,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,WithMinMax : bool=False,WithCutting : bool=True,Tolerance : float=1.0,NbIterations : int=2) -> None: ...
    pass
