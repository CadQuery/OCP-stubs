import OCP.BinLDrivers
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDocStd
import OCP.TCollection
import io
import OCP.NCollection
import OCP.Message
import OCP.BinMDF
import OCP.CDM
import OCP.PCDM
import OCP.Storage
import OCP.Standard
__all__  = [
"BinLDrivers",
"BinLDrivers_DocumentRetrievalDriver",
"BinLDrivers_DocumentSection",
"BinLDrivers_DocumentStorageDriver",
"BinLDrivers_Marker",
"BinLDrivers_VectorOfDocumentSection",
"BinLDrivers_ENDATTRLIST",
"BinLDrivers_ENDLABEL"
]
class BinLDrivers():
    """
    None
    """
    @staticmethod
    def AttributeDrivers_s(MsgDrv : OCP.Message.Message_Messenger) -> OCP.BinMDF.BinMDF_ADriverTable: 
        """
        Creates a table of the supported drivers' types
        """
    @staticmethod
    def DefineFormat_s(theApp : OCP.TDocStd.TDocStd_Application) -> None: 
        """
        Defines format "BinLOcaf" and registers its read and write drivers in the specified application
        """
    @staticmethod
    def Factory_s(theGUID : OCP.Standard.Standard_GUID) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    @staticmethod
    def StorageVersion_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns last storage version
        """
    def __init__(self) -> None: ...
    pass
class BinLDrivers_DocumentRetrievalDriver(OCP.PCDM.PCDM_RetrievalDriver, OCP.PCDM.PCDM_Reader, OCP.Standard.Standard_Transient):
    def AttributeDrivers(self,theMsgDriver : OCP.Message.Message_Messenger) -> OCP.BinMDF.BinMDF_ADriverTable: 
        """
        None
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
    def Read(self,theIStream : io.BytesIO,theStorageData : OCP.Storage.Storage_Data,theDoc : OCP.CDM.CDM_Document,theApplication : OCP.CDM.CDM_Application,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        retrieves the content of the file into a new Document.

        None
        """
    @overload
    def Read(self,theFileName : OCP.TCollection.TCollection_ExtendedString,theNewDocument : OCP.CDM.CDM_Document,theApplication : OCP.CDM.CDM_Application,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
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
class BinLDrivers_DocumentSection():
    """
    More or less independent part of the saved/restored document that is distinct from OCAF data themselves but may be referred by them.
    """
    def IsPostRead(self) -> bool: 
        """
        Query the status: if the Section should be read after OCAF; False means that the Section is read before starting to read OCAF data.
        """
    def Length(self) -> int: 
        """
        Query the length of the section in the persistent file
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Query the name of the section.
        """
    def Offset(self) -> int: 
        """
        Query the offset of the section in the persistent file
        """
    @staticmethod
    def ReadTOC_s(theSection : BinLDrivers_DocumentSection,theIS : io.BytesIO,theDocFormatVersion : int) -> None: 
        """
        Fill a DocumentSection instance from the data that are read from TOC.
        """
    def SetLength(self,theLength : int) -> None: 
        """
        Set the length of the section in the persistent file
        """
    def SetOffset(self,theOffset : int) -> None: 
        """
        Set the offset of the section in the persistent file
        """
    def Write(self,theOS : io.BytesIO,theOffset : int) -> None: 
        """
        Save Offset and Length data into the Section entry in the Document TOC (list of sections)
        """
    def WriteTOC(self,theOS : io.BytesIO) -> None: 
        """
        Create a Section entry in the Document TOC (list of sections)
        """
    @overload
    def __init__(self,theName : OCP.TCollection.TCollection_AsciiString,isPostRead : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BinLDrivers_DocumentStorageDriver(OCP.PCDM.PCDM_StorageDriver, OCP.PCDM.PCDM_Writer, OCP.Standard.Standard_Transient):
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
    def Write(self,theDocument : OCP.CDM.CDM_Document,theFileName : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Write <theDocument> to the binary file <theFileName>

        Write <theDocument> to theOStream
        """
    @overload
    def Write(self,theDocument : OCP.CDM.CDM_Document,theOStream : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
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
class BinLDrivers_Marker():
    """
    None

    Members:

      BinLDrivers_ENDATTRLIST

      BinLDrivers_ENDLABEL
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __init__(self,value : int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self,other : object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self,state : int) -> None: ...
    @property
    def name(self) -> None:
        """
        :type: None
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    BinLDrivers_ENDATTRLIST: OCP.BinLDrivers.BinLDrivers_Marker # value = <BinLDrivers_Marker.BinLDrivers_ENDATTRLIST: -1>
    BinLDrivers_ENDLABEL: OCP.BinLDrivers.BinLDrivers_Marker # value = <BinLDrivers_Marker.BinLDrivers_ENDLABEL: -2>
    __entries: dict # value = {'BinLDrivers_ENDATTRLIST': (<BinLDrivers_Marker.BinLDrivers_ENDATTRLIST: -1>, None), 'BinLDrivers_ENDLABEL': (<BinLDrivers_Marker.BinLDrivers_ENDLABEL: -2>, None)}
    __members__: dict # value = {'BinLDrivers_ENDATTRLIST': <BinLDrivers_Marker.BinLDrivers_ENDATTRLIST: -1>, 'BinLDrivers_ENDLABEL': <BinLDrivers_Marker.BinLDrivers_ENDLABEL: -2>}
    pass
class BinLDrivers_VectorOfDocumentSection(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BinLDrivers_DocumentSection) -> BinLDrivers_DocumentSection: 
        """
        Append
        """
    def Appended(self) -> BinLDrivers_DocumentSection: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BinLDrivers_VectorOfDocumentSection,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BinLDrivers_DocumentSection: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BinLDrivers_DocumentSection: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BinLDrivers_DocumentSection: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BinLDrivers_DocumentSection: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BinLDrivers_DocumentSection: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BinLDrivers_DocumentSection) -> BinLDrivers_DocumentSection: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BinLDrivers_DocumentSection: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BinLDrivers_VectorOfDocumentSection) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
BinLDrivers_ENDATTRLIST: OCP.BinLDrivers.BinLDrivers_Marker # value = <BinLDrivers_Marker.BinLDrivers_ENDATTRLIST: -1>
BinLDrivers_ENDLABEL: OCP.BinLDrivers.BinLDrivers_Marker # value = <BinLDrivers_Marker.BinLDrivers_ENDLABEL: -2>
