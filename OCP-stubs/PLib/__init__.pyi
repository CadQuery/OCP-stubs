import OCP.PLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.GeomAbs
import OCP.TColgp
import OCP.Standard
import OCP.math
__all__  = [
"PLib",
"PLib_Base",
"PLib_DoubleJacobiPolynomial",
"PLib_HermitJacobi",
"PLib_JacobiPolynomial"
]
class PLib():
    """
    PLib means Polynomial functions library. This pk provides basic computation functions for polynomial functions. Note: weight arrays can be passed by pointer for some functions so that NULL pointer is valid. That means no weights passed.
    """
    @staticmethod
    def Bin_s(N : int,P : int) -> float: 
        """
        Returns the Binomial Cnp. N should be <= BSplCLib::MaxDegree().
        """
    @staticmethod
    @overload
    def CoefficientsPoles_s(Coefs : OCP.TColStd.TColStd_Array1OfReal,WCoefs : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColStd.TColStd_Array1OfReal,WPoles : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def CoefficientsPoles_s(dim : int,Coefs : OCP.TColStd.TColStd_Array1OfReal,WCoefs : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColStd.TColStd_Array1OfReal,WPoles : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def CoefficientsPoles_s(Coefs : OCP.TColgp.TColgp_Array1OfPnt2d,WCoefs : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,WPoles : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def CoefficientsPoles_s(Coefs : OCP.TColgp.TColgp_Array1OfPnt,WCoefs : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt,WPoles : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def CoefficientsPoles_s(Coefs : OCP.TColgp.TColgp_Array2OfPnt,WCoefs : OCP.TColStd.TColStd_Array2OfReal,Poles : OCP.TColgp.TColgp_Array2OfPnt,WPoles : OCP.TColStd.TColStd_Array2OfReal) -> None: ...
    @staticmethod
    def ConstraintOrder_s(NivConstr : int) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        translates from Integer to GeomAbs_Shape
        """
    @staticmethod
    def EvalCubicHermite_s(U : float,DerivativeOrder : int,Dimension : int,ValueArray : float,DerivativeArray : float,ParameterArray : float,Results : float) -> int: 
        """
        Performs the Cubic Hermite Interpolation of given series of points with given parameters with the requested derivative order. ValueArray stores the value at the first and last parameter. It has the following format : [0], [Dimension-1] : value at first param [Dimension], [Dimension + Dimension-1] : value at last param Derivative array stores the value of the derivatives at the first parameter and at the last parameter in the following format [0], [Dimension-1] : derivative at first param [Dimension], [Dimension + Dimension-1] : derivative at last param
        """
    @staticmethod
    def EvalLagrange_s(U : float,DerivativeOrder : int,Degree : int,Dimension : int,ValueArray : float,ParameterArray : float,Results : float) -> int: 
        """
        Performs the Lagrange Interpolation of given series of points with given parameters with the requested derivative order Results will store things in the following format with d = DerivativeOrder
        """
    @staticmethod
    @overload
    def EvalLength_s(Degree : int,Dimension : int,U1 : float,U2 : float,Tol : float) -> Tuple[float, float, float]: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def EvalLength_s(Degree : int,Dimension : int,U1 : float,U2 : float) -> Tuple[float, float]: ...
    @staticmethod
    def EvalPoly2Var_s(U : float,V : float,UDerivativeOrder : int,VDerivativeOrder : int,UDegree : int,VDegree : int,Dimension : int) -> Tuple[float, float]: 
        """
        Applies EvalPolynomial twice to evaluate the derivative of orders UDerivativeOrder in U, VDerivativeOrder in V at parameters U,V
        """
    @staticmethod
    def EvalPolynomial_s(U : float,DerivativeOrder : int,Degree : int,Dimension : int) -> Tuple[float, float]: 
        """
        Performs Horner method with synthethic division for derivatives parameter <U>, with <Degree> and <Dimension>. PolynomialCoeff are stored in the following fashion c0(1) c0(2) .... c0(Dimension) c1(1) c1(2) .... c1(Dimension)
        """
    @staticmethod
    @overload
    def GetPoles_s(FP : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Get from FP the coordinates of the poles.

        Get from FP the coordinates of the poles.

        Get from FP the coordinates of the poles.

        Get from FP the coordinates of the poles.
        """
    @staticmethod
    @overload
    def GetPoles_s(FP : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def GetPoles_s(FP : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @staticmethod
    @overload
    def GetPoles_s(FP : OCP.TColStd.TColStd_Array1OfReal,Poles : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @staticmethod
    def HermiteCoefficients_s(FirstParameter : float,LastParameter : float,FirstOrder : int,LastOrder : int,MatrixCoefs : OCP.math.math_Matrix) -> bool: 
        """
        This build the coefficient of Hermite's polynomes on [FirstParameter, LastParameter]
        """
    @staticmethod
    def HermiteInterpolate_s(Dimension : int,FirstParameter : float,LastParameter : float,FirstOrder : int,LastOrder : int,FirstConstr : OCP.TColStd.TColStd_Array2OfReal,LastConstr : OCP.TColStd.TColStd_Array2OfReal,Coefficients : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Compute the coefficients in the canonical base of the polynomial satisfying the given constraints at the given parameters The array FirstContr(i,j) i=1,Dimension j=0,FirstOrder contains the values of the constraint at parameter FirstParameter idem for LastConstr
        """
    @staticmethod
    def JacobiParameters_s(ConstraintOrder : OCP.GeomAbs.GeomAbs_Shape,MaxDegree : int,Code : int) -> Tuple[int, int]: 
        """
        Compute the number of points used for integral computations (NbGaussPoints) and the degree of Jacobi Polynomial (WorkDegree). ConstraintOrder has to be GeomAbs_C0, GeomAbs_C1 or GeomAbs_C2 Code: Code d' init. des parametres de discretisation. = -5 = -4 = -3 = -2 = -1 = 1 calcul rapide avec precision moyenne. = 2 calcul rapide avec meilleure precision. = 3 calcul un peu plus lent avec bonne precision. = 4 calcul lent avec la meilleure precision possible.
        """
    @staticmethod
    def NivConstr_s(ConstraintOrder : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        translates from GeomAbs_Shape to Integer
        """
    @staticmethod
    def NoDerivativeEvalPolynomial_s(U : float,Degree : int,Dimension : int,DegreeDimension : int) -> Tuple[float, float]: 
        """
        Same as above with DerivativeOrder = 0;
        """
    @staticmethod
    def NoWeights2_s() -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        Used as argument for a non rational functions
        """
    @staticmethod
    def NoWeights_s() -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Used as argument for a non rational functions
        """
    @staticmethod
    def RationalDerivative_s(Degree : int,N : int,Dimension : int,All : bool=True) -> Tuple[float, float]: 
        """
        Computes the derivatives of a ratio at order <N> in dimension <Dimension>.
        """
    @staticmethod
    def RationalDerivatives_s(DerivativesRequest : int,Dimension : int) -> Tuple[float, float, float]: 
        """
        Computes DerivativesRequest derivatives of a ratio at of a BSpline function of degree <Degree> dimension <Dimension>.
        """
    @staticmethod
    @overload
    def SetPoles_s(Poles : OCP.TColgp.TColgp_Array1OfPnt,FP : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Copy in FP the coordinates of the poles.

        Copy in FP the coordinates of the poles.

        Copy in FP the coordinates of the poles.

        Copy in FP the coordinates of the poles.
        """
    @staticmethod
    @overload
    def SetPoles_s(Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,FP : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def SetPoles_s(Poles : OCP.TColgp.TColgp_Array1OfPnt2d,FP : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def SetPoles_s(Poles : OCP.TColgp.TColgp_Array1OfPnt2d,Weights : OCP.TColStd.TColStd_Array1OfReal,FP : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def Trimming_s(U1 : float,U2 : float,Coeffs : OCP.TColgp.TColgp_Array1OfPnt,WCoeffs : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def Trimming_s(U1 : float,U2 : float,Coeffs : OCP.TColgp.TColgp_Array1OfPnt2d,WCoeffs : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def Trimming_s(U1 : float,U2 : float,dim : int,Coeffs : OCP.TColStd.TColStd_Array1OfReal,WCoeffs : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    @overload
    def Trimming_s(U1 : float,U2 : float,Coeffs : OCP.TColStd.TColStd_Array1OfReal,WCoeffs : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @staticmethod
    def UTrimming_s(U1 : float,U2 : float,Coeffs : OCP.TColgp.TColgp_Array2OfPnt,WCoeffs : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        None
        """
    @staticmethod
    def VTrimming_s(V1 : float,V2 : float,Coeffs : OCP.TColgp.TColgp_Array2OfPnt,WCoeffs : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class PLib_Base(OCP.Standard.Standard_Transient):
    """
    To work with different polynomial's BasesTo work with different polynomial's BasesTo work with different polynomial's Bases
    """
    def D0(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values of the basis functions in u
        """
    def D1(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal,BasisD1 : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values and the derivatives values of the basis functions in u
        """
    def D2(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal,BasisD1 : OCP.TColStd.TColStd_Array1OfReal,BasisD2 : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values and the derivatives values of the basis functions in u
        """
    def D3(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal,BasisD1 : OCP.TColStd.TColStd_Array1OfReal,BasisD2 : OCP.TColStd.TColStd_Array1OfReal,BasisD3 : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values and the derivatives values of the basis functions in u
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
    def ReduceDegree(self,Dimension : int,MaxDegree : int,Tol : float) -> Tuple[float, int, float]: 
        """
        Compute NewDegree <= MaxDegree so that MaxError is lower than Tol. MaxError can be greater than Tol if it is not possible to find a NewDegree <= MaxDegree. In this case NewDegree = MaxDegree
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToCoefficients(self,Dimension : int,Degree : int,CoeffinBase : OCP.TColStd.TColStd_Array1OfReal,Coefficients : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Convert the polynomial P(t) in the canonical base.
        """
    def WorkDegree(self) -> int: 
        """
        returns WorkDegree
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
class PLib_DoubleJacobiPolynomial():
    """
    None
    """
    def AverageError(self,Dimension : int,DegreeU : int,DegreeV : int,dJacCoeff : int,JacCoeff : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        None
        """
    def MaxError(self,Dimension : int,MinDegreeU : int,MaxDegreeU : int,MinDegreeV : int,MaxDegreeV : int,dJacCoeff : int,JacCoeff : OCP.TColStd.TColStd_Array1OfReal,Error : float) -> float: 
        """
        None
        """
    def MaxErrorU(self,Dimension : int,DegreeU : int,DegreeV : int,dJacCoeff : int,JacCoeff : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        None
        """
    def MaxErrorV(self,Dimension : int,DegreeU : int,DegreeV : int,dJacCoeff : int,JacCoeff : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        None
        """
    def ReduceDegree(self,Dimension : int,MinDegreeU : int,MaxDegreeU : int,MinDegreeV : int,MaxDegreeV : int,dJacCoeff : int,JacCoeff : OCP.TColStd.TColStd_Array1OfReal,EpmsCut : float) -> Tuple[float, int, int]: 
        """
        None
        """
    def TabMaxU(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns myTabMaxU;

        returns myTabMaxU;
        """
    def TabMaxV(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns myTabMaxV;

        returns myTabMaxV;
        """
    def U(self) -> PLib_JacobiPolynomial: 
        """
        returns myJacPolU;

        returns myJacPolU;
        """
    def V(self) -> PLib_JacobiPolynomial: 
        """
        returns myJacPolV;

        returns myJacPolV;
        """
    def WDoubleJacobiToCoefficients(self,Dimension : int,DegreeU : int,DegreeV : int,JacCoeff : OCP.TColStd.TColStd_Array1OfReal,Coefficients : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,JacPolU : PLib_JacobiPolynomial,JacPolV : PLib_JacobiPolynomial) -> None: ...
    pass
class PLib_HermitJacobi(PLib_Base, OCP.Standard.Standard_Transient):
    """
    This class provides method to work with Jacobi Polynomials relativly to an order of constraint q = myWorkDegree-2*(myNivConstr+1) Jk(t) for k=0,q compose the Jacobi Polynomial base relativly to the weigth W(t) iorder is the integer value for the constraints: iorder = 0 <=> ConstraintOrder = GeomAbs_C0 iorder = 1 <=> ConstraintOrder = GeomAbs_C1 iorder = 2 <=> ConstraintOrder = GeomAbs_C2 P(t) = H(t) + W(t) * Q(t) Where W(t) = (1-t**2)**(2*iordre+2) the coefficients JacCoeff represents P(t) JacCoeff are stored as follow:This class provides method to work with Jacobi Polynomials relativly to an order of constraint q = myWorkDegree-2*(myNivConstr+1) Jk(t) for k=0,q compose the Jacobi Polynomial base relativly to the weigth W(t) iorder is the integer value for the constraints: iorder = 0 <=> ConstraintOrder = GeomAbs_C0 iorder = 1 <=> ConstraintOrder = GeomAbs_C1 iorder = 2 <=> ConstraintOrder = GeomAbs_C2 P(t) = H(t) + W(t) * Q(t) Where W(t) = (1-t**2)**(2*iordre+2) the coefficients JacCoeff represents P(t) JacCoeff are stored as follow:This class provides method to work with Jacobi Polynomials relativly to an order of constraint q = myWorkDegree-2*(myNivConstr+1) Jk(t) for k=0,q compose the Jacobi Polynomial base relativly to the weigth W(t) iorder is the integer value for the constraints: iorder = 0 <=> ConstraintOrder = GeomAbs_C0 iorder = 1 <=> ConstraintOrder = GeomAbs_C1 iorder = 2 <=> ConstraintOrder = GeomAbs_C2 P(t) = H(t) + W(t) * Q(t) Where W(t) = (1-t**2)**(2*iordre+2) the coefficients JacCoeff represents P(t) JacCoeff are stored as follow:
    """
    def AverageError(self,Dimension : int,HermJacCoeff : float,NewDegree : int) -> float: 
        """
        None
        """
    def D0(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values of the basis functions in u
        """
    def D1(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal,BasisD1 : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values and the derivatives values of the basis functions in u
        """
    def D2(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal,BasisD1 : OCP.TColStd.TColStd_Array1OfReal,BasisD2 : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values and the derivatives values of the basis functions in u
        """
    def D3(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal,BasisD1 : OCP.TColStd.TColStd_Array1OfReal,BasisD2 : OCP.TColStd.TColStd_Array1OfReal,BasisD3 : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values and the derivatives values of the basis functions in u
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
    def MaxError(self,Dimension : int,HermJacCoeff : float,NewDegree : int) -> float: 
        """
        This method computes the maximum error on the polynomial W(t) Q(t) obtained by missing the coefficients of JacCoeff from NewDegree +1 to Degree
        """
    def NivConstr(self) -> int: 
        """
        returns NivConstr

        returns NivConstr
        """
    def ReduceDegree(self,Dimension : int,MaxDegree : int,Tol : float) -> Tuple[float, int, float]: 
        """
        Compute NewDegree <= MaxDegree so that MaxError is lower than Tol. MaxError can be greater than Tol if it is not possible to find a NewDegree <= MaxDegree. In this case NewDegree = MaxDegree
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToCoefficients(self,Dimension : int,Degree : int,HermJacCoeff : OCP.TColStd.TColStd_Array1OfReal,Coefficients : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Convert the polynomial P(t) = H(t) + W(t) Q(t) in the canonical base.
        """
    def WorkDegree(self) -> int: 
        """
        returns WorkDegree

        returns WorkDegree
        """
    def __init__(self,WorkDegree : int,ConstraintOrder : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
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
class PLib_JacobiPolynomial(PLib_Base, OCP.Standard.Standard_Transient):
    """
    This class provides method to work with Jacobi Polynomials relativly to an order of constraint q = myWorkDegree-2*(myNivConstr+1) Jk(t) for k=0,q compose the Jacobi Polynomial base relativly to the weigth W(t) iorder is the integer value for the constraints: iorder = 0 <=> ConstraintOrder = GeomAbs_C0 iorder = 1 <=> ConstraintOrder = GeomAbs_C1 iorder = 2 <=> ConstraintOrder = GeomAbs_C2 P(t) = R(t) + W(t) * Q(t) Where W(t) = (1-t**2)**(2*iordre+2) the coefficients JacCoeff represents P(t) JacCoeff are stored as follow:This class provides method to work with Jacobi Polynomials relativly to an order of constraint q = myWorkDegree-2*(myNivConstr+1) Jk(t) for k=0,q compose the Jacobi Polynomial base relativly to the weigth W(t) iorder is the integer value for the constraints: iorder = 0 <=> ConstraintOrder = GeomAbs_C0 iorder = 1 <=> ConstraintOrder = GeomAbs_C1 iorder = 2 <=> ConstraintOrder = GeomAbs_C2 P(t) = R(t) + W(t) * Q(t) Where W(t) = (1-t**2)**(2*iordre+2) the coefficients JacCoeff represents P(t) JacCoeff are stored as follow:This class provides method to work with Jacobi Polynomials relativly to an order of constraint q = myWorkDegree-2*(myNivConstr+1) Jk(t) for k=0,q compose the Jacobi Polynomial base relativly to the weigth W(t) iorder is the integer value for the constraints: iorder = 0 <=> ConstraintOrder = GeomAbs_C0 iorder = 1 <=> ConstraintOrder = GeomAbs_C1 iorder = 2 <=> ConstraintOrder = GeomAbs_C2 P(t) = R(t) + W(t) * Q(t) Where W(t) = (1-t**2)**(2*iordre+2) the coefficients JacCoeff represents P(t) JacCoeff are stored as follow:
    """
    def AverageError(self,Dimension : int,JacCoeff : float,NewDegree : int) -> float: 
        """
        None
        """
    def D0(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values of the basis functions in u
        """
    def D1(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal,BasisD1 : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values and the derivatives values of the basis functions in u
        """
    def D2(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal,BasisD1 : OCP.TColStd.TColStd_Array1OfReal,BasisD2 : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values and the derivatives values of the basis functions in u
        """
    def D3(self,U : float,BasisValue : OCP.TColStd.TColStd_Array1OfReal,BasisD1 : OCP.TColStd.TColStd_Array1OfReal,BasisD2 : OCP.TColStd.TColStd_Array1OfReal,BasisD3 : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the values and the derivatives values of the basis functions in u
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
    def MaxError(self,Dimension : int,JacCoeff : float,NewDegree : int) -> float: 
        """
        This method computes the maximum error on the polynomial W(t) Q(t) obtained by missing the coefficients of JacCoeff from NewDegree +1 to Degree
        """
    def MaxValue(self,TabMax : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        this method loads for k=0,q the maximum value of abs ( W(t)*Jk(t) )for t bellonging to [-1,1] This values are loaded is the array TabMax(0,myWorkDegree-2*(myNivConst+1)) MaxValue ( me ; TabMaxPointer : in out Real );
        """
    def NivConstr(self) -> int: 
        """
        returns NivConstr

        returns NivConstr
        """
    def Points(self,NbGaussPoints : int,TabPoints : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        returns the Jacobi Points for Gauss integration ie the positive values of the Legendre roots by increasing values NbGaussPoints is the number of points choosen for the integral computation. TabPoints (0,NbGaussPoints/2) TabPoints (0) is loaded only for the odd values of NbGaussPoints The possible values for NbGaussPoints are : 8, 10, 15, 20, 25, 30, 35, 40, 50, 61 NbGaussPoints must be greater than Degree
        """
    def ReduceDegree(self,Dimension : int,MaxDegree : int,Tol : float) -> Tuple[float, int, float]: 
        """
        Compute NewDegree <= MaxDegree so that MaxError is lower than Tol. MaxError can be greater than Tol if it is not possible to find a NewDegree <= MaxDegree. In this case NewDegree = MaxDegree
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToCoefficients(self,Dimension : int,Degree : int,JacCoeff : OCP.TColStd.TColStd_Array1OfReal,Coefficients : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Convert the polynomial P(t) = R(t) + W(t) Q(t) in the canonical base.
        """
    def Weights(self,NbGaussPoints : int,TabWeights : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        returns the Jacobi weigths for Gauss integration only for the positive values of the Legendre roots in the order they are given by the method Points NbGaussPoints is the number of points choosen for the integral computation. TabWeights (0,NbGaussPoints/2,0,Degree) TabWeights (0,.) are only loaded for the odd values of NbGaussPoints The possible values for NbGaussPoints are : 8 , 10 , 15 ,20 ,25 , 30, 35 , 40 , 50 , 61 NbGaussPoints must be greater than Degree
        """
    def WorkDegree(self) -> int: 
        """
        returns WorkDegree

        returns WorkDegree
        """
    def __init__(self,WorkDegree : int,ConstraintOrder : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
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
