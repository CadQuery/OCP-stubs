import OCP.TColStd
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TCollection
import OCP.Standard
__all__  = [
"TColStd_Array1OfAsciiString",
"TColStd_Array1OfBoolean",
"TColStd_Array1OfByte",
"TColStd_Array1OfCharacter",
"TColStd_Array1OfExtendedString",
"TColStd_Array1OfInteger",
"TColStd_Array1OfListOfInteger",
"TColStd_Array1OfReal",
"TColStd_Array1OfTransient",
"TColStd_Array2OfBoolean",
"TColStd_Array2OfCharacter",
"TColStd_Array2OfInteger",
"TColStd_Array2OfReal",
"TColStd_Array2OfTransient",
"TColStd_DataMapOfAsciiStringInteger",
"TColStd_DataMapOfIntegerInteger",
"TColStd_DataMapOfIntegerListOfInteger",
"TColStd_DataMapOfIntegerReal",
"TColStd_DataMapOfStringInteger",
"TColStd_HArray1OfAsciiString",
"TColStd_HArray1OfBoolean",
"TColStd_HArray1OfByte",
"TColStd_HArray1OfCharacter",
"TColStd_HArray1OfExtendedString",
"TColStd_HArray1OfInteger",
"TColStd_HArray1OfListOfInteger",
"TColStd_HArray1OfReal",
"TColStd_HArray1OfTransient",
"TColStd_HArray2OfBoolean",
"TColStd_HArray2OfCharacter",
"TColStd_HArray2OfInteger",
"TColStd_HArray2OfReal",
"TColStd_HArray2OfTransient",
"TColStd_HPackedMapOfInteger",
"TColStd_SequenceOfAsciiString",
"TColStd_SequenceOfExtendedString",
"TColStd_SequenceOfHAsciiString",
"TColStd_SequenceOfHExtendedString",
"TColStd_SequenceOfInteger",
"TColStd_SequenceOfReal",
"TColStd_SequenceOfTransient",
"TColStd_IndexedDataMapOfStringString",
"TColStd_IndexedMapOfInteger",
"TColStd_IndexedMapOfReal",
"TColStd_IndexedMapOfTransient",
"TColStd_ListOfAsciiString",
"TColStd_ListOfInteger",
"TColStd_ListOfReal",
"TColStd_ListOfTransient",
"TColStd_MapIntegerHasher",
"TColStd_MapOfAsciiString",
"TColStd_MapOfInteger",
"TColStd_MapOfReal",
"TColStd_MapOfTransient",
"TColStd_MapRealHasher",
"TColStd_MapTransientHasher",
"TColStd_PackedMapOfInteger",
"TColStd_SequenceOfAddress",
"TColStd_HSequenceOfAsciiString",
"TColStd_SequenceOfBoolean",
"TColStd_HSequenceOfExtendedString",
"TColStd_HSequenceOfHAsciiString",
"TColStd_HSequenceOfHExtendedString",
"TColStd_HSequenceOfInteger",
"TColStd_HSequenceOfReal",
"TColStd_HSequenceOfTransient"
]
class TColStd_Array1OfAsciiString():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColStd_Array1OfAsciiString) -> TColStd_Array1OfAsciiString: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Variable value access
        """
    def First(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.TCollection.TCollection_AsciiString) -> None: 
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
    def Last(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def Move(self,theOther : TColStd_Array1OfAsciiString) -> TColStd_Array1OfAsciiString: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfAsciiString) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.TCollection.TCollection_AsciiString,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_Array1OfBoolean():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColStd_Array1OfBoolean) -> TColStd_Array1OfBoolean: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> bool: 
        """
        Returns first element
        """
    def ChangeLast(self) -> bool: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> bool: 
        """
        Variable value access
        """
    def First(self) -> bool: 
        """
        Returns first element
        """
    def Init(self,theValue : bool) -> None: 
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
    def Last(self) -> bool: 
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
    def Move(self,theOther : TColStd_Array1OfBoolean) -> TColStd_Array1OfBoolean: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : bool) -> None: 
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
    def Value(self,theIndex : int) -> bool: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : bool,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfBoolean) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_Array1OfByte():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColStd_Array1OfByte) -> TColStd_Array1OfByte: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> int: 
        """
        Returns first element
        """
    def ChangeLast(self) -> int: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> int: 
        """
        Variable value access
        """
    def First(self) -> int: 
        """
        Returns first element
        """
    def Init(self,theValue : int) -> None: 
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
    def Last(self) -> int: 
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
    def Move(self,theOther : TColStd_Array1OfByte) -> TColStd_Array1OfByte: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : int) -> None: 
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
    def Value(self,theIndex : int) -> int: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : int,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfByte) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_Array1OfCharacter():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColStd_Array1OfCharacter) -> TColStd_Array1OfCharacter: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> str: 
        """
        Returns first element
        """
    def ChangeLast(self) -> str: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> str: 
        """
        Variable value access
        """
    def First(self) -> str: 
        """
        Returns first element
        """
    def Init(self,theValue : str) -> None: 
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
    def Last(self) -> str: 
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
    def Move(self,theOther : TColStd_Array1OfCharacter) -> TColStd_Array1OfCharacter: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : str) -> None: 
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
    def Value(self,theIndex : int) -> str: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TColStd_Array1OfCharacter) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : str,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_Array1OfExtendedString():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColStd_Array1OfExtendedString) -> TColStd_Array1OfExtendedString: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Variable value access
        """
    def First(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.TCollection.TCollection_ExtendedString) -> None: 
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
    def Last(self) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def Move(self,theOther : TColStd_Array1OfExtendedString) -> TColStd_Array1OfExtendedString: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.TCollection.TCollection_ExtendedString,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfExtendedString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_Array1OfInteger():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColStd_Array1OfInteger) -> TColStd_Array1OfInteger: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> int: 
        """
        Returns first element
        """
    def ChangeLast(self) -> int: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> int: 
        """
        Variable value access
        """
    def First(self) -> int: 
        """
        Returns first element
        """
    def Init(self,theValue : int) -> None: 
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
    def Last(self) -> int: 
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
    def Move(self,theOther : TColStd_Array1OfInteger) -> TColStd_Array1OfInteger: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : int) -> None: 
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
    def Value(self,theIndex : int) -> int: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfInteger) -> None: ...
    @overload
    def __init__(self,theBegin : int,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_Array1OfListOfInteger():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColStd_Array1OfListOfInteger) -> TColStd_Array1OfListOfInteger: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> TColStd_ListOfInteger: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TColStd_ListOfInteger: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TColStd_ListOfInteger: 
        """
        Variable value access
        """
    def First(self) -> TColStd_ListOfInteger: 
        """
        Returns first element
        """
    def Init(self,theValue : TColStd_ListOfInteger) -> None: 
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
    def Last(self) -> TColStd_ListOfInteger: 
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
    def Move(self,theOther : TColStd_Array1OfListOfInteger) -> TColStd_Array1OfListOfInteger: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TColStd_ListOfInteger) -> None: 
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
    def Value(self,theIndex : int) -> TColStd_ListOfInteger: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : TColStd_ListOfInteger,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfListOfInteger) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_Array1OfReal():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColStd_Array1OfReal) -> TColStd_Array1OfReal: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
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
        Variable value access
        """
    def First(self) -> float: 
        """
        Returns first element
        """
    def Init(self,theValue : float) -> None: 
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
    def Last(self) -> float: 
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
    def Move(self,theOther : TColStd_Array1OfReal) -> TColStd_Array1OfReal: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : float) -> None: 
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
    def Value(self,theIndex : int) -> float: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : float,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_Array1OfTransient():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TColStd_Array1OfTransient) -> TColStd_Array1OfTransient: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Standard.Standard_Transient: 
        """
        Variable value access
        """
    def First(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.Standard.Standard_Transient) -> None: 
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
    def Last(self) -> OCP.Standard.Standard_Transient: 
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
    def Move(self,theOther : TColStd_Array1OfTransient) -> TColStd_Array1OfTransient: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Standard.Standard_Transient) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Standard.Standard_Transient: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.Standard.Standard_Transient,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfTransient) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_Array2OfBoolean():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : TColStd_Array2OfBoolean) -> TColStd_Array2OfBoolean: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> bool: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : bool) -> None: 
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
    def Move(self,theOther : TColStd_Array2OfBoolean) -> TColStd_Array2OfBoolean: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : bool) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> bool: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array2OfBoolean) -> None: ...
    @overload
    def __init__(self,theBegin : bool,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class TColStd_Array2OfCharacter():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : TColStd_Array2OfCharacter) -> TColStd_Array2OfCharacter: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> str: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : str) -> None: 
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
    def Move(self,theOther : TColStd_Array2OfCharacter) -> TColStd_Array2OfCharacter: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : str) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> str: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TColStd_Array2OfCharacter) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : str,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class TColStd_Array2OfInteger():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : TColStd_Array2OfInteger) -> TColStd_Array2OfInteger: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> int: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : int) -> None: 
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
    def Move(self,theOther : TColStd_Array2OfInteger) -> TColStd_Array2OfInteger: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : int) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> int: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array2OfInteger) -> None: ...
    @overload
    def __init__(self,theBegin : int,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class TColStd_Array2OfReal():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : TColStd_Array2OfReal) -> TColStd_Array2OfReal: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> float: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : float) -> None: 
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
    def Move(self,theOther : TColStd_Array2OfReal) -> TColStd_Array2OfReal: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : float) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> float: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array2OfReal) -> None: ...
    @overload
    def __init__(self,theBegin : float,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class TColStd_Array2OfTransient():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : TColStd_Array2OfTransient) -> TColStd_Array2OfTransient: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> OCP.Standard.Standard_Transient: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : OCP.Standard.Standard_Transient) -> None: 
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
    def Move(self,theOther : TColStd_Array2OfTransient) -> TColStd_Array2OfTransient: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : OCP.Standard.Standard_Transient) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> OCP.Standard.Standard_Transient: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array2OfTransient) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.Standard.Standard_Transient,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class TColStd_DataMapOfAsciiStringInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_DataMapOfAsciiStringInteger) -> TColStd_DataMapOfAsciiStringInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : TColStd_DataMapOfAsciiStringInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString,theValue : int) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString) -> int: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_DataMapOfAsciiStringInteger) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_DataMapOfIntegerInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_DataMapOfIntegerInteger) -> TColStd_DataMapOfIntegerInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> int: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : TColStd_DataMapOfIntegerInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> int: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : int) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> int: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_DataMapOfIntegerInteger) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_DataMapOfIntegerListOfInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_DataMapOfIntegerListOfInteger) -> TColStd_DataMapOfIntegerListOfInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : TColStd_ListOfInteger) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : TColStd_ListOfInteger) -> TColStd_ListOfInteger: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> TColStd_ListOfInteger: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> TColStd_ListOfInteger: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TColStd_DataMapOfIntegerListOfInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> TColStd_ListOfInteger: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : TColStd_ListOfInteger) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> TColStd_ListOfInteger: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_DataMapOfIntegerListOfInteger) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_DataMapOfIntegerReal(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_DataMapOfIntegerReal) -> TColStd_DataMapOfIntegerReal: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : float) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : float) -> float: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> float: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> float: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TColStd_DataMapOfIntegerReal) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : float) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> float: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> float: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_DataMapOfIntegerReal) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_DataMapOfStringInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_DataMapOfStringInteger) -> TColStd_DataMapOfStringInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_ExtendedString,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_ExtendedString,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> int: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TColStd_DataMapOfStringInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_ExtendedString,theValue : int) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> int: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> int: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : TColStd_DataMapOfStringInteger) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_HArray1OfAsciiString(TColStd_Array1OfAsciiString, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColStd_Array1OfAsciiString: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array1OfAsciiString) -> TColStd_Array1OfAsciiString: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColStd_Array1OfAsciiString: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
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
    def First(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def Init(self,theValue : OCP.TCollection.TCollection_AsciiString) -> None: 
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
    def Last(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def Move(self,theOther : TColStd_Array1OfAsciiString) -> TColStd_Array1OfAsciiString: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfAsciiString) -> None: ...
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
class TColStd_HArray1OfBoolean(TColStd_Array1OfBoolean, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColStd_Array1OfBoolean: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array1OfBoolean) -> TColStd_Array1OfBoolean: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColStd_Array1OfBoolean: 
        """
        None
        """
    def ChangeFirst(self) -> bool: 
        """
        Returns first element
        """
    def ChangeLast(self) -> bool: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> bool: 
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
    def First(self) -> bool: 
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
    def Init(self,theValue : bool) -> None: 
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
    def Last(self) -> bool: 
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
    def Move(self,theOther : TColStd_Array1OfBoolean) -> TColStd_Array1OfBoolean: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : bool) -> None: 
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
    def Value(self,theIndex : int) -> bool: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TColStd_Array1OfBoolean) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : bool) -> None: ...
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
class TColStd_HArray1OfByte(TColStd_Array1OfByte, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColStd_Array1OfByte: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array1OfByte) -> TColStd_Array1OfByte: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColStd_Array1OfByte: 
        """
        None
        """
    def ChangeFirst(self) -> int: 
        """
        Returns first element
        """
    def ChangeLast(self) -> int: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> int: 
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
    def First(self) -> int: 
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
    def Init(self,theValue : int) -> None: 
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
    def Last(self) -> int: 
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
    def Move(self,theOther : TColStd_Array1OfByte) -> TColStd_Array1OfByte: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : int) -> None: 
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
    def Value(self,theIndex : int) -> int: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfByte) -> None: ...
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
class TColStd_HArray1OfCharacter(TColStd_Array1OfCharacter, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColStd_Array1OfCharacter: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array1OfCharacter) -> TColStd_Array1OfCharacter: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColStd_Array1OfCharacter: 
        """
        None
        """
    def ChangeFirst(self) -> str: 
        """
        Returns first element
        """
    def ChangeLast(self) -> str: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> str: 
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
    def First(self) -> str: 
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
    def Init(self,theValue : str) -> None: 
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
    def Last(self) -> str: 
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
    def Move(self,theOther : TColStd_Array1OfCharacter) -> TColStd_Array1OfCharacter: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : str) -> None: 
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
    def Value(self,theIndex : int) -> str: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfCharacter) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : str) -> None: ...
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
class TColStd_HArray1OfExtendedString(TColStd_Array1OfExtendedString, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColStd_Array1OfExtendedString: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array1OfExtendedString) -> TColStd_Array1OfExtendedString: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColStd_Array1OfExtendedString: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def First(self) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def Init(self,theValue : OCP.TCollection.TCollection_ExtendedString) -> None: 
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
    def Last(self) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def Move(self,theOther : TColStd_Array1OfExtendedString) -> TColStd_Array1OfExtendedString: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TColStd_Array1OfExtendedString) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.TCollection.TCollection_ExtendedString) -> None: ...
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
class TColStd_HArray1OfInteger(TColStd_Array1OfInteger, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColStd_Array1OfInteger: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array1OfInteger) -> TColStd_Array1OfInteger: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColStd_Array1OfInteger: 
        """
        None
        """
    def ChangeFirst(self) -> int: 
        """
        Returns first element
        """
    def ChangeLast(self) -> int: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> int: 
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
    def First(self) -> int: 
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
    def Init(self,theValue : int) -> None: 
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
    def Last(self) -> int: 
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
    def Move(self,theOther : TColStd_Array1OfInteger) -> TColStd_Array1OfInteger: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : int) -> None: 
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
    def Value(self,theIndex : int) -> int: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfInteger) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : int) -> None: ...
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
class TColStd_HArray1OfListOfInteger(TColStd_Array1OfListOfInteger, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColStd_Array1OfListOfInteger: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array1OfListOfInteger) -> TColStd_Array1OfListOfInteger: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColStd_Array1OfListOfInteger: 
        """
        None
        """
    def ChangeFirst(self) -> TColStd_ListOfInteger: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TColStd_ListOfInteger: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TColStd_ListOfInteger: 
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
    def First(self) -> TColStd_ListOfInteger: 
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
    def Init(self,theValue : TColStd_ListOfInteger) -> None: 
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
    def Last(self) -> TColStd_ListOfInteger: 
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
    def Move(self,theOther : TColStd_Array1OfListOfInteger) -> TColStd_Array1OfListOfInteger: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TColStd_ListOfInteger) -> None: 
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
    def Value(self,theIndex : int) -> TColStd_ListOfInteger: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TColStd_Array1OfListOfInteger) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : TColStd_ListOfInteger) -> None: ...
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
class TColStd_HArray1OfReal(TColStd_Array1OfReal, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColStd_Array1OfReal: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array1OfReal) -> TColStd_Array1OfReal: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColStd_Array1OfReal: 
        """
        None
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
    def First(self) -> float: 
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
    def Init(self,theValue : float) -> None: 
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
    def Last(self) -> float: 
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
    def Move(self,theOther : TColStd_Array1OfReal) -> TColStd_Array1OfReal: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : float) -> None: 
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
    def Value(self,theIndex : int) -> float: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfReal) -> None: ...
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
class TColStd_HArray1OfTransient(TColStd_Array1OfTransient, OCP.Standard.Standard_Transient):
    def Array1(self) -> TColStd_Array1OfTransient: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array1OfTransient) -> TColStd_Array1OfTransient: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TColStd_Array1OfTransient: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Standard.Standard_Transient: 
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
    def First(self) -> OCP.Standard.Standard_Transient: 
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
    def Init(self,theValue : OCP.Standard.Standard_Transient) -> None: 
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
    def Last(self) -> OCP.Standard.Standard_Transient: 
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
    def Move(self,theOther : TColStd_Array1OfTransient) -> TColStd_Array1OfTransient: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Standard.Standard_Transient) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Standard.Standard_Transient: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array1OfTransient) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.Standard.Standard_Transient) -> None: ...
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
class TColStd_HArray2OfBoolean(TColStd_Array2OfBoolean, OCP.Standard.Standard_Transient):
    def Array2(self) -> TColStd_Array2OfBoolean: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array2OfBoolean) -> TColStd_Array2OfBoolean: 
        """
        Assignment
        """
    def ChangeArray2(self) -> TColStd_Array2OfBoolean: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> bool: 
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
    def Init(self,theValue : bool) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
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
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : TColStd_Array2OfBoolean) -> TColStd_Array2OfBoolean: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : bool) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> bool: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TColStd_Array2OfBoolean) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : bool) -> None: ...
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
class TColStd_HArray2OfCharacter(TColStd_Array2OfCharacter, OCP.Standard.Standard_Transient):
    def Array2(self) -> TColStd_Array2OfCharacter: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array2OfCharacter) -> TColStd_Array2OfCharacter: 
        """
        Assignment
        """
    def ChangeArray2(self) -> TColStd_Array2OfCharacter: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> str: 
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
    def Init(self,theValue : str) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
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
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : TColStd_Array2OfCharacter) -> TColStd_Array2OfCharacter: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : str) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> str: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : str) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array2OfCharacter) -> None: ...
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
class TColStd_HArray2OfInteger(TColStd_Array2OfInteger, OCP.Standard.Standard_Transient):
    def Array2(self) -> TColStd_Array2OfInteger: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array2OfInteger) -> TColStd_Array2OfInteger: 
        """
        Assignment
        """
    def ChangeArray2(self) -> TColStd_Array2OfInteger: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> int: 
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
    def Init(self,theValue : int) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
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
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : TColStd_Array2OfInteger) -> TColStd_Array2OfInteger: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : int) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> int: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : int) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_Array2OfInteger) -> None: ...
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
class TColStd_HArray2OfReal(TColStd_Array2OfReal, OCP.Standard.Standard_Transient):
    def Array2(self) -> TColStd_Array2OfReal: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array2OfReal) -> TColStd_Array2OfReal: 
        """
        Assignment
        """
    def ChangeArray2(self) -> TColStd_Array2OfReal: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> float: 
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
    def Init(self,theValue : float) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
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
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : TColStd_Array2OfReal) -> TColStd_Array2OfReal: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : float) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> float: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TColStd_Array2OfReal) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : float) -> None: ...
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
class TColStd_HArray2OfTransient(TColStd_Array2OfTransient, OCP.Standard.Standard_Transient):
    def Array2(self) -> TColStd_Array2OfTransient: 
        """
        None
        """
    def Assign(self,theOther : TColStd_Array2OfTransient) -> TColStd_Array2OfTransient: 
        """
        Assignment
        """
    def ChangeArray2(self) -> TColStd_Array2OfTransient: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> OCP.Standard.Standard_Transient: 
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
    def Init(self,theValue : OCP.Standard.Standard_Transient) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
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
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : TColStd_Array2OfTransient) -> TColStd_Array2OfTransient: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : OCP.Standard.Standard_Transient) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> OCP.Standard.Standard_Transient: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TColStd_Array2OfTransient) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : OCP.Standard.Standard_Transient) -> None: ...
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
class TColStd_HPackedMapOfInteger(OCP.Standard.Standard_Transient):
    """
    Extension of TColStd_PackedMapOfInteger class to be manipulated by handle.Extension of TColStd_PackedMapOfInteger class to be manipulated by handle.Extension of TColStd_PackedMapOfInteger class to be manipulated by handle.
    """
    def ChangeMap(self) -> TColStd_PackedMapOfInteger: 
        """
        Access to the map for modification

        Access to the map for modification
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
    def Map(self) -> TColStd_PackedMapOfInteger: 
        """
        Access to the map

        Access to the map
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOther : TColStd_PackedMapOfInteger) -> None: ...
    @overload
    def __init__(self,NbBuckets : int=1) -> None: ...
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
class TColStd_SequenceOfAsciiString(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : TColStd_SequenceOfAsciiString) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfAsciiString) -> TColStd_SequenceOfAsciiString: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
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
    def First(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfAsciiString) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfAsciiString) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def Prepend(self,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColStd_SequenceOfAsciiString) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfAsciiString) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfAsciiString) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TColStd_SequenceOfExtendedString(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : TColStd_SequenceOfExtendedString) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfExtendedString) -> TColStd_SequenceOfExtendedString: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def First(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfExtendedString) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfExtendedString) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def Prepend(self,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColStd_SequenceOfExtendedString) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfExtendedString) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfExtendedString) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TColStd_SequenceOfHAsciiString(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TColStd_SequenceOfHAsciiString) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfHAsciiString) -> TColStd_SequenceOfHAsciiString: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def First(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfHAsciiString) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfHAsciiString) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Prepend(self,theSeq : TColStd_SequenceOfHAsciiString) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfHAsciiString) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TColStd_SequenceOfHAsciiString) -> None: ...
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
class TColStd_SequenceOfHExtendedString(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TColStd_SequenceOfHExtendedString) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfHExtendedString) -> TColStd_SequenceOfHExtendedString: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_HExtendedString: 
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
    def First(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfHExtendedString) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfHExtendedString) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TCollection.TCollection_HExtendedString: 
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
    def Prepend(self,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColStd_SequenceOfHExtendedString) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfHExtendedString) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfHExtendedString) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TColStd_SequenceOfInteger(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : int) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : TColStd_SequenceOfInteger) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfInteger) -> TColStd_SequenceOfInteger: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> int: 
        """
        First item access
        """
    def ChangeLast(self) -> int: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> int: 
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
    def First(self) -> int: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfInteger) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : int) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : int) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfInteger) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> int: 
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
    def Prepend(self,theSeq : TColStd_SequenceOfInteger) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : int) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : int) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfInteger) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> int: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfInteger) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TColStd_SequenceOfReal(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TColStd_SequenceOfReal) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : float) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfReal) -> TColStd_SequenceOfReal: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> float: 
        """
        First item access
        """
    def ChangeLast(self) -> float: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> float: 
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
    def First(self) -> float: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfReal) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : float) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : float) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfReal) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> float: 
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
    def Prepend(self,theSeq : TColStd_SequenceOfReal) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : float) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : float) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfReal) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> float: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TColStd_SequenceOfReal) -> None: ...
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
class TColStd_SequenceOfTransient(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TColStd_SequenceOfTransient) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OCP.Standard.Standard_Transient) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfTransient) -> TColStd_SequenceOfTransient: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Standard.Standard_Transient: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Standard.Standard_Transient: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.Standard.Standard_Transient: 
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
    def First(self) -> OCP.Standard.Standard_Transient: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfTransient) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Standard.Standard_Transient) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Standard.Standard_Transient) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfTransient) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.Standard.Standard_Transient: 
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
    def Prepend(self,theSeq : TColStd_SequenceOfTransient) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.Standard.Standard_Transient) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.Standard.Standard_Transient) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfTransient) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Standard.Standard_Transient: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfTransient) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TColStd_IndexedDataMapOfStringString(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TCollection.TCollection_AsciiString,theItem : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_IndexedDataMapOfStringString) -> TColStd_IndexedDataMapOfStringString: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TColStd_IndexedDataMapOfStringString) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TCollection.TCollection_AsciiString,theValue : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    def FindIndex(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TCollection.TCollection_AsciiString,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theOther : TColStd_IndexedDataMapOfStringString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_IndexedMapOfInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : int) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_IndexedMapOfInteger) -> TColStd_IndexedMapOfInteger: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : int) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TColStd_IndexedMapOfInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : int) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> int: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,theExtent : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : int) -> bool: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : int) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_IndexedMapOfInteger) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TColStd_IndexedMapOfReal(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : float) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_IndexedMapOfReal) -> TColStd_IndexedMapOfReal: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : float) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TColStd_IndexedMapOfReal) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : float) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> float: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,theExtent : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : float) -> bool: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : float) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_IndexedMapOfReal) -> None: ...
    pass
class TColStd_IndexedMapOfTransient(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : OCP.Standard.Standard_Transient) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_IndexedMapOfTransient) -> TColStd_IndexedMapOfTransient: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : OCP.Standard.Standard_Transient) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TColStd_IndexedMapOfTransient) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : OCP.Standard.Standard_Transient) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.Standard.Standard_Transient: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,theExtent : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.Standard.Standard_Transient) -> bool: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.Standard.Standard_Transient) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theOther : TColStd_IndexedMapOfTransient) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class TColStd_ListOfAsciiString(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : TColStd_ListOfAsciiString) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_AsciiString,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    def Assign(self,theOther : TColStd_ListOfAsciiString) -> TColStd_ListOfAsciiString: 
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
    def First(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TColStd_ListOfAsciiString,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OCP.TCollection.TCollection_AsciiString,theIter : Any) -> OCP.TCollection.TCollection_AsciiString: ...
    @overload
    def InsertBefore(self,theItem : OCP.TCollection.TCollection_AsciiString,theIter : Any) -> OCP.TCollection.TCollection_AsciiString: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TColStd_ListOfAsciiString,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TColStd_ListOfAsciiString) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_ListOfAsciiString) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_ListOfInteger(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : int,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : int) -> int: ...
    @overload
    def Append(self,theOther : TColStd_ListOfInteger) -> None: ...
    def Assign(self,theOther : TColStd_ListOfInteger) -> TColStd_ListOfInteger: 
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
    def First(self) -> int: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TColStd_ListOfInteger,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : int,theIter : Any) -> int: ...
    @overload
    def InsertBefore(self,theItem : int,theIter : Any) -> int: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TColStd_ListOfInteger,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> int: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : int) -> int: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TColStd_ListOfInteger) -> None: ...
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
    def __init__(self,theOther : TColStd_ListOfInteger) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_ListOfReal(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : float,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TColStd_ListOfReal) -> None: ...
    @overload
    def Append(self,theItem : float) -> float: ...
    def Assign(self,theOther : TColStd_ListOfReal) -> TColStd_ListOfReal: 
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
    def First(self) -> float: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : float,theIter : Any) -> float: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TColStd_ListOfReal,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : float,theIter : Any) -> float: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TColStd_ListOfReal,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> float: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TColStd_ListOfReal) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : float) -> float: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_ListOfReal) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_ListOfTransient(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.Standard.Standard_Transient,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TColStd_ListOfTransient) -> None: ...
    @overload
    def Append(self,theItem : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: ...
    def Assign(self,theOther : TColStd_ListOfTransient) -> TColStd_ListOfTransient: 
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
    def First(self) -> OCP.Standard.Standard_Transient: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.Standard.Standard_Transient,theIter : Any) -> OCP.Standard.Standard_Transient: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TColStd_ListOfTransient,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : TColStd_ListOfTransient,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : OCP.Standard.Standard_Transient,theIter : Any) -> OCP.Standard.Standard_Transient: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.Standard.Standard_Transient: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TColStd_ListOfTransient) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: ...
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
    def __init__(self,theOther : TColStd_ListOfTransient) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TColStd_MapIntegerHasher():
    """
    Purpose: The DefaultHasher is a Hasher that is used by default in NCollection maps. To compute the hash code of the key is used the global function HashCode. To compare two keys is used the global function IsEqual.
    """
    @staticmethod
    def HashCode_s(theKey : int,theUpperBound : int) -> int: 
        """
        Returns hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theKey1 : int,theKey2 : int) -> bool: 
        """
        None
        """
    pass
class TColStd_MapOfAsciiString(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Add
        """
    def Added(self,K : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_MapOfAsciiString) -> TColStd_MapOfAsciiString: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,K : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : TColStd_MapOfAsciiString) -> bool: ...
    def Differ(self,theOther : TColStd_MapOfAsciiString) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TColStd_MapOfAsciiString,theRight : TColStd_MapOfAsciiString) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TColStd_MapOfAsciiString) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TColStd_MapOfAsciiString) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TColStd_MapOfAsciiString) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TColStd_MapOfAsciiString,theRight : TColStd_MapOfAsciiString) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TColStd_MapOfAsciiString) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TColStd_MapOfAsciiString) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TColStd_MapOfAsciiString,theRight : TColStd_MapOfAsciiString) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TColStd_MapOfAsciiString,theRight : TColStd_MapOfAsciiString) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TColStd_MapOfAsciiString) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_MapOfAsciiString) -> None: ...
    pass
class TColStd_MapOfInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : int) -> bool: 
        """
        Add
        """
    def Added(self,K : int) -> int: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_MapOfInteger) -> TColStd_MapOfInteger: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,K : int) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : TColStd_MapOfInteger) -> bool: ...
    def Differ(self,theOther : TColStd_MapOfInteger) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TColStd_MapOfInteger,theRight : TColStd_MapOfInteger) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TColStd_MapOfInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TColStd_MapOfInteger) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TColStd_MapOfInteger) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TColStd_MapOfInteger,theRight : TColStd_MapOfInteger) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TColStd_MapOfInteger) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : int) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TColStd_MapOfInteger) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TColStd_MapOfInteger,theRight : TColStd_MapOfInteger) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TColStd_MapOfInteger,theRight : TColStd_MapOfInteger) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TColStd_MapOfInteger) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_MapOfInteger) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class TColStd_MapOfReal(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : float) -> bool: 
        """
        Add
        """
    def Added(self,K : float) -> float: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_MapOfReal) -> TColStd_MapOfReal: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def Contains(self,K : float) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : TColStd_MapOfReal) -> bool: ...
    def Differ(self,theOther : TColStd_MapOfReal) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TColStd_MapOfReal,theRight : TColStd_MapOfReal) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TColStd_MapOfReal) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TColStd_MapOfReal) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TColStd_MapOfReal) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TColStd_MapOfReal,theRight : TColStd_MapOfReal) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TColStd_MapOfReal) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : float) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TColStd_MapOfReal) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TColStd_MapOfReal,theRight : TColStd_MapOfReal) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TColStd_MapOfReal,theRight : TColStd_MapOfReal) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TColStd_MapOfReal) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theOther : TColStd_MapOfReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class TColStd_MapOfTransient(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : OCP.Standard.Standard_Transient) -> bool: 
        """
        Add
        """
    def Added(self,K : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TColStd_MapOfTransient) -> TColStd_MapOfTransient: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,K : OCP.Standard.Standard_Transient) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : TColStd_MapOfTransient) -> bool: ...
    def Differ(self,theOther : TColStd_MapOfTransient) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TColStd_MapOfTransient,theRight : TColStd_MapOfTransient) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TColStd_MapOfTransient) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TColStd_MapOfTransient) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TColStd_MapOfTransient) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TColStd_MapOfTransient,theRight : TColStd_MapOfTransient) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TColStd_MapOfTransient) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : OCP.Standard.Standard_Transient) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TColStd_MapOfTransient) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TColStd_MapOfTransient,theRight : TColStd_MapOfTransient) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TColStd_MapOfTransient,theRight : TColStd_MapOfTransient) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TColStd_MapOfTransient) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_MapOfTransient) -> None: ...
    pass
class TColStd_MapRealHasher():
    """
    Purpose: The DefaultHasher is a Hasher that is used by default in NCollection maps. To compute the hash code of the key is used the global function HashCode. To compare two keys is used the global function IsEqual.
    """
    @staticmethod
    def HashCode_s(theKey : float,theUpperBound : int) -> int: 
        """
        Returns hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theKey1 : float,theKey2 : float) -> bool: 
        """
        None
        """
    pass
class TColStd_MapTransientHasher():
    """
    Purpose: The DefaultHasher is a Hasher that is used by default in NCollection maps. To compute the hash code of the key is used the global function HashCode. To compare two keys is used the global function IsEqual.
    """
    @staticmethod
    def HashCode_s(theKey : OCP.Standard.Standard_Transient,theUpperBound : int) -> int: 
        """
        Returns hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theKey1 : OCP.Standard.Standard_Transient,theKey2 : OCP.Standard.Standard_Transient) -> bool: 
        """
        None
        """
    pass
class TColStd_PackedMapOfInteger():
    """
    Optimized Map of integer values. Each block of 32 integers is stored in 8 bytes in memory.
    """
    def Add(self,aKey : int) -> bool: 
        """
        None
        """
    def Assign(self,arg1 : TColStd_PackedMapOfInteger) -> TColStd_PackedMapOfInteger: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def Contains(self,aKey : int) -> bool: 
        """
        None
        """
    def Differ(self,arg1 : TColStd_PackedMapOfInteger) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference().
        """
    def Difference(self,arg1 : TColStd_PackedMapOfInteger,arg2 : TColStd_PackedMapOfInteger) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous contents of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Extent(self) -> int: 
        """
        None
        """
    def GetMaximalMapped(self) -> int: 
        """
        Query the maximal contained key value.
        """
    def GetMinimalMapped(self) -> int: 
        """
        Query the minimal contained key value.
        """
    def HasIntersection(self,arg1 : TColStd_PackedMapOfInteger) -> bool: 
        """
        Returns True if this map has common items with the given one.
        """
    def Intersect(self,arg1 : TColStd_PackedMapOfInteger) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection().
        """
    def Intersection(self,arg1 : TColStd_PackedMapOfInteger,arg2 : TColStd_PackedMapOfInteger) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous contents of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands. The order of operands makes no difference; the method minimizes internally the number of iterations using the smallest map for the loop.
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def IsEqual(self,arg1 : TColStd_PackedMapOfInteger) -> bool: 
        """
        Returns True if this map is equal to the given one, i.e. they contain the same sets of elements
        """
    def IsSubset(self,arg1 : TColStd_PackedMapOfInteger) -> bool: 
        """
        Returns True if this map is subset of the given one, i.e. all elements contained in this map is contained also in the operand map. if this map is empty that this method returns true for any operand map.
        """
    def NbBuckets(self) -> int: 
        """
        None
        """
    def ReSize(self,NbBuckets : int) -> None: 
        """
        None
        """
    def Remove(self,aKey : int) -> bool: 
        """
        None
        """
    def Statistics(self,outStream : Any) -> None: 
        """
        None
        """
    def Subtract(self,arg1 : TColStd_PackedMapOfInteger) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands.
        """
    def Subtraction(self,arg1 : TColStd_PackedMapOfInteger,arg2 : TColStd_PackedMapOfInteger) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous contents of this Map is cleared. This map (result of the boolean operation) can also be used as the first operand.
        """
    def Union(self,arg1 : TColStd_PackedMapOfInteger,arg2 : TColStd_PackedMapOfInteger) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps. The new Map contains the values that are contained either in the first map or in the second map or in both. All previous contents of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,arg1 : TColStd_PackedMapOfInteger) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union().
        """
    @overload
    def __init__(self,NbBuckets : int=1) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_PackedMapOfInteger) -> None: ...
    def __ipow__(self,MM : TColStd_PackedMapOfInteger) -> TColStd_PackedMapOfInteger: 
        """
        Overloaded operator version of Differ().
        """
    def __isub__(self,MM : TColStd_PackedMapOfInteger) -> TColStd_PackedMapOfInteger: 
        """
        Overloaded operator version of Subtract().
        """
    pass
class TColStd_SequenceOfAddress(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TColStd_SequenceOfAddress) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : capsule) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfAddress) -> TColStd_SequenceOfAddress: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> capsule: 
        """
        First item access
        """
    def ChangeLast(self) -> capsule: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> capsule: 
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
    def First(self) -> capsule: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : capsule) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfAddress) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfAddress) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : capsule) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> capsule: 
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
    def Prepend(self,theItem : capsule) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColStd_SequenceOfAddress) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : capsule) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfAddress) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> capsule: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfAddress) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TColStd_HSequenceOfAsciiString(TColStd_SequenceOfAsciiString, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : TColStd_SequenceOfAsciiString) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_AsciiString) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfAsciiString) -> TColStd_SequenceOfAsciiString: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TColStd_SequenceOfAsciiString: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
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
    def First(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfAsciiString) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfAsciiString) -> None: ...
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
    def Last(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def Prepend(self,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColStd_SequenceOfAsciiString) -> None: ...
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
    def Sequence(self) -> TColStd_SequenceOfAsciiString: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfAsciiString) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TColStd_SequenceOfAsciiString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class TColStd_SequenceOfBoolean(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : bool) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : TColStd_SequenceOfBoolean) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfBoolean) -> TColStd_SequenceOfBoolean: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> bool: 
        """
        First item access
        """
    def ChangeLast(self) -> bool: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> bool: 
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
    def First(self) -> bool: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : bool) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfBoolean) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfBoolean) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : bool) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> bool: 
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
    def Prepend(self,theItem : bool) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColStd_SequenceOfBoolean) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : bool) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfBoolean) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> bool: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfBoolean) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TColStd_HSequenceOfExtendedString(TColStd_SequenceOfExtendedString, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : TColStd_SequenceOfExtendedString) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfExtendedString) -> TColStd_SequenceOfExtendedString: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TColStd_SequenceOfExtendedString: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def First(self) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def InsertAfter(self,theIndex : int,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfExtendedString) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfExtendedString) -> None: ...
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
    def Last(self) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def Prepend(self,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColStd_SequenceOfExtendedString) -> None: ...
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
    def Sequence(self) -> TColStd_SequenceOfExtendedString: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfExtendedString) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TColStd_SequenceOfExtendedString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class TColStd_HSequenceOfHAsciiString(TColStd_SequenceOfHAsciiString, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : TColStd_SequenceOfHAsciiString) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfHAsciiString) -> TColStd_SequenceOfHAsciiString: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TColStd_SequenceOfHAsciiString: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def First(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def InsertAfter(self,theIndex : int,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfHAsciiString) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfHAsciiString) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: ...
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
    def Last(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Prepend(self,theSeq : TColStd_SequenceOfHAsciiString) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: ...
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
    def Sequence(self) -> TColStd_SequenceOfHAsciiString: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfHAsciiString) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TColStd_SequenceOfHAsciiString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class TColStd_HSequenceOfHExtendedString(TColStd_SequenceOfHExtendedString, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : TColStd_SequenceOfHExtendedString) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfHExtendedString) -> TColStd_SequenceOfHExtendedString: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TColStd_SequenceOfHExtendedString: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_HExtendedString: 
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
    def First(self) -> OCP.TCollection.TCollection_HExtendedString: 
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
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfHExtendedString) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfHExtendedString) -> None: ...
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
    def Last(self) -> OCP.TCollection.TCollection_HExtendedString: 
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
    def Prepend(self,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TColStd_SequenceOfHExtendedString) -> None: ...
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
    def Sequence(self) -> TColStd_SequenceOfHExtendedString: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_HExtendedString) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfHExtendedString) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfHExtendedString) -> None: ...
    def __iter__(self) -> iterator: ...
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
class TColStd_HSequenceOfInteger(TColStd_SequenceOfInteger, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : int) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : TColStd_SequenceOfInteger) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfInteger) -> TColStd_SequenceOfInteger: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> int: 
        """
        First item access
        """
    def ChangeLast(self) -> int: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TColStd_SequenceOfInteger: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> int: 
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
    def First(self) -> int: 
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
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfInteger) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : int) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : int) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfInteger) -> None: ...
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
    def Last(self) -> int: 
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
    def Prepend(self,theSeq : TColStd_SequenceOfInteger) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : int) -> None: ...
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
    def Sequence(self) -> TColStd_SequenceOfInteger: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : int) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfInteger) -> None: 
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
    def Value(self,theIndex : int) -> int: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfInteger) -> None: ...
    def __iter__(self) -> iterator: ...
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
class TColStd_HSequenceOfReal(TColStd_SequenceOfReal, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : TColStd_SequenceOfReal) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : float) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfReal) -> TColStd_SequenceOfReal: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> float: 
        """
        First item access
        """
    def ChangeLast(self) -> float: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TColStd_SequenceOfReal: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> float: 
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
    def First(self) -> float: 
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
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfReal) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : float) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : float) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfReal) -> None: ...
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
    def Last(self) -> float: 
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
    def Prepend(self,theSeq : TColStd_SequenceOfReal) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : float) -> None: ...
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
    def Sequence(self) -> TColStd_SequenceOfReal: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : float) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfReal) -> None: 
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
    def Value(self,theIndex : int) -> float: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TColStd_SequenceOfReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class TColStd_HSequenceOfTransient(TColStd_SequenceOfTransient, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : TColStd_SequenceOfTransient) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : OCP.Standard.Standard_Transient) -> None: ...
    def Assign(self,theOther : TColStd_SequenceOfTransient) -> TColStd_SequenceOfTransient: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Standard.Standard_Transient: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Standard.Standard_Transient: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TColStd_SequenceOfTransient: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.Standard.Standard_Transient: 
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
    def First(self) -> OCP.Standard.Standard_Transient: 
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
    def InsertAfter(self,theIndex : int,theSeq : TColStd_SequenceOfTransient) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Standard.Standard_Transient) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Standard.Standard_Transient) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TColStd_SequenceOfTransient) -> None: ...
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
    def Last(self) -> OCP.Standard.Standard_Transient: 
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
    def Prepend(self,theSeq : TColStd_SequenceOfTransient) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.Standard.Standard_Transient) -> None: ...
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
    def Sequence(self) -> TColStd_SequenceOfTransient: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.Standard.Standard_Transient) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TColStd_SequenceOfTransient) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Standard.Standard_Transient: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TColStd_SequenceOfTransient) -> None: ...
    def __iter__(self) -> iterator: ...
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
