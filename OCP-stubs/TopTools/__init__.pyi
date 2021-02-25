import OCP.TopTools
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.TCollection
import io
import OCP.NCollection
import OCP.TopoDS
import OCP.Bnd
import OCP.TopLoc
import OCP.Standard
import OCP.TopAbs
__all__  = [
"TopTools",
"TopTools_Array1OfListOfShape",
"TopTools_Array1OfShape",
"TopTools_Array2OfShape",
"TopTools_DataMapOfIntegerListOfShape",
"TopTools_DataMapOfIntegerShape",
"TopTools_DataMapOfOrientedShapeInteger",
"TopTools_DataMapOfOrientedShapeShape",
"TopTools_DataMapOfShapeBox",
"TopTools_DataMapOfShapeInteger",
"TopTools_DataMapOfShapeListOfInteger",
"TopTools_DataMapOfShapeListOfShape",
"TopTools_DataMapOfShapeReal",
"TopTools_DataMapOfShapeSequenceOfShape",
"TopTools_DataMapOfShapeShape",
"TopTools_HArray1OfListOfShape",
"TopTools_HArray1OfShape",
"TopTools_HArray2OfShape",
"TopTools_SequenceOfShape",
"TopTools_IndexedDataMapOfShapeAddress",
"TopTools_IndexedDataMapOfShapeListOfShape",
"TopTools_IndexedDataMapOfShapeReal",
"TopTools_IndexedDataMapOfShapeShape",
"TopTools_IndexedMapOfOrientedShape",
"TopTools_IndexedMapOfShape",
"TopTools_ListOfListOfShape",
"TopTools_ListOfShape",
"TopTools_LocationSet",
"TopTools_MapOfOrientedShape",
"TopTools_MapOfShape",
"TopTools_MutexForShapeProvider",
"TopTools_OrientedShapeMapHasher",
"TopTools_HSequenceOfShape",
"TopTools_ShapeMapHasher",
"TopTools_ShapeSet"
]
class TopTools():
    """
    The TopTools package provides utilities for the topological data structure.
    """
    @staticmethod
    def Dummy_s(I : int) -> None: 
        """
        This is to bypass an extraction bug. It will force the inclusion of Standard_Integer.hxx itself including Standard_OStream.hxx at the correct position.
        """
    @staticmethod
    def Dump_s(Sh : OCP.TopoDS.TopoDS_Shape,S : io.BytesIO) -> None: 
        """
        A set of Shapes. Can be dump, wrote or read. Dumps the topological structure of <Sh> on the stream <S>.
        """
    def __init__(self) -> None: ...
    pass
class TopTools_Array1OfListOfShape():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TopTools_Array1OfListOfShape) -> TopTools_Array1OfListOfShape: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> TopTools_ListOfShape: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TopTools_ListOfShape: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TopTools_ListOfShape: 
        """
        Variable value access
        """
    def First(self) -> TopTools_ListOfShape: 
        """
        Returns first element
        """
    def Init(self,theValue : TopTools_ListOfShape) -> None: 
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
    def Last(self) -> TopTools_ListOfShape: 
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
    def Move(self,theOther : TopTools_Array1OfListOfShape) -> TopTools_Array1OfListOfShape: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TopTools_ListOfShape) -> None: 
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
    def Value(self,theIndex : int) -> TopTools_ListOfShape: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_Array1OfListOfShape) -> None: ...
    @overload
    def __init__(self,theBegin : TopTools_ListOfShape,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_Array1OfShape():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TopTools_Array1OfShape) -> TopTools_Array1OfShape: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Variable value access
        """
    def First(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def Last(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Move(self,theOther : TopTools_Array1OfShape) -> TopTools_Array1OfShape: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_Array1OfShape) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.TopoDS.TopoDS_Shape,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_Array2OfShape():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : TopTools_Array2OfShape) -> TopTools_Array2OfShape: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def Move(self,theOther : TopTools_Array2OfShape) -> TopTools_Array2OfShape: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : OCP.TopoDS.TopoDS_Shape,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_Array2OfShape) -> None: ...
    pass
class TopTools_DataMapOfIntegerListOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfIntegerListOfShape) -> TopTools_DataMapOfIntegerListOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : TopTools_ListOfShape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : TopTools_ListOfShape) -> TopTools_ListOfShape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> TopTools_ListOfShape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> TopTools_ListOfShape: 
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
    def Exchange(self,theOther : TopTools_DataMapOfIntegerListOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : TopTools_ListOfShape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> TopTools_ListOfShape: ...
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
    def Seek(self,theKey : int) -> TopTools_ListOfShape: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
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
    def __init__(self,theOther : TopTools_DataMapOfIntegerListOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfIntegerShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfIntegerShape) -> TopTools_DataMapOfIntegerShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Exchange(self,theOther : TopTools_DataMapOfIntegerShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> OCP.TopoDS.TopoDS_Shape: ...
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
    def Seek(self,theKey : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
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
    def __init__(self,theOther : TopTools_DataMapOfIntegerShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfOrientedShapeInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfOrientedShapeInteger) -> TopTools_DataMapOfOrientedShapeInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> int: 
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
    def Exchange(self,theOther : TopTools_DataMapOfOrientedShapeInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : int) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> int: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_DataMapOfOrientedShapeInteger) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfOrientedShapeShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfOrientedShapeShape) -> TopTools_DataMapOfOrientedShapeShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Exchange(self,theOther : TopTools_DataMapOfOrientedShapeShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_DataMapOfOrientedShapeShape) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfShapeBox(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfShapeBox) -> TopTools_DataMapOfShapeBox: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Bnd.Bnd_Box) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Bnd.Bnd_Box) -> OCP.Bnd.Bnd_Box: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: 
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
    def Exchange(self,theOther : TopTools_DataMapOfShapeBox) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.Bnd.Bnd_Box) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_DataMapOfShapeBox) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfShapeInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfShapeInteger) -> TopTools_DataMapOfShapeInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> int: 
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
    def Exchange(self,theOther : TopTools_DataMapOfShapeInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : int) -> bool: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_DataMapOfShapeInteger) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfShapeListOfInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfShapeListOfInteger) -> TopTools_DataMapOfShapeListOfInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColStd.TColStd_ListOfInteger) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColStd.TColStd_ListOfInteger) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_ListOfInteger: 
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
    def Exchange(self,theOther : TopTools_DataMapOfShapeListOfInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TColStd.TColStd_ListOfInteger) -> bool: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_DataMapOfShapeListOfInteger) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfShapeListOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfShapeListOfShape) -> TopTools_DataMapOfShapeListOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopTools_ListOfShape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopTools_ListOfShape) -> TopTools_ListOfShape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopTools_ListOfShape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopTools_ListOfShape: 
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
    def Exchange(self,theOther : TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : TopTools_ListOfShape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopTools_ListOfShape: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopTools_ListOfShape: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_DataMapOfShapeListOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfShapeReal(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfShapeReal) -> TopTools_DataMapOfShapeReal: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : float) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : float) -> float: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> float: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> float: 
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
    def Exchange(self,theOther : TopTools_DataMapOfShapeReal) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : float) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> float: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> float: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : TopTools_DataMapOfShapeReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfShapeSequenceOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfShapeSequenceOfShape) -> TopTools_DataMapOfShapeSequenceOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopTools_SequenceOfShape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopTools_SequenceOfShape) -> TopTools_SequenceOfShape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopTools_SequenceOfShape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopTools_SequenceOfShape: 
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
    def Exchange(self,theOther : TopTools_DataMapOfShapeSequenceOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : TopTools_SequenceOfShape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopTools_SequenceOfShape: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopTools_SequenceOfShape: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_DataMapOfShapeSequenceOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_DataMapOfShapeShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_DataMapOfShapeShape) -> TopTools_DataMapOfShapeShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Exchange(self,theOther : TopTools_DataMapOfShapeShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_DataMapOfShapeShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_HArray1OfListOfShape(TopTools_Array1OfListOfShape, OCP.Standard.Standard_Transient):
    def Array1(self) -> TopTools_Array1OfListOfShape: 
        """
        None
        """
    def Assign(self,theOther : TopTools_Array1OfListOfShape) -> TopTools_Array1OfListOfShape: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TopTools_Array1OfListOfShape: 
        """
        None
        """
    def ChangeFirst(self) -> TopTools_ListOfShape: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TopTools_ListOfShape: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TopTools_ListOfShape: 
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
    def First(self) -> TopTools_ListOfShape: 
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
    def Init(self,theValue : TopTools_ListOfShape) -> None: 
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
    def Last(self) -> TopTools_ListOfShape: 
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
    def Move(self,theOther : TopTools_Array1OfListOfShape) -> TopTools_Array1OfListOfShape: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TopTools_ListOfShape) -> None: 
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
    def Value(self,theIndex : int) -> TopTools_ListOfShape: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TopTools_Array1OfListOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : TopTools_ListOfShape) -> None: ...
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
class TopTools_HArray1OfShape(TopTools_Array1OfShape, OCP.Standard.Standard_Transient):
    def Array1(self) -> TopTools_Array1OfShape: 
        """
        None
        """
    def Assign(self,theOther : TopTools_Array1OfShape) -> TopTools_Array1OfShape: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TopTools_Array1OfShape: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def First(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Init(self,theValue : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def Last(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Move(self,theOther : TopTools_Array1OfShape) -> TopTools_Array1OfShape: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_Array1OfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class TopTools_HArray2OfShape(TopTools_Array2OfShape, OCP.Standard.Standard_Transient):
    def Array2(self) -> TopTools_Array2OfShape: 
        """
        None
        """
    def Assign(self,theOther : TopTools_Array2OfShape) -> TopTools_Array2OfShape: 
        """
        Assignment
        """
    def ChangeArray2(self) -> TopTools_Array2OfShape: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Init(self,theValue : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def Move(self,theOther : TopTools_Array2OfShape) -> TopTools_Array2OfShape: 
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
    def SetValue(self,theRow : int,theCol : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_Array2OfShape) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class TopTools_SequenceOfShape(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : TopTools_SequenceOfShape) -> None: ...
    def Assign(self,theOther : TopTools_SequenceOfShape) -> TopTools_SequenceOfShape: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def First(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TopTools_SequenceOfShape) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TopTools_SequenceOfShape) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Prepend(self,theSeq : TopTools_SequenceOfShape) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TopTools_SequenceOfShape) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TopTools_SequenceOfShape) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TopTools_IndexedDataMapOfShapeAddress(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : capsule) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_IndexedDataMapOfShapeAddress) -> TopTools_IndexedDataMapOfShapeAddress: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> capsule: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> capsule: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> capsule: 
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
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopTools_IndexedDataMapOfShapeAddress) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> capsule: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> capsule: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : capsule) -> bool: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> capsule: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : capsule) -> None: 
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
    def __init__(self,theOther : TopTools_IndexedDataMapOfShapeAddress) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_IndexedDataMapOfShapeListOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopTools_ListOfShape) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_IndexedDataMapOfShapeListOfShape) -> TopTools_IndexedDataMapOfShapeListOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> TopTools_ListOfShape: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopTools_ListOfShape: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopTools_ListOfShape: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopTools_IndexedDataMapOfShapeListOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> TopTools_ListOfShape: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopTools_ListOfShape: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : TopTools_ListOfShape) -> bool: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopTools_ListOfShape: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopTools_ListOfShape) -> None: 
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
    def __init__(self,theOther : TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_IndexedDataMapOfShapeReal(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : float) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_IndexedDataMapOfShapeReal) -> TopTools_IndexedDataMapOfShapeReal: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> float: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> float: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> float: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopTools_IndexedDataMapOfShapeReal) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> float: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : float) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> float: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> float: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : float) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theOther : TopTools_IndexedDataMapOfShapeReal) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_IndexedDataMapOfShapeShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_IndexedDataMapOfShapeShape) -> TopTools_IndexedDataMapOfShapeShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopTools_IndexedDataMapOfShapeShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theOther : TopTools_IndexedDataMapOfShapeShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_IndexedMapOfOrientedShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_IndexedMapOfOrientedShape) -> TopTools_IndexedMapOfOrientedShape: 
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
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopTools_IndexedMapOfOrientedShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_IndexedMapOfOrientedShape) -> None: ...
    pass
class TopTools_IndexedMapOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_IndexedMapOfShape) -> TopTools_IndexedMapOfShape: 
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
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopTools_IndexedMapOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def __init__(self,theOther : TopTools_IndexedMapOfShape) -> None: ...
    pass
class TopTools_ListOfListOfShape(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : TopTools_ListOfListOfShape) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : TopTools_ListOfShape) -> TopTools_ListOfShape: ...
    @overload
    def Append(self,theItem : TopTools_ListOfShape,theIter : Any) -> None: ...
    def Assign(self,theOther : TopTools_ListOfListOfShape) -> TopTools_ListOfListOfShape: 
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
    def First(self) -> TopTools_ListOfShape: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : TopTools_ListOfShape,theIter : Any) -> TopTools_ListOfShape: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TopTools_ListOfListOfShape,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : TopTools_ListOfShape,theIter : Any) -> TopTools_ListOfShape: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TopTools_ListOfListOfShape,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TopTools_ListOfShape: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TopTools_ListOfListOfShape) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : TopTools_ListOfShape) -> TopTools_ListOfShape: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_ListOfListOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_ListOfShape(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TopTools_ListOfShape) -> None: ...
    @overload
    def Append(self,theItem : OCP.TopoDS.TopoDS_Shape,theIter : Any) -> None: ...
    def Assign(self,theOther : TopTools_ListOfShape) -> TopTools_ListOfShape: 
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
    def First(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TopTools_ListOfShape,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OCP.TopoDS.TopoDS_Shape,theIter : Any) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def InsertBefore(self,theItem : OCP.TopoDS.TopoDS_Shape,theIter : Any) -> OCP.TopoDS.TopoDS_Shape: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TopTools_ListOfShape,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TopTools_ListOfShape) -> None: ...
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
    def __init__(self,theOther : TopTools_ListOfShape) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopTools_LocationSet():
    """
    The class LocationSet stores a set of location in a relocatable state.
    """
    def Add(self,L : OCP.TopLoc.TopLoc_Location) -> int: 
        """
        Incorporate a new Location in the set and returns its index.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def Dump(self,OS : io.BytesIO) -> None: 
        """
        Dumps the content of me on the stream <OS>.
        """
    def Index(self,L : OCP.TopLoc.TopLoc_Location) -> int: 
        """
        Returns the index of <L>.
        """
    def Location(self,I : int) -> OCP.TopLoc.TopLoc_Location: 
        """
        Returns the location of index <I>.
        """
    def Read(self,IS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.
        """
    def Write(self,OS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the content of me on the stream <OS> in a format that can be read back by Read.
        """
    def __init__(self) -> None: ...
    pass
class TopTools_MapOfOrientedShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Add
        """
    def Added(self,K : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_MapOfOrientedShape) -> TopTools_MapOfOrientedShape: 
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
    def Contains(self,theOther : TopTools_MapOfOrientedShape) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def Differ(self,theOther : TopTools_MapOfOrientedShape) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TopTools_MapOfOrientedShape,theRight : TopTools_MapOfOrientedShape) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TopTools_MapOfOrientedShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TopTools_MapOfOrientedShape) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TopTools_MapOfOrientedShape) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TopTools_MapOfOrientedShape,theRight : TopTools_MapOfOrientedShape) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TopTools_MapOfOrientedShape) -> bool: 
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
    def Remove(self,K : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TopTools_MapOfOrientedShape) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TopTools_MapOfOrientedShape,theRight : TopTools_MapOfOrientedShape) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TopTools_MapOfOrientedShape,theRight : TopTools_MapOfOrientedShape) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TopTools_MapOfOrientedShape) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theOther : TopTools_MapOfOrientedShape) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopTools_MapOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Add
        """
    def Added(self,K : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopTools_MapOfShape) -> TopTools_MapOfShape: 
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
    def Contains(self,K : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : TopTools_MapOfShape) -> bool: ...
    def Differ(self,theOther : TopTools_MapOfShape) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TopTools_MapOfShape,theRight : TopTools_MapOfShape) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TopTools_MapOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TopTools_MapOfShape) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TopTools_MapOfShape) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TopTools_MapOfShape,theRight : TopTools_MapOfShape) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TopTools_MapOfShape) -> bool: 
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
    def Remove(self,K : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TopTools_MapOfShape) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TopTools_MapOfShape,theRight : TopTools_MapOfShape) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TopTools_MapOfShape,theRight : TopTools_MapOfShape) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TopTools_MapOfShape) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopTools_MapOfShape) -> None: ...
    pass
class TopTools_MutexForShapeProvider():
    """
    Class TopTools_MutexForShapeProvider This class is used to create and store mutexes associated with shapes.
    """
    def CreateMutexForShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Creates and associates mutex with theShape
        """
    def CreateMutexesForSubShapes(self,theShape : OCP.TopoDS.TopoDS_Shape,theType : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        Creates and associates mutexes with each sub-shape of type theType in theShape.
        """
    def GetMutex(self,theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.Standard.Standard_Mutex: 
        """
        Returns pointer to mutex associated with theShape. In case when mutex not found returns NULL.
        """
    def RemoveAllMutexes(self) -> None: 
        """
        Removes all mutexes
        """
    def __init__(self) -> None: ...
    pass
class TopTools_OrientedShapeMapHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(theShape : OCP.TopoDS.TopoDS_Shape,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given shape, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns True when the two keys are equal. Two same keys must have the same hashcode, the contrary is not necessary.
        """
    def __init__(self) -> None: ...
    pass
class TopTools_HSequenceOfShape(TopTools_SequenceOfShape, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : TopTools_SequenceOfShape) -> None: ...
    def Assign(self,theOther : TopTools_SequenceOfShape) -> TopTools_SequenceOfShape: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TopTools_SequenceOfShape: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def First(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def InsertAfter(self,theIndex : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TopTools_SequenceOfShape) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TopTools_SequenceOfShape) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
    def Last(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Prepend(self,theSeq : TopTools_SequenceOfShape) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
    def Sequence(self) -> TopTools_SequenceOfShape: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TopTools_SequenceOfShape) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TopTools_SequenceOfShape) -> None: ...
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
class TopTools_ShapeMapHasher():
    """
    Hash tool, used for generating maps of shapes in topology.
    """
    @staticmethod
    def HashCode_s(theShape : OCP.TopoDS.TopoDS_Shape,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given shape, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns True when the two keys are the same. Two same keys must have the same hashcode, the contrary is not necessary.
        """
    def __init__(self) -> None: ...
    pass
class TopTools_ShapeSet():
    """
    A ShapeSets contains a Shape and all its sub-shapes and locations. It can be dump, write and read.
    """
    def Add(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Stores <S> and its sub-shape. Returns the index of <S>. The method AddGeometry is called on each sub-shape.
        """
    def AddGeometry(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Stores the geometry of <S>.
        """
    def AddShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Inserts the shape <S2> in the shape <S1>. This method must be redefined to use the correct builder.
        """
    def ChangeLocations(self) -> TopTools_LocationSet: 
        """
        None
        """
    def Check(self,T : OCP.TopAbs.TopAbs_ShapeEnum,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        This method is called after each new completed shape. <T> is the type. <S> is the shape. In this class it does nothing, but it gives the opportunity in derived classes to perform extra treatment on shapes.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the set. This method can be redefined.
        """
    @overload
    def Dump(self,OS : io.BytesIO) -> None: 
        """
        Dumps the content of me on the stream <OS>.

        Dumps on <OS> the shape <S>. Dumps the orientation, the index of the TShape and the index of the Location.
        """
    @overload
    def Dump(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: ...
    @overload
    def DumpExtent(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the number of objects in me on the stream <OS>. (Number of shapes of each type)

        Dumps the number of objects in me in the string S (Number of shapes of each type)
        """
    @overload
    def DumpExtent(self,S : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def DumpGeometry(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: 
        """
        Dumps the geometry of me on the stream <OS>.

        Dumps the geometry of <S> on the stream <OS>.
        """
    @overload
    def DumpGeometry(self,OS : io.BytesIO) -> None: ...
    def FormatNb(self) -> int: 
        """
        two formats available for the moment: First: does not write CurveOnSurface UV Points into the file on reading calls Check() method. Second: stores CurveOnSurface UV Points. On reading format is recognized from Version string.
        """
    def Index(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Returns the index of <S>.
        """
    def Locations(self) -> TopTools_LocationSet: 
        """
        None
        """
    def NbShapes(self) -> int: 
        """
        Returns number of shapes read from file.
        """
    @overload
    def Read(self,IS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.

        Reads from <IS> a shape and returns it in S.
        """
    @overload
    def Read(self,S : OCP.TopoDS.TopoDS_Shape,IS : io.BytesIO) -> None: ...
    @overload
    def ReadGeometry(self,T : OCP.TopAbs.TopAbs_ShapeEnum,IS : io.BytesIO,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Reads the geometry of me from the stream <IS>.

        Reads the geometry of a shape of type <T> from the stream <IS> and returns it in <S>.
        """
    @overload
    def ReadGeometry(self,IS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def SetFormatNb(self,theFormatNb : int) -> None: 
        """
        None
        """
    def Shape(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the sub-shape of index <I>.
        """
    @overload
    def Write(self,OS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the content of me on the stream <OS> in a format that can be read back by Read.

        Writes on <OS> the shape <S>. Writes the orientation, the index of the TShape and the index of the Location.
        """
    @overload
    def Write(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: ...
    @overload
    def WriteGeometry(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: 
        """
        Writes the geometry of me on the stream <OS> in a format that can be read back by Read.

        Writes the geometry of <S> on the stream <OS> in a format that can be read back by Read.
        """
    @overload
    def WriteGeometry(self,OS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def __init__(self) -> None: ...
    pass
