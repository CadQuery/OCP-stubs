import OCP.TColGeom2d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.Geom2d
import OCP.Standard
__all__  = [
"TColGeom2d_Array1OfBSplineCurve",
"TColGeom2d_Array1OfBezierCurve",
"TColGeom2d_Array1OfCurve",
"TColGeom2d_HArray1OfBSplineCurve",
"TColGeom2d_HArray1OfBezierCurve",
"TColGeom2d_HArray1OfCurve",
"TColGeom2d_SequenceOfBoundedCurve",
"TColGeom2d_SequenceOfCurve",
"TColGeom2d_HSequenceOfBoundedCurve",
"TColGeom2d_HSequenceOfCurve",
"TColGeom2d_SequenceOfGeometry"
]
class TColGeom2d_Array1OfBSplineCurve():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColGeom2d_Array1OfBSplineCurve) -> TColGeom2d_Array1OfBSplineCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Variable value access
        """
    def First(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
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
    def Last(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
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
    def Move(self,theOther : TColGeom2d_Array1OfBSplineCurve) -> TColGeom2d_Array1OfBSplineCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.Geom2d.Geom2d_BSplineCurve,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColGeom2d_Array1OfBSplineCurve) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TColGeom2d_Array1OfBezierCurve():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColGeom2d_Array1OfBezierCurve) -> TColGeom2d_Array1OfBezierCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Variable value access
        """
    def First(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
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
    def Last(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
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
    def Move(self,theOther : TColGeom2d_Array1OfBezierCurve) -> TColGeom2d_Array1OfBezierCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : OCP.Geom2d.Geom2d_BezierCurve,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColGeom2d_Array1OfBezierCurve) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TColGeom2d_Array1OfCurve():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColGeom2d_Array1OfCurve) -> TColGeom2d_Array1OfCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Variable value access
        """
    def First(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.Geom2d.Geom2d_Curve) -> None: 
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
    def Last(self) -> OCP.Geom2d.Geom2d_Curve: 
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
    def Move(self,theOther : TColGeom2d_Array1OfCurve) -> TColGeom2d_Array1OfCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Curve) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColGeom2d_Array1OfCurve) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.Geom2d.Geom2d_Curve,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TColGeom2d_HArray1OfBSplineCurve(TColGeom2d_Array1OfBSplineCurve, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColGeom2d_Array1OfBSplineCurve: 
        """
        None
        """
    def Assign(self,theOther : TColGeom2d_Array1OfBSplineCurve) -> TColGeom2d_Array1OfBSplineCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColGeom2d_Array1OfBSplineCurve: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_BSplineCurve: 
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
    def First(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
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
    def Init(self,theValue : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
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
    def Last(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
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
    def Move(self,theOther : TColGeom2d_Array1OfBSplineCurve) -> TColGeom2d_Array1OfBSplineCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TColGeom2d_Array1OfBSplineCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.Geom2d.Geom2d_BSplineCurve) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
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
class TColGeom2d_HArray1OfBezierCurve(TColGeom2d_Array1OfBezierCurve, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColGeom2d_Array1OfBezierCurve: 
        """
        None
        """
    def Assign(self,theOther : TColGeom2d_Array1OfBezierCurve) -> TColGeom2d_Array1OfBezierCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColGeom2d_Array1OfBezierCurve: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_BezierCurve: 
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
    def First(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
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
    def Init(self,theValue : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
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
    def Last(self) -> OCP.Geom2d.Geom2d_BezierCurve: 
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
    def Move(self,theOther : TColGeom2d_Array1OfBezierCurve) -> TColGeom2d_Array1OfBezierCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BezierCurve) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.Geom2d.Geom2d_BezierCurve) -> None: ...
    @overload
    def __init__(self,theOther : TColGeom2d_Array1OfBezierCurve) -> None: ...
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
class TColGeom2d_HArray1OfCurve(TColGeom2d_Array1OfCurve, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColGeom2d_Array1OfCurve: 
        """
        None
        """
    def Assign(self,theOther : TColGeom2d_Array1OfCurve) -> TColGeom2d_Array1OfCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColGeom2d_Array1OfCurve: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_Curve: 
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
    def First(self) -> OCP.Geom2d.Geom2d_Curve: 
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
    def Init(self,theValue : OCP.Geom2d.Geom2d_Curve) -> None: 
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
    def Last(self) -> OCP.Geom2d.Geom2d_Curve: 
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
    def Move(self,theOther : TColGeom2d_Array1OfCurve) -> TColGeom2d_Array1OfCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Curve) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColGeom2d_Array1OfCurve) -> None: ...
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
class TColGeom2d_SequenceOfBoundedCurve(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TColGeom2d_SequenceOfBoundedCurve) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: ...
    def Assign(self,theOther : TColGeom2d_SequenceOfBoundedCurve) -> TColGeom2d_SequenceOfBoundedCurve: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_BoundedCurve: 
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
    def First(self) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColGeom2d_SequenceOfBoundedCurve) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColGeom2d_SequenceOfBoundedCurve) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.Geom2d.Geom2d_BoundedCurve: 
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
    def Prepend(self,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColGeom2d_SequenceOfBoundedCurve) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColGeom2d_SequenceOfBoundedCurve) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColGeom2d_SequenceOfBoundedCurve) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TColGeom2d_SequenceOfCurve(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : TColGeom2d_SequenceOfCurve) -> None: ...
    def Assign(self,theOther : TColGeom2d_SequenceOfCurve) -> TColGeom2d_SequenceOfCurve: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_Curve: 
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
    def First(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColGeom2d_SequenceOfCurve) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColGeom2d_SequenceOfCurve) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.Geom2d.Geom2d_Curve: 
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
    def Prepend(self,theItem : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColGeom2d_SequenceOfCurve) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColGeom2d_SequenceOfCurve) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TColGeom2d_SequenceOfCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TColGeom2d_HSequenceOfBoundedCurve(TColGeom2d_SequenceOfBoundedCurve, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : TColGeom2d_SequenceOfBoundedCurve) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: ...
    def Assign(self,theOther : TColGeom2d_SequenceOfBoundedCurve) -> TColGeom2d_SequenceOfBoundedCurve: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TColGeom2d_SequenceOfBoundedCurve: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
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
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        First item access
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
    def InsertAfter(self,theIndex : int,theSeq : TColGeom2d_SequenceOfBoundedCurve) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColGeom2d_SequenceOfBoundedCurve) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> OCP.Geom2d.Geom2d_BoundedCurve: 
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
    def Prepend(self,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColGeom2d_SequenceOfBoundedCurve) -> None: ...
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
    def Sequence(self) -> TColGeom2d_SequenceOfBoundedCurve: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_BoundedCurve) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColGeom2d_SequenceOfBoundedCurve) -> None: 
        """
        Split in two sequences
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TColGeom2d_SequenceOfBoundedCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
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
class TColGeom2d_HSequenceOfCurve(TColGeom2d_SequenceOfCurve, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : TColGeom2d_SequenceOfCurve) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : OCP.Geom2d.Geom2d_Curve) -> None: ...
    def Assign(self,theOther : TColGeom2d_SequenceOfCurve) -> TColGeom2d_SequenceOfCurve: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TColGeom2d_SequenceOfCurve: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
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
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        First item access
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
    def InsertAfter(self,theIndex : int,theSeq : TColGeom2d_SequenceOfCurve) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColGeom2d_SequenceOfCurve) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> OCP.Geom2d.Geom2d_Curve: 
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
    def Prepend(self,theItem : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColGeom2d_SequenceOfCurve) -> None: ...
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
    def Sequence(self) -> TColGeom2d_SequenceOfCurve: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColGeom2d_SequenceOfCurve) -> None: 
        """
        Split in two sequences
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColGeom2d_SequenceOfCurve) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
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
class TColGeom2d_SequenceOfGeometry(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TColGeom2d_SequenceOfGeometry) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OCP.Geom2d.Geom2d_Geometry) -> None: ...
    def Assign(self,theOther : TColGeom2d_SequenceOfGeometry) -> TColGeom2d_SequenceOfGeometry: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.Geom2d.Geom2d_Geometry: 
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
    def First(self) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Geometry) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColGeom2d_SequenceOfGeometry) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColGeom2d_SequenceOfGeometry) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Geometry) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.Geom2d.Geom2d_Geometry: 
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
    def Prepend(self,theSeq : TColGeom2d_SequenceOfGeometry) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.Geom2d.Geom2d_Geometry) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.Geom2d.Geom2d_Geometry) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColGeom2d_SequenceOfGeometry) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TColGeom2d_SequenceOfGeometry) -> None: ...
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
