import OCP.BinDrivers
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDocStd
import OCP.TCollection
import OCP.Storage
import OCP.Standard
import OCP.Message
import OCP.BinMDF
import OCP.BinLDrivers
import OCP.PCDM
import OCP.CDM
__all__  = [
"BinDrivers",
"BinDrivers_DocumentRetrievalDriver",
"BinDrivers_DocumentStorageDriver",
"BinDrivers_Marker",
"BinDrivers_ENDATTRLIST",
"BinDrivers_ENDLABEL"
]
class BinDrivers():
    """
    None
    """
    @staticmethod
    def AttributeDrivers_s(MsgDrv : OCP.Message.Message_Messenger) -> OCP.BinMDF.BinMDF_ADriverTable: 
        """
        Creates the table of drivers of types supported
        """
    @staticmethod
    def DefineFormat_s(theApp : OCP.TDocStd.TDocStd_Application) -> None: 
        """
        Defines format "BinOcaf" and registers its read and write drivers in the specified application
        """
    @staticmethod
    def Factory_s(theGUID : OCP.Standard.Standard_GUID) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    @staticmethod
    def StorageVersion_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns "1"
        """
    def __init__(self) -> None: ...
    pass
class BinDrivers_DocumentRetrievalDriver(OCP.BinLDrivers.BinLDrivers_DocumentRetrievalDriver, OCP.PCDM.PCDM_RetrievalDriver, OCP.PCDM.PCDM_Reader, OCP.Standard.Standard_Transient):
    def AttributeDrivers(self,theMsgDriver : OCP.Message.Message_Messenger) -> OCP.BinMDF.BinMDF_ADriverTable: 
        """
        None
        """
    def CheckShapeSection(self,thePos : int,theIS : Any) -> None: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Clears the NamedShape driver
        """
    def CreateDocument(self) -> OCP.CDM.CDM_Document: 
        """
        pure virtual method definition
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
    @overload
    def Read(self,theFileName : OCP.TCollection.TCollection_ExtendedString,theNewDocument : OCP.CDM.CDM_Document,theApplication : OCP.CDM.CDM_Application) -> None: 
        """
        retrieves the content of the file into a new Document.

        None
        """
    @overload
    def Read(self,theIStream : Any,theStorageData : OCP.Storage.Storage_Data,theDoc : OCP.CDM.CDM_Document,theApplication : OCP.CDM.CDM_Application) -> None: ...
    def ReadShapeSection(self,theSection : OCP.BinLDrivers.BinLDrivers_DocumentSection,theIS : Any,isMess : bool=False) -> None: 
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
class BinDrivers_DocumentStorageDriver(OCP.BinLDrivers.BinLDrivers_DocumentStorageDriver, OCP.PCDM.PCDM_StorageDriver, OCP.PCDM.PCDM_Writer, OCP.Standard.Standard_Transient):
    """
    persistent implemention of storage a document in a binary filepersistent implemention of storage a document in a binary filepersistent implemention of storage a document in a binary file
    """
    def AddSection(self,theName : OCP.TCollection.TCollection_AsciiString,isPostRead : bool=True) -> None: 
        """
        Create a section that should be written after the OCAF data
        """
    def AttributeDrivers(self,theMsgDriver : OCP.Message.Message_Messenger) -> OCP.BinMDF.BinMDF_ADriverTable: 
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
    def IsWithTriangles(self) -> bool: 
        """
        Return true if shape should be stored with triangles.
        """
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
    def SetWithTriangles(self,theMessageDriver : OCP.Message.Message_Messenger,theWithTriangulation : bool) -> None: 
        """
        Set if triangulation should be stored or not.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Write(self,theDocument : OCP.CDM.CDM_Document,theFileName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Write <theDocument> to the binary file <theFileName>

        Write <theDocument> to theOStream
        """
    @overload
    def Write(self,theDocument : OCP.CDM.CDM_Document,theOStream : Any) -> None: ...
    def WriteShapeSection(self,theDocSection : OCP.BinLDrivers.BinLDrivers_DocumentSection,theOS : Any) -> None: 
        """
        implements the procedure of writing a shape section to file
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
class BinDrivers_Marker():
    """
    None

    Members:

      BinDrivers_ENDATTRLIST

      BinDrivers_ENDLABEL
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BinDrivers_ENDATTRLIST: OCP.BinDrivers.BinDrivers_Marker # value = BinDrivers_Marker.BinDrivers_ENDATTRLIST
    BinDrivers_ENDLABEL: OCP.BinDrivers.BinDrivers_Marker # value = BinDrivers_Marker.BinDrivers_ENDLABEL
    __entries: dict # value = {'BinDrivers_ENDATTRLIST': (BinDrivers_Marker.BinDrivers_ENDATTRLIST, None), 'BinDrivers_ENDLABEL': (BinDrivers_Marker.BinDrivers_ENDLABEL, None)}
    __members__: dict # value = {'BinDrivers_ENDATTRLIST': BinDrivers_Marker.BinDrivers_ENDATTRLIST, 'BinDrivers_ENDLABEL': BinDrivers_Marker.BinDrivers_ENDLABEL}
    pass
BinDrivers_ENDATTRLIST: OCP.BinDrivers.BinDrivers_Marker # value = BinDrivers_Marker.BinDrivers_ENDATTRLIST
BinDrivers_ENDLABEL: OCP.BinDrivers.BinDrivers_Marker # value = BinDrivers_Marker.BinDrivers_ENDLABEL
