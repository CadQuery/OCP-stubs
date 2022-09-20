import OCP.StdStorage
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StdObjMgt
import OCP.NCollection
import OCP.Storage
import OCP.Standard
import OCP.TCollection
import OCP.TColStd
__all__  = [
"StdStorage",
"StdStorage_BucketIterator",
"StdStorage_Data",
"StdStorage_SequenceOfRoots",
"StdStorage_HeaderData",
"StdStorage_Root",
"StdStorage_RootData",
"StdStorage_HSequenceOfRoots",
"StdStorage_TypeData"
]
class StdStorage():
    """
    StdStorage package is used to write and read persistent objects. These objects are read and written by a retrieval or storage algorithm (compatible with legacy Storage_Schema) in a container (disk, memory, network ...). Drivers (FSD_File objects) assign a physical container for data to be stored or retrieved. The standard procedure for an application in reading a container is to call one of the Read functions providing either a file path or a driver opened for reading. Thes function update the instance of the StdStorage_Data class which contains the data being read. The standard procedure for an application in writing a container is the following: - open the driver in writing mode, - create an instance of the StdStorage_Data class, then add the persistent data to write with the function AddRoot, - call the function Write from the storage, setting the driver and the Storage_Data instance as parameters, - close the driver.
    """
    @staticmethod
    @overload
    def Read_s(theDriver : OCP.Storage.Storage_BaseDriver,theData : StdStorage_Data) -> OCP.Storage.Storage_Error: 
        """
        Returns the data read from a file located at theFileName. The storage format is compartible with legacy persistent one. These data are aggregated in a StdStorage_Data object which may be browsed in order to extract the root objects from the container. Note: - theData object will be created if it is null or cleared otherwise.

        Returns the data read from the container defined by theDriver. The storage format is compartible with legacy persistent one. These data are aggregated in a StdStorage_Data object which may be browsed in order to extract the root objects from the container. Note: - theData object will be created if it is null or cleared otherwise.
        """
    @staticmethod
    @overload
    def Read_s(theFileName : OCP.TCollection.TCollection_AsciiString,theData : StdStorage_Data) -> OCP.Storage.Storage_Error: ...
    @staticmethod
    def Version_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the version of Storage's read/write routines
        """
    @staticmethod
    def Write_s(theDriver : OCP.Storage.Storage_BaseDriver,theData : StdStorage_Data) -> OCP.Storage.Storage_Error: 
        """
        Writes the data aggregated in theData object into the container defined by theDriver. The storage format is compartible with legacy persistent one. Note: - theData may aggregate several root objects to be stored together. - createion date specified in the srorage header will be overwritten.
        """
    def __init__(self) -> None: ...
    pass
class StdStorage_BucketIterator():
    def More(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StdObjMgt.StdObjMgt_Persistent: 
        """
        None
        """
    pass
class StdStorage_Data(OCP.Standard.Standard_Transient):
    """
    A picture memorizing the stored in a container (for example, in a file). A StdStorage_Data object represents either: - persistent data to be written into a container, or - persistent data which are read from a container. A StdStorage_Data object is used in both the storage and retrieval operations: - Storage mechanism: create an empty StdStorage_Data object, then add successively persistent objects (roots) to be stored using the StdStorage_RootData's function AddRoot. When the set of data is complete, write it to a container using the function Write in your StdStorage algorithm. - Retrieval mechanism: a StdStorage_Data object is returned by the Read function from your StdStorage algorithm. Use the StdStorage_RootData's functions NumberOfRoots and Roots to find the roots which were stored in the read container. The roots of a StdStorage_Data object may share references on objects. The shared internal references of a StdStorage_Data object are maintained by the storage/retrieval mechanism. Note: References shared by objects which are contained in two distinct StdStorage_Data objects are not maintained by the storage/retrieval mechanism: external references are not supported by Storage_Schema algorithm
    """
    def Clear(self) -> None: 
        """
        Makes the container empty
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
        Returns a type descriptor about this object.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HeaderData(self) -> StdStorage_HeaderData: 
        """
        Returns the header data section
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
    def RootData(self) -> StdStorage_RootData: 
        """
        Returns the root data section
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeData(self) -> StdStorage_TypeData: 
        """
        Returns the type data section
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        Returns type descriptor of Standard_Transient class
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StdStorage_SequenceOfRoots(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StdStorage_Root) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : StdStorage_SequenceOfRoots) -> None: ...
    def Assign(self,theOther : StdStorage_SequenceOfRoots) -> StdStorage_SequenceOfRoots: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StdStorage_Root: 
        """
        First item access
        """
    def ChangeLast(self) -> StdStorage_Root: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StdStorage_Root: 
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
    def First(self) -> StdStorage_Root: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StdStorage_Root) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StdStorage_SequenceOfRoots) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StdStorage_Root) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StdStorage_SequenceOfRoots) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StdStorage_Root: 
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
    def Prepend(self,theItem : StdStorage_Root) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StdStorage_SequenceOfRoots) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StdStorage_Root) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StdStorage_SequenceOfRoots) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StdStorage_Root: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : StdStorage_SequenceOfRoots) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StdStorage_HeaderData(OCP.Standard.Standard_Transient):
    """
    Storage header data section that contains some auxiliary information (application name, schema version, creation date, comments and so on...)Storage header data section that contains some auxiliary information (application name, schema version, creation date, comments and so on...)Storage header data section that contains some auxiliary information (application name, schema version, creation date, comments and so on...)
    """
    def AddToComments(self,aComment : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Add <theUserInfo> to the user information
        """
    def AddToUserInfo(self,theUserInfo : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Add <theUserInfo> to the user information
        """
    def ApplicationName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Get the name of the application
        """
    def ApplicationVersion(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Get the version of the application
        """
    def ClearErrorStatus(self) -> None: 
        """
        Clears error status
        """
    def Comments(self) -> OCP.TColStd.TColStd_SequenceOfExtendedString: 
        """
        Return the user information
        """
    def CreationDate(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return the creation date
        """
    def DataType(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns data type
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
    def ErrorStatus(self) -> OCP.Storage.Storage_Error: 
        """
        Returns a status of the latest call to Read / Write functions
        """
    def ErrorStatusExtension(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an error message if any of the latest call to Read / Write functions
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
    def NumberOfObjects(self) -> int: 
        """
        Returns the number of persistent objects
        """
    def Read(self,theDriver : OCP.Storage.Storage_BaseDriver) -> bool: 
        """
        Reads the header data section from the container defined by theDriver. Returns Standard_True in case of success. Otherwise, one need to get an error code and description using ErrorStatus and ErrorStatusExtension functions correspondingly.
        """
    def SchemaVersion(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Get the version of the schema
        """
    def SetApplicationName(self,aName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Set the name of the application
        """
    def SetApplicationVersion(self,aVersion : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Set the version of the application
        """
    def SetCreationDate(self,aDate : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetDataType(self,aType : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Set the data type
        """
    def SetNumberOfObjects(self,anObjectNumber : int) -> None: 
        """
        None
        """
    def SetSchemaName(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetSchemaVersion(self,aVersion : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetStorageVersion(self,aVersion : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def StorageVersion(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return the Storage package version
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UserInfo(self) -> OCP.TColStd.TColStd_SequenceOfAsciiString: 
        """
        Return the user information
        """
    def Write(self,theDriver : OCP.Storage.Storage_BaseDriver) -> bool: 
        """
        Writes the header data section to the container defined by theDriver. Returns Standard_True in case of success. Otherwise, one need to get an error code and description using ErrorStatus and ErrorStatusExtension functions correspondingly.
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
class StdStorage_Root(OCP.Standard.Standard_Transient):
    """
    Describes a named persistent rootDescribes a named persistent root
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
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a name of the root
        """
    def Object(self) -> OCP.StdObjMgt.StdObjMgt_Persistent: 
        """
        Returns a root's persistent object
        """
    def Reference(self) -> int: 
        """
        Returns root's position in the root data section
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets a name to the root object
        """
    def SetObject(self,anObject : OCP.StdObjMgt.StdObjMgt_Persistent) -> None: 
        """
        Sets a root's persistent object
        """
    def SetType(self,aType : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets a root's persistent type
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a root's persistent type
        """
    @overload
    def __init__(self,theName : OCP.TCollection.TCollection_AsciiString,theObject : OCP.StdObjMgt.StdObjMgt_Persistent) -> None: ...
    @overload
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
class StdStorage_RootData(OCP.Standard.Standard_Transient):
    """
    Storage root data section contains root persistent objectsStorage root data section contains root persistent objectsStorage root data section contains root persistent objects
    """
    def AddRoot(self,aRoot : StdStorage_Root) -> None: 
        """
        Add a root to <me>. If a root with same name is present, it will be replaced by <aRoot>.
        """
    def Clear(self) -> None: 
        """
        Removes all persistent root objects
        """
    def ClearErrorStatus(self) -> None: 
        """
        Clears error status
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
    def ErrorStatus(self) -> OCP.Storage.Storage_Error: 
        """
        Returns a status of the latest call to Read / Write functions
        """
    def ErrorStatusExtension(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an error message if any of the latest call to Read / Write functions
        """
    def Find(self,aName : OCP.TCollection.TCollection_AsciiString) -> StdStorage_Root: 
        """
        Finds a root with name <aName>.
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
    def IsRoot(self,aName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Returns Standard_True if <me> contains a root named <aName>
        """
    def NumberOfRoots(self) -> int: 
        """
        Returns the number of roots.
        """
    def Read(self,theDriver : OCP.Storage.Storage_BaseDriver) -> bool: 
        """
        Reads the root data section from the container defined by theDriver. Returns Standard_True in case of success. Otherwise, one need to get an error code and description using ErrorStatus and ErrorStatusExtension functions correspondingly.
        """
    def RemoveRoot(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Removes the root named <aName>.
        """
    def Roots(self) -> StdStorage_HSequenceOfRoots: 
        """
        Returns a sequence of all roots
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Write(self,theDriver : OCP.Storage.Storage_BaseDriver) -> bool: 
        """
        Writes the root data section to the container defined by theDriver. Returns Standard_True in case of success. Otherwise, one need to get an error code and description using ErrorStatus and ErrorStatusExtension functions correspondingly.
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
class StdStorage_HSequenceOfRoots(StdStorage_SequenceOfRoots, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : StdStorage_SequenceOfRoots) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : StdStorage_Root) -> None: ...
    def Assign(self,theOther : StdStorage_SequenceOfRoots) -> StdStorage_SequenceOfRoots: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StdStorage_Root: 
        """
        First item access
        """
    def ChangeLast(self) -> StdStorage_Root: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StdStorage_SequenceOfRoots: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StdStorage_Root: 
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
    def First(self) -> StdStorage_Root: 
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
    def InsertAfter(self,theIndex : int,theItem : StdStorage_Root) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StdStorage_SequenceOfRoots) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StdStorage_Root) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StdStorage_SequenceOfRoots) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> StdStorage_Root: 
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
    def Prepend(self,theItem : StdStorage_Root) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StdStorage_SequenceOfRoots) -> None: ...
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
    def Sequence(self) -> StdStorage_SequenceOfRoots: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StdStorage_Root) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StdStorage_SequenceOfRoots) -> None: 
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
    def Value(self,theIndex : int) -> StdStorage_Root: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StdStorage_SequenceOfRoots) -> None: ...
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
class StdStorage_TypeData(OCP.Standard.Standard_Transient):
    """
    Storage type data section keeps association between persistent textual types and their numbersStorage type data section keeps association between persistent textual types and their numbersStorage type data section keeps association between persistent textual types and their numbers
    """
    @overload
    def AddType(self,aPObj : OCP.StdObjMgt.StdObjMgt_Persistent) -> int: 
        """
        Add a type to the list in case of reading data

        Add a type of the persistent object in case of writing data
        """
    @overload
    def AddType(self,aTypeName : OCP.TCollection.TCollection_AsciiString,aTypeNum : int) -> None: ...
    def Clear(self) -> None: 
        """
        Unregisters all types
        """
    def ClearErrorStatus(self) -> None: 
        """
        Clears error status
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
    def ErrorStatus(self) -> OCP.Storage.Storage_Error: 
        """
        Returns a status of the latest call to Read / Write functions
        """
    def ErrorStatusExtension(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an error message if any of the latest call to Read / Write functions
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
    def IsType(self,aName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Checks if <aName> is a registered type
        """
    def NumberOfTypes(self) -> int: 
        """
        Returns the number of registered types
        """
    def Read(self,theDriver : OCP.Storage.Storage_BaseDriver) -> bool: 
        """
        Reads the type data section from the container defined by theDriver. Returns Standard_True in case of success. Otherwise, one need to get an error code and description using ErrorStatus and ErrorStatusExtension functions correspondingly.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Type(self,aTypeNum : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the type with number <aTypeNum>

        Returns the name of the type with number <aTypeNum>
        """
    @overload
    def Type(self,aTypeName : OCP.TCollection.TCollection_AsciiString) -> int: ...
    def Types(self) -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        Returns a sequence of all registered types
        """
    def Write(self,theDriver : OCP.Storage.Storage_BaseDriver) -> bool: 
        """
        Writes the type data section to the container defined by theDriver. Returns Standard_True in case of success. Otherwise, one need to get an error code and description using ErrorStatus and ErrorStatusExtension functions correspondingly.
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
