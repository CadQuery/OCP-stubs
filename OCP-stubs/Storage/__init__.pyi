import OCP.Storage
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TColStd
import OCP.Standard
import OCP.TCollection
__all__  = [
"Storage",
"Storage_ArrayOfCallBack",
"Storage_ArrayOfSchema",
"Storage_BaseDriver",
"Storage_BucketIterator",
"Storage_CallBack",
"Storage_Data",
"Storage_DefaultCallBack",
"Storage_Error",
"Storage_HArrayOfCallBack",
"Storage_HArrayOfSchema",
"Storage_PArray",
"Storage_SeqOfRoot",
"Storage_HeaderData",
"Storage_InternalData",
"Storage_OpenMode",
"Storage_HPArray",
"Storage_PType",
"Storage_Root",
"Storage_RootData",
"Storage_Schema",
"Storage_HSeqOfRoot",
"Storage_SolveMode",
"Storage_StreamFormatError",
"Storage_StreamModeError",
"Storage_StreamReadError",
"Storage_StreamWriteError",
"Storage_TypeData",
"Storage_TypedCallBack",
"Storage_AddSolve",
"Storage_ReadSolve",
"Storage_VSAlreadyOpen",
"Storage_VSCloseError",
"Storage_VSExtCharParityError",
"Storage_VSFormatError",
"Storage_VSInternalError",
"Storage_VSModeError",
"Storage_VSNone",
"Storage_VSNotOpen",
"Storage_VSOk",
"Storage_VSOpenError",
"Storage_VSRead",
"Storage_VSReadWrite",
"Storage_VSSectionNotFound",
"Storage_VSTypeMismatch",
"Storage_VSUnknownType",
"Storage_VSWrite",
"Storage_VSWriteError",
"Storage_VSWrongFileDriver",
"Storage_WriteSolve"
]
class Storage():
    """
    Storage package is used to write and read persistent objects. These objects are read and written by a retrieval or storage algorithm (Storage_Schema object) in a container (disk, memory, network ...). Drivers (FSD_File objects) assign a physical container for data to be stored or retrieved. The standard procedure for an application in reading a container is the following: - open the driver in reading mode, - call the Read function from the schema, setting the driver as a parameter. This function returns an instance of the Storage_Data class which contains the data being read, - close the driver. The standard procedure for an application in writing a container is the following: - open the driver in writing mode, - create an instance of the Storage_Data class, then add the persistent data to write with the function AddRoot, - call the function Write from the schema, setting the driver and the Storage_Data instance as parameters, - close the driver.
    """
    @staticmethod
    def Version_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns the version of Storage's read/write routines
        """
    def __init__(self) -> None: ...
    pass
class Storage_ArrayOfCallBack():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Storage_ArrayOfCallBack) -> Storage_ArrayOfCallBack: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Storage_CallBack: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Storage_CallBack: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Storage_CallBack: 
        """
        Variable value access
        """
    def First(self) -> Storage_CallBack: 
        """
        Returns first element
        """
    def Init(self,theValue : Storage_CallBack) -> None: 
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
    def Last(self) -> Storage_CallBack: 
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
    def Move(self,theOther : Storage_ArrayOfCallBack) -> Storage_ArrayOfCallBack: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Storage_CallBack) -> None: 
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
    def Value(self,theIndex : int) -> Storage_CallBack: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : Storage_CallBack,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Storage_ArrayOfCallBack) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Storage_ArrayOfSchema():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Storage_ArrayOfSchema) -> Storage_ArrayOfSchema: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Storage_Schema: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Storage_Schema: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Storage_Schema: 
        """
        Variable value access
        """
    def First(self) -> Storage_Schema: 
        """
        Returns first element
        """
    def Init(self,theValue : Storage_Schema) -> None: 
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
    def Last(self) -> Storage_Schema: 
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
    def Move(self,theOther : Storage_ArrayOfSchema) -> Storage_ArrayOfSchema: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Storage_Schema) -> None: 
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
    def Value(self,theIndex : int) -> Storage_Schema: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Storage_ArrayOfSchema) -> None: ...
    @overload
    def __init__(self,theBegin : Storage_Schema,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Storage_BaseDriver():
    """
    Root class for drivers. A driver assigns a physical container to data to be stored or retrieved, for instance a file. The FSD package provides two derived concrete classes : - FSD_File is a general driver which defines a file as the container of data.
    """
    def BeginReadCommentSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginReadDataSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginReadInfoSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginReadObjectData(self) -> None: 
        """
        None
        """
    def BeginReadPersistentObjectData(self) -> None: 
        """
        None
        """
    def BeginReadRefSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginReadRootSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginReadTypeSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginWriteCommentSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginWriteDataSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginWriteInfoSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginWriteObjectData(self) -> None: 
        """
        None
        """
    def BeginWritePersistentObjectData(self) -> None: 
        """
        None
        """
    def BeginWriteRefSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginWriteRootSection(self) -> Storage_Error: 
        """
        None
        """
    def BeginWriteTypeSection(self) -> Storage_Error: 
        """
        None
        """
    def Close(self) -> Storage_Error: 
        """
        None
        """
    def EndReadCommentSection(self) -> Storage_Error: 
        """
        None
        """
    def EndReadDataSection(self) -> Storage_Error: 
        """
        None
        """
    def EndReadInfoSection(self) -> Storage_Error: 
        """
        None
        """
    def EndReadObjectData(self) -> None: 
        """
        None
        """
    def EndReadPersistentObjectData(self) -> None: 
        """
        None
        """
    def EndReadRefSection(self) -> Storage_Error: 
        """
        None
        """
    def EndReadRootSection(self) -> Storage_Error: 
        """
        None
        """
    def EndReadTypeSection(self) -> Storage_Error: 
        """
        None
        """
    def EndWriteCommentSection(self) -> Storage_Error: 
        """
        None
        """
    def EndWriteDataSection(self) -> Storage_Error: 
        """
        None
        """
    def EndWriteInfoSection(self) -> Storage_Error: 
        """
        None
        """
    def EndWriteObjectData(self) -> None: 
        """
        None
        """
    def EndWritePersistentObjectData(self) -> None: 
        """
        None
        """
    def EndWriteRefSection(self) -> Storage_Error: 
        """
        None
        """
    def EndWriteRootSection(self) -> Storage_Error: 
        """
        None
        """
    def EndWriteTypeSection(self) -> Storage_Error: 
        """
        None
        """
    def GetBoolean(self,aValue : bool) -> Storage_BaseDriver: 
        """
        None
        """
    def GetCharacter(self,aValue : str) -> Storage_BaseDriver: 
        """
        None
        """
    def GetExtCharacter(self,aValue : str) -> Storage_BaseDriver: 
        """
        None
        """
    def GetInteger(self,aValue : int) -> Storage_BaseDriver: 
        """
        None
        """
    def GetReal(self,aValue : float) -> Storage_BaseDriver: 
        """
        None
        """
    def GetReference(self,aValue : int) -> Storage_BaseDriver: 
        """
        None
        """
    def GetShortReal(self,aValue : float) -> Storage_BaseDriver: 
        """
        None
        """
    def IsEnd(self) -> bool: 
        """
        returns True if we are at end of the stream
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    def Open(self,aName : OCP.TCollection.TCollection_AsciiString,aMode : Storage_OpenMode) -> Storage_Error: 
        """
        None
        """
    def OpenMode(self) -> Storage_OpenMode: 
        """
        None

        None
        """
    def PutBoolean(self,aValue : bool) -> Storage_BaseDriver: 
        """
        None
        """
    def PutCharacter(self,aValue : str) -> Storage_BaseDriver: 
        """
        None
        """
    def PutExtCharacter(self,aValue : str) -> Storage_BaseDriver: 
        """
        None
        """
    def PutInteger(self,aValue : int) -> Storage_BaseDriver: 
        """
        None
        """
    def PutReal(self,aValue : float) -> Storage_BaseDriver: 
        """
        None
        """
    def PutReference(self,aValue : int) -> Storage_BaseDriver: 
        """
        None
        """
    def PutShortReal(self,aValue : float) -> Storage_BaseDriver: 
        """
        None
        """
    def ReadComment(self,userComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        None
        """
    def ReadCompleteInfo(self,theIStream : Any,theData : Storage_Data) -> Any: 
        """
        None
        """
    def ReadInfo(self,dbVersion : OCP.TCollection.TCollection_AsciiString,date : OCP.TCollection.TCollection_AsciiString,schemaName : OCP.TCollection.TCollection_AsciiString,schemaVersion : OCP.TCollection.TCollection_AsciiString,appName : OCP.TCollection.TCollection_ExtendedString,appVersion : OCP.TCollection.TCollection_AsciiString,objectType : OCP.TCollection.TCollection_ExtendedString,userInfo : OCP.TColStd.TColStd_SequenceOfAsciiString) -> Tuple[int]: 
        """
        None
        """
    @staticmethod
    def ReadMagicNumber_s(theIStream : Any) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def ReadPersistentObjectHeader(self) -> Tuple[int, int]: 
        """
        None
        """
    def ReadReferenceType(self) -> Tuple[int, int]: 
        """
        None
        """
    def ReadRoot(self,rootName : OCP.TCollection.TCollection_AsciiString,aType : OCP.TCollection.TCollection_AsciiString) -> Tuple[int]: 
        """
        None
        """
    def ReadTypeInformations(self,typeName : OCP.TCollection.TCollection_AsciiString) -> Tuple[int]: 
        """
        None
        """
    def RefSectionSize(self) -> int: 
        """
        None
        """
    def RootSectionSize(self) -> int: 
        """
        None
        """
    def SetRefSectionSize(self,aSize : int) -> None: 
        """
        None
        """
    def SetRootSectionSize(self,aSize : int) -> None: 
        """
        None
        """
    def SetTypeSectionSize(self,aSize : int) -> None: 
        """
        None
        """
    def SkipObject(self) -> None: 
        """
        None
        """
    def Tell(self) -> int: 
        """
        return position in the file. Return -1 upon error.
        """
    def TypeSectionSize(self) -> int: 
        """
        None
        """
    def WriteComment(self,userComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        None
        """
    def WriteInfo(self,nbObj : int,dbVersion : OCP.TCollection.TCollection_AsciiString,date : OCP.TCollection.TCollection_AsciiString,schemaName : OCP.TCollection.TCollection_AsciiString,schemaVersion : OCP.TCollection.TCollection_AsciiString,appName : OCP.TCollection.TCollection_ExtendedString,appVersion : OCP.TCollection.TCollection_AsciiString,objectType : OCP.TCollection.TCollection_ExtendedString,userInfo : OCP.TColStd.TColStd_SequenceOfAsciiString) -> None: 
        """
        None
        """
    def WritePersistentObjectHeader(self,aRef : int,aType : int) -> None: 
        """
        None
        """
    def WriteReferenceType(self,reference : int,typeNum : int) -> None: 
        """
        None
        """
    def WriteRoot(self,rootName : OCP.TCollection.TCollection_AsciiString,aRef : int,aType : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def WriteTypeInformations(self,typeNum : int,typeName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    pass
class Storage_BucketIterator():
    def Init(self,arg1 : Storage_BucketOfPersistent) -> None: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def Reset(self) -> None: 
        """
        None
        """
    def Value(self) -> OCP.Standard.Standard_Persistent: 
        """
        None
        """
    def __init__(self,arg1 : Storage_BucketOfPersistent) -> None: ...
    pass
class Storage_CallBack(OCP.Standard.Standard_Transient):
    def Add(self,aPers : OCP.Standard.Standard_Persistent,aSchema : Storage_Schema) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def New(self) -> OCP.Standard.Standard_Persistent: 
        """
        None
        """
    def Read(self,aPers : OCP.Standard.Standard_Persistent,aDriver : Storage_BaseDriver,aSchema : Storage_Schema) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Write(self,aPers : OCP.Standard.Standard_Persistent,aDriver : Storage_BaseDriver,aSchema : Storage_Schema) -> None: 
        """
        None
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
class Storage_Data(OCP.Standard.Standard_Transient):
    """
    A picture memorizing the data stored in a container (for example, in a file). A Storage_Data object represents either: - persistent data to be written into a container, or - persistent data which are read from a container. A Storage_Data object is used in both the storage and retrieval operations: - Storage mechanism: create an empty Storage_Data object, then add successively persistent objects (roots) to be stored using the function AddRoot. When the set of data is complete, write it to a container using the function Write in your Storage_Schema storage/retrieval algorithm. - Retrieval mechanism: a Storage_Data object is returned by the Read function from your Storage_Schema storage/retrieval algorithm. Use the functions NumberOfRoots and Roots to find the roots which were stored in the read container. The roots of a Storage_Data object may share references on objects. The shared internal references of a Storage_Data object are maintained by the storage/retrieval mechanism. Note: References shared by objects which are contained in two distinct Storage_Data objects are not maintained by the storage/retrieval mechanism: external references are not supported by Storage_Schema algorithmA picture memorizing the data stored in a container (for example, in a file). A Storage_Data object represents either: - persistent data to be written into a container, or - persistent data which are read from a container. A Storage_Data object is used in both the storage and retrieval operations: - Storage mechanism: create an empty Storage_Data object, then add successively persistent objects (roots) to be stored using the function AddRoot. When the set of data is complete, write it to a container using the function Write in your Storage_Schema storage/retrieval algorithm. - Retrieval mechanism: a Storage_Data object is returned by the Read function from your Storage_Schema storage/retrieval algorithm. Use the functions NumberOfRoots and Roots to find the roots which were stored in the read container. The roots of a Storage_Data object may share references on objects. The shared internal references of a Storage_Data object are maintained by the storage/retrieval mechanism. Note: References shared by objects which are contained in two distinct Storage_Data objects are not maintained by the storage/retrieval mechanism: external references are not supported by Storage_Schema algorithmA picture memorizing the data stored in a container (for example, in a file). A Storage_Data object represents either: - persistent data to be written into a container, or - persistent data which are read from a container. A Storage_Data object is used in both the storage and retrieval operations: - Storage mechanism: create an empty Storage_Data object, then add successively persistent objects (roots) to be stored using the function AddRoot. When the set of data is complete, write it to a container using the function Write in your Storage_Schema storage/retrieval algorithm. - Retrieval mechanism: a Storage_Data object is returned by the Read function from your Storage_Schema storage/retrieval algorithm. Use the functions NumberOfRoots and Roots to find the roots which were stored in the read container. The roots of a Storage_Data object may share references on objects. The shared internal references of a Storage_Data object are maintained by the storage/retrieval mechanism. Note: References shared by objects which are contained in two distinct Storage_Data objects are not maintained by the storage/retrieval mechanism: external references are not supported by Storage_Schema algorithm
    """
    @overload
    def AddRoot(self,anObject : OCP.Standard.Standard_Persistent) -> None: 
        """
        add a persistent root to write. the name of the root is a driver reference number.

        Adds the root anObject to this set of data. The name of the root is aName if given; if not, it will be a reference number assigned by the driver when writing the set of data into the container. When naming the roots, it is easier to retrieve objects by significant references rather than by references without any semantic values.
        """
    @overload
    def AddRoot(self,aName : OCP.TCollection.TCollection_AsciiString,anObject : OCP.Standard.Standard_Persistent) -> None: ...
    def AddToComments(self,aComment : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        add <theUserInfo> to the user informations
        """
    def AddToUserInfo(self,anInfo : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        add <theUserInfo> to the user informations
        """
    def ApplicationName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        get the name of the application
        """
    def ApplicationVersion(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        get the version of the application
        """
    def Clear(self) -> None: 
        """
        None
        """
    def ClearErrorStatus(self) -> None: 
        """
        Clears the error status positioned either by: - the last storage operation performed with the Read function, or - the last retrieval operation performed with the Write function by a Storage_Schema algorithm, on this set of data. This error status may be read by the function ErrorStatus.
        """
    def Comments(self) -> OCP.TColStd.TColStd_SequenceOfExtendedString: 
        """
        return the user informations
        """
    def CreationDate(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        return the creation date
        """
    def DataType(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        returns data type
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
    def ErrorStatus(self) -> Storage_Error: 
        """
        Returns Storage_VSOk if - the last storage operation performed with the function Read, or - the last retrieval operation performed with the function Write by a Storage_Schema algorithm, on this set of data was successful. If the storage or retrieval operation was not performed, the returned error status indicates the reason why the operation failed. The algorithm stops its analysis at the first detected error
        """
    def ErrorStatusExtension(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def Find(self,aName : OCP.TCollection.TCollection_AsciiString) -> Storage_Root: 
        """
        Gives the root object whose name is aName in this set of data. The returned object is a Storage_Root object, from which the object it encapsulates may be extracted. Warning A null handle is returned if there is no root object whose name is aName in this set of data.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HeaderData(self) -> Storage_HeaderData: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InternalData(self) -> Storage_InternalData: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsRoot(self,aName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        returns Standard_True if <me> contains a root named <aName>
        """
    def IsType(self,aName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Returns true if this set of data contains an object of type aName. Persistent objects from this set of data must have types which are recognized by the Storage_Schema algorithm used to store or retrieve them.
        """
    def NumberOfObjects(self) -> int: 
        """
        the the number of persistent objects Return: the number of persistent objects readed
        """
    def NumberOfRoots(self) -> int: 
        """
        Returns the number of root objects in this set of data. - When preparing a storage operation, the result is the number of roots inserted into this set of data with the function AddRoot. - When retrieving an object, the result is the number of roots stored in the read container. Use the Roots function to get these roots in a sequence.
        """
    def NumberOfTypes(self) -> int: 
        """
        Returns the number of types of objects used in this set of data.
        """
    def RemoveRoot(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Removes from this set of data the root object named aName. Warning Nothing is done if there is no root object whose name is aName in this set of data.
        """
    def RootData(self) -> Storage_RootData: 
        """
        None
        """
    def Roots(self) -> Storage_HSeqOfRoot: 
        """
        Returns the roots of this set of data in a sequence. - When preparing a storage operation, the sequence contains the roots inserted into this set of data with the function AddRoot. - When retrieving an object, the sequence contains the roots stored in the container read. - An empty sequence is returned if there is no root in this set of data.
        """
    def SchemaName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        get the schema's name
        """
    def SchemaVersion(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        get the version of the schema
        """
    def SetApplicationName(self,aName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        set the name of the application
        """
    def SetApplicationVersion(self,aVersion : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        set the version of the application
        """
    def SetDataType(self,aType : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        set the data type
        """
    def StorageVersion(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        return the Storage package version
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeData(self) -> Storage_TypeData: 
        """
        None
        """
    def Types(self) -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        Gives the list of types of objects used in this set of data in a sequence.
        """
    def UserInfo(self) -> OCP.TColStd.TColStd_SequenceOfAsciiString: 
        """
        return the user informations
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
class Storage_DefaultCallBack(Storage_CallBack, OCP.Standard.Standard_Transient):
    def Add(self,aPers : OCP.Standard.Standard_Persistent,aSchema : Storage_Schema) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def New(self) -> OCP.Standard.Standard_Persistent: 
        """
        None
        """
    def Read(self,aPers : OCP.Standard.Standard_Persistent,aDriver : Storage_BaseDriver,aSchema : Storage_Schema) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Write(self,aPers : OCP.Standard.Standard_Persistent,aDriver : Storage_BaseDriver,aSchema : Storage_Schema) -> None: 
        """
        None
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
class Storage_Error():
    """
    Error codes returned by the ErrorStatus function on a Storage_Data set of data during a storage or retrieval operation : - Storage_VSOk : no problem has been detected - Storage_VSOpenError : an error has occurred when opening the driver - Storage_VSModeError : the driver has not been opened in the correct mode - Storage_VSCloseError : an error has occurred when closing the driver - Storage_VSAlreadyOpen : the driver is already open - Storage_VSNotOpen : the driver is not open - Storage_VSSectionNotFound : a section has not been found in the driver - Storage_VSWriteError : an error occurred when writing the driver - Storage_VSFormatError : the file format is wrong - Storage_VSUnknownType : a type is not known from the schema - Storage_VSTypeMismatch : trying to read a wrong type - Storage_VSInternalError : an internal error has been detected - Storage_VSExtCharParityError : an error has occurred while reading 16 bit characte

    Members:

      Storage_VSOk

      Storage_VSOpenError

      Storage_VSModeError

      Storage_VSCloseError

      Storage_VSAlreadyOpen

      Storage_VSNotOpen

      Storage_VSSectionNotFound

      Storage_VSWriteError

      Storage_VSFormatError

      Storage_VSUnknownType

      Storage_VSTypeMismatch

      Storage_VSInternalError

      Storage_VSExtCharParityError

      Storage_VSWrongFileDriver
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Storage_VSAlreadyOpen: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSAlreadyOpen
    Storage_VSCloseError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSCloseError
    Storage_VSExtCharParityError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSExtCharParityError
    Storage_VSFormatError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSFormatError
    Storage_VSInternalError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSInternalError
    Storage_VSModeError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSModeError
    Storage_VSNotOpen: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSNotOpen
    Storage_VSOk: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSOk
    Storage_VSOpenError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSOpenError
    Storage_VSSectionNotFound: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSSectionNotFound
    Storage_VSTypeMismatch: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSTypeMismatch
    Storage_VSUnknownType: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSUnknownType
    Storage_VSWriteError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSWriteError
    Storage_VSWrongFileDriver: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSWrongFileDriver
    __entries: dict # value = {'Storage_VSOk': (Storage_Error.Storage_VSOk, None), 'Storage_VSOpenError': (Storage_Error.Storage_VSOpenError, None), 'Storage_VSModeError': (Storage_Error.Storage_VSModeError, None), 'Storage_VSCloseError': (Storage_Error.Storage_VSCloseError, None), 'Storage_VSAlreadyOpen': (Storage_Error.Storage_VSAlreadyOpen, None), 'Storage_VSNotOpen': (Storage_Error.Storage_VSNotOpen, None), 'Storage_VSSectionNotFound': (Storage_Error.Storage_VSSectionNotFound, None), 'Storage_VSWriteError': (Storage_Error.Storage_VSWriteError, None), 'Storage_VSFormatError': (Storage_Error.Storage_VSFormatError, None), 'Storage_VSUnknownType': (Storage_Error.Storage_VSUnknownType, None), 'Storage_VSTypeMismatch': (Storage_Error.Storage_VSTypeMismatch, None), 'Storage_VSInternalError': (Storage_Error.Storage_VSInternalError, None), 'Storage_VSExtCharParityError': (Storage_Error.Storage_VSExtCharParityError, None), 'Storage_VSWrongFileDriver': (Storage_Error.Storage_VSWrongFileDriver, None)}
    __members__: dict # value = {'Storage_VSOk': Storage_Error.Storage_VSOk, 'Storage_VSOpenError': Storage_Error.Storage_VSOpenError, 'Storage_VSModeError': Storage_Error.Storage_VSModeError, 'Storage_VSCloseError': Storage_Error.Storage_VSCloseError, 'Storage_VSAlreadyOpen': Storage_Error.Storage_VSAlreadyOpen, 'Storage_VSNotOpen': Storage_Error.Storage_VSNotOpen, 'Storage_VSSectionNotFound': Storage_Error.Storage_VSSectionNotFound, 'Storage_VSWriteError': Storage_Error.Storage_VSWriteError, 'Storage_VSFormatError': Storage_Error.Storage_VSFormatError, 'Storage_VSUnknownType': Storage_Error.Storage_VSUnknownType, 'Storage_VSTypeMismatch': Storage_Error.Storage_VSTypeMismatch, 'Storage_VSInternalError': Storage_Error.Storage_VSInternalError, 'Storage_VSExtCharParityError': Storage_Error.Storage_VSExtCharParityError, 'Storage_VSWrongFileDriver': Storage_Error.Storage_VSWrongFileDriver}
    pass
class Storage_HArrayOfCallBack(Storage_ArrayOfCallBack, OCP.Standard.Standard_Transient):
    def Array1(self) -> Storage_ArrayOfCallBack: 
        """
        None
        """
    def Assign(self,theOther : Storage_ArrayOfCallBack) -> Storage_ArrayOfCallBack: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Storage_ArrayOfCallBack: 
        """
        None
        """
    def ChangeFirst(self) -> Storage_CallBack: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Storage_CallBack: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Storage_CallBack: 
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
    def First(self) -> Storage_CallBack: 
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
    def Init(self,theValue : Storage_CallBack) -> None: 
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
    def Last(self) -> Storage_CallBack: 
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
    def Move(self,theOther : Storage_ArrayOfCallBack) -> Storage_ArrayOfCallBack: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Storage_CallBack) -> None: 
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
    def Value(self,theIndex : int) -> Storage_CallBack: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Storage_ArrayOfCallBack) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Storage_CallBack) -> None: ...
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
class Storage_HArrayOfSchema(Storage_ArrayOfSchema, OCP.Standard.Standard_Transient):
    def Array1(self) -> Storage_ArrayOfSchema: 
        """
        None
        """
    def Assign(self,theOther : Storage_ArrayOfSchema) -> Storage_ArrayOfSchema: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Storage_ArrayOfSchema: 
        """
        None
        """
    def ChangeFirst(self) -> Storage_Schema: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Storage_Schema: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Storage_Schema: 
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
    def First(self) -> Storage_Schema: 
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
    def Init(self,theValue : Storage_Schema) -> None: 
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
    def Last(self) -> Storage_Schema: 
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
    def Move(self,theOther : Storage_ArrayOfSchema) -> Storage_ArrayOfSchema: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Storage_Schema) -> None: 
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
    def Value(self,theIndex : int) -> Storage_Schema: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Storage_ArrayOfSchema) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Storage_Schema) -> None: ...
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
class Storage_PArray():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Storage_PArray) -> Storage_PArray: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.Standard.Standard_Persistent: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Standard.Standard_Persistent: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Standard.Standard_Persistent: 
        """
        Variable value access
        """
    def First(self) -> OCP.Standard.Standard_Persistent: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.Standard.Standard_Persistent) -> None: 
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
    def Last(self) -> OCP.Standard.Standard_Persistent: 
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
    def Move(self,theOther : Storage_PArray) -> Storage_PArray: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Standard.Standard_Persistent) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Standard.Standard_Persistent: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Storage_PArray) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.Standard.Standard_Persistent,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Storage_SeqOfRoot(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Storage_Root) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Storage_SeqOfRoot) -> None: ...
    def Assign(self,theOther : Storage_SeqOfRoot) -> Storage_SeqOfRoot: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Storage_Root: 
        """
        First item access
        """
    def ChangeLast(self) -> Storage_Root: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Storage_Root: 
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
    def First(self) -> Storage_Root: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Storage_Root) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Storage_SeqOfRoot) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Storage_SeqOfRoot) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Storage_Root) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Storage_Root: 
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
    def Prepend(self,theItem : Storage_Root) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Storage_SeqOfRoot) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Storage_Root) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Storage_SeqOfRoot) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Storage_Root: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Storage_SeqOfRoot) -> None: ...
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
class Storage_HeaderData(OCP.Standard.Standard_Transient):
    def AddToComments(self,aComment : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        add <theUserInfo> to the user informations
        """
    def AddToUserInfo(self,theUserInfo : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        add <theUserInfo> to the user informations
        """
    def ApplicationName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        get the name of the application
        """
    def ApplicationVersion(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        get the version of the application
        """
    def ClearErrorStatus(self) -> None: 
        """
        None
        """
    def Comments(self) -> OCP.TColStd.TColStd_SequenceOfExtendedString: 
        """
        return the user informations
        """
    def CreationDate(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        return the creation date
        """
    def DataType(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        returns data type
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
    def ErrorStatus(self) -> Storage_Error: 
        """
        None
        """
    def ErrorStatusExtension(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NumberOfObjects(self) -> int: 
        """
        the the number of persistent objects Return: the number of persistent objects readed
        """
    def Read(self,theDriver : Storage_BaseDriver) -> bool: 
        """
        None
        """
    def SchemaName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        get the schema's name
        """
    def SchemaVersion(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        get the version of the schema
        """
    def SetApplicationName(self,aName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        set the name of the application
        """
    def SetApplicationVersion(self,aVersion : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        set the version of the application
        """
    def SetCreationDate(self,aDate : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetDataType(self,aType : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        set the data type
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
        return the Storage package version
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UserInfo(self) -> OCP.TColStd.TColStd_SequenceOfAsciiString: 
        """
        return the user informations
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
class Storage_InternalData(OCP.Standard.Standard_Transient):
    def Clear(self) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def ReadArray(self) -> Storage_HPArray: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class Storage_OpenMode():
    """
    Specifies opening modes for a file: - Storage_VSNone : no mode is specified - Storage_VSRead : the file is open for reading operations - Storage_VSWrite : the file is open for writing operations - Storage_VSReadWrite : the file is open for both reading and writing operations.

    Members:

      Storage_VSNone

      Storage_VSRead

      Storage_VSWrite

      Storage_VSReadWrite
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Storage_VSNone: OCP.Storage.Storage_OpenMode # value = Storage_OpenMode.Storage_VSNone
    Storage_VSRead: OCP.Storage.Storage_OpenMode # value = Storage_OpenMode.Storage_VSRead
    Storage_VSReadWrite: OCP.Storage.Storage_OpenMode # value = Storage_OpenMode.Storage_VSReadWrite
    Storage_VSWrite: OCP.Storage.Storage_OpenMode # value = Storage_OpenMode.Storage_VSWrite
    __entries: dict # value = {'Storage_VSNone': (Storage_OpenMode.Storage_VSNone, None), 'Storage_VSRead': (Storage_OpenMode.Storage_VSRead, None), 'Storage_VSWrite': (Storage_OpenMode.Storage_VSWrite, None), 'Storage_VSReadWrite': (Storage_OpenMode.Storage_VSReadWrite, None)}
    __members__: dict # value = {'Storage_VSNone': Storage_OpenMode.Storage_VSNone, 'Storage_VSRead': Storage_OpenMode.Storage_VSRead, 'Storage_VSWrite': Storage_OpenMode.Storage_VSWrite, 'Storage_VSReadWrite': Storage_OpenMode.Storage_VSReadWrite}
    pass
class Storage_HPArray(Storage_PArray, OCP.Standard.Standard_Transient):
    def Array1(self) -> Storage_PArray: 
        """
        None
        """
    def Assign(self,theOther : Storage_PArray) -> Storage_PArray: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Storage_PArray: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.Standard.Standard_Persistent: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Standard.Standard_Persistent: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Standard.Standard_Persistent: 
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
    def First(self) -> OCP.Standard.Standard_Persistent: 
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
    def Init(self,theValue : OCP.Standard.Standard_Persistent) -> None: 
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
    def Last(self) -> OCP.Standard.Standard_Persistent: 
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
    def Move(self,theOther : Storage_PArray) -> Storage_PArray: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Standard.Standard_Persistent) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Standard.Standard_Persistent: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.Standard.Standard_Persistent) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Storage_PArray) -> None: ...
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
class Storage_PType(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TCollection.TCollection_AsciiString,theItem : int) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Storage_PType) -> Storage_PType: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> int: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> int: 
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
    def Exchange(self,theOther : Storage_PType) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> int: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TCollection.TCollection_AsciiString,theValue : int) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> int: ...
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
    def Seek(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> int: 
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
    def Substitute(self,theIndex : int,theKey1 : OCP.TCollection.TCollection_AsciiString,theItem : int) -> None: 
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
    def __init__(self,theOther : Storage_PType) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Storage_Root(OCP.Standard.Standard_Transient):
    """
    A root object extracted from a Storage_Data object. A Storage_Root encapsulates a persistent object which is a root of a Storage_Data object. It contains additional information: the name and the data type of the persistent object. When retrieving a Storage_Data object from a container (for example, a file) you access its roots with the function Roots which returns a sequence of root objects. The provided functions allow you to request information about each root of the sequence. You do not create explicit roots: when inserting data in a Storage_Data object, you just provide the persistent object and optionally its name to the function AddRoot.A root object extracted from a Storage_Data object. A Storage_Root encapsulates a persistent object which is a root of a Storage_Data object. It contains additional information: the name and the data type of the persistent object. When retrieving a Storage_Data object from a container (for example, a file) you access its roots with the function Roots which returns a sequence of root objects. The provided functions allow you to request information about each root of the sequence. You do not create explicit roots: when inserting data in a Storage_Data object, you just provide the persistent object and optionally its name to the function AddRoot.A root object extracted from a Storage_Data object. A Storage_Root encapsulates a persistent object which is a root of a Storage_Data object. It contains additional information: the name and the data type of the persistent object. When retrieving a Storage_Data object from a container (for example, a file) you access its roots with the function Roots which returns a sequence of root objects. The provided functions allow you to request information about each root of the sequence. You do not create explicit roots: when inserting data in a Storage_Data object, you just provide the persistent object and optionally its name to the function AddRoot.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of this root object. The name may have been given explicitly when the root was inserted into the Storage_Data object. If not, the name is a reference number which was assigned automatically by the driver when writing the set of data into the container. When naming the roots, it is easier to retrieve objects by significant references rather than by references without any semantic values. Warning The returned string will be empty if you call this function before having named this root object, either explicitly, or when writing the set of data into the container.
        """
    def Object(self) -> OCP.Standard.Standard_Persistent: 
        """
        Returns the persistent object encapsulated by this root.
        """
    def Reference(self) -> int: 
        """
        None
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetObject(self,anObject : OCP.Standard.Standard_Persistent) -> None: 
        """
        None
        """
    def SetReference(self,aRef : int) -> None: 
        """
        None
        """
    def SetType(self,aType : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of this root type.
        """
    @overload
    def __init__(self,theName : OCP.TCollection.TCollection_AsciiString,theObject : OCP.Standard.Standard_Persistent) -> None: ...
    @overload
    def __init__(self,theName : OCP.TCollection.TCollection_AsciiString,theRef : int,theType : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Storage_RootData(OCP.Standard.Standard_Transient):
    def AddRoot(self,aRoot : Storage_Root) -> None: 
        """
        add a root to <me>. If a root with same name is present, it will be replaced by <aRoot>.
        """
    def ClearErrorStatus(self) -> None: 
        """
        None
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
    def ErrorStatus(self) -> Storage_Error: 
        """
        None
        """
    def ErrorStatusExtension(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def Find(self,aName : OCP.TCollection.TCollection_AsciiString) -> Storage_Root: 
        """
        find a root with name <aName>.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsRoot(self,aName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        returns Standard_True if <me> contains a root named <aName>
        """
    def NumberOfRoots(self) -> int: 
        """
        returns the number of roots.
        """
    def Read(self,theDriver : Storage_BaseDriver) -> bool: 
        """
        None
        """
    def RemoveRoot(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        remove the root named <aName>.
        """
    def Roots(self) -> Storage_HSeqOfRoot: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateRoot(self,aName : OCP.TCollection.TCollection_AsciiString,aPers : OCP.Standard.Standard_Persistent) -> None: 
        """
        None
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
class Storage_Schema(OCP.Standard.Standard_Transient):
    """
    Root class for basic storage/retrieval algorithms. A Storage_Schema object processes: - writing of a set of persistent data into a container (store mechanism), - reading of a container to extract all the contained persistent data (retrieve mechanism). A Storage_Schema object is based on the data schema for the persistent data of the application, i.e.: - the list of all persistent objects which may be known by the application, - the organization of their data; a data schema knows how to browse each persistent object it contains. During the store or retrieve operation, only persistent objects known from the data schema can be processed; they are then stored or retrieved according to their description in the schema. A data schema is specific to the object classes to be read or written. Tools dedicated to the environment in use allow a description of the application persistent data structure. Storage_Schema algorithms are called basic because they do not support external references between containers.Root class for basic storage/retrieval algorithms. A Storage_Schema object processes: - writing of a set of persistent data into a container (store mechanism), - reading of a container to extract all the contained persistent data (retrieve mechanism). A Storage_Schema object is based on the data schema for the persistent data of the application, i.e.: - the list of all persistent objects which may be known by the application, - the organization of their data; a data schema knows how to browse each persistent object it contains. During the store or retrieve operation, only persistent objects known from the data schema can be processed; they are then stored or retrieved according to their description in the schema. A data schema is specific to the object classes to be read or written. Tools dedicated to the environment in use allow a description of the application persistent data structure. Storage_Schema algorithms are called basic because they do not support external references between containers.Root class for basic storage/retrieval algorithms. A Storage_Schema object processes: - writing of a set of persistent data into a container (store mechanism), - reading of a container to extract all the contained persistent data (retrieve mechanism). A Storage_Schema object is based on the data schema for the persistent data of the application, i.e.: - the list of all persistent objects which may be known by the application, - the organization of their data; a data schema knows how to browse each persistent object it contains. During the store or retrieve operation, only persistent objects known from the data schema can be processed; they are then stored or retrieved according to their description in the schema. A data schema is specific to the object classes to be read or written. Tools dedicated to the environment in use allow a description of the application persistent data structure. Storage_Schema algorithms are called basic because they do not support external references between containers.
    """
    def AddPersistent(self,sp : OCP.Standard.Standard_Persistent,tName : str) -> bool: 
        """
        None
        """
    def AddReadUnknownTypeCallBack(self,aTypeName : OCP.TCollection.TCollection_AsciiString,aCallBack : Storage_CallBack) -> None: 
        """
        add two functions to the callback list
        """
    @staticmethod
    def CheckTypeMigration_s(theTypeName : OCP.TCollection.TCollection_AsciiString,theNewName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        returns True if theType migration is identified the callback support provides a way to read a file with a incomplete schema. ex. : A file contains 3 types a,b and c. The application's schema contains only 2 type a and b. If you try to read the file in the application, you will have an error.To bypass this problem you can give to your application's schema a callback used when the schema dosent know how to handle this type.
        """
    def ClearCallBackList(self) -> None: 
        """
        clear all callback from schema instance.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultCallBack(self) -> Storage_CallBack: 
        """
        returns the read function used when the UseDefaultCallBack() is set.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DontUseDefaultCallBack(self) -> None: 
        """
        tells schema to uninstall the default callback.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def ICreationDate_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        return a current date string
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InstalledCallBackList(self) -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        returns a list of type name with installed callback.
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
    def IsUsingDefaultCallBack(self) -> bool: 
        """
        ask if the schema is using the default callback.
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns the schema's name
        """
    def PersistentToAdd(self,sp : OCP.Standard.Standard_Persistent) -> bool: 
        """
        None
        """
    def RemoveReadUnknownTypeCallBack(self,aTypeName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        remove a callback for a type
        """
    def ResetDefaultCallBack(self) -> None: 
        """
        reset the default function defined by Storage package.
        """
    def SetDefaultCallBack(self,f : Storage_CallBack) -> None: 
        """
        overload the default function for build.(use to set an error message or skip an object while reading an unknown type).
        """
    def SetName(self,aSchemaName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        set the schema's name
        """
    def SetVersion(self,aVersion : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        returns version of the schema
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UseDefaultCallBack(self) -> None: 
        """
        install a callback for all unknown type. the objects with unknown types will be skipped. (look SkipObject method in BaseDriver)
        """
    def Version(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns the version of the schema
        """
    def Write(self,s : Storage_BaseDriver,aData : Storage_Data) -> None: 
        """
        Writes the data aggregated in aData into the container defined by the driver s. The storage operation is performed according to the data schema with which this algorithm is working. Note: aData may aggregate several root objects to be stored together.
        """
    @overload
    def WritePersistentObjectHeader(self,sp : OCP.Standard.Standard_Persistent,s : Storage_BaseDriver) -> None: 
        """
        None

        None
        """
    @overload
    def WritePersistentObjectHeader(self,sp : OCP.Standard.Standard_Persistent,f : Storage_BaseDriver) -> None: ...
    @overload
    def WritePersistentReference(self,sp : OCP.Standard.Standard_Persistent,f : Storage_BaseDriver) -> None: 
        """
        None

        None
        """
    @overload
    def WritePersistentReference(self,sp : OCP.Standard.Standard_Persistent,s : Storage_BaseDriver) -> None: ...
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
class Storage_HSeqOfRoot(Storage_SeqOfRoot, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Storage_Root) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : Storage_SeqOfRoot) -> None: ...
    def Assign(self,theOther : Storage_SeqOfRoot) -> Storage_SeqOfRoot: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Storage_Root: 
        """
        First item access
        """
    def ChangeLast(self) -> Storage_Root: 
        """
        Last item access
        """
    def ChangeSequence(self) -> Storage_SeqOfRoot: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> Storage_Root: 
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
    def First(self) -> Storage_Root: 
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
    def InsertAfter(self,theIndex : int,theItem : Storage_Root) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Storage_SeqOfRoot) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Storage_SeqOfRoot) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Storage_Root) -> None: ...
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> Storage_Root: 
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
    def Prepend(self,theItem : Storage_Root) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Storage_SeqOfRoot) -> None: ...
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
    def Sequence(self) -> Storage_SeqOfRoot: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : Storage_Root) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Storage_SeqOfRoot) -> None: 
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
    def Value(self,theIndex : int) -> Storage_Root: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Storage_SeqOfRoot) -> None: ...
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
class Storage_SolveMode():
    """
    None

    Members:

      Storage_AddSolve

      Storage_WriteSolve

      Storage_ReadSolve
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Storage_AddSolve: OCP.Storage.Storage_SolveMode # value = Storage_SolveMode.Storage_AddSolve
    Storage_ReadSolve: OCP.Storage.Storage_SolveMode # value = Storage_SolveMode.Storage_ReadSolve
    Storage_WriteSolve: OCP.Storage.Storage_SolveMode # value = Storage_SolveMode.Storage_WriteSolve
    __entries: dict # value = {'Storage_AddSolve': (Storage_SolveMode.Storage_AddSolve, None), 'Storage_WriteSolve': (Storage_SolveMode.Storage_WriteSolve, None), 'Storage_ReadSolve': (Storage_SolveMode.Storage_ReadSolve, None)}
    __members__: dict # value = {'Storage_AddSolve': Storage_SolveMode.Storage_AddSolve, 'Storage_WriteSolve': Storage_SolveMode.Storage_WriteSolve, 'Storage_ReadSolve': Storage_SolveMode.Storage_ReadSolve}
    pass
class Storage_StreamFormatError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Storage', '__weakref__': <attribute '__weakref__' of 'Storage_StreamFormatError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Storage_StreamFormatError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Storage_StreamModeError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Storage', '__weakref__': <attribute '__weakref__' of 'Storage_StreamModeError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Storage_StreamModeError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Storage_StreamReadError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Storage', '__weakref__': <attribute '__weakref__' of 'Storage_StreamReadError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Storage_StreamReadError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Storage_StreamWriteError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Storage', '__weakref__': <attribute '__weakref__' of 'Storage_StreamWriteError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Storage_StreamWriteError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Storage_TypeData(OCP.Standard.Standard_Transient):
    def AddType(self,aName : OCP.TCollection.TCollection_AsciiString,aTypeNum : int) -> None: 
        """
        add a type to the list
        """
    def Clear(self) -> None: 
        """
        None
        """
    def ClearErrorStatus(self) -> None: 
        """
        None
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
    def ErrorStatus(self) -> Storage_Error: 
        """
        None
        """
    def ErrorStatusExtension(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsType(self,aName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        None
        """
    def NumberOfTypes(self) -> int: 
        """
        None
        """
    def Read(self,theDriver : Storage_BaseDriver) -> bool: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Type(self,aTypeNum : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns the name of the type with number <aTypeNum>

        returns the name of the type with number <aTypeNum>
        """
    @overload
    def Type(self,aTypeName : OCP.TCollection.TCollection_AsciiString) -> int: ...
    def Types(self) -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        None
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
class Storage_TypedCallBack(OCP.Standard.Standard_Transient):
    def CallBack(self) -> Storage_CallBack: 
        """
        None
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
    def Index(self) -> int: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetCallBack(self,aCallBack : Storage_CallBack) -> None: 
        """
        None
        """
    def SetIndex(self,anIndex : int) -> None: 
        """
        None
        """
    def SetType(self,aType : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aTypeName : OCP.TCollection.TCollection_AsciiString,aCallBack : Storage_CallBack) -> None: ...
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
Storage_AddSolve: OCP.Storage.Storage_SolveMode # value = Storage_SolveMode.Storage_AddSolve
Storage_ReadSolve: OCP.Storage.Storage_SolveMode # value = Storage_SolveMode.Storage_ReadSolve
Storage_VSAlreadyOpen: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSAlreadyOpen
Storage_VSCloseError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSCloseError
Storage_VSExtCharParityError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSExtCharParityError
Storage_VSFormatError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSFormatError
Storage_VSInternalError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSInternalError
Storage_VSModeError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSModeError
Storage_VSNone: OCP.Storage.Storage_OpenMode # value = Storage_OpenMode.Storage_VSNone
Storage_VSNotOpen: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSNotOpen
Storage_VSOk: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSOk
Storage_VSOpenError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSOpenError
Storage_VSRead: OCP.Storage.Storage_OpenMode # value = Storage_OpenMode.Storage_VSRead
Storage_VSReadWrite: OCP.Storage.Storage_OpenMode # value = Storage_OpenMode.Storage_VSReadWrite
Storage_VSSectionNotFound: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSSectionNotFound
Storage_VSTypeMismatch: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSTypeMismatch
Storage_VSUnknownType: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSUnknownType
Storage_VSWrite: OCP.Storage.Storage_OpenMode # value = Storage_OpenMode.Storage_VSWrite
Storage_VSWriteError: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSWriteError
Storage_VSWrongFileDriver: OCP.Storage.Storage_Error # value = Storage_Error.Storage_VSWrongFileDriver
Storage_WriteSolve: OCP.Storage.Storage_SolveMode # value = Storage_SolveMode.Storage_WriteSolve
