import OCP.BinObjMgt
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.Standard
import OCP.TDF
import io
import OCP.Storage
__all__  = [
"BinObjMgt_Persistent",
"BinObjMgt_Position",
"BinObjMgt_RRelocationTable"
]
class BinObjMgt_Persistent():
    """
    Binary persistent representation of an object. Really it is used as a buffer for read/write an object.
    """
    def Destroy(self) -> None: 
        """
        Frees the allocated memory; This object can be reused after call to Init
        """
    def GetAsciiString(self,theValue : OCP.TCollection.TCollection_AsciiString) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetBoolean(self,theValue : bool) -> BinObjMgt_Persistent: 
        """
        None

        None
        """
    def GetByte(self,theValue : int) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetByteArray(self,theArray : int,theLength : int) -> BinObjMgt_Persistent: 
        """
        Get C array of unsigned chars, theLength is the number of elements; theArray must point to a space enough to place theLength elements
        """
    def GetCharArray(self,theArray : str,theLength : int) -> BinObjMgt_Persistent: 
        """
        Get C array of char, theLength is the number of elements; theArray must point to a space enough to place theLength elements
        """
    def GetCharacter(self,theValue : str) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetExtCharArray(self,theArray : str,theLength : int) -> BinObjMgt_Persistent: 
        """
        Get C array of ExtCharacter, theLength is the number of elements; theArray must point to a space enough to place theLength elements
        """
    def GetExtCharacter(self,theValue : str) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetExtendedString(self,theValue : OCP.TCollection.TCollection_ExtendedString) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetGUID(self,theValue : OCP.Standard.Standard_GUID) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetIntArray(self,theArray : int,theLength : int) -> BinObjMgt_Persistent: 
        """
        Get C array of int, theLength is the number of elements; theArray must point to a space enough to place theLength elements
        """
    def GetInteger(self,theValue : int) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetLabel(self,theDS : OCP.TDF.TDF_Data,theValue : OCP.TDF.TDF_Label) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetReal(self,theValue : float) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetRealArray(self,theArray : float,theLength : int) -> BinObjMgt_Persistent: 
        """
        Get C array of double, theLength is the number of elements; theArray must point to a space enough to place theLength elements
        """
    def GetShortReal(self,theValue : float) -> BinObjMgt_Persistent: 
        """
        None
        """
    def GetShortRealArray(self,theArray : float,theLength : int) -> BinObjMgt_Persistent: 
        """
        Get C array of float, theLength is the number of elements; theArray must point to a space enough to place theLength elements
        """
    def Id(self) -> int: 
        """
        Returns the Id of the object

        Returns the Id of the object
        """
    def Init(self) -> None: 
        """
        Initializes me to reuse again
        """
    def IsDirect(self) -> bool: 
        """
        Returns true if after this record a direct writing to the stream is performed.
        """
    def IsError(self) -> bool: 
        """
        Indicates an error after Get methods or SetPosition

        Indicates an error after Get methods or SetPosition
        """
    def IsOK(self) -> bool: 
        """
        Indicates a good state after Get methods or SetPosition

        Indicates a good state after Get methods or SetPosition
        """
    def Length(self) -> int: 
        """
        Returns the length of data

        Returns the length of data
        """
    def Position(self) -> int: 
        """
        Tells the current position for get/put

        Tells the current position for get/put
        """
    def PutAsciiString(self,theValue : OCP.TCollection.TCollection_AsciiString) -> BinObjMgt_Persistent: 
        """
        Offset in output buffer is word-aligned
        """
    def PutBoolean(self,theValue : bool) -> BinObjMgt_Persistent: 
        """
        None

        None
        """
    def PutByte(self,theValue : int) -> BinObjMgt_Persistent: 
        """
        None
        """
    def PutByteArray(self,theArray : int,theLength : int) -> BinObjMgt_Persistent: 
        """
        Put C array of unsigned chars, theLength is the number of elements
        """
    def PutCString(self,theValue : str) -> BinObjMgt_Persistent: 
        """
        Offset in output buffer is not aligned
        """
    def PutCharArray(self,theArray : str,theLength : int) -> BinObjMgt_Persistent: 
        """
        Put C array of char, theLength is the number of elements
        """
    def PutCharacter(self,theValue : str) -> BinObjMgt_Persistent: 
        """
        None
        """
    def PutExtCharArray(self,theArray : str,theLength : int) -> BinObjMgt_Persistent: 
        """
        Put C array of ExtCharacter, theLength is the number of elements
        """
    def PutExtCharacter(self,theValue : str) -> BinObjMgt_Persistent: 
        """
        None
        """
    def PutExtendedString(self,theValue : OCP.TCollection.TCollection_ExtendedString) -> BinObjMgt_Persistent: 
        """
        Offset in output buffer is word-aligned
        """
    def PutGUID(self,theValue : OCP.Standard.Standard_GUID) -> BinObjMgt_Persistent: 
        """
        None
        """
    def PutIntArray(self,theArray : int,theLength : int) -> BinObjMgt_Persistent: 
        """
        Put C array of int, theLength is the number of elements
        """
    def PutInteger(self,theValue : int) -> BinObjMgt_Persistent: 
        """
        None
        """
    def PutLabel(self,theValue : OCP.TDF.TDF_Label) -> BinObjMgt_Persistent: 
        """
        None
        """
    def PutReal(self,theValue : float) -> BinObjMgt_Persistent: 
        """
        None
        """
    def PutRealArray(self,theArray : float,theLength : int) -> BinObjMgt_Persistent: 
        """
        Put C array of double, theLength is the number of elements
        """
    def PutShortReal(self,theValue : float) -> BinObjMgt_Persistent: 
        """
        None
        """
    def PutShortRealArray(self,theArray : float,theLength : int) -> BinObjMgt_Persistent: 
        """
        Put C array of float, theLength is the number of elements
        """
    def Read(self,theIS : io.BytesIO) -> io.BytesIO: 
        """
        Retrieves <me> from the stream. inline Standard_IStream& operator>> (Standard_IStream&, BinObjMgt_Persistent&) is also available
        """
    def SetIStream(self,theStream : io.BytesIO) -> None: 
        """
        Sets the stream for direct reading
        """
    def SetId(self,theId : int) -> None: 
        """
        Sets the Id of the object

        Sets the Id of the object
        """
    def SetOStream(self,theStream : io.BytesIO) -> None: 
        """
        Sets the stream for direct writing
        """
    def SetPosition(self,thePos : int) -> bool: 
        """
        Sets the current position for get/put. Resets an error state depending on the validity of thePos. Returns the new state (value of IsOK())

        Sets the current position for get/put. Resets an error state depending on the validity of thePos. Returns the new state (value of IsOK())
        """
    @overload
    def SetTypeId(self,theId : int) -> None: 
        """
        Sets the Id of the type of the object

        Sets the Id of the type of the object
        """
    @overload
    def SetTypeId(self,theTypeId : int) -> None: ...
    def StreamStart(self) -> BinObjMgt_Position: 
        """
        Returns the start position of the direct writing in the stream
        """
    def Truncate(self) -> None: 
        """
        Truncates the buffer by current position, i.e. updates mySize

        Truncates the buffer by current position, i.e. updates mySize
        """
    def TypeId(self) -> int: 
        """
        Returns the Id of the type of the object

        Returns the Id of the type of the object
        """
    def Write(self,theOS : io.BytesIO,theDirectStream : bool=False) -> io.BytesIO: 
        """
        Stores <me> to the stream. inline Standard_OStream& operator<< (Standard_OStream&, BinObjMgt_Persistent&) is also available. If theDirectStream is true, after this data the direct stream data is stored.
        """
    def __init__(self) -> None: ...
    pass
class BinObjMgt_Position(OCP.Standard.Standard_Transient):
    """
    Stores and manipulates position in the stream.Stores and manipulates position in the stream.Stores and manipulates position in the stream.
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
    def StoreSize(self,theStream : io.BytesIO) -> None: 
        """
        Stores the difference between the current position and the stored one.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteSize(self,theStream : io.BytesIO,theDummy : bool=False) -> None: 
        """
        Writes stored size at the stored position. Changes the current stream position. If theDummy is true, is writes to the current position zero size.
        """
    def __init__(self,theStream : io.BytesIO) -> None: ...
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
class BinObjMgt_RRelocationTable():
    """
    Retrieval relocation table is modeled as a child class of TColStd_DataMapOfIntegerTransient that stores a handle to the file header section. With that attribute drivers have access to the file header section.
    """
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        None
        """
    def GetHeaderData(self) -> OCP.Storage.Storage_HeaderData: 
        """
        Returns a handle to the header data of the file that is begin read
        """
    def SetHeaderData(self,theHeaderData : OCP.Storage.Storage_HeaderData) -> None: 
        """
        Sets the storage header data.
        """
    def __init__(self) -> None: ...
    pass
