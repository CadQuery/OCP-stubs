import OCP.TObj
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Resource
import OCP.TDocStd
import OCP.TCollection
import OCP.CDF
import OCP.NCollection
import OCP.Message
import OCP.gp
import OCP.TDF
import OCP.CDM
import OCP.Standard
import OCP.PCDM
import OCP.TColStd
import io
__all__  = [
"TObj_Application",
"TObj_Assistant",
"TObj_CheckModel",
"TObj_DataMapOfNameLabel",
"TObj_DataMapOfStringPointer",
"TObj_DeletingMode",
"TObj_SequenceOfObject",
"TObj_Object",
"TObj_ObjectIterator",
"TObj_Model",
"TObj_ModelIterator",
"TObj_Partition",
"TObj_LabelIterator",
"TObj_OcafObjectIterator",
"TObj_HiddenPartition",
"TObj_Persistence",
"TObj_ReferenceIterator",
"TObj_SequenceIterator",
"TObj_SequenceOfIterator",
"TObj_HSequenceOfObject",
"TObj_TIntSparseArray",
"TObj_TIntSparseArray_VecOfData",
"TObj_TModel",
"TObj_TNameContainer",
"TObj_TObject",
"TObj_TReference",
"TObj_TXYZ",
"HashCode",
"IsEqual",
"TObj_Forced",
"TObj_FreeOnly",
"TObj_KeepDepending"
]
class TObj_Application(OCP.TDocStd.TDocStd_Application, OCP.CDF.CDF_Application, OCP.CDM.CDM_Application, OCP.Standard.Standard_Transient):
    """
    This is a base class for OCAF based TObj models with declared virtual methodsThis is a base class for OCAF based TObj models with declared virtual methods
    """
    def BeginOfUpdate(self,aDocument : OCP.CDM.CDM_Document) -> None: 
        """
        this method is called before the update of a document. By default, writes in MessageDriver().
        """
    def CanClose(self,aDocument : OCP.CDM.CDM_Document) -> OCP.CDM.CDM_CanCloseStatus: 
        """
        None
        """
    @overload
    def CanRetrieve(self,theFolder : OCP.TCollection.TCollection_ExtendedString,theName : OCP.TCollection.TCollection_ExtendedString,theAppendMode : bool) -> OCP.PCDM.PCDM_ReaderStatus: 
        """
        None

        None
        """
    @overload
    def CanRetrieve(self,theFolder : OCP.TCollection.TCollection_ExtendedString,theName : OCP.TCollection.TCollection_ExtendedString,theVersion : OCP.TCollection.TCollection_ExtendedString,theAppendMode : bool) -> OCP.PCDM.PCDM_ReaderStatus: ...
    def Close(self,aDoc : OCP.TDocStd.TDocStd_Document) -> None: 
        """
        Close the given document. the document is not any more handled by the applicative session.
        """
    def CreateNewDocument(self,theDoc : OCP.TDocStd.TDocStd_Document,theFormat : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Create the OCAF document from scratch
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultFolder(self) -> str: 
        """
        None
        """
    def DefineFormat(self,theFormat : OCP.TCollection.TCollection_AsciiString,theDescription : OCP.TCollection.TCollection_AsciiString,theExtension : OCP.TCollection.TCollection_AsciiString,theReader : OCP.PCDM.PCDM_RetrievalDriver,theWriter : OCP.PCDM.PCDM_StorageDriver) -> None: 
        """
        Sets up resources and registers read and storage drivers for the specified format.
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
    @overload
    def ErrorMessage(self,theMsg : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Signal error during Load or Save Default imiplementation is empty

        Signal error during Load or Save Default imiplementation invoke previous declaration with 0
        """
    @overload
    def ErrorMessage(self,theMsg : OCP.TCollection.TCollection_ExtendedString,theLevel : OCP.Message.Message_Gravity) -> None: ...
    def Format(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theFormat : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        try to retrieve a Format directly in the file or in application resource by using extension. returns True if found;
        """
    def GetDocument(self,index : int,aDoc : OCP.TDocStd.TDocStd_Document) -> Any: 
        """
        Constructs the new document aDoc. aDoc is identified by the index index which is any integer between 1 and n where n is the number of documents returned by NbDocument. Example Handle(TDocStd_Application) anApp; if (!CafTest::Find(A)) return 1; Handle(TDocStd) aDoc; Standard_Integer nbdoc = anApp->NbDocuments(); for (Standard_Integer i = 1; i <= nbdoc; i++) { aApp->GetDocument(i,aDoc);
        """
    @staticmethod
    def GetInstance_s() -> TObj_Application: 
        """
        Returns static instance of the application
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
    def InitDocument(self,aDoc : OCP.CDM.CDM_Document) -> None: 
        """
        Initialize the document aDoc for the applicative session. This virtual function is called by NewDocument and is to be redefined for each specific application. Modified flag (different of disk version) ============= to open/save a document =======================
        """
    def IsDriverLoaded(self) -> bool: 
        """
        Check if meta data driver was successfully loaded by the application constructor
        """
    def IsInSession(self,path : OCP.TCollection.TCollection_ExtendedString) -> int: 
        """
        Returns an index for the document found in the path path in this applicative session. If the returned value is 0, the document is not present in the applicative session. This method can be used for the interactive part of an application. For instance, on a call to Open, the document to be opened may already be in memory. IsInSession checks to see if this is the case. Open can be made to depend on the value of the index returned: if IsInSession returns 0, the document is opened; if it returns another value, a message is displayed asking the user if he wants to override the version of the document in memory. Example: Standard_Integer insession = A->IsInSession(aDoc); if (insession > 0) { std::cout << "document " << insession << " is already in session" << std::endl; return 0; }
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
    def IsVerbose(self) -> bool: 
        """
        Returns the verbose flag
        """
    @overload
    def LoadDocument(self,theIStream : io.BytesIO,theTargetDoc : OCP.TDocStd.TDocStd_Document) -> bool: 
        """
        Loading the OCAF document from a file

        Loading the OCAF document from a stream
        """
    @overload
    def LoadDocument(self,theSourceFile : OCP.TCollection.TCollection_ExtendedString,theTargetDoc : OCP.TDocStd.TDocStd_Document) -> bool: ...
    @staticmethod
    def Load_s(aGUID : OCP.Standard.Standard_GUID) -> OCP.CDF.CDF_Application: 
        """
        plugs an application.
        """
    def MessageDriver(self) -> OCP.Message.Message_Messenger: 
        """
        Returns default messenger;
        """
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns reference to associated messenger handle
        """
    def MetaDataDriver(self) -> OCP.CDF.CDF_MetaDataDriver: 
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
    def NbDocuments(self) -> int: 
        """
        returns the number of documents handled by the current applicative session.
        """
    @overload
    def NewDocument(self,format : OCP.TCollection.TCollection_ExtendedString,aDoc : OCP.TDocStd.TDocStd_Document) -> Any: 
        """
        Constructs the empty new document aDoc. This document will have the format format. If InitDocument is redefined for a specific application, the new document is handled by the applicative session.

        A non-virtual method taking a TDocStd_Documment object as an input. Internally it calls a virtual method NewDocument() with CDM_Document object.
        """
    @overload
    def NewDocument(self,format : OCP.TCollection.TCollection_ExtendedString,aDoc : OCP.CDM.CDM_Document) -> Any: ...
    def OnAbortTransaction(self,theDoc : OCP.TDocStd.TDocStd_Document) -> None: 
        """
        Notification that is fired at each AbortTransaction event.
        """
    def OnCommitTransaction(self,theDoc : OCP.TDocStd.TDocStd_Document) -> None: 
        """
        Notification that is fired at each CommitTransaction event.
        """
    def OnOpenTransaction(self,theDoc : OCP.TDocStd.TDocStd_Document) -> None: 
        """
        Notification that is fired at each OpenTransaction event.
        """
    @overload
    def Open(self,thePath : OCP.TCollection.TCollection_ExtendedString,theDoc : OCP.TDocStd.TDocStd_Document,theFilter : OCP.PCDM.PCDM_ReaderFilter,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_ReaderStatus: 
        """
        Retrieves the document from specified file. In order not to override a version of the document which is already in memory, this method can be made to depend on the value returned by IsInSession.

        Retrieves the document from specified file. In order not to override a version of the document which is already in memory, this method can be made to depend on the value returned by IsInSession.

        Retrieves document from standard stream.

        Retrieves document from standard stream.
        """
    @overload
    def Open(self,thePath : OCP.TCollection.TCollection_ExtendedString,theDoc : OCP.TDocStd.TDocStd_Document,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_ReaderStatus: ...
    @overload
    def Open(self,theIStream : io.BytesIO,theDoc : OCP.TDocStd.TDocStd_Document,theFilter : OCP.PCDM.PCDM_ReaderFilter,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_ReaderStatus: ...
    @overload
    def Open(self,theIStream : io.BytesIO,theDoc : OCP.TDocStd.TDocStd_Document,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_ReaderStatus: ...
    def Read(self,theIStream : io.BytesIO,theDocument : OCP.CDM.CDM_Document,theFilter : OCP.PCDM.PCDM_ReaderFilter=None,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> Any: 
        """
        Reads theDocument from standard SEEKABLE stream theIStream, the stream should support SEEK functionality
        """
    def ReaderFromFormat(self,aFormat : OCP.TCollection.TCollection_ExtendedString) -> OCP.PCDM.PCDM_Reader: 
        """
        Returns instance of read driver for specified format.
        """
    def ReadingFormats(self,theFormats : OCP.TColStd.TColStd_SequenceOfAsciiString) -> None: 
        """
        Returns the sequence of reading formats supported by the application.
        """
    def Resources(self) -> OCP.Resource.Resource_Manager: 
        """
        Returns resource manager defining supported persistent formats.
        """
    def ResourcesName(self) -> str: 
        """
        Return name of resource (i.e. "TObj")
        """
    @overload
    def Retrieve(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString,UseStorageConfiguration : bool=True,theFilter : OCP.PCDM.PCDM_ReaderFilter=None,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.CDM.CDM_Document: 
        """
        This method retrieves a document from the database. If the Document references other documents which have been updated, the latest version of these documents will be used if {UseStorageConfiguration} is Standard_True. The content of {aFolder}, {aName} and {aVersion} depends on the Database Manager system. If the DBMS is only based on the OS, {aFolder} is a directory and {aName} is the name of a file. In this case the use of the syntax with {aVersion} has no sense. For example:

        This method retrieves a document from the database. If the Document references other documents which have been updated, the latest version of these documents will be used if {UseStorageConfiguration} is Standard_True. -- If the DBMS is only based on the OS, this syntax should not be used.
        """
    @overload
    def Retrieve(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,UseStorageConfiguration : bool=True,theFilter : OCP.PCDM.PCDM_ReaderFilter=None,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.CDM.CDM_Document: ...
    @overload
    def Save(self,theDoc : OCP.TDocStd.TDocStd_Document,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: 
        """
        Save aDoc active document. Exceptions: Standard_NotImplemented if the document was not retrieved in the applicative session by using Open.

        Save the document overwriting the previous file
        """
    @overload
    def Save(self,theDoc : OCP.TDocStd.TDocStd_Document,theStatusMessage : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveAs(self,theDoc : OCP.TDocStd.TDocStd_Document,theOStream : io.BytesIO,theStatusMessage : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: 
        """
        Save the active document in the file <name> in the path <path> ; o verwrites the file if it already exists.

        Save theDoc to standard SEEKABLE stream theOStream. the stream should support SEEK functionality

        Save the active document in the file <name> in the path <path> . overwrite the file if it already exist.

        Save theDoc TO standard SEEKABLE stream theOStream. the stream should support SEEK functionality
        """
    @overload
    def SaveAs(self,theDoc : OCP.TDocStd.TDocStd_Document,theOStream : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveAs(self,theDoc : OCP.TDocStd.TDocStd_Document,path : OCP.TCollection.TCollection_ExtendedString,theStatusMessage : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveAs(self,theDoc : OCP.TDocStd.TDocStd_Document,path : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveDocument(self,theSourceDoc : OCP.TDocStd.TDocStd_Document,theOStream : io.BytesIO) -> bool: 
        """
        Saving the OCAF document to a file

        Saving the OCAF document to a stream
        """
    @overload
    def SaveDocument(self,theSourceDoc : OCP.TDocStd.TDocStd_Document,theTargetFile : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    def SetDefaultFolder(self,aFolder : str) -> bool: 
        """
        None
        """
    def SetVerbose(self,isVerbose : bool) -> None: 
        """
        Sets the verbose flag, meaning that load/save models should show CPU and elapsed times
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
    def WritingFormats(self,theFormats : OCP.TColStd.TColStd_SequenceOfAsciiString) -> None: 
        """
        Returns the sequence of writing formats supported by the application.
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
class TObj_Assistant():
    """
    This class provides interface to the static data to be used during save or load models.
    """
    @staticmethod
    def BindModel_s(theModel : TObj_Model) -> None: 
        """
        Binds model to the map
        """
    @staticmethod
    def BindType_s(theType : OCP.Standard.Standard_Type) -> int: 
        """
        Binds Standard_Type to the map; returns index of bound type
        """
    @staticmethod
    def ClearModelMap_s() -> None: 
        """
        Clears all records from the model map
        """
    @staticmethod
    def ClearTypeMap_s() -> None: 
        """
        Clears map of types
        """
    @staticmethod
    def FindModel_s(theName : str) -> TObj_Model: 
        """
        Finds model by name
        """
    @staticmethod
    def FindTypeIndex_s(theType : OCP.Standard.Standard_Type) -> int: 
        """
        Rinds index by Standard_Type; returns 0 if not found
        """
    @staticmethod
    def FindType_s(theTypeIndex : int) -> OCP.Standard.Standard_Type: 
        """
        Finds Standard_Type by index; returns NULL handle if not found
        """
    @staticmethod
    def GetAppVersion_s() -> int: 
        """
        Returns the version of application which wrote the currently read document. Returns 0 if it has not been set yet for the current document.
        """
    @staticmethod
    def GetCurrentModel_s() -> TObj_Model: 
        """
        Returns current model
        """
    @staticmethod
    def SetCurrentModel_s(theModel : TObj_Model) -> None: 
        """
        Sets current model
        """
    @staticmethod
    def UnSetCurrentModel_s() -> None: 
        """
        Unsets current model
        """
    def __init__(self) -> None: ...
    pass
class TObj_CheckModel(OCP.Message.Message_Algorithm, OCP.Standard.Standard_Transient):
    """
    This class provides consistency check of the TObj model. It collects all inconsistencies in the status bits and prepaires messages to be sent using SendStatusMessages (SendMessages) method. It supports also the fix mode, in which some inconsistencies are corrected.This class provides consistency check of the TObj model. It collects all inconsistencies in the status bits and prepaires messages to be sent using SendStatusMessages (SendMessages) method. It supports also the fix mode, in which some inconsistencies are corrected.
    """
    @overload
    def AddStatus(self,theStatus : OCP.Message.Message_ExecStatus,theOther : OCP.Message.Message_Algorithm) -> None: 
        """
        Add statuses to this algorithm from other algorithm (including messages)

        Add statuses to this algorithm from other algorithm, but only those items are moved that correspond to statuses set in theStatus
        """
    @overload
    def AddStatus(self,theOther : OCP.Message.Message_Algorithm) -> None: ...
    def ChangeStatus(self) -> OCP.Message.Message_ExecStatus: 
        """
        Returns exec status of algorithm

        Returns exec status of algorithm
        """
    def ClearStatus(self) -> None: 
        """
        Clear exec status of algorithm
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
    def GetMessageNumbers(self,theStatus : OCP.Message.Message_Status) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Return the numbers associated with the indicated status; Null handle if no such status or no numbers associated with it
        """
    def GetMessageStrings(self,theStatus : OCP.Message.Message_Status) -> OCP.TColStd.TColStd_HSequenceOfHExtendedString: 
        """
        Return the strings associated with the indicated status; Null handle if no such status or no strings associated with it
        """
    def GetMessenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns messenger of algorithm. The returned handle is always non-null and can be used for sending messages.

        Returns messenger of algorithm. The returned handle is always non-null and can be used for sending messages.
        """
    def GetModel(self) -> TObj_Model: 
        """
        Returns the checked model
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> OCP.Message.Message_ExecStatus: 
        """
        Returns copy of exec status of algorithm

        Returns copy of exec status of algorithm
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
    def IsToFix(self) -> bool: 
        """
        Returns true if it is allowed to fix inconsistencies
        """
    def Perform(self) -> bool: 
        """
        Performs all checks. Descendants should call parent method before doing own checks. This implementation checks OCAF references and back references between objects of the model. Returns true if no inconsistencies found.
        """
    @staticmethod
    @overload
    def PrepareReport_s(theError : OCP.TColStd.TColStd_HPackedMapOfInteger,theMaxCount : int) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Prepares a string containing a list of integers contained in theError map, but not more than theMaxCount

        Prepares a string containing a list of names contained in theReportSeq sequence, but not more than theMaxCount
        """
    @staticmethod
    @overload
    def PrepareReport_s(theReportSeq : OCP.TColStd.TColStd_SequenceOfHExtendedString,theMaxCount : int) -> OCP.TCollection.TCollection_ExtendedString: ...
    def SendMessages(self,theTraceLevel : OCP.Message.Message_Gravity=Message_Gravity.Message_Warning,theMaxCount : int=20) -> None: 
        """
        Convenient variant of SendStatusMessages() with theFilter having defined all WARN, ALARM, and FAIL (but not DONE) status flags
        """
    def SendStatusMessages(self,theFilter : OCP.Message.Message_ExecStatus,theTraceLevel : OCP.Message.Message_Gravity=Message_Gravity.Message_Warning,theMaxCount : int=20) -> None: 
        """
        Print messages for all status flags that have been set during algorithm execution, excluding statuses that are NOT set in theFilter.
        """
    def SetMessenger(self,theMsgr : OCP.Message.Message_Messenger) -> None: 
        """
        Sets messenger to algorithm
        """
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theStr : OCP.TCollection.TCollection_ExtendedString,noRepetitions : bool) -> None: 
        """
        Sets status with no parameter

        Sets status with integer parameter

        Sets status with string parameter. If noRepetitions is True, the parameter will be added only if it has not been yet recorded for the same status flag

        Sets status with string parameter If noRepetitions is True, the parameter will be added only if it has not been yet recorded for the same status flag

        Sets status with string parameter If noRepetitions is True, the parameter will be added only if it has not been yet recorded for the same status flag

        Sets status with string parameter If noRepetitions is True, the parameter will be added only if it has not been yet recorded for the same status flag

        Sets status with string parameter If noRepetitions is True, the parameter will be added only if it has not been yet recorded for the same status flag

        Sets status with preformatted message. This message will be used directly to report the status; automatic generation of status messages will be disabled for it.

        Sets status with string parameter. If noRepetitions is True, the parameter will be added only if it has not been yet recorded for the same status flag

        Sets status with string parameter If noRepetitions is True, the parameter will be added only if it has not been yet recorded for the same status flag

        Sets status with string parameter If noRepetitions is True, the parameter will be added only if it has not been yet recorded for the same status flag

        Sets status with string parameter If noRepetitions is True, the parameter will be added only if it has not been yet recorded for the same status flag
        """
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theStr : OCP.TCollection.TCollection_AsciiString,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theInt : int) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theStr : OCP.TCollection.TCollection_HExtendedString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theStr : OCP.TCollection.TCollection_ExtendedString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theStr : str,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theStr : OCP.TCollection.TCollection_HAsciiString,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theStr : OCP.TCollection.TCollection_HAsciiString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theMsg : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theStr : str,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : OCP.Message.Message_Status,theStr : OCP.TCollection.TCollection_AsciiString,noRepetitions : bool=True) -> None: ...
    def SetToFix(self,theToFix : bool) -> None: 
        """
        Sets flag allowing fixing inconsistencies
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theModel : TObj_Model) -> None: ...
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
class TObj_DataMapOfNameLabel(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TObj_DataMapOfNameLabel) -> TObj_DataMapOfNameLabel: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_HExtendedString,theItem : OCP.TDF.TDF_Label) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_HExtendedString,theItem : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_HExtendedString) -> OCP.TDF.TDF_Label: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_HExtendedString) -> OCP.TDF.TDF_Label: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : TObj_DataMapOfNameLabel) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_HExtendedString,theValue : OCP.TDF.TDF_Label) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_HExtendedString) -> OCP.TDF.TDF_Label: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_HExtendedString) -> bool: 
        """
        IsBound
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
    def Seek(self,theKey : OCP.TCollection.TCollection_HExtendedString) -> OCP.TDF.TDF_Label: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TCollection.TCollection_HExtendedString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TObj_DataMapOfNameLabel) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TObj_DataMapOfStringPointer(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TObj_DataMapOfStringPointer) -> TObj_DataMapOfStringPointer: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : capsule) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : capsule) -> capsule: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> capsule: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> capsule: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TObj_DataMapOfStringPointer) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString,theValue : capsule) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString) -> capsule: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        IsBound
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
    def Seek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> capsule: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : TObj_DataMapOfStringPointer) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TObj_DeletingMode():
    """
    None

    Members:

      TObj_FreeOnly

      TObj_KeepDepending

      TObj_Forced
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
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
    TObj_Forced: OCP.TObj.TObj_DeletingMode # value = <TObj_DeletingMode.TObj_Forced: 2>
    TObj_FreeOnly: OCP.TObj.TObj_DeletingMode # value = <TObj_DeletingMode.TObj_FreeOnly: 0>
    TObj_KeepDepending: OCP.TObj.TObj_DeletingMode # value = <TObj_DeletingMode.TObj_KeepDepending: 1>
    __entries: dict # value = {'TObj_FreeOnly': (<TObj_DeletingMode.TObj_FreeOnly: 0>, None), 'TObj_KeepDepending': (<TObj_DeletingMode.TObj_KeepDepending: 1>, None), 'TObj_Forced': (<TObj_DeletingMode.TObj_Forced: 2>, None)}
    __members__: dict # value = {'TObj_FreeOnly': <TObj_DeletingMode.TObj_FreeOnly: 0>, 'TObj_KeepDepending': <TObj_DeletingMode.TObj_KeepDepending: 1>, 'TObj_Forced': <TObj_DeletingMode.TObj_Forced: 2>}
    pass
class TObj_SequenceOfObject(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TObj_SequenceOfObject) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : TObj_Object) -> None: ...
    def Assign(self,theOther : TObj_SequenceOfObject) -> TObj_SequenceOfObject: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> TObj_Object: 
        """
        First item access
        """
    def ChangeLast(self) -> TObj_Object: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> TObj_Object: 
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
    def First(self) -> TObj_Object: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TObj_SequenceOfObject) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : TObj_Object) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TObj_SequenceOfObject) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : TObj_Object) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> TObj_Object: 
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
    def Prepend(self,theItem : TObj_Object) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TObj_SequenceOfObject) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : TObj_Object) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TObj_SequenceOfObject) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> TObj_Object: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TObj_SequenceOfObject) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TObj_Object(OCP.Standard.Standard_Transient):
    """
    Basis class for transient objects in OCAF-based modelsBasis class for transient objects in OCAF-based modelsBasis class for transient objects in OCAF-based models
    """
    class ObjectState_e():
        pass
    class TypeFlags_e():
        pass
    def AddBackReference(self,theObject : TObj_Object) -> None: 
        """
        Registers another object as being dependent on this one. Stores back references under sublabel 2 (purely transient data, not subject to persistency).
        """
    def AfterRetrieval(self) -> None: 
        """
        Performs updating the links and dependances of the object which are not stored in persistence. Should be redefined if necessary.
        """
    def BeforeForgetReference(self,arg1 : OCP.TDF.TDF_Label) -> None: 
        """
        Invokes from TObj_TReference::BeforeForget(). theLabel - label on that reference become removed Default implementation is empty
        """
    def BeforeStoring(self) -> None: 
        """
        Performs storing the objects transient fields in OCAF document which were outside transaction mechanism. Default implementation does nothing
        """
    def CanDetach(self,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Checks if object can be detached with specified mode
        """
    def CanRemoveReference(self,theObject : TObj_Object) -> bool: 
        """
        Returns True if the referred object theObject can be deleted without deletion of this object. Default implementation does nothing and returns False.
        """
    def ClearBackReferences(self) -> None: 
        """
        The default implementation just clear the back references container
        """
    def ClearFlags(self,theMask : int=-1) -> None: 
        """
        clears flags by the mask.
        """
    def Clone(self,theTargetLabel : OCP.TDF.TDF_Label,theRelocTable : OCP.TDF.TDF_RelocationTable) -> TObj_Object: 
        """
        Copy me to other label theTargetLabel New object will not have all the reference that has me. Coping object with data and childs, but change name by adding string "_copy" As result return handle of new object (null handle is something wrong) NOTE: BackReferences not coping. After cloning all objects it is necessary to call copy references with the same relocation table
        """
    def CopyChildren(self,theTargetLabel : OCP.TDF.TDF_Label,theRelocTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Coping the children from source label to the target.
        """
    def CopyReferences(self,theTargetObject : TObj_Object,theRelocTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Coping the references. return Standard_False is Target object is different type
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Detach(self,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Deletes the object from the model. The dependent objects are either deleted or modified when possible (see description of TObj_DeletingMode enumeration for more details) Returns True if deletion was successful. Checks if object can be deleted. Should be redefined for each specific kind of object
        """
    @staticmethod
    def Detach_s(theLabel : OCP.TDF.TDF_Label,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Deletes the object from the label. Checks if object can be deleted. Finds object on the label and detaches it by calling previous method. Returns true if there is no object on the label after detaching
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetBackReferences(self,theType : OCP.Standard.Standard_Type=None) -> TObj_ObjectIterator: 
        """
        Returns iterator for the objects which depend on this one. These referring objects may belong to other models. theType narrows a variety of iterated objects
        """
    def GetBadReference(self,theRoot : OCP.TDF.TDF_Label,theBadReference : OCP.TDF.TDF_Label) -> bool: 
        """
        Return True if this refers to the model theRoot belongs to and a referred label is not a descendant of theRoot. In this case theBadReference returns the currently referred label.
        """
    def GetChildLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label under which children are stored
        """
    def GetChildren(self,theType : OCP.Standard.Standard_Type=None) -> TObj_ObjectIterator: 
        """
        Returns iterator for the child objects. This method provides tree-like view of the objects hierarchy. The references to other objects are not considered as children. theType narrows a variety of iterated objects The default implementation search for children on 1 sublavel of the children sub label
        """
    def GetDataLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label which is the root for data OCAF sub-tree
        """
    def GetDictionary(self) -> TObj_TNameContainer: 
        """
        Returns the map of names of the objects Default implementation returns global Dictionary of the model
        """
    def GetFatherObject(self,theType : OCP.Standard.Standard_Type=None) -> TObj_Object: 
        """
        Returns the father object, which may be NULL theType gives type of father object to search
        """
    def GetFlags(self) -> int: 
        """
        Returns mask of seted flags
        """
    def GetLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the OCAF label on which object`s data are stored
        """
    def GetModel(self) -> TObj_Model: 
        """
        Returns the model to which the object belongs
        """
    @overload
    def GetName(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns the name of the object (empty string if object has no name)

        Returns the Standard_True is object has name and returns name to theName

        Returns the Standard_True is object has name and returns name to theName
        """
    @overload
    def GetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> bool: ...
    @overload
    def GetName(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    def GetNameForClone(self,arg1 : TObj_Object) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns name for copy default implementation returns the same name
        """
    @staticmethod
    def GetObj_s(theLabel : OCP.TDF.TDF_Label,theResult : TObj_Object,isSuper : bool=False) -> bool: 
        """
        Returns the Object attached to a given label. Returns False if no object of type TObj_Object is stored on the specified label. If isSuper is true tries to find on the super labels.
        """
    def GetOrder(self) -> int: 
        """
        returns order of object (or tag of their label if order is not initialised)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetReferenceLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label which is the root for reference OCAF sub-tree
        """
    def GetReferences(self,theType : OCP.Standard.Standard_Type=None) -> TObj_ObjectIterator: 
        """
        Returns an Iterator containing objects that compose the this one theType narrows a variety of iterated objects
        """
    def GetTypeFlags(self) -> int: 
        """
        Returns flags (bitmask) that define properties of objects of that type By default returns flag Visible
        """
    def HasBackReferences(self) -> bool: 
        """
        Returns TRUE if object has 1 or more back references
        """
    def HasModifications(self) -> bool: 
        """
        Public methods to check modifications of the object since last commit
        """
    def HasReference(self,theObject : TObj_Object) -> bool: 
        """
        Returns True if object has reference to indicated object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAlive(self) -> bool: 
        """
        Checks that object alive in model Default implementation checks that object has TObject attribute at own label.
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
    def RelocateReferences(self,theFromRoot : OCP.TDF.TDF_Label,theToRoot : OCP.TDF.TDF_Label,theUpdateBackRefs : bool=True) -> bool: 
        """
        Make that each reference pointing to a descendant label of theFromRoot to point to an equivalent label under theToRoot. Return False if a resulting reference does not point to an TObj_Object Example: a referred object label = 0:3:24:7:2:7 theFromRoot = 0:3:24 theToRoot = 0:2 a new referred label = 0:2:7:2:7
        """
    def RemoveAllReferences(self) -> None: 
        """
        Remove all references to other objects, by removing all reference attributes
        """
    def RemoveBackReference(self,theObject : TObj_Object,theSingleOnly : bool=True) -> None: 
        """
        Removes information on dependent object (back reference). If theSingleOnly is true only the first back reference is removed in the case of duplicate items.
        """
    def RemoveBackReferences(self,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Removes all back reference by removing references from other to me.
        """
    def RemoveReference(self,theObject : TObj_Object) -> None: 
        """
        Removes reference to the object by replace reference to NULL object
        """
    def ReplaceReference(self,theOldObject : TObj_Object,theNewObject : TObj_Object) -> None: 
        """
        Replace reference from old object to new object. If it is not possible, may raise exception. If new object is null then simple remove reference to old object.
        """
    def SetFlags(self,theMask : int) -> None: 
        """
        Sets flags with defined mask.
        """
    @overload
    def SetName(self,name : str) -> bool: 
        """
        Sets name of the object. Returns False if theName is not unique.

        Sets name of the object. Returns False if theName is not unique.

        Sets name of the object. Returns False if theName is not unique.
        """
    @overload
    def SetName(self,theName : OCP.TCollection.TCollection_HExtendedString) -> bool: ...
    @overload
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> bool: ...
    def SetOrder(self,theIndx : int) -> bool: 
        """
        sets order of object
        """
    def TestFlags(self,theMask : int) -> bool: 
        """
        tests flags by the mask.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def getChildLabel(self,theRank : int) -> OCP.TDF.TDF_Label: 
        """
        Returns the label for child with rank
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
    ObjectState_Hidden: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Hidden: 1>
    ObjectState_Imported: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Imported: 4>
    ObjectState_ImportedByFile: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_ImportedByFile: 8>
    ObjectState_Ordered: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Ordered: 16>
    ObjectState_Saved: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Saved: 2>
    Visible: OCP.TObj.TypeFlags_e # value = <TypeFlags_e.Visible: 1>
    pass
class TObj_ObjectIterator(OCP.Standard.Standard_Transient):
    """
    This class provides an iterator by objects in a partition. (implements TObj_ObjectIterator interface)This class provides an iterator by objects in a partition. (implements TObj_ObjectIterator interface)
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
    def More(self) -> bool: 
        """
        Returns True if iteration is not finished and method Current() will give the object. Default implementation returns False
        """
    def Next(self) -> None: 
        """
        Iterates to the next object Default implementation does nothing
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> TObj_Object: 
        """
        Returns current object (or null if iteration has finished) Default implementation returns null handle
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
class TObj_Model(OCP.Standard.Standard_Transient):
    """
    Base class for OCAF based models. Defines common behaviour for all models based on TObject classes, basic services to access model objects and common operations with the model. Provides default implementation for many methods.Base class for OCAF based models. Defines common behaviour for all models based on TObject classes, basic services to access model objects and common operations with the model. Provides default implementation for many methods.Base class for OCAF based models. Defines common behaviour for all models based on TObject classes, basic services to access model objects and common operations with the model. Provides default implementation for many methods.
    """
    def AbortCommand(self) -> None: 
        """
        Abort the Command transaction. Do nothing If there is no Command transaction open.
        """
    def Close(self) -> bool: 
        """
        Close the model
        """
    def CloseDocument(self,theDoc : OCP.TDocStd.TDocStd_Document) -> None: 
        """
        Close Free OCAF document
        """
    def CommitCommand(self) -> None: 
        """
        Commit the Command transaction. Do nothing If there is no Command transaction open.
        """
    def CopyReferences(self,theTarget : TObj_Model,theRelocTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Copy references from me to the other
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
    def FindObject(self,theName : OCP.TCollection.TCollection_HExtendedString,theDictionary : TObj_TNameContainer) -> TObj_Object: 
        """
        Returns an Object by given Name (or Null if not found).
        """
    def GetApplication(self) -> TObj_Application: 
        """
        Returns handle to static instance of the relevant application class
        """
    def GetChecker(self) -> TObj_CheckModel: 
        """
        Returns the tool checking model consistency. Descendant may redefine it to return its own tool.
        """
    def GetChildren(self) -> TObj_ObjectIterator: 
        """
        Returns an Iterator on objects in the main partition
        """
    def GetDictionary(self) -> TObj_TNameContainer: 
        """
        Returns the map of names of the objects
        """
    def GetDocument(self) -> OCP.TDocStd.TDocStd_Document: 
        """
        Returns OCAF document of Model
        """
    @staticmethod
    def GetDocumentModel_s(theLabel : OCP.TDF.TDF_Label) -> TObj_Model: 
        """
        Returns model which contains a document with the label, or NULL handle if label is NULL
        """
    def GetFile(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns the full file name this model is to be saved to, or null if the model was not saved yet
        """
    def GetFormat(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the format for save/restore. This implementation returns "BinOcaf". The method should be redefined for those models that should use another format.
        """
    def GetFormatVersion(self) -> int: 
        """
        Returns the version of format stored in TObj file
        """
    def GetGUID(self) -> OCP.Standard.Standard_GUID: 
        """
        Defines interface GUID for TObj_Model
        """
    def GetLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns OCAF label on which model data are stored.
        """
    def GetMainPartition(self) -> TObj_Partition: 
        """
        Returns root object of model
        """
    def GetModelName(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns the name of the model
        """
    def GetObjects(self) -> TObj_ObjectIterator: 
        """
        Returns an Iterator on all objects in the Model
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRoot(self) -> TObj_Object: 
        """
        Returns root object of model
        """
    def HasOpenCommand(self) -> bool: 
        """
        Returns True if a Command transaction is open Starting, finishing the transaction
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
    def IsModified(self) -> bool: 
        """
        Modification status
        """
    def IsRegisteredName(self,theName : OCP.TCollection.TCollection_HExtendedString,theDictionary : TObj_TNameContainer) -> bool: 
        """
        Returns True is name is registered in the names map The input argument may be NULL handle, then model check in own global container
        """
    @overload
    def Load(self,theFile : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Load the OCAF model from a file. If the filename is empty or file does not exists, it just initializes model by empty data.

        Load the OCAF model from a stream. If case of failure, it initializes the model by empty data.
        """
    @overload
    def Load(self,theIStream : io.BytesIO) -> bool: ...
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Get messenger used for messages output (by default, the messenger from application is used)
        """
    def NewEmpty(self) -> TObj_Model: 
        """
        This function have to create a new model with type like me
        """
    def OpenCommand(self) -> None: 
        """
        Open a new command transaction.
        """
    def Paste(self,theModel : TObj_Model,theRelocTable : OCP.TDF.TDF_RelocationTable) -> bool: 
        """
        Pastes me to the new model references will not be copied if theRelocTable is not 0 if theRelocTable is not NULL theRelocTable is filled by objects
        """
    def RegisterName(self,theName : OCP.TCollection.TCollection_HExtendedString,theLabel : OCP.TDF.TDF_Label,theDictionary : TObj_TNameContainer) -> None: 
        """
        Register name in the map The input argument may be NULL handle, then model check in own global container
        """
    def Save(self) -> bool: 
        """
        Save the model to the same file
        """
    @overload
    def SaveAs(self,theOStream : io.BytesIO) -> bool: 
        """
        Save the model to a file

        Save the model to a stream
        """
    @overload
    def SaveAs(self,theFile : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    def SetLabel(self,theLabel : OCP.TDF.TDF_Label) -> None: 
        """
        Sets OCAF label on which model data are stored. Used by persistence mechanism.
        """
    def SetMessenger(self,theMsgr : OCP.Message.Message_Messenger) -> None: 
        """
        Set messenger to use for messages output
        """
    def SetModified(self,theModified : bool) -> None: 
        """
        Sets modification status
        """
    @staticmethod
    def SetNewName_s(theObject : TObj_Object) -> None: 
        """
        Sets new unique name for the object
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnRegisterName(self,theName : OCP.TCollection.TCollection_HExtendedString,theDictionary : TObj_TNameContainer) -> None: 
        """
        Unregisters name from the map The input argument may be NULL handle, then model check in own global container
        """
    def Update(self) -> bool: 
        """
        this method is called before activating this model
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
class TObj_ModelIterator(TObj_ObjectIterator, OCP.Standard.Standard_Transient):
    """
    This class provides an iterator by all objects in the model.This class provides an iterator by all objects in the model.
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
    def More(self) -> bool: 
        """
        Returns True if iteration is not finished and method Value() will give the object
        """
    def Next(self) -> None: 
        """
        Iterates to the next object
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> TObj_Object: 
        """
        Returns current object (or MainObj of Model if iteration has finished)
        """
    def __init__(self,theModel : TObj_Model) -> None: ...
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
class TObj_Partition(TObj_Object, OCP.Standard.Standard_Transient):
    """
    This class provides tool handling one of partitions (the set of homogeneous elements) in the OCAF based model`s data structureThis class provides tool handling one of partitions (the set of homogeneous elements) in the OCAF based model`s data structure
    """
    class ObjectState_e():
        pass
    class TypeFlags_e():
        pass
    def AddBackReference(self,theObject : TObj_Object) -> None: 
        """
        Registers another object as being dependent on this one. Stores back references under sublabel 2 (purely transient data, not subject to persistency).
        """
    def AfterRetrieval(self) -> None: 
        """
        Performs updating the links and dependencies of the object which are not stored in persistence. Does not register the partition name
        """
    def BeforeForgetReference(self,arg1 : OCP.TDF.TDF_Label) -> None: 
        """
        Invokes from TObj_TReference::BeforeForget(). theLabel - label on that reference become removed Default implementation is empty
        """
    def BeforeStoring(self) -> None: 
        """
        Performs storing the objects transient fields in OCAF document which were outside transaction mechanism. Default implementation does nothing
        """
    def CanDetach(self,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Checks if object can be detached with specified mode
        """
    def CanRemoveReference(self,theObject : TObj_Object) -> bool: 
        """
        Returns True if the referred object theObject can be deleted without deletion of this object. Default implementation does nothing and returns False.
        """
    def ClearBackReferences(self) -> None: 
        """
        The default implementation just clear the back references container
        """
    def ClearFlags(self,theMask : int=-1) -> None: 
        """
        clears flags by the mask.
        """
    def Clone(self,theTargetLabel : OCP.TDF.TDF_Label,theRelocTable : OCP.TDF.TDF_RelocationTable) -> TObj_Object: 
        """
        Copy me to other label theTargetLabel New object will not have all the reference that has me. Coping object with data and childs, but change name by adding string "_copy" As result return handle of new object (null handle is something wrong) NOTE: BackReferences not coping. After cloning all objects it is necessary to call copy references with the same relocation table
        """
    def CopyChildren(self,theTargetLabel : OCP.TDF.TDF_Label,theRelocTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Coping the children from source label to the target.
        """
    def CopyReferences(self,theTargetObject : TObj_Object,theRelocTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Coping the references. return Standard_False is Target object is different type
        """
    @staticmethod
    def Create_s(theLabel : OCP.TDF.TDF_Label,theSetName : bool=True) -> TObj_Partition: 
        """
        Creates a new partition on given label.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Detach(self,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Deletes the object from the model. The dependent objects are either deleted or modified when possible (see description of TObj_DeletingMode enumeration for more details) Returns True if deletion was successful. Checks if object can be deleted. Should be redefined for each specific kind of object
        """
    @staticmethod
    def Detach_s(theLabel : OCP.TDF.TDF_Label,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Deletes the object from the label. Checks if object can be deleted. Finds object on the label and detaches it by calling previous method. Returns true if there is no object on the label after detaching
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetBackReferences(self,theType : OCP.Standard.Standard_Type=None) -> TObj_ObjectIterator: 
        """
        Returns iterator for the objects which depend on this one. These referring objects may belong to other models. theType narrows a variety of iterated objects
        """
    def GetBadReference(self,theRoot : OCP.TDF.TDF_Label,theBadReference : OCP.TDF.TDF_Label) -> bool: 
        """
        Return True if this refers to the model theRoot belongs to and a referred label is not a descendant of theRoot. In this case theBadReference returns the currently referred label.
        """
    def GetChildLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label under which children are stored
        """
    def GetChildren(self,theType : OCP.Standard.Standard_Type=None) -> TObj_ObjectIterator: 
        """
        Returns iterator for the child objects. This method provides tree-like view of the objects hierarchy. The references to other objects are not considered as children. theType narrows a variety of iterated objects The default implementation search for children on 1 sublavel of the children sub label
        """
    def GetDataLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label which is the root for data OCAF sub-tree
        """
    def GetDictionary(self) -> TObj_TNameContainer: 
        """
        Returns the map of names of the objects Default implementation returns global Dictionary of the model
        """
    def GetFatherObject(self,theType : OCP.Standard.Standard_Type=None) -> TObj_Object: 
        """
        Returns the father object, which may be NULL theType gives type of father object to search
        """
    def GetFlags(self) -> int: 
        """
        Returns mask of seted flags
        """
    def GetLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the OCAF label on which object`s data are stored
        """
    def GetLastIndex(self) -> int: 
        """
        Return Last index in partition (reserved);
        """
    def GetModel(self) -> TObj_Model: 
        """
        Returns the model to which the object belongs
        """
    @overload
    def GetName(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns the name of the object (empty string if object has no name)

        Returns the Standard_True is object has name and returns name to theName

        Returns the Standard_True is object has name and returns name to theName
        """
    @overload
    def GetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> bool: ...
    @overload
    def GetName(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    def GetNameForClone(self,arg1 : TObj_Object) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns name for copy default implementation returns the same name
        """
    def GetNamePrefix(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns prefix for names of the objects in partition.
        """
    def GetNewName(self,theIsToChangeCount : bool=True) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Generates and returns name for new object in partition. if theIsToChangeCount is true partition increase own counter to generate new name next time starting from new counter value
        """
    @staticmethod
    def GetObj_s(theLabel : OCP.TDF.TDF_Label,theResult : TObj_Object,isSuper : bool=False) -> bool: 
        """
        Returns the Object attached to a given label. Returns False if no object of type TObj_Object is stored on the specified label. If isSuper is true tries to find on the super labels.
        """
    def GetOrder(self) -> int: 
        """
        returns order of object (or tag of their label if order is not initialised)
        """
    @staticmethod
    def GetPartition_s(theObject : TObj_Object) -> TObj_Partition: 
        """
        Returns the partition in which object is stored. Null partition returned if not found
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetReferenceLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label which is the root for reference OCAF sub-tree
        """
    def GetReferences(self,theType : OCP.Standard.Standard_Type=None) -> TObj_ObjectIterator: 
        """
        Returns an Iterator containing objects that compose the this one theType narrows a variety of iterated objects
        """
    def GetTypeFlags(self) -> int: 
        """
        Returns flags (bitmask) that define properties of objects of that type By default returns flag Visible
        """
    def HasBackReferences(self) -> bool: 
        """
        Returns TRUE if object has 1 or more back references
        """
    def HasModifications(self) -> bool: 
        """
        Public methods to check modifications of the object since last commit
        """
    def HasReference(self,theObject : TObj_Object) -> bool: 
        """
        Returns True if object has reference to indicated object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAlive(self) -> bool: 
        """
        Checks that object alive in model Default implementation checks that object has TObject attribute at own label.
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
    def NewLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Creates and Returns label for new object in partition.
        """
    def RelocateReferences(self,theFromRoot : OCP.TDF.TDF_Label,theToRoot : OCP.TDF.TDF_Label,theUpdateBackRefs : bool=True) -> bool: 
        """
        Make that each reference pointing to a descendant label of theFromRoot to point to an equivalent label under theToRoot. Return False if a resulting reference does not point to an TObj_Object Example: a referred object label = 0:3:24:7:2:7 theFromRoot = 0:3:24 theToRoot = 0:2 a new referred label = 0:2:7:2:7
        """
    def RemoveAllReferences(self) -> None: 
        """
        Remove all references to other objects, by removing all reference attributes
        """
    def RemoveBackReference(self,theObject : TObj_Object,theSingleOnly : bool=True) -> None: 
        """
        Removes information on dependent object (back reference). If theSingleOnly is true only the first back reference is removed in the case of duplicate items.
        """
    def RemoveBackReferences(self,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Removes all back reference by removing references from other to me.
        """
    def RemoveReference(self,theObject : TObj_Object) -> None: 
        """
        Removes reference to the object by replace reference to NULL object
        """
    def ReplaceReference(self,theOldObject : TObj_Object,theNewObject : TObj_Object) -> None: 
        """
        Replace reference from old object to new object. If it is not possible, may raise exception. If new object is null then simple remove reference to old object.
        """
    def SetFlags(self,theMask : int) -> None: 
        """
        Sets flags with defined mask.
        """
    def SetLastIndex(self,theIndex : int) -> None: 
        """
        Sets Last index in partition (reserved);
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HExtendedString) -> bool: 
        """
        Sets name of the object. partition does not check unique of own name
        """
    def SetNamePrefix(self,thePrefix : OCP.TCollection.TCollection_HExtendedString) -> None: 
        """
        Sets prefix for names of the objects in partition.
        """
    def SetOrder(self,theIndx : int) -> bool: 
        """
        sets order of object
        """
    def TestFlags(self,theMask : int) -> bool: 
        """
        tests flags by the mask.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self) -> bool: 
        """
        Does nothing in the partition.
        """
    def getChildLabel(self,theRank : int) -> OCP.TDF.TDF_Label: 
        """
        Returns the label for child with rank
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
    ObjectState_Hidden: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Hidden: 1>
    ObjectState_Imported: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Imported: 4>
    ObjectState_ImportedByFile: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_ImportedByFile: 8>
    ObjectState_Ordered: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Ordered: 16>
    ObjectState_Saved: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Saved: 2>
    Visible: OCP.TObj.TypeFlags_e # value = <TypeFlags_e.Visible: 1>
    pass
class TObj_LabelIterator(TObj_ObjectIterator, OCP.Standard.Standard_Transient):
    """
    This class is a basis for OCAF based iterators.This class is a basis for OCAF based iterators.
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
    def LabelValue(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label of the current item
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Item in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Item
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> TObj_Object: 
        """
        Returns the current item
        """
    def __init__(self,theLabel : OCP.TDF.TDF_Label,isRecursive : bool=False) -> None: ...
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
class TObj_OcafObjectIterator(TObj_LabelIterator, TObj_ObjectIterator, OCP.Standard.Standard_Transient):
    """
    This class provides an iterator by objects in a partition. (implements TObj_ObjectIterator interface)This class provides an iterator by objects in a partition. (implements TObj_ObjectIterator interface)
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
    def LabelValue(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label of the current item
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Item in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Item
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> TObj_Object: 
        """
        Returns the current item
        """
    def __init__(self,theLabel : OCP.TDF.TDF_Label,theType : OCP.Standard.Standard_Type=None,theRecursive : bool=False,theAllSubChildren : bool=False) -> None: ...
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
class TObj_HiddenPartition(TObj_Partition, TObj_Object, OCP.Standard.Standard_Transient):
    """
    This class is partition is predefined hidden flagThis class is partition is predefined hidden flag
    """
    class ObjectState_e():
        """
        enumeration describing various object state bit flags (see Set/GetFlags())

        Members:

          ObjectState_Hidden

          ObjectState_Saved

          ObjectState_Imported

          ObjectState_ImportedByFile

          ObjectState_Ordered
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
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
        ObjectState_Hidden: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Hidden: 1>
        ObjectState_Imported: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Imported: 4>
        ObjectState_ImportedByFile: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_ImportedByFile: 8>
        ObjectState_Ordered: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Ordered: 16>
        ObjectState_Saved: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Saved: 2>
        __entries: dict # value = {'ObjectState_Hidden': (<ObjectState_e.ObjectState_Hidden: 1>, None), 'ObjectState_Saved': (<ObjectState_e.ObjectState_Saved: 2>, None), 'ObjectState_Imported': (<ObjectState_e.ObjectState_Imported: 4>, None), 'ObjectState_ImportedByFile': (<ObjectState_e.ObjectState_ImportedByFile: 8>, None), 'ObjectState_Ordered': (<ObjectState_e.ObjectState_Ordered: 16>, None)}
        __members__: dict # value = {'ObjectState_Hidden': <ObjectState_e.ObjectState_Hidden: 1>, 'ObjectState_Saved': <ObjectState_e.ObjectState_Saved: 2>, 'ObjectState_Imported': <ObjectState_e.ObjectState_Imported: 4>, 'ObjectState_ImportedByFile': <ObjectState_e.ObjectState_ImportedByFile: 8>, 'ObjectState_Ordered': <ObjectState_e.ObjectState_Ordered: 16>}
        pass
    class TypeFlags_e():
        """
        None

        Members:

          Visible
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
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
        Visible: OCP.TObj.TypeFlags_e # value = <TypeFlags_e.Visible: 1>
        __entries: dict # value = {'Visible': (<TypeFlags_e.Visible: 1>, None)}
        __members__: dict # value = {'Visible': <TypeFlags_e.Visible: 1>}
        pass
    def AddBackReference(self,theObject : TObj_Object) -> None: 
        """
        Registers another object as being dependent on this one. Stores back references under sublabel 2 (purely transient data, not subject to persistency).
        """
    def AfterRetrieval(self) -> None: 
        """
        Performs updating the links and dependencies of the object which are not stored in persistence. Does not register the partition name
        """
    def BeforeForgetReference(self,arg1 : OCP.TDF.TDF_Label) -> None: 
        """
        Invokes from TObj_TReference::BeforeForget(). theLabel - label on that reference become removed Default implementation is empty
        """
    def BeforeStoring(self) -> None: 
        """
        Performs storing the objects transient fields in OCAF document which were outside transaction mechanism. Default implementation does nothing
        """
    def CanDetach(self,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Checks if object can be detached with specified mode
        """
    def CanRemoveReference(self,theObject : TObj_Object) -> bool: 
        """
        Returns True if the referred object theObject can be deleted without deletion of this object. Default implementation does nothing and returns False.
        """
    def ClearBackReferences(self) -> None: 
        """
        The default implementation just clear the back references container
        """
    def ClearFlags(self,theMask : int=-1) -> None: 
        """
        clears flags by the mask.
        """
    def Clone(self,theTargetLabel : OCP.TDF.TDF_Label,theRelocTable : OCP.TDF.TDF_RelocationTable) -> TObj_Object: 
        """
        Copy me to other label theTargetLabel New object will not have all the reference that has me. Coping object with data and childs, but change name by adding string "_copy" As result return handle of new object (null handle is something wrong) NOTE: BackReferences not coping. After cloning all objects it is necessary to call copy references with the same relocation table
        """
    def CopyChildren(self,theTargetLabel : OCP.TDF.TDF_Label,theRelocTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Coping the children from source label to the target.
        """
    def CopyReferences(self,theTargetObject : TObj_Object,theRelocTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Coping the references. return Standard_False is Target object is different type
        """
    @staticmethod
    def Create_s(theLabel : OCP.TDF.TDF_Label,theSetName : bool=True) -> TObj_Partition: 
        """
        Creates a new partition on given label.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Detach(self,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Deletes the object from the model. The dependent objects are either deleted or modified when possible (see description of TObj_DeletingMode enumeration for more details) Returns True if deletion was successful. Checks if object can be deleted. Should be redefined for each specific kind of object
        """
    @staticmethod
    def Detach_s(theLabel : OCP.TDF.TDF_Label,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Deletes the object from the label. Checks if object can be deleted. Finds object on the label and detaches it by calling previous method. Returns true if there is no object on the label after detaching
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetBackReferences(self,theType : OCP.Standard.Standard_Type=None) -> TObj_ObjectIterator: 
        """
        Returns iterator for the objects which depend on this one. These referring objects may belong to other models. theType narrows a variety of iterated objects
        """
    def GetBadReference(self,theRoot : OCP.TDF.TDF_Label,theBadReference : OCP.TDF.TDF_Label) -> bool: 
        """
        Return True if this refers to the model theRoot belongs to and a referred label is not a descendant of theRoot. In this case theBadReference returns the currently referred label.
        """
    def GetChildLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label under which children are stored
        """
    def GetChildren(self,theType : OCP.Standard.Standard_Type=None) -> TObj_ObjectIterator: 
        """
        Returns iterator for the child objects. This method provides tree-like view of the objects hierarchy. The references to other objects are not considered as children. theType narrows a variety of iterated objects The default implementation search for children on 1 sublavel of the children sub label
        """
    def GetDataLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label which is the root for data OCAF sub-tree
        """
    def GetDictionary(self) -> TObj_TNameContainer: 
        """
        Returns the map of names of the objects Default implementation returns global Dictionary of the model
        """
    def GetFatherObject(self,theType : OCP.Standard.Standard_Type=None) -> TObj_Object: 
        """
        Returns the father object, which may be NULL theType gives type of father object to search
        """
    def GetFlags(self) -> int: 
        """
        Returns mask of seted flags
        """
    def GetLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the OCAF label on which object`s data are stored
        """
    def GetLastIndex(self) -> int: 
        """
        Return Last index in partition (reserved);
        """
    def GetModel(self) -> TObj_Model: 
        """
        Returns the model to which the object belongs
        """
    @overload
    def GetName(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns the name of the object (empty string if object has no name)

        Returns the Standard_True is object has name and returns name to theName

        Returns the Standard_True is object has name and returns name to theName
        """
    @overload
    def GetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> bool: ...
    @overload
    def GetName(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    def GetNameForClone(self,arg1 : TObj_Object) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns name for copy default implementation returns the same name
        """
    def GetNamePrefix(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Returns prefix for names of the objects in partition.
        """
    def GetNewName(self,theIsToChangeCount : bool=True) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Generates and returns name for new object in partition. if theIsToChangeCount is true partition increase own counter to generate new name next time starting from new counter value
        """
    @staticmethod
    def GetObj_s(theLabel : OCP.TDF.TDF_Label,theResult : TObj_Object,isSuper : bool=False) -> bool: 
        """
        Returns the Object attached to a given label. Returns False if no object of type TObj_Object is stored on the specified label. If isSuper is true tries to find on the super labels.
        """
    def GetOrder(self) -> int: 
        """
        returns order of object (or tag of their label if order is not initialised)
        """
    @staticmethod
    def GetPartition_s(theObject : TObj_Object) -> TObj_Partition: 
        """
        Returns the partition in which object is stored. Null partition returned if not found
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetReferenceLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label which is the root for reference OCAF sub-tree
        """
    def GetReferences(self,theType : OCP.Standard.Standard_Type=None) -> TObj_ObjectIterator: 
        """
        Returns an Iterator containing objects that compose the this one theType narrows a variety of iterated objects
        """
    def GetTypeFlags(self) -> int: 
        """
        Returns all flags of father except Visible
        """
    def HasBackReferences(self) -> bool: 
        """
        Returns TRUE if object has 1 or more back references
        """
    def HasModifications(self) -> bool: 
        """
        Public methods to check modifications of the object since last commit
        """
    def HasReference(self,theObject : TObj_Object) -> bool: 
        """
        Returns True if object has reference to indicated object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAlive(self) -> bool: 
        """
        Checks that object alive in model Default implementation checks that object has TObject attribute at own label.
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
    def NewLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Creates and Returns label for new object in partition.
        """
    def RelocateReferences(self,theFromRoot : OCP.TDF.TDF_Label,theToRoot : OCP.TDF.TDF_Label,theUpdateBackRefs : bool=True) -> bool: 
        """
        Make that each reference pointing to a descendant label of theFromRoot to point to an equivalent label under theToRoot. Return False if a resulting reference does not point to an TObj_Object Example: a referred object label = 0:3:24:7:2:7 theFromRoot = 0:3:24 theToRoot = 0:2 a new referred label = 0:2:7:2:7
        """
    def RemoveAllReferences(self) -> None: 
        """
        Remove all references to other objects, by removing all reference attributes
        """
    def RemoveBackReference(self,theObject : TObj_Object,theSingleOnly : bool=True) -> None: 
        """
        Removes information on dependent object (back reference). If theSingleOnly is true only the first back reference is removed in the case of duplicate items.
        """
    def RemoveBackReferences(self,theMode : TObj_DeletingMode=TObj_DeletingMode.TObj_FreeOnly) -> bool: 
        """
        Removes all back reference by removing references from other to me.
        """
    def RemoveReference(self,theObject : TObj_Object) -> None: 
        """
        Removes reference to the object by replace reference to NULL object
        """
    def ReplaceReference(self,theOldObject : TObj_Object,theNewObject : TObj_Object) -> None: 
        """
        Replace reference from old object to new object. If it is not possible, may raise exception. If new object is null then simple remove reference to old object.
        """
    def SetFlags(self,theMask : int) -> None: 
        """
        Sets flags with defined mask.
        """
    def SetLastIndex(self,theIndex : int) -> None: 
        """
        Sets Last index in partition (reserved);
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HExtendedString) -> bool: 
        """
        Sets name of the object. partition does not check unique of own name
        """
    def SetNamePrefix(self,thePrefix : OCP.TCollection.TCollection_HExtendedString) -> None: 
        """
        Sets prefix for names of the objects in partition.
        """
    def SetOrder(self,theIndx : int) -> bool: 
        """
        sets order of object
        """
    def TestFlags(self,theMask : int) -> bool: 
        """
        tests flags by the mask.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self) -> bool: 
        """
        Does nothing in the partition.
        """
    def __init__(self,theLabel : OCP.TDF.TDF_Label) -> None: ...
    def getChildLabel(self,theRank : int) -> OCP.TDF.TDF_Label: 
        """
        Returns the label for child with rank
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
    ObjectState_Hidden: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Hidden: 1>
    ObjectState_Imported: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Imported: 4>
    ObjectState_ImportedByFile: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_ImportedByFile: 8>
    ObjectState_Ordered: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Ordered: 16>
    ObjectState_Saved: OCP.TObj.ObjectState_e # value = <ObjectState_e.ObjectState_Saved: 2>
    Visible: OCP.TObj.TypeFlags_e # value = <TypeFlags_e.Visible: 1>
    pass
class TObj_Persistence():
    """
    This class is intended to be a root of tools (one per class) to manage persistence of objects inherited from TObj_Object It provides a mechanism to recover correctly typed objects (subtypes of TObj_Object) out of their persistent names
    """
    @staticmethod
    def CreateNewObject_s(theType : str,theLabel : OCP.TDF.TDF_Label) -> TObj_Object: 
        """
        Creates and returns a new object of the registered type If the type is not registered, returns Null handle
        """
    @staticmethod
    def DumpTypes_s(theOs : io.BytesIO) -> None: 
        """
        Dumps names of all the types registered for persistence to the specified stream
        """
    pass
class TObj_ReferenceIterator(TObj_LabelIterator, TObj_ObjectIterator, OCP.Standard.Standard_Transient):
    """
    This class provides an iterator by references of the object (implements TObj_ReferenceIterator interface)This class provides an iterator by references of the object (implements TObj_ReferenceIterator interface)
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
    def LabelValue(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label of the current item
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Item in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Item
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> TObj_Object: 
        """
        Returns the current item
        """
    def __init__(self,theLabel : OCP.TDF.TDF_Label,theType : OCP.Standard.Standard_Type=None,theRecursive : bool=True) -> None: ...
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
class TObj_SequenceIterator(TObj_ObjectIterator, OCP.Standard.Standard_Transient):
    """
    This class is an iterator on sequenceThis class is an iterator on sequence
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
    def More(self) -> bool: 
        """
        Returns True if there is a current Item in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Item
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> TObj_Object: 
        """
        Returns the current item
        """
    def __init__(self,theObjects : TObj_HSequenceOfObject,theType : OCP.Standard.Standard_Type=None) -> None: ...
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
class TObj_SequenceOfIterator(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TObj_ObjectIterator) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : TObj_SequenceOfIterator) -> None: ...
    def Assign(self,theOther : TObj_SequenceOfIterator) -> TObj_SequenceOfIterator: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> TObj_ObjectIterator: 
        """
        First item access
        """
    def ChangeLast(self) -> TObj_ObjectIterator: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> TObj_ObjectIterator: 
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
    def First(self) -> TObj_ObjectIterator: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TObj_SequenceOfIterator) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : TObj_ObjectIterator) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : TObj_ObjectIterator) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TObj_SequenceOfIterator) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> TObj_ObjectIterator: 
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
    def Prepend(self,theSeq : TObj_SequenceOfIterator) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : TObj_ObjectIterator) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : TObj_ObjectIterator) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TObj_SequenceOfIterator) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> TObj_ObjectIterator: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TObj_SequenceOfIterator) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TObj_HSequenceOfObject(TObj_SequenceOfObject, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : TObj_SequenceOfObject) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : TObj_Object) -> None: ...
    def Assign(self,theOther : TObj_SequenceOfObject) -> TObj_SequenceOfObject: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> TObj_Object: 
        """
        First item access
        """
    def ChangeLast(self) -> TObj_Object: 
        """
        Last item access
        """
    def ChangeSequence(self) -> TObj_SequenceOfObject: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> TObj_Object: 
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
    def First(self) -> TObj_Object: 
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
    def InsertAfter(self,theIndex : int,theSeq : TObj_SequenceOfObject) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : TObj_Object) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TObj_SequenceOfObject) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : TObj_Object) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> TObj_Object: 
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
    def Prepend(self,theItem : TObj_Object) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TObj_SequenceOfObject) -> None: ...
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
    def Sequence(self) -> TObj_SequenceOfObject: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : TObj_Object) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TObj_SequenceOfObject) -> None: 
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
    def Value(self,theIndex : int) -> TObj_Object: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TObj_SequenceOfObject) -> None: ...
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
class TObj_TIntSparseArray(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    OCAF Attribute to store a set of positive integer values in the OCAF tree. Each value is identified by ID (positive integer). The supporting underlying data structure is NCollection_SparseArray of integers.OCAF Attribute to store a set of positive integer values in the OCAF tree. Each value is identified by ID (positive integer). The supporting underlying data structure is NCollection_SparseArray of integers.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,theDelta : OCP.TDF.TDF_AttributeDelta,toForce : bool) -> bool: 
        """
        Clears my modification delta; called after application of theDelta
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Moves this delta into a new other attribute.
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        It is called just before Commit or Abort transaction and does Backup() to create a delta
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Clear(self) -> None: 
        """
        Clears the set
        """
    def ClearDelta(self) -> None: 
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
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    def DeltaOnModification(self,theDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Applies theDelta to this.
        """
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        This method is used in implementation of ID()
        """
    def GetIterator(self) -> Any: 
        """
        Returns iterator on objects contained in the set
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasValue(self,theId : int) -> bool: 
        """
        Returns true if the value with the given ID is present.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of this attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty TObj_TIntSparseArray attribute. It is used by the copy algorithm.
        """
    def Paste(self,theInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is used when copying an attribute from a source structure into a target structure.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theDelta : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the set using info saved in backup attribute theDelta.
        """
    def SetDoBackup(self,toDo : bool) -> None: 
        """
        Sets the flag pointing to the necessity to maintain a modification delta. It is called by the retrieval driver
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetValue(self,theId : int,theValue : int) -> None: 
        """
        Sets the value with the given ID. Raises an exception if theId is not positive
        """
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label) -> TObj_TIntSparseArray: 
        """
        Creates TObj_TIntSparseArray attribute on given label.
        """
    def Size(self) -> int: 
        """
        Returns the number of stored values in the set
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UnsetValue(self,theId : int) -> None: 
        """
        Unsets the value with the given ID. Raises an exception if theId is not positive
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def Value(self,theId : int) -> int: 
        """
        Returns the value by its ID. Raises an exception if no value is stored with this ID
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
class TObj_TIntSparseArray_VecOfData(OCP.NCollection.NCollection_SparseArrayBase):
    """
    Dynamically resizable sparse array of objects
    """
    def Assign(self,theOther : TObj_TIntSparseArray_VecOfData) -> TObj_TIntSparseArray_VecOfData: 
        """
        Explicit assignment operator
        """
    def Bind(self,theIndex : int,theValue : int) -> int: 
        """
        Set a value as explicit method
        """
    def ChangeFind(self,theIndex : int) -> int: 
        """
        Modification access to the item
        """
    def ChangeValue(self,theIndex : int) -> int: 
        """
        Modification access to the item
        """
    def Clear(self) -> None: 
        """
        Clears all the data
        """
    def Exchange(self,theOther : TObj_TIntSparseArray_VecOfData) -> None: 
        """
        Exchange the data of two arrays; can be used primarily to move contents of theOther into the new array in a fast way (without creation of duplicated data)
        """
    def Extent(self) -> int: 
        """
        Returns number of items in the array
        """
    def Find(self,theIndex : int) -> int: 
        """
        Direct const access to the item
        """
    def HasValue(self,theIndex : int) -> bool: 
        """
        Check whether the value at given index is set
        """
    def IsBound(self,theIndex : int) -> bool: 
        """
        Returns True if the item is defined
        """
    def IsEmpty(self) -> bool: 
        """
        Returns True if array is empty
        """
    def SetValue(self,theIndex : int,theValue : int) -> int: 
        """
        Set a value at specified index method
        """
    def Size(self) -> int: 
        """
        Returns number of currently contained items
        """
    def UnBind(self,theIndex : int) -> bool: 
        """
        Remove the item from array
        """
    def UnsetValue(self,theIndex : int) -> bool: 
        """
        Deletes the item from the array; returns True if that item was defined
        """
    def Value(self,theIndex : int) -> int: 
        """
        Direct const access to the item
        """
    def __init__(self,theIncrement : int) -> None: ...
    pass
class TObj_TModel(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Attribute to store OCAF-based models in OCAF tree The persistency mechanism of the TObj_TModel allowes to save and restore various types of models without recompilation of the schemaAttribute to store OCAF-based models in OCAF tree The persistency mechanism of the TObj_TModel allowes to save and restore various types of models without recompilation of the schema
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        This method is used in implementation of ID()
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of TObj_TModel attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def Model(self) -> TObj_Model: 
        """
        Returns the Model object
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty TObj_TModel attribute. It is used by the copy algorithm.
        """
    def Paste(self,theInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is used when copying an attribute from a source structure into a target structure.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theWith : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the backuped contents from <theWith> into this one. It is used when aborting a transaction.
        """
    def Set(self,theModel : TObj_Model) -> None: 
        """
        Sets the Model object
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TObj_TNameContainer(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    This class provides OCAF Attribute to storing the unique names of object in model.This class provides OCAF Attribute to storing the unique names of object in model.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Clear(self) -> None: 
        """
        Remove all names registered in container
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> TObj_DataMapOfNameLabel: 
        """
        Returns the TObj_DataMapOfNameLabel object
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        This method is used in implementation of ID()
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of TObj_TNameContainer attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsRegistered(self,theName : OCP.TCollection.TCollection_HExtendedString) -> bool: 
        """
        Return True is theName is registered in the Map
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty TObj_TNameContainer attribute. It is used by the copy algorithm.
        """
    def Paste(self,theInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is used when copying an attribute from a source structure into a target structure.
        """
    def RecordName(self,theName : OCP.TCollection.TCollection_HExtendedString,theLabel : OCP.TDF.TDF_Label) -> None: 
        """
        Records name with label attached
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveName(self,theName : OCP.TCollection.TCollection_HExtendedString) -> None: 
        """
        Remove name from the map
        """
    def Restore(self,theWith : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the backuped contents from <theWith> into this one. It is used when aborting a transaction.
        """
    def Set(self,theElem : TObj_DataMapOfNameLabel) -> None: 
        """
        Sets the TObj_DataMapOfNameLabel object
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label) -> TObj_TNameContainer: 
        """
        Creates TObj_DataMapOfNameLabel attribute on given label if not exist
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TObj_TObject(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Purpose: OCAF Attribute to storing objects (interfaces) of OCAF-based modelers in the OCAF tree. The persistency mechanism of the TObj_TObject allowes to save and restore objects of various subtypes without recompilation of the schemaPurpose: OCAF Attribute to storing objects (interfaces) of OCAF-based modelers in the OCAF tree. The persistency mechanism of the TObj_TObject allowes to save and restore objects of various subtypes without recompilation of the schema
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool) -> bool: 
        """
        Tell TObj_Object to rise from the dead, i.e. (myElem->IsAlive() == true) after that
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Tell TObj_Object to die, i.e. (myElem->IsAlive() == false) after that
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> TObj_Object: 
        """
        Returns the TObj_Object object
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        This method is used in implementation of ID()
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of TObj_TObject attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty TObj_TObject attribute. It is used by the copy algorithm.
        """
    def Paste(self,theInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is used when copying an attribute from a source structure into a target structure.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theWith : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the backuped contents from <theWith> into this one. It is used when aborting a transaction.
        """
    def Set(self,theElem : TObj_Object) -> None: 
        """
        Sets the TObj_Object object
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label,theElem : TObj_Object) -> TObj_TObject: 
        """
        Creates TObj_TObject attribute on given label
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TObj_TReference(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Attribute for storing references to the objects which implement TObj_Object interface in the OCAF tree. Its persistency mechanism provides transparent method for storing cross-model references. Each reference, when created, registers itself in the referred object, to support back referencesAttribute for storing references to the objects which implement TObj_Object interface in the OCAF tree. Its persistency mechanism provides transparent method for storing cross-model references. Each reference, when created, registers itself in the referred object, to support back references
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Check if back reference exists for reference.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Called after retrieval reference from file.
        """
    def AfterUndo(self,theDelta : OCP.TDF.TDF_AttributeDelta,isForced : bool=False) -> bool: 
        """
        It is necessary for tranzaction mechanism (Undo/Redo).
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Remove back references of it reference if it is in other document.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,theDelta : OCP.TDF.TDF_AttributeDelta,isForced : bool=False) -> bool: 
        """
        It is necessary for tranzaction mechanism (Undo/Redo).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> TObj_Object: 
        """
        Returns the referenced theObject
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        This method is used in implementation of ID()
        """
    def GetLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the referred label.
        """
    def GetMasterLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the Label of master object.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of TObj_TReference attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty TObj_TReference attribute. It is used by the copy algorithm.
        """
    def Paste(self,theInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is used when copying an attribute from a source structure into a target structure.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theWith : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the backuped contents from <theWith> into this one. It is used when aborting a transaction.
        """
    @overload
    def Set(self,theLabel : OCP.TDF.TDF_Label,theMasterLabel : OCP.TDF.TDF_Label) -> None: 
        """
        Sets the reference to the theObject

        Sets the reference to the theObject at indicated Label. It is method for persistent only. Don`t use anywhere else.
        """
    @overload
    def Set(self,theObject : TObj_Object,theMasterLabel : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label,theObject : TObj_Object,theMaster : TObj_Object) -> TObj_TReference: 
        """
        Creates reference on TDF_Label <theLabel> to the object <theObject> and creates backreference from the object <theObject> to <theMaster> one.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TObj_TXYZ(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,theOS : io.BytesIO) -> io.BytesIO: 
        """
        This method dumps the attribute value into the stream
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> OCP.gp.gp_XYZ: 
        """
        Returns the XYZ
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        This method is used in implementation of ID()
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of TObj_TXYZ attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty TObj_TXYZ attribute. It is used by the copy algorithm.
        """
    def Paste(self,theInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is used when copying an attribute from a source structure into a target structure.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theWith : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the backuped contents from <theWith> into this one. It is used when aborting a transaction.
        """
    def Set(self,theXYZ : OCP.gp.gp_XYZ) -> None: 
        """
        Sets the XYZ
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label,theXYZ : OCP.gp.gp_XYZ) -> TObj_TXYZ: 
        """
        Creates attribute and sets the XYZ
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
def HashCode(theHExtendedString : OCP.TCollection.TCollection_HExtendedString,theUpperBound : int) -> int:
    """
    Computes a hash code for the given handle referred to extended string, in the range [1, theUpperBound]
    """
def IsEqual(theStr1 : OCP.TCollection.TCollection_HExtendedString,theStr2 : OCP.TCollection.TCollection_HExtendedString) -> bool:
    """
    None
    """
TObj_Forced: OCP.TObj.TObj_DeletingMode # value = <TObj_DeletingMode.TObj_Forced: 2>
TObj_FreeOnly: OCP.TObj.TObj_DeletingMode # value = <TObj_DeletingMode.TObj_FreeOnly: 0>
TObj_KeepDepending: OCP.TObj.TObj_DeletingMode # value = <TObj_DeletingMode.TObj_KeepDepending: 1>
