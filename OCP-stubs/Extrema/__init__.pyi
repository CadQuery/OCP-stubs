import OCP.Extrema
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor2d
import OCP.Adaptor3d
import OCP.NCollection
import OCP.Geom2d
import OCP.Bnd
import OCP.Standard
import OCP.gp
import OCP.Geom
import OCP.GeomAdaptor
import OCP.TColStd
import OCP.GeomAbs
import OCP.math
__all__  = [
"Extrema_Array1OfPOnCurv",
"Extrema_Array1OfPOnCurv2d",
"Extrema_Array1OfPOnSurf",
"Extrema_Array2OfPOnCurv",
"Extrema_Array2OfPOnCurv2d",
"Extrema_Array2OfPOnSurf",
"Extrema_Array2OfPOnSurfParams",
"Extrema_CCLocFOfLocECC",
"Extrema_CCLocFOfLocECC2d",
"Extrema_Curve2dTool",
"Extrema_CurveTool",
"Extrema_ECC",
"Extrema_ECC2d",
"Extrema_ELPCOfLocateExtPC",
"Extrema_ELPCOfLocateExtPC2d",
"Extrema_EPCOfELPCOfLocateExtPC",
"Extrema_EPCOfELPCOfLocateExtPC2d",
"Extrema_EPCOfExtPC",
"Extrema_EPCOfExtPC2d",
"Extrema_ElementType",
"Extrema_ExtAlgo",
"Extrema_ExtCC",
"Extrema_ExtCC2d",
"Extrema_ExtCS",
"Extrema_ExtElC",
"Extrema_ExtElC2d",
"Extrema_ExtElCS",
"Extrema_ExtElSS",
"Extrema_ExtFlag",
"Extrema_ExtPC",
"Extrema_ExtPC2d",
"Extrema_ExtPElC",
"Extrema_ExtPElC2d",
"Extrema_ExtPElS",
"Extrema_ExtPExtS",
"Extrema_ExtPRevS",
"Extrema_ExtPS",
"Extrema_ExtSS",
"Extrema_FuncExtCS",
"Extrema_FuncExtSS",
"Extrema_FuncPSDist",
"Extrema_FuncPSNorm",
"Extrema_GenExtCS",
"Extrema_GenExtPS",
"Extrema_GenExtSS",
"Extrema_GenLocateExtCS",
"Extrema_GenLocateExtPS",
"Extrema_GenLocateExtSS",
"Extrema_GlobOptFuncCCC0",
"Extrema_GlobOptFuncCCC1",
"Extrema_GlobOptFuncCCC2",
"Extrema_GlobOptFuncCS",
"Extrema_HArray1OfPOnCurv",
"Extrema_HArray1OfPOnCurv2d",
"Extrema_HArray1OfPOnSurf",
"Extrema_HArray2OfPOnCurv",
"Extrema_HArray2OfPOnCurv2d",
"Extrema_HArray2OfPOnSurf",
"Extrema_HArray2OfPOnSurfParams",
"Extrema_LocECC",
"Extrema_LocECC2d",
"Extrema_LocEPCOfLocateExtPC",
"Extrema_LocEPCOfLocateExtPC2d",
"Extrema_LocateExtCC",
"Extrema_LocateExtCC2d",
"Extrema_LocateExtPC",
"Extrema_LocateExtPC2d",
"Extrema_PCFOfEPCOfELPCOfLocateExtPC",
"Extrema_PCFOfEPCOfELPCOfLocateExtPC2d",
"Extrema_PCFOfEPCOfExtPC",
"Extrema_PCFOfEPCOfExtPC2d",
"Extrema_PCLocFOfLocEPCOfLocateExtPC",
"Extrema_PCLocFOfLocEPCOfLocateExtPC2d",
"Extrema_POnCurv",
"Extrema_POnCurv2d",
"Extrema_POnSurf",
"Extrema_POnSurfParams",
"Extrema_SequenceOfPOnCurv",
"Extrema_SequenceOfPOnCurv2d",
"Extrema_SequenceOfPOnSurf",
"Extrema_UBTreeFillerOfSphere",
"Extrema_UBTreeOfSphere",
"Extrema_ExtAlgo_Grad",
"Extrema_ExtAlgo_Tree",
"Extrema_ExtFlag_MAX",
"Extrema_ExtFlag_MIN",
"Extrema_ExtFlag_MINMAX",
"Extrema_Face",
"Extrema_Node",
"Extrema_UIsoEdge",
"Extrema_VIsoEdge"
]
class Extrema_Array1OfPOnCurv():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Extrema_Array1OfPOnCurv) -> Extrema_Array1OfPOnCurv: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Extrema_POnCurv: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Extrema_POnCurv: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Extrema_POnCurv: 
        """
        Variable value access
        """
    def First(self) -> Extrema_POnCurv: 
        """
        Returns first element
        """
    def Init(self,theValue : Extrema_POnCurv) -> None: 
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
    def Last(self) -> Extrema_POnCurv: 
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
    def Move(self,theOther : Extrema_Array1OfPOnCurv) -> Extrema_Array1OfPOnCurv: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Extrema_POnCurv) -> None: 
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
    def Value(self,theIndex : int) -> Extrema_POnCurv: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : Extrema_POnCurv,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array1OfPOnCurv) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Extrema_Array1OfPOnCurv2d():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Extrema_Array1OfPOnCurv2d) -> Extrema_Array1OfPOnCurv2d: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Extrema_POnCurv2d: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Extrema_POnCurv2d: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Extrema_POnCurv2d: 
        """
        Variable value access
        """
    def First(self) -> Extrema_POnCurv2d: 
        """
        Returns first element
        """
    def Init(self,theValue : Extrema_POnCurv2d) -> None: 
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
    def Last(self) -> Extrema_POnCurv2d: 
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
    def Move(self,theOther : Extrema_Array1OfPOnCurv2d) -> Extrema_Array1OfPOnCurv2d: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Extrema_POnCurv2d) -> None: 
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
    def Value(self,theIndex : int) -> Extrema_POnCurv2d: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : Extrema_POnCurv2d,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array1OfPOnCurv2d) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Extrema_Array1OfPOnSurf():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Extrema_Array1OfPOnSurf) -> Extrema_Array1OfPOnSurf: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Extrema_POnSurf: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Extrema_POnSurf: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Extrema_POnSurf: 
        """
        Variable value access
        """
    def First(self) -> Extrema_POnSurf: 
        """
        Returns first element
        """
    def Init(self,theValue : Extrema_POnSurf) -> None: 
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
    def Last(self) -> Extrema_POnSurf: 
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
    def Move(self,theOther : Extrema_Array1OfPOnSurf) -> Extrema_Array1OfPOnSurf: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Extrema_POnSurf) -> None: 
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
    def Value(self,theIndex : int) -> Extrema_POnSurf: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : Extrema_POnSurf,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array1OfPOnSurf) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Extrema_Array2OfPOnCurv():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : Extrema_Array2OfPOnCurv) -> Extrema_Array2OfPOnCurv: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> Extrema_POnCurv: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : Extrema_POnCurv) -> None: 
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
    def Move(self,theOther : Extrema_Array2OfPOnCurv) -> Extrema_Array2OfPOnCurv: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : Extrema_POnCurv) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> Extrema_POnCurv: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array2OfPOnCurv) -> None: ...
    @overload
    def __init__(self,theBegin : Extrema_POnCurv,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class Extrema_Array2OfPOnCurv2d():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : Extrema_Array2OfPOnCurv2d) -> Extrema_Array2OfPOnCurv2d: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> Extrema_POnCurv2d: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : Extrema_POnCurv2d) -> None: 
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
    def Move(self,theOther : Extrema_Array2OfPOnCurv2d) -> Extrema_Array2OfPOnCurv2d: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : Extrema_POnCurv2d) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> Extrema_POnCurv2d: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : Extrema_POnCurv2d,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array2OfPOnCurv2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_Array2OfPOnSurf():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : Extrema_Array2OfPOnSurf) -> Extrema_Array2OfPOnSurf: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> Extrema_POnSurf: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : Extrema_POnSurf) -> None: 
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
    def Move(self,theOther : Extrema_Array2OfPOnSurf) -> Extrema_Array2OfPOnSurf: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : Extrema_POnSurf) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> Extrema_POnSurf: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Extrema_Array2OfPOnSurf) -> None: ...
    @overload
    def __init__(self,theBegin : Extrema_POnSurf,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_Array2OfPOnSurfParams():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : Extrema_Array2OfPOnSurfParams) -> Extrema_Array2OfPOnSurfParams: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> Extrema_POnSurfParams: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : Extrema_POnSurfParams) -> None: 
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
    def Move(self,theOther : Extrema_Array2OfPOnSurfParams) -> Extrema_Array2OfPOnSurfParams: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : Extrema_POnSurfParams) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> Extrema_POnSurfParams: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Extrema_Array2OfPOnSurfParams) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : Extrema_POnSurfParams,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class Extrema_CCLocFOfLocECC(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def CurvePtr(self,theRank : int) -> capsule: 
        """
        Returns a pointer to the curve specified in the constructor or in SetCurve() method.
        """
    def Derivatives(self,UV : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculate Fi'(U,V).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbExt(self) -> int: 
        """
        Return the number of found extrema.
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Points(self,N : int,P1 : Extrema_POnCurv,P2 : Extrema_POnCurv) -> None: 
        """
        Return the points of the Nth extreme distance.
        """
    def SearchOfTolerance(self,C : capsule) -> float: 
        """
        Computes a Tol value. If 1st derivative of curve |D1|<Tol, it is considered D1=0.
        """
    def SetCurve(self,theRank : int,C1 : OCP.Adaptor3d.Adaptor3d_Curve) -> None: 
        """
        None
        """
    def SetTolerance(self,theTol : float) -> None: 
        """
        None
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Return the value of the Nth distance.
        """
    def SubIntervalInitialize(self,theUfirst : OCP.math.math_Vector,theUlast : OCP.math.math_Vector) -> None: 
        """
        Determines of boundaries of subinterval for find of root.
        """
    def Tolerance(self) -> float: 
        """
        Returns a tolerance specified in the constructor or in SetTolerance() method.
        """
    def Value(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        Calculate Fi(U,V).
        """
    def Values(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculate Fi(U,V) and Fi'(U,V).
        """
    @overload
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve,thetol : float=1e-10) -> None: ...
    @overload
    def __init__(self,thetol : float=1e-10) -> None: ...
    pass
class Extrema_CCLocFOfLocECC2d(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def CurvePtr(self,theRank : int) -> capsule: 
        """
        Returns a pointer to the curve specified in the constructor or in SetCurve() method.
        """
    def Derivatives(self,UV : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculate Fi'(U,V).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbExt(self) -> int: 
        """
        Return the number of found extrema.
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Points(self,N : int,P1 : Extrema_POnCurv2d,P2 : Extrema_POnCurv2d) -> None: 
        """
        Return the points of the Nth extreme distance.
        """
    def SearchOfTolerance(self,C : capsule) -> float: 
        """
        Computes a Tol value. If 1st derivative of curve |D1|<Tol, it is considered D1=0.
        """
    def SetCurve(self,theRank : int,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        None
        """
    def SetTolerance(self,theTol : float) -> None: 
        """
        None
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Return the value of the Nth distance.
        """
    def SubIntervalInitialize(self,theUfirst : OCP.math.math_Vector,theUlast : OCP.math.math_Vector) -> None: 
        """
        Determines of boundaries of subinterval for find of root.
        """
    def Tolerance(self) -> float: 
        """
        Returns a tolerance specified in the constructor or in SetTolerance() method.
        """
    def Value(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        Calculate Fi(U,V).
        """
    def Values(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculate Fi(U,V) and Fi'(U,V).
        """
    @overload
    def __init__(self,thetol : float=1e-10) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,thetol : float=1e-10) -> None: ...
    pass
class Extrema_Curve2dTool():
    """
    None
    """
    @staticmethod
    def BSpline_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Circ2d: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Computes the point of parameter U on the curve.
        """
    @staticmethod
    def D1_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative.
        """
    @staticmethod
    def D2_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2.
        """
    @staticmethod
    def D3_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative.
        """
    @staticmethod
    def DN_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        The returned vector gives the value of the derivative for the order of derivation N.
        """
    @staticmethod
    def DeflCurvIntervals_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the parameters bounding the intervals of subdivision of curve according to Curvature deflection. Value of deflection is defined in method.
        """
    @staticmethod
    def Degree_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> int: 
        """
        None
        """
    @staticmethod
    def Ellipse_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Elips2d: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Hyperbola_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Hypr2d: 
        """
        None
        """
    @staticmethod
    def Intervals_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def IsClosed_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPeriodic_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> bool: 
        """
        None
        """
    @staticmethod
    def IsRational_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> bool: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        If necessary, breaks the curve in intervals of continuity <S>. And returns the number of intervals.
        """
    @staticmethod
    def NbKnots_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> int: 
        """
        None
        """
    @staticmethod
    def NbPoles_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> int: 
        """
        None
        """
    @staticmethod
    def Parabola_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @staticmethod
    def Period_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self) -> None: ...
    pass
class Extrema_CurveTool():
    """
    None
    """
    @staticmethod
    def BSpline_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.Geom.Geom_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Circ: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def D1_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D2_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def D3_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def DN_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def DeflCurvIntervals_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the parameters bounding the intervals of subdivision of curve according to Curvature deflection. Value of deflection is defined in method.
        """
    @staticmethod
    def Degree_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> int: 
        """
        None
        """
    @staticmethod
    def Ellipse_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Elips: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        None
        """
    @staticmethod
    def Hyperbola_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    @staticmethod
    def Intervals_s(C : OCP.Adaptor3d.Adaptor3d_Curve,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def IsPeriodic_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> bool: 
        """
        None
        """
    @staticmethod
    def IsRational_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> bool: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Lin: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    @staticmethod
    def NbKnots_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> int: 
        """
        None
        """
    @staticmethod
    def NbPoles_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> int: 
        """
        None
        """
    @staticmethod
    def Parabola_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Parab: 
        """
        None
        """
    @staticmethod
    def Period_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : OCP.Adaptor3d.Adaptor3d_Curve,R3d : float) -> float: 
        """
        None
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Extrema_ECC():
    """
    None
    """
    def GetSingleSolutionFlag(self) -> bool: 
        """
        Get flag for single extrema computation. Works on parametric solver only.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns state of myParallel flag.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self) -> None: 
        """
        Performs calculations.
        """
    def Points(self,N : int,P1 : Extrema_POnCurv,P2 : Extrema_POnCurv) -> None: 
        """
        Returns the points of the Nth extremum distance. P1 is on the first curve, P2 on the second one.
        """
    def SetParams(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve,Uinf : float,Usup : float,Vinf : float,Vsup : float) -> None: 
        """
        Set params in case of empty constructor is usage.
        """
    def SetSingleSolutionFlag(self,theSingleSolutionFlag : bool) -> None: 
        """
        Set flag for single extrema computation. Works on parametric solver only.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        None
        """
    def SquareDistance(self,N : int=1) -> float: 
        """
        Returns the value of the Nth square extremum distance.
        """
    @overload
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve,Uinf : float,Usup : float,Vinf : float,Vsup : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class Extrema_ECC2d():
    """
    None
    """
    def GetSingleSolutionFlag(self) -> bool: 
        """
        Get flag for single extrema computation. Works on parametric solver only.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns state of myParallel flag.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self) -> None: 
        """
        Performs calculations.
        """
    def Points(self,N : int,P1 : Extrema_POnCurv2d,P2 : Extrema_POnCurv2d) -> None: 
        """
        Returns the points of the Nth extremum distance. P1 is on the first curve, P2 on the second one.
        """
    def SetParams(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,Uinf : float,Usup : float,Vinf : float,Vsup : float) -> None: 
        """
        Set params in case of empty constructor is usage.
        """
    def SetSingleSolutionFlag(self,theSingleSolutionFlag : bool) -> None: 
        """
        Set flag for single extrema computation. Works on parametric solver only.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        None
        """
    def SquareDistance(self,N : int=1) -> float: 
        """
        Returns the value of the Nth square extremum distance.
        """
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,Uinf : float,Usup : float,Vinf : float,Vsup : float) -> None: ...
    pass
class Extrema_ELPCOfLocateExtPC():
    """
    None
    """
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Uinf : float,Usup : float,TolF : float=1e-10) -> None: 
        """
        initializes the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the <N>th extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the point of the <N>th extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the <N>th extremum square distance.
        """
    def TrimmedSquareDistances(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        if the curve is a trimmed curve, dist1 is a square distance between <P> and the point of parameter FirstParameter <P1> and dist2 is a square distance between <P> and the point of parameter LastParameter <P2>.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,TolF : float=1e-10) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,Uinf : float,Usup : float,TolF : float=1e-10) -> None: ...
    pass
class Extrema_ELPCOfLocateExtPC2d():
    """
    None
    """
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Uinf : float,Usup : float,TolF : float=1e-10) -> None: 
        """
        initializes the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the <N>th extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnCurv2d: 
        """
        Returns the point of the <N>th extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the <N>th extremum square distance.
        """
    def TrimmedSquareDistances(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        if the curve is a trimmed curve, dist1 is a square distance between <P> and the point of parameter FirstParameter <P1> and dist2 is a square distance between <P> and the point of parameter LastParameter <P2>.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,TolF : float=1e-10) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Uinf : float,Usup : float,TolF : float=1e-10) -> None: ...
    pass
class Extrema_EPCOfELPCOfLocateExtPC():
    """
    None
    """
    @overload
    def Initialize(self,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: 
        """
        sets the fields of the algorithm.

        sets the fields of the algorithm.

        sets the fields of the algorithm.

        sets the fields of the algorithm.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbU : int,TolU : float,TolF : float) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the Nth extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        the algorithm is done with the point P. An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the point of the Nth extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,NbU : int,TolU : float,TolF : float) -> None: ...
    pass
class Extrema_EPCOfELPCOfLocateExtPC2d():
    """
    None
    """
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        sets the fields of the algorithm.

        sets the fields of the algorithm.

        sets the fields of the algorithm.

        sets the fields of the algorithm.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: ...
    @overload
    def Initialize(self,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,TolU : float,TolF : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the Nth extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        the algorithm is done with the point P. An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnCurv2d: 
        """
        Returns the point of the Nth extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,TolU : float,TolF : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: ...
    pass
class Extrema_EPCOfExtPC():
    """
    None
    """
    @overload
    def Initialize(self,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: 
        """
        sets the fields of the algorithm.

        sets the fields of the algorithm.

        sets the fields of the algorithm.

        sets the fields of the algorithm.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbU : int,TolU : float,TolF : float) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the Nth extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        the algorithm is done with the point P. An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the point of the Nth extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,NbU : int,TolU : float,TolF : float) -> None: ...
    pass
class Extrema_EPCOfExtPC2d():
    """
    None
    """
    @overload
    def Initialize(self,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: 
        """
        sets the fields of the algorithm.

        sets the fields of the algorithm.

        sets the fields of the algorithm.

        sets the fields of the algorithm.
        """
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,TolU : float,TolF : float) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: ...
    @overload
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the Nth extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        the algorithm is done with the point P. An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnCurv2d: 
        """
        Returns the point of the Nth extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,TolU : float,TolF : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,NbU : int,Umin : float,Usup : float,TolU : float,TolF : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_ElementType():
    """
    None

    Members:

      Extrema_Node

      Extrema_UIsoEdge

      Extrema_VIsoEdge

      Extrema_Face
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Extrema_Face: OCP.Extrema.Extrema_ElementType # value = Extrema_ElementType.Extrema_Face
    Extrema_Node: OCP.Extrema.Extrema_ElementType # value = Extrema_ElementType.Extrema_Node
    Extrema_UIsoEdge: OCP.Extrema.Extrema_ElementType # value = Extrema_ElementType.Extrema_UIsoEdge
    Extrema_VIsoEdge: OCP.Extrema.Extrema_ElementType # value = Extrema_ElementType.Extrema_VIsoEdge
    __entries: dict # value = {'Extrema_Node': (Extrema_ElementType.Extrema_Node, None), 'Extrema_UIsoEdge': (Extrema_ElementType.Extrema_UIsoEdge, None), 'Extrema_VIsoEdge': (Extrema_ElementType.Extrema_VIsoEdge, None), 'Extrema_Face': (Extrema_ElementType.Extrema_Face, None)}
    __members__: dict # value = {'Extrema_Node': Extrema_ElementType.Extrema_Node, 'Extrema_UIsoEdge': Extrema_ElementType.Extrema_UIsoEdge, 'Extrema_VIsoEdge': Extrema_ElementType.Extrema_VIsoEdge, 'Extrema_Face': Extrema_ElementType.Extrema_Face}
    pass
class Extrema_ExtAlgo():
    """
    None

    Members:

      Extrema_ExtAlgo_Grad

      Extrema_ExtAlgo_Tree
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Extrema_ExtAlgo_Grad: OCP.Extrema.Extrema_ExtAlgo # value = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad
    Extrema_ExtAlgo_Tree: OCP.Extrema.Extrema_ExtAlgo # value = Extrema_ExtAlgo.Extrema_ExtAlgo_Tree
    __entries: dict # value = {'Extrema_ExtAlgo_Grad': (Extrema_ExtAlgo.Extrema_ExtAlgo_Grad, None), 'Extrema_ExtAlgo_Tree': (Extrema_ExtAlgo.Extrema_ExtAlgo_Tree, None)}
    __members__: dict # value = {'Extrema_ExtAlgo_Grad': Extrema_ExtAlgo.Extrema_ExtAlgo_Grad, 'Extrema_ExtAlgo_Tree': Extrema_ExtAlgo.Extrema_ExtAlgo_Tree}
    pass
class Extrema_ExtCC():
    """
    It calculates all the distance between two curves. These distances can be maximum or minimum.
    """
    def GetSingleSolutionFlag(self) -> bool: 
        """
        Get flag for single extrema computation. Works on parametric solver only.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the two curves are parallel.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self) -> None: 
        """
        None
        """
    def Points(self,N : int,P1 : Extrema_POnCurv,P2 : Extrema_POnCurv) -> None: 
        """
        Returns the points of the Nth extremum distance. P1 is on the first curve, P2 on the second one.
        """
    @overload
    def SetCurve(self,theRank : int,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def SetCurve(self,theRank : int,C : OCP.Adaptor3d.Adaptor3d_Curve,Uinf : float,Usup : float) -> None: ...
    def SetRange(self,theRank : int,Uinf : float,Usup : float) -> None: 
        """
        None
        """
    def SetSingleSolutionFlag(self,theSingleSolutionFlag : bool) -> None: 
        """
        Set flag for single extrema computation. Works on parametric solver only.
        """
    def SetTolerance(self,theRank : int,Tol : float) -> None: 
        """
        None
        """
    def SquareDistance(self,N : int=1) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    def TrimmedSquareDistances(self,P11 : OCP.gp.gp_Pnt,P12 : OCP.gp.gp_Pnt,P21 : OCP.gp.gp_Pnt,P22 : OCP.gp.gp_Pnt) -> Tuple[float, float, float, float]: 
        """
        if the curve is a trimmed curve, dist11 is a square distance between the point on C1 of parameter FirstParameter and the point of parameter FirstParameter on C2.
        """
    @overload
    def __init__(self,TolC1 : float=1e-10,TolC2 : float=1e-10) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve,TolC1 : float=1e-10,TolC2 : float=1e-10) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,V1 : float,V2 : float,TolC1 : float=1e-10,TolC2 : float=1e-10) -> None: ...
    pass
class Extrema_ExtCC2d():
    """
    It calculates all the distance between two curves. These distances can be maximum or minimum.
    """
    def GetSingleSolutionFlag(self) -> bool: 
        """
        Get flag for single extrema computation. Works on parametric solver only.
        """
    def Initialize(self,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,V1 : float,V2 : float,TolC1 : float=1e-10,TolC2 : float=1e-10) -> None: 
        """
        initializes the fields.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the two curves are parallel.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,U1 : float,U2 : float) -> None: 
        """
        None
        """
    def Points(self,N : int,P1 : Extrema_POnCurv2d,P2 : Extrema_POnCurv2d) -> None: 
        """
        Returns the points of the Nth extremum distance. P1 is on the first curve, P2 on the second one.
        """
    def SetSingleSolutionFlag(self,theSingleSolutionFlag : bool) -> None: 
        """
        Set flag for single extrema computation. Works on parametric solver only.
        """
    def SquareDistance(self,N : int=1) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    def TrimmedSquareDistances(self,P11 : OCP.gp.gp_Pnt2d,P12 : OCP.gp.gp_Pnt2d,P21 : OCP.gp.gp_Pnt2d,P22 : OCP.gp.gp_Pnt2d) -> Tuple[float, float, float, float]: 
        """
        if the curve is a trimmed curve, dist11 is a square distance between the point on C1 of parameter FirstParameter and the point of parameter FirstParameter on C2.
        """
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,TolC1 : float=1e-10,TolC2 : float=1e-10) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,U1 : float,U2 : float,V1 : float,V2 : float,TolC1 : float=1e-10,TolC2 : float=1e-10) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_ExtCS():
    """
    It calculates all the extremum distances between a curve and a surface. These distances can be minimum or maximum.
    """
    def Initialize(self,S : OCP.Adaptor3d.Adaptor3d_Surface,Uinf : float,Usup : float,Vinf : float,Vsup : float,TolC : float,TolS : float) -> None: 
        """
        Initializes the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the curve is on a parallel surface.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Uinf : float,Usup : float) -> None: 
        """
        Computes the distances. An exception is raised if the fieds have not been initialized.
        """
    def Points(self,N : int,P1 : Extrema_POnCurv,P2 : Extrema_POnSurf) -> None: 
        """
        Returns the point of the Nth resulting distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth resulting square distance.
        """
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface,UCinf : float,UCsup : float,Uinf : float,Usup : float,Vinf : float,Vsup : float,TolC : float,TolS : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface,TolC : float,TolS : float) -> None: ...
    pass
class Extrema_ExtElC():
    """
    It calculates all the distance between two elementary curves. These distances can be maximum or minimum.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the two curves are parallel.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Points(self,N : int,P1 : Extrema_POnCurv,P2 : Extrema_POnCurv) -> None: 
        """
        Returns the points of the Nth extremum distance. P1 is on the first curve, P2 on the second one.
        """
    def SquareDistance(self,N : int=1) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin,C2 : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin,C2 : OCP.gp.gp_Lin,AngTol : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ,C2 : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin,C2 : OCP.gp.gp_Elips) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin,C2 : OCP.gp.gp_Parab) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin,C2 : OCP.gp.gp_Circ,Tol : float) -> None: ...
    pass
class Extrema_ExtElC2d():
    """
    It calculates all the distance between two elementary curves. These distances can be maximum or minimum.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the two curves are parallel.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Points(self,N : int,P1 : Extrema_POnCurv2d,P2 : Extrema_POnCurv2d) -> None: 
        """
        Returns the points of the Nth extremum distance. P1 is on the first curve, P2 on the second one.
        """
    def SquareDistance(self,N : int=1) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.gp.gp_Elips2d) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin2d,C2 : OCP.gp.gp_Parab2d) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin2d,C2 : OCP.gp.gp_Circ2d,Tol : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin2d,C2 : OCP.gp.gp_Lin2d,AngTol : float) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin2d,C2 : OCP.gp.gp_Hypr2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Lin2d,C2 : OCP.gp.gp_Elips2d) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.gp.gp_Parab2d) -> None: ...
    @overload
    def __init__(self,C1 : OCP.gp.gp_Circ2d,C2 : OCP.gp.gp_Hypr2d) -> None: ...
    pass
class Extrema_ExtElCS():
    """
    It calculates all the distances between a curve and a surface. These distances can be maximum or minimum.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the curve is on a parallel surface.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    @overload
    def Perform(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Pln) -> None: 
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

        None

        None
        """
    @overload
    def Perform(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Torus) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Cone) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Torus) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Cone) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Pln) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Hypr,S : OCP.gp.gp_Pln) -> None: ...
    def Points(self,N : int,P1 : Extrema_POnCurv,P2 : Extrema_POnSurf) -> None: 
        """
        Returns the points of the Nth extremum distance. P1 is on the curve, P2 on the surface.
        """
    def SquareDistance(self,N : int=1) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Torus) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Hypr,S : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Torus) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Cone) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,S : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Lin,S : OCP.gp.gp_Cone) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_ExtElSS():
    """
    It calculates all the distances between 2 elementary surfaces. These distances can be maximum or minimum.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the two surfaces are parallel.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    @overload
    def Perform(self,S1 : OCP.gp.gp_Sphere,S2 : OCP.gp.gp_Cone) -> None: 
        """
        None

        None

        None

        None

        None

        None
        """
    @overload
    def Perform(self,S1 : OCP.gp.gp_Pln,S2 : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def Perform(self,S1 : OCP.gp.gp_Sphere,S2 : OCP.gp.gp_Torus) -> None: ...
    @overload
    def Perform(self,S1 : OCP.gp.gp_Sphere,S2 : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def Perform(self,S1 : OCP.gp.gp_Pln,S2 : OCP.gp.gp_Pln) -> None: ...
    @overload
    def Perform(self,S1 : OCP.gp.gp_Sphere,S2 : OCP.gp.gp_Sphere) -> None: ...
    def Points(self,N : int,P1 : Extrema_POnSurf,P2 : Extrema_POnSurf) -> None: 
        """
        Returns the points for the Nth resulting distance. P1 is on the first surface, P2 on the second one.
        """
    def SquareDistance(self,N : int=1) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Sphere,S2 : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Sphere,S2 : OCP.gp.gp_Cone) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pln,S2 : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Sphere,S2 : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Sphere,S2 : OCP.gp.gp_Torus) -> None: ...
    @overload
    def __init__(self,S1 : OCP.gp.gp_Pln,S2 : OCP.gp.gp_Pln) -> None: ...
    pass
class Extrema_ExtFlag():
    """
    None

    Members:

      Extrema_ExtFlag_MIN

      Extrema_ExtFlag_MAX

      Extrema_ExtFlag_MINMAX
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Extrema_ExtFlag_MAX: OCP.Extrema.Extrema_ExtFlag # value = Extrema_ExtFlag.Extrema_ExtFlag_MAX
    Extrema_ExtFlag_MIN: OCP.Extrema.Extrema_ExtFlag # value = Extrema_ExtFlag.Extrema_ExtFlag_MIN
    Extrema_ExtFlag_MINMAX: OCP.Extrema.Extrema_ExtFlag # value = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX
    __entries: dict # value = {'Extrema_ExtFlag_MIN': (Extrema_ExtFlag.Extrema_ExtFlag_MIN, None), 'Extrema_ExtFlag_MAX': (Extrema_ExtFlag.Extrema_ExtFlag_MAX, None), 'Extrema_ExtFlag_MINMAX': (Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, None)}
    __members__: dict # value = {'Extrema_ExtFlag_MIN': Extrema_ExtFlag.Extrema_ExtFlag_MIN, 'Extrema_ExtFlag_MAX': Extrema_ExtFlag.Extrema_ExtFlag_MAX, 'Extrema_ExtFlag_MINMAX': Extrema_ExtFlag.Extrema_ExtFlag_MINMAX}
    pass
class Extrema_ExtPC():
    """
    None
    """
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Uinf : float,Usup : float,TolF : float=1e-10) -> None: 
        """
        initializes the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the <N>th extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the point of the <N>th extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the <N>th extremum square distance.
        """
    def TrimmedSquareDistances(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        if the curve is a trimmed curve, dist1 is a square distance between <P> and the point of parameter FirstParameter <P1> and dist2 is a square distance between <P> and the point of parameter LastParameter <P2>.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,TolF : float=1e-10) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,Uinf : float,Usup : float,TolF : float=1e-10) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_ExtPC2d():
    """
    None
    """
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Uinf : float,Usup : float,TolF : float=1e-10) -> None: 
        """
        initializes the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the <N>th extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnCurv2d: 
        """
        Returns the point of the <N>th extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the <N>th extremum square distance.
        """
    def TrimmedSquareDistances(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> Tuple[float, float]: 
        """
        if the curve is a trimmed curve, dist1 is a square distance between <P> and the point of parameter FirstParameter <P1> and dist2 is a square distance between <P> and the point of parameter LastParameter <P2>.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Uinf : float,Usup : float,TolF : float=1e-10) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,TolF : float=1e-10) -> None: ...
    pass
class Extrema_ExtPElC():
    """
    It calculates all the distances between a point and an elementary curve. These distances can be minimum or maximum.
    """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the Nth extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Hypr,Tol : float,Uinf : float,Usup : float) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Parab,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Circ,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Lin,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Elips,Tol : float,Uinf : float,Usup : float) -> None: ...
    def Point(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the point of the Nth extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Elips,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Hypr,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Circ,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Lin,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.gp.gp_Parab,Tol : float,Uinf : float,Usup : float) -> None: ...
    pass
class Extrema_ExtPElC2d():
    """
    It calculates all the distances between a point and an elementary curve. These distances can be minimum or maximum.
    """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the Nth extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt2d,C : OCP.gp.gp_Elips2d,Tol : float,Uinf : float,Usup : float) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt2d,C : OCP.gp.gp_Parab2d,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt2d,C : OCP.gp.gp_Circ2d,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt2d,L : OCP.gp.gp_Lin2d,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt2d,C : OCP.gp.gp_Hypr2d,Tol : float,Uinf : float,Usup : float) -> None: ...
    def Point(self,N : int) -> Extrema_POnCurv2d: 
        """
        Returns the point of the Nth extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth extremum square distance.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.gp.gp_Circ2d,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.gp.gp_Elips2d,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.gp.gp_Hypr2d,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.gp.gp_Lin2d,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.gp.gp_Parab2d,Tol : float,Uinf : float,Usup : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_ExtPElS():
    """
    It calculates all the extremum distances between a point and a surface. These distances can be minimum or maximum.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Torus,Tol : float) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Pln,Tol : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Cylinder,Tol : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Cone,Tol : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Sphere,Tol : float) -> None: ...
    def Point(self,N : int) -> Extrema_POnSurf: 
        """
        Returns the point of the Nth resulting distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth resulting square distance.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Cylinder,Tol : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Sphere,Tol : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Pln,Tol : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.gp.gp_Cone,Tol : float) -> None: ...
    pass
class Extrema_ExtPExtS(OCP.Standard.Standard_Transient):
    """
    It calculates all the extremum (minimum and maximum) distances between a point and a linear extrusion surface.It calculates all the extremum (minimum and maximum) distances between a point and a linear extrusion surface.It calculates all the extremum (minimum and maximum) distances between a point and a linear extrusion surface.
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
    def Initialize(self,S : OCP.GeomAdaptor.GeomAdaptor_HSurfaceOfLinearExtrusion,Uinf : float,Usup : float,Vinf : float,Vsup : float,TolU : float,TolV : float) -> None: 
        """
        Initializes the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def Point(self,N : int) -> Extrema_POnSurf: 
        """
        Returns the point of the Nth resulting distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth resulting square distance.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.GeomAdaptor.GeomAdaptor_HSurfaceOfLinearExtrusion,TolU : float,TolV : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.GeomAdaptor.GeomAdaptor_HSurfaceOfLinearExtrusion,Umin : float,Usup : float,Vmin : float,Vsup : float,TolU : float,TolV : float) -> None: ...
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
class Extrema_ExtPRevS(OCP.Standard.Standard_Transient):
    """
    It calculates all the extremum (minimum and maximum) distances between a point and a surface of revolution.It calculates all the extremum (minimum and maximum) distances between a point and a surface of revolution.It calculates all the extremum (minimum and maximum) distances between a point and a surface of revolution.
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
    def Initialize(self,S : OCP.GeomAdaptor.GeomAdaptor_HSurfaceOfRevolution,Umin : float,Usup : float,Vmin : float,Vsup : float,TolU : float,TolV : float) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def Point(self,N : int) -> Extrema_POnSurf: 
        """
        Returns the point of the Nth resulting distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth resulting square distance.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.GeomAdaptor.GeomAdaptor_HSurfaceOfRevolution,Umin : float,Usup : float,Vmin : float,Vsup : float,TolU : float,TolV : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.GeomAdaptor.GeomAdaptor_HSurfaceOfRevolution,TolU : float,TolV : float) -> None: ...
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
class Extrema_ExtPS():
    """
    It calculates all the extremum distances between a point and a surface. These distances can be minimum or maximum.
    """
    def Initialize(self,S : OCP.Adaptor3d.Adaptor3d_Surface,Uinf : float,Usup : float,Vinf : float,Vsup : float,TolU : float,TolV : float) -> None: 
        """
        Initializes the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the distances. An exception is raised if the fieds have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnSurf: 
        """
        Returns the point of the Nth resulting distance.
        """
    def SetAlgo(self,A : Extrema_ExtAlgo) -> None: 
        """
        None
        """
    def SetFlag(self,F : Extrema_ExtFlag) -> None: 
        """
        None
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth resulting square distance.
        """
    def TrimmedSquareDistances(self,PUfVf : OCP.gp.gp_Pnt,PUfVl : OCP.gp.gp_Pnt,PUlVf : OCP.gp.gp_Pnt,PUlVl : OCP.gp.gp_Pnt) -> Tuple[float, float, float, float]: 
        """
        if the surface is a trimmed surface, dUfVf is a square distance between <P> and the point of parameter FirstUParameter and FirstVParameter <PUfVf>. dUfVl is a square distance between <P> and the point of parameter FirstUParameter and LastVParameter <PUfVl>. dUlVf is a square distance between <P> and the point of parameter LastUParameter and FirstVParameter <PUlVf>. dUlVl is a square distance between <P> and the point of parameter LastUParameter and LastVParameter <PUlVl>.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.Adaptor3d.Adaptor3d_Surface,Uinf : float,Usup : float,Vinf : float,Vsup : float,TolU : float,TolV : float,F : Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,A : Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.Adaptor3d.Adaptor3d_Surface,TolU : float,TolV : float,F : Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,A : Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_ExtSS():
    """
    It calculates all the extremum distances between two surfaces. These distances can be minimum or maximum.
    """
    def Initialize(self,S2 : OCP.Adaptor3d.Adaptor3d_Surface,Uinf2 : float,Usup2 : float,Vinf2 : float,Vsup2 : float,TolS1 : float) -> None: 
        """
        Initializes the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the curve is on a parallel surface.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,Uinf1 : float,Usup1 : float,Vinf1 : float,Vsup1 : float,TolS1 : float) -> None: 
        """
        Computes the distances. An exception is raised if the fieds have not been initialized.
        """
    def Points(self,N : int,P1 : Extrema_POnSurf,P2 : Extrema_POnSurf) -> None: 
        """
        Returns the point of the Nth resulting distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth resulting square distance.
        """
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,Uinf1 : float,Usup1 : float,Vinf1 : float,Vsup1 : float,Uinf2 : float,Usup2 : float,Vinf2 : float,Vsup2 : float,TolS1 : float,TolS2 : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,TolS1 : float,TolS2 : float) -> None: ...
    pass
class Extrema_FuncExtCS(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Function to find extrema of the distance between a curve and a surface.
    """
    def Derivatives(self,UV : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculation of Fi'(U,V).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface) -> None: 
        """
        sets the field mysurf of the function.
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbExt(self) -> int: 
        """
        Return the number of found extrema.
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def PointOnCurve(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the Nth extremum on C.
        """
    def PointOnSurface(self,N : int) -> Extrema_POnSurf: 
        """
        Return the Nth extremum on S.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Return the value of the Nth distance.
        """
    def Value(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        Calculation of Fi(U,V).
        """
    def Values(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculation of Fi(U,V) and Fi'(U,V).
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    pass
class Extrema_FuncExtSS(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Function to find extrema of the distance between two surfaces.
    """
    def Derivatives(self,UV : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculate Fi'(U,V).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def Initialize(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface) -> None: 
        """
        sets the field mysurf of the function.
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbExt(self) -> int: 
        """
        Return the number of found extrema.
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def PointOnS1(self,N : int) -> Extrema_POnSurf: 
        """
        Return the Nth extremum on S1.
        """
    def PointOnS2(self,N : int) -> Extrema_POnSurf: 
        """
        Renvoie le Nieme extremum sur S2.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Return the value of the Nth distance.
        """
    def Value(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        Calculate Fi(U,V).
        """
    def Values(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculate Fi(U,V) and Fi'(U,V).
        """
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_FuncPSDist(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    Functional for search of extremum of the square Euclidean distance between point P and surface S, starting from approximate solution (u0, v0).
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : OCP.math.math_Vector,G : OCP.math.math_Vector) -> bool: 
        """
        Gradient.
        """
    def NbVariables(self) -> int: 
        """
        Number of variables.
        """
    def Value(self,X : OCP.math.math_Vector,F : float) -> bool: 
        """
        Value.
        """
    def Values(self,X : OCP.math.math_Vector,F : float,G : OCP.math.math_Vector) -> bool: 
        """
        Value and gradient.
        """
    def __init__(self,theS : OCP.Adaptor3d.Adaptor3d_Surface,theP : OCP.gp.gp_Pnt) -> None: ...
    pass
class Extrema_FuncPSNorm(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Functional for search of extremum of the distance between point P and surface S, starting from approximate solution (u0, v0).
    """
    def Derivatives(self,UV : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculate Fi'(U,V).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def Initialize(self,S : OCP.Adaptor3d.Adaptor3d_Surface) -> None: 
        """
        sets the field mysurf of the function.
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbExt(self) -> int: 
        """
        Return the number of found extrema.
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Point(self,N : int) -> Extrema_POnSurf: 
        """
        Returns the Nth extremum.
        """
    def SetPoint(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        sets the field mysurf of the function.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Return the value of the Nth distance.
        """
    def Value(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        Calculate Fi(U,V).
        """
    def Values(self,UV : OCP.math.math_Vector,F : OCP.math.math_Vector,DF : OCP.math.math_Matrix) -> bool: 
        """
        Calculate Fi(U,V) and Fi'(U,V).
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_GenExtCS():
    """
    It calculates all the extremum distances between acurve and a surface. These distances can be minimum or maximum.
    """
    @overload
    def Initialize(self,S : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,Umin : float,Usup : float,Vmin : float,Vsup : float,Tol2 : float) -> None: 
        """
        None

        None
        """
    @overload
    def Initialize(self,S : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,Tol2 : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    @overload
    def Perform(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbT : int,Tol1 : float) -> None: 
        """
        the algorithm is done with S An exception is raised if the fields have not been initialized.

        the algorithm is done with C An exception is raised if the fields have not been initialized.
        """
    @overload
    def Perform(self,C : OCP.Adaptor3d.Adaptor3d_Curve,NbT : int,tmin : float,tsup : float,Tol1 : float) -> None: ...
    def PointOnCurve(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the point of the Nth resulting distance.
        """
    def PointOnSurface(self,N : int) -> Extrema_POnSurf: 
        """
        Returns the point of the Nth resulting distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth resulting square distance.
        """
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface,NbT : int,NbU : int,NbV : int,Tol1 : float,Tol2 : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface,NbT : int,NbU : int,NbV : int,tmin : float,tsup : float,Umin : float,Usup : float,Vmin : float,Vsup : float,Tol1 : float,Tol2 : float) -> None: ...
    pass
class Extrema_GenExtPS():
    """
    It calculates all the extremum distances between a point and a surface. These distances can be minimum or maximum.
    """
    @overload
    def Initialize(self,S : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,TolU : float,TolV : float) -> None: 
        """
        None

        None
        """
    @overload
    def Initialize(self,S : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,Umin : float,Usup : float,Vmin : float,Vsup : float,TolU : float,TolV : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Perform(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        the algorithm is done with the point P. An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> Extrema_POnSurf: 
        """
        Returns the point of the Nth resulting distance.
        """
    def SetAlgo(self,A : Extrema_ExtAlgo) -> None: 
        """
        None
        """
    def SetFlag(self,F : Extrema_ExtFlag) -> None: 
        """
        None
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth resulting square distance.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,Umin : float,Usup : float,Vmin : float,Vsup : float,TolU : float,TolV : float,F : Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,A : Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,S : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,TolU : float,TolV : float,F : Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,A : Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    pass
class Extrema_GenExtSS():
    """
    It calculates all the extremum distances between two surfaces. These distances can be minimum or maximum.
    """
    @overload
    def Initialize(self,S2 : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,U2min : float,U2sup : float,V2min : float,V2sup : float,Tol2 : float) -> None: 
        """
        None

        None
        """
    @overload
    def Initialize(self,S2 : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,Tol2 : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns True if the distances are found.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    @overload
    def Perform(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,U1min : float,U1sup : float,V1min : float,V1sup : float,Tol1 : float) -> None: 
        """
        the algorithm is done with S1 An exception is raised if the fields have not been initialized.

        the algorithm is done withS1 An exception is raised if the fields have not been initialized.
        """
    @overload
    def Perform(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,Tol1 : float) -> None: ...
    def PointOnS1(self,N : int) -> Extrema_POnSurf: 
        """
        Returns the point of the Nth resulting distance.
        """
    def PointOnS2(self,N : int) -> Extrema_POnSurf: 
        """
        Returns the point of the Nth resulting distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the Nth resulting square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,U1min : float,U1sup : float,V1min : float,V1sup : float,U2min : float,U2sup : float,V2min : float,V2sup : float,Tol1 : float,Tol2 : float) -> None: ...
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,NbU : int,NbV : int,Tol1 : float,Tol2 : float) -> None: ...
    pass
class Extrema_GenLocateExtCS():
    """
    With two close points it calculates the distance between two surfaces. This distance can be a minimum or a maximum.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def Perform(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface,T : float,U : float,V : float,Tol1 : float,Tol2 : float) -> None: 
        """
        None
        """
    def PointOnCurve(self) -> Extrema_POnCurv: 
        """
        Returns the point of the extremum distance on C.
        """
    def PointOnSurface(self) -> Extrema_POnSurf: 
        """
        Returns the point of the extremum distance on S.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface,T : float,U : float,V : float,Tol1 : float,Tol2 : float) -> None: ...
    pass
class Extrema_GenLocateExtPS():
    """
    With a close point, it calculates the distance between a point and a surface. Criteria type is defined in "Perform" method.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def Perform(self,theP : OCP.gp.gp_Pnt,theU0 : float,theV0 : float,isDistanceCriteria : bool=False) -> None: 
        """
        Calculates the extrema between the point and the surface using a close point. The close point is defined by the parameter values theU0 and theV0. Type of the algorithm depends on the isDistanceCriteria flag. If flag value is false - normal projection criteria will be used. If flag value is true - distance criteria will be used.
        """
    def Point(self) -> Extrema_POnSurf: 
        """
        Returns the point of the extremum distance.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    def __init__(self,theS : OCP.Adaptor3d.Adaptor3d_Surface,theTolU : float=9.999999999999999e-10,theTolV : float=9.999999999999999e-10) -> None: ...
    pass
class Extrema_GenLocateExtSS():
    """
    With two close points it calculates the distance between two surfaces. This distance can be a minimum or a maximum.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def Perform(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,U1 : float,V1 : float,U2 : float,V2 : float,Tol1 : float,Tol2 : float) -> None: 
        """
        None
        """
    def PointOnS1(self) -> Extrema_POnSurf: 
        """
        Returns the point of the extremum distance on S1.
        """
    def PointOnS2(self) -> Extrema_POnSurf: 
        """
        Returns the point of the extremum distance on S2.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,U1 : float,V1 : float,U2 : float,V2 : float,Tol1 : float,Tol2 : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_GlobOptFuncCCC0(OCP.math.math_MultipleVarFunction):
    """
    This class implements function which calculate Eucluidean distance between point on curve and point on other curve in case of C1 and C2 continuity is C0.
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : float) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class Extrema_GlobOptFuncCCC1(OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    This class implements function which calculate Eucluidean distance between point on curve and point on other curve in case of C1 and C2 continuity is C1.
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : OCP.math.math_Vector,G : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : float) -> bool: 
        """
        None
        """
    def Values(self,X : OCP.math.math_Vector,F : float,G : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class Extrema_GlobOptFuncCCC2(OCP.math.math_MultipleVarFunctionWithHessian, OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    This class implements function which calculate Eucluidean distance between point on curve and point on other curve in case of C1 and C2 continuity is C2.
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : OCP.math.math_Vector,G : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : float) -> bool: 
        """
        None
        """
    @overload
    def Values(self,X : OCP.math.math_Vector,F : float,G : OCP.math.math_Vector) -> bool: 
        """
        None

        None
        """
    @overload
    def Values(self,X : OCP.math.math_Vector,F : float,G : OCP.math.math_Vector,H : OCP.math.math_Matrix) -> bool: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class Extrema_GlobOptFuncCS(OCP.math.math_MultipleVarFunctionWithHessian, OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    This class implements function which calculate square Eucluidean distance between point on curve and point on surface in case of continuity is C2.
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,theX : OCP.math.math_Vector,theG : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Value(self,theX : OCP.math.math_Vector,theF : float) -> bool: 
        """
        None
        """
    @overload
    def Values(self,theX : OCP.math.math_Vector,theF : float,theG : OCP.math.math_Vector,theH : OCP.math.math_Matrix) -> bool: 
        """
        None

        None
        """
    @overload
    def Values(self,theX : OCP.math.math_Vector,theF : float,theG : OCP.math.math_Vector) -> bool: ...
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    pass
class Extrema_HArray1OfPOnCurv(Extrema_Array1OfPOnCurv, OCP.Standard.Standard_Transient):
    def Array1(self) -> Extrema_Array1OfPOnCurv: 
        """
        None
        """
    def Assign(self,theOther : Extrema_Array1OfPOnCurv) -> Extrema_Array1OfPOnCurv: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Extrema_Array1OfPOnCurv: 
        """
        None
        """
    def ChangeFirst(self) -> Extrema_POnCurv: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Extrema_POnCurv: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Extrema_POnCurv: 
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
    def First(self) -> Extrema_POnCurv: 
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
    def Init(self,theValue : Extrema_POnCurv) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> Extrema_POnCurv: 
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
    def Move(self,theOther : Extrema_Array1OfPOnCurv) -> Extrema_Array1OfPOnCurv: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Extrema_POnCurv) -> None: 
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
    def Value(self,theIndex : int) -> Extrema_POnCurv: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Extrema_POnCurv) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array1OfPOnCurv) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class Extrema_HArray1OfPOnCurv2d(Extrema_Array1OfPOnCurv2d, OCP.Standard.Standard_Transient):
    def Array1(self) -> Extrema_Array1OfPOnCurv2d: 
        """
        None
        """
    def Assign(self,theOther : Extrema_Array1OfPOnCurv2d) -> Extrema_Array1OfPOnCurv2d: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Extrema_Array1OfPOnCurv2d: 
        """
        None
        """
    def ChangeFirst(self) -> Extrema_POnCurv2d: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Extrema_POnCurv2d: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Extrema_POnCurv2d: 
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
    def First(self) -> Extrema_POnCurv2d: 
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
    def Init(self,theValue : Extrema_POnCurv2d) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> Extrema_POnCurv2d: 
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
    def Move(self,theOther : Extrema_Array1OfPOnCurv2d) -> Extrema_Array1OfPOnCurv2d: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Extrema_POnCurv2d) -> None: 
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
    def Value(self,theIndex : int) -> Extrema_POnCurv2d: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array1OfPOnCurv2d) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Extrema_POnCurv2d) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
class Extrema_HArray1OfPOnSurf(Extrema_Array1OfPOnSurf, OCP.Standard.Standard_Transient):
    def Array1(self) -> Extrema_Array1OfPOnSurf: 
        """
        None
        """
    def Assign(self,theOther : Extrema_Array1OfPOnSurf) -> Extrema_Array1OfPOnSurf: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Extrema_Array1OfPOnSurf: 
        """
        None
        """
    def ChangeFirst(self) -> Extrema_POnSurf: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Extrema_POnSurf: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Extrema_POnSurf: 
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
    def First(self) -> Extrema_POnSurf: 
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
    def Init(self,theValue : Extrema_POnSurf) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> Extrema_POnSurf: 
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
    def Move(self,theOther : Extrema_Array1OfPOnSurf) -> Extrema_Array1OfPOnSurf: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Extrema_POnSurf) -> None: 
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
    def Value(self,theIndex : int) -> Extrema_POnSurf: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Extrema_POnSurf) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array1OfPOnSurf) -> None: ...
    def __iter__(self) -> iterator: ...
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
class Extrema_HArray2OfPOnCurv(Extrema_Array2OfPOnCurv, OCP.Standard.Standard_Transient):
    def Array2(self) -> Extrema_Array2OfPOnCurv: 
        """
        None
        """
    def Assign(self,theOther : Extrema_Array2OfPOnCurv) -> Extrema_Array2OfPOnCurv: 
        """
        Assignment
        """
    def ChangeArray2(self) -> Extrema_Array2OfPOnCurv: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> Extrema_POnCurv: 
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
    def Init(self,theValue : Extrema_POnCurv) -> None: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : Extrema_Array2OfPOnCurv) -> Extrema_Array2OfPOnCurv: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : Extrema_POnCurv) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> Extrema_POnCurv: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : Extrema_POnCurv) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array2OfPOnCurv) -> None: ...
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
class Extrema_HArray2OfPOnCurv2d(Extrema_Array2OfPOnCurv2d, OCP.Standard.Standard_Transient):
    def Array2(self) -> Extrema_Array2OfPOnCurv2d: 
        """
        None
        """
    def Assign(self,theOther : Extrema_Array2OfPOnCurv2d) -> Extrema_Array2OfPOnCurv2d: 
        """
        Assignment
        """
    def ChangeArray2(self) -> Extrema_Array2OfPOnCurv2d: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> Extrema_POnCurv2d: 
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
    def Init(self,theValue : Extrema_POnCurv2d) -> None: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : Extrema_Array2OfPOnCurv2d) -> Extrema_Array2OfPOnCurv2d: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : Extrema_POnCurv2d) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> Extrema_POnCurv2d: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Extrema_Array2OfPOnCurv2d) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : Extrema_POnCurv2d) -> None: ...
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
class Extrema_HArray2OfPOnSurf(Extrema_Array2OfPOnSurf, OCP.Standard.Standard_Transient):
    def Array2(self) -> Extrema_Array2OfPOnSurf: 
        """
        None
        """
    def Assign(self,theOther : Extrema_Array2OfPOnSurf) -> Extrema_Array2OfPOnSurf: 
        """
        Assignment
        """
    def ChangeArray2(self) -> Extrema_Array2OfPOnSurf: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> Extrema_POnSurf: 
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
    def Init(self,theValue : Extrema_POnSurf) -> None: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : Extrema_Array2OfPOnSurf) -> Extrema_Array2OfPOnSurf: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : Extrema_POnSurf) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> Extrema_POnSurf: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Extrema_Array2OfPOnSurf) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : Extrema_POnSurf) -> None: ...
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
class Extrema_HArray2OfPOnSurfParams(Extrema_Array2OfPOnSurfParams, OCP.Standard.Standard_Transient):
    def Array2(self) -> Extrema_Array2OfPOnSurfParams: 
        """
        None
        """
    def Assign(self,theOther : Extrema_Array2OfPOnSurfParams) -> Extrema_Array2OfPOnSurfParams: 
        """
        Assignment
        """
    def ChangeArray2(self) -> Extrema_Array2OfPOnSurfParams: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> Extrema_POnSurfParams: 
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
    def Init(self,theValue : Extrema_POnSurfParams) -> None: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : Extrema_Array2OfPOnSurfParams) -> Extrema_Array2OfPOnSurfParams: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : Extrema_POnSurfParams) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> Extrema_POnSurfParams: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : Extrema_POnSurfParams) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_Array2OfPOnSurfParams) -> None: ...
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
class Extrema_LocECC():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def Point(self,P1 : Extrema_POnCurv,P2 : Extrema_POnCurv) -> None: 
        """
        Returns the points of the extremum distance. P1 is on the first curve, P2 on the second one.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve,U0 : float,V0 : float,TolU : float,TolV : float) -> None: ...
    pass
class Extrema_LocECC2d():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def Point(self,P1 : Extrema_POnCurv2d,P2 : Extrema_POnCurv2d) -> None: 
        """
        Returns the points of the extremum distance. P1 is on the first curve, P2 on the second one.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,V0 : float,TolU : float,TolV : float) -> None: ...
    pass
class Extrema_LocEPCOfLocateExtPC():
    """
    None
    """
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Umin : float,Usup : float,TolU : float) -> None: 
        """
        sets the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def IsMin(self) -> bool: 
        """
        Returns True if the extremum distance is a minimum.
        """
    def Perform(self,P : OCP.gp.gp_Pnt,U0 : float) -> None: 
        """
        the algorithm is done with the point P. An exception is raised if the fields have not been initialized.
        """
    def Point(self) -> Extrema_POnCurv: 
        """
        Returns the point of the extremum distance.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,U0 : float,Umin : float,Usup : float,TolU : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,U0 : float,TolU : float) -> None: ...
    pass
class Extrema_LocEPCOfLocateExtPC2d():
    """
    None
    """
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Umin : float,Usup : float,TolU : float) -> None: 
        """
        sets the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def IsMin(self) -> bool: 
        """
        Returns True if the extremum distance is a minimum.
        """
    def Perform(self,P : OCP.gp.gp_Pnt2d,U0 : float) -> None: 
        """
        the algorithm is done with the point P. An exception is raised if the fields have not been initialized.
        """
    def Point(self) -> Extrema_POnCurv2d: 
        """
        Returns the point of the extremum distance.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,Umin : float,Usup : float,TolU : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,TolU : float) -> None: ...
    pass
class Extrema_LocateExtCC():
    """
    It calculates the distance between two curves with a close point; these distances can be maximum or minimum.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def Point(self,P1 : Extrema_POnCurv,P2 : Extrema_POnCurv) -> None: 
        """
        Returns the points of the extremum distance. P1 is on the first curve, P2 on the second one.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_Curve,C2 : OCP.Adaptor3d.Adaptor3d_Curve,U0 : float,V0 : float) -> None: ...
    pass
class Extrema_LocateExtCC2d():
    """
    It calculates the distance between two curves with a close point; these distances can be maximum or minimum.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def Point(self,P1 : Extrema_POnCurv2d,P2 : Extrema_POnCurv2d) -> None: 
        """
        Returns the points of the extremum distance. P1 is on the first curve, P2 on the second one.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    def __init__(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2 : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,V0 : float) -> None: ...
    pass
class Extrema_LocateExtPC():
    """
    None
    """
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Umin : float,Usup : float,TolF : float) -> None: 
        """
        sets the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def IsMin(self) -> bool: 
        """
        Returns True if the extremum distance is a minimum.
        """
    def Perform(self,P : OCP.gp.gp_Pnt,U0 : float) -> None: 
        """
        None
        """
    def Point(self) -> Extrema_POnCurv: 
        """
        Returns the point of the extremum distance.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,U0 : float,TolF : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve,U0 : float,Umin : float,Usup : float,TolF : float) -> None: ...
    pass
class Extrema_LocateExtPC2d():
    """
    None
    """
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d,Umin : float,Usup : float,TolF : float) -> None: 
        """
        sets the fields of the algorithm.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the distance is found.
        """
    def IsMin(self) -> bool: 
        """
        Returns True if the extremum distance is a minimum.
        """
    def Perform(self,P : OCP.gp.gp_Pnt2d,U0 : float) -> None: 
        """
        None
        """
    def Point(self) -> Extrema_POnCurv2d: 
        """
        Returns the point of the extremum distance.
        """
    def SquareDistance(self) -> float: 
        """
        Returns the value of the extremum square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,Umin : float,Usup : float,TolF : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,TolF : float) -> None: ...
    pass
class Extrema_PCFOfEPCOfELPCOfLocateExtPC(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,U : float,DF : float) -> bool: 
        """
        Calculation of F'(U).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: 
        """
        sets the field mycurve of the function.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Shows if the Nth distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Return the nunber of found extrema.
        """
    def Point(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the Nth extremum.
        """
    def SearchOfTolerance(self) -> float: 
        """
        Computes a Tol value. If 1st derivative of curve |D1|<Tol, it is considered D1=0.
        """
    def SetPoint(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        sets the field P of the function.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the Nth distance.
        """
    def SubIntervalInitialize(self,theUfirst : float,theUlast : float) -> None: 
        """
        Determines boundaries of subinterval for find of root.
        """
    def Value(self,U : float,F : float) -> bool: 
        """
        Calculation of F(U).
        """
    def Values(self,U : float,F : float,DF : float) -> bool: 
        """
        Calculation of F(U) and F'(U).
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class Extrema_PCFOfEPCOfELPCOfLocateExtPC2d(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,U : float,DF : float) -> bool: 
        """
        Calculation of F'(U).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        sets the field mycurve of the function.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Shows if the Nth distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Return the nunber of found extrema.
        """
    def Point(self,N : int) -> Extrema_POnCurv2d: 
        """
        Returns the Nth extremum.
        """
    def SearchOfTolerance(self) -> float: 
        """
        Computes a Tol value. If 1st derivative of curve |D1|<Tol, it is considered D1=0.
        """
    def SetPoint(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        sets the field P of the function.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the Nth distance.
        """
    def SubIntervalInitialize(self,theUfirst : float,theUlast : float) -> None: 
        """
        Determines boundaries of subinterval for find of root.
        """
    def Value(self,U : float,F : float) -> bool: 
        """
        Calculation of F(U).
        """
    def Values(self,U : float,F : float,DF : float) -> bool: 
        """
        Calculation of F(U) and F'(U).
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_PCFOfEPCOfExtPC(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,U : float,DF : float) -> bool: 
        """
        Calculation of F'(U).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: 
        """
        sets the field mycurve of the function.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Shows if the Nth distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Return the nunber of found extrema.
        """
    def Point(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the Nth extremum.
        """
    def SearchOfTolerance(self) -> float: 
        """
        Computes a Tol value. If 1st derivative of curve |D1|<Tol, it is considered D1=0.
        """
    def SetPoint(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        sets the field P of the function.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the Nth distance.
        """
    def SubIntervalInitialize(self,theUfirst : float,theUlast : float) -> None: 
        """
        Determines boundaries of subinterval for find of root.
        """
    def Value(self,U : float,F : float) -> bool: 
        """
        Calculation of F(U).
        """
    def Values(self,U : float,F : float,DF : float) -> bool: 
        """
        Calculation of F(U) and F'(U).
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_PCFOfEPCOfExtPC2d(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,U : float,DF : float) -> bool: 
        """
        Calculation of F'(U).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        sets the field mycurve of the function.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Shows if the Nth distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Return the nunber of found extrema.
        """
    def Point(self,N : int) -> Extrema_POnCurv2d: 
        """
        Returns the Nth extremum.
        """
    def SearchOfTolerance(self) -> float: 
        """
        Computes a Tol value. If 1st derivative of curve |D1|<Tol, it is considered D1=0.
        """
    def SetPoint(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        sets the field P of the function.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the Nth distance.
        """
    def SubIntervalInitialize(self,theUfirst : float,theUlast : float) -> None: 
        """
        Determines boundaries of subinterval for find of root.
        """
    def Value(self,U : float,F : float) -> bool: 
        """
        Calculation of F(U).
        """
    def Values(self,U : float,F : float,DF : float) -> bool: 
        """
        Calculation of F(U) and F'(U).
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_PCLocFOfLocEPCOfLocateExtPC(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,U : float,DF : float) -> bool: 
        """
        Calculation of F'(U).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def Initialize(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: 
        """
        sets the field mycurve of the function.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Shows if the Nth distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Return the nunber of found extrema.
        """
    def Point(self,N : int) -> Extrema_POnCurv: 
        """
        Returns the Nth extremum.
        """
    def SearchOfTolerance(self) -> float: 
        """
        Computes a Tol value. If 1st derivative of curve |D1|<Tol, it is considered D1=0.
        """
    def SetPoint(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        sets the field P of the function.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the Nth distance.
        """
    def SubIntervalInitialize(self,theUfirst : float,theUlast : float) -> None: 
        """
        Determines boundaries of subinterval for find of root.
        """
    def Value(self,U : float,F : float) -> bool: 
        """
        Calculation of F(U).
        """
    def Values(self,U : float,F : float,DF : float) -> bool: 
        """
        Calculation of F(U) and F'(U).
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_PCLocFOfLocEPCOfLocateExtPC2d(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,U : float,DF : float) -> bool: 
        """
        Calculation of F'(U).
        """
    def GetStateNumber(self) -> int: 
        """
        Save the found extremum.
        """
    def Initialize(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        sets the field mycurve of the function.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Shows if the Nth distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Return the nunber of found extrema.
        """
    def Point(self,N : int) -> Extrema_POnCurv2d: 
        """
        Returns the Nth extremum.
        """
    def SearchOfTolerance(self) -> float: 
        """
        Computes a Tol value. If 1st derivative of curve |D1|<Tol, it is considered D1=0.
        """
    def SetPoint(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        sets the field P of the function.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the Nth distance.
        """
    def SubIntervalInitialize(self,theUfirst : float,theUlast : float) -> None: 
        """
        Determines boundaries of subinterval for find of root.
        """
    def Value(self,U : float,F : float) -> bool: 
        """
        Calculation of F(U).
        """
    def Values(self,U : float,F : float,DF : float) -> bool: 
        """
        Calculation of F(U) and F'(U).
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_POnCurv():
    """
    None
    """
    def Parameter(self) -> float: 
        """
        Returns the parameter on the curve.
        """
    def SetValues(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        sets the point and parameter values.
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,U : float,P : OCP.gp.gp_Pnt) -> None: ...
    pass
class Extrema_POnCurv2d():
    """
    None
    """
    def Parameter(self) -> float: 
        """
        Returns the parameter on the curve.
        """
    def SetValues(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        sets the point and parameter values.
        """
    def Value(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the point.
        """
    @overload
    def __init__(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_POnSurf():
    """
    Definition of a point on surface.
    """
    def Parameter(self) -> Tuple[float, float]: 
        """
        Returns the parameter values on the surface.

        Returns the parameter values on the surface.
        """
    @overload
    def SetParameters(self,theU : float,theV : float,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the params of current POnSurf instance. (e.g. to the point to be projected).

        Sets the params of current POnSurf instance. (e.g. to the point to be projected).
        """
    @overload
    def SetParameters(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: ...
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the 3d point.

        Returns the 3d point.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: ...
    pass
class Extrema_POnSurfParams(Extrema_POnSurf):
    """
    Data container for point on surface parameters. These parameters are required to compute an initial approximation for extrema computation.
    """
    def GetElementType(self) -> Extrema_ElementType: 
        """
        Query the element type on which this point is situated.

        Query the element type on which this point is situated.
        """
    def GetIndices(self) -> Tuple[int, int]: 
        """
        Query the U and V indices of an element that contains this point.

        Query the U and V indices of an element that contains this point.
        """
    def GetSqrDistance(self) -> float: 
        """
        Query the square distance from this point to another one.

        Query the square distance from this point to another one.
        """
    def Parameter(self) -> Tuple[float, float]: 
        """
        Returns the parameter values on the surface.

        Returns the parameter values on the surface.
        """
    def SetElementType(self,theElementType : Extrema_ElementType) -> None: 
        """
        Sets the element type on which this point is situated.

        Sets the element type on which this point is situated.
        """
    def SetIndices(self,theIndexU : int,theIndexV : int) -> None: 
        """
        Sets the U and V indices of an element that contains this point.

        Sets the U and V indices of an element that contains this point.
        """
    @overload
    def SetParameters(self,theU : float,theV : float,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the params of current POnSurf instance. (e.g. to the point to be projected).

        Sets the params of current POnSurf instance. (e.g. to the point to be projected).
        """
    @overload
    def SetParameters(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: ...
    def SetSqrDistance(self,theSqrDistance : float) -> None: 
        """
        Sets the square distance from this point to another one (e.g. to the point to be projected).

        Sets the square distance from this point to another one (e.g. to the point to be projected).
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the 3d point.

        Returns the 3d point.
        """
    @overload
    def __init__(self,theU : float,theV : float,thePnt : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Extrema_SequenceOfPOnCurv(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Extrema_SequenceOfPOnCurv) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Extrema_POnCurv) -> None: ...
    def Assign(self,theOther : Extrema_SequenceOfPOnCurv) -> Extrema_SequenceOfPOnCurv: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Extrema_POnCurv: 
        """
        First item access
        """
    def ChangeLast(self) -> Extrema_POnCurv: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Extrema_POnCurv: 
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
    def First(self) -> Extrema_POnCurv: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Extrema_SequenceOfPOnCurv) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Extrema_POnCurv) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Extrema_SequenceOfPOnCurv) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Extrema_POnCurv) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Extrema_POnCurv: 
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
    def Prepend(self,theItem : Extrema_POnCurv) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Extrema_SequenceOfPOnCurv) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Extrema_POnCurv) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Extrema_SequenceOfPOnCurv) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Extrema_POnCurv: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Extrema_SequenceOfPOnCurv) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Extrema_SequenceOfPOnCurv2d(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Extrema_POnCurv2d) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Extrema_SequenceOfPOnCurv2d) -> None: ...
    def Assign(self,theOther : Extrema_SequenceOfPOnCurv2d) -> Extrema_SequenceOfPOnCurv2d: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Extrema_POnCurv2d: 
        """
        First item access
        """
    def ChangeLast(self) -> Extrema_POnCurv2d: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Extrema_POnCurv2d: 
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
    def First(self) -> Extrema_POnCurv2d: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Extrema_SequenceOfPOnCurv2d) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Extrema_POnCurv2d) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Extrema_POnCurv2d) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Extrema_SequenceOfPOnCurv2d) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Extrema_POnCurv2d: 
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
    def Prepend(self,theItem : Extrema_POnCurv2d) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Extrema_SequenceOfPOnCurv2d) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Extrema_POnCurv2d) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Extrema_SequenceOfPOnCurv2d) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Extrema_POnCurv2d: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Extrema_SequenceOfPOnCurv2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Extrema_SequenceOfPOnSurf(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Extrema_POnSurf) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Extrema_SequenceOfPOnSurf) -> None: ...
    def Assign(self,theOther : Extrema_SequenceOfPOnSurf) -> Extrema_SequenceOfPOnSurf: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Extrema_POnSurf: 
        """
        First item access
        """
    def ChangeLast(self) -> Extrema_POnSurf: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Extrema_POnSurf: 
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
    def First(self) -> Extrema_POnSurf: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Extrema_SequenceOfPOnSurf) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Extrema_POnSurf) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Extrema_POnSurf) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Extrema_SequenceOfPOnSurf) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Extrema_POnSurf: 
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
    def Prepend(self,theItem : Extrema_POnSurf) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Extrema_SequenceOfPOnSurf) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Extrema_POnSurf) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Extrema_SequenceOfPOnSurf) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Extrema_POnSurf: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Extrema_SequenceOfPOnSurf) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Extrema_UBTreeFillerOfSphere():
    """
    This class is used to fill an UBTree in a random order. The quality of a tree is much better (from the point of view of the search time) if objects are added to it in a random order to avoid adding a chain of neerby objects one following each other.
    """
    def Add(self,theObj : int,theBnd : OCP.Bnd.Bnd_Sphere) -> None: 
        """
        Adds a pair (theObj, theBnd) to my sequence
        """
    def CheckTree(self,theStream : Any) -> int: 
        """
        Check the filled tree for the total number of items and the balance outputting these results to std::ostream.
        """
    def Fill(self) -> int: 
        """
        Fills the tree with the objects from my sequence. This method clears the internal buffer of added items making sure that no item would be added twice.
        """
    def Reset(self) -> None: 
        """
        Remove all data from Filler, partculary if the Tree no more needed so the destructor of this Filler should not populate the useless Tree.
        """
    def __init__(self,theTree : Extrema_UBTreeOfSphere,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None,isFullRandom : bool=True) -> None: ...
    pass
class Extrema_UBTreeOfSphere():
    """
    The algorithm of unbalanced binary tree of overlapped bounding boxes.
    """
    def Add(self,theObj : int,theBnd : OCP.Bnd.Bnd_Sphere) -> bool: 
        """
        Update the tree with a new object and its bounding box.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Recommended to be used only in sub-classes.
        """
    def Clear(self,aNewAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clears the contents of the tree.
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
Extrema_ExtAlgo_Grad: OCP.Extrema.Extrema_ExtAlgo # value = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad
Extrema_ExtAlgo_Tree: OCP.Extrema.Extrema_ExtAlgo # value = Extrema_ExtAlgo.Extrema_ExtAlgo_Tree
Extrema_ExtFlag_MAX: OCP.Extrema.Extrema_ExtFlag # value = Extrema_ExtFlag.Extrema_ExtFlag_MAX
Extrema_ExtFlag_MIN: OCP.Extrema.Extrema_ExtFlag # value = Extrema_ExtFlag.Extrema_ExtFlag_MIN
Extrema_ExtFlag_MINMAX: OCP.Extrema.Extrema_ExtFlag # value = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX
Extrema_Face: OCP.Extrema.Extrema_ElementType # value = Extrema_ElementType.Extrema_Face
Extrema_Node: OCP.Extrema.Extrema_ElementType # value = Extrema_ElementType.Extrema_Node
Extrema_UIsoEdge: OCP.Extrema.Extrema_ElementType # value = Extrema_ElementType.Extrema_UIsoEdge
Extrema_VIsoEdge: OCP.Extrema.Extrema_ElementType # value = Extrema_ElementType.Extrema_VIsoEdge
