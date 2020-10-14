import OCP.NCollection
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
import OCP.gp
__all__  = [
"NCollection_BaseAllocator",
"NCollection_AlignedAllocator",
"NCollection_AccAllocator",
"NCollection_BaseList",
"NCollection_BaseMap",
"NCollection_BaseSequence",
"NCollection_BaseVector",
"NCollection_Buffer",
"NCollection_CellFilter_Action",
"NCollection_CellFilter_InspectorXY",
"NCollection_CellFilter_InspectorXYZ",
"NCollection_HeapAllocator",
"NCollection_IncAllocator",
"NCollection_SparseArrayBase",
"NCollection_StdAllocator_void",
"NCollection_Utf16Iter",
"NCollection_Utf16String",
"NCollection_Utf32Iter",
"NCollection_Utf32String",
"NCollection_Utf8Iter",
"NCollection_Utf8String",
"NCollection_UtfStringTool",
"NCollection_UtfWideIter",
"NCollection_UtfWideString",
"NCollection_WinHeapAllocator",
"GetCapacity",
"CellFilter_Keep",
"CellFilter_Purge"
]
class NCollection_BaseAllocator(OCP.Standard.Standard_Transient):
    """
    Purpose: Basic class for memory allocation wizards. Defines the interface for devising different allocators firstly to be used by collections of NCollection, though it it is not deferred. It allocates/frees the memory through Standard procedures, thus it is unnecessary (and sometimes injurious) to have more than one such allocator. To avoid creation of multiple objects the constructors were maid inaccessible. To create the BaseAllocator use the method CommonBaseAllocator. Note that this object is managed by Handle.Purpose: Basic class for memory allocation wizards. Defines the interface for devising different allocators firstly to be used by collections of NCollection, though it it is not deferred. It allocates/frees the memory through Standard procedures, thus it is unnecessary (and sometimes injurious) to have more than one such allocator. To avoid creation of multiple objects the constructors were maid inaccessible. To create the BaseAllocator use the method CommonBaseAllocator. Note that this object is managed by Handle.
    """
    def Allocate(self,size : int) -> capsule: 
        """
        None
        """
    @staticmethod
    def CommonBaseAllocator_s() -> NCollection_BaseAllocator: 
        """
        CommonBaseAllocator This method is designed to have the only one BaseAllocator (to avoid useless copying of collections). However one can use operator new to create more BaseAllocators, but it is injurious.
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
    def Free(self,anAddress : capsule) -> None: 
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
    @staticmethod
    def PrintMemUsageStatistics_s() -> None: 
        """
        Prints memory usage statistics cumulated by StandardCallBack
        """
    @staticmethod
    def StandardCallBack_s(theIsAlloc : bool,theStorage : capsule,theRoundSize : int,theSize : int) -> None: 
        """
        Callback function to register alloc/free calls
        """
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
class NCollection_AlignedAllocator(NCollection_BaseAllocator, OCP.Standard.Standard_Transient):
    """
    NCollection allocator with managed memory alignment capabilities.NCollection allocator with managed memory alignment capabilities.
    """
    def Allocate(self,theSize : int) -> capsule: 
        """
        Allocate memory with given size. Returns NULL on failure.
        """
    @staticmethod
    def CommonBaseAllocator_s() -> NCollection_BaseAllocator: 
        """
        CommonBaseAllocator This method is designed to have the only one BaseAllocator (to avoid useless copying of collections). However one can use operator new to create more BaseAllocators, but it is injurious.
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
    def Free(self,thePtr : capsule) -> None: 
        """
        Free a previously allocated memory.
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
    @staticmethod
    def PrintMemUsageStatistics_s() -> None: 
        """
        Prints memory usage statistics cumulated by StandardCallBack
        """
    @staticmethod
    def StandardCallBack_s(theIsAlloc : bool,theStorage : capsule,theRoundSize : int,theSize : int) -> None: 
        """
        Callback function to register alloc/free calls
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theAlignment : int) -> None: ...
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
class NCollection_AccAllocator(NCollection_BaseAllocator, OCP.Standard.Standard_Transient):
    """
    Class NCollection_AccAllocator - accumulating memory allocator. This class allocates memory on request returning the pointer to the allocated space. The allocation units are grouped in blocks requested from the system as required. This memory is returned to the system when all allocations in a block are freed.Class NCollection_AccAllocator - accumulating memory allocator. This class allocates memory on request returning the pointer to the allocated space. The allocation units are grouped in blocks requested from the system as required. This memory is returned to the system when all allocations in a block are freed.
    """
    def Allocate(self,theSize : int) -> capsule: 
        """
        Allocate memory with given size
        """
    @staticmethod
    def CommonBaseAllocator_s() -> NCollection_BaseAllocator: 
        """
        CommonBaseAllocator This method is designed to have the only one BaseAllocator (to avoid useless copying of collections). However one can use operator new to create more BaseAllocators, but it is injurious.
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
    def Free(self,theAddress : capsule) -> None: 
        """
        Free a previously allocated memory; memory is returned to the OS when all allocations in some block are freed
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
    @staticmethod
    def PrintMemUsageStatistics_s() -> None: 
        """
        Prints memory usage statistics cumulated by StandardCallBack
        """
    @staticmethod
    def StandardCallBack_s(theIsAlloc : bool,theStorage : capsule,theRoundSize : int,theSize : int) -> None: 
        """
        Callback function to register alloc/free calls
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theBlockSize : int=24600) -> None: ...
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
class NCollection_BaseList():
    """
    None
    """
    def Allocator(self) -> NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Extent(self) -> int: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    pass
class NCollection_BaseMap():
    """
    Purpose: This is a base class for all Maps: Map DataMap DoubleMap IndexedMap IndexedDataMap Provides utilitites for managing the buckets.
    """
    def Allocator(self) -> NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    pass
class NCollection_BaseSequence():
    """
    Purpose: This is a base class for the Sequence. It deals with an indexed bidirectional list of NCollection_SeqNode's.
    """
    def Allocator(self) -> NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Length(self) -> int: 
        """
        None
        """
    pass
class NCollection_BaseVector():
    """
    Class NCollection_BaseVector - base for NCollection_Vector template
    """
    def Allocator(self) -> NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    pass
class NCollection_Buffer(OCP.Standard.Standard_Transient):
    """
    Low-level buffer object.Low-level buffer object.
    """
    def Allocate(self,theSize : int) -> bool: 
        """
        Allocate the buffer.
        """
    def Allocator(self) -> NCollection_BaseAllocator: 
        """
        Returns buffer allocator
        """
    def ChangeData(self) -> int: 
        """
        Returns buffer data
        """
    def Data(self) -> int: 
        """
        Returns buffer data
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
    def Free(self) -> None: 
        """
        De-allocate buffer.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if buffer is not allocated
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
    def SetAllocator(self,theAlloc : NCollection_BaseAllocator) -> None: 
        """
        Assign new buffer allocator with de-allocation of buffer.
        """
    def Size(self) -> int: 
        """
        Return buffer length in bytes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theAlloc : NCollection_BaseAllocator,theSize : int=0,theData : int=None) -> None: ...
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
class NCollection_CellFilter_Action():
    """
    Auxiliary enumeration serving as responce from method Inspect

    Members:

      CellFilter_Keep

      CellFilter_Purge
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
    CellFilter_Keep: OCP.NCollection.NCollection_CellFilter_Action # value = NCollection_CellFilter_Action.CellFilter_Keep
    CellFilter_Purge: OCP.NCollection.NCollection_CellFilter_Action # value = NCollection_CellFilter_Action.CellFilter_Purge
    __entries: dict # value = {'CellFilter_Keep': (NCollection_CellFilter_Action.CellFilter_Keep, None), 'CellFilter_Purge': (NCollection_CellFilter_Action.CellFilter_Purge, None)}
    __members__: dict # value = {'CellFilter_Keep': NCollection_CellFilter_Action.CellFilter_Keep, 'CellFilter_Purge': NCollection_CellFilter_Action.CellFilter_Purge}
    pass
class NCollection_CellFilter_InspectorXY():
    """
    None
    """
    @staticmethod
    def Coord_s(i : int,thePnt : OCP.gp.gp_XY) -> float: 
        """
        Access to co-ordinate
        """
    def Shift(self,thePnt : OCP.gp.gp_XY,theTol : float) -> OCP.gp.gp_XY: 
        """
        Auxiliary method to shift point by each coordinate on given value; useful for preparing a points range for Inspect with tolerance
        """
    def __init__(self) -> None: ...
    pass
class NCollection_CellFilter_InspectorXYZ():
    """
    None
    """
    @staticmethod
    def Coord_s(i : int,thePnt : OCP.gp.gp_XYZ) -> float: 
        """
        Access to co-ordinate
        """
    def Shift(self,thePnt : OCP.gp.gp_XYZ,theTol : float) -> OCP.gp.gp_XYZ: 
        """
        Auxiliary method to shift point by each coordinate on given value; useful for preparing a points range for Inspect with tolerance
        """
    def __init__(self) -> None: ...
    pass
class NCollection_HeapAllocator(NCollection_BaseAllocator, OCP.Standard.Standard_Transient):
    """
    Allocator that uses the global dynamic heap (malloc / free).Allocator that uses the global dynamic heap (malloc / free).
    """
    def Allocate(self,theSize : int) -> capsule: 
        """
        None
        """
    @staticmethod
    def CommonBaseAllocator_s() -> NCollection_BaseAllocator: 
        """
        CommonBaseAllocator This method is designed to have the only one BaseAllocator (to avoid useless copying of collections). However one can use operator new to create more BaseAllocators, but it is injurious.
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
    def Free(self,anAddress : capsule) -> None: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def GlobalHeapAllocator_s() -> NCollection_HeapAllocator: 
        """
        None
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
    @staticmethod
    def PrintMemUsageStatistics_s() -> None: 
        """
        Prints memory usage statistics cumulated by StandardCallBack
        """
    @staticmethod
    def StandardCallBack_s(theIsAlloc : bool,theStorage : capsule,theRoundSize : int,theSize : int) -> None: 
        """
        Callback function to register alloc/free calls
        """
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
class NCollection_IncAllocator(NCollection_BaseAllocator, OCP.Standard.Standard_Transient):
    """
    Class NCollection_IncAllocator - incremental memory allocator. This class allocates memory on request returning the pointer to an allocated block. This memory is never returned to the system until the allocator is destroyed.Class NCollection_IncAllocator - incremental memory allocator. This class allocates memory on request returning the pointer to an allocated block. This memory is never returned to the system until the allocator is destroyed.
    """
    def Allocate(self,size : int) -> capsule: 
        """
        Allocate memory with given size. Returns NULL on failure
        """
    @staticmethod
    def CommonBaseAllocator_s() -> NCollection_BaseAllocator: 
        """
        CommonBaseAllocator This method is designed to have the only one BaseAllocator (to avoid useless copying of collections). However one can use operator new to create more BaseAllocators, but it is injurious.
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
    def Free(self,anAddress : capsule) -> None: 
        """
        Free a previously allocated memory. Does nothing
        """
    def GetMemSize(self) -> int: 
        """
        Diagnostic method, returns the total allocated size
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
    @staticmethod
    def PrintMemUsageStatistics_s() -> None: 
        """
        Prints memory usage statistics cumulated by StandardCallBack
        """
    def Reallocate(self,anAddress : capsule,oldSize : int,newSize : int) -> capsule: 
        """
        Reallocation: it is always allowed but is only efficient with the last allocated item
        """
    def Reset(self,doReleaseMem : bool=True) -> None: 
        """
        Re-initialize the allocator so that the next Allocate call should start allocating in the very begining as though the allocator is just constructed. Warning: make sure that all previously allocated data are no more used in your code!
        """
    def SetThreadSafe(self,theIsThreadSafe : bool=True) -> None: 
        """
        Setup mutex for thread-safe allocations.
        """
    @staticmethod
    def StandardCallBack_s(theIsAlloc : bool,theStorage : capsule,theRoundSize : int,theSize : int) -> None: 
        """
        Callback function to register alloc/free calls
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theBlockSize : int=24600) -> None: ...
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
class NCollection_SparseArrayBase():
    """
    Base class for NCollection_SparseArray; provides non-template implementation of general mechanics of block allocation, items creation / deletion etc.
    """
    def Clear(self) -> None: 
        """
        Clears all the data
        """
    def HasValue(self,theIndex : int) -> bool: 
        """
        Check whether the value at given index is set
        """
    def Size(self) -> int: 
        """
        Returns number of currently contained items
        """
    def UnsetValue(self,theIndex : int) -> bool: 
        """
        Deletes the item from the array; returns True if that item was defined
        """
    pass
class NCollection_StdAllocator_void():
    """
    Implements specialization NCollection_StdAllocator<void>. Specialization is of low value and should normally be avoided in favor of a typed specialization.
    """
    def Allocator(self) -> NCollection_BaseAllocator: 
        """
        Returns an underlying NCollection_BaseAllocator instance. Returns an object specified in the constructor.
        """
    @overload
    def __init__(self,X : NCollection_StdAllocator_void) -> None: ...
    @overload
    def __init__(self,theAlloc : NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class NCollection_Utf16Iter():
    """
    Template class for Unicode strings support.
    """
    def AdvanceBytesUtf16(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-16. 0 means an invalid symbol; 2 bytes is a general case; 4 bytes for surrogate pair.
        """
    def AdvanceBytesUtf32(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-32. Always 4 bytes (method for consistency).
        """
    def AdvanceBytesUtf8(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-8. 0 means an invalid symbol; 1-4 bytes are valid range.
        """
    def AdvanceCodeUnitsUtf16(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-16. 0 means an invalid symbol; 1 16-bit code unit is a general case; 2 16-bit code units for surrogate pair.
        """
    def BufferHere(self) -> str: 
        """
        Buffer-fetching getter.
        """
    def BufferNext(self) -> str: 
        """
        Buffer-fetching getter.
        """
    def ChangeBufferHere(self) -> str: 
        """
        Buffer-fetching getter. Dangerous! Iterator should be reinitialized on buffer change.
        """
    def GetUtf16(self,theBuffer : str) -> str: 
        """
        Fill the UTF-16 buffer within current Unicode symbol. Use method AdvanceUtf16() to allocate buffer with enough size.
        """
    def GetUtf32(self,theBuffer : str) -> str: 
        """
        Fill the UTF-32 buffer within current Unicode symbol. Use method AdvanceUtf32() to allocate buffer with enough size.
        """
    @overload
    def GetUtf8(self,theBuffer : int) -> int: 
        """
        Fill the UTF-8 buffer within current Unicode symbol. Use method AdvanceUtf8() to allocate buffer with enough size.

        None
        """
    @overload
    def GetUtf8(self,theBuffer : str) -> str: ...
    def Index(self) -> int: 
        """
        Returns the index displacement from iterator intialization (first symbol has index 0)
        """
    def Init(self,theString : str) -> None: 
        """
        Initialize iterator within specified NULL-terminated string.
        """
    def IsValid(self) -> bool: 
        """
        Return true if Unicode symbol is within valid range.
        """
    def __init__(self,theString : str) -> None: ...
    def __mul__(self) -> str: 
        """
        Dereference operator.
        """
    def __rmul__(self) -> str: 
        """
        Dereference operator.
        """
    pass
class NCollection_Utf16String():
    """
    This template class represent constant UTF-* string. String stored in memory continuously, always NULL-terminated and can be used as standard C-string using ToCString() method.
    """
    def Assign(self,theOther : NCollection_Utf16String) -> NCollection_Utf16String: 
        """
        Copy from another string.
        """
    def Clear(self) -> None: 
        """
        Zero string.
        """
    def FromLocale(self,theString : str,theLength : int=-1) -> None: 
        """
        Copy from multibyte string in current system locale.
        """
    def GetChar(self,theCharIndex : int) -> str: 
        """
        Retrieve Unicode symbol at specified position. Warning! This is a slow access. Iterator should be used for consecutive parsing.
        """
    def GetCharBuffer(self,theCharIndex : int) -> str: 
        """
        Retrieve string buffer at specified position. Warning! This is a slow access. Iterator should be used for consecutive parsing.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if string is empty
        """
    def IsEqual(self,theCompare : NCollection_Utf16String) -> bool: 
        """
        Compares this string with another one.
        """
    def Iterator(self) -> NCollection_Utf16Iter: 
        """
        None
        """
    def Length(self) -> int: 
        """
        Returns the length of the string in Unicode symbols
        """
    def Size(self) -> int: 
        """
        Returns the size of the buffer in bytes, excluding NULL-termination symbol
        """
    def SubString(self,theStart : int,theEnd : int) -> NCollection_Utf16String: 
        """
        Returns the substring.
        """
    def Swap(self,theOther : NCollection_Utf16String) -> None: 
        """
        Exchange the data of two strings (without reallocating memory).
        """
    def ToCString(self) -> str: 
        """
        Returns NULL-terminated Unicode string. Should not be modifed or deleted!
        """
    def ToLocale(self,theBuffer : str,theSizeBytes : int) -> bool: 
        """
        Converts the string into string in the current system locale.
        """
    def ToUtf16(self) -> NCollection_Utf16String: 
        """
        Returns copy in UTF-16 format
        """
    def ToUtf32(self) -> NCollection_Utf32String: 
        """
        Returns copy in UTF-32 format
        """
    def ToUtf8(self) -> NCollection_Utf8String: 
        """
        Returns copy in UTF-8 format
        """
    def ToUtfWide(self) -> NCollection_UtfWideString: 
        """
        Returns copy in wide format (UTF-16 on Windows and UTF-32 on Linux)
        """
    def __iadd__(self,theAppend : NCollection_Utf16String) -> NCollection_Utf16String: 
        """
        Join strings.
        """
    @overload
    def __init__(self,theCopy : NCollection_Utf16String) -> None: ...
    @overload
    def __init__(self,theCopyUtf32 : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self,theCopyUtf16 : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self,theCopyUtfWide : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCopyUtf8 : str,theLength : int=-1) -> None: ...
    pass
class NCollection_Utf32Iter():
    """
    Template class for Unicode strings support.
    """
    def AdvanceBytesUtf16(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-16. 0 means an invalid symbol; 2 bytes is a general case; 4 bytes for surrogate pair.
        """
    def AdvanceBytesUtf32(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-32. Always 4 bytes (method for consistency).
        """
    def AdvanceBytesUtf8(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-8. 0 means an invalid symbol; 1-4 bytes are valid range.
        """
    def AdvanceCodeUnitsUtf16(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-16. 0 means an invalid symbol; 1 16-bit code unit is a general case; 2 16-bit code units for surrogate pair.
        """
    def BufferHere(self) -> str: 
        """
        Buffer-fetching getter.
        """
    def BufferNext(self) -> str: 
        """
        Buffer-fetching getter.
        """
    def ChangeBufferHere(self) -> str: 
        """
        Buffer-fetching getter. Dangerous! Iterator should be reinitialized on buffer change.
        """
    def GetUtf16(self,theBuffer : str) -> str: 
        """
        Fill the UTF-16 buffer within current Unicode symbol. Use method AdvanceUtf16() to allocate buffer with enough size.
        """
    def GetUtf32(self,theBuffer : str) -> str: 
        """
        Fill the UTF-32 buffer within current Unicode symbol. Use method AdvanceUtf32() to allocate buffer with enough size.
        """
    @overload
    def GetUtf8(self,theBuffer : str) -> str: 
        """
        Fill the UTF-8 buffer within current Unicode symbol. Use method AdvanceUtf8() to allocate buffer with enough size.

        None
        """
    @overload
    def GetUtf8(self,theBuffer : int) -> int: ...
    def Index(self) -> int: 
        """
        Returns the index displacement from iterator intialization (first symbol has index 0)
        """
    def Init(self,theString : str) -> None: 
        """
        Initialize iterator within specified NULL-terminated string.
        """
    def IsValid(self) -> bool: 
        """
        Return true if Unicode symbol is within valid range.
        """
    def __init__(self,theString : str) -> None: ...
    def __mul__(self) -> str: 
        """
        Dereference operator.
        """
    def __rmul__(self) -> str: 
        """
        Dereference operator.
        """
    pass
class NCollection_Utf32String():
    """
    This template class represent constant UTF-* string. String stored in memory continuously, always NULL-terminated and can be used as standard C-string using ToCString() method.
    """
    def Assign(self,theOther : NCollection_Utf32String) -> NCollection_Utf32String: 
        """
        Copy from another string.
        """
    def Clear(self) -> None: 
        """
        Zero string.
        """
    def FromLocale(self,theString : str,theLength : int=-1) -> None: 
        """
        Copy from multibyte string in current system locale.
        """
    def GetChar(self,theCharIndex : int) -> str: 
        """
        Retrieve Unicode symbol at specified position. Warning! This is a slow access. Iterator should be used for consecutive parsing.
        """
    def GetCharBuffer(self,theCharIndex : int) -> str: 
        """
        Retrieve string buffer at specified position. Warning! This is a slow access. Iterator should be used for consecutive parsing.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if string is empty
        """
    def IsEqual(self,theCompare : NCollection_Utf32String) -> bool: 
        """
        Compares this string with another one.
        """
    def Iterator(self) -> NCollection_Utf32Iter: 
        """
        None
        """
    def Length(self) -> int: 
        """
        Returns the length of the string in Unicode symbols
        """
    def Size(self) -> int: 
        """
        Returns the size of the buffer in bytes, excluding NULL-termination symbol
        """
    def SubString(self,theStart : int,theEnd : int) -> NCollection_Utf32String: 
        """
        Returns the substring.
        """
    def Swap(self,theOther : NCollection_Utf32String) -> None: 
        """
        Exchange the data of two strings (without reallocating memory).
        """
    def ToCString(self) -> str: 
        """
        Returns NULL-terminated Unicode string. Should not be modifed or deleted!
        """
    def ToLocale(self,theBuffer : str,theSizeBytes : int) -> bool: 
        """
        Converts the string into string in the current system locale.
        """
    def ToUtf16(self) -> NCollection_Utf16String: 
        """
        Returns copy in UTF-16 format
        """
    def ToUtf32(self) -> NCollection_Utf32String: 
        """
        Returns copy in UTF-32 format
        """
    def ToUtf8(self) -> NCollection_Utf8String: 
        """
        Returns copy in UTF-8 format
        """
    def ToUtfWide(self) -> NCollection_UtfWideString: 
        """
        Returns copy in wide format (UTF-16 on Windows and UTF-32 on Linux)
        """
    def __iadd__(self,theAppend : NCollection_Utf32String) -> NCollection_Utf32String: 
        """
        Join strings.
        """
    @overload
    def __init__(self,theCopyUtf32 : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self,theCopy : NCollection_Utf32String) -> None: ...
    @overload
    def __init__(self,theCopyUtf8 : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self,theCopyUtfWide : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCopyUtf16 : str,theLength : int=-1) -> None: ...
    pass
class NCollection_Utf8Iter():
    """
    Template class for Unicode strings support.
    """
    def AdvanceBytesUtf16(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-16. 0 means an invalid symbol; 2 bytes is a general case; 4 bytes for surrogate pair.
        """
    def AdvanceBytesUtf32(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-32. Always 4 bytes (method for consistency).
        """
    def AdvanceBytesUtf8(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-8. 0 means an invalid symbol; 1-4 bytes are valid range.
        """
    def AdvanceCodeUnitsUtf16(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-16. 0 means an invalid symbol; 1 16-bit code unit is a general case; 2 16-bit code units for surrogate pair.
        """
    def BufferHere(self) -> str: 
        """
        Buffer-fetching getter.
        """
    def BufferNext(self) -> str: 
        """
        Buffer-fetching getter.
        """
    def ChangeBufferHere(self) -> str: 
        """
        Buffer-fetching getter. Dangerous! Iterator should be reinitialized on buffer change.
        """
    def GetUtf16(self,theBuffer : str) -> str: 
        """
        Fill the UTF-16 buffer within current Unicode symbol. Use method AdvanceUtf16() to allocate buffer with enough size.
        """
    def GetUtf32(self,theBuffer : str) -> str: 
        """
        Fill the UTF-32 buffer within current Unicode symbol. Use method AdvanceUtf32() to allocate buffer with enough size.
        """
    @overload
    def GetUtf8(self,theBuffer : str) -> str: 
        """
        Fill the UTF-8 buffer within current Unicode symbol. Use method AdvanceUtf8() to allocate buffer with enough size.

        None
        """
    @overload
    def GetUtf8(self,theBuffer : int) -> int: ...
    def Index(self) -> int: 
        """
        Returns the index displacement from iterator intialization (first symbol has index 0)
        """
    def Init(self,theString : str) -> None: 
        """
        Initialize iterator within specified NULL-terminated string.
        """
    def IsValid(self) -> bool: 
        """
        Return true if Unicode symbol is within valid range.
        """
    def __init__(self,theString : str) -> None: ...
    def __mul__(self) -> str: 
        """
        Dereference operator.
        """
    def __rmul__(self) -> str: 
        """
        Dereference operator.
        """
    pass
class NCollection_Utf8String():
    """
    This template class represent constant UTF-* string. String stored in memory continuously, always NULL-terminated and can be used as standard C-string using ToCString() method.
    """
    def Assign(self,theOther : NCollection_Utf8String) -> NCollection_Utf8String: 
        """
        Copy from another string.
        """
    def Clear(self) -> None: 
        """
        Zero string.
        """
    def FromLocale(self,theString : str,theLength : int=-1) -> None: 
        """
        Copy from multibyte string in current system locale.
        """
    def GetChar(self,theCharIndex : int) -> str: 
        """
        Retrieve Unicode symbol at specified position. Warning! This is a slow access. Iterator should be used for consecutive parsing.
        """
    def GetCharBuffer(self,theCharIndex : int) -> str: 
        """
        Retrieve string buffer at specified position. Warning! This is a slow access. Iterator should be used for consecutive parsing.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if string is empty
        """
    def IsEqual(self,theCompare : NCollection_Utf8String) -> bool: 
        """
        Compares this string with another one.
        """
    def Iterator(self) -> NCollection_Utf8Iter: 
        """
        None
        """
    def Length(self) -> int: 
        """
        Returns the length of the string in Unicode symbols
        """
    def Size(self) -> int: 
        """
        Returns the size of the buffer in bytes, excluding NULL-termination symbol
        """
    def SubString(self,theStart : int,theEnd : int) -> NCollection_Utf8String: 
        """
        Returns the substring.
        """
    def Swap(self,theOther : NCollection_Utf8String) -> None: 
        """
        Exchange the data of two strings (without reallocating memory).
        """
    def ToCString(self) -> str: 
        """
        Returns NULL-terminated Unicode string. Should not be modifed or deleted!
        """
    def ToLocale(self,theBuffer : str,theSizeBytes : int) -> bool: 
        """
        Converts the string into string in the current system locale.
        """
    def ToUtf16(self) -> NCollection_Utf16String: 
        """
        Returns copy in UTF-16 format
        """
    def ToUtf32(self) -> NCollection_Utf32String: 
        """
        Returns copy in UTF-32 format
        """
    def ToUtf8(self) -> NCollection_Utf8String: 
        """
        Returns copy in UTF-8 format
        """
    def ToUtfWide(self) -> NCollection_UtfWideString: 
        """
        Returns copy in wide format (UTF-16 on Windows and UTF-32 on Linux)
        """
    def __iadd__(self,theAppend : NCollection_Utf8String) -> NCollection_Utf8String: 
        """
        Join strings.
        """
    @overload
    def __init__(self,theCopyUtf8 : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self,theCopyUtfWide : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCopyUtf32 : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self,theCopy : NCollection_Utf8String) -> None: ...
    @overload
    def __init__(self,theCopyUtf16 : str,theLength : int=-1) -> None: ...
    pass
class NCollection_UtfStringTool():
    """
    Auxiliary convertion tool.
    """
    def FromLocale(self,theString : str) -> str: 
        """
        Convert the string from current locale into UNICODE (wide characters) using system APIs. Returned pointer will be released by this tool.
        """
    @staticmethod
    def ToLocale_s(theWideString : str,theBuffer : str,theSizeBytes : int) -> bool: 
        """
        Convert the UNICODE (wide characters) string into locale using system APIs.
        """
    def __init__(self) -> None: ...
    pass
class NCollection_UtfWideIter():
    """
    Template class for Unicode strings support.
    """
    def AdvanceBytesUtf16(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-16. 0 means an invalid symbol; 2 bytes is a general case; 4 bytes for surrogate pair.
        """
    def AdvanceBytesUtf32(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-32. Always 4 bytes (method for consistency).
        """
    def AdvanceBytesUtf8(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-8. 0 means an invalid symbol; 1-4 bytes are valid range.
        """
    def AdvanceCodeUnitsUtf16(self) -> int: 
        """
        Returns the advance in bytes to store current symbol in UTF-16. 0 means an invalid symbol; 1 16-bit code unit is a general case; 2 16-bit code units for surrogate pair.
        """
    def BufferHere(self) -> str: 
        """
        Buffer-fetching getter.
        """
    def BufferNext(self) -> str: 
        """
        Buffer-fetching getter.
        """
    def ChangeBufferHere(self) -> str: 
        """
        Buffer-fetching getter. Dangerous! Iterator should be reinitialized on buffer change.
        """
    def GetUtf16(self,theBuffer : str) -> str: 
        """
        Fill the UTF-16 buffer within current Unicode symbol. Use method AdvanceUtf16() to allocate buffer with enough size.
        """
    def GetUtf32(self,theBuffer : str) -> str: 
        """
        Fill the UTF-32 buffer within current Unicode symbol. Use method AdvanceUtf32() to allocate buffer with enough size.
        """
    @overload
    def GetUtf8(self,theBuffer : str) -> str: 
        """
        Fill the UTF-8 buffer within current Unicode symbol. Use method AdvanceUtf8() to allocate buffer with enough size.

        None
        """
    @overload
    def GetUtf8(self,theBuffer : int) -> int: ...
    def Index(self) -> int: 
        """
        Returns the index displacement from iterator intialization (first symbol has index 0)
        """
    def Init(self,theString : str) -> None: 
        """
        Initialize iterator within specified NULL-terminated string.
        """
    def IsValid(self) -> bool: 
        """
        Return true if Unicode symbol is within valid range.
        """
    def __init__(self,theString : str) -> None: ...
    def __mul__(self) -> str: 
        """
        Dereference operator.
        """
    def __rmul__(self) -> str: 
        """
        Dereference operator.
        """
    pass
class NCollection_UtfWideString():
    """
    This template class represent constant UTF-* string. String stored in memory continuously, always NULL-terminated and can be used as standard C-string using ToCString() method.
    """
    def Assign(self,theOther : NCollection_UtfWideString) -> NCollection_UtfWideString: 
        """
        Copy from another string.
        """
    def Clear(self) -> None: 
        """
        Zero string.
        """
    def FromLocale(self,theString : str,theLength : int=-1) -> None: 
        """
        Copy from multibyte string in current system locale.
        """
    def GetChar(self,theCharIndex : int) -> str: 
        """
        Retrieve Unicode symbol at specified position. Warning! This is a slow access. Iterator should be used for consecutive parsing.
        """
    def GetCharBuffer(self,theCharIndex : int) -> str: 
        """
        Retrieve string buffer at specified position. Warning! This is a slow access. Iterator should be used for consecutive parsing.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if string is empty
        """
    def IsEqual(self,theCompare : NCollection_UtfWideString) -> bool: 
        """
        Compares this string with another one.
        """
    def Iterator(self) -> NCollection_UtfWideIter: 
        """
        None
        """
    def Length(self) -> int: 
        """
        Returns the length of the string in Unicode symbols
        """
    def Size(self) -> int: 
        """
        Returns the size of the buffer in bytes, excluding NULL-termination symbol
        """
    def SubString(self,theStart : int,theEnd : int) -> NCollection_UtfWideString: 
        """
        Returns the substring.
        """
    def Swap(self,theOther : NCollection_UtfWideString) -> None: 
        """
        Exchange the data of two strings (without reallocating memory).
        """
    def ToCString(self) -> str: 
        """
        Returns NULL-terminated Unicode string. Should not be modifed or deleted!
        """
    def ToLocale(self,theBuffer : str,theSizeBytes : int) -> bool: 
        """
        Converts the string into string in the current system locale.
        """
    def ToUtf16(self) -> NCollection_Utf16String: 
        """
        Returns copy in UTF-16 format
        """
    def ToUtf32(self) -> NCollection_Utf32String: 
        """
        Returns copy in UTF-32 format
        """
    def ToUtf8(self) -> NCollection_Utf8String: 
        """
        Returns copy in UTF-8 format
        """
    def ToUtfWide(self) -> NCollection_UtfWideString: 
        """
        Returns copy in wide format (UTF-16 on Windows and UTF-32 on Linux)
        """
    def __iadd__(self,theAppend : NCollection_UtfWideString) -> NCollection_UtfWideString: 
        """
        Join strings.
        """
    @overload
    def __init__(self,theCopyUtf16 : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self,theCopyUtf8 : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCopy : NCollection_UtfWideString) -> None: ...
    @overload
    def __init__(self,theCopyUtfWide : str,theLength : int=-1) -> None: ...
    @overload
    def __init__(self,theCopyUtf32 : str,theLength : int=-1) -> None: ...
    pass
class NCollection_WinHeapAllocator(NCollection_BaseAllocator, OCP.Standard.Standard_Transient):
    """
    This memory allocator creates dedicated heap for allocations. This technics available only on Windows platform (no alternative on Unix systems). It may be used to take control over memory fragmentation because on destruction ALL allocated memory will be released to the system.This memory allocator creates dedicated heap for allocations. This technics available only on Windows platform (no alternative on Unix systems). It may be used to take control over memory fragmentation because on destruction ALL allocated memory will be released to the system.
    """
    def Allocate(self,theSize : int) -> capsule: 
        """
        Allocate memory
        """
    @staticmethod
    def CommonBaseAllocator_s() -> NCollection_BaseAllocator: 
        """
        CommonBaseAllocator This method is designed to have the only one BaseAllocator (to avoid useless copying of collections). However one can use operator new to create more BaseAllocators, but it is injurious.
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
    def Free(self,theAddress : capsule) -> None: 
        """
        Release memory
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
    @staticmethod
    def PrintMemUsageStatistics_s() -> None: 
        """
        Prints memory usage statistics cumulated by StandardCallBack
        """
    @staticmethod
    def StandardCallBack_s(theIsAlloc : bool,theStorage : capsule,theRoundSize : int,theSize : int) -> None: 
        """
        Callback function to register alloc/free calls
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theInitSizeBytes : int=524288) -> None: ...
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
def GetCapacity(theIncrement : int) -> int:
    """
    None
    """
CellFilter_Keep: OCP.NCollection.NCollection_CellFilter_Action # value = NCollection_CellFilter_Action.CellFilter_Keep
CellFilter_Purge: OCP.NCollection.NCollection_CellFilter_Action # value = NCollection_CellFilter_Action.CellFilter_Purge
