import OCP.TDF
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import io
import OCP.Standard
import OCP.TCollection
import OCP.TColStd
__all__  = [
"TDF",
"TDF_Attribute",
"TDF_AttributeArray1",
"TDF_AttributeDelta",
"TDF_AttributeDeltaList",
"TDF_AttributeIndexedMap",
"TDF_AttributeIterator",
"TDF_AttributeList",
"TDF_AttributeMap",
"TDF_AttributeSequence",
"TDF_ChildIDIterator",
"TDF_ChildIterator",
"TDF_ClosureMode",
"TDF_ClosureTool",
"TDF_ComparisonTool",
"TDF_CopyLabel",
"TDF_CopyTool",
"TDF_Data",
"TDF_DataSet",
"TDF_DeltaOnModification",
"TDF_DeltaOnRemoval",
"TDF_Delta",
"TDF_DeltaList",
"TDF_DeltaOnAddition",
"TDF_DeltaOnForget",
"TDF_DefaultDeltaOnModification",
"TDF_DefaultDeltaOnRemoval",
"TDF_DeltaOnResume",
"TDF_DerivedAttribute",
"TDF_GUIDProgIDMap",
"TDF_HAttributeArray1",
"TDF_IDFilter",
"TDF_IDList",
"TDF_IDMap",
"TDF_Label",
"TDF_LabelDataMap",
"TDF_LabelDoubleMap",
"TDF_LabelIndexedMap",
"TDF_LabelIntegerMap",
"TDF_LabelList",
"TDF_LabelMap",
"TDF_LabelMapHasher",
"TDF_LabelSequence",
"TDF_Reference",
"TDF_RelocationTable",
"TDF_TagSource",
"TDF_Tool",
"TDF_Transaction",
"TDF_AttributeBackupMsk",
"TDF_AttributeForgottenMsk",
"TDF_AttributeValidMsk",
"TDF_LabelNodeAttModMsk",
"TDF_LabelNodeFlagsMsk",
"TDF_LabelNodeImportMsk",
"TDF_LabelNodeMayModMsk"
]
class TDF():
    """
    This package provides data framework for binding features and data structures.
    """
    @staticmethod
    def AddLinkGUIDToProgID_s(ID : OCP.Standard.Standard_GUID,ProgID : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Sets link between GUID and ProgID in hidden DataMap
        """
    @staticmethod
    def GUIDFromProgID_s(ProgID : OCP.TCollection.TCollection_ExtendedString,ID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns True if there is GUID for given <ProgID> then GUID is returned in <ID>
        """
    @staticmethod
    def LowestID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns ID "00000000-0000-0000-0000-000000000000", sometimes used as null ID.
        """
    @staticmethod
    def ProgIDFromGUID_s(ID : OCP.Standard.Standard_GUID,ProgID : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Returns True if there is ProgID for given <ID> then ProgID is returned in <ProgID>
        """
    @staticmethod
    def UppestID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns ID "ffffffff-ffff-ffff-ffff-ffffffffffff".
        """
    def __init__(self) -> None: ...
    pass
class TDF_Attribute(OCP.Standard.Standard_Transient):
    """
    A class each application has to implement. It is used to contain the application data. This abstract class, alongwith Label, is one of the cornerstones of Model Editor. The groundwork is to define the root of information. This information is to be attached to a Label, and could be of any of the following types: - a feature - a constraint - a commentA class each application has to implement. It is used to contain the application data. This abstract class, alongwith Label, is one of the cornerstones of Model Editor. The groundwork is to define the root of information. This information is to be attached to a Label, and could be of any of the following types: - a feature - a constraint - a commentA class each application has to implement. It is used to contain the application data. This abstract class, alongwith Label, is one of the cornerstones of Model Editor. The groundwork is to define the root of information. This information is to be attached to a Label, and could be of any of the following types: - a feature - a constraint - a comment
    """
    def AddAttribute(self,other : TDF_Attribute) -> None: 
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
    def AfterUndo(self,anAttDelta : TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> TDF_Attribute: 
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
    def BeforeUndo(self,anAttDelta : TDF_AttributeDelta,forceIt : bool=False) -> bool: 
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
    def DeltaOnAddition(self) -> TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : TDF_Attribute) -> TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> TDF_DeltaOnResume: 
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
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : TDF_IDFilter,aMap : TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : TDF_Attribute) -> bool: 
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> TDF_Attribute: 
        """
        Returns an new empty attribute from the good end type. It is used by the copy algorithm.
        """
    def Paste(self,intoAttribute : TDF_Attribute,aRelocationTable : TDF_RelocationTable) -> None: 
        """
        This method is different from the "Copy" one, because it is used when copying an attribute from a source structure into a target structure. This method may paste the contents of <me> into <intoAttribute>.
        """
    def References(self,aDataSet : TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,anAttribute : TDF_Attribute) -> None: 
        """
        Restores the backuped contents from <anAttribute> into this one. It is used when aborting a transaction.
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
class TDF_AttributeArray1():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TDF_AttributeArray1) -> TDF_AttributeArray1: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> TDF_Attribute: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TDF_Attribute: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TDF_Attribute: 
        """
        Variable value access
        """
    def First(self) -> TDF_Attribute: 
        """
        Returns first element
        """
    def Init(self,theValue : TDF_Attribute) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> TDF_Attribute: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : TDF_AttributeArray1) -> TDF_AttributeArray1: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TDF_Attribute) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> TDF_Attribute: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : TDF_Attribute,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TDF_AttributeArray1) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDF_AttributeDelta(OCP.Standard.Standard_Transient):
    """
    This class describes the services we need to implement Delta and Undo/Redo services.This class describes the services we need to implement Delta and Undo/Redo services.This class describes the services we need to implement Delta and Undo/Redo services.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label concerned by <me>.
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
class TDF_AttributeDeltaList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TDF_AttributeDelta,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TDF_AttributeDeltaList) -> None: ...
    @overload
    def Append(self,theItem : TDF_AttributeDelta) -> TDF_AttributeDelta: ...
    def Assign(self,theOther : TDF_AttributeDeltaList) -> TDF_AttributeDeltaList: 
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
    def First(self) -> TDF_AttributeDelta: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : TDF_AttributeDelta,theIter : Any) -> TDF_AttributeDelta: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TDF_AttributeDeltaList,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : TDF_AttributeDeltaList,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : TDF_AttributeDelta,theIter : Any) -> TDF_AttributeDelta: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TDF_AttributeDelta: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : TDF_AttributeDelta) -> TDF_AttributeDelta: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TDF_AttributeDeltaList) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_AttributeDeltaList) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDF_AttributeIndexedMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : TDF_Attribute) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDF_AttributeIndexedMap) -> TDF_AttributeIndexedMap: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : TDF_Attribute) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TDF_AttributeIndexedMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : TDF_Attribute) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> TDF_Attribute: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,theExtent : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : TDF_Attribute) -> bool: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : TDF_Attribute) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theOther : TDF_AttributeIndexedMap) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TDF_AttributeIterator():
    """
    None
    """
    def Initialize(self,aLabel : TDF_Label,withoutForgotten : bool=True) -> None: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None

        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def PtrValue(self) -> TDF_Attribute: 
        """
        Provides an access to the internal pointer of the current attribute. The method has better performance as not-creating handle.
        """
    def Value(self) -> TDF_Attribute: 
        """
        None

        None
        """
    @overload
    def __init__(self,aLabelNode : TDF_LabelNode,withoutForgotten : bool=True) -> None: ...
    @overload
    def __init__(self,aLabel : TDF_Label,withoutForgotten : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TDF_AttributeList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : TDF_AttributeList) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : TDF_Attribute) -> TDF_Attribute: ...
    @overload
    def Append(self,theItem : TDF_Attribute,theIter : Any) -> None: ...
    def Assign(self,theOther : TDF_AttributeList) -> TDF_AttributeList: 
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
    def First(self) -> TDF_Attribute: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TDF_AttributeList,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : TDF_Attribute,theIter : Any) -> TDF_Attribute: ...
    @overload
    def InsertBefore(self,theOther : TDF_AttributeList,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : TDF_Attribute,theIter : Any) -> TDF_Attribute: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TDF_Attribute: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : TDF_Attribute) -> TDF_Attribute: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TDF_AttributeList) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TDF_AttributeList) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDF_AttributeMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : TDF_Attribute) -> bool: 
        """
        Add
        """
    def Added(self,K : TDF_Attribute) -> TDF_Attribute: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDF_AttributeMap) -> TDF_AttributeMap: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def Contains(self,theOther : TDF_AttributeMap) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : TDF_Attribute) -> bool: ...
    def Differ(self,theOther : TDF_AttributeMap) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TDF_AttributeMap,theRight : TDF_AttributeMap) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TDF_AttributeMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TDF_AttributeMap) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TDF_AttributeMap) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TDF_AttributeMap,theRight : TDF_AttributeMap) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TDF_AttributeMap) -> bool: 
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
    def Remove(self,K : TDF_Attribute) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TDF_AttributeMap) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TDF_AttributeMap,theRight : TDF_AttributeMap) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TDF_AttributeMap,theRight : TDF_AttributeMap) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TDF_AttributeMap) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_AttributeMap) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class TDF_AttributeSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TDF_AttributeSequence) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : TDF_Attribute) -> None: ...
    def Assign(self,theOther : TDF_AttributeSequence) -> TDF_AttributeSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> TDF_Attribute: 
        """
        First item access
        """
    def ChangeLast(self) -> TDF_Attribute: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> TDF_Attribute: 
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
    def First(self) -> TDF_Attribute: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TDF_AttributeSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : TDF_Attribute) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : TDF_Attribute) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TDF_AttributeSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> TDF_Attribute: 
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
    def Prepend(self,theItem : TDF_Attribute) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : TDF_AttributeSequence) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : TDF_Attribute) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TDF_AttributeSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> TDF_Attribute: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_AttributeSequence) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TDF_ChildIDIterator():
    """
    Iterates on the children of a label, to find attributes having ID as Attribute ID.
    """
    def Initialize(self,aLabel : TDF_Label,anID : OCP.Standard.Standard_GUID,allLevels : bool=False) -> None: 
        """
        Initializes the iteration on the children of the given label. If <allLevels> option is set to true, it explores not only the first, but all the sub label levels.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Item in the iteration.

        Returns True if there is a current Item in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Item
        """
    def NextBrother(self) -> None: 
        """
        Move to the next Brother. If there is none, go up etc. This method is interesting only with "allLevels" behavior, because it avoids to explore the current label children.
        """
    def Value(self) -> TDF_Attribute: 
        """
        Returns the current item; a null handle if there is none.

        Returns the current item; a null handle if there is none.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aLabel : TDF_Label,anID : OCP.Standard.Standard_GUID,allLevels : bool=False) -> None: ...
    pass
class TDF_ChildIterator():
    """
    Iterates on the children of a label, at the first level only. It is possible to ask the iterator to explore all the sub label levels of the given one, with the option "allLevels".
    """
    def Initialize(self,aLabel : TDF_Label,allLevels : bool=False) -> None: 
        """
        Initializes the iteration on the children of the given label. If <allLevels> option is set to true, it explores not only the first, but all the sub label levels. If allLevels is false, only the first level of child labels is explored. In the example below, the label is iterated using Initialize, More and Next and its child labels dumped using TDF_Tool::Entry. Example void DumpChildren(const TDF_Label& aLabel) { TDF_ChildIterator it; TCollection_AsciiString es; for (it.Initialize(aLabel,Standard_True); it.More(); it.Next()){ TDF_Tool::Entry(it.Value(),es); std::cout << as.ToCString() << std::endl; } }
        """
    def More(self) -> bool: 
        """
        Returns true if a current label is found in the iteration process.

        Returns true if a current label is found in the iteration process.
        """
    def Next(self) -> None: 
        """
        Move the current iteration to the next Item.
        """
    def NextBrother(self) -> None: 
        """
        Moves this iteration to the next brother label. A brother label is one with the same father as an initial label. Use this function when the non-empty constructor or Initialize has allLevels set to true. The result is that the iteration does not explore the children of the current label. This method is interesting only with "allLevels" behavior, because it avoids to explore the current label children.
        """
    def Value(self) -> TDF_Label: 
        """
        Returns the current label; or, if there is none, a null label.

        Returns the current label; or, if there is none, a null label.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aLabel : TDF_Label,allLevels : bool=False) -> None: ...
    pass
class TDF_ClosureMode():
    """
    This class provides options closure management.
    """
    @overload
    def Descendants(self) -> bool: 
        """
        Sets the mode "Descendants" to <aStatus>.

        Returns true if the mode "Descendants" is set.

        Sets the mode "Descendants" to <aStatus>.

        Returns true if the mode "Descendants" is set.
        """
    @overload
    def Descendants(self,aStatus : bool) -> None: ...
    @overload
    def References(self,aStatus : bool) -> None: 
        """
        Sets the mode "References" to <aStatus>.

        Returns true if the mode "References" is set.

        Sets the mode "References" to <aStatus>.

        Returns true if the mode "References" is set.
        """
    @overload
    def References(self) -> bool: ...
    def __init__(self,aMode : bool=True) -> None: ...
    pass
class TDF_ClosureTool():
    """
    This class provides services to build the closure of an information set. This class gives services around the transitive enclosure of a set of information, starting from a list of label. You can set closure options by using IDFilter (to select or exclude specific attribute IDs) and CopyOption objects and by giving to Closure method.
    """
    @staticmethod
    @overload
    def Closure_s(aDataSet : TDF_DataSet) -> None: 
        """
        Builds the transitive closure of label and attribute sets into <aDataSet>.

        Builds the transitive closure of label and attribute sets into <aDataSet>. Uses <aFilter> to determine if an attribute has to be taken in account or not. Uses <aMode> for various way of closing.

        Builds the transitive closure of <aLabel>.
        """
    @staticmethod
    @overload
    def Closure_s(aDataSet : TDF_DataSet,aFilter : TDF_IDFilter,aMode : TDF_ClosureMode) -> None: ...
    @staticmethod
    @overload
    def Closure_s(aLabel : TDF_Label,aLabMap : TDF_LabelMap,anAttMap : TDF_AttributeMap,aFilter : TDF_IDFilter,aMode : TDF_ClosureMode) -> None: ...
    def __init__(self) -> None: ...
    pass
class TDF_ComparisonTool():
    """
    This class provides services to compare sets of information. The use of this tool can works after a copy, acted by a CopyTool.
    """
    @staticmethod
    def Compare_s(aSourceDataSet : TDF_DataSet,aTargetDataSet : TDF_DataSet,aFilter : TDF_IDFilter,aRelocationTable : TDF_RelocationTable) -> None: 
        """
        Compares <aSourceDataSet> with <aTargetDataSet>, updating <aRelocationTable> with labels and attributes found in both sets.
        """
    @staticmethod
    def Cut_s(aDataSet : TDF_DataSet) -> None: 
        """
        Removes attributes from <aDataSet>.
        """
    @staticmethod
    def IsSelfContained_s(aLabel : TDF_Label,aDataSet : TDF_DataSet) -> bool: 
        """
        Returns true if all the labels of <aDataSet> are descendant of <aLabel>.
        """
    @staticmethod
    def SourceUnbound_s(aRefDataSet : TDF_DataSet,aRelocationTable : TDF_RelocationTable,aFilter : TDF_IDFilter,aDiffDataSet : TDF_DataSet,anOption : int=2) -> bool: 
        """
        Finds from <aRefDataSet> all the keys not bound into <aRelocationTable> and put them into <aDiffDataSet>. Returns True if the difference contains at least one key. (A key is a source object).
        """
    @staticmethod
    def TargetUnbound_s(aRefDataSet : TDF_DataSet,aRelocationTable : TDF_RelocationTable,aFilter : TDF_IDFilter,aDiffDataSet : TDF_DataSet,anOption : int=2) -> bool: 
        """
        Substracts from <aRefDataSet> all the items bound into <aRelocationTable>. The result is put into <aDiffDataSet>. Returns True if the difference contains at least one item. (An item is a target object).
        """
    def __init__(self) -> None: ...
    pass
class TDF_CopyLabel():
    """
    This class gives copy of source label hierarchy
    """
    @staticmethod
    @overload
    def ExternalReferences_s(Lab : TDF_Label,aExternals : TDF_AttributeMap,aFilter : TDF_IDFilter) -> bool: 
        """
        Check external references and if exist fills the aExternals Map

        Check external references and if exist fills the aExternals Map
        """
    @staticmethod
    @overload
    def ExternalReferences_s(aRefLab : TDF_Label,Lab : TDF_Label,aExternals : TDF_AttributeMap,aFilter : TDF_IDFilter,aDataSet : TDF_DataSet) -> None: ...
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def Load(self,aSource : TDF_Label,aTarget : TDF_Label) -> None: 
        """
        Loads src and tgt labels
        """
    def Perform(self) -> None: 
        """
        performs algorithm of selfcontained copy
        """
    def RelocationTable(self) -> TDF_RelocationTable: 
        """
        returns relocation table
        """
    def UseFilter(self,aFilter : TDF_IDFilter) -> None: 
        """
        Sets filter
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aSource : TDF_Label,aTarget : TDF_Label) -> None: ...
    pass
class TDF_CopyTool():
    """
    This class provides services to build, copy or paste a set of information.
    """
    @staticmethod
    @overload
    def Copy_s(aSourceDataSet : TDF_DataSet,aRelocationTable : TDF_RelocationTable,aPrivilegeFilter : TDF_IDFilter,aRefFilter : TDF_IDFilter,setSelfContained : bool) -> None: 
        """
        Copy <aSourceDataSet> with using and updating <aRelocationTable>. This method ignores target attributes privilege over source ones.

        Copy <aSourceDataSet> using and updating <aRelocationTable>. Use <aPrivilegeFilter> to give a list of IDs for which the target attribute prevails over the source one.

        Copy <aSourceDataSet> using and updating <aRelocationTable>. Use <aPrivilegeFilter> to give a list of IDs for which the target attribute prevails over the source one. If <setSelfContained> is set to true, every TDF_Reference will be replaced by the referenced structure according to <aRefFilter>.
        """
    @staticmethod
    @overload
    def Copy_s(aSourceDataSet : TDF_DataSet,aRelocationTable : TDF_RelocationTable) -> None: ...
    @staticmethod
    @overload
    def Copy_s(aSourceDataSet : TDF_DataSet,aRelocationTable : TDF_RelocationTable,aPrivilegeFilter : TDF_IDFilter) -> None: ...
    def __init__(self) -> None: ...
    pass
class TDF_Data(OCP.Standard.Standard_Transient):
    """
    This class is used to manipulate a complete independent, self sufficient data structure and its services:This class is used to manipulate a complete independent, self sufficient data structure and its services:This class is used to manipulate a complete independent, self sufficient data structure and its services:
    """
    @overload
    def AllowModification(self,isAllowed : bool) -> None: 
        """
        Sets modification mode.

        Sets modification mode.
        """
    @overload
    def AllowModification(self,theAllowModification : bool) -> None: ...
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
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the Data on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetLabel(self,anEntry : OCP.TCollection.TCollection_AsciiString,aLabel : TDF_Label) -> bool: 
        """
        Returns a label by an entry. Returns Standard_False, if such a label doesn't exist or mechanism for fast access to the label by entry is not initialized.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAccessByEntries(self) -> bool: 
        """
        Returns a status of mechanism for fast access to the labels via entries.
        """
    def IsApplicable(self,aDelta : TDF_Delta) -> bool: 
        """
        Returns true if <aDelta> is applicable HERE and NOW.
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
    def IsModificationAllowed(self) -> bool: 
        """
        returns modification mode.

        returns modification mode.
        """
    def LabelNodeAllocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns TDF_HAllocator, which is an incremental allocator used by TDF_LabelNode. This allocator is used to manage TDF_LabelNode objects, but it can also be used for allocating memory to application-specific data (be careful because this allocator does not release the memory). The benefits of this allocation scheme are noticeable when dealing with large OCAF documents, due to: 1. Very quick allocation of objects (memory heap is not used, the algorithm that replaces it is very simple). 2. Very quick destruction of objects (memory is released not by destructors of TDF_LabelNode, but rather by the destructor of TDF_Data). 3. TDF_LabelNode objects do not fragmentize the memory; they are kept compactly in a number of arrays of 16K each. 4. Swapping is reduced on large data, because each document now occupies a smaller number of memory pages.

        Returns TDF_HAllocator, which is an incremental allocator used by TDF_LabelNode. This allocator is used to manage TDF_LabelNode objects, but it can also be used for allocating memory to application-specific data (be careful because this allocator does not release the memory). The benefits of this allocation scheme are noticeable when dealing with large OCAF documents, due to: 1. Very quick allocation of objects (memory heap is not used, the algorithm that replaces it is very simple). 2. Very quick destruction of objects (memory is released not by destructors of TDF_LabelNode, but rather by the destructor of TDF_Data). 3. TDF_LabelNode objects do not fragmentize the memory; they are kept compactly in a number of arrays of 16K each. 4. Swapping is reduced on large data, because each document now occupies a smaller number of memory pages.
        """
    def NotUndoMode(self) -> bool: 
        """
        Returns the undo mode status.

        Returns the undo mode status.
        """
    def RegisterLabel(self,aLabel : TDF_Label) -> None: 
        """
        An internal method. It is used internally on creation of new labels. It adds a new label into internal table for fast access to the labels by entry.
        """
    def Root(self) -> TDF_Label: 
        """
        Returns the root label of the Data structure.

        Returns the root label of the Data structure.
        """
    def SetAccessByEntries(self,aSet : bool) -> None: 
        """
        Initializes a mechanism for fast access to the labels by their entries. The fast access is useful for large documents and often access to the labels via entries. Internally, a table of entry - label is created, which allows to obtain a label by its entry in a very fast way. If the mechanism is turned off, the internal table is cleaned. New labels are added to the table, if the mechanism is on (no need to re-initialize the mechanism).
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Time(self) -> int: 
        """
        Returns the current tick. It is incremented each Commit.

        Returns the current tick. It is incremented each Commit.
        """
    def Transaction(self) -> int: 
        """
        Returns the current transaction number.

        Returns the current transaction number.
        """
    def Undo(self,aDelta : TDF_Delta,withDelta : bool=False) -> TDF_Delta: 
        """
        Apply <aDelta> to undo a set of attribute modifications.
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
class TDF_DataSet(OCP.Standard.Standard_Transient):
    """
    This class is a set of TDF information like labels and attributes.This class is a set of TDF information like labels and attributes.This class is a set of TDF information like labels and attributes.
    """
    def AddAttribute(self,anAttribute : TDF_Attribute) -> None: 
        """
        Adds <anAttribute> into the current data set.

        Adds <anAttribute> into the current data set.
        """
    def AddLabel(self,aLabel : TDF_Label) -> None: 
        """
        Adds <aLabel> in the current data set.

        Adds <aLabel> in the current data set.
        """
    def AddRoot(self,aLabel : TDF_Label) -> None: 
        """
        Adds a root label to <myRootLabels>.

        Adds a root label to <myRootLabels>.
        """
    def Attributes(self) -> TDF_AttributeMap: 
        """
        Returns the map of attributes in the current data set. This map can be used directly, or updated.

        Returns the map of attributes in the current data set. This map can be used directly, or updated.
        """
    def Clear(self) -> None: 
        """
        Clears all information.
        """
    def ContainsAttribute(self,anAttribute : TDF_Attribute) -> bool: 
        """
        Returns true if <anAttribute> is in the data set.

        Returns true if <anAttribute> is in the data set.
        """
    def ContainsLabel(self,aLabel : TDF_Label) -> bool: 
        """
        Returns true if the label <alabel> is in the data set.

        Returns true if the label <alabel> is in the data set.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
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
        Returns true if there is at least one label or one attribute.

        Returns true if there is at least one label or one attribute.
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
    def Labels(self) -> TDF_LabelMap: 
        """
        Returns the map of labels in this data set. This map can be used directly, or updated.

        Returns the map of labels in this data set. This map can be used directly, or updated.
        """
    def Roots(self) -> TDF_LabelList: 
        """
        Returns <myRootLabels> to be used or updated.

        Returns <myRootLabels> to be used or updated.
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
class TDF_DeltaOnModification(TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label concerned by <me>.
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
class TDF_DeltaOnRemoval(TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on a REMOVAL action.This class provides default services for an AttributeDelta on a REMOVAL action.This class provides default services for an AttributeDelta on a REMOVAL action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label concerned by <me>.
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
class TDF_Delta(OCP.Standard.Standard_Transient):
    """
    A set of AttributeDelta for a given transaction number and reference time number. A delta set is available at <aSourceTime>. If applied, it restores the TDF_Data in the state it was at <aTargetTime>.A set of AttributeDelta for a given transaction number and reference time number. A delta set is available at <aSourceTime>. If applied, it restores the TDF_Data in the state it was at <aTargetTime>.A set of AttributeDelta for a given transaction number and reference time number. A delta set is available at <aSourceTime>. If applied, it restores the TDF_Data in the state it was at <aTargetTime>.
    """
    def AttributeDeltas(self) -> TDF_AttributeDeltaList: 
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
    def Labels(self,aLabelList : TDF_LabelList) -> None: 
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
class TDF_DeltaList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TDF_Delta,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TDF_DeltaList) -> None: ...
    @overload
    def Append(self,theItem : TDF_Delta) -> TDF_Delta: ...
    def Assign(self,theOther : TDF_DeltaList) -> TDF_DeltaList: 
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
    def First(self) -> TDF_Delta: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TDF_DeltaList,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : TDF_Delta,theIter : Any) -> TDF_Delta: ...
    @overload
    def InsertBefore(self,theOther : TDF_DeltaList,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : TDF_Delta,theIter : Any) -> TDF_Delta: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TDF_Delta: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : TDF_Delta) -> TDF_Delta: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TDF_DeltaList) -> None: ...
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
    def __init__(self,theOther : TDF_DeltaList) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDF_DeltaOnAddition(TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on an ADDITION action.This class provides default services for an AttributeDelta on an ADDITION action.This class provides default services for an AttributeDelta on an ADDITION action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,anAtt : TDF_Attribute) -> None: ...
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
class TDF_DeltaOnForget(TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on an Forget action.This class provides default services for an AttributeDelta on an Forget action.This class provides default services for an AttributeDelta on an Forget action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,anAtt : TDF_Attribute) -> None: ...
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
class TDF_DefaultDeltaOnModification(TDF_DeltaOnModification, TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides a default implementation of a TDF_DeltaOnModification.This class provides a default implementation of a TDF_DeltaOnModification.This class provides a default implementation of a TDF_DeltaOnModification.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,anAttribute : TDF_Attribute) -> None: ...
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
class TDF_DefaultDeltaOnRemoval(TDF_DeltaOnRemoval, TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides a default implementation of a TDF_DeltaOnRemoval.This class provides a default implementation of a TDF_DeltaOnRemoval.This class provides a default implementation of a TDF_DeltaOnRemoval.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,anAttribute : TDF_Attribute) -> None: ...
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
class TDF_DeltaOnResume(TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on an Resume action.This class provides default services for an AttributeDelta on an Resume action.This class provides default services for an AttributeDelta on an Resume action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,anAtt : TDF_Attribute) -> None: ...
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
class TDF_DerivedAttribute():
    """
    Class provides global access (through static methods) to all derived attributres information. It is used internally by macros for registration of derived attributes and driver-tables for getting this data.
    """
    @staticmethod
    def Attribute_s(theType : str) -> TDF_Attribute: 
        """
        Returns the derived registered attribute by its type.
        """
    @staticmethod
    def Attributes_s(theList : TDF_AttributeList) -> None: 
        """
        Returns all the derived registered attributes list.
        """
    @staticmethod
    def TypeName_s(theType : str) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the type name of the registered attribute by its type.
        """
    def __init__(self) -> None: ...
    pass
class TDF_GUIDProgIDMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DoubleMap is used to bind pairs (Key1,Key2) and retrieve them in linear time.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def AreBound(self,theKey1 : OCP.Standard.Standard_GUID,theKey2 : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        * AreBound
        """
    def Assign(self,theOther : TDF_GUIDProgIDMap) -> TDF_GUIDProgIDMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey1 : OCP.Standard.Standard_GUID,theKey2 : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Bind
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TDF_GUIDProgIDMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find1(self,theKey1 : OCP.Standard.Standard_GUID) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Find the Key1 and return Key2 value. Raises an exception if Key1 was not bound.

        Find the Key1 and return Key2 value (by copying its value).
        """
    @overload
    def Find1(self,theKey1 : OCP.Standard.Standard_GUID,theKey2 : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    @overload
    def Find2(self,theKey2 : OCP.TCollection.TCollection_ExtendedString) -> OCP.Standard.Standard_GUID: 
        """
        Find the Key2 and return Key1 value. Raises an exception if Key2 was not bound.

        Find the Key2 and return Key1 value (by copying its value).
        """
    @overload
    def Find2(self,theKey2 : OCP.TCollection.TCollection_ExtendedString,theKey1 : OCP.Standard.Standard_GUID) -> bool: ...
    def IsBound1(self,theKey1 : OCP.Standard.Standard_GUID) -> bool: 
        """
        IsBound1
        """
    def IsBound2(self,theKey2 : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        IsBound2
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
    def Seek1(self,theKey1 : OCP.Standard.Standard_GUID) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Find the Key1 and return pointer to Key2 or NULL if Key1 is not bound.
        """
    def Seek2(self,theKey2 : OCP.TCollection.TCollection_ExtendedString) -> OCP.Standard.Standard_GUID: 
        """
        Find the Key2 and return pointer to Key1 or NULL if not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind1(self,theKey1 : OCP.Standard.Standard_GUID) -> bool: 
        """
        UnBind1
        """
    def UnBind2(self,theKey2 : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        UnBind2
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_GUIDProgIDMap) -> None: ...
    pass
class TDF_HAttributeArray1(TDF_AttributeArray1, OCP.Standard.Standard_Transient):
    def Array1(self) -> TDF_AttributeArray1: 
        """
        None
        """
    def Assign(self,theOther : TDF_AttributeArray1) -> TDF_AttributeArray1: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TDF_AttributeArray1: 
        """
        None
        """
    def ChangeFirst(self) -> TDF_Attribute: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TDF_Attribute: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TDF_Attribute: 
        """
        Variable value access
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
    def First(self) -> TDF_Attribute: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : TDF_Attribute) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> TDF_Attribute: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : TDF_AttributeArray1) -> TDF_AttributeArray1: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TDF_Attribute) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> TDF_Attribute: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TDF_AttributeArray1) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : TDF_Attribute) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class TDF_IDFilter():
    """
    This class offers filtering services around an ID list.
    """
    def Assign(self,theFilter : TDF_IDFilter) -> None: 
        """
        Assignment
        """
    def Copy(self,fromFilter : TDF_IDFilter) -> None: 
        """
        Copies into <me> the contents of <fromFilter>. <me> is cleared before copy.
        """
    def Dump(self,anOS : io.BytesIO) -> None: 
        """
        Writes the contents of <me> to <OS>.
        """
    def IDList(self,anIDList : TDF_IDList) -> None: 
        """
        Copies the list of ID to be kept or ignored in <anIDList>. <anIDList> is cleared before use.
        """
    @overload
    def Ignore(self,anIDList : TDF_IDList) -> None: 
        """
        An attribute with <anID> as ID is to be ignored and the filter will answer false to the question IsKept(<anID>).

        Attributes with ID owned by <anIDList> are to be ignored and the filter will answer false to the question IsKept(<anID>) with ID from <anIDList>.
        """
    @overload
    def Ignore(self,anID : OCP.Standard.Standard_GUID) -> None: ...
    @overload
    def IgnoreAll(self) -> bool: 
        """
        The list of ID is cleared and the filter mode is set to ignore mode if <keep> is true; false otherwise.

        Returns true is the mode is set to "ignore all but...".

        Returns true is the mode is set to "ignore all but...".
        """
    @overload
    def IgnoreAll(self,ignore : bool) -> None: ...
    @overload
    def IsIgnored(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if the ID is to be ignored.

        Returns true if the attribute is to be ignored.

        Returns true if the ID is to be ignored.

        Returns true if the attribute is to be ignored.
        """
    @overload
    def IsIgnored(self,anAtt : TDF_Attribute) -> bool: ...
    @overload
    def IsKept(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if the ID is to be kept.

        Returns true if the attribute is to be kept.

        Returns true if the ID is to be kept.

        Returns true if the attribute is to be kept.
        """
    @overload
    def IsKept(self,anAtt : TDF_Attribute) -> bool: ...
    @overload
    def Keep(self,anID : OCP.Standard.Standard_GUID) -> None: 
        """
        An attribute with <anID> as ID is to be kept and the filter will answer true to the question IsKept(<anID>).

        Attributes with ID owned by <anIDList> are to be kept and the filter will answer true to the question IsKept(<anID>) with ID from <anIDList>.
        """
    @overload
    def Keep(self,anIDList : TDF_IDList) -> None: ...
    def __init__(self,ignoreMode : bool=True) -> None: ...
    pass
class TDF_IDList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.Standard.Standard_GUID,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.Standard.Standard_GUID) -> OCP.Standard.Standard_GUID: ...
    @overload
    def Append(self,theOther : TDF_IDList) -> None: ...
    def Assign(self,theOther : TDF_IDList) -> TDF_IDList: 
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
    def First(self) -> OCP.Standard.Standard_GUID: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.Standard.Standard_GUID,theIter : Any) -> OCP.Standard.Standard_GUID: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TDF_IDList,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : OCP.Standard.Standard_GUID,theIter : Any) -> OCP.Standard.Standard_GUID: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TDF_IDList,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.Standard.Standard_GUID: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.Standard.Standard_GUID) -> OCP.Standard.Standard_GUID: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TDF_IDList) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_IDList) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDF_IDMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : OCP.Standard.Standard_GUID) -> bool: 
        """
        Add
        """
    def Added(self,K : OCP.Standard.Standard_GUID) -> OCP.Standard.Standard_GUID: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDF_IDMap) -> TDF_IDMap: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def Contains(self,theOther : TDF_IDMap) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : OCP.Standard.Standard_GUID) -> bool: ...
    def Differ(self,theOther : TDF_IDMap) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TDF_IDMap,theRight : TDF_IDMap) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TDF_IDMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TDF_IDMap) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TDF_IDMap) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TDF_IDMap,theRight : TDF_IDMap) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TDF_IDMap) -> bool: 
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
    def Remove(self,K : OCP.Standard.Standard_GUID) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TDF_IDMap) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TDF_IDMap,theRight : TDF_IDMap) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TDF_IDMap,theRight : TDF_IDMap) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TDF_IDMap) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theOther : TDF_IDMap) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class TDF_Label():
    """
    This class provides basic operations to define a label in a data structure. A label is a feature in the feature hierarchy. A label is always connected to a Data from TDF. To a label is attached attributes containing the software components information.
    """
    def AddAttribute(self,anAttribute : TDF_Attribute,append : bool=True) -> None: 
        """
        Adds an Attribute to the current label. Raises if there is already one.
        """
    def AttributesModified(self) -> bool: 
        """
        Returns true if <me> owns attributes not yet available in transaction 0. It means at least one attribute is new, modified or deleted.

        Returns true if <me> owns attributes not yet available in transaction 0. It means at least one attribute is new, modified or deleted.
        """
    def Data(self) -> TDF_Data: 
        """
        Returns the Data owning <me>.

        Returns the Data owning <me>.
        """
    def Depth(self) -> int: 
        """
        Returns the depth of the label in the data framework. This corresponds to the number of fathers which this label has, and is used in determining whether a label is root, null or equivalent to another label. Exceptions: Standard_NullObject if this label is null. This is because a null object can have no depth.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def EntryDump(self,anOS : io.BytesIO) -> None: 
        """
        Dumps the label entry.
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : TDF_IDFilter,aMap : TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the label on <aStream> and its attributes rank in <aMap> if their IDs are kept by <IDFilter>.
        """
    def Father(self) -> TDF_Label: 
        """
        Returns the label father. This label may be null if the label is root.

        Returns the label father. This label may be null if the label is root.
        """
    def FindAttribute(self,GUID : OCP.Standard.Standard_GUID,Attribute : TDF_Attribute) -> bool: 
        """
        Finds an attributes according to an ID.
        """
    def FindChild(self,aTag : int,create : bool=True) -> TDF_Label: 
        """
        Finds a child label having <aTag> as tag. Creates The tag aTag identifies the label which will be the parent. If create is true and no child label is found, a new one is created. Example: //creating a label with tag 10 at Root TDF_Label lab1 = aDF->Root().FindChild(10); //creating labels 7 and 2 on label 10 TDF_Label lab2 = lab1.FindChild(7); TDF_Label lab3 = lab1.FindChild(2);
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes. Does it on also on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms.
        """
    @overload
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets an Attribute from the current label, setting its forgotten status true and its valid status false. Raises if the attribute is not in the structure.

        Forgets the Attribute of GUID <aguid> from the current label . If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @overload
    def ForgetAttribute(self,anAttribute : TDF_Attribute) -> None: ...
    def HasAttribute(self) -> bool: 
        """
        Returns true if this label has at least one attribute.
        """
    def HasChild(self) -> bool: 
        """
        Returns true if this label has at least one child.

        Returns true if this label has at least one child.
        """
    def HasGreaterNode(self,otherLabel : TDF_Label) -> bool: 
        """
        Returns true if node address of <me> is greater than <otherLabel> one. Used to quickly sort labels (not on entry criterion).
        """
    def HasLowerNode(self,otherLabel : TDF_Label) -> bool: 
        """
        Returns true if node address of <me> is lower than <otherLabel> one. Used to quickly sort labels (not on entry criterion).
        """
    def Imported(self,aStatus : bool) -> None: 
        """
        Sets or unsets <me> and all its descendants as imported label, according to <aStatus>.
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if <me> owns an attribute with <anID> as ID.
        """
    def IsDescendant(self,aLabel : TDF_Label) -> bool: 
        """
        Returns True if <me> is a descendant of <aLabel>. Attention: every label is its own descendant.
        """
    def IsDifferent(self,aLabel : TDF_Label) -> bool: 
        """
        None

        None
        """
    def IsEqual(self,aLabel : TDF_Label) -> bool: 
        """
        Returns True if the <aLabel> is equal to me (same LabelNode*).

        Returns True if the <aLabel> is equal to me (same LabelNode*).
        """
    def IsImported(self) -> bool: 
        """
        Returns True if the <aLabel> is imported.

        Returns True if the <aLabel> is imported.
        """
    def IsNull(self) -> bool: 
        """
        Returns True if the <aLabel> is null, i.e. it has not been included in the data framework.

        Returns True if the <aLabel> is null, i.e. it has not been included in the data framework.
        """
    def IsRoot(self) -> bool: 
        """
        None

        None
        """
    def MayBeModified(self) -> bool: 
        """
        Returns true if <me> or a DESCENDANT of <me> owns attributes not yet available in transaction 0. It means at least one of their attributes is new, modified or deleted.

        Returns true if <me> or a DESCENDANT of <me> owns attributes not yet available in transaction 0. It means at least one of their attributes is new, modified or deleted.
        """
    def NbAttributes(self) -> int: 
        """
        Returns the number of attributes.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of children.
        """
    def NewChild(self) -> TDF_Label: 
        """
        Create a new child label of me using autoamtic delivery tags provided by TagSource.

        Create a new child label of me using autoamtic delivery tags provided by TagSource.
        """
    def Nullify(self) -> None: 
        """
        Nullifies the label.

        Nullifies the label.
        """
    def ResumeAttribute(self,anAttribute : TDF_Attribute) -> None: 
        """
        Undo Forget action, setting its forgotten status false and its valid status true. Raises if the attribute is not in the structure.
        """
    def Root(self) -> TDF_Label: 
        """
        Returns the root label Root of the data structure. This has a depth of 0. Exceptions: Standard_NullObject if this label is null. This is because a null object can have no depth.
        """
    def Tag(self) -> int: 
        """
        Returns the tag of the label. This is the integer assigned randomly to a label in a data framework. This integer is used to identify this label in an entry.

        Returns the tag of the label. This is the integer assigned randomly to a label in a data framework. This integer is used to identify this label in an entry.
        """
    def Transaction(self) -> int: 
        """
        Returns the current transaction index.
        """
    def __init__(self) -> None: ...
    pass
class TDF_LabelDataMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDF_LabelDataMap) -> TDF_LabelDataMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : TDF_Label,theItem : TDF_Label) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : TDF_Label,theItem : TDF_Label) -> TDF_Label: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : TDF_Label) -> TDF_Label: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : TDF_Label) -> TDF_Label: 
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
    def Exchange(self,theOther : TDF_LabelDataMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : TDF_Label,theValue : TDF_Label) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : TDF_Label) -> TDF_Label: ...
    def IsBound(self,theKey : TDF_Label) -> bool: 
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
    def Seek(self,theKey : TDF_Label) -> TDF_Label: 
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
    def UnBind(self,theKey : TDF_Label) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_LabelDataMap) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDF_LabelDoubleMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DoubleMap is used to bind pairs (Key1,Key2) and retrieve them in linear time.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def AreBound(self,theKey1 : TDF_Label,theKey2 : TDF_Label) -> bool: 
        """
        * AreBound
        """
    def Assign(self,theOther : TDF_LabelDoubleMap) -> TDF_LabelDoubleMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey1 : TDF_Label,theKey2 : TDF_Label) -> None: 
        """
        Bind
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : TDF_LabelDoubleMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find1(self,theKey1 : TDF_Label,theKey2 : TDF_Label) -> bool: 
        """
        Find the Key1 and return Key2 value. Raises an exception if Key1 was not bound.

        Find the Key1 and return Key2 value (by copying its value).
        """
    @overload
    def Find1(self,theKey1 : TDF_Label) -> TDF_Label: ...
    @overload
    def Find2(self,theKey2 : TDF_Label,theKey1 : TDF_Label) -> bool: 
        """
        Find the Key2 and return Key1 value. Raises an exception if Key2 was not bound.

        Find the Key2 and return Key1 value (by copying its value).
        """
    @overload
    def Find2(self,theKey2 : TDF_Label) -> TDF_Label: ...
    def IsBound1(self,theKey1 : TDF_Label) -> bool: 
        """
        IsBound1
        """
    def IsBound2(self,theKey2 : TDF_Label) -> bool: 
        """
        IsBound2
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
    def Seek1(self,theKey1 : TDF_Label) -> TDF_Label: 
        """
        Find the Key1 and return pointer to Key2 or NULL if Key1 is not bound.
        """
    def Seek2(self,theKey2 : TDF_Label) -> TDF_Label: 
        """
        Find the Key2 and return pointer to Key1 or NULL if not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind1(self,theKey1 : TDF_Label) -> bool: 
        """
        UnBind1
        """
    def UnBind2(self,theKey2 : TDF_Label) -> bool: 
        """
        UnBind2
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_LabelDoubleMap) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class TDF_LabelIndexedMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : TDF_Label) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDF_LabelIndexedMap) -> TDF_LabelIndexedMap: 
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
    def Contains(self,theKey1 : TDF_Label) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TDF_LabelIndexedMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : TDF_Label) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> TDF_Label: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,theExtent : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : TDF_Label) -> bool: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : TDF_Label) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_LabelIndexedMap) -> None: ...
    pass
class TDF_LabelIntegerMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDF_LabelIntegerMap) -> TDF_LabelIntegerMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : TDF_Label,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : TDF_Label,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : TDF_Label) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : TDF_Label) -> int: 
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
    def Exchange(self,theOther : TDF_LabelIntegerMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : TDF_Label,theValue : int) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : TDF_Label) -> int: ...
    def IsBound(self,theKey : TDF_Label) -> bool: 
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
    def Seek(self,theKey : TDF_Label) -> int: 
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
    def UnBind(self,theKey : TDF_Label) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_LabelIntegerMap) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDF_LabelList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TDF_Label) -> TDF_Label: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TDF_LabelList) -> None: ...
    @overload
    def Append(self,theItem : TDF_Label,theIter : Any) -> None: ...
    def Assign(self,theOther : TDF_LabelList) -> TDF_LabelList: 
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
    def First(self) -> TDF_Label: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TDF_LabelList,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : TDF_Label,theIter : Any) -> TDF_Label: ...
    @overload
    def InsertBefore(self,theOther : TDF_LabelList,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : TDF_Label,theIter : Any) -> TDF_Label: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TDF_Label: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : TDF_Label) -> TDF_Label: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TDF_LabelList) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_LabelList) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDF_LabelMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : TDF_Label) -> bool: 
        """
        Add
        """
    def Added(self,K : TDF_Label) -> TDF_Label: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDF_LabelMap) -> TDF_LabelMap: 
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
    def Contains(self,K : TDF_Label) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : TDF_LabelMap) -> bool: ...
    def Differ(self,theOther : TDF_LabelMap) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TDF_LabelMap,theRight : TDF_LabelMap) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TDF_LabelMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TDF_LabelMap) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TDF_LabelMap) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TDF_LabelMap,theRight : TDF_LabelMap) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TDF_LabelMap) -> bool: 
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
    def Remove(self,K : TDF_Label) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TDF_LabelMap) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TDF_LabelMap,theRight : TDF_LabelMap) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TDF_LabelMap,theRight : TDF_LabelMap) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TDF_LabelMap) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theOther : TDF_LabelMap) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TDF_LabelMapHasher():
    """
    A label hasher for label maps.
    """
    @staticmethod
    def HashCode_s(theLabel : TDF_Label,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given label, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(aLab1 : TDF_Label,aLab2 : TDF_Label) -> bool: 
        """
        Returns True when the two keys are the same. Two same keys must have the same hashcode, the contrary is not necessary.
        """
    def __init__(self) -> None: ...
    pass
class TDF_LabelSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : TDF_LabelSequence) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : TDF_Label) -> None: ...
    def Assign(self,theOther : TDF_LabelSequence) -> TDF_LabelSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> TDF_Label: 
        """
        First item access
        """
    def ChangeLast(self) -> TDF_Label: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> TDF_Label: 
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
    def First(self) -> TDF_Label: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : TDF_Label) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : TDF_LabelSequence) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : TDF_Label) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : TDF_LabelSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> TDF_Label: 
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
    def Prepend(self,theSeq : TDF_LabelSequence) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : TDF_Label) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : TDF_Label) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : TDF_LabelSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> TDF_Label: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDF_LabelSequence) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class TDF_Reference(TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    This attribute is used to store in the framework a reference to an other label.This attribute is used to store in the framework a reference to an other label.This attribute is used to store in the framework a reference to an other label.
    """
    def AddAttribute(self,other : TDF_Attribute) -> None: 
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
    def AfterUndo(self,anAttDelta : TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> TDF_Attribute: 
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
    def BeforeUndo(self,anAttDelta : TDF_AttributeDelta,forceIt : bool=False) -> bool: 
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
    def DeltaOnAddition(self) -> TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : TDF_Attribute) -> TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> TDF_DeltaOnResume: 
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
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : TDF_IDFilter,aMap : TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : TDF_Attribute) -> bool: 
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
    def Get(self) -> TDF_Label: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : TDF_Attribute,RT : TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,DS : TDF_DataSet) -> None: 
        """
        None
        """
    def Restore(self,With : TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,Origin : TDF_Label) -> None: 
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
    @staticmethod
    def Set_s(I : TDF_Label,Origin : TDF_Label) -> TDF_Reference: 
        """
        None
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
class TDF_RelocationTable(OCP.Standard.Standard_Transient):
    """
    This is a relocation dictionary between source and target labels, attributes or any transient(useful for copy or paste actions). Note that one target value may be the relocation value of more than one source object.This is a relocation dictionary between source and target labels, attributes or any transient(useful for copy or paste actions). Note that one target value may be the relocation value of more than one source object.This is a relocation dictionary between source and target labels, attributes or any transient(useful for copy or paste actions). Note that one target value may be the relocation value of more than one source object.
    """
    @overload
    def AfterRelocate(self) -> bool: 
        """
        None

        Returns <myAfterRelocate>.
        """
    @overload
    def AfterRelocate(self,afterRelocate : bool) -> None: ...
    def AttributeTable(self) -> Any: 
        """
        Returns <myAttributeTable> to be used or updated.
        """
    def Clear(self) -> None: 
        """
        Clears the relocation dictionary, but lets the self relocation flag to its current value.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,dumpLabels : bool,dumpAttributes : bool,dumpTransients : bool,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the relocation table.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def HasRelocation(self,aSourceLabel : TDF_Label,aTargetLabel : TDF_Label) -> bool: 
        """
        Finds the relocation value of <aSourceLabel> and returns it into <aTargetLabel>.

        Finds the relocation value of <aSourceAttribute> and returns it into <aTargetAttribute>.
        """
    @overload
    def HasRelocation(self,aSourceAttribute : TDF_Attribute,aTargetAttribute : TDF_Attribute) -> bool: ...
    def HasTransientRelocation(self,aSourceTransient : OCP.Standard.Standard_Transient,aTargetTransient : OCP.Standard.Standard_Transient) -> bool: 
        """
        Finds the relocation value of <aSourceTransient> and returns it into <aTargetTransient>.
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
    def LabelTable(self) -> TDF_LabelDataMap: 
        """
        Returns <myLabelTable> to be used or updated.
        """
    @overload
    def SelfRelocate(self,selfRelocate : bool) -> None: 
        """
        Sets <mySelfRelocate> to <selfRelocate>.

        Returns <mySelfRelocate>.
        """
    @overload
    def SelfRelocate(self) -> bool: ...
    @overload
    def SetRelocation(self,aSourceLabel : TDF_Label,aTargetLabel : TDF_Label) -> None: 
        """
        Sets the relocation value of <aSourceLabel> to <aTargetLabel>.

        Sets the relocation value of <aSourceAttribute> to <aTargetAttribute>.
        """
    @overload
    def SetRelocation(self,aSourceAttribute : TDF_Attribute,aTargetAttribute : TDF_Attribute) -> None: ...
    def SetTransientRelocation(self,aSourceTransient : OCP.Standard.Standard_Transient,aTargetTransient : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets the relocation value of <aSourceTransient> to <aTargetTransient>.
        """
    def TargetAttributeMap(self,anAttributeMap : TDF_AttributeMap) -> None: 
        """
        Fills <anAttributeMap> with target relocation attributes. <anAttributeMap> is not cleared before use.
        """
    def TargetLabelMap(self,aLabelMap : TDF_LabelMap) -> None: 
        """
        Fills <aLabelMap> with target relocation labels. <aLabelMap> is not cleared before use.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransientTable(self) -> Any: 
        """
        Returns <myTransientTable> to be used or updated.
        """
    def __init__(self,selfRelocate : bool=False) -> None: ...
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
class TDF_TagSource(TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    This attribute manage a tag provider to create child labels of a given one.This attribute manage a tag provider to create child labels of a given one.This attribute manage a tag provider to create child labels of a given one.
    """
    def AddAttribute(self,other : TDF_Attribute) -> None: 
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
    def AfterUndo(self,anAttDelta : TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> TDF_Attribute: 
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
    def BeforeUndo(self,anAttDelta : TDF_AttributeDelta,forceIt : bool=False) -> bool: 
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
    def DeltaOnAddition(self) -> TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : TDF_Attribute) -> TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> TDF_DeltaOnResume: 
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
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : TDF_IDFilter,aMap : TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : TDF_Attribute) -> bool: 
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
    def Get(self) -> int: 
        """
        None
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
    def Label(self) -> TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewChild(self) -> TDF_Label: 
        """
        None
        """
    @staticmethod
    def NewChild_s(L : TDF_Label) -> TDF_Label: ...
    def NewEmpty(self) -> TDF_Attribute: 
        """
        None
        """
    def NewTag(self) -> int: 
        """
        None
        """
    def Paste(self,Into : TDF_Attribute,RT : TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,T : int) -> None: 
        """
        TDF_Attribute methods =====================
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
    def Set_s(label : TDF_Label) -> TDF_TagSource: 
        """
        Find, or create, a TagSource attribute. the TagSource attribute is returned.
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
class TDF_Tool():
    """
    This class provides general services for a data framework.
    """
    @staticmethod
    def CountLabels_s(aLabelList : TDF_LabelList,aLabelMap : TDF_LabelIntegerMap) -> None: 
        """
        Adds the labels of <aLabelList> to <aLabelMap> if they are unbound, or increases their reference counters. At the end of the process, <aLabelList> contains only the ADDED labels.
        """
    @staticmethod
    def DeductLabels_s(aLabelList : TDF_LabelList,aLabelMap : TDF_LabelIntegerMap) -> None: 
        """
        Decreases the reference counters of the labels of <aLabelList> to <aLabelMap>, and removes labels with null counter. At the end of the process, <aLabelList> contains only the SUPPRESSED labels.
        """
    @staticmethod
    @overload
    def DeepDump_s(anOS : io.BytesIO,aDF : TDF_Data) -> None: 
        """
        Dumps <aDF> and its labels and their attributes.

        Dumps <aLabel>, its children and their attributes.
        """
    @staticmethod
    @overload
    def DeepDump_s(anOS : io.BytesIO,aLabel : TDF_Label) -> None: ...
    @staticmethod
    def Entry_s(aLabel : TDF_Label,anEntry : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Returns the entry for the label aLabel in the form of the ASCII character string anEntry containing the tag list for aLabel.
        """
    @staticmethod
    @overload
    def ExtendedDeepDump_s(anOS : io.BytesIO,aLabel : TDF_Label,aFilter : TDF_IDFilter) -> None: 
        """
        Dumps <aDF> and its labels and their attributes, if their IDs are kept by <aFilter>. Dumps also the attributes content.

        Dumps <aLabel>, its children and their attributes, if their IDs are kept by <aFilter>. Dumps also the attributes content.
        """
    @staticmethod
    @overload
    def ExtendedDeepDump_s(anOS : io.BytesIO,aDF : TDF_Data,aFilter : TDF_IDFilter) -> None: ...
    @staticmethod
    @overload
    def IsSelfContained_s(aLabel : TDF_Label) -> bool: 
        """
        Returns true if <aLabel> and its descendants reference only attributes or labels attached to themselves.

        Returns true if <aLabel> and its descendants reference only attributes or labels attached to themselves and kept by <aFilter>.
        """
    @staticmethod
    @overload
    def IsSelfContained_s(aLabel : TDF_Label,aFilter : TDF_IDFilter) -> bool: ...
    @staticmethod
    @overload
    def Label_s(aDF : TDF_Data,anEntry : OCP.TCollection.TCollection_AsciiString,aLabel : TDF_Label,create : bool=False) -> None: 
        """
        Returns the label expressed by <anEntry>; creates the label if it does not exist and if <create> is true.

        Returns the label expressed by <anEntry>; creates the label if it does not exist and if <create> is true.

        Returns the label expressed by <anEntry>; creates the label if it does not exist and if <create> is true.
        """
    @staticmethod
    @overload
    def Label_s(aDF : TDF_Data,anEntry : str,aLabel : TDF_Label,create : bool=False) -> None: ...
    @staticmethod
    @overload
    def Label_s(aDF : TDF_Data,aTagList : OCP.TColStd.TColStd_ListOfInteger,aLabel : TDF_Label,create : bool=False) -> None: ...
    @staticmethod
    @overload
    def NbAttributes_s(aLabel : TDF_Label,aFilter : TDF_IDFilter) -> int: 
        """
        Returns the total number of attributes attached to the labels dependent on the label aLabel. The attributes of aLabel are also included in this figure. This information is useful in setting the size of an array.

        Returns the number of attributes of the tree, selected by a<Filter>, including those of <aLabel>.
        """
    @staticmethod
    @overload
    def NbAttributes_s(aLabel : TDF_Label) -> int: ...
    @staticmethod
    def NbLabels_s(aLabel : TDF_Label) -> int: 
        """
        Returns the number of labels of the tree, including <aLabel>. aLabel is also included in this figure. This information is useful in setting the size of an array.
        """
    @staticmethod
    @overload
    def OutReferences_s(aLabel : TDF_Label,aFilterForReferers : TDF_IDFilter,aFilterForReferences : TDF_IDFilter,atts : TDF_AttributeMap) -> None: 
        """
        Returns in <atts> the referenced attributes. Caution: <atts> is not cleared before use!

        Returns in <atts> the referenced attributes and kept by <aFilterForReferences>. It considers only the referrers kept by <aFilterForReferers>. Caution: <atts> is not cleared before use!
        """
    @staticmethod
    @overload
    def OutReferences_s(aLabel : TDF_Label,atts : TDF_AttributeMap) -> None: ...
    @staticmethod
    @overload
    def OutReferers_s(theLabel : TDF_Label,theAtts : TDF_AttributeMap) -> None: 
        """
        Returns in <theAtts> the attributes having out references.

        Returns in <atts> the attributes having out references and kept by <aFilterForReferers>. It considers only the references kept by <aFilterForReferences>. Caution: <atts> is not cleared before use!
        """
    @staticmethod
    @overload
    def OutReferers_s(aLabel : TDF_Label,aFilterForReferers : TDF_IDFilter,aFilterForReferences : TDF_IDFilter,atts : TDF_AttributeMap) -> None: ...
    @staticmethod
    def RelocateLabel_s(aSourceLabel : TDF_Label,fromRoot : TDF_Label,toRoot : TDF_Label,aTargetLabel : TDF_Label,create : bool=False) -> None: 
        """
        Returns the label having the same sub-entry as <aLabel> but located as descendant as <toRoot> instead of <fromRoot>.
        """
    @staticmethod
    @overload
    def TagList_s(anEntry : OCP.TCollection.TCollection_AsciiString,aTagList : OCP.TColStd.TColStd_ListOfInteger) -> None: 
        """
        Returns the entry of <aLabel> as list of integers in <aTagList>.

        Returns the entry expressed by <anEntry> as list of integers in <aTagList>.
        """
    @staticmethod
    @overload
    def TagList_s(aLabel : TDF_Label,aTagList : OCP.TColStd.TColStd_ListOfInteger) -> None: ...
    def __init__(self) -> None: ...
    pass
class TDF_Transaction():
    """
    This class offers services to open, commit or abort a transaction in a more secure way than using Data from TDF. If you forget to close a transaction, it will be automatically aborted at the destruction of this object, at the closure of its scope.
    """
    def Abort(self) -> None: 
        """
        Aborts the transactions until AND including the current opened one.
        """
    def Commit(self,withDelta : bool=False) -> TDF_Delta: 
        """
        Commits the transactions until AND including the current opened one.
        """
    def Data(self) -> TDF_Data: 
        """
        Returns the Data from TDF.

        Returns the Data from TDF.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def Initialize(self,aDF : TDF_Data) -> None: 
        """
        Aborts all the transactions on <myDF> and sets <aDF> to build a transaction context on <aDF>, ready to be opened.
        """
    def IsOpen(self) -> bool: 
        """
        Returns true if the transaction is open.

        Returns true if the transaction is open.
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the transaction name.

        Returns the transaction name.
        """
    def Open(self) -> int: 
        """
        If not yet done, opens a new transaction on <myDF>. Returns the index of the just opened transaction.
        """
    def Transaction(self) -> int: 
        """
        Returns the number of the transaction opened by <me>.

        Returns the number of the transaction opened by <me>.
        """
    @overload
    def __init__(self,aName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,aDF : TDF_Data,aName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    pass
TDF_AttributeBackupMsk = 2
TDF_AttributeForgottenMsk = 4
TDF_AttributeValidMsk = 1
TDF_LabelNodeAttModMsk = 1073741824
TDF_LabelNodeFlagsMsk = -536870912
TDF_LabelNodeImportMsk = -2147483648
TDF_LabelNodeMayModMsk = 536870912
