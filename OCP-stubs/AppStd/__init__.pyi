import OCP.AppStd
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64

_Shape = Tuple[int, ...]
import OCP.TDocStd
import OCP.CDF
import OCP.TCollection
import OCP.Standard
import OCP.Message
import OCP.Resource
import OCP.PCDM
import OCP.TColStd
import OCP.CDM

__all__ = ["AppStd_Application"]

class AppStd_Application(
    OCP.TDocStd.TDocStd_Application,
    OCP.CDF.CDF_Application,
    OCP.CDM.CDM_Application,
    OCP.Standard.Standard_Transient,
):
    """
    Legacy class defining resources name for standard OCAF documentsLegacy class defining resources name for standard OCAF documentsLegacy class defining resources name for standard OCAF documents
    """

    def BeginOfUpdate(self, aDocument: OCP.CDM.CDM_Document) -> None:
        """
        this method is called before the update of a document. By default, writes in MessageDriver().
        """
    def CanClose(self, aDocument: OCP.CDM.CDM_Document) -> OCP.CDM.CDM_CanCloseStatus:
        """
        None
        """
    @overload
    def CanRetrieve(
        self,
        aFolder: OCP.TCollection.TCollection_ExtendedString,
        aName: OCP.TCollection.TCollection_ExtendedString,
        aVersion: OCP.TCollection.TCollection_ExtendedString,
    ) -> OCP.PCDM.PCDM_ReaderStatus:
        """
        None

        None
        """
    @overload
    def CanRetrieve(
        self,
        aFolder: OCP.TCollection.TCollection_ExtendedString,
        aName: OCP.TCollection.TCollection_ExtendedString,
    ) -> OCP.PCDM.PCDM_ReaderStatus: ...
    def Close(self, aDoc: OCP.TDocStd.TDocStd_Document) -> None:
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
    def DefineFormat(
        self,
        theFormat: OCP.TCollection.TCollection_AsciiString,
        theDescription: OCP.TCollection.TCollection_AsciiString,
        theExtension: OCP.TCollection.TCollection_AsciiString,
        theReader: OCP.PCDM.PCDM_RetrievalDriver,
        theWriter: OCP.PCDM.PCDM_StorageDriver,
    ) -> None:
        """
        Sets up resources and registers read and storage drivers for the specified format.
        """
    def Delete(self) -> None:
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type:
        """
        None
        """
    def EndOfUpdate(
        self,
        aDocument: OCP.CDM.CDM_Document,
        theStatus: bool,
        ErrorString: OCP.TCollection.TCollection_ExtendedString,
    ) -> None:
        """
        this method is called affter the update of a document. By default, writes in MessageDriver().
        """
    def Format(
        self,
        aFileName: OCP.TCollection.TCollection_ExtendedString,
        theFormat: OCP.TCollection.TCollection_ExtendedString,
    ) -> bool:
        """
        try to retrieve a Format directly in the file or in application resource by using extension. returns True if found;
        """
    def GetDocument(self, index: int, aDoc: OCP.TDocStd.TDocStd_Document) -> Any:
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
    def InitDocument(self, aDoc: OCP.TDocStd.TDocStd_Document) -> None:
        """
        Initialize the document aDoc for the applicative session. This virtual function is called by NewDocument and is to be redefined for each specific application. Modified flag (different of disk version) ============= to open/save a document =======================
        """
    def IsDriverLoaded(self) -> bool:
        """
        Check if meta data driver was successfully loaded by the application constructor
        """
    def IsInSession(self, path: OCP.TCollection.TCollection_ExtendedString) -> int:
        """
        Returns an index for the document found in the path path in this applicative session. If the returned value is 0, the document is not present in the applicative session. This method can be used for the interactive part of an application. For instance, on a call to Open, the document to be opened may already be in memory. IsInSession checks to see if this is the case. Open can be made to depend on the value of the index returned: if IsInSession returns 0, the document is opened; if it returns another value, a message is displayed asking the user if he wants to override the version of the document in memory. Example: Standard_Integer insession = A->IsInSession(aDoc); if (insession > 0) { std::cout << "document " << insession << " is already in session" << std::endl; return 0; }
        """
    @overload
    def IsInstance(self, theTypeName: str) -> bool:
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self, theType: OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self, theType: OCP.Standard.Standard_Type) -> bool:
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self, theTypeName: str) -> bool: ...
    @staticmethod
    def Load_s(aGUID: OCP.Standard.Standard_GUID) -> OCP.CDF.CDF_Application:
        """
        plugs an application.
        """
    def MessageDriver(self) -> OCP.Message.Message_Messenger:
        """
        Redefines message driver, by default outputs to std::cout.
        """
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString:
        """
        Returns the application name.
        """
    def NbDocuments(self) -> int:
        """
        returns the number of documents handled by the current applicative session.
        """
    def NewDocument(
        self,
        format: OCP.TCollection.TCollection_ExtendedString,
        aDoc: OCP.TDocStd.TDocStd_Document,
    ) -> Any:
        """
        Constructs the empty new document aDoc. This document will have the format format. If InitDocument is redefined for a specific application, the new document is handled by the applicative session.
        """
    def OnAbortTransaction(self, theDoc: OCP.TDocStd.TDocStd_Document) -> None:
        """
        Notification that is fired at each AbortTransaction event.
        """
    def OnCommitTransaction(self, theDoc: OCP.TDocStd.TDocStd_Document) -> None:
        """
        Notification that is fired at each CommitTransaction event.
        """
    def OnOpenTransaction(self, theDoc: OCP.TDocStd.TDocStd_Document) -> None:
        """
        Notification that is fired at each OpenTransaction event.
        """
    @overload
    def Open(
        self, theIStream: Any, theDoc: OCP.TDocStd.TDocStd_Document
    ) -> OCP.PCDM.PCDM_ReaderStatus:
        """
        Retrieves the document aDoc stored under the name aName in the directory directory. In order not to override a version of aDoc which is already in memory, this method can be made to depend on the value returned by IsInSession.

        Retrieves aDoc from standard SEEKABLE stream theIStream. the stream should support SEEK fuctionality
        """
    @overload
    def Open(
        self,
        path: OCP.TCollection.TCollection_ExtendedString,
        aDoc: OCP.TDocStd.TDocStd_Document,
    ) -> OCP.PCDM.PCDM_ReaderStatus: ...
    def Read(self, theIStream: Any) -> OCP.CDM.CDM_Document:
        """
        Reads aDoc from standard SEEKABLE stream theIStream, the stream should support SEEK fuctionality
        """
    def ReaderFromFormat(
        self, aFormat: OCP.TCollection.TCollection_ExtendedString
    ) -> OCP.PCDM.PCDM_Reader:
        """
        Returns instance of read driver for specified format.
        """
    def ReadingFormats(
        self, theFormats: OCP.TColStd.TColStd_SequenceOfAsciiString
    ) -> None:
        """
        Returns the sequence of reading formats supported by the application.
        """
    def Resources(self) -> OCP.Resource.Resource_Manager:
        """
        Returns resource manager defining supported persistent formats.
        """
    def ResourcesName(self) -> str:
        """
        returns the file name which contains application resources
        """
    @overload
    def Retrieve(
        self,
        aFolder: OCP.TCollection.TCollection_ExtendedString,
        aName: OCP.TCollection.TCollection_ExtendedString,
        aVersion: OCP.TCollection.TCollection_ExtendedString,
        UseStorageConfiguration: bool = True,
    ) -> OCP.CDM.CDM_Document:
        """
        This method retrieves a document from the database. If the Document references other documents which have been updated, the latest version of these documents will be used if {UseStorageConfiguration} is Standard_True. The content of {aFolder}, {aName} and {aVersion} depends on the Database Manager system. If the DBMS is only based on the OS, {aFolder} is a directory and {aName} is the name of a file. In this case the use of the syntax with {aVersion} has no sense. For example:

        This method retrieves a document from the database. If the Document references other documents which have been updated, the latest version of these documents will be used if {UseStorageConfiguration} is Standard_True. -- If the DBMS is only based on the OS, this syntax should not be used.
        """
    @overload
    def Retrieve(
        self,
        aFolder: OCP.TCollection.TCollection_ExtendedString,
        aName: OCP.TCollection.TCollection_ExtendedString,
        UseStorageConfiguration: bool = True,
    ) -> OCP.CDM.CDM_Document: ...
    @overload
    def Save(self, aDoc: OCP.TDocStd.TDocStd_Document) -> OCP.PCDM.PCDM_StoreStatus:
        """
        Save aDoc active document. Exceptions: Standard_NotImplemented if the document was not retrieved in the applicative session by using Open.

        Save the document overwriting the previous file
        """
    @overload
    def Save(
        self,
        aDoc: OCP.TDocStd.TDocStd_Document,
        theStatusMessage: OCP.TCollection.TCollection_ExtendedString,
    ) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveAs(
        self,
        aDoc: OCP.TDocStd.TDocStd_Document,
        path: OCP.TCollection.TCollection_ExtendedString,
    ) -> OCP.PCDM.PCDM_StoreStatus:
        """
        Save the active document in the file <name> in the path <path> ; o verwrites the file if it already exists.

        Save theDoc to standard SEEKABLE stream theOStream. the stream should support SEEK fuctionality

        Save the active document in the file <name> in the path <path> . overwrite the file if it already exist.

        Save theDoc TO standard SEEKABLE stream theOStream. the stream should support SEEK fuctionality
        """
    @overload
    def SaveAs(
        self,
        theDoc: OCP.TDocStd.TDocStd_Document,
        theOStream: Any,
        theStatusMessage: OCP.TCollection.TCollection_ExtendedString,
    ) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveAs(
        self, theDoc: OCP.TDocStd.TDocStd_Document, theOStream: Any
    ) -> OCP.PCDM.PCDM_StoreStatus: ...
    @overload
    def SaveAs(
        self,
        aDoc: OCP.TDocStd.TDocStd_Document,
        path: OCP.TCollection.TCollection_ExtendedString,
        theStatusMessage: OCP.TCollection.TCollection_ExtendedString,
    ) -> OCP.PCDM.PCDM_StoreStatus: ...
    def SetDefaultFolder(self, aFolder: str) -> bool:
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
    def Write(self, aString: str) -> None:
        """
        writes the string in the application MessagerDriver.
        """
    def WriterFromFormat(
        self, aFormat: OCP.TCollection.TCollection_ExtendedString
    ) -> OCP.PCDM.PCDM_StorageDriver:
        """
        Returns instance of storage driver for specified format.
        """
    def WritingFormats(
        self, theFormats: OCP.TColStd.TColStd_SequenceOfAsciiString
    ) -> None:
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
