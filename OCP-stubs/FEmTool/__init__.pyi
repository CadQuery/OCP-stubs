import OCP.FEmTool
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.GeomAbs
import OCP.math
import OCP.NCollection
import OCP.PLib
import OCP.Standard
import OCP.TColStd
__all__  = [
"FEmTool_Assembly",
"FEmTool_AssemblyTable",
"FEmTool_Curve",
"FEmTool_ElementaryCriterion",
"FEmTool_ElementsOfRefMatrix",
"FEmTool_HAssemblyTable",
"FEmTool_LinearFlexion",
"FEmTool_LinearJerk",
"FEmTool_LinearTension",
"FEmTool_ListOfVectors",
"FEmTool_SparseMatrix",
"FEmTool_SeqOfLinConstr",
"FEmTool_ProfileMatrix"
]
class FEmTool_Assembly():
    """
    Assemble and solve system from (one dimensional) Finite Elements
    """
    def AddConstraint(self,IndexofConstraint : int,Element : int,Dimension : int,LinearForm : OCP.math.math_Vector,Value : float) -> None: 
        """
        None
        """
    def AddMatrix(self,Element : int,Dimension1 : int,Dimension2 : int,Mat : OCP.math.math_Matrix) -> None: 
        """
        Add an elementary Matrix in the assembly Matrix if Dependence(Dimension1,Dimension2) is False
        """
    def AddVector(self,Element : int,Dimension : int,Vec : OCP.math.math_Vector) -> None: 
        """
        Add an elementary Vector in the assembly Vector (second member)
        """
    def GetAssemblyTable(self,AssTable : FEmTool_HAssemblyTable) -> Any: 
        """
        None
        """
    def NbGlobVar(self) -> int: 
        """
        None
        """
    def NullifyConstraint(self) -> None: 
        """
        Nullify all Constraints.
        """
    def NullifyMatrix(self) -> None: 
        """
        Nullify all Matrix 's Coefficient
        """
    def NullifyVector(self) -> None: 
        """
        Nullify all Coordinate of assembly Vector (second member)
        """
    def ResetConstraint(self) -> None: 
        """
        Delete all Constraints.
        """
    def Solution(self,Solution : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def Solve(self) -> bool: 
        """
        Solve the assembly system Returns Standard_False if the computation failed.
        """
    def __init__(self,Dependence : OCP.TColStd.TColStd_Array2OfInteger,Table : FEmTool_HAssemblyTable) -> None: ...
    pass
class FEmTool_AssemblyTable():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : FEmTool_AssemblyTable) -> FEmTool_AssemblyTable: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : FEmTool_AssemblyTable) -> FEmTool_AssemblyTable: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : FEmTool_AssemblyTable) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.TColStd.TColStd_HArray1OfInteger,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class FEmTool_Curve(OCP.Standard.Standard_Transient):
    """
    Curve defined by Polynomial Elements.Curve defined by Polynomial Elements.Curve defined by Polynomial Elements.
    """
    def Base(self) -> OCP.PLib.PLib_Base: 
        """
        None
        """
    def D0(self,U : float,Pnt : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def D1(self,U : float,Vec : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def D2(self,U : float,Vec : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self,IndexOfElement : int) -> int: 
        """
        None
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimension(self) -> int: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetElement(self,IndexOfElement : int,Coeffs : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        None
        """
    def GetPolynom(self,Coeffs : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        returns coefficients of all elements in canonical base.
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Knots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def Length(self,FirstU : float,LastU : float) -> Tuple[float]: 
        """
        None
        """
    def NbElements(self) -> int: 
        """
        None
        """
    def ReduceDegree(self,IndexOfElement : int,Tol : float) -> Tuple[int, float]: 
        """
        None
        """
    def SetDegree(self,IndexOfElement : int,Degree : int) -> None: 
        """
        None
        """
    def SetElement(self,IndexOfElement : int,Coeffs : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Dimension : int,NbElements : int,TheBase : OCP.PLib.PLib_Base,Tolerance : float) -> None: ...
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
class FEmTool_ElementaryCriterion(OCP.Standard.Standard_Transient):
    """
    defined J Criteria to used in minimisationdefined J Criteria to used in minimisationdefined J Criteria to used in minimisation
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
        To know if two dimension are independent.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Gradient(self,Dim : int,G : OCP.math.math_Vector) -> None: 
        """
        To Compute the coefficients in the dimension <dim> of the J(E)'s Gradient where E is the current Element
        """
    def Hessian(self,Dim1 : int,Dim2 : int,H : OCP.math.math_Matrix) -> None: 
        """
        To Compute J(E) the coefficients of Hessian matrix of J(E) which are crossed derivatives in dimensions <Dim1> and <Dim2>. If DependenceTable(Dimension1,Dimension2) is False
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def Set(self,Coeff : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        Set the coefficient of the Element (the Curve)

        Set the definition interval of the Element
        """
    @overload
    def Set(self,FirstKnot : float,LastKnot : float) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> float: 
        """
        To Compute J(E) where E is the current Element
        """
    def __init__(self) -> None: ...
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
class FEmTool_ElementsOfRefMatrix(OCP.math.math_FunctionSet):
    """
    this class describes the functions needed for calculating matrix elements of RefMatrix for linear criteriums (Tension, Flexsion and Jerk) by Gauss integration. Each function from set gives value Pi(u)'*Pj(u)' or Pi(u)''*Pj(u)'' or Pi(u)'''*Pj(u)''' for each i and j, where Pi(u) is i-th basis function of expansion and (') means derivative.
    """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function. It is supposed that NbVariables = 1.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the functions for the variable <X>. returns True if the computation was done successfully, False otherwise. F contains results only for i<=j in following order: P0*P0, P0*P1, P0*P2... P1*P1, P1*P2,... (upper triangle of matrix {PiPj})
        """
    def __init__(self,TheBase : OCP.PLib.PLib_Base,DerOrder : int) -> None: ...
    pass
class FEmTool_HAssemblyTable(FEmTool_AssemblyTable, OCP.Standard.Standard_Transient):
    def Array2(self) -> FEmTool_AssemblyTable: 
        """
        None
        """
    def Assign(self,theOther : FEmTool_AssemblyTable) -> FEmTool_AssemblyTable: 
        """
        Assignment
        """
    def ChangeArray2(self) -> FEmTool_AssemblyTable: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
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
    def Init(self,theValue : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : FEmTool_AssemblyTable) -> FEmTool_AssemblyTable: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : OCP.TColStd.TColStd_HArray1OfInteger) -> None: ...
    @overload
    def __init__(self,theOther : FEmTool_AssemblyTable) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
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
class FEmTool_LinearFlexion(FEmTool_ElementaryCriterion, OCP.Standard.Standard_Transient):
    """
    Criterium of LinearFlexion To Hermit-Jacobi elementsCriterium of LinearFlexion To Hermit-Jacobi elementsCriterium of LinearFlexion To Hermit-Jacobi elements
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Gradient(self,Dimension : int,G : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def Hessian(self,Dimension1 : int,Dimension2 : int,H : OCP.math.math_Matrix) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def Set(self,Coeff : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        Set the coefficient of the Element (the Curve)

        Set the definition interval of the Element
        """
    @overload
    def Set(self,FirstKnot : float,LastKnot : float) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> float: 
        """
        None
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
class FEmTool_LinearJerk(FEmTool_ElementaryCriterion, OCP.Standard.Standard_Transient):
    """
    Criterion of LinearJerk To Hermit-Jacobi elementsCriterion of LinearJerk To Hermit-Jacobi elementsCriterion of LinearJerk To Hermit-Jacobi elements
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Gradient(self,Dimension : int,G : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def Hessian(self,Dimension1 : int,Dimension2 : int,H : OCP.math.math_Matrix) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def Set(self,Coeff : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        Set the coefficient of the Element (the Curve)

        Set the definition interval of the Element
        """
    @overload
    def Set(self,FirstKnot : float,LastKnot : float) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> float: 
        """
        None
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
class FEmTool_LinearTension(FEmTool_ElementaryCriterion, OCP.Standard.Standard_Transient):
    """
    Criterium of LinearTension To Hermit-Jacobi elementsCriterium of LinearTension To Hermit-Jacobi elementsCriterium of LinearTension To Hermit-Jacobi elements
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Gradient(self,Dimension : int,G : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def Hessian(self,Dimension1 : int,Dimension2 : int,H : OCP.math.math_Matrix) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def Set(self,Coeff : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        Set the coefficient of the Element (the Curve)

        Set the definition interval of the Element
        """
    @overload
    def Set(self,FirstKnot : float,LastKnot : float) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> float: 
        """
        None
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
class FEmTool_ListOfVectors(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TColStd.TColStd_HArray1OfReal,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : FEmTool_ListOfVectors) -> None: ...
    @overload
    def Append(self,theItem : OCP.TColStd.TColStd_HArray1OfReal) -> OCP.TColStd.TColStd_HArray1OfReal: ...
    def Assign(self,theOther : FEmTool_ListOfVectors) -> FEmTool_ListOfVectors: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.TColStd.TColStd_HArray1OfReal,theIter : Any) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : FEmTool_ListOfVectors,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : OCP.TColStd.TColStd_HArray1OfReal,theIter : Any) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : FEmTool_ListOfVectors,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.TColStd.TColStd_HArray1OfReal) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : FEmTool_ListOfVectors) -> None: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self,theOther : FEmTool_ListOfVectors) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class FEmTool_SparseMatrix(OCP.Standard.Standard_Transient):
    """
    Sparse Matrix definitionSparse Matrix definitionSparse Matrix definition
    """
    def ChangeValue(self,I : int,J : int) -> float: 
        """
        None
        """
    def ColNumber(self) -> int: 
        """
        returns the column range of the matrix.
        """
    def Decompose(self) -> bool: 
        """
        To make a Factorization of <me>
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
    def Init(self,Value : float) -> None: 
        """
        None
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Multiplied(self,X : OCP.math.math_Vector,MX : OCP.math.math_Vector) -> None: 
        """
        returns the product of a SparseMatrix by a vector. An exception is raised if the dimensions are different
        """
    def Prepare(self) -> bool: 
        """
        Make Preparation to iterative solve
        """
    def RowNumber(self) -> int: 
        """
        returns the row range of a matrix.
        """
    @overload
    def Solve(self,B : OCP.math.math_Vector,X : OCP.math.math_Vector) -> None: 
        """
        Direct Solve of AX = B

        Iterative solve of AX = B
        """
    @overload
    def Solve(self,B : OCP.math.math_Vector,Init : OCP.math.math_Vector,X : OCP.math.math_Vector,Residual : OCP.math.math_Vector,Tolerance : float=1e-08,NbIterations : int=50) -> None: ...
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
class FEmTool_SeqOfLinConstr(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : FEmTool_SeqOfLinConstr) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : FEmTool_ListOfVectors) -> None: ...
    def Assign(self,theOther : FEmTool_SeqOfLinConstr) -> FEmTool_SeqOfLinConstr: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> FEmTool_ListOfVectors: 
        """
        First item access
        """
    def ChangeLast(self) -> FEmTool_ListOfVectors: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> FEmTool_ListOfVectors: 
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
    def First(self) -> FEmTool_ListOfVectors: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : FEmTool_SeqOfLinConstr) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : FEmTool_ListOfVectors) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : FEmTool_ListOfVectors) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : FEmTool_SeqOfLinConstr) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> FEmTool_ListOfVectors: 
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
    def Prepend(self,theSeq : FEmTool_SeqOfLinConstr) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : FEmTool_ListOfVectors) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : FEmTool_ListOfVectors) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : FEmTool_SeqOfLinConstr) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> FEmTool_ListOfVectors: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : FEmTool_SeqOfLinConstr) -> None: ...
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
class FEmTool_ProfileMatrix(FEmTool_SparseMatrix, OCP.Standard.Standard_Transient):
    """
    Symmetric Sparse ProfileMatrix useful for 1D Finite Element methodsSymmetric Sparse ProfileMatrix useful for 1D Finite Element methodsSymmetric Sparse ProfileMatrix useful for 1D Finite Element methods
    """
    def ChangeValue(self,I : int,J : int) -> float: 
        """
        None
        """
    def ColNumber(self) -> int: 
        """
        returns the column range of the matrix.
        """
    def Decompose(self) -> bool: 
        """
        To make a Factorization of <me>
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
    def Init(self,Value : float) -> None: 
        """
        None
        """
    def IsInProfile(self,i : int,j : int) -> bool: 
        """
        None
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Multiplied(self,X : OCP.math.math_Vector,MX : OCP.math.math_Vector) -> None: 
        """
        returns the product of a SparseMatrix by a vector. An exception is raised if the dimensions are different
        """
    def OutM(self) -> None: 
        """
        None
        """
    def OutS(self) -> None: 
        """
        None
        """
    def Prepare(self) -> bool: 
        """
        Make Preparation to iterative solve
        """
    def RowNumber(self) -> int: 
        """
        returns the row range of a matrix.
        """
    @overload
    def Solve(self,B : OCP.math.math_Vector,X : OCP.math.math_Vector) -> None: 
        """
        Direct Solve of AX = B

        Iterative solve of AX = B
        """
    @overload
    def Solve(self,B : OCP.math.math_Vector,Init : OCP.math.math_Vector,X : OCP.math.math_Vector,Residual : OCP.math.math_Vector,Tolerance : float=1e-08,NbIterations : int=50) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,FirstIndexes : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
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
