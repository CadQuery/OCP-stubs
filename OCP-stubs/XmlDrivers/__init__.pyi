import OCP.XmlDrivers
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDocStd
import OCP.LDOM
import OCP.TCollection
import io
import OCP.XmlMDF
import OCP.Message
import OCP.XmlLDrivers
import OCP.CDM
import OCP.PCDM
import OCP.Storage
import OCP.Standard
__all__  = [
"XmlDrivers",
"XmlDrivers_DocumentRetrievalDriver",
"XmlDrivers_DocumentStorageDriver"
]
class XmlDrivers():
    """
    None
    """
    @staticmethod
    def AttributeDrivers_s(theMsgDriver : OCP.Message.Message_Messenger) -> OCP.XmlMDF.XmlMDF_ADriverTable: 
        """
        None
        """
    @staticmethod
    def DefineFormat_s(theApp : OCP.TDocStd.TDocStd_Application) -> None: 
        """
        Defines format "XmlOcaf" and registers its read and write drivers in the specified application
        """
    @staticmethod
    def Factory_s(theGUID : OCP.Standard.Standard_GUID) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class XmlDrivers_DocumentRetrievalDriver(OCP.XmlLDrivers.XmlLDrivers_DocumentRetrievalDriver, OCP.PCDM.PCDM_RetrievalDriver, OCP.PCDM.PCDM_Reader, OCP.Standard.Standard_Transient):
    def AttributeDrivers(self,theMsgDriver : OCP.Message.Message_Messenger) -> OCP.XmlMDF.XmlMDF_ADriverTable: 
        """
        None
        """
    def CreateDocument(self) -> OCP.CDM.CDM_Document: 
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
    def GetStatus(self) -> OCP.PCDM.PCDM_ReaderStatus: 
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
    def Read(self,theFileName : OCP.TCollection.TCollection_ExtendedString,theNewDocument : OCP.CDM.CDM_Document,theApplication : OCP.CDM.CDM_Application,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        None

        None
        """
    @overload
    def Read(self,theIStream : io.BytesIO,theStorageData : OCP.Storage.Storage_Data,theDoc : OCP.CDM.CDM_Document,theApplication : OCP.CDM.CDM_Application,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def ReadShapeSection(self,thePDoc : OCP.LDOM.LDOM_Element,theMsgDriver : OCP.Message.Message_Messenger,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.XmlMDF.XmlMDF_ADriver: 
        """
        None
        """
    @staticmethod
    def ReferenceCounter_s(theFileName : OCP.TCollection.TCollection_ExtendedString,theMsgDriver : OCP.Message.Message_Messenger) -> int: 
        """
        None
        """
    def SetFormat(self,aformat : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    def ShapeSetCleaning(self,theDriver : OCP.XmlMDF.XmlMDF_ADriver) -> None: 
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
class XmlDrivers_DocumentStorageDriver(OCP.XmlLDrivers.XmlLDrivers_DocumentStorageDriver, OCP.PCDM.PCDM_StorageDriver, OCP.PCDM.PCDM_Writer, OCP.Standard.Standard_Transient):
    def AttributeDrivers(self,theMsgDriver : OCP.Message.Message_Messenger) -> OCP.XmlMDF.XmlMDF_ADriverTable: 
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
    def GetFormat(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStoreStatus(self) -> OCP.PCDM.PCDM_StoreStatus: 
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
    def Make(self,aDocument : OCP.CDM.CDM_Document) -> OCP.PCDM.PCDM_Document: 
        """
        raises NotImplemented.

        By default, puts in the Sequence the document returns by the previous Make method.
        """
    @overload
    def Make(self,aDocument : OCP.CDM.CDM_Document,Documents : OCP.PCDM.PCDM_SequenceOfDocument) -> None: ...
    def SetFormat(self,aformat : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    def SetIsError(self,theIsError : bool) -> None: 
        """
        None
        """
    def SetStoreStatus(self,theStoreStatus : OCP.PCDM.PCDM_StoreStatus) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Write(self,theDocument : OCP.CDM.CDM_Document,theOStream : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        None

        None
        """
    @overload
    def Write(self,theDocument : OCP.CDM.CDM_Document,theFileName : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def WriteShapeSection(self,thePDoc : OCP.LDOM.LDOM_Element,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        None
        """
    def __init__(self,theCopyright : OCP.TCollection.TCollection_ExtendedString) -> None: ...
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
