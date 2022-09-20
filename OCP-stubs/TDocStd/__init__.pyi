import OCP.TDocStd
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.CDF
import OCP.TDF
import OCP.CDM
import OCP.NCollection
import OCP.PCDM
import io
import OCP.Standard
import OCP.TColStd
import OCP.Message
import OCP.TCollection
import OCP.Resource
__all__  = [
"TDocStd",
"TDocStd_Application",
"TDocStd_ApplicationDelta",
"TDocStd_CompoundDelta",
"TDocStd_Context",
"TDocStd_Document",
"TDocStd_FormatVersion",
"TDocStd_LabelIDMapDataMap",
"TDocStd_Modified",
"TDocStd_MultiTransactionManager",
"TDocStd_Owner",
"TDocStd_PathParser",
"TDocStd_SequenceOfApplicationDelta",
"TDocStd_SequenceOfDocument",
"TDocStd_XLink",
"TDocStd_XLinkIterator",
"TDocStd_XLinkRoot",
"TDocStd_XLinkTool",
"TDocStd_FormatVersion_CURRENT",
"TDocStd_FormatVersion_LOWER",
"TDocStd_FormatVersion_UPPER",
"TDocStd_FormatVersion_VERSION_10",
"TDocStd_FormatVersion_VERSION_11",
"TDocStd_FormatVersion_VERSION_12",
"TDocStd_FormatVersion_VERSION_2",
"TDocStd_FormatVersion_VERSION_3",
"TDocStd_FormatVersion_VERSION_4",
"TDocStd_FormatVersion_VERSION_5",
"TDocStd_FormatVersion_VERSION_6",
"TDocStd_FormatVersion_VERSION_7",
"TDocStd_FormatVersion_VERSION_8",
"TDocStd_FormatVersion_VERSION_9"
]
class TDocStd():
    """
    This package define CAF main classes.
    """
    @staticmethod
    def IDList_s(anIDList : OCP.TDF.TDF_IDList) -> None: 
        """
        specific GUID of this package ============================= Appends to <anIDList> the list of the attributes IDs of this package. CAUTION: <anIDList> is NOT cleared before use.
        """
    def __init__(self) -> None: ...
    pass
class TDocStd_Application(OCP.CDF.CDF_Application, OCP.CDM.CDM_Application, OCP.Standard.Standard_Transient):
    """
    The abstract root class for all application classes. They are in charge of: - Creating documents - Storing documents and retrieving them - Initializing document views. To create a useful OCAF-based application, you derive a class from Application and implement the methods below. You will have to redefine the deferred (virtual) methods Formats, InitDocument, and Resources, and override others. The application is a container for a document, which in its turn is the container of the data framework made up of labels and attributes. Besides furnishing a container for documents, TDocStd_Application provides the following services for them: - Creation of new documents - Activation of documents in sessions of an application - Storage and retrieval of documents - Initialization of document views. Note: If a client needs detailed information concerning the events during the Open/Store operation, a MessageDriver based on Message_PrinterOStream may be used. In case of need client can implement his own version inheriting from Message_Printer class and add it to the Messenger. Also the trace level of messages can be tuned by setting trace level (SetTraceLevel (Gravity )) for the used Printer. By default, trace level is Message_Info, so that all messages are output.The abstract root class for all application classes. They are in charge of: - Creating documents - Storing documents and retrieving them - Initializing document views. To create a useful OCAF-based application, you derive a class from Application and implement the methods below. You will have to redefine the deferred (virtual) methods Formats, InitDocument, and Resources, and override others. The application is a container for a document, which in its turn is the container of the data framework made up of labels and attributes. Besides furnishing a container for documents, TDocStd_Application provides the following services for them: - Creation of new documents - Activation of documents in sessions of an application - Storage and retrieval of documents - Initialization of document views. Note: If a client needs detailed information concerning the events during the Open/Store operation, a MessageDriver based on Message_PrinterOStream may be used. In case of need client can implement his own version inheriting from Message_Printer class and add it to the Messenger. Also the trace level of messages can be tuned by setting trace level (SetTraceLevel (Gravity )) for the used Printer. By default, trace level is Message_Info, so that all messages are output.The abstract root class for all application classes. They are in charge of: - Creating documents - Storing documents and retrieving them - Initializing document views. To create a useful OCAF-based application, you derive a class from Application and implement the methods below. You will have to redefine the deferred (virtual) methods Formats, InitDocument, and Resources, and override others. The application is a container for a document, which in its turn is the container of the data framework made up of labels and attributes. Besides furnishing a container for documents, TDocStd_Application provides the following services for them: - Creation of new documents - Activation of documents in sessions of an application - Storage and retrieval of documents - Initialization of document views. Note: If a client needs detailed information concerning the events during the Open/Store operation, a MessageDriver based on Message_PrinterOStream may be used. In case of need client can implement his own version inheriting from Message_Printer class and add it to the Messenger. Also the trace level of messages can be tuned by setting trace level (SetTraceLevel (Gravity )) for the used Printer. By default, trace level is Message_Info, so that all messages are output.
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
    def CanRetrieve(self,theFolder : OCP.TCollection.TCollection_ExtendedString,theName : OCP.TCollection.TCollection_ExtendedString,theVersion : OCP.TCollection.TCollection_ExtendedString,theAppendMode : bool) -> OCP.PCDM.PCDM_ReaderStatus: 
        """
        None

        None
        """
    @overload
    def CanRetrieve(self,theFolder : OCP.TCollection.TCollection_ExtendedString,theName : OCP.TCollection.TCollection_ExtendedString,theAppendMode : bool) -> OCP.PCDM.PCDM_ReaderStatus: ...
    def Close(self,aDoc : TDocStd_Document) -> None: 
        """
        Close the given document. the document is not any more handled by the applicative session.
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
    def Format(self,aFileName : OCP.TCollection.TCollection_ExtendedString,theFormat : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        try to retrieve a Format directly in the file or in application resource by using extension. returns True if found;
        """
    def GetDocument(self,index : int,aDoc : TDocStd_Document) -> Any: 
        """
        Constructs the new document aDoc. aDoc is identified by the index index which is any integer between 1 and n where n is the number of documents returned by NbDocument. Example Handle(TDocStd_Application) anApp; if (!CafTest::Find(A)) return 1; Handle(TDocStd) aDoc; Standard_Integer nbdoc = anApp->NbDocuments(); for (Standard_Integer i = 1; i <= nbdoc; i++) { aApp->GetDocument(i,aDoc);
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
    @staticmethod
    def Load_s(aGUID : OCP.Standard.Standard_GUID) -> OCP.CDF.CDF_Application: 
        """
        plugs an application.
        """
    def MessageDriver(self) -> OCP.Message.Message_Messenger: 
        """
        Returns default messenger;
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
    def NewDocument(self,format : OCP.TCollection.TCollection_ExtendedString,aDoc : OCP.CDM.CDM_Document) -> Any: 
        """
        Constructs the empty new document aDoc. This document will have the format format. If InitDocument is redefined for a specific application, the new document is handled by the applicative session.

        A non-virtual method taking a TDocStd_Documment object as an input. Internally it calls a virtual method NewDocument() with CDM_Document object.
        """
    @overload
    def NewDocument(self,format : OCP.TCollection.TCollection_ExtendedString,aDoc : TDocStd_Document) -> Any: ...
    def OnAbortTransaction(self,theDoc : TDocStd_Document) -> None: 
        """
        Notification that is fired at each AbortTransaction event.
        """
    def OnCommitTransaction(self,theDoc : TDocStd_Document) -> None: 
        """
        Notification that is fired at each CommitTransaction event.
        """
    def OnOpenTransaction(self,theDoc : TDocStd_Document) -> None: 
        """
        Notification that is fired at each OpenTransaction event.
        """
    @overload
    def Open(self,theIStream : io.BytesIO,theDoc : TDocStd_Document,theFilter : OCP.PCDM.PCDM_ReaderFilter,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_ReaderStatus: 
        """
        Retrieves the document from specified file. In order not to override a version of the document which is already in memory, this method can be made to depend on the value returned by IsInSession.

        Retrieves the document from specified file. In order not to override a version of the document which is already in memory, this method can be made to depend on the value returned by IsInSession.

        Retrieves document from standard stream.

        Retrieves document from standard stream.
        """
    @overload
    def Open(self,thePath : OCP.TCollection.TCollection_ExtendedString,theDoc : TDocStd_Document,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_ReaderStatus: ...
    @overload
    def Open(self,thePath : OCP.TCollection.TCollection_ExtendedString,theDoc : TDocStd_Document,theFilter : OCP.PCDM.PCDM_ReaderFilter,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_ReaderStatus: ...
    @overload
    def Open(self,theIStream : io.BytesIO,theDoc : TDocStd_Document,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_ReaderStatus: ...
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
        Returns the name of the file containing the resources of this application, for support of legacy method of loading formats data from resource files.
        """
    @overload
    def Retrieve(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,UseStorageConfiguration : bool=True,theFilter : OCP.PCDM.PCDM_ReaderFilter=None,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.CDM.CDM_Document: 
        """
        This method retrieves a document from the database. If the Document references other documents which have been updated, the latest version of these documents will be used if {UseStorageConfiguration} is Standard_True. The content of {aFolder}, {aName} and {aVersion} depends on the Database Manager system. If the DBMS is only based on the OS, {aFolder} is a directory and {aName} is the name of a file. In this case the use of the syntax with {aVersion} has no sense. For example:

        This method retrieves a document from the database. If the Document references other documents which have been updated, the latest version of these documents will be used if {UseStorageConfiguration} is Standard_True. -- If the DBMS is only based on the OS, this syntax should not be used.
        """
    @overload
    def Retrieve(self,aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString,UseStorageConfiguration : bool=True,theFilter : OCP.PCDM.PCDM_ReaderFilter=None,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.CDM.CDM_Document: ...
    @overload
    def Save(self,theDoc : TDocStd_Document,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: 
        """
        Save aDoc active document. Exceptions: Standard_NotImplemented if the document was not retrieved in the applicative session by using Open.

        Save the document overwriting the previous file
        """
    @overload
    def Save(self,theDoc : TDocStd_Document,theStatusMessage : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveAs(self,theDoc : TDocStd_Document,theOStream : io.BytesIO,theStatusMessage : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: 
        """
        Save the active document in the file <name> in the path <path> ; o verwrites the file if it already exists.

        Save theDoc to standard SEEKABLE stream theOStream. the stream should support SEEK functionality

        Save the active document in the file <name> in the path <path> . overwrite the file if it already exist.

        Save theDoc TO standard SEEKABLE stream theOStream. the stream should support SEEK functionality
        """
    @overload
    def SaveAs(self,theDoc : TDocStd_Document,path : OCP.TCollection.TCollection_ExtendedString,theStatusMessage : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveAs(self,theDoc : TDocStd_Document,path : OCP.TCollection.TCollection_ExtendedString,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveAs(self,theDoc : TDocStd_Document,theOStream : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.PCDM.PCDM_StoreStatus: ...
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
    def WritingFormats(self,theFormats : OCP.TColStd.TColStd_SequenceOfAsciiString) -> None: 
        """
        Returns the sequence of writing formats supported by the application.
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
class TDocStd_ApplicationDelta(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,anOS : io.BytesIO) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetDocuments(self) -> TDocStd_SequenceOfDocument: 
        """
        None

        None
        """
    def GetName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None

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
    def SetName(self,theName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None

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
class TDocStd_CompoundDelta(OCP.TDF.TDF_Delta, OCP.Standard.Standard_Transient):
    """
    A delta set is available at <aSourceTime>. If applied, it restores the TDF_Data in the state it was at <aTargetTime>.A delta set is available at <aSourceTime>. If applied, it restores the TDF_Data in the state it was at <aTargetTime>.A delta set is available at <aSourceTime>. If applied, it restores the TDF_Data in the state it was at <aTargetTime>.
    """
    def AttributeDeltas(self) -> OCP.TDF.TDF_AttributeDeltaList: 
        """
        Returns the field <myAttDeltaList>.

        Returns the field <myAttDeltaList>.
        """
    def BeginTime(self) -> int: 
        """
        Returns the field <myBeginTime>.

        Returns the field <myBeginTime>.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> None: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndTime(self) -> int: 
        """
        Returns the field <myEndTime>.

        Returns the field <myEndTime>.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsApplicable(self,aCurrentTime : int) -> bool: 
        """
        Returns true if the Undo action of <me> is applicable at <aCurrentTime>.

        Returns true if the Undo action of <me> is applicable at <aCurrentTime>.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if there is nothing to undo.

        Returns true if there is nothing to undo.
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
    def Labels(self,aLabelList : OCP.TDF.TDF_LabelList) -> None: 
        """
        Adds in <aLabelList> the labels of the attribute deltas. Caution: <aLabelList> is not cleared before use.
        """
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns a name associated with this delta.

        Returns a name associated with this delta.
        """
    def SetName(self,theName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Associates a name <theName> with this delta

        Associates a name <theName> with this delta
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
class TDocStd_Context():
    """
    None
    """
    def ModifiedReferences(self) -> bool: 
        """
        None
        """
    def SetModifiedReferences(self,Mod : bool) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TDocStd_Document(OCP.CDM.CDM_Document, OCP.Standard.Standard_Transient):
    """
    The contents of a TDocStd_Application, a document is a container for a data framework composed of labels and attributes. As such, TDocStd_Document is the entry point into the data framework. To gain access to the data, you create a document as follows: Handle(TDocStd_Document) MyDF = new TDocStd_Document The document also allows you to manage: - modifications, providing Undo and Redo functions. - command transactions. Warning: The only data saved is the framework (TDF_Data)The contents of a TDocStd_Application, a document is a container for a data framework composed of labels and attributes. As such, TDocStd_Document is the entry point into the data framework. To gain access to the data, you create a document as follows: Handle(TDocStd_Document) MyDF = new TDocStd_Document The document also allows you to manage: - modifications, providing Undo and Redo functions. - command transactions. Warning: The only data saved is the framework (TDF_Data)The contents of a TDocStd_Application, a document is a container for a data framework composed of labels and attributes. As such, TDocStd_Document is the entry point into the data framework. To gain access to the data, you create a document as follows: Handle(TDocStd_Document) MyDF = new TDocStd_Document The document also allows you to manage: - modifications, providing Undo and Redo functions. - command transactions. Warning: The only data saved is the framework (TDF_Data)
    """
    def AbortCommand(self) -> None: 
        """
        Abort the Command transaction. Does nothing If there is no Command transaction open.
        """
    def AddComment(self,aComment : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        appends a comment into comments of this document.
        """
    def Application(self) -> OCP.CDM.CDM_Application: 
        """
        None
        """
    def BeforeClose(self) -> None: 
        """
        Prepares document for closing
        """
    def CanClose(self) -> OCP.CDM.CDM_CanCloseStatus: 
        """
        None
        """
    def CanCloseReference(self,aDocument : OCP.CDM.CDM_Document,aReferenceIdentifier : int) -> bool: 
        """
        A referenced document may indicate through this virtual method that it does not allow the closing of aDocument which it references through the reference aReferenceIdentifier. By default returns Standard_True.
        """
    def ChangeStorageFormat(self,newStorageFormat : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        methods for the nested transaction mode
        """
    def ChangeStorageFormatVersion(self,theVersion : TDocStd_FormatVersion) -> None: 
        """
        Sets version of the format to be used to store the document
        """
    def ClearRedos(self) -> None: 
        """
        Remove all stored Redos
        """
    def ClearUndos(self) -> None: 
        """
        Remove all stored Undos and Redos
        """
    def Close(self) -> None: 
        """
        None
        """
    def CloseReference(self,aDocument : OCP.CDM.CDM_Document,aReferenceIdentifier : int) -> None: 
        """
        A referenced document may update its internal data structure when {aDocument} which it references through the reference {aReferenceIdentifier} is being closed. By default this method does nothing.
        """
    def Comment(self) -> str: 
        """
        Returns the first of associated comments. By default the comment is an empty string.
        """
    def Comments(self,aComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        returns the associated comments through <aComments>. Returns empty sequence if no comments are associated.
        """
    def CommitCommand(self) -> bool: 
        """
        Commits documents transactions and fills the transaction manager with documents that have been changed during the transaction. If no command transaction is open, nothing is done. Returns True if a new delta has been added to myUndos.
        """
    def CopyReference(self,aFromDocument : OCP.CDM.CDM_Document,aReferenceIdentifier : int) -> int: 
        """
        Copies a reference to this document. This method avoid retrieval of referenced document. The arguments are the original document and a valid reference identifier Returns the local identifier.
        """
    @overload
    def CreateReference(self,anOtherDocument : OCP.CDM.CDM_Document) -> int: 
        """
        Creates a reference from this document to {anOtherDocument}. Returns a reference identifier. This reference identifier is unique in the document and will not be used for the next references, even after the storing of the document. If there is already a reference between the two documents, the reference is not created, but its reference identifier is returned.

        None

        None
        """
    @overload
    def CreateReference(self,aMetaData : OCP.CDM.CDM_MetaData,anApplication : OCP.CDM.CDM_Application,aDocumentVersion : int,UseStorageConfiguration : bool) -> int: ...
    @overload
    def CreateReference(self,aMetaData : OCP.CDM.CDM_MetaData,aReferenceIdentifier : int,anApplication : OCP.CDM.CDM_Application,aToDocumentVersion : int,UseStorageConfiguration : bool) -> None: ...
    @staticmethod
    def CurrentStorageFormatVersion_s() -> TDocStd_FormatVersion: 
        """
        Returns current storage format version of the document.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DeepReferences(self,aDocument : OCP.CDM.CDM_Document) -> bool: 
        """
        returns True is this document references aDocument;
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        gets the `FileFormat`.Description resource.
        """
    def Document(self,aReferenceIdentifier : int) -> OCP.CDM.CDM_Document: 
        """
        Returns the To Document of the reference identified by aReferenceIdentifier. If the ToDocument is stored and has not yet been retrieved, this method will retrieve it.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EmptyLabelsSavingMode(self) -> bool: 
        """
        Returns saving mode for empty labels.

        Returns saving mode for empty labels.
        """
    def Extensions(self,Extensions : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        by default empties the extensions.
        """
    def FileExtension(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        gets the Desktop.Domain.Application.`FileFormat`.FileExtension resource.
        """
    def FindDescription(self) -> bool: 
        """
        None
        """
    def FindFileExtension(self) -> bool: 
        """
        None
        """
    def Folder(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def FromReferencesNumber(self) -> int: 
        """
        returns the number of references having this document as To Document.
        """
    def GetAlternativeDocument(self,aFormat : OCP.TCollection.TCollection_ExtendedString,anAlternativeDocument : OCP.CDM.CDM_Document) -> bool: 
        """
        This method can be redefined to extract another document in a different format. For example, to extract a Shape from an applicative document.
        """
    def GetAvailableRedos(self) -> int: 
        """
        Returns the number of redos stored in this document. If this figure is greater than 0, the method Redo can be used.
        """
    def GetAvailableUndos(self) -> int: 
        """
        Returns the number of undos stored in this document. If this figure is greater than 0, the method Undo can be used.
        """
    def GetData(self) -> OCP.TDF.TDF_Data: 
        """
        None
        """
    def GetModified(self) -> OCP.TDF.TDF_LabelMap: 
        """
        Returns the labels which have been modified in this document.
        """
    def GetName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        raise if <me> is not saved.
        """
    def GetPath(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        returns the OS path of the file, in which one <me> is saved. Raise an exception if <me> is not saved.
        """
    def GetRedos(self) -> OCP.TDF.TDF_DeltaList: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSavedTime(self) -> int: 
        """
        Returns value of <mySavedTime> to be used later in SetSavedTime()

        Returns value of <mySavedTime> to be used later in SetSavedTime()
        """
    def GetUndoLimit(self) -> int: 
        """
        The current limit on the number of undos
        """
    def GetUndos(self) -> OCP.TDF.TDF_DeltaList: 
        """
        None
        """
    @staticmethod
    def Get_s(L : OCP.TDF.TDF_Label) -> TDocStd_Document: 
        """
        Will Abort any execution, clear fields returns the document which contains <L>. raises an exception if the document is not found.
        """
    def HasOpenCommand(self) -> bool: 
        """
        returns True if a Command transaction is open in the curret .
        """
    def HasRequestedFolder(self) -> bool: 
        """
        None
        """
    def HasRequestedPreviousVersion(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitDeltaCompaction(self) -> bool: 
        """
        Initializes the procedure of delta compaction Returns false if there is no delta to compact Marks the last delta as a "from" delta
        """
    def IsChanged(self) -> bool: 
        """
        returns True if document differs from the state of last saving. this method have to be called only working in the transaction mode

        returns True if document differs from the state of last saving. this method have to be called only working in the transaction mode
        """
    def IsEmpty(self) -> bool: 
        """
        Returns True if the main label has no attributes
        """
    def IsInSession(self,aReferenceIdentifier : int) -> bool: 
        """
        returns True if the To Document of the reference identified by aReferenceIdentifier is in session, False if it corresponds to a not yet retrieved document.
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
    def IsModified(self) -> bool: 
        """
        returns true if the version is greater than the storage version
        """
    def IsNestedTransactionMode(self) -> bool: 
        """
        Returns Standard_True if mode is set

        Returns Standard_True if mode is set
        """
    @overload
    def IsOpened(self) -> bool: 
        """
        None

        returns true if the document corresponding to the given reference has been retrieved and opened. Otherwise returns false. This method does not retrieve the referenced document
        """
    @overload
    def IsOpened(self,aReferenceIdentifier : int) -> bool: ...
    @overload
    def IsReadOnly(self,aReferenceIdentifier : int) -> bool: 
        """
        indicates that this document cannot be modified.

        indicates that the referenced document cannot be modified,
        """
    @overload
    def IsReadOnly(self) -> bool: ...
    def IsSaved(self) -> bool: 
        """
        the document is saved in a file.
        """
    @overload
    def IsStored(self) -> bool: 
        """
        returns True if the To Document of the reference identified by aReferenceIdentifier has already been stored, False otherwise.

        None
        """
    @overload
    def IsStored(self,aReferenceIdentifier : int) -> bool: ...
    def IsUpToDate(self,aReferenceIdentifier : int) -> bool: 
        """
        returns true if the modification counter found in the given reference is equal to the actual modification counter of the To Document. This method is able to deal with a reference to a not retrieved document.
        """
    def IsValid(self) -> bool: 
        """
        Returns False if the document has been modified but not recomputed.
        """
    def LoadResources(self) -> None: ...
    def Main(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the main label in this data framework. By definition, this is the label with the entry 0:1.
        """
    def MetaData(self) -> OCP.CDM.CDM_MetaData: 
        """
        None
        """
    def ModificationMode(self) -> bool: 
        """
        returns True if changes allowed only inside transactions

        returns True if changes allowed only inside transactions
        """
    def Modifications(self) -> int: 
        """
        returns the current modification counter.
        """
    def Modify(self) -> None: 
        """
        Indicates that this document has been modified. This method increments the modification counter.
        """
    def Name(self,aReferenceIdentifier : int) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        returns the name of the metadata of the To Document of the reference identified by aReferenceIdentifier.
        """
    def NewCommand(self) -> None: 
        """
        Launches a new command. This command may be undone.
        """
    def Open(self,anApplication : OCP.CDM.CDM_Application) -> None: 
        """
        None
        """
    def OpenCommand(self) -> None: 
        """
        Opens a new command transaction in this document. You can use HasOpenCommand to see whether a command is already open. Exceptions Standard_DomainError if a command is already open in this document.
        """
    def PerformDeltaCompaction(self) -> bool: 
        """
        Performs the procedure of delta compaction Makes all deltas starting from "from" delta till the last one to be one delta.
        """
    def Print(self,anOStream : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def PurgeModified(self) -> None: 
        """
        Remove all modifications. After this call The document becomesagain Valid.
        """
    def Recompute(self) -> None: 
        """
        Recompute if the document was not valid and propagate the reccorded modification.
        """
    def Redo(self) -> bool: 
        """
        Will REDO one step, returns False if no redo was done (Redos == 0). Otherwise, true is returned, and one step in the list of redoes is done again.
        """
    def Reference(self,aReferenceIdentifier : int) -> OCP.CDM.CDM_Reference: 
        """
        None
        """
    def ReferenceCounter(self) -> int: 
        """
        None
        """
    def RemoveAllReferences(self) -> None: 
        """
        Removes all references having this document for From Document.
        """
    def RemoveFirstUndo(self) -> None: 
        """
        Removes the first undo in the list of document undos. It is used in the application when the undo limit is exceed.
        """
    def RemoveReference(self,aReferenceIdentifier : int) -> None: 
        """
        Removes the reference between the From Document and the To Document identified by a reference identifier.
        """
    def RequestedComment(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def RequestedFolder(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def RequestedName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Determines under which the document is going to be store. By default the name of the document will be used. If the document has no name its presentation will be used.
        """
    def RequestedPreviousVersion(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def SetComment(self,aComment : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        associates a comment with this document.
        """
    def SetComments(self,aComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        associates a comments with this document.
        """
    def SetData(self,data : OCP.TDF.TDF_Data) -> None: 
        """
        None
        """
    def SetEmptyLabelsSavingMode(self,isAllowed : bool) -> None: 
        """
        Sets saving mode for empty labels. If Standard_True, empty labels will be saved.

        Sets saving mode for empty labels. If Standard_True, empty labels will be saved.
        """
    def SetIsReadOnly(self) -> None: 
        """
        None
        """
    def SetIsUpToDate(self,aReferenceIdentifier : int) -> None: 
        """
        Resets the modification counter in the given reference to the actual modification counter of its To Document. This method should be called after the application has updated this document.
        """
    def SetMetaData(self,aMetaData : OCP.CDM.CDM_MetaData) -> None: 
        """
        associates database information to a document which has been stored. The name of the document is now the name which has beenused to store the data.
        """
    def SetModificationMode(self,theTransactionOnly : bool) -> None: 
        """
        if theTransactionOnly is True changes is denied outside transactions

        if theTransactionOnly is True changes is denied outside transactions
        """
    def SetModifications(self,Modifications : int) -> None: 
        """
        None
        """
    def SetModified(self,L : OCP.TDF.TDF_Label) -> None: 
        """
        Notify the label as modified, the Document becomes UnValid. returns True if <L> has been notified as modified.
        """
    @overload
    def SetNestedTransactionMode(self,isAllowed : bool=True) -> None: 
        """
        Sets nested transaction mode if isAllowed == Standard_True

        Sets nested transaction mode if isAllowed == Standard_True
        """
    @overload
    def SetNestedTransactionMode(self,isAllowed : bool) -> None: ...
    def SetReferenceCounter(self,aReferenceCounter : int) -> None: 
        """
        None
        """
    def SetRequestedComment(self,aComment : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        defines the Comment with which the object should be stored.
        """
    def SetRequestedFolder(self,aFolder : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        defines the folder in which the object should be stored.
        """
    def SetRequestedName(self,aName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        defines the name under which the object should be stored.
        """
    def SetRequestedPreviousVersion(self,aPreviousVersion : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    def SetSaved(self) -> None: 
        """
        This method have to be called to show document that it has been saved

        This method have to be called to show document that it has been saved
        """
    def SetSavedTime(self,theTime : int) -> None: 
        """
        Say to document what it is not saved. Use value, returned earlier by GetSavedTime().

        Say to document what it is not saved. Use value, returned earlier by GetSavedTime().
        """
    def SetUndoLimit(self,L : int) -> None: 
        """
        Set the limit on the number of Undo Delta stored 0 will disable Undo on the document A negative value means no limit. Note that by default Undo is disabled. Enabling it will take effect with the next call to NewCommand. Of course this limit is the same for Redo
        """
    def ShallowReferences(self,aDocument : OCP.CDM.CDM_Document) -> bool: 
        """
        returns True is this document references aDocument;
        """
    def StorageFormat(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def StorageFormatVersion(self) -> TDocStd_FormatVersion: 
        """
        Returns version of the format to be used to store the document
        """
    def StorageVersion(self) -> int: 
        """
        returns the value of the modification counter at the time of storage. By default returns 0.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToReferencesNumber(self) -> int: 
        """
        returns the number of references having this document as From Document.
        """
    def UnModify(self) -> None: 
        """
        None
        """
    def Undo(self) -> bool: 
        """
        Will UNDO one step, returns False if no undo was done (Undos == 0). Otherwise, true is returned and one step in the list of undoes is undone.
        """
    def UnsetIsReadOnly(self) -> None: 
        """
        None
        """
    def UnsetIsStored(self) -> None: 
        """
        None
        """
    def UnsetRequestedPreviousVersion(self) -> None: 
        """
        None
        """
    def Update(self,aToDocument : OCP.CDM.CDM_Document,aReferenceIdentifier : int,aModifContext : capsule) -> None: 
        """
        This method Update will be called to signal the end of the modified references list. The document should be recomputed and UpdateFromDocuments should be called. Update should returns True in case of success, false otherwise. In case of Failure, additional information can be given in ErrorString. Update the document by propagation ================================== Update the document from internal stored modifications. If you want to undoing this operation, please call NewCommand before. to change format (advanced programming) ================
        """
    def UpdateFromDocuments(self,aModifContext : capsule) -> None: 
        """
        call virtual method Update on all referencing documents. This method keeps the list of the -- documents to process.It may be the starting of an update -- cycle. If not, the reentrant calls made by Update method (without argument) will append the referencing documents to the list and call the Update method (with arguments). Only the first call to UpdateFromDocuments generate call to Update().
        """
    def UpdateReferences(self,aDocEntry : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Set modifications on labels impacted by external references to the entry. The document becomes invalid and must be recomputed.
        """
    def __init__(self,astorageformat : OCP.TCollection.TCollection_ExtendedString) -> None: ...
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
class TDocStd_FormatVersion():
    """
    Storage format versions of OCAF documents in XML and binary file formats.

    Members:

      TDocStd_FormatVersion_VERSION_2

      TDocStd_FormatVersion_VERSION_3

      TDocStd_FormatVersion_VERSION_4

      TDocStd_FormatVersion_VERSION_5

      TDocStd_FormatVersion_VERSION_6

      TDocStd_FormatVersion_VERSION_7

      TDocStd_FormatVersion_VERSION_8

      TDocStd_FormatVersion_VERSION_9

      TDocStd_FormatVersion_VERSION_10

      TDocStd_FormatVersion_VERSION_11

      TDocStd_FormatVersion_VERSION_12

      TDocStd_FormatVersion_CURRENT
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
    TDocStd_FormatVersion_CURRENT: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_12: 12>
    TDocStd_FormatVersion_VERSION_10: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_10: 10>
    TDocStd_FormatVersion_VERSION_11: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_11: 11>
    TDocStd_FormatVersion_VERSION_12: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_12: 12>
    TDocStd_FormatVersion_VERSION_2: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_2: 2>
    TDocStd_FormatVersion_VERSION_3: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_3: 3>
    TDocStd_FormatVersion_VERSION_4: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_4: 4>
    TDocStd_FormatVersion_VERSION_5: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_5: 5>
    TDocStd_FormatVersion_VERSION_6: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_6: 6>
    TDocStd_FormatVersion_VERSION_7: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_7: 7>
    TDocStd_FormatVersion_VERSION_8: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_8: 8>
    TDocStd_FormatVersion_VERSION_9: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_9: 9>
    __entries: dict # value = {'TDocStd_FormatVersion_VERSION_2': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_2: 2>, None), 'TDocStd_FormatVersion_VERSION_3': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_3: 3>, None), 'TDocStd_FormatVersion_VERSION_4': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_4: 4>, None), 'TDocStd_FormatVersion_VERSION_5': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_5: 5>, None), 'TDocStd_FormatVersion_VERSION_6': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_6: 6>, None), 'TDocStd_FormatVersion_VERSION_7': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_7: 7>, None), 'TDocStd_FormatVersion_VERSION_8': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_8: 8>, None), 'TDocStd_FormatVersion_VERSION_9': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_9: 9>, None), 'TDocStd_FormatVersion_VERSION_10': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_10: 10>, None), 'TDocStd_FormatVersion_VERSION_11': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_11: 11>, None), 'TDocStd_FormatVersion_VERSION_12': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_12: 12>, None), 'TDocStd_FormatVersion_CURRENT': (<TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_12: 12>, None)}
    __members__: dict # value = {'TDocStd_FormatVersion_VERSION_2': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_2: 2>, 'TDocStd_FormatVersion_VERSION_3': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_3: 3>, 'TDocStd_FormatVersion_VERSION_4': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_4: 4>, 'TDocStd_FormatVersion_VERSION_5': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_5: 5>, 'TDocStd_FormatVersion_VERSION_6': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_6: 6>, 'TDocStd_FormatVersion_VERSION_7': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_7: 7>, 'TDocStd_FormatVersion_VERSION_8': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_8: 8>, 'TDocStd_FormatVersion_VERSION_9': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_9: 9>, 'TDocStd_FormatVersion_VERSION_10': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_10: 10>, 'TDocStd_FormatVersion_VERSION_11': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_11: 11>, 'TDocStd_FormatVersion_VERSION_12': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_12: 12>, 'TDocStd_FormatVersion_CURRENT': <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_12: 12>}
    pass
class TDocStd_LabelIDMapDataMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDocStd_LabelIDMapDataMap) -> TDocStd_LabelIDMapDataMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TDF.TDF_Label,theItem : OCP.TDF.TDF_IDMap) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TDF.TDF_Label,theItem : OCP.TDF.TDF_IDMap) -> OCP.TDF.TDF_IDMap: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_IDMap: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_IDMap: 
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
    def Exchange(self,theOther : TDocStd_LabelIDMapDataMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_IDMap: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TDF.TDF_Label,theValue : OCP.TDF.TDF_IDMap) -> bool: ...
    def IsBound(self,theKey : OCP.TDF.TDF_Label) -> bool: 
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
    def Seek(self,theKey : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_IDMap: 
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
    def UnBind(self,theKey : OCP.TDF.TDF_Label) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : TDocStd_LabelIDMapDataMap) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDocStd_Modified(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Transient attribute which register modified labels. This attribute is attached to root label.Transient attribute which register modified labels. This attribute is attached to root label.Transient attribute which register modified labels. This attribute is attached to root label.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AddLabel(self,L : OCP.TDF.TDF_Label) -> bool: 
        """
        add <L> as modified
        """
    @staticmethod
    def Add_s(alabel : OCP.TDF.TDF_Label) -> bool: 
        """
        None
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
        None
        """
    @staticmethod
    def Clear_s(access : OCP.TDF.TDF_Label) -> None: 
        """
        remove all modified labels. becomes empty
        """
    @staticmethod
    def Contains_s(alabel : OCP.TDF.TDF_Label) -> bool: 
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
        None
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
    def Get(self) -> OCP.TDF.TDF_LabelMap: 
        """
        returns modified label map
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Modified methods ================
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(access : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_LabelMap: 
        """
        if <IsEmpty> raise an exception.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
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
    def IsEmpty(self) -> bool: 
        """
        None
        """
    @staticmethod
    def IsEmpty_s(access : OCP.TDF.TDF_Label) -> bool: 
        """
        API class methods =================
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveLabel(self,L : OCP.TDF.TDF_Label) -> bool: 
        """
        remove <L> as modified
        """
    @staticmethod
    def Remove_s(alabel : OCP.TDF.TDF_Label) -> bool: 
        """
        None
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self) -> None: ...
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
class TDocStd_MultiTransactionManager(OCP.Standard.Standard_Transient):
    """
    Class for synchronization of transactions within multiple documents. Each transaction of this class involvess one transaction in each modified document.Class for synchronization of transactions within multiple documents. Each transaction of this class involvess one transaction in each modified document.Class for synchronization of transactions within multiple documents. Each transaction of this class involvess one transaction in each modified document.
    """
    def AbortCommand(self) -> None: 
        """
        Unsets the flag of started manager transaction and aborts transaction in each document.
        """
    def AddDocument(self,theDoc : TDocStd_Document) -> None: 
        """
        Adds the document to the transaction manager and checks if it has been already added
        """
    def ClearRedos(self) -> None: 
        """
        Clears redos in the manager and in documents.
        """
    def ClearUndos(self) -> None: 
        """
        Clears undos in the manager and in documents.
        """
    @overload
    def CommitCommand(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Commits transaction in all documents and fills the transaction manager with the documents that have been changed during the transaction. Returns True if new data has been added to myUndos. NOTE: All nested transactions in the documents will be committed.

        Makes the same steps as the previous function but defines the name for transaction. Returns True if new data has been added to myUndos.
        """
    @overload
    def CommitCommand(self) -> bool: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Documents(self) -> TDocStd_SequenceOfDocument: 
        """
        Returns the added documents to the transaction manager.

        Returns the added documents to the transaction manager.
        """
    def DumpTransaction(self,theOS : io.BytesIO) -> None: 
        """
        Dumps transactions in undos and redos
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetAvailableRedos(self) -> TDocStd_SequenceOfApplicationDelta: 
        """
        Returns available manager redos.

        Returns available manager redos.
        """
    def GetAvailableUndos(self) -> TDocStd_SequenceOfApplicationDelta: 
        """
        Returns available manager undos.

        Returns available manager undos.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetUndoLimit(self) -> int: 
        """
        Returns undo limit for the manager.

        Returns undo limit for the manager.
        """
    def HasOpenCommand(self) -> bool: 
        """
        Returns true if a transaction is opened.

        Returns true if a transaction is opened.
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
    def IsNestedTransactionMode(self) -> bool: 
        """
        Returns Standard_True if NestedTransaction mode is set. Methods for protection of changes outside transactions

        Returns Standard_True if NestedTransaction mode is set. Methods for protection of changes outside transactions
        """
    def ModificationMode(self) -> bool: 
        """
        Returns True if changes are allowed only inside transactions.

        Returns True if changes are allowed only inside transactions.
        """
    def OpenCommand(self) -> None: 
        """
        Opens transaction in each document and sets the flag that transaction is opened. If there are already opened transactions in the documents, these transactions will be aborted before opening new ones.
        """
    def Redo(self) -> None: 
        """
        Redoes the current transaction of the application. It calls the Redo () method of the document being on top of the manager list of redos (list.First()) and moves the list item to the top of the list of manager undos (list.Prepend(item)).
        """
    def RemoveDocument(self,theDoc : TDocStd_Document) -> None: 
        """
        Removes the document from the transaction manager.
        """
    def RemoveLastUndo(self) -> None: 
        """
        Removes undo information from the list of undos of the manager and all documents which have been modified during the transaction.
        """
    def SetModificationMode(self,theTransactionOnly : bool) -> None: 
        """
        If theTransactionOnly is True, denies all changes outside transactions.
        """
    def SetNestedTransactionMode(self,isAllowed : bool=True) -> None: 
        """
        Sets nested transaction mode if isAllowed == Standard_True NOTE: field myIsNestedTransactionMode exists only for synchronization between several documents and has no effect on transactions of multitransaction manager.
        """
    def SetUndoLimit(self,theLimit : int) -> None: 
        """
        Sets undo limit for the manager and all documents.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Undo(self) -> None: 
        """
        Undoes the current transaction of the manager. It calls the Undo () method of the document being on top of the manager list of undos (list.First()) and moves the list item to the top of the list of manager redos (list.Prepend(item)).
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
class TDocStd_Owner(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    This attribute located at the root label of the framework contains a back reference to the owner TDocStd_Document, providing access to the document from any label. private class Owner;This attribute located at the root label of the framework contains a back reference to the owner TDocStd_Document, providing access to the document from any label. private class Owner;This attribute located at the root label of the framework contains a back reference to the owner TDocStd_Document, providing access to the document from any label. private class Owner;
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
        None
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
    def GetDocument(self) -> TDocStd_Document: 
        """
        None
        """
    @staticmethod
    def GetDocument_s(ofdata : OCP.TDF.TDF_Data) -> TDocStd_Document: 
        """
        Owner methods ===============
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods =============
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
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
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetDocument(self,document : TDocStd_Document) -> None: 
        """
        None

        None
        """
    @staticmethod
    def SetDocument_s(indata : OCP.TDF.TDF_Data,doc : TDocStd_Document) -> None: 
        """
        None

        None
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self) -> None: ...
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
class TDocStd_PathParser():
    """
    parse an OS path
    """
    def Extension(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def Length(self) -> int: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def Parse(self) -> None: 
        """
        None
        """
    def Path(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def Trek(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def __init__(self,path : OCP.TCollection.TCollection_ExtendedString) -> None: ...
    pass
class TDocStd_SequenceOfApplicationDelta(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TDocStd_ApplicationDelta) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : TDocStd_SequenceOfApplicationDelta) -> None: ...
    def Assign(self,theOther : TDocStd_SequenceOfApplicationDelta) -> TDocStd_SequenceOfApplicationDelta: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> TDocStd_ApplicationDelta: 
        """
        First item access
        """
    def ChangeLast(self) -> TDocStd_ApplicationDelta: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> TDocStd_ApplicationDelta: 
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
    def First(self) -> TDocStd_ApplicationDelta: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : TDocStd_ApplicationDelta) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TDocStd_SequenceOfApplicationDelta) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : TDocStd_ApplicationDelta) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TDocStd_SequenceOfApplicationDelta) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> TDocStd_ApplicationDelta: 
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
    def Prepend(self,theItem : TDocStd_ApplicationDelta) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TDocStd_SequenceOfApplicationDelta) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : TDocStd_ApplicationDelta) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TDocStd_SequenceOfApplicationDelta) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> TDocStd_ApplicationDelta: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TDocStd_SequenceOfApplicationDelta) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TDocStd_SequenceOfDocument(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TDocStd_SequenceOfDocument) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : TDocStd_Document) -> None: ...
    def Assign(self,theOther : TDocStd_SequenceOfDocument) -> TDocStd_SequenceOfDocument: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> TDocStd_Document: 
        """
        First item access
        """
    def ChangeLast(self) -> TDocStd_Document: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> TDocStd_Document: 
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
    def First(self) -> TDocStd_Document: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : TDocStd_Document) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TDocStd_SequenceOfDocument) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TDocStd_SequenceOfDocument) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : TDocStd_Document) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> TDocStd_Document: 
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
    def Prepend(self,theSeq : TDocStd_SequenceOfDocument) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : TDocStd_Document) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : TDocStd_Document) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TDocStd_SequenceOfDocument) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> TDocStd_Document: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : TDocStd_SequenceOfDocument) -> None: ...
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
class TDocStd_XLink(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    An attribute to store the path and the entry of external links. These refer from one data structure to a data structure in another document.An attribute to store the path and the entry of external links. These refer from one data structure to a data structure in another document.An attribute to store the path and the entry of external links. These refer from one data structure to a data structure in another document.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Updates the XLinkRoot attribute by adding <me> to its list.
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
        Something to do after applying <anAttDelta>.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns a null handle. Raise always for it is nonsense to use this method.
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
        Updates the XLinkRoot attribute by removing <me> from its list.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>.
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
    @overload
    def DocumentEntry(self,aDocEntry : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the name aDocEntry for the external document in this external link attribute.

        Returns the contents of the document identified by aDocEntry. aDocEntry provides external data to this external link attribute.
        """
    @overload
    def DocumentEntry(self) -> OCP.TCollection.TCollection_AsciiString: ...
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the attribute on <aStream>.
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
        Returns the GUID for external links.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
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
    @overload
    def LabelEntry(self,aLabEntry : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the label entry for this external link attribute with the label aLabel. aLabel pilots the importation of data from the document entry.

        Sets the label entry for this external link attribute as a document identified by aLabEntry.

        Returns the contents of the field <myLabelEntry>.
        """
    @overload
    def LabelEntry(self,aLabel : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def LabelEntry(self) -> OCP.TCollection.TCollection_AsciiString: ...
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns a null handle.
        """
    def Paste(self,intoAttribute : OCP.TDF.TDF_Attribute,aRelocationTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Does nothing.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,anAttribute : OCP.TDF.TDF_Attribute) -> None: 
        """
        Does nothing.
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self) -> None: ...
    @staticmethod
    def Set_s(atLabel : OCP.TDF.TDF_Label) -> TDocStd_XLink: 
        """
        Sets an empty external reference, at the label aLabel.
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
    def Update(self) -> OCP.TDF.TDF_Reference: 
        """
        Updates the data referenced in this external link attribute.
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
class TDocStd_XLinkIterator():
    """
    Iterates on Reference attributes. This is an iterator giving all the external references of a Document.
    """
    def Initialize(self,D : TDocStd_Document) -> None: 
        """
        Restarts an iteration with <D>.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Item in the iteration.

        Returns True if there is a current Item in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next item; raises if there is no more item.
        """
    def Value(self) -> TDocStd_XLink: 
        """
        Returns the current item; a null handle if there is none.

        Returns the current item; a null handle if there is none.
        """
    @overload
    def __init__(self,D : TDocStd_Document) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TDocStd_XLinkRoot(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    This attribute is the root of all external references contained in a Data from TDF. Only one instance of this class is added to the TDF_Data root label. Starting from this attribute all the Reference are linked together, to be found easily.This attribute is the root of all external references contained in a Data from TDF. Only one instance of this class is added to the TDF_Data root label. Starting from this attribute all the Reference are linked together, to be found easily.This attribute is the root of all external references contained in a Data from TDF. Only one instance of this class is added to the TDF_Data root label. Starting from this attribute all the Reference are linked together, to be found easily.
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
        Returns a null handle.
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
        Dumps the attribute on <aStream>.
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
        Returns the ID: 2a96b61d-ec8b-11d0-bee7-080009dc3333
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
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
        Returns a null handle.
        """
    def Paste(self,intoAttribute : OCP.TDF.TDF_Attribute,aRelocationTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Does nothing.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,anAttribute : OCP.TDF.TDF_Attribute) -> None: 
        """
        Does nothing.
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self) -> None: ...
    @staticmethod
    def Set_s(aDF : OCP.TDF.TDF_Data) -> TDocStd_XLinkRoot: 
        """
        Sets an empty XLinkRoot to Root or gets the existing one. Only one attribute per TDF_Data.
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
class TDocStd_XLinkTool():
    """
    This tool class is used to copy the content of source label under target label. Only child labels and attributes of source are copied. attributes located out of source scope are not copied by this algorithm. Depending of the called method an external reference is set in the target document to registered the externallink. Provide services to set, update and perform external references. Warning1: Nothing is provided in this class about the opportunity to copy, set a link or update it. Such decisions must be under application control. Warning2: If the document manages shapes, use after copy TNaming::ChangeShapes(target,M) to make copy of shapes.
    """
    def Copy(self,intarget : OCP.TDF.TDF_Label,fromsource : OCP.TDF.TDF_Label) -> None: 
        """
        Copy the content of <fromsource> under <intarget>. No link is registered. No check is done. Example Handle(TDocStd_Document) DOC, XDOC; TDF_Label L, XL; TDocStd_XLinkTool xlinktool; xlinktool.Copy(L,XL); Exceptions: Standard_DomainError if the contents of fromsource are not entirely in the scope of this label, in other words, are not self-contained. !!! ==> Warning: If the document manages shapes use the next way: TDocStd_XLinkTool xlinktool; xlinktool.Copy(L,XL); TopTools_DataMapOfShapeShape M; TNaming::ChangeShapes(target,M);
        """
    def CopyWithLink(self,intarget : OCP.TDF.TDF_Label,fromsource : OCP.TDF.TDF_Label) -> None: 
        """
        Copies the content of the label <fromsource> to the label <intarget>. The link is registered with an XLink attribute by <intarget> label. if the content of <fromsource> is not self-contained, and/or <intarget> has already an XLink attribute, an exception is raised.
        """
    def DataSet(self) -> OCP.TDF.TDF_DataSet: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def RelocationTable(self) -> OCP.TDF.TDF_RelocationTable: 
        """
        None
        """
    def UpdateLink(self,L : OCP.TDF.TDF_Label) -> None: 
        """
        Update the external reference set at <L>. Example Handle(TDocStd_Document) aDoc; if (!OCAFTest::GetDocument(1,aDoc)) return 1; Handle(TDataStd_Reference) aRef; TDocStd_XLinkTool xlinktool; if (!OCAFTest::Find(aDoc,2),TDataStd_Reference::GetID(),aRef) return 1; xlinktool.UpdateLink(aRef->Label()); Exceptions Standard_DomainError if <L> has no XLink attribute.
        """
    def __init__(self) -> None: ...
    pass
TDocStd_FormatVersion_CURRENT: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_12: 12>
TDocStd_FormatVersion_LOWER = 2
TDocStd_FormatVersion_UPPER = 12
TDocStd_FormatVersion_VERSION_10: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_10: 10>
TDocStd_FormatVersion_VERSION_11: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_11: 11>
TDocStd_FormatVersion_VERSION_12: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_12: 12>
TDocStd_FormatVersion_VERSION_2: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_2: 2>
TDocStd_FormatVersion_VERSION_3: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_3: 3>
TDocStd_FormatVersion_VERSION_4: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_4: 4>
TDocStd_FormatVersion_VERSION_5: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_5: 5>
TDocStd_FormatVersion_VERSION_6: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_6: 6>
TDocStd_FormatVersion_VERSION_7: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_7: 7>
TDocStd_FormatVersion_VERSION_8: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_8: 8>
TDocStd_FormatVersion_VERSION_9: OCP.TDocStd.TDocStd_FormatVersion # value = <TDocStd_FormatVersion.TDocStd_FormatVersion_VERSION_9: 9>
