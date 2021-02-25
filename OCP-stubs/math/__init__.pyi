import OCP.math
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.TColStd
import io
__all__  = [
"PSO_Particle",
"math",
"math_Array1OfValueAndWeight",
"math_BFGS",
"math_BissecNewton",
"math_BracketMinimum",
"math_BracketedRoot",
"math_BrentMinimum",
"math_BullardGenerator",
"math_ComputeGaussPointsAndWeights",
"math_ComputeKronrodPointsAndWeights",
"math_Crout",
"math_DirectPolynomialRoots",
"math_DoubleTab",
"math_EigenValuesSearcher",
"math_FRPR",
"math_Function",
"math_FunctionAllRoots",
"math_FunctionRoot",
"math_FunctionRoots",
"math_FunctionSample",
"math_FunctionSet",
"math_FunctionSetRoot",
"math_FunctionSetWithDerivatives",
"math_FunctionWithDerivative",
"math_Gauss",
"math_GaussLeastSquare",
"math_GaussMultipleIntegration",
"math_GaussSetIntegration",
"math_GaussSingleIntegration",
"math_GlobOptMin",
"math_Householder",
"math_IntegerVector",
"math_Jacobi",
"math_KronrodSingleIntegration",
"math_Matrix",
"math_MultipleVarFunction",
"math_MultipleVarFunctionWithGradient",
"math_MultipleVarFunctionWithHessian",
"math_NewtonFunctionRoot",
"math_NewtonFunctionSetRoot",
"math_NewtonMinimum",
"math_NotSquare",
"math_PSO",
"math_PSOParticlesPool",
"math_Powell",
"math_SVD",
"math_SingularMatrix",
"math_Status",
"math_TrigonometricEquationFunction",
"math_TrigonometricFunctionRoots",
"math_Uzawa",
"math_ValueAndWeight",
"math_Vector",
"DACTCL_Decompose",
"DACTCL_Solve",
"Jacobi",
"LU_Decompose",
"LU_Invert",
"LU_Solve",
"SVD_Decompose",
"SVD_Solve",
"__mul__",
"__rmul__",
"math_DirectionSearchError",
"math_FunctionError",
"math_NotBracketed",
"math_OK",
"math_TooManyIterations"
]
class PSO_Particle():
    """
    Describes particle pool for using in PSO algorithm. Indexes: 0 <= aDimidx <= myDimensionCount - 1
    """
    def __init__(self) -> None: ...
    @property
    def BestDistance(self) -> float:
        """
        :type: float
        """
    @BestDistance.setter
    def BestDistance(self, arg0: float) -> None:
        pass
    @property
    def Distance(self) -> float:
        """
        :type: float
        """
    @Distance.setter
    def Distance(self, arg0: float) -> None:
        pass
    pass
class math():
    """
    None
    """
    @staticmethod
    def GaussPointsMax_s() -> int: 
        """
        None
        """
    @staticmethod
    def GaussPoints_s(Index : int,Points : math_Vector) -> None: 
        """
        None
        """
    @staticmethod
    def GaussWeights_s(Index : int,Weights : math_Vector) -> None: 
        """
        None
        """
    @staticmethod
    def KronrodPointsAndWeights_s(Index : int,Points : math_Vector,Weights : math_Vector) -> bool: 
        """
        Returns a vector of Kronrod points and a vector of their weights for Gauss-Kronrod computation method. Index should be odd and greater then or equal to 3, as the number of Kronrod points is equal to 2*N + 1, where N is a number of Gauss points. Points and Weights should have the size equal to Index. Each even element of Points represents a Gauss point value of N-th Gauss quadrature. The values from Index equal to 3 to 123 are stored in a table (see the file math_Kronrod.cxx). If Index is greater, then points and weights will be computed. Returns Standard_True if Index is odd, it is equal to the size of Points and Weights and the computation of Points and Weights is performed successfully. Otherwise this method returns Standard_False.
        """
    @staticmethod
    def KronrodPointsMax_s() -> int: 
        """
        Returns the maximal number of points for that the values are stored in the table. If the number is greater then KronrodPointsMax, the points will be computed.
        """
    @staticmethod
    def OrderedGaussPointsAndWeights_s(Index : int,Points : math_Vector,Weights : math_Vector) -> bool: 
        """
        Returns a vector of Gauss points and a vector of their weights. The difference with the method GaussPoints is the following: - the points are returned in increasing order. - if Index is greater then GaussPointsMax, the points are computed. Returns Standard_True if Index is positive, Points' and Weights' length is equal to Index, Points and Weights are successfully computed.
        """
    def __init__(self) -> None: ...
    pass
class math_Array1OfValueAndWeight():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : math_Array1OfValueAndWeight) -> math_Array1OfValueAndWeight: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> math_ValueAndWeight: 
        """
        Returns first element
        """
    def ChangeLast(self) -> math_ValueAndWeight: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> math_ValueAndWeight: 
        """
        Variable value access
        """
    def First(self) -> math_ValueAndWeight: 
        """
        Returns first element
        """
    def Init(self,theValue : math_ValueAndWeight) -> None: 
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
    def Last(self) -> math_ValueAndWeight: 
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
    def Move(self,theOther : math_Array1OfValueAndWeight) -> math_Array1OfValueAndWeight: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : math_ValueAndWeight) -> None: 
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
    def Value(self,theIndex : int) -> math_ValueAndWeight: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : math_Array1OfValueAndWeight) -> None: ...
    @overload
    def __init__(self,theBegin : math_ValueAndWeight,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class math_BFGS():
    """
    This class implements the Broyden-Fletcher-Goldfarb-Shanno variant of Davidson-Fletcher-Powell minimization algorithm of a function of multiple variables.Knowledge of the function's gradient is required.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    @overload
    def Gradient(self,Grad : math_Vector) -> None: 
        """
        Returns the value of the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        Returns the value of the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        Returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.

        Returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Gradient(self) -> math_Vector: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def IsSolutionReached(self,F : math_MultipleVarFunctionWithGradient) -> bool: 
        """
        This method is called at the end of each iteration to check if the solution is found. It can be redefined in a sub-class to implement a specific test to stop the iterations.
        """
    @overload
    def Location(self,Loc : math_Vector) -> None: 
        """
        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Location(self) -> math_Vector: ...
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
    def Perform(self,F : math_MultipleVarFunctionWithGradient,StartingPoint : math_Vector) -> None: 
        """
        Given the starting point StartingPoint, minimization is done on the function F. The solution F = Fi is found when : 2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1) + ZEPS). Tolerance, ZEPS and maximum number of iterations are given in the constructor.
        """
    def SetBoundary(self,theLeftBorder : math_Vector,theRightBorder : math_Vector) -> None: 
        """
        Set boundaries for conditional optimization. The expected indices range of vectors is [1, NbVariables].
        """
    def __init__(self,NbVariables : int,Tolerance : float=1e-08,NbIterations : int=200,ZEPS : float=1e-12) -> None: ...
    pass
class math_BissecNewton():
    """
    This class implements a combination of Newton-Raphson and bissection methods to find the root of the function between two bounds. Knowledge of the derivative is required.
    """
    def Derivative(self) -> float: 
        """
        returns the value of the derivative at the root. Exception NotDone is raised if the minimum was not found.

        returns the value of the derivative at the root. Exception NotDone is raised if the minimum was not found.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redifine the operator <<.
        """
    def IsDone(self) -> bool: 
        """
        Tests is the root has been successfully found.

        Tests is the root has been successfully found.
        """
    @overload
    def IsSolutionReached(self,arg1 : math_FunctionWithDerivative) -> bool: 
        """
        This method is called at the end of each iteration to check if the solution has been found. It can be redefined in a sub-class to implement a specific test to stop the iterations.

        This method is called at the end of each iteration to check if the solution has been found. It can be redefined in a sub-class to implement a specific test to stop the iterations.
        """
    @overload
    def IsSolutionReached(self,theFunction : math_FunctionWithDerivative) -> bool: ...
    def Perform(self,F : math_FunctionWithDerivative,Bound1 : float,Bound2 : float,NbIterations : int=100) -> None: 
        """
        A combination of Newton-Raphson and bissection methods is done to find the root of the function F between the bounds Bound1 and Bound2 on the function F. The tolerance required on the root is given by TolX. The solution is found when: abs(Xi - Xi-1) <= TolX and F(Xi) * F(Xi-1) <= 0 The maximum number of iterations allowed is given by NbIterations.
        """
    def Root(self) -> float: 
        """
        returns the value of the root. Exception NotDone is raised if the minimum was not found.

        returns the value of the root. Exception NotDone is raised if the minimum was not found.
        """
    def Value(self) -> float: 
        """
        returns the value of the function at the root. Exception NotDone is raised if the minimum was not found.

        returns the value of the function at the root. Exception NotDone is raised if the minimum was not found.
        """
    def __init__(self,theXTolerance : float) -> None: ...
    pass
class math_BracketMinimum():
    """
    Given two distinct initial points, BracketMinimum implements the computation of three points (a, b, c) which bracket the minimum of the function and verify A less than B, B less than C and F(B) less than F(A), F(B) less than F(C).
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def FunctionValues(self) -> Tuple[float, float, float]: 
        """
        returns the bracketed triplet function values. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def Perform(self,F : math_Function) -> None: 
        """
        The method performing the job. It is called automatically by constructors with the function.
        """
    def SetFA(self,theValue : float) -> None: 
        """
        Set function value at A

        Set function value at A
        """
    def SetFB(self,theValue : float) -> None: 
        """
        Set function value at B

        Set function value at B
        """
    def SetLimits(self,theLeft : float,theRight : float) -> None: 
        """
        Set limits of the parameter. By default no limits are applied to the parameter change. If no minimum is found in limits then IsDone() will return false. The user is in charge of providing A and B to be in limits.

        Set limits of the parameter. By default no limits are applied to the parameter change. If no minimum is found in limits then IsDone() will return false. The user is in charge of providing A and B to be in limits.
        """
    def Values(self) -> Tuple[float, float, float]: 
        """
        Returns the bracketed triplet of abscissae. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """
    @overload
    def __init__(self,F : math_Function,A : float,B : float,FA : float) -> None: ...
    @overload
    def __init__(self,F : math_Function,A : float,B : float,FA : float,FB : float) -> None: ...
    @overload
    def __init__(self,F : math_Function,A : float,B : float) -> None: ...
    @overload
    def __init__(self,A : float,B : float) -> None: ...
    pass
class math_BracketedRoot():
    """
    This class implements the Brent method to find the root of a function located within two bounds. No knowledge of the derivative is required.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def NbIterations(self) -> int: 
        """
        returns the number of iterations really done during the computation of the Root. Exception NotDone is raised if the minimum was not found.

        returns the number of iterations really done during the computation of the Root. Exception NotDone is raised if the minimum was not found.
        """
    def Root(self) -> float: 
        """
        returns the value of the root. Exception NotDone is raised if the minimum was not found.

        returns the value of the root. Exception NotDone is raised if the minimum was not found.
        """
    def Value(self) -> float: 
        """
        returns the value of the function at the root. Exception NotDone is raised if the minimum was not found.

        returns the value of the function at the root. Exception NotDone is raised if the minimum was not found.
        """
    def __init__(self,F : math_Function,Bound1 : float,Bound2 : float,Tolerance : float,NbIterations : int=100,ZEPS : float=1e-12) -> None: ...
    pass
class math_BrentMinimum():
    """
    This class implements the Brent's method to find the minimum of a function of a single variable. No knowledge of the derivative is required.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    @overload
    def IsSolutionReached(self,arg1 : math_Function) -> bool: 
        """
        This method is called at the end of each iteration to check if the solution is found. It can be redefined in a sub-class to implement a specific test to stop the iterations.

        This method is called at the end of each iteration to check if the solution is found. It can be redefined in a sub-class to implement a specific test to stop the iterations.
        """
    @overload
    def IsSolutionReached(self,theFunction : math_Function) -> bool: ...
    def Location(self) -> float: 
        """
        returns the location value of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the location value of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def Minimum(self) -> float: 
        """
        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def NbIterations(self) -> int: 
        """
        returns the number of iterations really done during the computation of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the number of iterations really done during the computation of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def Perform(self,F : math_Function,Ax : float,Bx : float,Cx : float) -> None: 
        """
        Brent minimization is performed on function F from a given bracketing triplet of abscissas Ax, Bx, Cx (such that Bx is between Ax and Cx, F(Bx) is less than both F(Bx) and F(Cx)) The solution is found when: abs(Xi - Xi-1) <= TolX * abs(Xi) + ZEPS;
        """
    @overload
    def __init__(self,TolX : float,NbIterations : int=100,ZEPS : float=1e-12) -> None: ...
    @overload
    def __init__(self,TolX : float,Fbx : float,NbIterations : int=100,ZEPS : float=1e-12) -> None: ...
    pass
class math_BullardGenerator():
    """
    Fast random number generator (the algorithm proposed by Ian C. Bullard).
    """
    def NextInt(self) -> int: 
        """
        Generates new 64-bit integer value.
        """
    def NextReal(self) -> float: 
        """
        Generates new floating-point value.
        """
    def SetSeed(self,theSeed : int=1) -> None: 
        """
        Setup new seed / reset defaults.
        """
    def __init__(self,theSeed : int=1) -> None: ...
    pass
class math_ComputeGaussPointsAndWeights():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Points(self) -> math_Vector: 
        """
        None
        """
    def Weights(self) -> math_Vector: 
        """
        None
        """
    def __init__(self,Number : int) -> None: ...
    pass
class math_ComputeKronrodPointsAndWeights():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Points(self) -> math_Vector: 
        """
        None
        """
    def Weights(self) -> math_Vector: 
        """
        None
        """
    def __init__(self,Number : int) -> None: ...
    pass
class math_Crout():
    """
    This class implements the Crout algorithm used to solve a system A*X = B where A is a symmetric matrix. It can be used to invert a symmetric matrix. This algorithm is similar to Gauss but is faster than Gauss. Only the inferior triangle of A and the diagonal can be given.
    """
    def Determinant(self) -> float: 
        """
        Returns the value of the determinant of the previously LU decomposed matrix A. Zero is returned if the matrix A is considered as singular. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).

        Returns the value of the determinant of the previously LU decomposed matrix A. Zero is returned if the matrix A is considered as singular. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object.
        """
    def Inverse(self) -> math_Matrix: 
        """
        returns the inverse matrix of A. Only the inferior triangle is returned. Exception NotDone is raised if NotDone.

        returns the inverse matrix of A. Only the inferior triangle is returned. Exception NotDone is raised if NotDone.
        """
    def Invert(self,Inv : math_Matrix) -> None: 
        """
        returns in Inv the inverse matrix of A. Only the inferior triangle is returned. Exception NotDone is raised if NotDone.

        returns in Inv the inverse matrix of A. Only the inferior triangle is returned. Exception NotDone is raised if NotDone.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if all has been correctly done.

        Returns True if all has been correctly done.
        """
    def Solve(self,B : math_Vector,X : math_Vector) -> None: 
        """
        Given an input vector <B>, this routine returns the solution of the set of linear equations A . X = B. Exception NotDone is raised if the decomposition was not done successfully. Exception DimensionError is raised if the range of B is not equal to the rowrange of A.
        """
    def __init__(self,A : math_Matrix,MinPivot : float=1e-20) -> None: ...
    pass
class math_DirectPolynomialRoots():
    """
    This class implements the calculation of all the real roots of a real polynomial of degree <= 4 using a direct method. Once found, the roots are polished using the Newton method.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def InfiniteRoots(self) -> bool: 
        """
        Returns true if there is an infinity of roots, otherwise returns false.

        Returns true if there is an infinity of roots, otherwise returns false.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def NbSolutions(self) -> int: 
        """
        returns the number of solutions. An exception is raised if there are an infinity of roots.

        returns the number of solutions. An exception is raised if there are an infinity of roots.
        """
    def Value(self,Nieme : int) -> float: 
        """
        returns the value of the Nieme root. An exception is raised if there are an infinity of roots. Exception RangeError is raised if Nieme is < 1 or Nieme > NbSolutions.

        returns the value of the Nieme root. An exception is raised if there are an infinity of roots. Exception RangeError is raised if Nieme is < 1 or Nieme > NbSolutions.
        """
    @overload
    def __init__(self,A : float,B : float,C : float,D : float,E : float) -> None: ...
    @overload
    def __init__(self,A : float,B : float) -> None: ...
    @overload
    def __init__(self,A : float,B : float,C : float,D : float) -> None: ...
    @overload
    def __init__(self,A : float,B : float,C : float) -> None: ...
    pass
class math_DoubleTab():
    """
    None
    """
    def Copy(self,Other : math_DoubleTab) -> None: 
        """
        None

        None
        """
    def Free(self) -> None: 
        """
        None
        """
    def Init(self,InitValue : float) -> None: 
        """
        None
        """
    def SetLowerCol(self,LowerCol : int) -> None: 
        """
        None
        """
    def SetLowerRow(self,LowerRow : int) -> None: 
        """
        None
        """
    def Value(self,RowIndex : int,ColIndex : int) -> float: 
        """
        None

        None
        """
    @overload
    def __init__(self,Tab : capsule,LowerRow : int,UpperRow : int,LowerCol : int,UpperCol : int) -> None: ...
    @overload
    def __init__(self,LowerRow : int,UpperRow : int,LowerCol : int,UpperCol : int) -> None: ...
    @overload
    def __init__(self,Other : math_DoubleTab) -> None: ...
    pass
class math_EigenValuesSearcher():
    """
    This class finds eigen values and vectors of real symmetric tridiagonal matrix
    """
    def Dimension(self) -> int: 
        """
        Returns the dimension of matrix
        """
    def EigenValue(self,Index : int) -> float: 
        """
        Returns the Index_th eigen value of matrix Index must be in [1, Dimension()]
        """
    def EigenVector(self,Index : int) -> math_Vector: 
        """
        Returns the Index_th eigen vector of matrix Index must be in [1, Dimension()]
        """
    def IsDone(self) -> bool: 
        """
        Returns Standard_True if computation is performed successfully.
        """
    def __init__(self,Diagonal : OCP.TColStd.TColStd_Array1OfReal,Subdiagonal : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    pass
class math_FRPR():
    """
    this class implements the Fletcher-Reeves-Polak_Ribiere minimization algorithm of a function of multiple variables. Knowledge of the function's gradient is required.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    @overload
    def Gradient(self) -> math_Vector: 
        """
        outputs the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        outputs the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.

        returns the gradient vector at the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Gradient(self,Grad : math_Vector) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    @overload
    def IsSolutionReached(self,arg1 : math_MultipleVarFunctionWithGradient) -> bool: 
        """
        The solution F = Fi is found when: 2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1)) + ZEPS. The maximum number of iterations allowed is given by NbIterations.

        The solution F = Fi is found when: 2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1)) + ZEPS. The maximum number of iterations allowed is given by NbIterations.
        """
    @overload
    def IsSolutionReached(self,theFunction : math_MultipleVarFunctionWithGradient) -> bool: ...
    @overload
    def Location(self,Loc : math_Vector) -> None: 
        """
        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Location(self) -> math_Vector: ...
    def Minimum(self) -> float: 
        """
        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def NbIterations(self) -> int: 
        """
        returns the number of iterations really done during the computation of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the number of iterations really done during the computation of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def Perform(self,theFunction : math_MultipleVarFunctionWithGradient,theStartingPoint : math_Vector) -> None: 
        """
        The solution F = Fi is found when 2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1) + ZEPS).
        """
    def __init__(self,theFunction : math_MultipleVarFunctionWithGradient,theTolerance : float,theNbIterations : int=200,theZEPS : float=1e-12) -> None: ...
    pass
class math_Function():
    """
    This abstract class describes the virtual functions associated with a Function of a single variable.
    """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Computes the value of the function <F> for a given value of variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    pass
class math_FunctionAllRoots():
    """
    This algorithm uses a sample of the function to find all intervals on which the function is null, and afterwards uses the FunctionRoots algorithm to find the points where the function is null outside the "null intervals". Knowledge of the derivative is required.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object.
        """
    def GetInterval(self,Index : int) -> Tuple[float, float]: 
        """
        Returns the interval of parameter of range Index. An exception is raised if IsDone returns False; An exception is raised if Index<=0 or Index >Nbintervals.

        Returns the interval of parameter of range Index. An exception is raised if IsDone returns False; An exception is raised if Index<=0 or Index >Nbintervals.
        """
    def GetIntervalState(self,Index : int) -> Tuple[int, int]: 
        """
        returns the State Number associated to the interval Index. An exception is raised if IsDone returns False; An exception is raised if Index<=0 or Index >Nbintervals.

        returns the State Number associated to the interval Index. An exception is raised if IsDone returns False; An exception is raised if Index<=0 or Index >Nbintervals.
        """
    def GetPoint(self,Index : int) -> float: 
        """
        Returns the parameter of the point of range Index. An exception is raised if IsDone returns False; An exception is raised if Index<=0 or Index >NbPoints.

        Returns the parameter of the point of range Index. An exception is raised if IsDone returns False; An exception is raised if Index<=0 or Index >NbPoints.
        """
    def GetPointState(self,Index : int) -> int: 
        """
        returns the State Number associated to the point Index. An exception is raised if IsDone returns False; An exception is raised if Index<=0 or Index >Nbintervals.

        returns the State Number associated to the point Index. An exception is raised if IsDone returns False; An exception is raised if Index<=0 or Index >Nbintervals.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the computation has been done successfully.

        Returns True if the computation has been done successfully.
        """
    def NbIntervals(self) -> int: 
        """
        Returns the number of intervals on which the function is Null. An exception is raised if IsDone returns False.

        Returns the number of intervals on which the function is Null. An exception is raised if IsDone returns False.
        """
    def NbPoints(self) -> int: 
        """
        returns the number of points where the function is Null. An exception is raised if IsDone returns False.

        returns the number of points where the function is Null. An exception is raised if IsDone returns False.
        """
    def __init__(self,F : math_FunctionWithDerivative,S : math_FunctionSample,EpsX : float,EpsF : float,EpsNul : float) -> None: ...
    pass
class math_FunctionRoot():
    """
    This class implements the computation of a root of a function of a single variable which is near an initial guess using a minimization algorithm.Knowledge of the derivative is required. The algorithm used is the same as in
    """
    def Derivative(self) -> float: 
        """
        returns the value of the derivative at the root. Exception NotDone is raised if the root was not found.

        returns the value of the derivative at the root. Exception NotDone is raised if the root was not found.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def NbIterations(self) -> int: 
        """
        returns the number of iterations really done on the computation of the Root. Exception NotDone is raised if the root was not found.

        returns the number of iterations really done on the computation of the Root. Exception NotDone is raised if the root was not found.
        """
    def Root(self) -> float: 
        """
        returns the value of the root. Exception NotDone is raised if the root was not found.

        returns the value of the root. Exception NotDone is raised if the root was not found.
        """
    def Value(self) -> float: 
        """
        returns the value of the function at the root. Exception NotDone is raised if the root was not found.

        returns the value of the function at the root. Exception NotDone is raised if the root was not found.
        """
    @overload
    def __init__(self,F : math_FunctionWithDerivative,Guess : float,Tolerance : float,A : float,B : float,NbIterations : int=100) -> None: ...
    @overload
    def __init__(self,F : math_FunctionWithDerivative,Guess : float,Tolerance : float,NbIterations : int=100) -> None: ...
    pass
class math_FunctionRoots():
    """
    This class implements an algorithm which finds all the real roots of a function with derivative within a given range. Knowledge of the derivative is required.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object.
        """
    def IsAllNull(self) -> bool: 
        """
        returns true if the function is considered as null between A and B. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).

        returns true if the function is considered as null between A and B. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def NbSolutions(self) -> int: 
        """
        Returns the number of solutions found. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).

        Returns the number of solutions found. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """
    def StateNumber(self,Nieme : int) -> int: 
        """
        returns the StateNumber of the Nieme root. Exception RangeError is raised if Nieme is < 1 or Nieme > NbSolutions.

        returns the StateNumber of the Nieme root. Exception RangeError is raised if Nieme is < 1 or Nieme > NbSolutions.
        """
    def Value(self,Nieme : int) -> float: 
        """
        Returns the Nth value of the root of function F. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).

        Returns the Nth value of the root of function F. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """
    def __init__(self,F : math_FunctionWithDerivative,A : float,B : float,NbSample : int,EpsX : float=0.0,EpsF : float=0.0,EpsNull : float=0.0,K : float=0.0) -> None: ...
    pass
class math_FunctionSample():
    """
    This class gives a default sample (constant difference of parameter) for a function defined between two bound A,B.
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        Returns the bounds of parameters.
        """
    def GetParameter(self,Index : int) -> float: 
        """
        Returns the value of parameter of the point of range Index : A + ((Index-1)/(NbPoints-1))*B. An exception is raised if Index<=0 or Index>NbPoints.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of sample points.
        """
    def __init__(self,A : float,B : float,N : int) -> None: ...
    pass
class math_FunctionSet():
    """
    This abstract class describes the virtual functions associated to a set on N Functions of M independant variables.
    """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        Returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns the number of variables of the function.
        """
    def Value(self,X : math_Vector,F : math_Vector) -> bool: 
        """
        Computes the values <F> of the functions for the variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    pass
class math_FunctionSetRoot():
    """
    The math_FunctionSetRoot class calculates the root of a set of N functions of M variables (N<M, N=M or N>M). Knowing an initial guess of the solution and using a minimization algorithm, a search is made in the Newton direction and then in the Gradient direction if there is no success in the Newton direction. This algorithm can also be used for functions minimization. Knowledge of all the partial derivatives (the Jacobian) is required.
    """
    @overload
    def Derivative(self) -> math_Matrix: 
        """
        outputs the matrix value of the derivative at the root in Der. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the column range of <Der> is not equal to the range of the startingPoint.

        outputs the matrix value of the derivative at the root in Der. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the column range of <Der> is not equal to the range of the startingPoint.

        Returns the matrix value of the derivative at the root. Exception NotDone is raised if the root was not found.

        Returns the matrix value of the derivative at the root. Exception NotDone is raised if the root was not found.
        """
    @overload
    def Derivative(self,Der : math_Matrix) -> None: ...
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    @overload
    def FunctionSetErrors(self) -> math_Vector: 
        """
        outputs the vector value of the error done on the functions at the root in Err. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the range of Err is not equal to the range of the StartingPoint.

        returns the vector value of the error done on the functions at the root. Exception NotDone is raised if the root was not found.

        returns the vector value of the error done on the functions at the root. Exception NotDone is raised if the root was not found.
        """
    @overload
    def FunctionSetErrors(self,Err : math_Vector) -> None: ...
    def IsDivergent(self) -> bool: 
        """
        None

        None
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    @overload
    def IsSolutionReached(self,F : math_FunctionSetWithDerivatives) -> bool: 
        """
        This routine is called at the end of each iteration to check if the solution was found. It can be redefined in a sub-class to implement a specific test to stop the iterations. In this case, the solution is found when: abs(Xi - Xi-1) <= Tolerance for all unknowns.

        This routine is called at the end of each iteration to check if the solution was found. It can be redefined in a sub-class to implement a specific test to stop the iterations. In this case, the solution is found when: abs(Xi - Xi-1) <= Tolerance for all unknowns.
        """
    @overload
    def IsSolutionReached(self,arg1 : math_FunctionSetWithDerivatives) -> bool: ...
    def NbIterations(self) -> int: 
        """
        Returns the number of iterations really done during the computation of the root. Exception NotDone is raised if the root was not found.

        Returns the number of iterations really done during the computation of the root. Exception NotDone is raised if the root was not found.
        """
    @overload
    def Perform(self,theFunction : math_FunctionSetWithDerivatives,theStartingPoint : math_Vector,theInfBound : math_Vector,theSupBound : math_Vector,theStopOnDivergent : bool=False) -> None: 
        """
        Improves the root of function from the initial guess point. The infinum and supremum may be given to constrain the solution. In this case, the solution is found when: abs(Xi - Xi-1)(j) <= Tolerance(j) for all unknowns.

        Improves the root of function from the initial guess point. The infinum and supremum may be given to constrain the solution. In this case, the solution is found when: abs(Xi - Xi-1) <= Tolerance for all unknowns.
        """
    @overload
    def Perform(self,theFunction : math_FunctionSetWithDerivatives,theStartingPoint : math_Vector,theStopOnDivergent : bool=False) -> None: ...
    @overload
    def Root(self,Root : math_Vector) -> None: 
        """
        Outputs the root vector in Root. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the range of Root is not equal to the range of the StartingPoint.

        Returns the value of the root of function F. Exception NotDone is raised if the root was not found.

        Returns the value of the root of function F. Exception NotDone is raised if the root was not found.
        """
    @overload
    def Root(self) -> math_Vector: ...
    def SetTolerance(self,Tolerance : math_Vector) -> None: 
        """
        Initializes the tolerance values.
        """
    def StateNumber(self) -> int: 
        """
        returns the stateNumber (as returned by F.GetStateNumber()) associated to the root found.

        returns the stateNumber (as returned by F.GetStateNumber()) associated to the root found.
        """
    @overload
    def __init__(self,F : math_FunctionSetWithDerivatives,Tolerance : math_Vector,NbIterations : int=100) -> None: ...
    @overload
    def __init__(self,F : math_FunctionSetWithDerivatives,NbIterations : int=100) -> None: ...
    pass
class math_FunctionSetWithDerivatives(math_FunctionSet):
    """
    This abstract class describes the virtual functions associated with a set of N Functions each of M independant variables.
    """
    def Derivatives(self,X : math_Vector,D : math_Matrix) -> bool: 
        """
        Returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        Returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns the number of variables of the function.
        """
    def Value(self,X : math_Vector,F : math_Vector) -> bool: 
        """
        Computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : math_Vector,F : math_Vector,D : math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class math_FunctionWithDerivative(math_Function):
    """
    This abstract class describes the virtual functions associated with a function of a single variable for which the first derivative is available.
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        Computes the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Computes the value <F>of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        Computes the value <F> and the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    pass
class math_Gauss():
    """
    This class implements the Gauss LU decomposition (Crout algorithm) with partial pivoting (rows interchange) of a square matrix and the different possible derived calculation : - solution of a set of linear equations. - inverse of a matrix. - determinant of a matrix.
    """
    def Determinant(self) -> float: 
        """
        This routine returns the value of the determinant of the previously LU decomposed matrix A. Exception NotDone may be raised if the decomposition of A was not done successfully, zero is returned if the matrix A was considered as singular.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def Invert(self,Inv : math_Matrix) -> None: 
        """
        This routine outputs Inv the inverse of the previously LU decomposed matrix A. Exception DimensionError is raised if the ranges of B are not equal to the ranges of A.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false
        """
    @overload
    def Solve(self,B : math_Vector) -> None: 
        """
        Given the input Vector B this routine returns the solution X of the set of linear equations A . X = B. Exception NotDone is raised if the decomposition of A was not done successfully. Exception DimensionError is raised if the range of B is not equal to the number of rows of A.

        Given the input Vector B this routine solves the set of linear equations A . X = B. B is replaced by the vector solution X. Exception NotDone is raised if the decomposition of A was not done successfully. Exception DimensionError is raised if the range of B is not equal to the number of rows of A.
        """
    @overload
    def Solve(self,B : math_Vector,X : math_Vector) -> None: ...
    def __init__(self,A : math_Matrix,MinPivot : float=1e-20,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    pass
class math_GaussLeastSquare():
    """
    This class implements the least square solution of a set of n linear equations of m unknowns (n >= m) using the gauss LU decomposition algorithm. This algorithm is more likely subject to numerical instability than math_SVD.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.e

        Returns true if the computations are successful, otherwise returns false.e
        """
    def Solve(self,B : math_Vector,X : math_Vector) -> None: 
        """
        Given the input Vector <B> this routine solves the set of linear equations A . X = B. Exception NotDone is raised if the decomposition of A was not done successfully. Exception DimensionError is raised if the range of B Inv is not equal to the rowrange of A. Exception DimensionError is raised if the range of X Inv is not equal to the colrange of A.
        """
    def __init__(self,A : math_Matrix,MinPivot : float=1e-20) -> None: ...
    pass
class math_GaussMultipleIntegration():
    """
    This class implements the integration of a function of multiple variables between the parameter bounds Lower[a..b] and Upper[a..b]. Warning: Each element of Order must be inferior or equal to 61.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.

        returns True if all has been correctly done.
        """
    def Value(self) -> float: 
        """
        returns the value of the integral.

        returns the value of the integral.
        """
    def __init__(self,F : math_MultipleVarFunction,Lower : math_Vector,Upper : math_Vector,Order : math_IntegerVector) -> None: ...
    pass
class math_GaussSetIntegration():
    """
    -- This class implements the integration of a set of N functions of M variables variables between the parameter bounds Lower[a..b] and Upper[a..b]. Warning: - The case M>1 is not implemented.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.

        returns True if all has been correctly done.
        """
    def Value(self) -> math_Vector: 
        """
        returns the value of the integral.

        returns the value of the integral.
        """
    def __init__(self,F : math_FunctionSet,Lower : math_Vector,Upper : math_Vector,Order : math_IntegerVector) -> None: ...
    pass
class math_GaussSingleIntegration():
    """
    This class implements the integration of a function of a single variable between the parameter bounds Lower and Upper. Warning: Order must be inferior or equal to 61.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object.
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.

        returns True if all has been correctly done.
        """
    def Value(self) -> float: 
        """
        returns the value of the integral.

        returns the value of the integral.
        """
    @overload
    def __init__(self,F : math_Function,Lower : float,Upper : float,Order : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,F : math_Function,Lower : float,Upper : float,Order : int,Tol : float) -> None: ...
    pass
class math_GlobOptMin():
    """
    This class represents Evtushenko's algorithm of global optimization based on non-uniform mesh. Article: Yu. Evtushenko. Numerical methods for finding global extreme (case of a non-uniform mesh). U.S.S.R. Comput. Maths. Math. Phys., Vol. 11, N 6, pp. 38-54.
    """
    def GetContinuity(self) -> int: 
        """
        None
        """
    def GetF(self) -> float: 
        """
        Get best functional value.
        """
    def GetFunctionalMinimalValue(self) -> float: 
        """
        None
        """
    def GetLipConstState(self) -> bool: 
        """
        None
        """
    def GetTol(self) -> Tuple[float, float]: 
        """
        Method to get tolerances.
        """
    def NbExtrema(self) -> int: 
        """
        Return count of global extremas.
        """
    def Perform(self,isFindSingleSolution : bool=False) -> None: ...
    def Points(self,theIndex : int,theSol : math_Vector) -> None: 
        """
        Return solution theIndex, 1 <= theIndex <= NbExtrema.
        """
    def SetContinuity(self,theCont : int) -> None: 
        """
        Set / Get continuity of local borders splits (0 ~ C0, 1 ~ C1, 2 ~ C2).
        """
    def SetFunctionalMinimalValue(self,theMinimalValue : float) -> None: 
        """
        Set / Get functional minimal value.
        """
    def SetGlobalParams(self,theFunc : math_MultipleVarFunction,theLowerBorder : math_Vector,theUpperBorder : math_Vector,theC : float=9.0,theDiscretizationTol : float=0.01,theSameTol : float=1e-07) -> None: ...
    def SetLipConstState(self,theFlag : bool) -> None: 
        """
        Set / Get Lipchitz constant modification state. True means that the constant is locked and unlocked otherwise.
        """
    def SetLocalParams(self,theLocalA : math_Vector,theLocalB : math_Vector) -> None: 
        """
        Method to reduce bounding box. Perform will use this box.
        """
    def SetTol(self,theDiscretizationTol : float,theSameTol : float) -> None: 
        """
        Method to set tolerances.
        """
    def __init__(self,theFunc : math_MultipleVarFunction,theLowerBorder : math_Vector,theUpperBorder : math_Vector,theC : float=9.0,theDiscretizationTol : float=0.01,theSameTol : float=1e-07) -> None: ...
    def isDone(self) -> bool: 
        """
        Return computation state of the algorithm.
        """
    pass
class math_Householder():
    """
    This class implements the least square solution of a set of linear equations of m unknowns (n >= m) using the Householder method. It solves A.X = B. This algorithm has more numerical stability than GaussLeastSquare but is longer. It must be used if the matrix is singular or nearly singular. It is about 16% longer than GaussLeastSquare if there is only one member B to solve. It is about 30% longer if there are twenty B members to solve.
    """
    def AllValues(self) -> math_Matrix: 
        """
        Returns the matrix sol of all the solutions of the system A.X = B. Exception NotDone is raised is the resolution has not be done.

        Returns the matrix sol of all the solutions of the system A.X = B. Exception NotDone is raised is the resolution has not be done.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints informations on the current state of the object.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    @overload
    def Value(self,sol : math_Vector,Index : int) -> None: 
        """
        Given the integer Index, this routine returns the corresponding least square solution sol. Exception NotDone is raised if the resolution has not be done. Exception OutOfRange is raised if Index <=0 or Index is more than the number of columns of B.

        Given the integer Index, this routine returns the corresponding least square solution sol. Exception NotDone is raised if the resolution has not be done. Exception OutOfRange is raised if Index <=0 or Index is more than the number of columns of B.
        """
    @overload
    def Value(self,sol : math_Vector,Index : int=1) -> None: ...
    @overload
    def __init__(self,A : math_Matrix,B : math_Matrix,lowerArow : int,upperArow : int,lowerAcol : int,upperAcol : int,EPS : float=1e-20) -> None: ...
    @overload
    def __init__(self,A : math_Matrix,B : math_Matrix,EPS : float=1e-20) -> None: ...
    @overload
    def __init__(self,A : math_Matrix,B : math_Vector,EPS : float=1e-20) -> None: ...
    pass
class math_IntegerVector():
    """
    This class implements the real IntegerVector abstract data type. IntegerVectors can have an arbitrary range which must be define at the declaration and cannot be changed after this declaration. Example:
    """
    @overload
    def Add(self,theLeft : math_IntegerVector,theRight : math_IntegerVector) -> None: 
        """
        adds the IntegerVector "theRight" to an IntegerVector. An exception is raised if the IntegerVectors have not the same length. An exception is raised if the lengths are not equal.

        sets an IntegerVector to the sum of the IntegerVector "theLeft" and the IntegerVector "theRight". An exception is raised if the lengths are different.
        """
    @overload
    def Add(self,theRight : math_IntegerVector) -> None: ...
    def Added(self,theRight : math_IntegerVector) -> math_IntegerVector: 
        """
        adds the IntegerVector "theRight" to an IntegerVector. An exception is raised if the IntegerVectors have not the same length. An exception is raised if the lengths are not equal.
        """
    def Dump(self,theO : io.BytesIO) -> None: 
        """
        Prints on the stream theO information on the current state of the object. Is used to redefine the operator <<.
        """
    def Init(self,theInitialValue : int) -> None: 
        """
        Initialize an IntegerVector with all the elements set to theInitialValue.
        """
    def Initialized(self,theOther : math_IntegerVector) -> math_IntegerVector: 
        """
        Initialises an IntegerVector by copying "theOther". An exception is raised if the Lengths are different.
        """
    def Inverse(self) -> math_IntegerVector: 
        """
        returns the inverse IntegerVector of an IntegerVector.
        """
    def Invert(self) -> None: 
        """
        inverses an IntegerVector.
        """
    def Length(self) -> int: 
        """
        returns the length of an IntegerVector
        """
    def Lower(self) -> int: 
        """
        returns the value of the Lower index of an IntegerVector.
        """
    def Max(self) -> int: 
        """
        returns the value of the Index of the maximum element of an IntegerVector.
        """
    def Min(self) -> int: 
        """
        returns the value of the Index of the minimum element of an IntegerVector.
        """
    @overload
    def Multiplied(self,theRight : int) -> math_IntegerVector: 
        """
        returns the product of an IntegerVector by an integer value.

        returns the inner product of 2 IntegerVectors. An exception is raised if the lengths are not equal.
        """
    @overload
    def Multiplied(self,theRight : math_IntegerVector) -> int: ...
    @overload
    def Multiply(self,theRight : int) -> None: 
        """
        returns the product of an IntegerVector by an integer value.

        returns the multiplication of an integer by an IntegerVector.
        """
    @overload
    def Multiply(self,theLeft : int,theRight : math_IntegerVector) -> None: ...
    def Norm(self) -> float: 
        """
        returns the value of the norm of an IntegerVector.
        """
    def Norm2(self) -> float: 
        """
        returns the value of the square of the norm of an IntegerVector.
        """
    def Opposite(self) -> math_IntegerVector: 
        """
        returns the opposite of an IntegerVector.
        """
    def Set(self,theI1 : int,theI2 : int,theV : math_IntegerVector) -> None: 
        """
        sets an IntegerVector from "theI1" to "theI2" to the IntegerVector "theV"; An exception is raised if "theI1" is less than "LowerIndex" or "theI2" is greater than "UpperIndex" or "theI1" is greater than "theI2". An exception is raised if "theI2-theI1+1" is different from the Length of "theV".
        """
    def Slice(self,theI1 : int,theI2 : int) -> math_IntegerVector: 
        """
        slices the values of the IntegerVector between "theI1" and "theI2": Example: [2, 1, 2, 3, 4, 5] becomes [2, 4, 3, 2, 1, 5] between 2 and 5. An exception is raised if "theI1" is less than "LowerIndex" or "theI2" is greater than "UpperIndex".
        """
    @overload
    def Subtract(self,theLeft : math_IntegerVector,theRight : math_IntegerVector) -> None: 
        """
        sets an IntegerVector to the substraction of "theRight" from "theLeft". An exception is raised if the IntegerVectors have not the same length.

        returns the subtraction of "theRight" from "me". An exception is raised if the IntegerVectors have not the same length.
        """
    @overload
    def Subtract(self,theRight : math_IntegerVector) -> None: ...
    def Subtracted(self,theRight : math_IntegerVector) -> math_IntegerVector: 
        """
        returns the subtraction of "theRight" from "me". An exception is raised if the IntegerVectors have not the same length.
        """
    def TMultiplied(self,theRight : int) -> math_IntegerVector: 
        """
        returns the product of a vector and a real value.
        """
    def Upper(self) -> int: 
        """
        returns the value of the Upper index of an IntegerVector.
        """
    def Value(self,theNum : int) -> int: 
        """
        accesses the value of index theNum of an IntegerVector.
        """
    def __add__(self,theRight : math_IntegerVector) -> math_IntegerVector: 
        """
        None
        """
    def __iadd__(self,theRight : math_IntegerVector) -> None: 
        """
        None
        """
    def __imul__(self,theRight : int) -> None: 
        """
        None
        """
    @overload
    def __init__(self,theFirst : int,theLast : int) -> None: ...
    @overload
    def __init__(self,theFirst : int,theLast : int,theInitialValue : int) -> None: ...
    @overload
    def __init__(self,theTab : int,theFirst : int,theLast : int) -> None: ...
    @overload
    def __init__(self,theOther : math_IntegerVector) -> None: ...
    def __isub__(self,theRight : math_IntegerVector) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,theRight : int) -> math_IntegerVector: 
        """
        None

        None
        """
    @overload
    def __mul__(self,theRight : math_IntegerVector) -> int: ...
    @overload
    def __rmul__(self,theRight : int) -> math_IntegerVector: 
        """
        None

        None
        """
    @overload
    def __rmul__(self,theRight : math_IntegerVector) -> int: ...
    @overload
    def __sub__(self) -> math_IntegerVector: 
        """
        None

        None
        """
    @overload
    def __sub__(self,theRight : math_IntegerVector) -> math_IntegerVector: ...
    pass
class math_Jacobi():
    """
    This class implements the Jacobi method to find the eigenvalues and the eigenvectors of a real symmetric square matrix. A sort of eigenvalues is done.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object. Is used to redefine the operator <<.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def Value(self,Num : int) -> float: 
        """
        returns the eigenvalue number Num. Eigenvalues are in the range (1..n). Exception NotDone is raised if calculation is not done successfully.

        returns the eigenvalue number Num. Eigenvalues are in the range (1..n). Exception NotDone is raised if calculation is not done successfully.
        """
    def Values(self) -> math_Vector: 
        """
        Returns the eigenvalues vector. Exception NotDone is raised if calculation is not done successfully.

        Returns the eigenvalues vector. Exception NotDone is raised if calculation is not done successfully.
        """
    def Vector(self,Num : int,V : math_Vector) -> None: 
        """
        Returns the eigenvector V of number Num. Eigenvectors are in the range (1..n). Exception NotDone is raised if calculation is not done successfully.

        Returns the eigenvector V of number Num. Eigenvectors are in the range (1..n). Exception NotDone is raised if calculation is not done successfully.
        """
    def Vectors(self) -> math_Matrix: 
        """
        returns the eigenvectors matrix. Exception NotDone is raised if calculation is not done successfully.

        returns the eigenvectors matrix. Exception NotDone is raised if calculation is not done successfully.
        """
    def __init__(self,A : math_Matrix) -> None: ...
    pass
class math_KronrodSingleIntegration():
    """
    This class implements the Gauss-Kronrod method of integral computation.
    """
    def AbsolutError(self) -> float: 
        """
        Returns the value of the relative error reached.

        Returns the value of the relative error reached.
        """
    def ErrorReached(self) -> float: 
        """
        Returns the value of the relative error reached.

        Returns the value of the relative error reached.
        """
    @staticmethod
    def GKRule_s(theFunction : math_Function,theLower : float,theUpper : float,theGaussP : math_Vector,theGaussW : math_Vector,theKronrodP : math_Vector,theKronrodW : math_Vector,theValue : float,theError : float) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        Returns Standard_True if computation is performed successfully.

        Returns Standard_True if computation is performed successfully.
        """
    def NbIterReached(self) -> int: 
        """
        Returns the number of iterations that were made to compute result.

        Returns the number of iterations that were made to compute result.
        """
    def OrderReached(self) -> int: 
        """
        Returns the number of Kronrod points for which the result is computed.

        Returns the number of Kronrod points for which the result is computed.
        """
    @overload
    def Perform(self,theFunction : math_Function,theLower : float,theUpper : float,theNbPnts : int,theTolerance : float,theMaxNbIter : int) -> None: 
        """
        Computation of the integral. Takes the function, the lower and upper bound values, the initial number of Kronrod points, the relative tolerance value and the maximal number of iterations as parameters. theNbPnts should be odd and greater then or equal to 3.

        Computation of the integral. Takes the function, the lower and upper bound values, the initial number of Kronrod points, the relative tolerance value and the maximal number of iterations as parameters. theNbPnts should be odd and greater then or equal to 3. Note that theTolerance is relative, i.e. the criterion of solution reaching is: Abs(Kronrod - Gauss)/Abs(Kronrod) < theTolerance. theTolerance should be positive.
        """
    @overload
    def Perform(self,theFunction : math_Function,theLower : float,theUpper : float,theNbPnts : int) -> None: ...
    def Value(self) -> float: 
        """
        Returns the value of the integral.

        Returns the value of the integral.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theFunction : math_Function,theLower : float,theUpper : float,theNbPnts : int,theTolerance : float,theMaxNbIter : int) -> None: ...
    @overload
    def __init__(self,theFunction : math_Function,theLower : float,theUpper : float,theNbPnts : int) -> None: ...
    pass
class math_Matrix():
    """
    This class implements the real matrix abstract data type. Matrixes can have an arbitrary range which must be defined at the declaration and cannot be changed after this declaration math_Matrix(-3,5,2,4); //a vector with range [-3..5, 2..4] Matrix values may be initialized and retrieved using indexes which must lie within the range of definition of the matrix. Matrix objects follow "value semantics", that is, they cannot be shared and are copied through assignment Matrices are copied through assignement: math_Matrix M2(1, 9, 1, 3); ... M2 = M1; M1(1) = 2.0;//the matrix M2 will not be modified.
    """
    @overload
    def Add(self,Right : math_Matrix) -> None: 
        """
        adds the matrix <Right> to a matrix. An exception is raised if the dimensions are different. Warning In order to save time when copying matrices, it is preferable to use operator += or the function Add whenever possible.

        sets a matrix to the addition of <Left> and <Right>. An exception is raised if the dimensions are different.
        """
    @overload
    def Add(self,Left : math_Matrix,Right : math_Matrix) -> None: ...
    def Added(self,Right : math_Matrix) -> math_Matrix: 
        """
        adds the matrix <Right> to a matrix. An exception is raised if the dimensions are different.
        """
    def Col(self,Col : int) -> math_Vector: 
        """
        Returns the column of index <Col> of a matrix.
        """
    def ColNumber(self) -> int: 
        """
        Returns the number of rows of this matrix. Note that for a matrix A you always have the following relations: - A.RowNumber() = A.UpperRow() - A.LowerRow() + 1 - A.ColNumber() = A.UpperCol() - A.LowerCol() + 1 - the length of a row of A is equal to the number of columns of A, - the length of a column of A is equal to the number of rows of A.returns the row range of a matrix.

        Returns the number of rows of this matrix. Note that for a matrix A you always have the following relations: - A.RowNumber() = A.UpperRow() - A.LowerRow() + 1 - A.ColNumber() = A.UpperCol() - A.LowerCol() + 1 - the length of a row of A is equal to the number of columns of A, - the length of a column of A is equal to the number of rows of A.returns the row range of a matrix.
        """
    def Determinant(self) -> float: 
        """
        Computes the determinant of a matrix. An exception is raised if the matrix is not a square matrix.
        """
    def Divide(self,Right : float) -> None: 
        """
        divides all the elements of a matrix by the value <Right>. An exception is raised if <Right> = 0.
        """
    def Divided(self,Right : float) -> math_Matrix: 
        """
        divides all the elements of a matrix by the value <Right>. An exception is raised if <Right> = 0.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object. Is used to redefine the operator <<.
        """
    def Init(self,InitialValue : float) -> None: 
        """
        Initialize all the elements of a matrix to InitialValue.
        """
    def Initialized(self,Other : math_Matrix) -> math_Matrix: 
        """
        Matrixes are copied through assignement. An exception is raised if the dimensions are differents.
        """
    def Inverse(self) -> math_Matrix: 
        """
        Returns the inverse of a matrix. Exception NotSquare is raised if the matrix is not square. Exception SingularMatrix is raised if the matrix is singular.
        """
    def Invert(self) -> None: 
        """
        Inverts a matrix using Gauss algorithm. Exception NotSquare is raised if the matrix is not square. Exception SingularMatrix is raised if the matrix is singular.
        """
    def LowerCol(self) -> int: 
        """
        Returns the value of the Lower index of the column range of a matrix.

        Returns the value of the Lower index of the column range of a matrix.
        """
    def LowerRow(self) -> int: 
        """
        Returns the value of the Lower index of the row range of a matrix.

        Returns the value of the Lower index of the row range of a matrix.
        """
    @overload
    def Multiplied(self,Right : math_Vector) -> math_Vector: 
        """
        multiplies all the elements of a matrix by the value <Right>.

        Returns the product of 2 matrices. An exception is raised if the dimensions are different.

        Returns the product of a matrix by a vector. An exception is raised if the dimensions are different.
        """
    @overload
    def Multiplied(self,Right : math_Matrix) -> math_Matrix: ...
    @overload
    def Multiplied(self,Right : float) -> math_Matrix: ...
    @overload
    def Multiply(self,Left : math_Vector,Right : math_Vector) -> None: 
        """
        Sets this matrix to the product of the matrix Left, and the matrix Right. Example math_Matrix A (1, 3, 1, 3); math_Matrix B (1, 3, 1, 3); // A = ... , B = ... math_Matrix C (1, 3, 1, 3); C.Multiply(A, B); Exceptions Standard_DimensionError if matrices are of incompatible dimensions, i.e. if: - the number of columns of matrix Left, or the number of rows of matrix TLeft is not equal to the number of rows of matrix Right, or - the number of rows of matrix Left, or the number of columns of matrix TLeft is not equal to the number of rows of this matrix, or - the number of columns of matrix Right is not equal to the number of columns of this matrix.

        Computes a matrix as the product of 2 vectors. An exception is raised if the dimensions are different. <me> = <Left> * <Right>.

        Computes a matrix as the product of 2 matrixes. An exception is raised if the dimensions are different.

        Returns the product of 2 matrices. An exception is raised if the dimensions are different.
        """
    @overload
    def Multiply(self,Left : math_Matrix,Right : math_Matrix) -> None: ...
    @overload
    def Multiply(self,Right : float) -> None: ...
    @overload
    def Multiply(self,Right : math_Matrix) -> None: ...
    def Opposite(self) -> math_Matrix: 
        """
        Returns the opposite of a matrix. An exception is raised if the dimensions are different.
        """
    def Row(self,Row : int) -> math_Vector: 
        """
        Returns the row of index Row of a matrix.
        """
    def RowNumber(self) -> int: 
        """
        Returns the number of rows of this matrix. Note that for a matrix A you always have the following relations: - A.RowNumber() = A.UpperRow() - A.LowerRow() + 1 - A.ColNumber() = A.UpperCol() - A.LowerCol() + 1 - the length of a row of A is equal to the number of columns of A, - the length of a column of A is equal to the number of rows of A.returns the row range of a matrix.

        Returns the number of rows of this matrix. Note that for a matrix A you always have the following relations: - A.RowNumber() = A.UpperRow() - A.LowerRow() + 1 - A.ColNumber() = A.UpperCol() - A.LowerCol() + 1 - the length of a row of A is equal to the number of columns of A, - the length of a column of A is equal to the number of rows of A.returns the row range of a matrix.
        """
    def Set(self,I1 : int,I2 : int,J1 : int,J2 : int,M : math_Matrix) -> None: 
        """
        Sets the values of this matrix, - from index I1 to index I2 on the row dimension, and - from index J1 to index J2 on the column dimension, to those of matrix M. Exceptions Standard_DimensionError if: - I1 is less than the index of the lower row bound of this matrix, or - I2 is greater than the index of the upper row bound of this matrix, or - J1 is less than the index of the lower column bound of this matrix, or - J2 is greater than the index of the upper column bound of this matrix, or - I2 - I1 + 1 is not equal to the number of rows of matrix M, or - J2 - J1 + 1 is not equal to the number of columns of matrix M.
        """
    def SetCol(self,Col : int,V : math_Vector) -> None: 
        """
        Sets the column of index Col of a matrix to the vector <V>. An exception is raised if the dimensions are different. An exception is raises if <Col> is inferior to the lower column of the matrix or <Col> is superior to the upper column.
        """
    def SetDiag(self,Value : float) -> None: 
        """
        Sets the diagonal of a matrix to the value <Value>. An exception is raised if the matrix is not square.
        """
    def SetRow(self,Row : int,V : math_Vector) -> None: 
        """
        Sets the row of index Row of a matrix to the vector <V>. An exception is raised if the dimensions are different. An exception is raises if <Row> is inferior to the lower row of the matrix or <Row> is superior to the upper row.
        """
    @overload
    def Subtract(self,Left : math_Matrix,Right : math_Matrix) -> None: 
        """
        Subtracts the matrix <Right> from <me>. An exception is raised if the dimensions are different. Warning In order to avoid time-consuming copying of matrices, it is preferable to use operator -= or the function Subtract whenever possible.

        Sets a matrix to the Subtraction of the matrix <Right> from the matrix <Left>. An exception is raised if the dimensions are different.
        """
    @overload
    def Subtract(self,Right : math_Matrix) -> None: ...
    def Subtracted(self,Right : math_Matrix) -> math_Matrix: 
        """
        Returns the result of the subtraction of <Right> from <me>. An exception is raised if the dimensions are different.
        """
    def SwapCol(self,Col1 : int,Col2 : int) -> None: 
        """
        Swaps the columns of index <Col1> and <Col2>. An exception is raised if <Col1> or <Col2> is out of range.
        """
    def SwapRow(self,Row1 : int,Row2 : int) -> None: 
        """
        Swaps the rows of index Row1 and Row2. An exception is raised if <Row1> or <Row2> is out of range.
        """
    def TMultiplied(self,Right : float) -> math_Matrix: 
        """
        Sets this matrix to the product of the transposed matrix TLeft, and the matrix Right. Example math_Matrix A (1, 3, 1, 3); math_Matrix B (1, 3, 1, 3); // A = ... , B = ... math_Matrix C (1, 3, 1, 3); C.Multiply(A, B); Exceptions Standard_DimensionError if matrices are of incompatible dimensions, i.e. if: - the number of columns of matrix Left, or the number of rows of matrix TLeft is not equal to the number of rows of matrix Right, or - the number of rows of matrix Left, or the number of columns of matrix TLeft is not equal to the number of rows of this matrix, or - the number of columns of matrix Right is not equal to the number of columns of this matrix.
        """
    @overload
    def TMultiply(self,TLeft : math_Matrix,Right : math_Matrix) -> None: 
        """
        Returns the product of the transpose of a matrix with the matrix <Right>. An exception is raised if the dimensions are different.

        Computes a matrix to the product of the transpose of the matrix <TLeft> with the matrix <Right>. An exception is raised if the dimensions are different.
        """
    @overload
    def TMultiply(self,Right : math_Matrix) -> math_Matrix: ...
    def Transpose(self) -> None: 
        """
        Transposes a given matrix. An exception is raised if the matrix is not a square matrix.
        """
    def Transposed(self) -> math_Matrix: 
        """
        Teturns the transposed of a matrix. An exception is raised if the matrix is not a square matrix.
        """
    def UpperCol(self) -> int: 
        """
        Returns the value of the upper index of the column range of a matrix.

        Returns the value of the upper index of the column range of a matrix.
        """
    def UpperRow(self) -> int: 
        """
        Returns the Upper index of the row range of a matrix.

        Returns the Upper index of the row range of a matrix.
        """
    def Value(self,Row : int,Col : int) -> float: ...
    def __add__(self,Right : math_Matrix) -> math_Matrix: 
        """
        None
        """
    def __iadd__(self,Right : math_Matrix) -> None: 
        """
        None
        """
    @overload
    def __imul__(self,Right : math_Matrix) -> None: 
        """
        None

        None
        """
    @overload
    def __imul__(self,Right : float) -> None: ...
    @overload
    def __init__(self,LowerRow : int,UpperRow : int,LowerCol : int,UpperCol : int,InitialValue : float) -> None: ...
    @overload
    def __init__(self,Other : math_Matrix) -> None: ...
    @overload
    def __init__(self,Tab : capsule,LowerRow : int,UpperRow : int,LowerCol : int,UpperCol : int) -> None: ...
    @overload
    def __init__(self,LowerRow : int,UpperRow : int,LowerCol : int,UpperCol : int) -> None: ...
    def __isub__(self,Right : math_Matrix) -> None: 
        """
        None
        """
    def __itruediv__(self,Right : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,Right : math_Vector) -> math_Vector: 
        """
        None

        None

        None
        """
    @overload
    def __mul__(self,Right : math_Matrix) -> math_Matrix: ...
    @overload
    def __mul__(self,Right : float) -> math_Matrix: ...
    @overload
    def __rmul__(self,Right : math_Vector) -> math_Vector: 
        """
        None

        None

        None
        """
    @overload
    def __rmul__(self,Right : math_Matrix) -> math_Matrix: ...
    @overload
    def __rmul__(self,Right : float) -> math_Matrix: ...
    @overload
    def __sub__(self,Right : math_Matrix) -> math_Matrix: 
        """
        None

        None
        """
    @overload
    def __sub__(self) -> math_Matrix: ...
    def __truediv__(self,Right : float) -> math_Matrix: 
        """
        None
        """
    pass
class math_MultipleVarFunction():
    """
    Describes the virtual functions associated with a multiple variable function.
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbVariables(self) -> int: 
        """
        Returns the number of variables of the function
        """
    def Value(self,X : math_Vector,F : float) -> bool: 
        """
        Computes the values of the Functions <F> for the variable <X>. returns True if the computation was done successfully, otherwise false.
        """
    pass
class math_MultipleVarFunctionWithGradient(math_MultipleVarFunction):
    """
    The abstract class MultipleVarFunctionWithGradient describes the virtual functions associated with a multiple variable function.
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : math_Vector,G : math_Vector) -> bool: 
        """
        Computes the gradient <G> of the functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def NbVariables(self) -> int: 
        """
        Returns the number of variables of the function.
        """
    def Value(self,X : math_Vector,F : float) -> bool: 
        """
        Computes the values of the Functions <F> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : math_Vector,F : float,G : math_Vector) -> bool: 
        """
        computes the value <F> and the gradient <G> of the functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class math_MultipleVarFunctionWithHessian(math_MultipleVarFunctionWithGradient, math_MultipleVarFunction):
    """
    None
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : math_Vector,G : math_Vector) -> bool: 
        """
        computes the gradient <G> of the functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function.
        """
    def Value(self,X : math_Vector,F : float) -> bool: 
        """
        computes the values of the Functions <F> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    @overload
    def Values(self,X : math_Vector,F : float,G : math_Vector,H : math_Matrix) -> bool: 
        """
        computes the value <F> and the gradient <G> of the functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.

        computes the value <F>, the gradient <G> and the hessian <H> of the functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    @overload
    def Values(self,X : math_Vector,F : float,G : math_Vector) -> bool: ...
    pass
class math_NewtonFunctionRoot():
    """
    This class implements the calculation of a root of a function of a single variable starting from an initial near guess using the Newton algorithm. Knowledge of the derivative is required.
    """
    def Derivative(self) -> float: 
        """
        returns the value of the derivative at the root. Exception NotDone is raised if the root was not found.

        returns the value of the derivative at the root. Exception NotDone is raised if the root was not found.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def NbIterations(self) -> int: 
        """
        Returns the number of iterations really done on the computation of the Root. Exception NotDone is raised if the root was not found.

        Returns the number of iterations really done on the computation of the Root. Exception NotDone is raised if the root was not found.
        """
    def Perform(self,F : math_FunctionWithDerivative,Guess : float) -> None: 
        """
        is used internally by the constructors.
        """
    def Root(self) -> float: 
        """
        Returns the value of the root of function <F>. Exception NotDone is raised if the root was not found.

        Returns the value of the root of function <F>. Exception NotDone is raised if the root was not found.
        """
    def Value(self) -> float: 
        """
        returns the value of the function at the root. Exception NotDone is raised if the root was not found.

        returns the value of the function at the root. Exception NotDone is raised if the root was not found.
        """
    @overload
    def __init__(self,A : float,B : float,EpsX : float,EpsF : float,NbIterations : int=100) -> None: ...
    @overload
    def __init__(self,F : math_FunctionWithDerivative,Guess : float,EpsX : float,EpsF : float,A : float,B : float,NbIterations : int=100) -> None: ...
    @overload
    def __init__(self,F : math_FunctionWithDerivative,Guess : float,EpsX : float,EpsF : float,NbIterations : int=100) -> None: ...
    pass
class math_NewtonFunctionSetRoot():
    """
    This class computes the root of a set of N functions of N variables, knowing an initial guess at the solution and using the Newton Raphson algorithm. Knowledge of all the partial derivatives (Jacobian) is required.
    """
    @overload
    def Derivative(self) -> math_Matrix: 
        """
        Outputs the matrix value of the derivative at the root in Der. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the range of Der is not equal to the range of the StartingPoint.

        Outputs the matrix value of the derivative at the root in Der. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the range of Der is not equal to the range of the StartingPoint.

        Returns the matrix value of the derivative at the root. Exception NotDone is raised if the root was not found.

        Returns the matrix value of the derivative at the root. Exception NotDone is raised if the root was not found.
        """
    @overload
    def Derivative(self,Der : math_Matrix) -> None: ...
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object. Is used to redefine the operator <<.
        """
    @overload
    def FunctionSetErrors(self,Err : math_Vector) -> None: 
        """
        Outputs the vector value of the error done on the functions at the root in Err. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the range of Err is not equal to the range of the StartingPoint.

        Outputs the vector value of the error done on the functions at the root in Err. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the range of Err is not equal to the range of the StartingPoint.

        Returns the vector value of the error done on the functions at the root. Exception NotDone is raised if the root was not found.

        Returns the vector value of the error done on the functions at the root. Exception NotDone is raised if the root was not found.
        """
    @overload
    def FunctionSetErrors(self) -> math_Vector: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    @overload
    def IsSolutionReached(self,F : math_FunctionSetWithDerivatives) -> bool: 
        """
        This method is called at the end of each iteration to check if the solution is found. Vectors DeltaX, Fvalues and Jacobian Matrix are consistent with the possible solution Vector Sol and can be inspected to decide whether the solution is reached or not.

        This method is called at the end of each iteration to check if the solution is found. Vectors DeltaX, Fvalues and Jacobian Matrix are consistent with the possible solution Vector Sol and can be inspected to decide whether the solution is reached or not.
        """
    @overload
    def IsSolutionReached(self,arg1 : math_FunctionSetWithDerivatives) -> bool: ...
    def NbIterations(self) -> int: 
        """
        Returns the number of iterations really done during the computation of the Root. Exception NotDone is raised if the root was not found.

        Returns the number of iterations really done during the computation of the Root. Exception NotDone is raised if the root was not found.
        """
    @overload
    def Perform(self,theFunction : math_FunctionSetWithDerivatives,theStartingPoint : math_Vector,theInfBound : math_Vector,theSupBound : math_Vector) -> None: 
        """
        The Newton method is done to improve the root of the function from the initial guess point. The solution is found when: abs(Xj - Xj-1)(i) <= XTol(i) and abs(Fi) <= FTol for all i;

        The Newton method is done to improve the root of the function from the initial guess point. Bounds may be given, to constrain the solution. The solution is found when: abs(Xj - Xj-1)(i) <= XTol(i) and abs(Fi) <= FTol for all i;
        """
    @overload
    def Perform(self,theFunction : math_FunctionSetWithDerivatives,theStartingPoint : math_Vector) -> None: ...
    @overload
    def Root(self) -> math_Vector: 
        """
        outputs the root vector in Root. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the range of Root is not equal to the range of the StartingPoint.

        outputs the root vector in Root. Exception NotDone is raised if the root was not found. Exception DimensionError is raised if the range of Root is not equal to the range of the StartingPoint.

        Returns the value of the root of function F. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).

        Returns the value of the root of function F. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """
    @overload
    def Root(self,Root : math_Vector) -> None: ...
    def SetTolerance(self,XTol : math_Vector) -> None: 
        """
        Initializes the tolerance values for the unknowns.
        """
    @overload
    def __init__(self,theFunction : math_FunctionSetWithDerivatives,theFTolerance : float,theNbIterations : int=100) -> None: ...
    @overload
    def __init__(self,theFunction : math_FunctionSetWithDerivatives,theXTolerance : math_Vector,theFTolerance : float,tehNbIterations : int=100) -> None: ...
    pass
class math_NewtonMinimum():
    """
    None
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def GetStatus(self) -> math_Status: 
        """
        Returns the Status of computation. The exception NotDone is raised if an error has occured.

        Returns the Status of computation. The exception NotDone is raised if an error has occured.
        """
    @overload
    def Gradient(self,Grad : math_Vector) -> None: 
        """
        outputs the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        outputs the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        returns the gradient vector at the minimum. Exception NotDone is raised if an error has occured.the minimum was not found.

        returns the gradient vector at the minimum. Exception NotDone is raised if an error has occured.the minimum was not found.
        """
    @overload
    def Gradient(self) -> math_Vector: ...
    def IsConverged(self) -> bool: 
        """
        This method is called at the end of each iteration to check the convergence: || Xi+1 - Xi || < Tolerance or || F(Xi+1) - F(Xi)|| < Tolerance * || F(Xi) || It can be redefined in a sub-class to implement a specific test.

        This method is called at the end of each iteration to check the convergence: || Xi+1 - Xi || < Tolerance or || F(Xi+1) - F(Xi)|| < Tolerance * || F(Xi) || It can be redefined in a sub-class to implement a specific test.
        """
    def IsDone(self) -> bool: 
        """
        Tests if an error has occured.

        Tests if an error has occured.
        """
    @overload
    def Location(self) -> math_Vector: 
        """
        outputs the location vector of the minimum in Loc. Exception NotDone is raised if an error has occured. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        outputs the location vector of the minimum in Loc. Exception NotDone is raised if an error has occured. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        returns the location vector of the minimum. Exception NotDone is raised if an error has occured.

        returns the location vector of the minimum. Exception NotDone is raised if an error has occured.
        """
    @overload
    def Location(self,Loc : math_Vector) -> None: ...
    def Minimum(self) -> float: 
        """
        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def NbIterations(self) -> int: 
        """
        returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if an error has occured.

        returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if an error has occured.
        """
    def Perform(self,theFunction : math_MultipleVarFunctionWithHessian,theStartingPoint : math_Vector) -> None: 
        """
        Search the solution.
        """
    def SetBoundary(self,theLeftBorder : math_Vector,theRightBorder : math_Vector) -> None: 
        """
        Set boundaries.
        """
    def __init__(self,theFunction : math_MultipleVarFunctionWithHessian,theTolerance : float=1e-07,theNbIterations : int=40,theConvexity : float=1e-06,theWithSingularity : bool=True) -> None: ...
    pass
class math_NotSquare(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.math', '__weakref__': <attribute '__weakref__' of 'math_NotSquare' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'math_NotSquare' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class math_PSO():
    """
    In this class implemented variation of Particle Swarm Optimization (PSO) method. A. Ismael F. Vaz, L. N. Vicente "A particle swarm pattern search method for bound constrained global optimization"
    """
    @overload
    def Perform(self,theSteps : math_Vector,theOutPnt : math_Vector,theNbIter : int=100) -> Tuple[float]: 
        """
        Perform computations, particles array is constructed inside of this function.

        Perform computations with given particles array.
        """
    @overload
    def Perform(self,theParticles : math_PSOParticlesPool,theNbParticles : int,theOutPnt : math_Vector,theNbIter : int=100) -> Tuple[float]: ...
    def __init__(self,theFunc : math_MultipleVarFunction,theLowBorder : math_Vector,theUppBorder : math_Vector,theSteps : math_Vector,theNbParticles : int=32,theNbIter : int=100) -> None: ...
    pass
class math_PSOParticlesPool():
    """
    None
    """
    def GetBestParticle(self) -> PSO_Particle: 
        """
        None
        """
    def GetParticle(self,theIdx : int) -> PSO_Particle: 
        """
        None
        """
    def GetWorstParticle(self) -> PSO_Particle: 
        """
        None
        """
    def __init__(self,theParticlesCount : int,theDimensionCount : int) -> None: ...
    pass
class math_Powell():
    """
    This class implements the Powell method to find the minimum of function of multiple variables (the gradient does not have to be known).
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object. Is used to redefine the operator <<.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    @overload
    def IsSolutionReached(self,arg1 : math_MultipleVarFunction) -> bool: 
        """
        Solution F = Fi is found when: 2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1)) + ZEPS. The maximum number of iterations allowed is given by NbIterations.

        Solution F = Fi is found when: 2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1)) + ZEPS. The maximum number of iterations allowed is given by NbIterations.
        """
    @overload
    def IsSolutionReached(self,theFunction : math_MultipleVarFunction) -> bool: ...
    @overload
    def Location(self) -> math_Vector: 
        """
        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        outputs the location vector of the minimum in Loc. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the location vector of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    @overload
    def Location(self,Loc : math_Vector) -> None: ...
    def Minimum(self) -> float: 
        """
        Returns the value of the minimum. Exception NotDone is raised if the minimum was not found.

        Returns the value of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def NbIterations(self) -> int: 
        """
        Returns the number of iterations really done during the computation of the minimum. Exception NotDone is raised if the minimum was not found.

        Returns the number of iterations really done during the computation of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def Perform(self,theFunction : math_MultipleVarFunction,theStartingPoint : math_Vector,theStartingDirections : math_Matrix) -> None: 
        """
        Computes Powell minimization on the function F given theStartingPoint, and an initial matrix theStartingDirection whose columns contain the initial set of directions. The solution F = Fi is found when: 2.0 * abs(Fi - Fi-1) =< Tolerance * (abs(Fi) + abs(Fi-1) + ZEPS).
        """
    def __init__(self,theFunction : math_MultipleVarFunction,theTolerance : float,theNbIterations : int=200,theZEPS : float=1e-12) -> None: ...
    pass
class math_SVD():
    """
    SVD implements the solution of a set of N linear equations of M unknowns without condition on N or M. The Singular Value Decomposition algorithm is used. For singular or nearly singular matrices SVD is a better choice than Gauss or GaussLeastSquare.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object. Is used to redefine the operator <<.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def PseudoInverse(self,Inv : math_Matrix,Eps : float=1e-06) -> None: 
        """
        Computes the inverse Inv of matrix A such as A * Inverse = Identity. Exceptions StdFail_NotDone if the algorithm fails (and IsDone returns false). Standard_DimensionError if the ranges of Inv are compatible with the ranges of A.
        """
    def Solve(self,B : math_Vector,X : math_Vector,Eps : float=1e-06) -> None: 
        """
        Given the input Vector B this routine solves the set of linear equations A . X = B. Exception NotDone is raised if the decomposition of A was not done successfully. Exception DimensionError is raised if the range of B is not equal to the rowrange of A. Exception DimensionError is raised if the range of X is not equal to the colrange of A.
        """
    def __init__(self,A : math_Matrix) -> None: ...
    pass
class math_SingularMatrix(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.math', '__weakref__': <attribute '__weakref__' of 'math_SingularMatrix' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'math_SingularMatrix' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class math_Status():
    """
    None

    Members:

      math_OK

      math_TooManyIterations

      math_FunctionError

      math_DirectionSearchError

      math_NotBracketed
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
    __entries: dict # value = {'math_OK': (<math_Status.math_OK: 0>, None), 'math_TooManyIterations': (<math_Status.math_TooManyIterations: 1>, None), 'math_FunctionError': (<math_Status.math_FunctionError: 2>, None), 'math_DirectionSearchError': (<math_Status.math_DirectionSearchError: 3>, None), 'math_NotBracketed': (<math_Status.math_NotBracketed: 4>, None)}
    __members__: dict # value = {'math_OK': <math_Status.math_OK: 0>, 'math_TooManyIterations': <math_Status.math_TooManyIterations: 1>, 'math_FunctionError': <math_Status.math_FunctionError: 2>, 'math_DirectionSearchError': <math_Status.math_DirectionSearchError: 3>, 'math_NotBracketed': <math_Status.math_NotBracketed: 4>}
    math_DirectionSearchError: OCP.math.math_Status # value = <math_Status.math_DirectionSearchError: 3>
    math_FunctionError: OCP.math.math_Status # value = <math_Status.math_FunctionError: 2>
    math_NotBracketed: OCP.math.math_Status # value = <math_Status.math_NotBracketed: 4>
    math_OK: OCP.math.math_Status # value = <math_Status.math_OK: 0>
    math_TooManyIterations: OCP.math.math_Status # value = <math_Status.math_TooManyIterations: 1>
    pass
class math_TrigonometricEquationFunction(math_FunctionWithDerivative, math_Function):
    """
    This is function, which corresponds trigonometric equation a*Cos(x)*Cos(x) + 2*b*Cos(x)*Sin(x) + c*Cos(x) + d*Sin(x) + e = 0 See class math_TrigonometricFunctionRoots
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        None
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        None
        """
    def __init__(self,A : float,B : float,C : float,D : float,E : float) -> None: ...
    pass
class math_TrigonometricFunctionRoots():
    """
    This class implements the solutions of the equation a*Cos(x)*Cos(x) + 2*b*Cos(x)*Sin(x) + c*Cos(x) + d*Sin(x) + e The degree of this equation can be 4, 3 or 2.
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object.
        """
    def InfiniteRoots(self) -> bool: 
        """
        Returns true if there is an infinity of roots, otherwise returns false.

        Returns true if there is an infinity of roots, otherwise returns false.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def NbSolutions(self) -> int: 
        """
        Returns the number of solutions found. An exception is raised if NotDone. An exception is raised if there is an infinity of solutions.

        Returns the number of solutions found. An exception is raised if NotDone. An exception is raised if there is an infinity of solutions.
        """
    def Value(self,Index : int) -> float: 
        """
        Returns the solution of range Index. An exception is raised if NotDone. An exception is raised if Index>NbSolutions. An exception is raised if there is an infinity of solutions.

        Returns the solution of range Index. An exception is raised if NotDone. An exception is raised if Index>NbSolutions. An exception is raised if there is an infinity of solutions.
        """
    @overload
    def __init__(self,C : float,D : float,E : float,InfBound : float,SupBound : float) -> None: ...
    @overload
    def __init__(self,D : float,E : float,InfBound : float,SupBound : float) -> None: ...
    @overload
    def __init__(self,A : float,B : float,C : float,D : float,E : float,InfBound : float,SupBound : float) -> None: ...
    pass
class math_Uzawa():
    """
    This class implements a system resolution C*X = B with an approach solution X0. There are no conditions on the number of equations. The algorithm used is the Uzawa algorithm. It is possible to have equal or inequal (<) equations to solve. The resolution is done with a minimization of Norm(X-X0). If there are only equal equations, the resolution is directly done and is similar to Gauss resolution with an optimisation because the matrix is a symmetric matrix. (The resolution is done with Crout algorithm)
    """
    def Duale(self,V : math_Vector) -> None: 
        """
        returns the duale variables V of the systeme.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object.
        """
    def Error(self) -> math_Vector: 
        """
        Returns the difference between X solution and the StartingPoint. An exception is raised if NotDone.

        Returns the difference between X solution and the StartingPoint. An exception is raised if NotDone.
        """
    def InitialError(self) -> math_Vector: 
        """
        Returns the initial error Cont*StartingPoint-Secont. An exception is raised if NotDone.

        Returns the initial error Cont*StartingPoint-Secont. An exception is raised if NotDone.
        """
    def InverseCont(self) -> math_Matrix: 
        """
        returns the inverse matrix of (C * Transposed(C)). This result is needed for the computation of the gradient when approximating a curve.

        returns the inverse matrix of (C * Transposed(C)). This result is needed for the computation of the gradient when approximating a curve.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the computations are successful, otherwise returns false.

        Returns true if the computations are successful, otherwise returns false.
        """
    def NbIterations(self) -> int: 
        """
        returns the number of iterations really done. An exception is raised if NotDone.

        returns the number of iterations really done. An exception is raised if NotDone.
        """
    def Value(self) -> math_Vector: 
        """
        Returns the vector solution of the system above. An exception is raised if NotDone.

        Returns the vector solution of the system above. An exception is raised if NotDone.
        """
    @overload
    def __init__(self,Cont : math_Matrix,Secont : math_Vector,StartingPoint : math_Vector,EpsLix : float=1e-06,EpsLic : float=1e-06,NbIterations : int=500) -> None: ...
    @overload
    def __init__(self,Cont : math_Matrix,Secont : math_Vector,StartingPoint : math_Vector,Nci : int,Nce : int,EpsLix : float=1e-06,EpsLic : float=1e-06,NbIterations : int=500) -> None: ...
    pass
class math_ValueAndWeight():
    """
    Simple container storing two reals: value and weight
    """
    def Value(self) -> float: 
        """
        None
        """
    def Weight(self) -> float: 
        """
        None
        """
    @overload
    def __init__(self,theValue : float,theWeight : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class math_Vector():
    """
    This class implements the real vector abstract data type. Vectors can have an arbitrary range which must be defined at the declaration and cannot be changed after this declaration.
    """
    @overload
    def Add(self,theRight : math_Vector) -> None: 
        """
        adds the vector "theRight" to a vector. An exception is raised if the vectors have not the same length. Warning In order to avoid time-consuming copying of vectors, it is preferable to use operator += or the function Add whenever possible.

        sets a vector to the sum of the vector "theLeft" and the vector "theRight". An exception is raised if the lengths are different.
        """
    @overload
    def Add(self,theLeft : math_Vector,theRight : math_Vector) -> None: ...
    def Added(self,theRight : math_Vector) -> math_Vector: 
        """
        adds the vector theRight to a vector. An exception is raised if the vectors have not the same length. An exception is raised if the lengths are not equal.
        """
    def Divide(self,theRight : float) -> None: 
        """
        divides a vector by the value "theRight". An exception is raised if "theRight" = 0.
        """
    def Divided(self,theRight : float) -> math_Vector: 
        """
        divides a vector by the value "theRight". An exception is raised if "theRight" = 0.
        """
    def Dump(self,theO : io.BytesIO) -> None: 
        """
        Prints information on the current state of the object. Is used to redefine the operator <<.
        """
    def Init(self,theInitialValue : float) -> None: 
        """
        Initialize all the elements of a vector with "theInitialValue".
        """
    def Initialized(self,theOther : math_Vector) -> math_Vector: 
        """
        Initialises a vector by copying "theOther". An exception is raised if the Lengths are differents.
        """
    def Inverse(self) -> math_Vector: 
        """
        Inverts this vector and creates a new vector.
        """
    def Invert(self) -> None: 
        """
        Inverts this vector and assigns the result to this vector.
        """
    def Length(self) -> int: 
        """
        Returns the length of a vector
        """
    def Lower(self) -> int: 
        """
        Returns the value of the theLower index of a vector.
        """
    def Max(self) -> int: 
        """
        Returns the value of the "Index" of the maximum element of a vector.
        """
    def Min(self) -> int: 
        """
        Returns the value of the "Index" of the minimum element of a vector.
        """
    @overload
    def Multiplied(self,theRight : float) -> math_Vector: 
        """
        returns the product of a vector and a real value.

        returns the inner product of 2 vectors. An exception is raised if the lengths are not equal.

        returns the product of a vector by a matrix.
        """
    @overload
    def Multiplied(self,theRight : math_Vector) -> float: ...
    @overload
    def Multiplied(self,theRight : math_Matrix) -> math_Vector: ...
    @overload
    def Multiply(self,theRight : float) -> None: 
        """
        returns the product of a vector and a real value.

        sets a vector to the product of the vector "theLeft" with the matrix "theRight".

        sets a vector to the product of the matrix "theLeft" with the vector "theRight".

        returns the multiplication of a real by a vector. "me" = "theLeft" * "theRight"
        """
    @overload
    def Multiply(self,theLeft : float,theRight : math_Vector) -> None: ...
    @overload
    def Multiply(self,theLeft : math_Matrix,theRight : math_Vector) -> None: ...
    @overload
    def Multiply(self,theLeft : math_Vector,theRight : math_Matrix) -> None: ...
    def Norm(self) -> float: 
        """
        Returns the value or the square of the norm of this vector.
        """
    def Norm2(self) -> float: 
        """
        Returns the value of the square of the norm of a vector.
        """
    def Normalize(self) -> None: 
        """
        Normalizes this vector (the norm of the result is equal to 1.0) and assigns the result to this vector Exceptions Standard_NullValue if this vector is null (i.e. if its norm is less than or equal to Standard_Real::RealEpsilon().
        """
    def Normalized(self) -> math_Vector: 
        """
        Normalizes this vector (the norm of the result is equal to 1.0) and creates a new vector Exceptions Standard_NullValue if this vector is null (i.e. if its norm is less than or equal to Standard_Real::RealEpsilon().
        """
    def Opposite(self) -> math_Vector: 
        """
        returns the opposite of a vector.
        """
    def Set(self,theI1 : int,theI2 : int,theV : math_Vector) -> None: 
        """
        sets a vector from "theI1" to "theI2" to the vector "theV"; An exception is raised if "theI1" is less than "LowerIndex" or "theI2" is greater than "UpperIndex" or "theI1" is greater than "theI2". An exception is raised if "theI2-theI1+1" is different from the "Length" of "theV".
        """
    def Slice(self,theI1 : int,theI2 : int) -> math_Vector: 
        """
        Creates a new vector by inverting the values of this vector between indexes "theI1" and "theI2". If the values of this vector were (1., 2., 3., 4.,5., 6.), by slicing it between indexes 2 and 5 the values of the resulting vector are (1., 5., 4., 3., 2., 6.)
        """
    @overload
    def Subtract(self,theRight : math_Vector) -> None: 
        """
        sets a vector to the Subtraction of the vector theRight from the vector theLeft. An exception is raised if the vectors have not the same length. Warning In order to avoid time-consuming copying of vectors, it is preferable to use operator -= or the function Subtract whenever possible.

        returns the subtraction of "theRight" from "me". An exception is raised if the vectors have not the same length.
        """
    @overload
    def Subtract(self,theLeft : math_Vector,theRight : math_Vector) -> None: ...
    def Subtracted(self,theRight : math_Vector) -> math_Vector: 
        """
        returns the subtraction of "theRight" from "me". An exception is raised if the vectors have not the same length.
        """
    def TMultiplied(self,theRight : float) -> math_Vector: 
        """
        returns the product of a vector and a real value.
        """
    @overload
    def TMultiply(self,theTLeft : math_Matrix,theRight : math_Vector) -> None: 
        """
        sets a vector to the product of the transpose of the matrix "theTLeft" by the vector "theRight".

        sets a vector to the product of the vector "theLeft" by the transpose of the matrix "theTRight".
        """
    @overload
    def TMultiply(self,theLeft : math_Vector,theTRight : math_Matrix) -> None: ...
    def Upper(self) -> int: 
        """
        Returns the value of the theUpper index of a vector.
        """
    def Value(self,theNum : int) -> float: 
        """
        accesses the value of index "theNum" of a vector.
        """
    def __add__(self,theRight : math_Vector) -> math_Vector: 
        """
        None
        """
    def __iadd__(self,theRight : math_Vector) -> None: 
        """
        None
        """
    def __imul__(self,theRight : float) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Other : OCP.gp.gp_XY) -> None: ...
    @overload
    def __init__(self,theTab : float,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : math_Vector) -> None: ...
    @overload
    def __init__(self,Other : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theInitialValue : float) -> None: ...
    def __isub__(self,theRight : math_Vector) -> None: 
        """
        None
        """
    def __itruediv__(self,theRight : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,theRight : float) -> math_Vector: 
        """
        None

        None

        None
        """
    @overload
    def __mul__(self,theRight : math_Vector) -> float: ...
    @overload
    def __mul__(self,theRight : math_Matrix) -> math_Vector: ...
    @overload
    def __rmul__(self,theRight : float) -> math_Vector: 
        """
        None

        None

        None
        """
    @overload
    def __rmul__(self,theRight : math_Matrix) -> math_Vector: ...
    @overload
    def __rmul__(self,theRight : math_Vector) -> float: ...
    @overload
    def __sub__(self) -> math_Vector: 
        """
        None

        None
        """
    @overload
    def __sub__(self,theRight : math_Vector) -> math_Vector: ...
    def __truediv__(self,theRight : float) -> math_Vector: 
        """
        None
        """
    pass
def DACTCL_Decompose(a : math_Vector,indx : math_IntegerVector,MinPivot : float=1e-20) -> int:
    """
    None
    """
def DACTCL_Solve(a : math_Vector,b : math_Vector,indx : math_IntegerVector,MinPivot : float=1e-20) -> int:
    """
    None
    """
def Jacobi(a : math_Matrix,d : math_Vector,v : math_Matrix,nrot : int) -> int:
    """
    None
    """
@overload
def LU_Decompose(a : math_Matrix,indx : math_IntegerVector,d : float,vv : math_Vector,TINY : float=1e-30,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int:
    """
    None

    None
    """
@overload
def LU_Decompose(a : math_Matrix,indx : math_IntegerVector,d : float,TINY : float=1e-20,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int:
    pass
def LU_Invert(a : math_Matrix) -> int:
    """
    None
    """
def LU_Solve(a : math_Matrix,indx : math_IntegerVector,b : math_Vector) -> None:
    """
    None
    """
@overload
def SVD_Decompose(a : math_Matrix,w : math_Vector,v : math_Matrix) -> int:
    """
    None

    None
    """
@overload
def SVD_Decompose(a : math_Matrix,w : math_Vector,v : math_Matrix,rv1 : math_Vector) -> int:
    pass
def SVD_Solve(u : math_Matrix,w : math_Vector,v : math_Matrix,b : math_Vector,x : math_Vector) -> None:
    """
    None
    """
def __mul__(Left : float,Right : math_Matrix) -> math_Matrix:
    """
    None
    """
def __rmul__(Left : float,Right : math_Matrix) -> math_Matrix:
    """
    None
    """
math_DirectionSearchError: OCP.math.math_Status # value = <math_Status.math_DirectionSearchError: 3>
math_FunctionError: OCP.math.math_Status # value = <math_Status.math_FunctionError: 2>
math_NotBracketed: OCP.math.math_Status # value = <math_Status.math_NotBracketed: 4>
math_OK: OCP.math.math_Status # value = <math_Status.math_OK: 0>
math_TooManyIterations: OCP.math.math_Status # value = <math_Status.math_TooManyIterations: 1>
