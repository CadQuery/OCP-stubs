import OCP.TDataStd
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.TColStd
import OCP.TCollection
import io
import OCP.NCollection
import OCP.Standard
__all__  = [
"TDataStd",
"TDataStd_AsciiString",
"TDataStd_BooleanArray",
"TDataStd_BooleanList",
"TDataStd_ByteArray",
"TDataStd_ChildNodeIterator",
"TDataStd_GenericExtString",
"TDataStd_Current",
"TDataStd_DataMapOfStringByte",
"TDataStd_DataMapOfStringReal",
"TDataStd_DataMapOfStringString",
"TDataStd_DeltaOnModificationOfByteArray",
"TDataStd_DeltaOnModificationOfExtStringArray",
"TDataStd_DeltaOnModificationOfIntArray",
"TDataStd_DeltaOnModificationOfIntPackedMap",
"TDataStd_DeltaOnModificationOfRealArray",
"TDataStd_GenericEmpty",
"TDataStd_Expression",
"TDataStd_ExtStringArray",
"TDataStd_ExtStringList",
"TDataStd_Directory",
"TDataStd_Comment",
"TDataStd_HDataMapOfStringByte",
"TDataStd_HDataMapOfStringHArray1OfInteger",
"TDataStd_HDataMapOfStringHArray1OfReal",
"TDataStd_HDataMapOfStringInteger",
"TDataStd_HDataMapOfStringReal",
"TDataStd_HDataMapOfStringString",
"TDataStd_LabelArray1",
"TDataStd_IntPackedMap",
"TDataStd_Integer",
"TDataStd_IntegerArray",
"TDataStd_IntegerList",
"TDataStd_HLabelArray1",
"TDataStd_ListOfByte",
"TDataStd_ListOfExtendedString",
"TDataStd_Name",
"TDataStd_NamedData",
"TDataStd_NoteBook",
"TDataStd_Real",
"TDataStd_RealArray",
"TDataStd_RealEnum",
"TDataStd_RealList",
"TDataStd_ReferenceArray",
"TDataStd_ReferenceList",
"TDataStd_Relation",
"TDataStd_Tick",
"TDataStd_TreeNode",
"TDataStd_UAttribute",
"TDataStd_Variable",
"TDataStd_ANGULAR",
"TDataStd_LENGTH",
"TDataStd_SCALAR"
]
class TDataStd():
    """
    This package defines standard attributes for modelling. These allow you to create and modify labels and attributes for many basic data types. Standard topological and visualization attributes have also been created. To find an attribute attached to a specific label, you use the GUID of the type of attribute you are looking for. To do this, first find this information using the method GetID as follows: Standard_GUID anID = MyAttributeClass::GetID(); Then, use the method Find for the label as follows: Standard_Boolean HasAttribute = aLabel.Find(anID,anAttribute); Note For information on the relations between this component of OCAF and the others, refer to the OCAF User's Guide.
    """
    @staticmethod
    def IDList_s(anIDList : OCP.TDF.TDF_IDList) -> None: 
        """
        Appends to <anIDList> the list of the attributes IDs of this package. CAUTION: <anIDList> is NOT cleared before use.
        """
    @staticmethod
    def Print_s(DIM : TDataStd_RealEnum,S : io.BytesIO) -> io.BytesIO: 
        """
        Prints the name of the real dimension <DIM> as a String on the Stream <S> and returns <S>.
        """
    def __init__(self) -> None: ...
    pass
class TDataStd_AsciiString(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Used to define an AsciiString attribute containing a TCollection_AsciiStringUsed to define an AsciiString attribute containing a TCollection_AsciiStringUsed to define an AsciiString attribute containing a TCollection_AsciiString
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods ============= Returns the GUID of the attribute.
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
    def IsEmpty(self) -> bool: 
        """
        None
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
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,S : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit user defined GUID to the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,guid : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,string : OCP.TCollection.TCollection_AsciiString) -> TDataStd_AsciiString: 
        """
        Finds, or creates an AsciiString attribute and sets the string. the AsciiString attribute is returned. AsciiString methods ===================

        Finds, or creates, an AsciiString attribute with explicit user defined <guid> and sets <string>. The Name attribute is returned.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,guid : OCP.Standard.Standard_GUID,string : OCP.TCollection.TCollection_AsciiString) -> TDataStd_AsciiString: ...
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
class TDataStd_BooleanArray(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    An array of boolean values.An array of boolean values.An array of boolean values.
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
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Static methods ============== Returns an ID for array.
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
    def Init(self,lower : int,upper : int) -> None: 
        """
        Initialize the inner array with bounds from <lower> to <upper>
        """
    def InternalArray(self) -> OCP.TColStd.TColStd_HArray1OfByte: 
        """
        None
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
    def Length(self) -> int: 
        """
        Returns the number of elements in the array.
        """
    def Lower(self) -> int: 
        """
        Returns the lower boundary of the array.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: ...
    def SetInternalArray(self,values : OCP.TColStd.TColStd_HArray1OfByte) -> None: 
        """
        None
        """
    def SetValue(self,index : int,value : bool) -> None: 
        """
        Sets the <Index>th element of the array to <Value> OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the internal array.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID,lower : int,upper : int) -> TDataStd_BooleanArray: 
        """
        Finds or creates an attribute with internal boolean array.

        Finds or creates an attribute with the array using explicit user defined <guid>.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,lower : int,upper : int) -> TDataStd_BooleanArray: ...
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
    def Upper(self) -> int: 
        """
        Returns the upper boundary of the array.
        """
    def Value(self,Index : int) -> bool: 
        """
        Return the value of the <Index>th element of the array.
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
class TDataStd_BooleanList(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Contains a list of bolleans.Contains a list of bolleans.Contains a list of bolleans.
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
    def Append(self,value : bool) -> None: 
        """
        None
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
    def Extent(self) -> int: 
        """
        None
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def First(self) -> bool: 
        """
        None
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Static methods ============== Returns the ID of the list of booleans attribute.
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
    def InsertAfter(self,index : int,after_value : bool) -> bool: 
        """
        Inserts the <value> after the <index> position. The indices start with 1 .. Extent().
        """
    def InsertBefore(self,index : int,before_value : bool) -> bool: 
        """
        Inserts the <value> before the <index> position. The indices start with 1 .. Extent().
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
    def Last(self) -> bool: 
        """
        None
        """
    def List(self) -> TDataStd_ListOfByte: 
        """
        1 - means TRUE, 0 - means FALSE.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def Prepend(self,value : bool) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Remove(self,index : int) -> bool: 
        """
        Removes a value at <index> position.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID) -> TDataStd_BooleanList: 
        """
        Finds or creates a list of boolean values attribute.

        Finds or creates a list of boolean values attribute with explicit user defined <guid>.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_BooleanList: ...
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
class TDataStd_ByteArray(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    An array of Byte (unsigned char) values.An array of Byte (unsigned char) values.An array of Byte (unsigned char) values.
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
    def ChangeArray(self,newArray : OCP.TColStd.TColStd_HArray1OfByte,isCheckItems : bool=True) -> None: 
        """
        Sets the inner array <myValue> of the attribute to <newArray>. If value of <newArray> differs from <myValue>, Backup performed and myValue refers to new instance of HArray1OfInteger that holds <newArray> values. If <isCheckItems> equal True each item of <newArray> will be checked with each item of <myValue> for coincidence (to avoid backup).
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
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute>.
        """
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDelta(self) -> bool: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Static methods ============== Returns an ID for array.
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
    def Init(self,lower : int,upper : int) -> None: 
        """
        Initialize the inner array with bounds from <lower> to <upper>
        """
    def InternalArray(self) -> OCP.TColStd.TColStd_HArray1OfByte: 
        """
        None
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
    def Length(self) -> int: 
        """
        Returns the number of elements in the array.
        """
    def Lower(self) -> int: 
        """
        Returns the lower boundary of the array.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetDelta(self,isDelta : bool) -> None: 
        """
        for internal use only!
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self) -> None: ...
    def SetValue(self,index : int,value : int) -> None: 
        """
        Sets the <Index>th element of the array to <Value> OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the internal array.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,lower : int,upper : int,isDelta : bool=False) -> TDataStd_ByteArray: 
        """
        Finds or creates an attribute with the array on the specified label. If <isDelta> == False, DefaultDeltaOnModification is used. If <isDelta> == True, DeltaOnModification of the current attribute is used. If attribute is already set, all input parameters are refused and the found attribute is returned.

        Finds or creates an attribute with byte array and explicit user defined <guid> on the specified label.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID,lower : int,upper : int,isDelta : bool=False) -> TDataStd_ByteArray: ...
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
    def Upper(self) -> int: 
        """
        Returns the upper boundary of the array.
        """
    def Value(self,Index : int) -> int: 
        """
        Return the value of the <Index>th element of the array.
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
class TDataStd_ChildNodeIterator():
    """
    Iterates on the ChildStepren step of a step, at the first level only. It is possible to ask the iterator to explore all the sub step levels of the given one, with the option "allLevels".
    """
    def Initialize(self,aTreeNode : TDataStd_TreeNode,allLevels : bool=False) -> None: 
        """
        Initializes the iteration on the Children Step of the given Step. If <allLevels> option is set to true, it explores not only the first, but all the sub Step levels.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Item in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Item
        """
    def NextBrother(self) -> None: 
        """
        Move to the next Brother. If there is none, go up etc. This method is interesting only with "allLevels" behavior, because it avoids to explore the current Step ChildStepren.
        """
    def Value(self) -> TDataStd_TreeNode: 
        """
        Returns the current item; a null Step if there is no one.
        """
    @overload
    def __init__(self,aTreeNode : TDataStd_TreeNode,allLevels : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TDataStd_GenericExtString(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    An ancestor attibute for all attributes which have TCollection_ExtendedString field. If an attribute inherits this one it should not have drivers for persistence. Also this attribute provides functionality to have on the same label same attributes with different IDs.An ancestor attibute for all attributes which have TCollection_ExtendedString field. If an attribute inherits this one it should not have drivers for persistence. Also this attribute provides functionality to have on the same label same attributes with different IDs.An ancestor attibute for all attributes which have TCollection_ExtendedString field. If an attribute inherits this one it should not have drivers for persistence. Also this attribute provides functionality to have on the same label same attributes with different IDs.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the name contained in this name attribute.
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
        Returns an new empty attribute from the good end type. It is used by the copy algorithm.
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,S : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Sets <S> as name. Raises if <S> is not a valid name.
        """
    def SetID(self,guid : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the explicit user defined GUID to the attribute.
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
class TDataStd_Current(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    this attribute, located at root label, manage an access to a current label.this attribute, located at root label, manage an access to a current label.this attribute, located at root label, manage an access to a current label.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods =============
        """
    def GetLabel(self) -> OCP.TDF.TDF_Label: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        returns current of <acces> Framework. raise if (!Has)
        """
    @staticmethod
    def Has_s(acces : OCP.TDF.TDF_Label) -> bool: 
        """
        returns True if a current label is managed in <acces> Framework. class methods =============
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
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetLabel(self,current : OCP.TDF.TDF_Label) -> None: 
        """
        None
        """
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> None: 
        """
        Set <L> as current of <L> Framework.
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
class TDataStd_DataMapOfStringByte(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDataStd_DataMapOfStringByte) -> TDataStd_DataMapOfStringByte: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_ExtendedString,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_ExtendedString,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> int: 
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
    def Exchange(self,theOther : TDataStd_DataMapOfStringByte) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> int: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_ExtendedString,theValue : int) -> bool: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> bool: 
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
    def Seek(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> int: 
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
    def UnBind(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : TDataStd_DataMapOfStringByte) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDataStd_DataMapOfStringReal(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDataStd_DataMapOfStringReal) -> TDataStd_DataMapOfStringReal: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_ExtendedString,theItem : float) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_ExtendedString,theItem : float) -> float: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> float: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> float: 
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
    def Exchange(self,theOther : TDataStd_DataMapOfStringReal) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_ExtendedString,theValue : float) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> float: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> bool: 
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
    def Seek(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> float: 
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
    def UnBind(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TDataStd_DataMapOfStringReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDataStd_DataMapOfStringString(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TDataStd_DataMapOfStringString) -> TDataStd_DataMapOfStringString: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_ExtendedString,theItem : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_ExtendedString,theItem : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def Exchange(self,theOther : TDataStd_DataMapOfStringString) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_ExtendedString,theValue : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> bool: 
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
    def Seek(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def UnBind(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TDataStd_DataMapOfStringString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDataStd_DeltaOnModificationOfByteArray(OCP.TDF.TDF_DeltaOnModification, OCP.TDF.TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> OCP.TDF.TDF_Attribute: 
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
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Arr : TDataStd_ByteArray) -> None: ...
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
class TDataStd_DeltaOnModificationOfExtStringArray(OCP.TDF.TDF_DeltaOnModification, OCP.TDF.TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> OCP.TDF.TDF_Attribute: 
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
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Arr : TDataStd_ExtStringArray) -> None: ...
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
class TDataStd_DeltaOnModificationOfIntArray(OCP.TDF.TDF_DeltaOnModification, OCP.TDF.TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> OCP.TDF.TDF_Attribute: 
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
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Arr : TDataStd_IntegerArray) -> None: ...
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
class TDataStd_DeltaOnModificationOfIntPackedMap(OCP.TDF.TDF_DeltaOnModification, OCP.TDF.TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> OCP.TDF.TDF_Attribute: 
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
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Arr : TDataStd_IntPackedMap) -> None: ...
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
class TDataStd_DeltaOnModificationOfRealArray(OCP.TDF.TDF_DeltaOnModification, OCP.TDF.TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on a MODIFICATION actionThis class provides default services for an AttributeDelta on a MODIFICATION actionThis class provides default services for an AttributeDelta on a MODIFICATION action
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> OCP.TDF.TDF_Attribute: 
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
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Arr : TDataStd_RealArray) -> None: ...
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
class TDataStd_GenericEmpty(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    An ancestor attibute for all attributes which have no fields. If an attribute inherits this one it should not have drivers for persistence.An ancestor attibute for all attributes which have no fields. If an attribute inherits this one it should not have drivers for persistence.An ancestor attibute for all attributes which have no fields. If an attribute inherits this one it should not have drivers for persistence.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
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
        Returns an new empty attribute from the good end type. It is used by the copy algorithm.
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
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
class TDataStd_Expression(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Expression attribute. ====================Expression attribute. ====================Expression attribute. ====================
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetExpression(self) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def GetVariables(self) -> OCP.TDF.TDF_AttributeList: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        build and return the expression name
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
    def SetExpression(self,E : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
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
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_Expression: 
        """
        Find, or create, an Expression attribute. Expressionmethods ============
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
class TDataStd_ExtStringArray(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    ExtStringArray Attribute. Handles an array of UNICODE strings (represented by the TCollection_ExtendedString class).ExtStringArray Attribute. Handles an array of UNICODE strings (represented by the TCollection_ExtendedString class).ExtStringArray Attribute. Handles an array of UNICODE strings (represented by the TCollection_ExtendedString class).
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
    def Array(self) -> OCP.TColStd.TColStd_HArray1OfExtendedString: 
        """
        Return the inner array of the ExtStringArray attribute
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
    def ChangeArray(self,newArray : OCP.TColStd.TColStd_HArray1OfExtendedString,isCheckItems : bool=True) -> None: 
        """
        Sets the inner array <myValue> of the ExtStringArray attribute to <newArray>. If value of <newArray> differs from <myValue>, Backup performed and myValue refers to new instance of HArray1OfExtendedString that holds <newArray> values If <isCheckItems> equal True each item of <newArray> will be checked with each item of <myValue> for coincidence (to avoid backup).
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
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute>.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDelta(self) -> bool: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods ============= Returns the GUID for the attribute.
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
    def Init(self,lower : int,upper : int) -> None: 
        """
        Initializes the inner array with bounds from <lower> to <upper>
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
    def Length(self) -> int: 
        """
        Return the number of elements of <me>.
        """
    def Lower(self) -> int: 
        """
        Return the lower bound.
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
    def SetDelta(self,isDelta : bool) -> None: 
        """
        for internal use only!
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self) -> None: ...
    def SetValue(self,Index : int,Value : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Sets the <Index>th element of the array to <Value> OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the internal array.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,lower : int,upper : int,isDelta : bool=False) -> TDataStd_ExtStringArray: 
        """
        Finds, or creates, an ExtStringArray attribute with <lower> and <upper> bounds on the specified label. If <isDelta> == False, DefaultDeltaOnModification is used. If <isDelta> == True, DeltaOnModification of the current attribute is used. If attribute is already set, all input parameters are refused and the found attribute is returned.

        Finds, or creates, an ExtStringArray attribute with explicit user defined <guid>. The ExtStringArray attribute is returned.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID,lower : int,upper : int,isDelta : bool=False) -> TDataStd_ExtStringArray: ...
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
    def Upper(self) -> int: 
        """
        Return the upper bound
        """
    def Value(self,Index : int) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the value of the <Index>th element of the array
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
class TDataStd_ExtStringList(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Contains a list of ExtendedString.Contains a list of ExtendedString.Contains a list of ExtendedString.
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
    def Append(self,value : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
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
    def Extent(self) -> int: 
        """
        None
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def First(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Static methods ============== Returns the ID of the list of strings attribute.
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
    @overload
    def InsertAfter(self,index : int,after_value : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Inserts the <value> after the first meet of <after_value>.

        Inserts the <value> after the <index> position. The indices start with 1 .. Extent().
        """
    @overload
    def InsertAfter(self,value : OCP.TCollection.TCollection_ExtendedString,after_value : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    @overload
    def InsertBefore(self,value : OCP.TCollection.TCollection_ExtendedString,before_value : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Inserts the <value> before the first meet of <before_value>.

        Inserts the <value> before the <index> position. The indices start with 1 .. Extent().
        """
    @overload
    def InsertBefore(self,index : int,before_value : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
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
    def Last(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def List(self) -> TDataStd_ListOfExtendedString: 
        """
        None
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def Prepend(self,value : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    @overload
    def Remove(self,index : int) -> bool: 
        """
        Removes the first meet of the <value>.

        Removes a value at <index> position.
        """
    @overload
    def Remove(self,value : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID) -> TDataStd_ExtStringList: 
        """
        Finds or creates a list of string values attribute with explicit user defined <guid>.

        Finds or creates a list of string values attribute.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_ExtStringList: ...
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
class TDataStd_Directory(TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Associates a directory in the data framework with a TDataStd_TagSource attribute. You can create a new directory label and add sub-directory or object labels to it,Associates a directory in the data framework with a TDataStd_TagSource attribute. You can create a new directory label and add sub-directory or object labels to it,Associates a directory in the data framework with a TDataStd_TagSource attribute. You can create a new directory label and add sub-directory or object labels to it,
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    @staticmethod
    def AddDirectory_s(dir : TDataStd_Directory) -> TDataStd_Directory: 
        """
        Creates a new sub-label and sets the sub-directory dir on that label.
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
    @staticmethod
    def Find_s(current : OCP.TDF.TDF_Label,D : TDataStd_Directory) -> bool: 
        """
        class methods ============= Searches for a directory attribute on the label current, or on one of the father labels of current. If a directory attribute is found, true is returned, and the attribute found is set as D.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Directory methods ===============
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
    @staticmethod
    def MakeObjectLabel_s(dir : TDataStd_Directory) -> OCP.TDF.TDF_Label: 
        """
        Makes new label and returns it to insert other object attributes (sketch,part...etc...)
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    @staticmethod
    def New_s(label : OCP.TDF.TDF_Label) -> TDataStd_Directory: 
        """
        Creates an empty Directory attribute, located at <label>. Raises if <label> has attribute
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
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
class TDataStd_Comment(TDataStd_GenericExtString, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Comment attribute. may be associated to any label to store user comment.Comment attribute. may be associated to any label to store user comment.Comment attribute. may be associated to any label to store user comment.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the name contained in this name attribute.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods ============= Returns the GUID for comments.
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
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,S : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    @overload
    def SetID(self,guid : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the explicit user defined GUID to the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,string : OCP.TCollection.TCollection_ExtendedString) -> TDataStd_Comment: 
        """
        Find, or create a Comment attribute. the Comment attribute is returned.

        Finds, or creates a Comment attribute and sets the string. the Comment attribute is returned. Comment methods ============
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_Comment: ...
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
class TDataStd_HDataMapOfStringByte(OCP.Standard.Standard_Transient):
    """
    Extension of TDataStd_DataMapOfStringByte class to be manipulated by handle.Extension of TDataStd_DataMapOfStringByte class to be manipulated by handle.
    """
    def ChangeMap(self) -> TDataStd_DataMapOfStringByte: 
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
    def Map(self) -> TDataStd_DataMapOfStringByte: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOther : TDataStd_DataMapOfStringByte) -> None: ...
    @overload
    def __init__(self,NbBuckets : int=1) -> None: ...
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
class TDataStd_HDataMapOfStringHArray1OfInteger(OCP.Standard.Standard_Transient):
    """
    Extension of TDataStd_DataMapOfStringHArray1OfInteger class to be manipulated by handle.Extension of TDataStd_DataMapOfStringHArray1OfInteger class to be manipulated by handle.
    """
    def ChangeMap(self) -> Any: 
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
    def Map(self) -> Any: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,NbBuckets : int=1) -> None: ...
    @overload
    def __init__(self,theOther : Any) -> None: ...
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
class TDataStd_HDataMapOfStringHArray1OfReal(OCP.Standard.Standard_Transient):
    """
    Extension of TDataStd_DataMapOfStringHArray1OfReal class to be manipulated by handle.Extension of TDataStd_DataMapOfStringHArray1OfReal class to be manipulated by handle.
    """
    def ChangeMap(self) -> Any: 
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
    def Map(self) -> Any: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,NbBuckets : int=1) -> None: ...
    @overload
    def __init__(self,theOther : Any) -> None: ...
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
class TDataStd_HDataMapOfStringInteger(OCP.Standard.Standard_Transient):
    """
    Extension of TColStd_DataMapOfStringInteger class to be manipulated by handle.Extension of TColStd_DataMapOfStringInteger class to be manipulated by handle.
    """
    def ChangeMap(self) -> OCP.TColStd.TColStd_DataMapOfStringInteger: 
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
    def Map(self) -> OCP.TColStd.TColStd_DataMapOfStringInteger: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOther : OCP.TColStd.TColStd_DataMapOfStringInteger) -> None: ...
    @overload
    def __init__(self,NbBuckets : int=1) -> None: ...
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
class TDataStd_HDataMapOfStringReal(OCP.Standard.Standard_Transient):
    """
    Extension of TDataStd_DataMapOfStringReal class to be manipulated by handle.Extension of TDataStd_DataMapOfStringReal class to be manipulated by handle.
    """
    def ChangeMap(self) -> TDataStd_DataMapOfStringReal: 
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
    def Map(self) -> TDataStd_DataMapOfStringReal: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,NbBuckets : int=1) -> None: ...
    @overload
    def __init__(self,theOther : TDataStd_DataMapOfStringReal) -> None: ...
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
class TDataStd_HDataMapOfStringString(OCP.Standard.Standard_Transient):
    """
    Extension of TDataStd_DataMapOfStringString class to be manipulated by handle.Extension of TDataStd_DataMapOfStringString class to be manipulated by handle.
    """
    def ChangeMap(self) -> TDataStd_DataMapOfStringString: 
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
    def Map(self) -> TDataStd_DataMapOfStringString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOther : TDataStd_DataMapOfStringString) -> None: ...
    @overload
    def __init__(self,NbBuckets : int=1) -> None: ...
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
class TDataStd_LabelArray1():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TDataStd_LabelArray1) -> TDataStd_LabelArray1: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.TDF.TDF_Label: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TDF.TDF_Label: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TDF.TDF_Label: 
        """
        Variable value access
        """
    def First(self) -> OCP.TDF.TDF_Label: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.TDF.TDF_Label) -> None: 
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
    def Last(self) -> OCP.TDF.TDF_Label: 
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
    def Move(self,theOther : TDataStd_LabelArray1) -> TDataStd_LabelArray1: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TDF.TDF_Label) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TDF.TDF_Label: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TDataStd_LabelArray1) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.TDF.TDF_Label,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDataStd_IntPackedMap(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Attribute for storing TColStd_PackedMapOfIntegerAttribute for storing TColStd_PackedMapOfIntegerAttribute for storing TColStd_PackedMapOfInteger
    """
    def Add(self,theKey : int) -> bool: 
        """
        None
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
    @overload
    def ChangeMap(self,theMap : OCP.TColStd.TColStd_PackedMapOfInteger) -> bool: 
        """
        None

        None
        """
    @overload
    def ChangeMap(self,theMap : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    def Clear(self) -> bool: 
        """
        None
        """
    def Contains(self,theKey : int) -> bool: 
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
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute>.
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
    def Extent(self) -> int: 
        """
        None
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDelta(self) -> bool: 
        """
        None
        """
    def GetHMap(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods ============= Returns the GUID of the attribute.
        """
    def GetMap(self) -> OCP.TColStd.TColStd_PackedMapOfInteger: 
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
    def IsEmpty(self) -> bool: 
        """
        None
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
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Remove(self,theKey : int) -> bool: 
        """
        None
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetDelta(self,isDelta : bool) -> None: 
        """
        for internal use only!
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
    def Set_s(label : OCP.TDF.TDF_Label,isDelta : bool=False) -> TDataStd_IntPackedMap: 
        """
        Finds or creates an integer map attribute on the given label. If <isDelta> == False, DefaultDeltaOnModification is used. If <isDelta> == True, DeltaOnModification of the current attribute is used. If attribute is already set, input parameter <isDelta> is refused and the found attribute returned. Attribute methods ===================
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
class TDataStd_Integer(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    The basis to define an integer attribute.The basis to define an integer attribute.The basis to define an integer attribute.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> int: 
        """
        Returns the integer value contained in the attribute.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods ============= Returns the GUID for integers.
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
    def IsCaptured(self) -> bool: 
        """
        Returns True if there is a reference on the same label
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
    def Set(self,V : int) -> None: 
        """
        Integer methods ===============
        """
    @overload
    def SetID(self,guid : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,value : int) -> TDataStd_Integer: 
        """
        Finds, or creates, an Integer attribute and sets <value> the Integer attribute is returned.

        Finds, or creates, an Integer attribute with explicit user defined <guid> and sets <value>. The Integer attribute is returned.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,guid : OCP.Standard.Standard_GUID,value : int) -> TDataStd_Integer: ...
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
class TDataStd_IntegerArray(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Contains an array of integers.Contains an array of integers.Contains an array of integers.
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
    def Array(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Return the inner array of the IntegerArray attribute
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
    def ChangeArray(self,newArray : OCP.TColStd.TColStd_HArray1OfInteger,isCheckItems : bool=True) -> None: 
        """
        Sets the inner array <myValue> of the IntegerArray attribute to <newArray>. If value of <newArray> differs from <myValue>, Backup performed and myValue refers to new instance of HArray1OfInteger that holds <newArray> values If <isCheckItems> equal True each item of <newArray> will be checked with each item of <myValue> for coincidence (to avoid backup).
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
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute>.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDelta(self) -> bool: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods ============= Returns the GUID for arrays of integers.
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
    def Init(self,lower : int,upper : int) -> None: 
        """
        Initialize the inner array with bounds from <lower> to <upper>
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
    def Length(self) -> int: 
        """
        Returns the length of this array of integers in terms of the number of elements it contains.
        """
    def Lower(self) -> int: 
        """
        Returns the lower boundary of this array of integers.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Note. Uses inside ChangeArray() method
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetDelta(self,isDelta : bool) -> None: 
        """
        for internal use only!
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self) -> None: ...
    def SetValue(self,Index : int,Value : int) -> None: 
        """
        Sets the <Index>th element of the array to <Value> OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the internal array.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID,lower : int,upper : int,isDelta : bool=False) -> TDataStd_IntegerArray: 
        """
        Finds or creates on the <label> an integer array attribute with the specified <lower> and <upper> boundaries. If <isDelta> == False, DefaultDeltaOnModification is used. If <isDelta> == True, DeltaOnModification of the current attribute is used. If attribute is already set, all input parameters are refused and the found attribute is returned.

        Finds, or creates, an IntegerArray attribute with explicit user defined <guid>. The IntegerArray attribute is returned.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,lower : int,upper : int,isDelta : bool=False) -> TDataStd_IntegerArray: ...
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
    def Upper(self) -> int: 
        """
        Return the upper boundary of this array of integers.
        """
    def Value(self,Index : int) -> int: 
        """
        Return the value of the <Index>th element of the array
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
class TDataStd_IntegerList(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Contains a list of integers.Contains a list of integers.Contains a list of integers.
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
    def Append(self,value : int) -> None: 
        """
        None
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
    def Extent(self) -> int: 
        """
        None
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def First(self) -> int: 
        """
        None
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Static methods ============== Returns the ID of the list of integer attribute.
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
    def InsertAfter(self,value : int,after_value : int) -> bool: 
        """
        Inserts the <value> after the first meet of <after_value>.
        """
    def InsertAfterByIndex(self,index : int,after_value : int) -> bool: 
        """
        Inserts the <value> after the <index> position. The indices start with 1 .. Extent().
        """
    def InsertBefore(self,value : int,before_value : int) -> bool: 
        """
        Inserts the <value> before the first meet of <before_value>.
        """
    def InsertBeforeByIndex(self,index : int,before_value : int) -> bool: 
        """
        Inserts the <value> before the <index> position. The indices start with 1 .. Extent().
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
    def Last(self) -> int: 
        """
        None
        """
    def List(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        None
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def Prepend(self,value : int) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Remove(self,value : int) -> bool: 
        """
        Removes the first meet of the <value>.
        """
    def RemoveByIndex(self,index : int) -> bool: 
        """
        Removes a value at <index> position.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_IntegerList: 
        """
        Finds or creates a list of integer values attribute.

        Finds or creates a list of integer values attribute with explicit user defined <guid>.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID) -> TDataStd_IntegerList: ...
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
class TDataStd_HLabelArray1(TDataStd_LabelArray1, OCP.Standard.Standard_Transient):
    def Array1(self) -> TDataStd_LabelArray1: 
        """
        None
        """
    def Assign(self,theOther : TDataStd_LabelArray1) -> TDataStd_LabelArray1: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TDataStd_LabelArray1: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.TDF.TDF_Label: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TDF.TDF_Label: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TDF.TDF_Label: 
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
    def First(self) -> OCP.TDF.TDF_Label: 
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
    def Init(self,theValue : OCP.TDF.TDF_Label) -> None: 
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
    def Last(self) -> OCP.TDF.TDF_Label: 
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
    def Move(self,theOther : TDataStd_LabelArray1) -> TDataStd_LabelArray1: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TDF.TDF_Label) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TDF.TDF_Label: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : TDataStd_LabelArray1) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class TDataStd_ListOfByte(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : int) -> int: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : int,theIter : Any) -> None: ...
    @overload
    def Append(self,theOther : TDataStd_ListOfByte) -> None: ...
    def Assign(self,theOther : TDataStd_ListOfByte) -> TDataStd_ListOfByte: 
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
    def First(self) -> int: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TDataStd_ListOfByte,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : int,theIter : Any) -> int: ...
    @overload
    def InsertBefore(self,theItem : int,theIter : Any) -> int: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TDataStd_ListOfByte,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> int: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TDataStd_ListOfByte) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : int) -> int: ...
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
    def __init__(self,theOther : TDataStd_ListOfByte) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDataStd_ListOfExtendedString(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : TDataStd_ListOfExtendedString) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_ExtendedString,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: ...
    def Assign(self,theOther : TDataStd_ListOfExtendedString) -> TDataStd_ListOfExtendedString: 
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
    def First(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TDataStd_ListOfExtendedString,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OCP.TCollection.TCollection_ExtendedString,theIter : Any) -> OCP.TCollection.TCollection_ExtendedString: ...
    @overload
    def InsertBefore(self,theOther : TDataStd_ListOfExtendedString,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : OCP.TCollection.TCollection_ExtendedString,theIter : Any) -> OCP.TCollection.TCollection_ExtendedString: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TDataStd_ListOfExtendedString) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: ...
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
    def __init__(self,theOther : TDataStd_ListOfExtendedString) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TDataStd_Name(TDataStd_GenericExtString, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Used to define a name attribute containing a string which specifies the name.Used to define a name attribute containing a string which specifies the name.Used to define a name attribute containing a string which specifies the name.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the name contained in this name attribute.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods working on the name itself ======================================== Returns the GUID for name attributes.
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
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,S : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Sets <S> as name. Raises if <S> is not a valid name.
        """
    @overload
    def SetID(self,guid : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the explicit user defined GUID to the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,guid : OCP.Standard.Standard_GUID,string : OCP.TCollection.TCollection_ExtendedString) -> TDataStd_Name: 
        """
        Finds, or creates, a Name attribute with explicit user defined <guid> and sets <string>. The Name attribute is returned.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,string : OCP.TCollection.TCollection_ExtendedString) -> TDataStd_Name: ...
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
class TDataStd_NamedData(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Contains a named data.Contains a named data.Contains a named data.
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
    def ChangeArraysOfIntegers(self,theArraysOfIntegers : Any) -> None: 
        """
        Replace the container content by new content of the <theArraysOfIntegers>.
        """
    def ChangeArraysOfReals(self,theArraysOfReals : Any) -> None: 
        """
        Replace the container content by new content of the <theArraysOfReals>.
        """
    def ChangeBytes(self,theBytes : TDataStd_DataMapOfStringByte) -> None: 
        """
        Replace the container content by new content of the <theBytes>.
        """
    def ChangeIntegers(self,theIntegers : OCP.TColStd.TColStd_DataMapOfStringInteger) -> None: 
        """
        Replace the container content by new content of the <theIntegers>.
        """
    def ChangeReals(self,theReals : TDataStd_DataMapOfStringReal) -> None: 
        """
        Replace the container content by new content of the <theReals>.
        """
    def ChangeStrings(self,theStrings : TDataStd_DataMapOfStringString) -> None: 
        """
        Replace the container content by new content of the <theStrings>.
        """
    def Clear(self) -> None: 
        """
        Clear data.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetArrayOfIntegers(self,theName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Returns the named array of integer values. It returns a NULL Handle if there is no such a named array of integers (use HasArrayOfIntegers()).
        """
    def GetArrayOfReals(self,theName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the named array of real values. It returns a NULL Handle if there is no such a named array of reals (use HasArrayOfReals()).
        """
    def GetArraysOfIntegersContainer(self) -> Any: 
        """
        Returns the internal container of named arrays of integer values.
        """
    def GetArraysOfRealsContainer(self) -> Any: 
        """
        Returns the internal container of named arrays of real values.
        """
    def GetByte(self,theName : OCP.TCollection.TCollection_ExtendedString) -> int: 
        """
        Returns the named byte. It returns 0 if there is no such a named byte (use HasByte()).
        """
    def GetBytesContainer(self) -> TDataStd_DataMapOfStringByte: 
        """
        Returns the internal container of named bytes.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the named data attribute.
        """
    def GetInteger(self,theName : OCP.TCollection.TCollection_ExtendedString) -> int: 
        """
        Returns the integer value specified by the Name. It returns 0 if internal map doesn't contain the specified integer (use HasInteger() to check before).
        """
    def GetIntegersContainer(self) -> OCP.TColStd.TColStd_DataMapOfStringInteger: 
        """
        Returns the internal container of named integers.
        """
    def GetReal(self,theName : OCP.TCollection.TCollection_ExtendedString) -> float: 
        """
        Returns the named real. It returns 0.0 if there is no such a named real (use HasReal()).
        """
    def GetRealsContainer(self) -> TDataStd_DataMapOfStringReal: 
        """
        Returns the internal container of named reals.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetString(self,theName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the named string. It returns an empty string if there is no such a named string (use HasString()).
        """
    def GetStringsContainer(self) -> TDataStd_DataMapOfStringString: 
        """
        Returns the internal container of named strings.
        """
    def HasArrayOfIntegers(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Returns true if the attribute contains this named array of integer values.
        """
    def HasArrayOfReals(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Returns true if the attribute contains this named array of real values.
        """
    def HasArraysOfIntegers(self) -> bool: 
        """
        Returns true if there are some named arrays of integer values in the attribute.
        """
    def HasArraysOfReals(self) -> bool: 
        """
        Returns true if there are some named arrays of real values in the attribute.
        """
    def HasByte(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Returns true if the attribute contains this named byte.
        """
    def HasBytes(self) -> bool: 
        """
        Returns true if there are some named bytes in the attribute.
        """
    def HasDeferredData(self) -> bool: 
        """
        Returns TRUE if some data is not loaded from deferred storage and can be loaded using LoadDeferredData().
        """
    def HasInteger(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Returns true if the attribute contains specified by Name integer value.
        """
    def HasIntegers(self) -> bool: 
        """
        Returns true if at least one named integer value is kept in the attribute.
        """
    def HasReal(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Returns true if the attribute contains a real specified by Name.
        """
    def HasReals(self) -> bool: 
        """
        Returns true if at least one named real value is kept in the attribute.
        """
    def HasString(self,theName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Returns true if the attribute contains this named string.
        """
    def HasStrings(self) -> bool: 
        """
        Returns true if there are some named strings in the attribute.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: ...
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
    def LoadDeferredData(self,theToKeepDeferred : bool=False) -> bool: 
        """
        Load data from deferred storage, without calling Backup(). As result, the content of the object will be overidden by data from deferred storage (which is normally read-only).
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
    def SetArrayOfIntegers(self,theName : OCP.TCollection.TCollection_ExtendedString,theArrayOfIntegers : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        Defines a named array of integer values.
        """
    def SetArrayOfReals(self,theName : OCP.TCollection.TCollection_ExtendedString,theArrayOfReals : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Defines a named array of real values.
        """
    def SetByte(self,theName : OCP.TCollection.TCollection_ExtendedString,theByte : int) -> None: 
        """
        Defines a named byte. If the byte already exists, it changes its value to <theByte>.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetInteger(self,theName : OCP.TCollection.TCollection_ExtendedString,theInteger : int) -> None: 
        """
        Defines a named integer. If the integer already exists, it changes its value to <theInteger>.
        """
    def SetReal(self,theName : OCP.TCollection.TCollection_ExtendedString,theReal : float) -> None: 
        """
        Defines a named real. If the real already exists, it changes its value to <theReal>.
        """
    def SetString(self,theName : OCP.TCollection.TCollection_ExtendedString,theString : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Defines a named string. If the string already exists, it changes its value to <theString>.
        """
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_NamedData: 
        """
        Finds or creates a named data attribute.
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
    def UnloadDeferredData(self) -> bool: 
        """
        Releases data if object has connected deferred storage, without calling Backup(). WARNING! This operation does not unload modifications to deferred storage (normally it is read-only), so that modifications will be discarded (if any).
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
    def clear(self) -> None: 
        """
        Clear data without calling Backup().
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
    def setArrayOfIntegers(self,theName : OCP.TCollection.TCollection_ExtendedString,theArrayOfIntegers : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        Defines a named array of integer values (without calling Backup).
        """
    def setArrayOfReals(self,theName : OCP.TCollection.TCollection_ExtendedString,theArrayOfReals : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Defines a named array of real values (without calling Backup).
        """
    def setByte(self,theName : OCP.TCollection.TCollection_ExtendedString,theByte : int) -> None: 
        """
        Defines a named byte (without calling Backup).
        """
    def setInteger(self,theName : OCP.TCollection.TCollection_ExtendedString,theInteger : int) -> None: 
        """
        Defines a named integer (without calling Backup).
        """
    def setReal(self,theName : OCP.TCollection.TCollection_ExtendedString,theReal : float) -> None: 
        """
        Defines a named real (without calling Backup).
        """
    def setString(self,theName : OCP.TCollection.TCollection_ExtendedString,theString : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Defines a named string (without calling Backup).
        """
    pass
class TDataStd_NoteBook(TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    NoteBook Object attributeNoteBook Object attributeNoteBook Object attribute
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
    @overload
    def Append(self,value : float,isExported : bool=False) -> TDataStd_Real: 
        """
        Tool to Create an Integer attribute from <value>, Insert it in a new son label of <me>. The Real attribute is returned.

        Tool to Create an Real attribute from <value>, Insert it in a new son label of <me>. The Integer attribute is returned.
        """
    @overload
    def Append(self,value : int,isExported : bool=False) -> TDataStd_Integer: ...
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
    @staticmethod
    def Find_s(current : OCP.TDF.TDF_Label,N : TDataStd_NoteBook) -> bool: 
        """
        class methods ============= try to retrieve a NoteBook attribute at <current> label or in fathers label of <current>. Returns True if found and set <N>.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        NoteBook methods ===============
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
        None
        """
    @staticmethod
    def New_s(label : OCP.TDF.TDF_Label) -> TDataStd_NoteBook: 
        """
        Create an enpty NoteBook attribute, located at <label>. Raises if <label> has attribute
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
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
class TDataStd_Real(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    The basis to define a real number attribute.The basis to define a real number attribute.The basis to define a real number attribute.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> float: 
        """
        Returns the real number value contained in the attribute.
        """
    def GetDimension(self) -> TDataStd_RealEnum: 
        """
        Obsolete method that will be removed in next versions. This field is not supported in the persistence mechanism.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods ============= Returns the default GUID for real numbers.
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
    def IsCaptured(self) -> bool: 
        """
        Returns True if there is a reference on the same label
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
    def Set(self,V : float) -> None: 
        """
        Sets the real number V.
        """
    def SetDimension(self,DIM : TDataStd_RealEnum) -> None: 
        """
        Obsolete method that will be removed in next versions. This field is not supported in the persistence mechanism.
        """
    @overload
    def SetID(self,guid : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the explicit GUID for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,value : float) -> TDataStd_Real: 
        """
        Finds, or creates, a Real attribute with default GUID and sets <value>. The Real attribute is returned. The Real dimension is Scalar by default. Use SetDimension to overwrite. Real methods ============

        Finds, or creates, a Real attribute with explicit GUID and sets <value>. The Real attribute is returned. Real methods ============
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,guid : OCP.Standard.Standard_GUID,value : float) -> TDataStd_Real: ...
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
class TDataStd_RealArray(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    A framework for an attribute composed of a real number array.A framework for an attribute composed of a real number array.A framework for an attribute composed of a real number array.
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
    def Array(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the handle of this array of reals.
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
    def ChangeArray(self,newArray : OCP.TColStd.TColStd_HArray1OfReal,isCheckItems : bool=True) -> None: 
        """
        Sets the inner array <myValue> of the RealArray attribute to <newArray>. If value of <newArray> differs from <myValue>, Backup performed and myValue refers to new instance of HArray1OfReal that holds <newArray> values If <isCheckItems> equal True each item of <newArray> will be checked with each item of <myValue> for coincidence (to avoid backup).
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
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute>.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDelta(self) -> bool: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods ============= Returns the GUID for arrays of reals.
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
    def Init(self,lower : int,upper : int) -> None: 
        """
        Initialize the inner array with bounds from <lower> to <upper>
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
    def Length(self) -> int: 
        """
        Returns the number of elements of the array of reals in terms of the number of elements it contains.
        """
    def Lower(self) -> int: 
        """
        Returns the lower boundary of the array.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Note. Uses inside ChangeArray() method
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetDelta(self,isDelta : bool) -> None: 
        """
        for internal use only!
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: ...
    def SetValue(self,Index : int,Value : float) -> None: 
        """
        Sets the <Index>th element of the array to <Value> OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the internal array.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID,lower : int,upper : int,isDelta : bool=False) -> TDataStd_RealArray: 
        """
        Finds or creates on the <label> a real array attribute with the specified <lower> and <upper> boundaries. If <isDelta> == False, DefaultDeltaOnModification is used. If <isDelta> == True, DeltaOnModification of the current attribute is used. If attribute is already set, input parameter <isDelta> is refused and the found attribute returned.

        Finds, or creates, an RealArray attribute with explicit user defined <guid>. The RealArray attribute is returned.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,lower : int,upper : int,isDelta : bool=False) -> TDataStd_RealArray: ...
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
    def Upper(self) -> int: 
        """
        Returns the upper boundary of the array.
        """
    def Value(self,Index : int) -> float: 
        """
        Return the value of the <Index>th element of the array
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
class TDataStd_RealEnum():
    """
    The terms of this enumeration define the semantics of a real number value.

    Members:

      TDataStd_SCALAR

      TDataStd_LENGTH

      TDataStd_ANGULAR
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
    TDataStd_ANGULAR: OCP.TDataStd.TDataStd_RealEnum # value = <TDataStd_RealEnum.TDataStd_ANGULAR: 2>
    TDataStd_LENGTH: OCP.TDataStd.TDataStd_RealEnum # value = <TDataStd_RealEnum.TDataStd_LENGTH: 1>
    TDataStd_SCALAR: OCP.TDataStd.TDataStd_RealEnum # value = <TDataStd_RealEnum.TDataStd_SCALAR: 0>
    __entries: dict # value = {'TDataStd_SCALAR': (<TDataStd_RealEnum.TDataStd_SCALAR: 0>, None), 'TDataStd_LENGTH': (<TDataStd_RealEnum.TDataStd_LENGTH: 1>, None), 'TDataStd_ANGULAR': (<TDataStd_RealEnum.TDataStd_ANGULAR: 2>, None)}
    __members__: dict # value = {'TDataStd_SCALAR': <TDataStd_RealEnum.TDataStd_SCALAR: 0>, 'TDataStd_LENGTH': <TDataStd_RealEnum.TDataStd_LENGTH: 1>, 'TDataStd_ANGULAR': <TDataStd_RealEnum.TDataStd_ANGULAR: 2>}
    pass
class TDataStd_RealList(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Contains a list of doubles.Contains a list of doubles.Contains a list of doubles.
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
    def Append(self,value : float) -> None: 
        """
        None
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
    def Extent(self) -> int: 
        """
        None
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def First(self) -> float: 
        """
        None
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Static methods ============== Returns the ID of the list of doubles attribute.
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
    def InsertAfter(self,value : float,after_value : float) -> bool: 
        """
        Inserts the <value> after the first meet of <after_value>.
        """
    def InsertAfterByIndex(self,index : int,after_value : float) -> bool: 
        """
        Inserts the <value> after the <index> position. The indices start with 1 .. Extent().
        """
    def InsertBefore(self,value : float,before_value : float) -> bool: 
        """
        Inserts the <value> before the first meet of <before_value>.
        """
    def InsertBeforeByIndex(self,index : int,before_value : float) -> bool: 
        """
        Inserts the <value> before the <index> position. The indices start with 1 .. Extent().
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
    def Last(self) -> float: 
        """
        None
        """
    def List(self) -> OCP.TColStd.TColStd_ListOfReal: 
        """
        None
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def Prepend(self,value : float) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Remove(self,value : float) -> bool: 
        """
        Removes the first meet of the <value>.
        """
    def RemoveByIndex(self,index : int) -> bool: 
        """
        Removes a value at <index> position.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_RealList: 
        """
        Finds or creates a list of double values attribute.

        Finds or creates a list of double values attribute with explicit user defined <guid>.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID) -> TDataStd_RealList: ...
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
class TDataStd_ReferenceArray(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Contains an array of references to the labels.Contains an array of references to the labels.Contains an array of references to the labels.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Static methods ============== Returns the ID of the array of references (labels) attribute.
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
    def Init(self,lower : int,upper : int) -> None: 
        """
        Initialize the inner array with bounds from <lower> to <upper>
        """
    def InternalArray(self) -> TDataStd_HLabelArray1: 
        """
        None
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
    def Length(self) -> int: 
        """
        Returns the number of elements in the array.
        """
    def Lower(self) -> int: 
        """
        Returns the lower boundary of the array.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,DS : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: ...
    def SetInternalArray(self,values : TDataStd_HLabelArray1,isCheckItems : bool=True) -> None: 
        """
        None
        """
    def SetValue(self,index : int,value : OCP.TDF.TDF_Label) -> None: 
        """
        Sets the <Index>th element of the array to <Value> OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the internal array.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID,lower : int,upper : int) -> TDataStd_ReferenceArray: 
        """
        Finds or creates an array of reference values (labels) attribute.

        Finds or creates an array of reference values (labels) attribute with explicit user defined <guid>.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,lower : int,upper : int) -> TDataStd_ReferenceArray: ...
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
    def Upper(self) -> int: 
        """
        Returns the upper boundary of the array.
        """
    def Value(self,Index : int) -> OCP.TDF.TDF_Label: 
        """
        Returns the value of the <Index>th element of the array.
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
class TDataStd_ReferenceList(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Contains a list of references.Contains a list of references.Contains a list of references.
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
    def Append(self,value : OCP.TDF.TDF_Label) -> None: 
        """
        None
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
    def Extent(self) -> int: 
        """
        None
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def First(self) -> OCP.TDF.TDF_Label: 
        """
        None
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Static methods ============== Returns the ID of the list of references (labels) attribute.
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
    @overload
    def InsertAfter(self,value : OCP.TDF.TDF_Label,after_value : OCP.TDF.TDF_Label) -> bool: 
        """
        Inserts the <value> after the first meet of <after_value>.

        Inserts the label after the <index> position. The indices start with 1 .. Extent().
        """
    @overload
    def InsertAfter(self,index : int,after_value : OCP.TDF.TDF_Label) -> bool: ...
    @overload
    def InsertBefore(self,index : int,before_value : OCP.TDF.TDF_Label) -> bool: 
        """
        Inserts the <value> before the first meet of <before_value>.

        Inserts the label before the <index> position. The indices start with 1 .. Extent().
        """
    @overload
    def InsertBefore(self,value : OCP.TDF.TDF_Label,before_value : OCP.TDF.TDF_Label) -> bool: ...
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
    def Last(self) -> OCP.TDF.TDF_Label: 
        """
        None
        """
    def List(self) -> OCP.TDF.TDF_LabelList: 
        """
        None
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def Prepend(self,value : OCP.TDF.TDF_Label) -> None: 
        """
        None
        """
    def References(self,DS : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    @overload
    def Remove(self,index : int) -> bool: 
        """
        Removes the first meet of the <value>.

        Removes a label at "index" position.
        """
    @overload
    def Remove(self,value : OCP.TDF.TDF_Label) -> bool: ...
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID (user defined) for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,theGuid : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,theGuid : OCP.Standard.Standard_GUID) -> TDataStd_ReferenceList: 
        """
        Finds or creates a list of reference values (labels) attribute.

        Finds or creates a list of reference values (labels) attribute with explicit user defined <guid>.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_ReferenceList: ...
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
class TDataStd_Relation(TDataStd_Expression, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Relation attribute. ==================Relation attribute. ==================Relation attribute. ==================
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetExpression(self) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def GetRelation(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def GetVariables(self) -> OCP.TDF.TDF_AttributeList: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        build and return the expression name
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
    def SetExpression(self,E : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetRelation(self,E : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_Relation: 
        """
        Find, or create, an Relation attribute. Real methods ============
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
class TDataStd_Tick(TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Defines a boolean attribute. If it exists at a label - true, Otherwise - false.Defines a boolean attribute. If it exists at a label - true, Otherwise - false.Defines a boolean attribute. If it exists at a label - true, Otherwise - false.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Static methods ==============
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
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
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
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_Tick: 
        """
        Find, or create, a Tick attribute. Tick methods ============
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
class TDataStd_TreeNode(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Allows you to define an explicit tree of labels which you can also edit. Without this class, the data structure cannot be fully edited. This service is required if for presentation purposes, you want to create an application with a tree which allows you to organize and link data as a function of application features.Allows you to define an explicit tree of labels which you can also edit. Without this class, the data structure cannot be fully edited. This service is required if for presentation purposes, you want to create an application with a tree which allows you to organize and link data as a function of application features.Allows you to define an explicit tree of labels which you can also edit. Without this class, the data structure cannot be fully edited. This service is required if for presentation purposes, you want to create an application with a tree which allows you to organize and link data as a function of application features.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Connect the TreeNode to its father child list
        """
    def AfterResume(self) -> None: 
        """
        Reconnect the TreeNode to its father child list.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Reconnect the TreeNode, if necessary. Implementation of Attribute methods: ===================================
        """
    def Append(self,Child : TDataStd_TreeNode) -> bool: 
        """
        Insert the TreeNode <Child> as last child of <me>. If the insertion is successful <me> becomes the Father of <Child>.
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
        Disconnect the TreeNode from its Father child list
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Disconnect the TreeNode, if necessary.
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
    def Depth(self) -> int: 
        """
        Returns the depth of this tree node in the overall tree node structure. In other words, the number of father tree nodes of this one is returned.
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
    def Father(self) -> TDataStd_TreeNode: 
        """
        Returns the father TreeNode of <me>. Null if root.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def FindLast(self) -> TDataStd_TreeNode: 
        """
        Returns the last child tree node in this tree node object. to set fields =============
        """
    @staticmethod
    def Find_s(L : OCP.TDF.TDF_Label,T : TDataStd_TreeNode) -> bool: 
        """
        class methods working on the node =================================== Returns true if the tree node T is found on the label L. Otherwise, false is returned.
        """
    def First(self) -> TDataStd_TreeNode: 
        """
        Returns the first child tree node in this tree node object.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetDefaultTreeID_s() -> OCP.Standard.Standard_GUID: 
        """
        returns a default tree ID. this ID is used by the <Set> method without explicit tree ID. Instance methods: ================
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFather(self) -> bool: 
        """
        Returns true if this tree node attribute has a father tree node.

        Returns true if this tree node attribute has a father tree node.
        """
    def HasFirst(self) -> bool: 
        """
        Returns true if this tree node attribute has a first child tree node.

        Returns true if this tree node attribute has a first child tree node.
        """
    def HasLast(self) -> bool: 
        """
        Returns true if this tree node attribute has a last child tree node.

        Returns true if this tree node attribute has a last child tree node.
        """
    def HasNext(self) -> bool: 
        """
        Returns true if this tree node attribute has a next tree node.

        Returns true if this tree node attribute has a next tree node.
        """
    def HasPrevious(self) -> bool: 
        """
        Returns true if this tree node attribute has a previous tree node.

        Returns true if this tree node attribute has a previous tree node.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the tree ID (default or explicit one depending onthe Set method used).
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InsertAfter(self,Node : TDataStd_TreeNode) -> bool: 
        """
        Inserts the TreeNode <Node> after <me>. If insertion is successful <me> and <Node> belongs to the same Father.
        """
    def InsertBefore(self,Node : TDataStd_TreeNode) -> bool: 
        """
        Inserts the TreeNode <Node> before <me>. If insertion is successful <me> and <Node> belongs to the same Father.
        """
    def IsAscendant(self,of : TDataStd_TreeNode) -> bool: 
        """
        Returns true if this tree node attribute is an ascendant of of. In other words, if it is a father or the father of a father of of.
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
    def IsChild(self,of : TDataStd_TreeNode) -> bool: 
        """
        Returns true if this tree node attribute is a child of of.
        """
    def IsDescendant(self,of : TDataStd_TreeNode) -> bool: 
        """
        Returns true if this tree node attribute is a descendant of of. In other words, if it is a child or the child of a child of of.
        """
    def IsFather(self,of : TDataStd_TreeNode) -> bool: 
        """
        Returns true if this tree node attribute is a father of of.
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
    def IsRoot(self) -> bool: 
        """
        Returns true if this tree node attribute is the ultimate father in the tree.
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
    def Last(self) -> TDataStd_TreeNode: 
        """
        Returns the last child tree node in this tree node object.
        """
    def NbChildren(self,allLevels : bool=False) -> int: 
        """
        Returns the number of child nodes. If <allLevels> is true, the method counts children of all levels (children of children ...)
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Next(self) -> TDataStd_TreeNode: 
        """
        Returns the next tree node in this tree node attribute. Warning This tree node is null if it is the last one in this tree node attribute.Returns the next TreeNode of <me>. Null if last.
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def Prepend(self,Child : TDataStd_TreeNode) -> bool: 
        """
        Insert the the TreeNode <Child> as first child of <me>. If the insertion is successful <me> becomes the Father of <Child>
        """
    def Previous(self) -> TDataStd_TreeNode: 
        """
        Returns the previous tree node of this tree node attribute. Warning This tree node is null if it is the first one in this tree node attribute.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    def Remove(self) -> bool: 
        """
        Removes this tree node attribute from its father node. The result is that this attribute becomes a root node.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Root(self) -> TDataStd_TreeNode: 
        """
        Returns the ultimate father of this tree node attribute.
        """
    def SetFather(self,F : TDataStd_TreeNode) -> None: 
        """
        None
        """
    def SetFirst(self,F : TDataStd_TreeNode) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetLast(self,F : TDataStd_TreeNode) -> None: 
        """
        TreeNode callback: ==================
        """
    def SetNext(self,F : TDataStd_TreeNode) -> None: 
        """
        None
        """
    def SetPrevious(self,F : TDataStd_TreeNode) -> None: 
        """
        None
        """
    def SetTreeID(self,explicitID : OCP.Standard.Standard_GUID) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def Set_s(L : OCP.TDF.TDF_Label) -> TDataStd_TreeNode: 
        """
        Finds or Creates a TreeNode attribute on the label <L> with the default tree ID, returned by the method <GetDefaultTreeID>. Returns the created/found TreeNode attribute.

        Finds or Creates a TreeNode attribute on the label <L>, with an explicit tree ID. <ExplicitTreeID> is the ID returned by <TDF_Attribute::ID> method. Returns the found/created TreeNode attribute.
        """
    @staticmethod
    @overload
    def Set_s(L : OCP.TDF.TDF_Label,ExplicitTreeID : OCP.Standard.Standard_GUID) -> TDataStd_TreeNode: ...
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
class TDataStd_UAttribute(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
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
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,DS : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetID(self,LocalID : OCP.Standard.Standard_GUID) -> None: 
        """
        None
        """
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label,LocalID : OCP.Standard.Standard_GUID) -> TDataStd_UAttribute: 
        """
        api class methods ============= Find, or create, a UAttribute attribute with <LocalID> as Local GUID. The UAttribute attribute is returned. UAttribute methods ============
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
class TDataStd_Variable(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Variable attribute. ==================Variable attribute. ==================Variable attribute. ==================
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
    def Assign(self) -> TDataStd_Expression: ...
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
    def Constant(self,status : bool) -> None: 
        """
        if <status> is True, this variable will not be modified by the solver.
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
    def Desassign(self) -> None: 
        """
        if <me> is assigned delete the associated expression attribute.
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
    def Expression(self) -> TDataStd_Expression: 
        """
        if <me> is assigned, returns associated Expression attribute.
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
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> float: 
        """
        returns value stored in associated Real attribute.
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
    def IsAssigned(self) -> bool: 
        """
        returns True if an Expression attribute is associated. create(if doesn't exist), set and returns the assigned expression attribute.
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
    def IsCaptured(self) -> bool: 
        """
        shortcut for <Real()->IsCaptured()>
        """
    def IsConstant(self) -> bool: 
        """
        A constant value is not modified by regeneration.
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
    def IsValued(self) -> bool: 
        """
        returns True if a Real attribute is associated.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    @overload
    def Name(self,string : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        set or change the name of the variable, in myUnknown and my associated Name attribute.

        returns string stored in the associated Name attribute.
        """
    @overload
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString: ...
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def Real(self) -> TDataStd_Real: 
        """
        returns associated Real attribute.
        """
    def References(self,DS : OCP.TDF.TDF_DataSet) -> None: 
        """
        to export reference to the associated Name attribute.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def Set(self,value : float) -> None: 
        """
        retrieve or create the associated real attribute and set the value <value>.

        Obsolete method that will be removed in next versions. The dimension argument is not supported in the persistence mechanism.
        """
    @overload
    def Set(self,value : float,dimension : TDataStd_RealEnum) -> None: ...
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataStd_Variable: 
        """
        Find, or create, a Variable attribute. Real methods ============
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
    @overload
    def Unit(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        to read/write fields ===================
        """
    @overload
    def Unit(self,unit : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
TDataStd_ANGULAR: OCP.TDataStd.TDataStd_RealEnum # value = <TDataStd_RealEnum.TDataStd_ANGULAR: 2>
TDataStd_LENGTH: OCP.TDataStd.TDataStd_RealEnum # value = <TDataStd_RealEnum.TDataStd_LENGTH: 1>
TDataStd_SCALAR: OCP.TDataStd.TDataStd_RealEnum # value = <TDataStd_RealEnum.TDataStd_SCALAR: 0>
