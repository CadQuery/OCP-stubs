import OCP.PCDM
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.TColStd
import OCP.Message
import OCP.Storage
import OCP.Standard
import OCP.CDM
import OCP.NCollection
__all__  = [
"PCDM",
"PCDM_Document",
"PCDM_DriverError",
"PCDM_ReadWriter",
"PCDM_ReadWriter_1",
"PCDM_Reader",
"PCDM_ReaderStatus",
"PCDM_Reference",
"PCDM_ReferenceIterator",
"PCDM_RetrievalDriver",
"PCDM_SequenceOfDocument",
"PCDM_SequenceOfReference",
"PCDM_Writer",
"PCDM_StoreStatus",
"PCDM_TypeOfFileDriver",
"PCDM_StorageDriver",
"PCDM_RS_AlreadyRetrieved",
"PCDM_RS_AlreadyRetrievedAndModified",
"PCDM_RS_DriverFailure",
"PCDM_RS_ExtensionFailure",
"PCDM_RS_FormatFailure",
"PCDM_RS_MakeFailure",
"PCDM_RS_NoDocument",
"PCDM_RS_NoDriver",
"PCDM_RS_NoModel",
"PCDM_RS_NoSchema",
"PCDM_RS_NoVersion",
"PCDM_RS_OK",
"PCDM_RS_OpenError",
"PCDM_RS_PermissionDenied",
"PCDM_RS_ReaderException",
"PCDM_RS_TypeFailure",
"PCDM_RS_TypeNotFoundInSchema",
"PCDM_RS_UnknownDocument",
"PCDM_RS_UnknownFileDriver",
"PCDM_RS_UnrecognizedFileFormat",
"PCDM_RS_WrongResource",
"PCDM_RS_WrongStreamMode",
"PCDM_SS_Doc_IsNull",
"PCDM_SS_DriverFailure",
"PCDM_SS_Failure",
"PCDM_SS_Info_Section_Error",
"PCDM_SS_No_Obj",
"PCDM_SS_OK",
"PCDM_SS_WriteFailure",
"PCDM_TOFD_CmpFile",
"PCDM_TOFD_File",
"PCDM_TOFD_Unknown",
"PCDM_TOFD_XmlFile"
]
class PCDM():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class PCDM_Document(OCP.Standard.Standard_Persistent, OCP.Standard.Standard_Transient):
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
    @property
    def TypeNum(self) -> int:
        """
        None

        :type: int
        """
    @TypeNum.setter
    def TypeNum(self, arg1: int) -> None:
        """
        None
        """
    pass
class PCDM_DriverError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.PCDM', '__weakref__': <attribute '__weakref__' of 'PCDM_DriverError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'PCDM_DriverError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class PCDM_ReadWriter(OCP.Standard.Standard_Transient):
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
    @staticmethod
    def FileFormat_s(aFileName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        tries to get a format in the file. returns an empty string if the file could not be read or does not have a FileFormat information.
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
    def Open_s(aDriver : OCP.Storage.Storage_BaseDriver,aFileName : OCP.TCollection.TCollection_ExtendedString,anOpenMode : OCP.Storage.Storage_OpenMode) -> None: 
        """
        None
        """
    def ReadDocumentVersion(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theMsgDriver : OCP.Message.Message_Messenger) -> int: 
        """
        None
        """
    def ReadExtensions(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theExtensions : OCP.TColStd.TColStd_SequenceOfExtendedString,theMsgDriver : OCP.Message.Message_Messenger) -> None: 
        """
        None
        """
    def ReadReferenceCounter(self,theFileName : OCP.TCollection.TCollection_ExtendedString,theMsgDriver : OCP.Message.Message_Messenger) -> int: 
        """
        None
        """
    def ReadReferences(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theReferences : PCDM_SequenceOfReference,theMsgDriver : OCP.Message.Message_Messenger) -> None: 
        """
        None
        """
    @staticmethod
    def Reader_s(aFileName : OCP.TCollection.TCollection_ExtendedString) -> PCDM_ReadWriter: 
        """
        returns the convenient Reader for a File.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Version(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns PCDM_ReadWriter_1.
        """
    def WriteExtensions(self,aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        None
        """
    @staticmethod
    def WriteFileFormat_s(aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        None
        """
    def WriteReferenceCounter(self,aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        None
        """
    def WriteReferences(self,aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document,theReferencerFileName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    def WriteVersion(self,aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        None
        """
    @staticmethod
    def Writer_s() -> PCDM_ReadWriter: 
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
class PCDM_ReadWriter_1(PCDM_ReadWriter, OCP.Standard.Standard_Transient):
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
    @staticmethod
    def FileFormat_s(aFileName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        tries to get a format in the file. returns an empty string if the file could not be read or does not have a FileFormat information.
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
    def Open_s(aDriver : OCP.Storage.Storage_BaseDriver,aFileName : OCP.TCollection.TCollection_ExtendedString,anOpenMode : OCP.Storage.Storage_OpenMode) -> None: 
        """
        None
        """
    def ReadDocumentVersion(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theMsgDriver : OCP.Message.Message_Messenger) -> int: 
        """
        None
        """
    def ReadExtensions(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theExtensions : OCP.TColStd.TColStd_SequenceOfExtendedString,theMsgDriver : OCP.Message.Message_Messenger) -> None: 
        """
        None
        """
    def ReadReferenceCounter(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theMsgDriver : OCP.Message.Message_Messenger) -> int: 
        """
        None
        """
    def ReadReferences(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theReferences : PCDM_SequenceOfReference,theMsgDriver : OCP.Message.Message_Messenger) -> None: 
        """
        None
        """
    @staticmethod
    def Reader_s(aFileName : OCP.TCollection.TCollection_ExtendedString) -> PCDM_ReadWriter: 
        """
        returns the convenient Reader for a File.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Version(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns PCDM_ReadWriter_1.
        """
    def WriteExtensions(self,aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        None
        """
    @staticmethod
    def WriteFileFormat_s(aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        None
        """
    def WriteReferenceCounter(self,aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        None
        """
    def WriteReferences(self,aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document,theReferencerFileName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    def WriteVersion(self,aData : OCP.Storage.Storage_Data,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        None
        """
    @staticmethod
    def Writer_s() -> PCDM_ReadWriter: 
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
class PCDM_Reader(OCP.Standard.Standard_Transient):
    def CreateDocument(self) -> OCP.CDM.CDM_Document: 
        """
        this method is called by the framework before the read method.
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
    def GetStatus(self) -> PCDM_ReaderStatus: 
        """
        None

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
    @overload
    def Read(self,aFileName : OCP.TCollection.TCollection_ExtendedString,aNewDocument : OCP.CDM.CDM_Document,anApplication : OCP.CDM.CDM_Application) -> None: 
        """
        retrieves the content of the file into a new Document.

        None
        """
    @overload
    def Read(self,theIStream : Any,theStorageData : OCP.Storage.Storage_Data,theDoc : OCP.CDM.CDM_Document,theApplication : OCP.CDM.CDM_Application) -> None: ...
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
class PCDM_ReaderStatus():
    """
    None

    Members:

      PCDM_RS_OK

      PCDM_RS_NoDriver

      PCDM_RS_UnknownFileDriver

      PCDM_RS_OpenError

      PCDM_RS_NoVersion

      PCDM_RS_NoSchema

      PCDM_RS_NoDocument

      PCDM_RS_ExtensionFailure

      PCDM_RS_WrongStreamMode

      PCDM_RS_FormatFailure

      PCDM_RS_TypeFailure

      PCDM_RS_TypeNotFoundInSchema

      PCDM_RS_UnrecognizedFileFormat

      PCDM_RS_MakeFailure

      PCDM_RS_PermissionDenied

      PCDM_RS_DriverFailure

      PCDM_RS_AlreadyRetrievedAndModified

      PCDM_RS_AlreadyRetrieved

      PCDM_RS_UnknownDocument

      PCDM_RS_WrongResource

      PCDM_RS_ReaderException

      PCDM_RS_NoModel
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
    PCDM_RS_AlreadyRetrieved: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_AlreadyRetrieved
    PCDM_RS_AlreadyRetrievedAndModified: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_AlreadyRetrievedAndModified
    PCDM_RS_DriverFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_DriverFailure
    PCDM_RS_ExtensionFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_ExtensionFailure
    PCDM_RS_FormatFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_FormatFailure
    PCDM_RS_MakeFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_MakeFailure
    PCDM_RS_NoDocument: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoDocument
    PCDM_RS_NoDriver: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoDriver
    PCDM_RS_NoModel: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoModel
    PCDM_RS_NoSchema: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoSchema
    PCDM_RS_NoVersion: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoVersion
    PCDM_RS_OK: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_OK
    PCDM_RS_OpenError: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_OpenError
    PCDM_RS_PermissionDenied: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_PermissionDenied
    PCDM_RS_ReaderException: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_ReaderException
    PCDM_RS_TypeFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_TypeFailure
    PCDM_RS_TypeNotFoundInSchema: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_TypeNotFoundInSchema
    PCDM_RS_UnknownDocument: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_UnknownDocument
    PCDM_RS_UnknownFileDriver: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_UnknownFileDriver
    PCDM_RS_UnrecognizedFileFormat: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_UnrecognizedFileFormat
    PCDM_RS_WrongResource: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_WrongResource
    PCDM_RS_WrongStreamMode: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_WrongStreamMode
    __entries: dict # value = {'PCDM_RS_OK': (PCDM_ReaderStatus.PCDM_RS_OK, None), 'PCDM_RS_NoDriver': (PCDM_ReaderStatus.PCDM_RS_NoDriver, None), 'PCDM_RS_UnknownFileDriver': (PCDM_ReaderStatus.PCDM_RS_UnknownFileDriver, None), 'PCDM_RS_OpenError': (PCDM_ReaderStatus.PCDM_RS_OpenError, None), 'PCDM_RS_NoVersion': (PCDM_ReaderStatus.PCDM_RS_NoVersion, None), 'PCDM_RS_NoSchema': (PCDM_ReaderStatus.PCDM_RS_NoSchema, None), 'PCDM_RS_NoDocument': (PCDM_ReaderStatus.PCDM_RS_NoDocument, None), 'PCDM_RS_ExtensionFailure': (PCDM_ReaderStatus.PCDM_RS_ExtensionFailure, None), 'PCDM_RS_WrongStreamMode': (PCDM_ReaderStatus.PCDM_RS_WrongStreamMode, None), 'PCDM_RS_FormatFailure': (PCDM_ReaderStatus.PCDM_RS_FormatFailure, None), 'PCDM_RS_TypeFailure': (PCDM_ReaderStatus.PCDM_RS_TypeFailure, None), 'PCDM_RS_TypeNotFoundInSchema': (PCDM_ReaderStatus.PCDM_RS_TypeNotFoundInSchema, None), 'PCDM_RS_UnrecognizedFileFormat': (PCDM_ReaderStatus.PCDM_RS_UnrecognizedFileFormat, None), 'PCDM_RS_MakeFailure': (PCDM_ReaderStatus.PCDM_RS_MakeFailure, None), 'PCDM_RS_PermissionDenied': (PCDM_ReaderStatus.PCDM_RS_PermissionDenied, None), 'PCDM_RS_DriverFailure': (PCDM_ReaderStatus.PCDM_RS_DriverFailure, None), 'PCDM_RS_AlreadyRetrievedAndModified': (PCDM_ReaderStatus.PCDM_RS_AlreadyRetrievedAndModified, None), 'PCDM_RS_AlreadyRetrieved': (PCDM_ReaderStatus.PCDM_RS_AlreadyRetrieved, None), 'PCDM_RS_UnknownDocument': (PCDM_ReaderStatus.PCDM_RS_UnknownDocument, None), 'PCDM_RS_WrongResource': (PCDM_ReaderStatus.PCDM_RS_WrongResource, None), 'PCDM_RS_ReaderException': (PCDM_ReaderStatus.PCDM_RS_ReaderException, None), 'PCDM_RS_NoModel': (PCDM_ReaderStatus.PCDM_RS_NoModel, None)}
    __members__: dict # value = {'PCDM_RS_OK': PCDM_ReaderStatus.PCDM_RS_OK, 'PCDM_RS_NoDriver': PCDM_ReaderStatus.PCDM_RS_NoDriver, 'PCDM_RS_UnknownFileDriver': PCDM_ReaderStatus.PCDM_RS_UnknownFileDriver, 'PCDM_RS_OpenError': PCDM_ReaderStatus.PCDM_RS_OpenError, 'PCDM_RS_NoVersion': PCDM_ReaderStatus.PCDM_RS_NoVersion, 'PCDM_RS_NoSchema': PCDM_ReaderStatus.PCDM_RS_NoSchema, 'PCDM_RS_NoDocument': PCDM_ReaderStatus.PCDM_RS_NoDocument, 'PCDM_RS_ExtensionFailure': PCDM_ReaderStatus.PCDM_RS_ExtensionFailure, 'PCDM_RS_WrongStreamMode': PCDM_ReaderStatus.PCDM_RS_WrongStreamMode, 'PCDM_RS_FormatFailure': PCDM_ReaderStatus.PCDM_RS_FormatFailure, 'PCDM_RS_TypeFailure': PCDM_ReaderStatus.PCDM_RS_TypeFailure, 'PCDM_RS_TypeNotFoundInSchema': PCDM_ReaderStatus.PCDM_RS_TypeNotFoundInSchema, 'PCDM_RS_UnrecognizedFileFormat': PCDM_ReaderStatus.PCDM_RS_UnrecognizedFileFormat, 'PCDM_RS_MakeFailure': PCDM_ReaderStatus.PCDM_RS_MakeFailure, 'PCDM_RS_PermissionDenied': PCDM_ReaderStatus.PCDM_RS_PermissionDenied, 'PCDM_RS_DriverFailure': PCDM_ReaderStatus.PCDM_RS_DriverFailure, 'PCDM_RS_AlreadyRetrievedAndModified': PCDM_ReaderStatus.PCDM_RS_AlreadyRetrievedAndModified, 'PCDM_RS_AlreadyRetrieved': PCDM_ReaderStatus.PCDM_RS_AlreadyRetrieved, 'PCDM_RS_UnknownDocument': PCDM_ReaderStatus.PCDM_RS_UnknownDocument, 'PCDM_RS_WrongResource': PCDM_ReaderStatus.PCDM_RS_WrongResource, 'PCDM_RS_ReaderException': PCDM_ReaderStatus.PCDM_RS_ReaderException, 'PCDM_RS_NoModel': PCDM_ReaderStatus.PCDM_RS_NoModel}
    pass
class PCDM_Reference():
    """
    None
    """
    def DocumentVersion(self) -> int: 
        """
        None
        """
    def FileName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def ReferenceIdentifier(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self,aReferenceIdentifier : int,aFileName : OCP.TCollection.TCollection_ExtendedString,aDocumentVersion : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class PCDM_ReferenceIterator(OCP.Standard.Standard_Transient):
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
    def Init(self,aMetaData : OCP.CDM.CDM_MetaData) -> None: 
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
    def LoadReferences(self,aDocument : OCP.CDM.CDM_Document,aMetaData : OCP.CDM.CDM_MetaData,anApplication : OCP.CDM.CDM_Application,UseStorageConfiguration : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theMessageDriver : OCP.Message.Message_Messenger) -> None: ...
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
class PCDM_RetrievalDriver(PCDM_Reader, OCP.Standard.Standard_Transient):
    def CreateDocument(self) -> OCP.CDM.CDM_Document: 
        """
        this method is called by the framework before the read method.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @staticmethod
    def DocumentVersion_s(theFileName : OCP.TCollection.TCollection_ExtendedString,theMsgDriver : OCP.Message.Message_Messenger) -> int: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetFormat(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> PCDM_ReaderStatus: 
        """
        None

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
    @overload
    def Read(self,aFileName : OCP.TCollection.TCollection_ExtendedString,aNewDocument : OCP.CDM.CDM_Document,anApplication : OCP.CDM.CDM_Application) -> None: 
        """
        retrieves the content of the file into a new Document.

        None
        """
    @overload
    def Read(self,theIStream : Any,theStorageData : OCP.Storage.Storage_Data,theDoc : OCP.CDM.CDM_Document,theApplication : OCP.CDM.CDM_Application) -> None: ...
    @staticmethod
    def ReferenceCounter_s(theFileName : OCP.TCollection.TCollection_ExtendedString,theMsgDriver : OCP.Message.Message_Messenger) -> int: 
        """
        None
        """
    def SetFormat(self,aformat : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
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
class PCDM_SequenceOfDocument(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : PCDM_SequenceOfDocument) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : PCDM_Document) -> None: ...
    def Assign(self,theOther : PCDM_SequenceOfDocument) -> PCDM_SequenceOfDocument: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> PCDM_Document: 
        """
        First item access
        """
    def ChangeLast(self) -> PCDM_Document: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> PCDM_Document: 
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
    def First(self) -> PCDM_Document: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : PCDM_Document) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : PCDM_SequenceOfDocument) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : PCDM_SequenceOfDocument) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : PCDM_Document) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> PCDM_Document: 
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
    def Prepend(self,theSeq : PCDM_SequenceOfDocument) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : PCDM_Document) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : PCDM_Document) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : PCDM_SequenceOfDocument) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> PCDM_Document: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : PCDM_SequenceOfDocument) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class PCDM_SequenceOfReference(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : PCDM_Reference) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : PCDM_SequenceOfReference) -> None: ...
    def Assign(self,theOther : PCDM_SequenceOfReference) -> PCDM_SequenceOfReference: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> PCDM_Reference: 
        """
        First item access
        """
    def ChangeLast(self) -> PCDM_Reference: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> PCDM_Reference: 
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
    def First(self) -> PCDM_Reference: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : PCDM_Reference) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : PCDM_SequenceOfReference) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : PCDM_SequenceOfReference) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : PCDM_Reference) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> PCDM_Reference: 
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
    def Prepend(self,theItem : PCDM_Reference) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : PCDM_SequenceOfReference) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : PCDM_Reference) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : PCDM_SequenceOfReference) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> PCDM_Reference: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : PCDM_SequenceOfReference) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class PCDM_Writer(OCP.Standard.Standard_Transient):
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Write(self,aDocument : OCP.CDM.CDM_Document,aFileName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None

        Write <theDocument> to theOStream
        """
    @overload
    def Write(self,theDocument : OCP.CDM.CDM_Document,theOStream : Any) -> None: ...
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
class PCDM_StoreStatus():
    """
    None

    Members:

      PCDM_SS_OK

      PCDM_SS_DriverFailure

      PCDM_SS_WriteFailure

      PCDM_SS_Failure

      PCDM_SS_Doc_IsNull

      PCDM_SS_No_Obj

      PCDM_SS_Info_Section_Error
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
    PCDM_SS_Doc_IsNull: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_Doc_IsNull
    PCDM_SS_DriverFailure: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_DriverFailure
    PCDM_SS_Failure: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_Failure
    PCDM_SS_Info_Section_Error: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_Info_Section_Error
    PCDM_SS_No_Obj: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_No_Obj
    PCDM_SS_OK: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_OK
    PCDM_SS_WriteFailure: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_WriteFailure
    __entries: dict # value = {'PCDM_SS_OK': (PCDM_StoreStatus.PCDM_SS_OK, None), 'PCDM_SS_DriverFailure': (PCDM_StoreStatus.PCDM_SS_DriverFailure, None), 'PCDM_SS_WriteFailure': (PCDM_StoreStatus.PCDM_SS_WriteFailure, None), 'PCDM_SS_Failure': (PCDM_StoreStatus.PCDM_SS_Failure, None), 'PCDM_SS_Doc_IsNull': (PCDM_StoreStatus.PCDM_SS_Doc_IsNull, None), 'PCDM_SS_No_Obj': (PCDM_StoreStatus.PCDM_SS_No_Obj, None), 'PCDM_SS_Info_Section_Error': (PCDM_StoreStatus.PCDM_SS_Info_Section_Error, None)}
    __members__: dict # value = {'PCDM_SS_OK': PCDM_StoreStatus.PCDM_SS_OK, 'PCDM_SS_DriverFailure': PCDM_StoreStatus.PCDM_SS_DriverFailure, 'PCDM_SS_WriteFailure': PCDM_StoreStatus.PCDM_SS_WriteFailure, 'PCDM_SS_Failure': PCDM_StoreStatus.PCDM_SS_Failure, 'PCDM_SS_Doc_IsNull': PCDM_StoreStatus.PCDM_SS_Doc_IsNull, 'PCDM_SS_No_Obj': PCDM_StoreStatus.PCDM_SS_No_Obj, 'PCDM_SS_Info_Section_Error': PCDM_StoreStatus.PCDM_SS_Info_Section_Error}
    pass
class PCDM_TypeOfFileDriver():
    """
    None

    Members:

      PCDM_TOFD_File

      PCDM_TOFD_CmpFile

      PCDM_TOFD_XmlFile

      PCDM_TOFD_Unknown
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
    PCDM_TOFD_CmpFile: OCP.PCDM.PCDM_TypeOfFileDriver # value = PCDM_TypeOfFileDriver.PCDM_TOFD_CmpFile
    PCDM_TOFD_File: OCP.PCDM.PCDM_TypeOfFileDriver # value = PCDM_TypeOfFileDriver.PCDM_TOFD_File
    PCDM_TOFD_Unknown: OCP.PCDM.PCDM_TypeOfFileDriver # value = PCDM_TypeOfFileDriver.PCDM_TOFD_Unknown
    PCDM_TOFD_XmlFile: OCP.PCDM.PCDM_TypeOfFileDriver # value = PCDM_TypeOfFileDriver.PCDM_TOFD_XmlFile
    __entries: dict # value = {'PCDM_TOFD_File': (PCDM_TypeOfFileDriver.PCDM_TOFD_File, None), 'PCDM_TOFD_CmpFile': (PCDM_TypeOfFileDriver.PCDM_TOFD_CmpFile, None), 'PCDM_TOFD_XmlFile': (PCDM_TypeOfFileDriver.PCDM_TOFD_XmlFile, None), 'PCDM_TOFD_Unknown': (PCDM_TypeOfFileDriver.PCDM_TOFD_Unknown, None)}
    __members__: dict # value = {'PCDM_TOFD_File': PCDM_TypeOfFileDriver.PCDM_TOFD_File, 'PCDM_TOFD_CmpFile': PCDM_TypeOfFileDriver.PCDM_TOFD_CmpFile, 'PCDM_TOFD_XmlFile': PCDM_TypeOfFileDriver.PCDM_TOFD_XmlFile, 'PCDM_TOFD_Unknown': PCDM_TypeOfFileDriver.PCDM_TOFD_Unknown}
    pass
class PCDM_StorageDriver(PCDM_Writer, OCP.Standard.Standard_Transient):
    """
    persistent implemention of storage.persistent implemention of storage.persistent implemention of storage.
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
    def GetFormat(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStoreStatus(self) -> PCDM_StoreStatus: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsError(self) -> bool: 
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
    @overload
    def Make(self,aDocument : OCP.CDM.CDM_Document) -> PCDM_Document: 
        """
        raises NotImplemented.

        By default, puts in the Sequence the document returns by the previous Make method.
        """
    @overload
    def Make(self,aDocument : OCP.CDM.CDM_Document,Documents : PCDM_SequenceOfDocument) -> None: ...
    def SetFormat(self,aformat : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    def SetIsError(self,theIsError : bool) -> None: 
        """
        None
        """
    def SetStoreStatus(self,theStoreStatus : PCDM_StoreStatus) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Write(self,theDocument : OCP.CDM.CDM_Document,theOStream : Any) -> None: 
        """
        Warning! raises DriverError if an error occurs during inside the Make method. stores the content of the Document into a new file.

        Write <theDocument> to theOStream
        """
    @overload
    def Write(self,aDocument : OCP.CDM.CDM_Document,aFileName : OCP.TCollection.TCollection_ExtendedString) -> None: ...
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
PCDM_RS_AlreadyRetrieved: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_AlreadyRetrieved
PCDM_RS_AlreadyRetrievedAndModified: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_AlreadyRetrievedAndModified
PCDM_RS_DriverFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_DriverFailure
PCDM_RS_ExtensionFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_ExtensionFailure
PCDM_RS_FormatFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_FormatFailure
PCDM_RS_MakeFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_MakeFailure
PCDM_RS_NoDocument: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoDocument
PCDM_RS_NoDriver: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoDriver
PCDM_RS_NoModel: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoModel
PCDM_RS_NoSchema: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoSchema
PCDM_RS_NoVersion: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_NoVersion
PCDM_RS_OK: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_OK
PCDM_RS_OpenError: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_OpenError
PCDM_RS_PermissionDenied: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_PermissionDenied
PCDM_RS_ReaderException: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_ReaderException
PCDM_RS_TypeFailure: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_TypeFailure
PCDM_RS_TypeNotFoundInSchema: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_TypeNotFoundInSchema
PCDM_RS_UnknownDocument: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_UnknownDocument
PCDM_RS_UnknownFileDriver: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_UnknownFileDriver
PCDM_RS_UnrecognizedFileFormat: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_UnrecognizedFileFormat
PCDM_RS_WrongResource: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_WrongResource
PCDM_RS_WrongStreamMode: OCP.PCDM.PCDM_ReaderStatus # value = PCDM_ReaderStatus.PCDM_RS_WrongStreamMode
PCDM_SS_Doc_IsNull: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_Doc_IsNull
PCDM_SS_DriverFailure: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_DriverFailure
PCDM_SS_Failure: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_Failure
PCDM_SS_Info_Section_Error: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_Info_Section_Error
PCDM_SS_No_Obj: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_No_Obj
PCDM_SS_OK: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_OK
PCDM_SS_WriteFailure: OCP.PCDM.PCDM_StoreStatus # value = PCDM_StoreStatus.PCDM_SS_WriteFailure
PCDM_TOFD_CmpFile: OCP.PCDM.PCDM_TypeOfFileDriver # value = PCDM_TypeOfFileDriver.PCDM_TOFD_CmpFile
PCDM_TOFD_File: OCP.PCDM.PCDM_TypeOfFileDriver # value = PCDM_TypeOfFileDriver.PCDM_TOFD_File
PCDM_TOFD_Unknown: OCP.PCDM.PCDM_TypeOfFileDriver # value = PCDM_TypeOfFileDriver.PCDM_TOFD_Unknown
PCDM_TOFD_XmlFile: OCP.PCDM.PCDM_TypeOfFileDriver # value = PCDM_TypeOfFileDriver.PCDM_TOFD_XmlFile
