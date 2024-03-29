import OCP.FSD
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.NCollection
import OCP.Standard
import OCP.Storage
import OCP.TColStd
import io
__all__  = [
"FSD_Base64",
"FSD_BinaryFile",
"FSD_File",
"FSD_CmpFile",
"FSD_FileHeader"
]
class FSD_Base64():
    """
    Tool for encoding/decoding base64 stream.
    """
    @staticmethod
    @overload
    def Decode_s(theStr : str,theLen : int) -> OCP.NCollection.NCollection_Buffer: 
        """
        Function decoding base64 string.

        Function decoding base64 string.
        """
    @staticmethod
    @overload
    def Decode_s(theDecodedData : int,theDataLen : int,theEncodedStr : str,theStrLen : int) -> int: ...
    @staticmethod
    @overload
    def Encode_s(theData : int,theDataLen : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Function encoding a buffer to base64 string.

        Function encoding a buffer to base64 string.
        """
    @staticmethod
    @overload
    def Encode_s(theEncodedStr : str,theStrLen : int,theData : int,theDataLen : int) -> int: ...
    def __init__(self) -> None: ...
    pass
class FSD_BinaryFile(OCP.Storage.Storage_BaseDriver, OCP.Standard.Standard_Transient):
    def BeginReadCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def BeginReadRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    @overload
    def BeginWriteCommentSection(self,theOStream : io.BytesIO) -> OCP.Storage.Storage_Error: 
        """
        None

        None
        """
    @overload
    def BeginWriteCommentSection(self) -> OCP.Storage.Storage_Error: ...
    def BeginWriteDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def BeginWriteRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def Close(self) -> OCP.Storage.Storage_Error: 
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
    def Destroy(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndReadCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def EndReadRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    @overload
    def EndWriteCommentSection(self,theOStream : io.BytesIO) -> OCP.Storage.Storage_Error: 
        """
        None

        None
        """
    @overload
    def EndWriteCommentSection(self) -> OCP.Storage.Storage_Error: ...
    def EndWriteDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    @overload
    def EndWriteInfoSection(self,theOStream : io.BytesIO) -> OCP.Storage.Storage_Error: 
        """
        None

        None
        """
    @overload
    def EndWriteInfoSection(self) -> OCP.Storage.Storage_Error: ...
    def EndWriteObjectData(self) -> None: 
        """
        None
        """
    def EndWritePersistentObjectData(self) -> None: 
        """
        None
        """
    def EndWriteRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def GetBoolean(self,aValue : bool) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetExtCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetInteger(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    @staticmethod
    def GetInteger_s(theIStream : io.BytesIO) -> Tuple[int]: 
        """
        None
        """
    def GetReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetReference(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    @staticmethod
    def GetReference_s(theIStream : io.BytesIO) -> Tuple[int]: 
        """
        None
        """
    def GetShortReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @staticmethod
    def InverseExtChar_s(theValue : str) -> str: 
        """
        Inverse bytes in extended character value
        """
    @staticmethod
    def InverseInt_s(theValue : int) -> int: 
        """
        Inverse bytes in integer value
        """
    @staticmethod
    def InverseReal_s(theValue : float) -> float: 
        """
        Inverse bytes in real value
        """
    @staticmethod
    def InverseShortReal_s(theValue : float) -> float: 
        """
        Inverse bytes in short real value
        """
    @staticmethod
    def InverseSize_s(theValue : int) -> int: 
        """
        Inverse bytes in size value
        """
    @staticmethod
    def InverseUint64_s(theValue : int) -> int: 
        """
        Inverse bytes in 64bit unsigned int value
        """
    def IsEnd(self) -> bool: 
        """
        None
        """
    @staticmethod
    def IsGoodFileType_s(aName : OCP.TCollection.TCollection_AsciiString) -> OCP.Storage.Storage_Error: 
        """
        None
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
    def MagicNumber_s() -> str: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def Open(self,aName : OCP.TCollection.TCollection_AsciiString,aMode : OCP.Storage.Storage_OpenMode) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def OpenMode(self) -> OCP.Storage.Storage_OpenMode: 
        """
        None
        """
    def PutBoolean(self,aValue : bool) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutExtCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutInteger(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    @staticmethod
    def PutInteger_s(theOStream : io.BytesIO,aValue : int,theOnlyCount : bool=False) -> int: 
        """
        None
        """
    def PutReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutReference(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutShortReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def ReadComment(self,userComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        None
        """
    @staticmethod
    def ReadComment_s(theIStream : io.BytesIO,userComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        None
        """
    def ReadCompleteInfo(self,theIStream : io.BytesIO,theData : OCP.Storage.Storage_Data) -> Any: 
        """
        None
        """
    @staticmethod
    def ReadExtendedString_s(theIStream : io.BytesIO,buffer : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    @staticmethod
    def ReadHeaderData_s(theIStream : io.BytesIO,theHeaderData : OCP.Storage.Storage_HeaderData) -> None: 
        """
        None
        """
    @staticmethod
    def ReadHeader_s(theIStream : io.BytesIO,theFileHeader : FSD_FileHeader) -> None: 
        """
        None
        """
    def ReadInfo(self,dbVersion : OCP.TCollection.TCollection_AsciiString,date : OCP.TCollection.TCollection_AsciiString,schemaName : OCP.TCollection.TCollection_AsciiString,schemaVersion : OCP.TCollection.TCollection_AsciiString,appName : OCP.TCollection.TCollection_ExtendedString,appVersion : OCP.TCollection.TCollection_AsciiString,objectType : OCP.TCollection.TCollection_ExtendedString,userInfo : OCP.TColStd.TColStd_SequenceOfAsciiString) -> Tuple[int]: 
        """
        None
        """
    @staticmethod
    def ReadMagicNumber_s(theIStream : io.BytesIO) -> OCP.TCollection.TCollection_AsciiString: 
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
    @staticmethod
    def ReadReferenceType_s(theIStream : io.BytesIO) -> Tuple[int, int]: 
        """
        None
        """
    def ReadRoot(self,rootName : OCP.TCollection.TCollection_AsciiString,aType : OCP.TCollection.TCollection_AsciiString) -> Tuple[int]: 
        """
        None
        """
    @staticmethod
    def ReadRoot_s(theIStream : io.BytesIO,rootName : OCP.TCollection.TCollection_AsciiString,aType : OCP.TCollection.TCollection_AsciiString) -> Tuple[int]: 
        """
        None
        """
    @staticmethod
    def ReadString_s(theIStream : io.BytesIO,buffer : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def ReadTypeInformations(self,typeName : OCP.TCollection.TCollection_AsciiString) -> Tuple[int]: 
        """
        None
        """
    @staticmethod
    def ReadTypeInformations_s(theIStream : io.BytesIO,typeName : OCP.TCollection.TCollection_AsciiString) -> Tuple[int]: 
        """
        None
        """
    def RefSectionSize(self) -> int: 
        """
        None
        """
    @staticmethod
    def RefSectionSize_s(theIStream : io.BytesIO) -> int: 
        """
        None
        """
    def RootSectionSize(self) -> int: 
        """
        None
        """
    @staticmethod
    def RootSectionSize_s(theIStream : io.BytesIO) -> int: 
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeSectionSize(self) -> int: 
        """
        None
        """
    @staticmethod
    def TypeSectionSize_s(theIStream : io.BytesIO) -> int: 
        """
        None
        """
    def WriteComment(self,userComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        None
        """
    @staticmethod
    def WriteComment_s(theOStream : io.BytesIO,theComments : OCP.TColStd.TColStd_SequenceOfExtendedString,theOnlyCount : bool=False) -> int: 
        """
        None
        """
    @staticmethod
    def WriteHeader_s(theOStream : io.BytesIO,theHeader : FSD_FileHeader,theOnlyCount : bool=False) -> int: 
        """
        None
        """
    def WriteInfo(self,nbObj : int,dbVersion : OCP.TCollection.TCollection_AsciiString,date : OCP.TCollection.TCollection_AsciiString,schemaName : OCP.TCollection.TCollection_AsciiString,schemaVersion : OCP.TCollection.TCollection_AsciiString,appName : OCP.TCollection.TCollection_ExtendedString,appVersion : OCP.TCollection.TCollection_AsciiString,objectType : OCP.TCollection.TCollection_ExtendedString,userInfo : OCP.TColStd.TColStd_SequenceOfAsciiString) -> None: 
        """
        None
        """
    @staticmethod
    def WriteInfo_s(theOStream : io.BytesIO,nbObj : int,dbVersion : OCP.TCollection.TCollection_AsciiString,date : OCP.TCollection.TCollection_AsciiString,schemaName : OCP.TCollection.TCollection_AsciiString,schemaVersion : OCP.TCollection.TCollection_AsciiString,appName : OCP.TCollection.TCollection_ExtendedString,appVersion : OCP.TCollection.TCollection_AsciiString,objectType : OCP.TCollection.TCollection_ExtendedString,userInfo : OCP.TColStd.TColStd_SequenceOfAsciiString,theOnlyCount : bool=False) -> int: 
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
class FSD_File(OCP.Storage.Storage_BaseDriver, OCP.Standard.Standard_Transient):
    """
    A general driver which defines as a file, the physical container for data to be stored or retrieved.A general driver which defines as a file, the physical container for data to be stored or retrieved.
    """
    def BeginReadCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def BeginReadRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def BeginWriteRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def Close(self) -> OCP.Storage.Storage_Error: 
        """
        Closes the file driven by this driver. This file was opened by the last call to the function Open. The function returns Storage_VSOk if the closure is correctly done, or any other value of the Storage_Error enumeration which specifies the problem encountered.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndReadCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def EndReadRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def EndWriteRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def GetBoolean(self,aValue : bool) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetExtCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetInteger(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetReference(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetShortReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEnd(self) -> bool: 
        """
        None
        """
    @staticmethod
    def IsGoodFileType_s(aName : OCP.TCollection.TCollection_AsciiString) -> OCP.Storage.Storage_Error: 
        """
        None
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
    def MagicNumber_s() -> str: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def Open(self,aName : OCP.TCollection.TCollection_AsciiString,aMode : OCP.Storage.Storage_OpenMode) -> OCP.Storage.Storage_Error: 
        """
        Assigns as aName the name of the file to be driven by this driver. aMode precises if the file is opened in read or write mode. The function returns Storage_VSOk if the file is opened correctly, or any other value of the Storage_Error enumeration which specifies the problem encountered.
        """
    def OpenMode(self) -> OCP.Storage.Storage_OpenMode: 
        """
        None
        """
    def PutBoolean(self,aValue : bool) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutExtCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutInteger(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutReference(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutShortReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def ReadComment(self,userComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        None
        """
    def ReadCompleteInfo(self,theIStream : io.BytesIO,theData : OCP.Storage.Storage_Data) -> Any: 
        """
        None
        """
    def ReadInfo(self,dbVersion : OCP.TCollection.TCollection_AsciiString,date : OCP.TCollection.TCollection_AsciiString,schemaName : OCP.TCollection.TCollection_AsciiString,schemaVersion : OCP.TCollection.TCollection_AsciiString,appName : OCP.TCollection.TCollection_ExtendedString,appVersion : OCP.TCollection.TCollection_AsciiString,objectType : OCP.TCollection.TCollection_ExtendedString,userInfo : OCP.TColStd.TColStd_SequenceOfAsciiString) -> Tuple[int]: 
        """
        None
        """
    @staticmethod
    def ReadMagicNumber_s(theIStream : io.BytesIO) -> OCP.TCollection.TCollection_AsciiString: 
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class FSD_CmpFile(FSD_File, OCP.Storage.Storage_BaseDriver, OCP.Standard.Standard_Transient):
    def BeginReadCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def BeginReadRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginReadTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def BeginWriteRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def BeginWriteTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def Close(self) -> OCP.Storage.Storage_Error: 
        """
        Closes the file driven by this driver. This file was opened by the last call to the function Open. The function returns Storage_VSOk if the closure is correctly done, or any other value of the Storage_Error enumeration which specifies the problem encountered.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndReadCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def EndReadRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndReadTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteCommentSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteDataSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteInfoSection(self) -> OCP.Storage.Storage_Error: 
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
    def EndWriteRefSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteRootSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def EndWriteTypeSection(self) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def GetBoolean(self,aValue : bool) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetExtCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetInteger(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetReference(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def GetShortReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEnd(self) -> bool: 
        """
        None
        """
    @staticmethod
    def IsGoodFileType_s(aName : OCP.TCollection.TCollection_AsciiString) -> OCP.Storage.Storage_Error: 
        """
        None
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
    def MagicNumber_s() -> str: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def Open(self,aName : OCP.TCollection.TCollection_AsciiString,aMode : OCP.Storage.Storage_OpenMode) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    def OpenMode(self) -> OCP.Storage.Storage_OpenMode: 
        """
        None
        """
    def PutBoolean(self,aValue : bool) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutExtCharacter(self,aValue : str) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutInteger(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutReference(self,aValue : int) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def PutShortReal(self,aValue : float) -> OCP.Storage.Storage_BaseDriver: 
        """
        None
        """
    def ReadComment(self,userComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        None
        """
    def ReadCompleteInfo(self,theIStream : io.BytesIO,theData : OCP.Storage.Storage_Data) -> Any: 
        """
        None
        """
    def ReadInfo(self,dbVersion : OCP.TCollection.TCollection_AsciiString,date : OCP.TCollection.TCollection_AsciiString,schemaName : OCP.TCollection.TCollection_AsciiString,schemaVersion : OCP.TCollection.TCollection_AsciiString,appName : OCP.TCollection.TCollection_ExtendedString,appVersion : OCP.TCollection.TCollection_AsciiString,objectType : OCP.TCollection.TCollection_ExtendedString,userInfo : OCP.TColStd.TColStd_SequenceOfAsciiString) -> Tuple[int]: 
        """
        None
        """
    @staticmethod
    def ReadMagicNumber_s(theIStream : io.BytesIO) -> OCP.TCollection.TCollection_AsciiString: 
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class FSD_FileHeader():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def bcomment(self) -> int:
        """
        :type: int
        """
    @bcomment.setter
    def bcomment(self, arg0: int) -> None:
        pass
    @property
    def bdata(self) -> int:
        """
        :type: int
        """
    @bdata.setter
    def bdata(self, arg0: int) -> None:
        pass
    @property
    def binfo(self) -> int:
        """
        :type: int
        """
    @binfo.setter
    def binfo(self, arg0: int) -> None:
        pass
    @property
    def bref(self) -> int:
        """
        :type: int
        """
    @bref.setter
    def bref(self, arg0: int) -> None:
        pass
    @property
    def broot(self) -> int:
        """
        :type: int
        """
    @broot.setter
    def broot(self, arg0: int) -> None:
        pass
    @property
    def btype(self) -> int:
        """
        :type: int
        """
    @btype.setter
    def btype(self, arg0: int) -> None:
        pass
    @property
    def ecomment(self) -> int:
        """
        :type: int
        """
    @ecomment.setter
    def ecomment(self, arg0: int) -> None:
        pass
    @property
    def edata(self) -> int:
        """
        :type: int
        """
    @edata.setter
    def edata(self, arg0: int) -> None:
        pass
    @property
    def einfo(self) -> int:
        """
        :type: int
        """
    @einfo.setter
    def einfo(self, arg0: int) -> None:
        pass
    @property
    def eref(self) -> int:
        """
        :type: int
        """
    @eref.setter
    def eref(self, arg0: int) -> None:
        pass
    @property
    def eroot(self) -> int:
        """
        :type: int
        """
    @eroot.setter
    def eroot(self, arg0: int) -> None:
        pass
    @property
    def etype(self) -> int:
        """
        :type: int
        """
    @etype.setter
    def etype(self, arg0: int) -> None:
        pass
    @property
    def testindian(self) -> int:
        """
        :type: int
        """
    @testindian.setter
    def testindian(self, arg0: int) -> None:
        pass
    pass
