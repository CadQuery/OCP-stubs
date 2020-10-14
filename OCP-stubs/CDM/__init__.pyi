import OCP.CDM
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Resource
import OCP.TCollection
import OCP.TColStd
import OCP.Message
import OCP.Standard
import OCP.NCollection
__all__  = [
"CDM_Application",
"CDM_CanCloseStatus",
"CDM_Document",
"CDM_DocumentHasher",
"CDM_ListOfDocument",
"CDM_ListOfReferences",
"CDM_MapOfDocument",
"CDM_MetaData",
"CDM_Reference",
"CDM_ReferenceIterator",
"CDM_CCS_ModifiedReferenced",
"CDM_CCS_NotOpen",
"CDM_CCS_OK",
"CDM_CCS_ReferenceRejection",
"CDM_CCS_UnstoredReferenced"
]
class CDM_Application(OCP.Standard.Standard_Transient):
    def BeginOfUpdate(self,aDocument : CDM_Document) -> None: 
        """
        this method is called before the update of a document. By default, writes in MessageDriver().
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
    def EndOfUpdate(self,aDocument : CDM_Document,theStatus : bool,ErrorString : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        this method is called affter the update of a document. By default, writes in MessageDriver().
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
    def MessageDriver(self) -> OCP.Message.Message_Messenger: 
        """
        Returns default messenger;
        """
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the application name.
        """
    def Resources(self) -> OCP.Resource.Resource_Manager: 
        """
        The manager returned by this virtual method will be used to search for Format.Retrieval resource items.
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
class CDM_CanCloseStatus():
    """
    None

    Members:

      CDM_CCS_OK

      CDM_CCS_NotOpen

      CDM_CCS_UnstoredReferenced

      CDM_CCS_ModifiedReferenced

      CDM_CCS_ReferenceRejection
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
    CDM_CCS_ModifiedReferenced: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_ModifiedReferenced
    CDM_CCS_NotOpen: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_NotOpen
    CDM_CCS_OK: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_OK
    CDM_CCS_ReferenceRejection: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_ReferenceRejection
    CDM_CCS_UnstoredReferenced: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_UnstoredReferenced
    __entries: dict # value = {'CDM_CCS_OK': (CDM_CanCloseStatus.CDM_CCS_OK, None), 'CDM_CCS_NotOpen': (CDM_CanCloseStatus.CDM_CCS_NotOpen, None), 'CDM_CCS_UnstoredReferenced': (CDM_CanCloseStatus.CDM_CCS_UnstoredReferenced, None), 'CDM_CCS_ModifiedReferenced': (CDM_CanCloseStatus.CDM_CCS_ModifiedReferenced, None), 'CDM_CCS_ReferenceRejection': (CDM_CanCloseStatus.CDM_CCS_ReferenceRejection, None)}
    __members__: dict # value = {'CDM_CCS_OK': CDM_CanCloseStatus.CDM_CCS_OK, 'CDM_CCS_NotOpen': CDM_CanCloseStatus.CDM_CCS_NotOpen, 'CDM_CCS_UnstoredReferenced': CDM_CanCloseStatus.CDM_CCS_UnstoredReferenced, 'CDM_CCS_ModifiedReferenced': CDM_CanCloseStatus.CDM_CCS_ModifiedReferenced, 'CDM_CCS_ReferenceRejection': CDM_CanCloseStatus.CDM_CCS_ReferenceRejection}
    pass
class CDM_Document(OCP.Standard.Standard_Transient):
    """
    An applicative document is an instance of a class inheriting CDM_Document. These documents have the following properties: - they can have references to other documents. - the modifications of a document are propagated to the referencing documents. - a document can be stored in different formats, with or without a persistent model. - the drivers for storing and retrieving documents are plugged in when necessary. - a document has a modification counter. This counter is incremented when the document is modified. When a document is stored, the current counter value is memorized as the last storage version of the document. A document is considered to be modified when the counter value is different from the storage version. Once the document is saved the storage version and the counter value are identical. The document is now not considered to be modified. - a reference is a link between two documents. A reference has two components: the "From Document" and the "To Document". When a reference is created, an identifier of the reference is generated. This identifier is unique in the scope of the From Document and is conserved during storage and retrieval. This means that the referenced document will be always accessible through this identifier. - a reference memorizes the counter value of the To Document when the reference is created. The From Document is considered to be up to date relative to the To Document when the reference counter value is equal to the To Document counter value. - retrieval of a document having references does not imply the retrieving of the referenced documents.An applicative document is an instance of a class inheriting CDM_Document. These documents have the following properties: - they can have references to other documents. - the modifications of a document are propagated to the referencing documents. - a document can be stored in different formats, with or without a persistent model. - the drivers for storing and retrieving documents are plugged in when necessary. - a document has a modification counter. This counter is incremented when the document is modified. When a document is stored, the current counter value is memorized as the last storage version of the document. A document is considered to be modified when the counter value is different from the storage version. Once the document is saved the storage version and the counter value are identical. The document is now not considered to be modified. - a reference is a link between two documents. A reference has two components: the "From Document" and the "To Document". When a reference is created, an identifier of the reference is generated. This identifier is unique in the scope of the From Document and is conserved during storage and retrieval. This means that the referenced document will be always accessible through this identifier. - a reference memorizes the counter value of the To Document when the reference is created. The From Document is considered to be up to date relative to the To Document when the reference counter value is equal to the To Document counter value. - retrieval of a document having references does not imply the retrieving of the referenced documents.An applicative document is an instance of a class inheriting CDM_Document. These documents have the following properties: - they can have references to other documents. - the modifications of a document are propagated to the referencing documents. - a document can be stored in different formats, with or without a persistent model. - the drivers for storing and retrieving documents are plugged in when necessary. - a document has a modification counter. This counter is incremented when the document is modified. When a document is stored, the current counter value is memorized as the last storage version of the document. A document is considered to be modified when the counter value is different from the storage version. Once the document is saved the storage version and the counter value are identical. The document is now not considered to be modified. - a reference is a link between two documents. A reference has two components: the "From Document" and the "To Document". When a reference is created, an identifier of the reference is generated. This identifier is unique in the scope of the From Document and is conserved during storage and retrieval. This means that the referenced document will be always accessible through this identifier. - a reference memorizes the counter value of the To Document when the reference is created. The From Document is considered to be up to date relative to the To Document when the reference counter value is equal to the To Document counter value. - retrieval of a document having references does not imply the retrieving of the referenced documents.
    """
    def AddComment(self,aComment : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        appends a comment into comments of this document.
        """
    def Application(self) -> CDM_Application: 
        """
        None
        """
    def CanClose(self) -> CDM_CanCloseStatus: 
        """
        None
        """
    def CanCloseReference(self,aDocument : CDM_Document,aReferenceIdentifier : int) -> bool: 
        """
        A referenced document may indicate through this virtual method that it does not allow the closing of aDocument which it references through the reference aReferenceIdentifier. By default returns Standard_True;;
        """
    def ChangeStorageFormatVersion(self,theVersion : int) -> None: 
        """
        Sets <theVersion> of the format to be used to store the document
        """
    def Close(self) -> None: 
        """
        None
        """
    def CloseReference(self,aDocument : CDM_Document,aReferenceIdentifier : int) -> None: 
        """
        A referenced document may update its internal data structure when {aDocument} which it references through the reference {aReferenceIdentifier} is being closed. By default this method does nothing.
        """
    def Comment(self) -> str: 
        """
        returns the first of associated comments. By defaut the comment is an empty string.
        """
    def Comments(self,aComments : OCP.TColStd.TColStd_SequenceOfExtendedString) -> None: 
        """
        returns the associated comments through <aComments>. Returns empty sequence if no comments are associated.
        """
    def CopyReference(self,aFromDocument : CDM_Document,aReferenceIdentifier : int) -> int: 
        """
        Copies a reference to this document. This method avoid retrieval of referenced document. The arguments are the original document and a valid reference identifier Returns the local identifier.
        """
    @overload
    def CreateReference(self,aMetaData : CDM_MetaData,anApplication : CDM_Application,aDocumentVersion : int,UseStorageConfiguration : bool) -> int: 
        """
        Creates a reference from this document to {anOtherDocument}. Returns a reference identifier. This reference identifier is unique in the document and will not be used for the next references, even after the storing of the document. If there is already a reference between the two documents, the reference is not created, but its reference identifier is returned.

        None

        None
        """
    @overload
    def CreateReference(self,anOtherDocument : CDM_Document) -> int: ...
    @overload
    def CreateReference(self,aMetaData : CDM_MetaData,aReferenceIdentifier : int,anApplication : CDM_Application,aToDocumentVersion : int,UseStorageConfiguration : bool) -> None: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DeepReferences(self,aDocument : CDM_Document) -> bool: 
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
    def Document(self,aReferenceIdentifier : int) -> CDM_Document: 
        """
        Returns the To Document of the reference identified by aReferenceIdentifier. If the ToDocument is stored and has not yet been retrieved, this method will retrieve it.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
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
    @staticmethod
    def FindFromPresentation_s(aPresentation : OCP.TCollection.TCollection_ExtendedString) -> CDM_Document: 
        """
        returns the document having the given alphanumeric presentation.
        """
    @staticmethod
    def FindPresentation_s(aPresentation : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        indicates whether a document having the given presentation does exist.
        """
    def Folder(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def FromReferencesNumber(self) -> int: 
        """
        returns the number of references having this document as To Document.
        """
    def GetAlternativeDocument(self,aFormat : OCP.TCollection.TCollection_ExtendedString,anAlternativeDocument : CDM_Document) -> bool: 
        """
        This method can be redefined to extract another document in a different format. For example, to extract a Shape from an applicative document.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
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
    def IsInSession(self,aReferenceIdentifier : int) -> bool: 
        """
        returns True if the To Document of the reference identified by aReferenceIdentifier is in session, False if it corresponds to a not yet retrieved document.
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
        returns true if the version is greater than the storage version
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
    def IsReadOnly(self) -> bool: 
        """
        indicates that this document cannot be modified.

        indicates that the referenced document cannot be modified,
        """
    @overload
    def IsReadOnly(self,aReferenceIdentifier : int) -> bool: ...
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
    def LoadResources(self) -> None: ...
    def MetaData(self) -> CDM_MetaData: 
        """
        None
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
    def Open(self,anApplication : CDM_Application) -> None: 
        """
        None
        """
    def Presentation(self) -> str: 
        """
        Returns an alphanumeric string identifying this document in a unique manner in the current process. The presentation may change when the document is stored. Tries to get the 'FileFormat`.Presentation resource This item is used to give a default presentation to the document.
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def Reference(self,aReferenceIdentifier : int) -> CDM_Reference: 
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
        determines under which the document is going to be store. By default the name of the document wil be -- used. If the document has no name its presentation will be used.
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
    def SetIsReadOnly(self) -> None: 
        """
        None
        """
    def SetIsUpToDate(self,aReferenceIdentifier : int) -> None: 
        """
        Resets the modification counter in the given reference to the actual modification counter of its To Document. This method should be called after the application has updated this document.
        """
    def SetMetaData(self,aMetaData : CDM_MetaData) -> None: 
        """
        associates database information to a document which has been stored. The name of the document is now the name which has beenused to store the data.
        """
    def SetModifications(self,Modifications : int) -> None: 
        """
        None
        """
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
    def ShallowReferences(self,aDocument : CDM_Document) -> bool: 
        """
        returns True is this document references aDocument;
        """
    def StorageFormat(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        The Storage Format is the key which is used to determine in the application resources the storage driver plugin, the file extension and other data used to store the document.
        """
    def StorageFormatVersion(self) -> int: 
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
    @overload
    def Update(self,aToDocument : CDM_Document,aReferenceIdentifier : int,aModifContext : capsule) -> None: 
        """
        The Update method will be called once for each reference, but it should not perform any computation, to avoid multiple computation of a same document.

        This method Update will be called to signal the end of the modified references list. The document should be recomputed and UpdateFromDocuments should be called. Update should returns True in case of success, false otherwise. In case of Failure, additional information can be given in ErrorString.

        the following method should be used instead:
        """
    @overload
    def Update(self,ErrorString : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    @overload
    def Update(self) -> None: ...
    def UpdateFromDocuments(self,aModifContext : capsule) -> None: 
        """
        call virtual method Update on all referencing documents. This method keeps the list of the -- documents to process.It may be the starting of an update -- cycle. If not, the reentrant calls made by Update method (without argument) will append the referencing documents to the list and call the Update method (with arguments). Only the first call to UpdateFromDocuments generate call to Update().
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
class CDM_DocumentHasher():
    """
    Purpose: The DefaultHasher is a Hasher that is used by default in NCollection maps. To compute the hash code of the key is used the global function HashCode. To compare two keys is used the global function IsEqual.
    """
    @staticmethod
    def HashCode_s(theKey : CDM_Document,theUpperBound : int) -> int: 
        """
        Returns hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theKey1 : CDM_Document,theKey2 : CDM_Document) -> bool: 
        """
        None
        """
    pass
class CDM_ListOfDocument(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : CDM_Document) -> CDM_Document: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : CDM_ListOfDocument) -> None: ...
    @overload
    def Append(self,theItem : CDM_Document,theIter : Any) -> None: ...
    def Assign(self,theOther : CDM_ListOfDocument) -> CDM_ListOfDocument: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> CDM_Document: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : CDM_Document,theIter : Any) -> CDM_Document: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : CDM_ListOfDocument,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : CDM_ListOfDocument,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : CDM_Document,theIter : Any) -> CDM_Document: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> CDM_Document: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : CDM_Document) -> CDM_Document: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : CDM_ListOfDocument) -> None: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : CDM_ListOfDocument) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class CDM_ListOfReferences(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : CDM_ListOfReferences) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : CDM_Reference,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : CDM_Reference) -> CDM_Reference: ...
    def Assign(self,theOther : CDM_ListOfReferences) -> CDM_ListOfReferences: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> CDM_Reference: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : CDM_ListOfReferences,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : CDM_Reference,theIter : Any) -> CDM_Reference: ...
    @overload
    def InsertBefore(self,theItem : CDM_Reference,theIter : Any) -> CDM_Reference: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : CDM_ListOfReferences,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> CDM_Reference: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : CDM_Reference) -> CDM_Reference: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : CDM_ListOfReferences) -> None: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : CDM_ListOfReferences) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class CDM_MapOfDocument(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : CDM_Document) -> bool: 
        """
        Add
        """
    def Added(self,K : CDM_Document) -> CDM_Document: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : CDM_MapOfDocument) -> CDM_MapOfDocument: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,K : CDM_Document) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : CDM_MapOfDocument) -> bool: ...
    def Differ(self,theOther : CDM_MapOfDocument) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : CDM_MapOfDocument,theRight : CDM_MapOfDocument) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : CDM_MapOfDocument) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : CDM_MapOfDocument) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : CDM_MapOfDocument) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : CDM_MapOfDocument,theRight : CDM_MapOfDocument) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : CDM_MapOfDocument) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : CDM_Document) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : CDM_MapOfDocument) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : CDM_MapOfDocument,theRight : CDM_MapOfDocument) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : CDM_MapOfDocument,theRight : CDM_MapOfDocument) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : CDM_MapOfDocument) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : CDM_MapOfDocument) -> None: ...
    pass
class CDM_MetaData(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Document(self) -> CDM_Document: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FileName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def Folder(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        returns the folder in which the meta-data has to be created or has to be found.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasVersion(self) -> bool: 
        """
        indicates that the version has to be taken into account when searching the corresponding meta-data.
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
    def IsReadOnly(self) -> bool: 
        """
        None
        """
    def IsRetrieved(self) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def LookUp_s(aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aPath : OCP.TCollection.TCollection_ExtendedString,aFileName : OCP.TCollection.TCollection_ExtendedString,ReadOnly : bool) -> CDM_MetaData: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def LookUp_s(aFolder : OCP.TCollection.TCollection_ExtendedString,aName : OCP.TCollection.TCollection_ExtendedString,aPath : OCP.TCollection.TCollection_ExtendedString,aVersion : OCP.TCollection.TCollection_ExtendedString,aFileName : OCP.TCollection.TCollection_ExtendedString,ReadOnly : bool) -> CDM_MetaData: ...
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        returns the name under which the meta-data has to be created or has to be found.
        """
    def Path(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetIsReadOnly(self) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnsetDocument(self) -> None: 
        """
        None
        """
    def UnsetIsReadOnly(self) -> None: 
        """
        None
        """
    def Version(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        returns the version under which the meta-data has to be found. Warning: raises NoSuchObject from Standard if no Version has been defined
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
class CDM_Reference(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DocumentVersion(self) -> int: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FromDocument(self) -> CDM_Document: 
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
    def IsReadOnly(self) -> bool: 
        """
        None
        """
    def ReferenceIdentifier(self) -> int: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToDocument(self) -> CDM_Document: 
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
class CDM_ReferenceIterator():
    """
    None
    """
    def Document(self) -> CDM_Document: 
        """
        None
        """
    def DocumentVersion(self) -> int: 
        """
        returns the Document Version in the reference.
        """
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def ReferenceIdentifier(self) -> int: 
        """
        None
        """
    def __init__(self,aDocument : CDM_Document) -> None: ...
    pass
CDM_CCS_ModifiedReferenced: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_ModifiedReferenced
CDM_CCS_NotOpen: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_NotOpen
CDM_CCS_OK: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_OK
CDM_CCS_ReferenceRejection: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_ReferenceRejection
CDM_CCS_UnstoredReferenced: OCP.CDM.CDM_CanCloseStatus # value = CDM_CanCloseStatus.CDM_CCS_UnstoredReferenced
