import OCP.AppParCurves
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.TColgp
import OCP.Standard
import OCP.NCollection
import OCP.math
import OCP.gp
__all__  = [
"AppParCurves",
"AppParCurves_Array1OfConstraintCouple",
"AppParCurves_Array1OfMultiBSpCurve",
"AppParCurves_Array1OfMultiCurve",
"AppParCurves_Array1OfMultiPoint",
"AppParCurves_Constraint",
"AppParCurves_ConstraintCouple",
"AppParCurves_HArray1OfConstraintCouple",
"AppParCurves_HArray1OfMultiBSpCurve",
"AppParCurves_HArray1OfMultiCurve",
"AppParCurves_HArray1OfMultiPoint",
"AppParCurves_MultiCurve",
"AppParCurves_MultiBSpCurve",
"AppParCurves_MultiPoint",
"AppParCurves_SequenceOfMultiBSpCurve",
"AppParCurves_SequenceOfMultiCurve",
"AppParCurves_CurvaturePoint",
"AppParCurves_NoConstraint",
"AppParCurves_PassPoint",
"AppParCurves_TangencyPoint"
]
class AppParCurves():
    """
    Parallel Approximation in n curves. This package gives all the algorithms used to approximate a MultiLine described by the tool MLineTool. The result of the approximation will be a MultiCurve.
    """
    @staticmethod
    def BernsteinMatrix_s(NbPoles : int,U : OCP.math.math_Vector,A : OCP.math.math_Matrix) -> None: 
        """
        None
        """
    @staticmethod
    def Bernstein_s(NbPoles : int,U : OCP.math.math_Vector,A : OCP.math.math_Matrix,DA : OCP.math.math_Matrix) -> None: 
        """
        None
        """
    @staticmethod
    def SecondDerivativeBernstein_s(U : float,DDA : OCP.math.math_Vector) -> None: 
        """
        None
        """
    @staticmethod
    def SplineFunction_s(NbPoles : int,Degree : int,Parameters : OCP.math.math_Vector,FlatKnots : OCP.math.math_Vector,A : OCP.math.math_Matrix,DA : OCP.math.math_Matrix,Index : OCP.math.math_IntegerVector) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class AppParCurves_Array1OfConstraintCouple():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : AppParCurves_Array1OfConstraintCouple) -> AppParCurves_Array1OfConstraintCouple: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> AppParCurves_ConstraintCouple: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppParCurves_ConstraintCouple: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_ConstraintCouple: 
        """
        Variable value access
        """
    def First(self) -> AppParCurves_ConstraintCouple: 
        """
        Returns first element
        """
    def Init(self,theValue : AppParCurves_ConstraintCouple) -> None: 
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
    def Last(self) -> AppParCurves_ConstraintCouple: 
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
    def Move(self,theOther : AppParCurves_Array1OfConstraintCouple) -> AppParCurves_Array1OfConstraintCouple: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppParCurves_ConstraintCouple) -> None: 
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
    def Value(self,theIndex : int) -> AppParCurves_ConstraintCouple: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : AppParCurves_ConstraintCouple,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : AppParCurves_Array1OfConstraintCouple) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class AppParCurves_Array1OfMultiBSpCurve():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : AppParCurves_Array1OfMultiBSpCurve) -> AppParCurves_Array1OfMultiBSpCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> AppParCurves_MultiBSpCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppParCurves_MultiBSpCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_MultiBSpCurve: 
        """
        Variable value access
        """
    def First(self) -> AppParCurves_MultiBSpCurve: 
        """
        Returns first element
        """
    def Init(self,theValue : AppParCurves_MultiBSpCurve) -> None: 
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
    def Last(self) -> AppParCurves_MultiBSpCurve: 
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
    def Move(self,theOther : AppParCurves_Array1OfMultiBSpCurve) -> AppParCurves_Array1OfMultiBSpCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppParCurves_MultiBSpCurve) -> None: 
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
    def Value(self,theIndex : int) -> AppParCurves_MultiBSpCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : AppParCurves_MultiBSpCurve,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : AppParCurves_Array1OfMultiBSpCurve) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class AppParCurves_Array1OfMultiCurve():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : AppParCurves_Array1OfMultiCurve) -> AppParCurves_Array1OfMultiCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> AppParCurves_MultiCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppParCurves_MultiCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_MultiCurve: 
        """
        Variable value access
        """
    def First(self) -> AppParCurves_MultiCurve: 
        """
        Returns first element
        """
    def Init(self,theValue : AppParCurves_MultiCurve) -> None: 
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
    def Last(self) -> AppParCurves_MultiCurve: 
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
    def Move(self,theOther : AppParCurves_Array1OfMultiCurve) -> AppParCurves_Array1OfMultiCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppParCurves_MultiCurve) -> None: 
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
    def Value(self,theIndex : int) -> AppParCurves_MultiCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : AppParCurves_Array1OfMultiCurve) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : AppParCurves_MultiCurve,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class AppParCurves_Array1OfMultiPoint():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : AppParCurves_Array1OfMultiPoint) -> AppParCurves_Array1OfMultiPoint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> AppParCurves_MultiPoint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppParCurves_MultiPoint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_MultiPoint: 
        """
        Variable value access
        """
    def First(self) -> AppParCurves_MultiPoint: 
        """
        Returns first element
        """
    def Init(self,theValue : AppParCurves_MultiPoint) -> None: 
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
    def Last(self) -> AppParCurves_MultiPoint: 
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
    def Move(self,theOther : AppParCurves_Array1OfMultiPoint) -> AppParCurves_Array1OfMultiPoint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppParCurves_MultiPoint) -> None: 
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
    def Value(self,theIndex : int) -> AppParCurves_MultiPoint: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : AppParCurves_MultiPoint,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : AppParCurves_Array1OfMultiPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class AppParCurves_Constraint():
    """
    - NoConstraint: this point has no constraints. - PassPoint: the approximation curve passes through this point. - TangencyPoint: this point has a tangency constraint. - CurvaturePoint: this point has a curvature constraint.

    Members:

      AppParCurves_NoConstraint

      AppParCurves_PassPoint

      AppParCurves_TangencyPoint

      AppParCurves_CurvaturePoint
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    AppParCurves_CurvaturePoint: OCP.AppParCurves.AppParCurves_Constraint # value = AppParCurves_Constraint.AppParCurves_CurvaturePoint
    AppParCurves_NoConstraint: OCP.AppParCurves.AppParCurves_Constraint # value = AppParCurves_Constraint.AppParCurves_NoConstraint
    AppParCurves_PassPoint: OCP.AppParCurves.AppParCurves_Constraint # value = AppParCurves_Constraint.AppParCurves_PassPoint
    AppParCurves_TangencyPoint: OCP.AppParCurves.AppParCurves_Constraint # value = AppParCurves_Constraint.AppParCurves_TangencyPoint
    __entries: dict # value = {'AppParCurves_NoConstraint': (AppParCurves_Constraint.AppParCurves_NoConstraint, None), 'AppParCurves_PassPoint': (AppParCurves_Constraint.AppParCurves_PassPoint, None), 'AppParCurves_TangencyPoint': (AppParCurves_Constraint.AppParCurves_TangencyPoint, None), 'AppParCurves_CurvaturePoint': (AppParCurves_Constraint.AppParCurves_CurvaturePoint, None)}
    __members__: dict # value = {'AppParCurves_NoConstraint': AppParCurves_Constraint.AppParCurves_NoConstraint, 'AppParCurves_PassPoint': AppParCurves_Constraint.AppParCurves_PassPoint, 'AppParCurves_TangencyPoint': AppParCurves_Constraint.AppParCurves_TangencyPoint, 'AppParCurves_CurvaturePoint': AppParCurves_Constraint.AppParCurves_CurvaturePoint}
    pass
class AppParCurves_ConstraintCouple():
    """
    associates an index and a constraint for an object. This couple is used by AppDef_TheVariational when performing approximations.
    """
    def Constraint(self) -> AppParCurves_Constraint: 
        """
        returns the constraint of the object.
        """
    def Index(self) -> int: 
        """
        returns the index of the constraint object.
        """
    def SetConstraint(self,Cons : AppParCurves_Constraint) -> None: 
        """
        Changes the constraint of the object.
        """
    def SetIndex(self,TheIndex : int) -> None: 
        """
        Changes the index of the constraint object.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,TheIndex : int,Cons : AppParCurves_Constraint) -> None: ...
    pass
class AppParCurves_HArray1OfConstraintCouple(AppParCurves_Array1OfConstraintCouple, OCP.Standard.Standard_Transient):
    def Array1(self) -> AppParCurves_Array1OfConstraintCouple: 
        """
        None
        """
    def Assign(self,theOther : AppParCurves_Array1OfConstraintCouple) -> AppParCurves_Array1OfConstraintCouple: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> AppParCurves_Array1OfConstraintCouple: 
        """
        None
        """
    def ChangeFirst(self) -> AppParCurves_ConstraintCouple: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppParCurves_ConstraintCouple: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_ConstraintCouple: 
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
    def First(self) -> AppParCurves_ConstraintCouple: 
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
    def Init(self,theValue : AppParCurves_ConstraintCouple) -> None: 
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
    def Last(self) -> AppParCurves_ConstraintCouple: 
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
    def Move(self,theOther : AppParCurves_Array1OfConstraintCouple) -> AppParCurves_Array1OfConstraintCouple: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppParCurves_ConstraintCouple) -> None: 
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
    def Value(self,theIndex : int) -> AppParCurves_ConstraintCouple: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : AppParCurves_Array1OfConstraintCouple) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : AppParCurves_ConstraintCouple) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
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
class AppParCurves_HArray1OfMultiBSpCurve(AppParCurves_Array1OfMultiBSpCurve, OCP.Standard.Standard_Transient):
    def Array1(self) -> AppParCurves_Array1OfMultiBSpCurve: 
        """
        None
        """
    def Assign(self,theOther : AppParCurves_Array1OfMultiBSpCurve) -> AppParCurves_Array1OfMultiBSpCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> AppParCurves_Array1OfMultiBSpCurve: 
        """
        None
        """
    def ChangeFirst(self) -> AppParCurves_MultiBSpCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppParCurves_MultiBSpCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_MultiBSpCurve: 
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
    def First(self) -> AppParCurves_MultiBSpCurve: 
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
    def Init(self,theValue : AppParCurves_MultiBSpCurve) -> None: 
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
    def Last(self) -> AppParCurves_MultiBSpCurve: 
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
    def Move(self,theOther : AppParCurves_Array1OfMultiBSpCurve) -> AppParCurves_Array1OfMultiBSpCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppParCurves_MultiBSpCurve) -> None: 
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
    def Value(self,theIndex : int) -> AppParCurves_MultiBSpCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : AppParCurves_MultiBSpCurve) -> None: ...
    @overload
    def __init__(self,theOther : AppParCurves_Array1OfMultiBSpCurve) -> None: ...
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
class AppParCurves_HArray1OfMultiCurve(AppParCurves_Array1OfMultiCurve, OCP.Standard.Standard_Transient):
    def Array1(self) -> AppParCurves_Array1OfMultiCurve: 
        """
        None
        """
    def Assign(self,theOther : AppParCurves_Array1OfMultiCurve) -> AppParCurves_Array1OfMultiCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> AppParCurves_Array1OfMultiCurve: 
        """
        None
        """
    def ChangeFirst(self) -> AppParCurves_MultiCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppParCurves_MultiCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_MultiCurve: 
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
    def First(self) -> AppParCurves_MultiCurve: 
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
    def Init(self,theValue : AppParCurves_MultiCurve) -> None: 
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
    def Last(self) -> AppParCurves_MultiCurve: 
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
    def Move(self,theOther : AppParCurves_Array1OfMultiCurve) -> AppParCurves_Array1OfMultiCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppParCurves_MultiCurve) -> None: 
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
    def Value(self,theIndex : int) -> AppParCurves_MultiCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : AppParCurves_MultiCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : AppParCurves_Array1OfMultiCurve) -> None: ...
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
class AppParCurves_HArray1OfMultiPoint(AppParCurves_Array1OfMultiPoint, OCP.Standard.Standard_Transient):
    def Array1(self) -> AppParCurves_Array1OfMultiPoint: 
        """
        None
        """
    def Assign(self,theOther : AppParCurves_Array1OfMultiPoint) -> AppParCurves_Array1OfMultiPoint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> AppParCurves_Array1OfMultiPoint: 
        """
        None
        """
    def ChangeFirst(self) -> AppParCurves_MultiPoint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> AppParCurves_MultiPoint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_MultiPoint: 
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
    def First(self) -> AppParCurves_MultiPoint: 
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
    def Init(self,theValue : AppParCurves_MultiPoint) -> None: 
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
    def Last(self) -> AppParCurves_MultiPoint: 
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
    def Move(self,theOther : AppParCurves_Array1OfMultiPoint) -> AppParCurves_Array1OfMultiPoint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : AppParCurves_MultiPoint) -> None: 
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
    def Value(self,theIndex : int) -> AppParCurves_MultiPoint: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : AppParCurves_MultiPoint) -> None: ...
    @overload
    def __init__(self,theOther : AppParCurves_Array1OfMultiPoint) -> None: ...
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
class AppParCurves_MultiCurve():
    """
    This class describes a MultiCurve approximating a Multiline. As a Multiline is a set of n lines, a MultiCurve is a set of n curves. These curves are Bezier curves. A MultiCurve is composed of m MultiPoint. The approximating degree of these n curves is the same for each one.
    """
    @overload
    def Curve(self,CuIndex : int,TabPnt : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        returns the Pole array of the curve of range CuIndex. An exception is raised if the dimension of the curve is 2d.

        returns the Pole array of the curve of range CuIndex. An exception is raised if the dimension of the curve is 3d.
        """
    @overload
    def Curve(self,CuIndex : int,TabPnt : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def D1(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        returns the value of the point with a parameter U on the Bezier curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 3d.

        returns the value of the point with a parameter U on the Bezier curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 2d.
        """
    @overload
    def D1(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @overload
    def D2(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        returns the value of the point with a parameter U on the Bezier curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 3d.

        returns the value of the point with a parameter U on the Bezier curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 2d.
        """
    @overload
    def D2(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: ...
    def Degree(self) -> int: 
        """
        returns the degree of the curves.
        """
    def Dimension(self,CuIndex : int) -> int: 
        """
        returns the dimension of the CuIndex curve. An exception is raised if CuIndex<0 or CuIndex>NbCurves.
        """
    def Dump(self,o : Any) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def NbCurves(self) -> int: 
        """
        Returns the number of curves resulting from the approximation of a MultiLine.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles on curves resulting from the approximation of a MultiLine.
        """
    def Pole(self,CuIndex : int,Nieme : int) -> OCP.gp.gp_Pnt: 
        """
        returns the Nieme pole of the CuIndex curve. the curve must be a 3D curve.
        """
    def Pole2d(self,CuIndex : int,Nieme : int) -> OCP.gp.gp_Pnt2d: 
        """
        returns the Nieme pole of the CuIndex curve. the curve must be a 2D curve.
        """
    def SetNbPoles(self,nbPoles : int) -> None: 
        """
        The number of poles of the MultiCurve will be set to <nbPoles>.
        """
    def SetValue(self,Index : int,MPoint : AppParCurves_MultiPoint) -> None: 
        """
        sets the MultiPoint of range Index to the value <MPoint>. An exception is raised if Index <0 or Index >NbMPoint.
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
    def Value(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt) -> None: 
        """
        returns the Index MultiPoint. An exception is raised if Index <0 or Index >Degree+1.

        returns the value of the point with a parameter U on the Bezier curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 2d.

        returns the value of the point with a parameter U on the Bezier curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 3d.
        """
    @overload
    def Value(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def Value(self,Index : int) -> AppParCurves_MultiPoint: ...
    @overload
    def __init__(self,tabMU : AppParCurves_Array1OfMultiPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,NbPol : int) -> None: ...
    pass
class AppParCurves_MultiBSpCurve(AppParCurves_MultiCurve):
    """
    This class describes a MultiBSpCurve approximating a Multiline. Just as a Multiline is a set of a given number of lines, a MultiBSpCurve is a set of a specified number of bsplines defined by: - A specified number of MultiPoints - the poles of a specified number of curves - The degree of approximation identical for each of the specified number of curves.
    """
    @overload
    def Curve(self,CuIndex : int,TabPnt : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        returns the Pole array of the curve of range CuIndex. An exception is raised if the dimension of the curve is 2d.

        returns the Pole array of the curve of range CuIndex. An exception is raised if the dimension of the curve is 3d.
        """
    @overload
    def Curve(self,CuIndex : int,TabPnt : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def D1(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        returns the value of the point with a parameter U on the BSpline curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 3d.

        returns the value of the point with a parameter U on the BSpline curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 2d.
        """
    @overload
    def D1(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: ...
    @overload
    def D2(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        returns the value of the point with a parameter U on the BSpline curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 3d.

        returns the value of the point with a parameter U on the BSpline curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 2d.
        """
    @overload
    def D2(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: ...
    def Degree(self) -> int: 
        """
        returns the degree of the curve(s).
        """
    def Dimension(self,CuIndex : int) -> int: 
        """
        returns the dimension of the CuIndex curve. An exception is raised if CuIndex<0 or CuIndex>NbCurves.
        """
    def Dump(self,o : Any) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def Knots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Returns an array of Reals containing the multiplicities of curves resulting from the approximation.
        """
    def Multiplicities(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        Returns an array of Reals containing the multiplicities of curves resulting from the approximation.
        """
    def NbCurves(self) -> int: 
        """
        Returns the number of curves resulting from the approximation of a MultiLine.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles on curves resulting from the approximation of a MultiLine.
        """
    def Pole(self,CuIndex : int,Nieme : int) -> OCP.gp.gp_Pnt: 
        """
        returns the Nieme pole of the CuIndex curve. the curve must be a 3D curve.
        """
    def Pole2d(self,CuIndex : int,Nieme : int) -> OCP.gp.gp_Pnt2d: 
        """
        returns the Nieme pole of the CuIndex curve. the curve must be a 2D curve.
        """
    def SetKnots(self,theKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Knots of the multiBSpCurve are assigned to <theknots>.
        """
    def SetMultiplicities(self,theMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Multiplicities of the multiBSpCurve are assigned to <theMults>.
        """
    def SetNbPoles(self,nbPoles : int) -> None: 
        """
        The number of poles of the MultiCurve will be set to <nbPoles>.
        """
    def SetValue(self,Index : int,MPoint : AppParCurves_MultiPoint) -> None: 
        """
        sets the MultiPoint of range Index to the value <MPoint>. An exception is raised if Index <0 or Index >NbMPoint.
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
    def Value(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt2d) -> None: 
        """
        returns the value of the point with a parameter U on the BSpline curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 2d.

        returns the value of the point with a parameter U on the BSpline curve number CuIndex. An exception is raised if CuIndex <0 or > NbCurves. An exception is raised if the curve dimension is 3d.
        """
    @overload
    def Value(self,CuIndex : int,U : float,Pt : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,tabMU : AppParCurves_Array1OfMultiPoint,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
    @overload
    def __init__(self,SC : AppParCurves_MultiCurve,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
    @overload
    def __init__(self,NbPol : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class AppParCurves_MultiPoint():
    """
    This class describes Points composing a MultiPoint. These points can be 2D or 3D. The user must first give the 3D Points and then the 2D Points. They are Poles of a Bezier Curve. This class is used either to define data input or results when performing the approximation of several lines in parallel.
    """
    def Dimension(self,Index : int) -> int: 
        """
        returns the dimension of the point of range Index. An exception is raised if Index <0 or Index > NbCurves.

        returns the dimension of the point of range Index. An exception is raised if Index <0 or Index > NbCurves.
        """
    def Dump(self,o : Any) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
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
    def SetPoint(self,Index : int,Point : OCP.gp.gp_Pnt) -> None: 
        """
        the 3d Point of range Index of this MultiPoint is set to <Point>. An exception is raised if Index < 0 or Index > number of 3d Points.
        """
    def SetPoint2d(self,Index : int,Point : OCP.gp.gp_Pnt2d) -> None: 
        """
        The 2d Point of range Index is set to <Point>. An exception is raised if Index > 3d Points or Index > total number of Points.
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
    def __init__(self,tabP2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @overload
    def __init__(self,tabP : OCP.TColgp.TColgp_Array1OfPnt,tabP2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    @overload
    def __init__(self,NbPoints : int,NbPoints2d : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,tabP : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    pass
class AppParCurves_SequenceOfMultiBSpCurve(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : AppParCurves_SequenceOfMultiBSpCurve) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : AppParCurves_MultiBSpCurve) -> None: ...
    def Assign(self,theOther : AppParCurves_SequenceOfMultiBSpCurve) -> AppParCurves_SequenceOfMultiBSpCurve: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> AppParCurves_MultiBSpCurve: 
        """
        First item access
        """
    def ChangeLast(self) -> AppParCurves_MultiBSpCurve: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_MultiBSpCurve: 
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
    def First(self) -> AppParCurves_MultiBSpCurve: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : AppParCurves_MultiBSpCurve) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : AppParCurves_SequenceOfMultiBSpCurve) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : AppParCurves_MultiBSpCurve) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : AppParCurves_SequenceOfMultiBSpCurve) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> AppParCurves_MultiBSpCurve: 
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
    def Prepend(self,theSeq : AppParCurves_SequenceOfMultiBSpCurve) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : AppParCurves_MultiBSpCurve) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : AppParCurves_MultiBSpCurve) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : AppParCurves_SequenceOfMultiBSpCurve) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> AppParCurves_MultiBSpCurve: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : AppParCurves_SequenceOfMultiBSpCurve) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class AppParCurves_SequenceOfMultiCurve(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : AppParCurves_SequenceOfMultiCurve) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : AppParCurves_MultiCurve) -> None: ...
    def Assign(self,theOther : AppParCurves_SequenceOfMultiCurve) -> AppParCurves_SequenceOfMultiCurve: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> AppParCurves_MultiCurve: 
        """
        First item access
        """
    def ChangeLast(self) -> AppParCurves_MultiCurve: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> AppParCurves_MultiCurve: 
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
    def First(self) -> AppParCurves_MultiCurve: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : AppParCurves_MultiCurve) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : AppParCurves_SequenceOfMultiCurve) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : AppParCurves_MultiCurve) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : AppParCurves_SequenceOfMultiCurve) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> AppParCurves_MultiCurve: 
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
    def Prepend(self,theItem : AppParCurves_MultiCurve) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : AppParCurves_SequenceOfMultiCurve) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : AppParCurves_MultiCurve) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : AppParCurves_SequenceOfMultiCurve) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> AppParCurves_MultiCurve: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : AppParCurves_SequenceOfMultiCurve) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
AppParCurves_CurvaturePoint: OCP.AppParCurves.AppParCurves_Constraint # value = AppParCurves_Constraint.AppParCurves_CurvaturePoint
AppParCurves_NoConstraint: OCP.AppParCurves.AppParCurves_Constraint # value = AppParCurves_Constraint.AppParCurves_NoConstraint
AppParCurves_PassPoint: OCP.AppParCurves.AppParCurves_Constraint # value = AppParCurves_Constraint.AppParCurves_PassPoint
AppParCurves_TangencyPoint: OCP.AppParCurves.AppParCurves_Constraint # value = AppParCurves_Constraint.AppParCurves_TangencyPoint
