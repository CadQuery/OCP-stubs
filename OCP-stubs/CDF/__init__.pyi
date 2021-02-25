import OCP.CDF
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import io
import OCP.Message
import OCP.CDM
import OCP.PCDM
import OCP.Resource
import OCP.Standard
__all__  = [
"CDF_Application",
"CDF_Directory",
"CDF_DirectoryIterator",
"CDF_MetaDataDriver",
"CDF_FWOSDriver",
"CDF_MetaDataDriverError",
"CDF_MetaDataDriverFactory",
"CDF_Store",
"CDF_StoreList",
"CDF_StoreSetNameStatus",
"CDF_SubComponentStatus",
"CDF_TryStoreStatus",
"CDF_TypeOfActivation",
"CDF_SCS_Consistent",
"CDF_SCS_Modified",
"CDF_SCS_Stored",
"CDF_SCS_Unconsistent",
"CDF_SSNS_OK",
"CDF_SSNS_OpenDocument",
"CDF_SSNS_ReplacingAnExistentDocument",
"CDF_TOA_Modified",
"CDF_TOA_New",
"CDF_TOA_Unchanged",
"CDF_TS_NoCurrentDocument",
"CDF_TS_NoDriver",
"CDF_TS_NoSubComponentDriver",
"CDF_TS_OK"
]
class CDF_Application(OCP.CDM.CDM_Application, OCP.Standard.Standard_Transient):
    def BeginOfUpdate(self,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        this method is called before the update of a document. By default, writes in MessageDriver().
        """
    def CanClose(self,aDocument : OCP.CDM.CDM_Document) -> OCP.CDM.CDM_CanCloseStatus: 
        """
        None
        """
    @overload
    def CanRetrieve(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString) -> OCP.PCDM.PCDM_ReaderStatus: 
        """
        None

        None
        """
    @overload
    def CanRetrieve(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString) -> OCP.PCDM.PCDM_ReaderStatus: ...
    def Close(self,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        removes the document of the current session directory and closes the document;
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultFolder(self) -> str: 
        """
        None
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndOfUpdate(self,aDocument : OCP.CDM.CDM_Document,theStatus : bool,ErrorString : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        this method is called affter the update of a document. By default, writes in MessageDriver().
        """
    def Format(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theFormat : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        try to retrieve a Format directly in the file or in application resource by using extension. returns True if found;
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRetrieveStatus(self) -> OCP.PCDM.PCDM_ReaderStatus: 
        """
        Checks status after Retrieve
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
    def Load_s(aGUID : OCP.Standard.Standard_GUID) -> CDF_Application: 
        """
        plugs an application.
        """
    def MessageDriver(self) -> OCP.Message.Message_Messenger: 
        """
        Returns default messenger;
        """
    def MetaDataDriver(self) -> CDF_MetaDataDriver: 
        """
        returns MetaDatdDriver of this application
        """
    def MetaDataLookUpTable(self) -> Any: 
        """
        Returns MetaData LookUpTable
        """
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the application name.
        """
    def Open(self,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        puts the document in the current session directory and calls the virtual method Activate on it.
        """
    def Read(self,theIStream : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.CDM.CDM_Document: 
        """
        Reads aDoc from standard SEEKABLE stream theIStream, the stream should support SEEK fuctionality
        """
    def ReaderFromFormat(self,aFormat : OCP.TCollection.TCollection_ExtendedString) -> OCP.PCDM.PCDM_Reader: 
        """
        Returns instance of read driver for specified format.
        """
    def Resources(self) -> OCP.Resource.Resource_Manager: 
        """
        The manager returned by this virtual method will be used to search for Format.Retrieval resource items.
        """
    @overload
    def Retrieve(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,UseStorageConfiguration : bool=True,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.CDM.CDM_Document: 
        """
        This method retrieves a document from the database. If the Document references other documents which have been updated, the latest version of these documents will be used if {UseStorageConfiguration} is Standard_True. The content of {aFolder}, {aName} and {aVersion} depends on the Database Manager system. If the DBMS is only based on the OS, {aFolder} is a directory and {aName} is the name of a file. In this case the use of the syntax with {aVersion} has no sense. For example:

        This method retrieves a document from the database. If the Document references other documents which have been updated, the latest version of these documents will be used if {UseStorageConfiguration} is Standard_True. -- If the DBMS is only based on the OS, this syntax should not be used.
        """
    @overload
    def Retrieve(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString,UseStorageConfiguration : bool=True,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.CDM.CDM_Document: ...
    def SetDefaultFolder(self,aFolder : str) -> bool: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Version(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the application version.
        """
    def Write(self,aString : str) -> None: 
        """
        writes the string in the application MessagerDriver.
        """
    def WriterFromFormat(self,aFormat : OCP.TCollection.TCollection_ExtendedString) -> OCP.PCDM.PCDM_StorageDriver: 
        """
        Returns instance of storage driver for specified format.
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
class CDF_Directory(OCP.Standard.Standard_Transient):
    """
    A directory is a collection of documents. There is only one instance of a given document in a directory. put.A directory is a collection of documents. There is only one instance of a given document in a directory. put.A directory is a collection of documents. There is only one instance of a given document in a directory. put.
    """
    def Add(self,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        adds a document into the directory.
        """
    def Contains(self,aDocument : OCP.CDM.CDM_Document) -> bool: 
        """
        Returns true if the document aDocument is in the directory
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
    def IsEmpty(self) -> bool: 
        """
        returns true if the directory is empty.
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
    def Last(self) -> OCP.CDM.CDM_Document: 
        """
        returns the last document (if any) which has been added in the directory.
        """
    def Length(self) -> int: 
        """
        returns the number of documents of the directory.
        """
    def Remove(self,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        removes the document.
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
class CDF_DirectoryIterator():
    """
    None
    """
    def Document(self) -> OCP.CDM.CDM_Document: 
        """
        Returns item value of current entry
        """
    def MoreDocument(self) -> bool: 
        """
        Returns True if there are more entries to return
        """
    def NextDocument(self) -> None: 
        """
        Go to the next entry (if there is not, Value will raise an exception)
        """
    def __init__(self,aDirectory : CDF_Directory) -> None: ...
    pass
class CDF_MetaDataDriver(OCP.Standard.Standard_Transient):
    """
    this class list the method that must be available for a specific DBMSthis class list the method that must be available for a specific DBMSthis class list the method that must be available for a specific DBMS
    """
    def BuildFileName(self,aDocument : OCP.CDM.CDM_Document) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def CreateDependsOn(self,aFirstData : OCP.CDM.CDM_MetaData,aSecondData : OCP.CDM.CDM_MetaData) -> None: 
        """
        Creates a "Depends On" relation between two Datas. By default does nothing
        """
    def CreateMetaData(self,aDocument : OCP.CDM.CDM_Document,aFileName : OCP.TCollection.TCollection_ExtendedString) -> OCP.CDM.CDM_MetaData: 
        """
        should create meta-data corresponding to aData and maintaining a meta-link between these meta-data and aFileName CreateMetaData is called by CreateData If the metadata-driver has version capabilities, version must be set in the returned Data.
        """
    def CreateReference(self,aFrom : OCP.CDM.CDM_MetaData,aTo : OCP.CDM.CDM_MetaData,aReferenceIdentifier : int,aToDocumentVersion : int) -> None: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultFolder(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def Find(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        should indicate whether meta-data exist in the DBMS corresponding to the Data. aVersion may be NULL;

        calls Find with an empty version
        """
    @overload
    def Find(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    def FindFolder(self,aFolder : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasReadPermission(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        None
        """
    def HasVersion(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        by default return Standard_True.
        """
    def HasVersionCapability(self) -> bool: 
        """
        returns true if the MetaDataDriver can manage different versions of a Data. By default, returns Standard_False.
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
    def LastVersion(self,aMetaData : OCP.CDM.CDM_MetaData) -> OCP.CDM.CDM_MetaData: 
        """
        by default returns aMetaDATA should return the MetaData stored in the DBMS with the meta-data corresponding to the path. If the MetaDataDriver has version management capabilities the version has to be set in the returned MetaData. MetaData is called by GetMetaData If the version is not included in the path , MetaData should return the last version of the metadata is deferred;
        """
    @overload
    def MetaData(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString) -> OCP.CDM.CDM_MetaData: 
        """
        should return the MetaData stored in the DBMS with the meta-data corresponding to the Data. If the MetaDataDriver has version management capabilities the version has to be set in the returned MetaData. aVersion may be NULL MetaData is called by GetMetaData If the version is set to NULL, MetaData should return the last version of the metadata

        calls MetaData with an empty version
        """
    @overload
    def MetaData(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString) -> OCP.CDM.CDM_MetaData: ...
    def ReferenceIterator(self,theMessageDriver : OCP.Message.Message_Messenger) -> OCP.PCDM.PCDM_ReferenceIterator: 
        """
        None
        """
    def SetName(self,aDocument : OCP.CDM.CDM_Document,aName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        this methods is usefull if the name of an object -- depends on the metadatadriver. For example a Driver -- based on the operating system can choose to add the extension of file to create to the object.
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
class CDF_FWOSDriver(CDF_MetaDataDriver, OCP.Standard.Standard_Transient):
    def BuildFileName(self,aDocument : OCP.CDM.CDM_Document) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def CreateDependsOn(self,aFirstData : OCP.CDM.CDM_MetaData,aSecondData : OCP.CDM.CDM_MetaData) -> None: 
        """
        Creates a "Depends On" relation between two Datas. By default does nothing
        """
    def CreateMetaData(self,aDocument : OCP.CDM.CDM_Document,aFileName : OCP.TCollection.TCollection_ExtendedString) -> OCP.CDM.CDM_MetaData: 
        """
        should create meta-data corresponding to aData and maintaining a meta-link between these meta-data and aFileName CreateMetaData is called by CreateData If the metadata-driver has version capabilities, version must be set in the returned Data.
        """
    def CreateReference(self,aFrom : OCP.CDM.CDM_MetaData,aTo : OCP.CDM.CDM_MetaData,aReferenceIdentifier : int,aToDocumentVersion : int) -> None: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultFolder(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Find(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        indicate whether a file exists corresponding to the folder and the name
        """
    def FindFolder(self,aFolder : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasReadPermission(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        None
        """
    def HasVersion(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        by default return Standard_True.
        """
    def HasVersionCapability(self) -> bool: 
        """
        returns true if the MetaDataDriver can manage different versions of a Data. By default, returns Standard_False.
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
    def LastVersion(self,aMetaData : OCP.CDM.CDM_MetaData) -> OCP.CDM.CDM_MetaData: 
        """
        by default returns aMetaDATA should return the MetaData stored in the DBMS with the meta-data corresponding to the path. If the MetaDataDriver has version management capabilities the version has to be set in the returned MetaData. MetaData is called by GetMetaData If the version is not included in the path , MetaData should return the last version of the metadata is deferred;
        """
    @overload
    def MetaData(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString) -> OCP.CDM.CDM_MetaData: 
        """
        should return the MetaData stored in the DBMS with the meta-data corresponding to the Data. If the MetaDataDriver has version management capabilities the version has to be set in the returned MetaData. aVersion may be NULL MetaData is called by GetMetaData If the version is set to NULL, MetaData should return the last version of the metadata

        calls MetaData with an empty version
        """
    @overload
    def MetaData(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString) -> OCP.CDM.CDM_MetaData: ...
    def ReferenceIterator(self,theMessageDriver : OCP.Message.Message_Messenger) -> OCP.PCDM.PCDM_ReferenceIterator: 
        """
        None
        """
    def SetName(self,aDocument : OCP.CDM.CDM_Document,aName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theLookUpTable : Any) -> None: ...
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
class CDF_MetaDataDriverError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.CDF', '__weakref__': <attribute '__weakref__' of 'CDF_MetaDataDriverError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'CDF_MetaDataDriverError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class CDF_MetaDataDriverFactory(OCP.Standard.Standard_Transient):
    def Build(self) -> CDF_MetaDataDriver: 
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
class CDF_Store():
    """
    None
    """
    def AssociatedStatusText(self) -> str: 
        """
        None
        """
    def Comment(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        None
        """
    def CurrentIsConsistent(self) -> bool: 
        """
        None
        """
    def Description(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        returns the description of the format of the main object.
        """
    def Folder(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        returns the folder in which the current document will be stored.
        """
    def HasAPreviousVersion(self) -> bool: 
        """
        None
        """
    def IsConsistent(self) -> bool: 
        """
        None
        """
    def IsMainDocument(self) -> bool: 
        """
        returns true if the currentdocument is the main one, ie the document of the current selection.
        """
    def IsModified(self) -> bool: 
        """
        None
        """
    def IsStored(self) -> bool: 
        """
        returns true if the current document is already stored
        """
    def MetaDataPath(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        returns the path of the previous store is the object is already stored, otherwise an empty string;
        """
    def Name(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        returns the name under which the current document will be stored
        """
    def Path(self) -> str: 
        """
        returns the complete path of the created meta-data.
        """
    def PreviousVersion(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        None
        """
    def Realize(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        None
        """
    def RecheckName(self) -> CDF_StoreSetNameStatus: 
        """
        defines the name under which the document should be stored. uses for example after modification of the folder.
        """
    def SetComment(self,aComment : str) -> None: 
        """
        None
        """
    def SetCurrent(self,aPresentation : str) -> None: 
        """
        None
        """
    @overload
    def SetFolder(self,aFolder : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        defines the folder in which the document should be stored. returns Standard_True if the Folder exists, Standard_False otherwise.

        defines the folder in which the document should be stored. returns Standard_True if the Folder exists, Standard_False otherwise.
        """
    @overload
    def SetFolder(self,aFolder : str) -> bool: ...
    def SetMain(self) -> None: 
        """
        the two following methods can be used just after Realize or Import -- method to know if thes methods worked correctly, and if not why.
        """
    @overload
    def SetName(self,aName : OCP.TCollection.TCollection_ExtendedString) -> CDF_StoreSetNameStatus: 
        """
        defines the name under which the document should be stored.

        defines the name under which the document should be stored.
        """
    @overload
    def SetName(self,aName : str) -> CDF_StoreSetNameStatus: ...
    def SetPreviousVersion(self,aPreviousVersion : str) -> bool: 
        """
        None
        """
    def StoreStatus(self) -> OCP.PCDM.PCDM_StoreStatus: 
        """
        None
        """
    def __init__(self,aDocument : OCP.CDM.CDM_Document) -> None: ...
    pass
class CDF_StoreList(OCP.Standard.Standard_Transient):
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
    def Init(self) -> None: 
        """
        None
        """
    def IsConsistent(self) -> bool: 
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
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def Store(self,aMetaData : OCP.CDM.CDM_MetaData,aStatusAssociatedText : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: 
        """
        stores each object of the storelist in the reverse order of which they had been added.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> OCP.CDM.CDM_Document: 
        """
        None
        """
    def __init__(self,aDocument : OCP.CDM.CDM_Document) -> None: ...
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
class CDF_StoreSetNameStatus():
    """
    None

    Members:

      CDF_SSNS_OK

      CDF_SSNS_ReplacingAnExistentDocument

      CDF_SSNS_OpenDocument
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
    CDF_SSNS_OK: OCP.CDF.CDF_StoreSetNameStatus # value = <CDF_StoreSetNameStatus.CDF_SSNS_OK: 0>
    CDF_SSNS_OpenDocument: OCP.CDF.CDF_StoreSetNameStatus # value = <CDF_StoreSetNameStatus.CDF_SSNS_OpenDocument: 2>
    CDF_SSNS_ReplacingAnExistentDocument: OCP.CDF.CDF_StoreSetNameStatus # value = <CDF_StoreSetNameStatus.CDF_SSNS_ReplacingAnExistentDocument: 1>
    __entries: dict # value = {'CDF_SSNS_OK': (<CDF_StoreSetNameStatus.CDF_SSNS_OK: 0>, None), 'CDF_SSNS_ReplacingAnExistentDocument': (<CDF_StoreSetNameStatus.CDF_SSNS_ReplacingAnExistentDocument: 1>, None), 'CDF_SSNS_OpenDocument': (<CDF_StoreSetNameStatus.CDF_SSNS_OpenDocument: 2>, None)}
    __members__: dict # value = {'CDF_SSNS_OK': <CDF_StoreSetNameStatus.CDF_SSNS_OK: 0>, 'CDF_SSNS_ReplacingAnExistentDocument': <CDF_StoreSetNameStatus.CDF_SSNS_ReplacingAnExistentDocument: 1>, 'CDF_SSNS_OpenDocument': <CDF_StoreSetNameStatus.CDF_SSNS_OpenDocument: 2>}
    pass
class CDF_SubComponentStatus():
    """
    None

    Members:

      CDF_SCS_Consistent

      CDF_SCS_Unconsistent

      CDF_SCS_Stored

      CDF_SCS_Modified
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
    CDF_SCS_Consistent: OCP.CDF.CDF_SubComponentStatus # value = <CDF_SubComponentStatus.CDF_SCS_Consistent: 0>
    CDF_SCS_Modified: OCP.CDF.CDF_SubComponentStatus # value = <CDF_SubComponentStatus.CDF_SCS_Modified: 3>
    CDF_SCS_Stored: OCP.CDF.CDF_SubComponentStatus # value = <CDF_SubComponentStatus.CDF_SCS_Stored: 2>
    CDF_SCS_Unconsistent: OCP.CDF.CDF_SubComponentStatus # value = <CDF_SubComponentStatus.CDF_SCS_Unconsistent: 1>
    __entries: dict # value = {'CDF_SCS_Consistent': (<CDF_SubComponentStatus.CDF_SCS_Consistent: 0>, None), 'CDF_SCS_Unconsistent': (<CDF_SubComponentStatus.CDF_SCS_Unconsistent: 1>, None), 'CDF_SCS_Stored': (<CDF_SubComponentStatus.CDF_SCS_Stored: 2>, None), 'CDF_SCS_Modified': (<CDF_SubComponentStatus.CDF_SCS_Modified: 3>, None)}
    __members__: dict # value = {'CDF_SCS_Consistent': <CDF_SubComponentStatus.CDF_SCS_Consistent: 0>, 'CDF_SCS_Unconsistent': <CDF_SubComponentStatus.CDF_SCS_Unconsistent: 1>, 'CDF_SCS_Stored': <CDF_SubComponentStatus.CDF_SCS_Stored: 2>, 'CDF_SCS_Modified': <CDF_SubComponentStatus.CDF_SCS_Modified: 3>}
    pass
class CDF_TryStoreStatus():
    """
    None

    Members:

      CDF_TS_OK

      CDF_TS_NoCurrentDocument

      CDF_TS_NoDriver

      CDF_TS_NoSubComponentDriver
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
    CDF_TS_NoCurrentDocument: OCP.CDF.CDF_TryStoreStatus # value = <CDF_TryStoreStatus.CDF_TS_NoCurrentDocument: 1>
    CDF_TS_NoDriver: OCP.CDF.CDF_TryStoreStatus # value = <CDF_TryStoreStatus.CDF_TS_NoDriver: 2>
    CDF_TS_NoSubComponentDriver: OCP.CDF.CDF_TryStoreStatus # value = <CDF_TryStoreStatus.CDF_TS_NoSubComponentDriver: 3>
    CDF_TS_OK: OCP.CDF.CDF_TryStoreStatus # value = <CDF_TryStoreStatus.CDF_TS_OK: 0>
    __entries: dict # value = {'CDF_TS_OK': (<CDF_TryStoreStatus.CDF_TS_OK: 0>, None), 'CDF_TS_NoCurrentDocument': (<CDF_TryStoreStatus.CDF_TS_NoCurrentDocument: 1>, None), 'CDF_TS_NoDriver': (<CDF_TryStoreStatus.CDF_TS_NoDriver: 2>, None), 'CDF_TS_NoSubComponentDriver': (<CDF_TryStoreStatus.CDF_TS_NoSubComponentDriver: 3>, None)}
    __members__: dict # value = {'CDF_TS_OK': <CDF_TryStoreStatus.CDF_TS_OK: 0>, 'CDF_TS_NoCurrentDocument': <CDF_TryStoreStatus.CDF_TS_NoCurrentDocument: 1>, 'CDF_TS_NoDriver': <CDF_TryStoreStatus.CDF_TS_NoDriver: 2>, 'CDF_TS_NoSubComponentDriver': <CDF_TryStoreStatus.CDF_TS_NoSubComponentDriver: 3>}
    pass
class CDF_TypeOfActivation():
    """
    None

    Members:

      CDF_TOA_New

      CDF_TOA_Modified

      CDF_TOA_Unchanged
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
    CDF_TOA_Modified: OCP.CDF.CDF_TypeOfActivation # value = <CDF_TypeOfActivation.CDF_TOA_Modified: 1>
    CDF_TOA_New: OCP.CDF.CDF_TypeOfActivation # value = <CDF_TypeOfActivation.CDF_TOA_New: 0>
    CDF_TOA_Unchanged: OCP.CDF.CDF_TypeOfActivation # value = <CDF_TypeOfActivation.CDF_TOA_Unchanged: 2>
    __entries: dict # value = {'CDF_TOA_New': (<CDF_TypeOfActivation.CDF_TOA_New: 0>, None), 'CDF_TOA_Modified': (<CDF_TypeOfActivation.CDF_TOA_Modified: 1>, None), 'CDF_TOA_Unchanged': (<CDF_TypeOfActivation.CDF_TOA_Unchanged: 2>, None)}
    __members__: dict # value = {'CDF_TOA_New': <CDF_TypeOfActivation.CDF_TOA_New: 0>, 'CDF_TOA_Modified': <CDF_TypeOfActivation.CDF_TOA_Modified: 1>, 'CDF_TOA_Unchanged': <CDF_TypeOfActivation.CDF_TOA_Unchanged: 2>}
    pass
CDF_SCS_Consistent: OCP.CDF.CDF_SubComponentStatus # value = <CDF_SubComponentStatus.CDF_SCS_Consistent: 0>
CDF_SCS_Modified: OCP.CDF.CDF_SubComponentStatus # value = <CDF_SubComponentStatus.CDF_SCS_Modified: 3>
CDF_SCS_Stored: OCP.CDF.CDF_SubComponentStatus # value = <CDF_SubComponentStatus.CDF_SCS_Stored: 2>
CDF_SCS_Unconsistent: OCP.CDF.CDF_SubComponentStatus # value = <CDF_SubComponentStatus.CDF_SCS_Unconsistent: 1>
CDF_SSNS_OK: OCP.CDF.CDF_StoreSetNameStatus # value = <CDF_StoreSetNameStatus.CDF_SSNS_OK: 0>
CDF_SSNS_OpenDocument: OCP.CDF.CDF_StoreSetNameStatus # value = <CDF_StoreSetNameStatus.CDF_SSNS_OpenDocument: 2>
CDF_SSNS_ReplacingAnExistentDocument: OCP.CDF.CDF_StoreSetNameStatus # value = <CDF_StoreSetNameStatus.CDF_SSNS_ReplacingAnExistentDocument: 1>
CDF_TOA_Modified: OCP.CDF.CDF_TypeOfActivation # value = <CDF_TypeOfActivation.CDF_TOA_Modified: 1>
CDF_TOA_New: OCP.CDF.CDF_TypeOfActivation # value = <CDF_TypeOfActivation.CDF_TOA_New: 0>
CDF_TOA_Unchanged: OCP.CDF.CDF_TypeOfActivation # value = <CDF_TypeOfActivation.CDF_TOA_Unchanged: 2>
CDF_TS_NoCurrentDocument: OCP.CDF.CDF_TryStoreStatus # value = <CDF_TryStoreStatus.CDF_TS_NoCurrentDocument: 1>
CDF_TS_NoDriver: OCP.CDF.CDF_TryStoreStatus # value = <CDF_TryStoreStatus.CDF_TS_NoDriver: 2>
CDF_TS_NoSubComponentDriver: OCP.CDF.CDF_TryStoreStatus # value = <CDF_TryStoreStatus.CDF_TS_NoSubComponentDriver: 3>
CDF_TS_OK: OCP.CDF.CDF_TryStoreStatus # value = <CDF_TryStoreStatus.CDF_TS_OK: 0>
