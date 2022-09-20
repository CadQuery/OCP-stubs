import OCP.TFunction
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.NCollection
import io
import OCP.Standard
import OCP.TColStd
__all__  = [
"TFunction_Array1OfDataMapOfGUIDDriver",
"TFunction_DataMapOfLabelListOfLabel",
"TFunction_DoubleMapOfIntegerLabel",
"TFunction_Driver",
"TFunction_DriverTable",
"TFunction_ExecutionStatus",
"TFunction_Function",
"TFunction_GraphNode",
"TFunction_HArray1OfDataMapOfGUIDDriver",
"TFunction_IFunction",
"TFunction_Iterator",
"TFunction_Logbook",
"TFunction_Scope",
"TFunction_ES_Executing",
"TFunction_ES_Failed",
"TFunction_ES_NotExecuted",
"TFunction_ES_Succeeded",
"TFunction_ES_WrongDefinition"
]
class TFunction_Array1OfDataMapOfGUIDDriver():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TFunction_Array1OfDataMapOfGUIDDriver) -> TFunction_Array1OfDataMapOfGUIDDriver: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Any: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Any: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Any: 
        """
        Variable value access
        """
    def First(self) -> Any: 
        """
        Returns first element
        """
    def Init(self,theValue : Any) -> None: 
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
    def Last(self) -> Any: 
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
    def Move(self,theOther : TFunction_Array1OfDataMapOfGUIDDriver) -> TFunction_Array1OfDataMapOfGUIDDriver: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Any) -> None: 
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
    def Value(self,theIndex : int) -> Any: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : Any,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TFunction_Array1OfDataMapOfGUIDDriver) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TFunction_DataMapOfLabelListOfLabel(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TFunction_DataMapOfLabelListOfLabel) -> TFunction_DataMapOfLabelListOfLabel: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TDF.TDF_Label,theItem : OCP.TDF.TDF_LabelList) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TDF.TDF_Label,theItem : OCP.TDF.TDF_LabelList) -> OCP.TDF.TDF_LabelList: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_LabelList: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_LabelList: 
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
    def Exchange(self,theOther : TFunction_DataMapOfLabelListOfLabel) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TDF.TDF_Label,theValue : OCP.TDF.TDF_LabelList) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_LabelList: ...
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
    def Seek(self,theKey : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_LabelList: 
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
    def __init__(self,theOther : TFunction_DataMapOfLabelListOfLabel) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TFunction_DoubleMapOfIntegerLabel(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DoubleMap is used to bind pairs (Key1,Key2) and retrieve them in linear time.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def AreBound(self,theKey1 : int,theKey2 : OCP.TDF.TDF_Label) -> bool: 
        """
        * AreBound
        """
    def Assign(self,theOther : TFunction_DoubleMapOfIntegerLabel) -> TFunction_DoubleMapOfIntegerLabel: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey1 : int,theKey2 : OCP.TDF.TDF_Label) -> None: 
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
    def Exchange(self,theOther : TFunction_DoubleMapOfIntegerLabel) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find1(self,theKey1 : int) -> OCP.TDF.TDF_Label: 
        """
        Find the Key1 and return Key2 value. Raises an exception if Key1 was not bound.

        Find the Key1 and return Key2 value (by copying its value).
        """
    @overload
    def Find1(self,theKey1 : int,theKey2 : OCP.TDF.TDF_Label) -> bool: ...
    @overload
    def Find2(self,theKey2 : OCP.TDF.TDF_Label) -> int: 
        """
        Find the Key2 and return Key1 value. Raises an exception if Key2 was not bound.

        Find the Key2 and return Key1 value (by copying its value).
        """
    @overload
    def Find2(self,theKey2 : OCP.TDF.TDF_Label,theKey1 : int) -> bool: ...
    def IsBound1(self,theKey1 : int) -> bool: 
        """
        IsBound1
        """
    def IsBound2(self,theKey2 : OCP.TDF.TDF_Label) -> bool: 
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
    def Seek1(self,theKey1 : int) -> OCP.TDF.TDF_Label: 
        """
        Find the Key1 and return pointer to Key2 or NULL if Key1 is not bound.
        """
    def Seek2(self,theKey2 : OCP.TDF.TDF_Label) -> int: 
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
    def UnBind1(self,theKey1 : int) -> bool: 
        """
        UnBind1
        """
    def UnBind2(self,theKey2 : OCP.TDF.TDF_Label) -> bool: 
        """
        UnBind2
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TFunction_DoubleMapOfIntegerLabel) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class TFunction_Driver(OCP.Standard.Standard_Transient):
    """
    This driver class provide services around function execution. One instance of this class is built for the whole session. The driver is bound to the DriverGUID in the DriverTable class. It allows you to create classes which inherit from this abstract class. These subclasses identify the various algorithms which can be applied to the data contained in the attributes of sub-labels of a model. A single instance of this class and each of its subclasses is built for the whole session.This driver class provide services around function execution. One instance of this class is built for the whole session. The driver is bound to the DriverGUID in the DriverTable class. It allows you to create classes which inherit from this abstract class. These subclasses identify the various algorithms which can be applied to the data contained in the attributes of sub-labels of a model. A single instance of this class and each of its subclasses is built for the whole session.This driver class provide services around function execution. One instance of this class is built for the whole session. The driver is bound to the DriverGUID in the DriverTable class. It allows you to create classes which inherit from this abstract class. These subclasses identify the various algorithms which can be applied to the data contained in the attributes of sub-labels of a model. A single instance of this class and each of its subclasses is built for the whole session.
    """
    def Arguments(self,args : OCP.TDF.TDF_LabelList) -> None: 
        """
        The method fills-in the list by labels, where the arguments of the function are located.
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
    def Execute(self,log : TFunction_Logbook) -> int: 
        """
        Executes the function in this function driver and puts the impacted labels in the logbook log. arguments & results of functions ================================
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,L : OCP.TDF.TDF_Label) -> None: 
        """
        Initializes the label L for this function prior to its execution.
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
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label of the driver for this function.

        Returns the label of the driver for this function.
        """
    def MustExecute(self,log : TFunction_Logbook) -> bool: 
        """
        Analyzes the labels in the logbook log. Returns true if attributes have been modified. If the function label itself has been modified, the function must be executed.
        """
    def Results(self,res : OCP.TDF.TDF_LabelList) -> None: 
        """
        The method fills-in the list by labels, where the results of the function are located.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Validate(self,log : TFunction_Logbook) -> Any: 
        """
        Validates labels of a function in <log>. This function is the one initialized in this function driver. Warning In regeneration mode, the solver must call this method even if the function is not executed. execution of function =====================
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
class TFunction_DriverTable(OCP.Standard.Standard_Transient):
    """
    A container for instances of drivers. You create a new instance of TFunction_Driver and use the method AddDriver to load it into the driver table.A container for instances of drivers. You create a new instance of TFunction_Driver and use the method AddDriver to load it into the driver table.A container for instances of drivers. You create a new instance of TFunction_Driver and use the method AddDriver to load it into the driver table.
    """
    def AddDriver(self,guid : OCP.Standard.Standard_GUID,driver : TFunction_Driver,thread : int=0) -> bool: 
        """
        Returns true if the driver has been added successfully to the driver table.
        """
    def Clear(self) -> None: 
        """
        Removes all drivers. Returns true if the driver has been removed successfully.
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
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FindDriver(self,guid : OCP.Standard.Standard_GUID,driver : TFunction_Driver,thread : int=0) -> bool: 
        """
        Returns true if the driver was found.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s() -> TFunction_DriverTable: 
        """
        Returns the driver table. If a driver does not exist, creates it.
        """
    def HasDriver(self,guid : OCP.Standard.Standard_GUID,thread : int=0) -> bool: 
        """
        Returns true if the driver exists in the driver table.
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
    def RemoveDriver(self,guid : OCP.Standard.Standard_GUID,thread : int=0) -> bool: 
        """
        Removes a driver with the given GUID. Returns true if the driver has been removed successfully.
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
class TFunction_ExecutionStatus():
    """
    None

    Members:

      TFunction_ES_WrongDefinition

      TFunction_ES_NotExecuted

      TFunction_ES_Executing

      TFunction_ES_Succeeded

      TFunction_ES_Failed
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
    TFunction_ES_Executing: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_Executing: 2>
    TFunction_ES_Failed: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_Failed: 4>
    TFunction_ES_NotExecuted: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_NotExecuted: 1>
    TFunction_ES_Succeeded: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_Succeeded: 3>
    TFunction_ES_WrongDefinition: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_WrongDefinition: 0>
    __entries: dict # value = {'TFunction_ES_WrongDefinition': (<TFunction_ExecutionStatus.TFunction_ES_WrongDefinition: 0>, None), 'TFunction_ES_NotExecuted': (<TFunction_ExecutionStatus.TFunction_ES_NotExecuted: 1>, None), 'TFunction_ES_Executing': (<TFunction_ExecutionStatus.TFunction_ES_Executing: 2>, None), 'TFunction_ES_Succeeded': (<TFunction_ExecutionStatus.TFunction_ES_Succeeded: 3>, None), 'TFunction_ES_Failed': (<TFunction_ExecutionStatus.TFunction_ES_Failed: 4>, None)}
    __members__: dict # value = {'TFunction_ES_WrongDefinition': <TFunction_ExecutionStatus.TFunction_ES_WrongDefinition: 0>, 'TFunction_ES_NotExecuted': <TFunction_ExecutionStatus.TFunction_ES_NotExecuted: 1>, 'TFunction_ES_Executing': <TFunction_ExecutionStatus.TFunction_ES_Executing: 2>, 'TFunction_ES_Succeeded': <TFunction_ExecutionStatus.TFunction_ES_Succeeded: 3>, 'TFunction_ES_Failed': <TFunction_ExecutionStatus.TFunction_ES_Failed: 4>}
    pass
class TFunction_Function(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Provides the following two services - a link to an evaluation driver - the means of providing a link between a function and an evaluation driver.Provides the following two services - a link to an evaluation driver - the means of providing a link between a function and an evaluation driver.Provides the following two services - a link to an evaluation driver - the means of providing a link between a function and an evaluation driver.
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
    def Failed(self) -> bool: 
        """
        Returns true if the execution failed
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
    def GetDriverGUID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the GUID for this function's driver.
        """
    def GetFailure(self) -> int: 
        """
        Returns an index of failure if the execution of this function failed. If this integer value is 0, no failure has occurred. Implementation of Attribute methods: ===================================
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the GUID for functions. Returns a function found on the label. Instance methods: ================
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
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetDriverGUID(self,guid : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the driver for this function as that identified by the GUID guid.
        """
    def SetFailure(self,mode : int=0) -> None: 
        """
        Sets the failed index.
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
    @overload
    def Set_s(L : OCP.TDF.TDF_Label) -> TFunction_Function: 
        """
        Static methods: ============== Finds or Creates a function attribute on the label <L>. Returns the function attribute.

        Finds or Creates a function attribute on the label <L>. Sets a driver ID to the function. Returns the function attribute.
        """
    @staticmethod
    @overload
    def Set_s(L : OCP.TDF.TDF_Label,DriverID : OCP.Standard.Standard_GUID) -> TFunction_Function: ...
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
class TFunction_GraphNode(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Provides links between functions.Provides links between functions.Provides links between functions.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    @overload
    def AddNext(self,func : OCP.TDF.TDF_Label) -> bool: 
        """
        Defines a reference to the function as a next one.

        Defines a reference to the function as a next one.
        """
    @overload
    def AddNext(self,funcID : int) -> bool: ...
    @overload
    def AddPrevious(self,funcID : int) -> bool: 
        """
        Defines a reference to the function as a previous one.

        Defines a reference to the function as a previous one.
        """
    @overload
    def AddPrevious(self,func : OCP.TDF.TDF_Label) -> bool: ...
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
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the GUID for GraphNode attribute. Instant methods =============== Constructor (empty).
        """
    def GetNext(self) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Returns a map of next functions.
        """
    def GetPrevious(self) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Returns a map of previous functions.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> TFunction_ExecutionStatus: 
        """
        Returns the execution status of the function.
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
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    def RemoveAllNext(self) -> None: 
        """
        Clears a map of next functions.
        """
    def RemoveAllPrevious(self) -> None: 
        """
        Clears a map of previous functions.
        """
    @overload
    def RemoveNext(self,funcID : int) -> bool: 
        """
        Removes a reference to the function as a next one.

        Removes a reference to the function as a next one.
        """
    @overload
    def RemoveNext(self,func : OCP.TDF.TDF_Label) -> bool: ...
    @overload
    def RemovePrevious(self,func : OCP.TDF.TDF_Label) -> bool: 
        """
        Removes a reference to the function as a previous one.

        Removes a reference to the function as a previous one.
        """
    @overload
    def RemovePrevious(self,funcID : int) -> bool: ...
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
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
    def SetStatus(self,status : TFunction_ExecutionStatus) -> None: 
        """
        Defines an execution status for a function. Implementation of Attribute methods ===================================
        """
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> TFunction_GraphNode: 
        """
        Static methods ============== Finds or Creates a graph node attribute at the label <L>. Returns the attribute.
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
class TFunction_HArray1OfDataMapOfGUIDDriver(TFunction_Array1OfDataMapOfGUIDDriver, OCP.Standard.Standard_Transient):
    def Array1(self) -> TFunction_Array1OfDataMapOfGUIDDriver: 
        """
        None
        """
    def Assign(self,theOther : TFunction_Array1OfDataMapOfGUIDDriver) -> TFunction_Array1OfDataMapOfGUIDDriver: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TFunction_Array1OfDataMapOfGUIDDriver: 
        """
        None
        """
    def ChangeFirst(self) -> Any: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Any: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Any: 
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
    def First(self) -> Any: 
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
    def Init(self,theValue : Any) -> None: 
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
    def Last(self) -> Any: 
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
    def Move(self,theOther : TFunction_Array1OfDataMapOfGUIDDriver) -> TFunction_Array1OfDataMapOfGUIDDriver: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Any) -> None: 
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
    def Value(self,theIndex : int) -> Any: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TFunction_Array1OfDataMapOfGUIDDriver) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Any) -> None: ...
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
class TFunction_IFunction():
    """
    Interface class for usage of Function Mechanism
    """
    def Arguments(self,args : OCP.TDF.TDF_LabelList) -> None: 
        """
        The method fills-in the list by labels, where the arguments of the function are located.
        """
    @staticmethod
    def DeleteFunction_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Deletes a function attached to a label <L>. It deletes a TFunction_Function attribute and a TFunction_GraphNode. It deletes the functions from the scope of function of this document.
        """
    def GetAllFunctions(self) -> TFunction_DoubleMapOfIntegerLabel: 
        """
        Returns the scope of all functions.
        """
    def GetDriver(self,thread : int=0) -> TFunction_Driver: 
        """
        Returns a driver of the function.
        """
    def GetGraphNode(self) -> TFunction_GraphNode: 
        """
        Returns a graph node of the function.
        """
    def GetLogbook(self) -> TFunction_Logbook: 
        """
        Returns the Logbook - keeper of modifications.
        """
    def GetNext(self,prev : OCP.TDF.TDF_LabelList) -> None: 
        """
        Returns a list of next functions.
        """
    def GetPrevious(self,prev : OCP.TDF.TDF_LabelList) -> None: 
        """
        Returns a list of previous functions.
        """
    def GetStatus(self) -> TFunction_ExecutionStatus: 
        """
        Returns the execution status of the function.
        """
    def Init(self,L : OCP.TDF.TDF_Label) -> None: 
        """
        Initializes the interface by the label of function.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns a label of the function.
        """
    @staticmethod
    def NewFunction_s(L : OCP.TDF.TDF_Label,ID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Sets a new function attached to a label <L> with <ID>. It creates a new TFunction_Function attribute initialized by the <ID>, a new TFunction_GraphNode with an empty list of dependencies and the status equal to TFunction_ES_WrongDefinition. It registers the function in the scope of functions for this document.
        """
    def Results(self,res : OCP.TDF.TDF_LabelList) -> None: 
        """
        The method fills-in the list by labels, where the results of the function are located.
        """
    def SetStatus(self,status : TFunction_ExecutionStatus) -> None: 
        """
        Defines an execution status for a function.
        """
    def UpdateDependencies(self) -> bool: 
        """
        Updates the dependencies of this function only.
        """
    @staticmethod
    def UpdateDependencies_s(Access : OCP.TDF.TDF_Label) -> bool: 
        """
        Updates dependencies for all functions of the scope. It returns false in case of an error. An empty constructor.
        """
    @overload
    def __init__(self,L : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TFunction_Iterator():
    """
    Iterator of the graph of functions
    """
    def Current(self) -> OCP.TDF.TDF_LabelList: 
        """
        Returns the current list of functions. If the iterator uses the execution status, the returned list contains only the functions with "not executed" status.
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def GetMaxNbThreads(self) -> int: 
        """
        Analyses the graph of dependencies and returns maximum number of threads may be used to calculate the model.
        """
    def GetStatus(self,func : OCP.TDF.TDF_Label) -> TFunction_ExecutionStatus: 
        """
        A help-function aimed to help the user to check the status of retrurned function. It calls TFunction_GraphNode::GetStatus() inside.
        """
    def GetUsageOfExecutionStatus(self) -> bool: 
        """
        Returns usage of execution status by the iterator.
        """
    def Init(self,Access : OCP.TDF.TDF_Label) -> None: 
        """
        Initializes the Iterator.
        """
    def More(self) -> bool: 
        """
        Returns false if the graph of functions is fully iterated.
        """
    def Next(self) -> None: 
        """
        Switches the iterator to the next list of current functions.
        """
    def SetStatus(self,func : OCP.TDF.TDF_Label,status : TFunction_ExecutionStatus) -> None: 
        """
        A help-function aimed to help the user to change the execution status of a function. It calls TFunction_GraphNode::SetStatus() inside.
        """
    def SetUsageOfExecutionStatus(self,usage : bool) -> None: 
        """
        Defines the mode of iteration - usage or not of the execution status. If the iterator takes into account the execution status, the method ::Current() returns only "not executed" functions while their status is not changed. If the iterator ignores the execution status, the method ::Current() returns the functions following their dependencies and ignoring the execution status.
        """
    @overload
    def __init__(self,Access : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TFunction_Logbook(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    This class contains information which is written and read during the solving process. Information is divided in three groups.This class contains information which is written and read during the solving process. Information is divided in three groups.This class contains information which is written and read during the solving process. Information is divided in three groups.This class contains information which is written and read during the solving process. Information is divided in three groups.
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
        Clears this logbook to its default, empty state.
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
    def Done(self,status : bool) -> None: 
        """
        Sets status of execution.

        Sets status of execution.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Prints th data of the attributes (touched, impacted and valid labels).
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
        Returns the GUID for logbook attribute.
        """
    def GetImpacted(self) -> OCP.TDF.TDF_LabelMap: 
        """
        Returns the map of impacted labels contained in this logbook.

        Returns the map of impacted labels contained in this logbook.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTouched(self) -> OCP.TDF.TDF_LabelMap: 
        """
        Returns the map of touched labels in this logbook. A touched label is the one modified by the end user.

        Returns the map of touched labels in this logbook. A touched label is the one modified by the end user.
        """
    @overload
    def GetValid(self,Ls : OCP.TDF.TDF_LabelMap) -> None: 
        """
        None

        Returns the map of valid labels in this logbook.

        Returns the map of valid labels in this logbook.
        """
    @overload
    def GetValid(self) -> OCP.TDF.TDF_LabelMap: ...
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
    def IsDone(self) -> bool: 
        """
        Returns status of execution.

        Returns status of execution.
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
    def IsModified(self,L : OCP.TDF.TDF_Label,WithChildren : bool=False) -> bool: 
        """
        Returns True if the label L is touched or impacted. This method is called by <TFunction_FunctionDriver::MustExecute>. If <WithChildren> is set to true, the method checks all the sublabels of <L> too.
        """
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
        Returns a new empty instance of the attribute.
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Pastes the attribute to another label.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: ...
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self) -> None: ...
    def SetImpacted(self,L : OCP.TDF.TDF_Label,WithChildren : bool=False) -> None: 
        """
        Sets the label L as an impacted label in this logbook. This method is called by execution of the function driver.
        """
    def SetTouched(self,L : OCP.TDF.TDF_Label) -> None: 
        """
        Sets the label L as a touched label in this logbook. In other words, L is understood to have been modified by the end user.

        Sets the label L as a touched label in this logbook. In other words, L is understood to have been modified by the end user.
        """
    @overload
    def SetValid(self,L : OCP.TDF.TDF_Label,WithChildren : bool=False) -> None: 
        """
        Sets the label L as a valid label in this logbook.

        None
        """
    @overload
    def SetValid(self,Ls : OCP.TDF.TDF_LabelMap) -> None: ...
    @staticmethod
    def Set_s(Access : OCP.TDF.TDF_Label) -> TFunction_Logbook: 
        """
        Finds or Creates a TFunction_Logbook attribute at the root label accessed by <Access>. Returns the attribute.
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
class TFunction_Scope(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Keeps a scope of functions.Keeps a scope of functions.Keeps a scope of functions.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AddFunction(self,L : OCP.TDF.TDF_Label) -> bool: 
        """
        Adds a function to the scope of functions.
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
    def ChangeFunctions(self) -> TFunction_DoubleMapOfIntegerLabel: 
        """
        Returns the scope of functions for modification. Warning: Don't use this method if You are not sure what You do!
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
    def GetFreeID(self) -> int: 
        """
        None
        """
    @overload
    def GetFunction(self,L : OCP.TDF.TDF_Label) -> int: 
        """
        Returns an ID of the function.

        Returns the label of the function with this ID.
        """
    @overload
    def GetFunction(self,ID : int) -> OCP.TDF.TDF_Label: ...
    def GetFunctions(self) -> TFunction_DoubleMapOfIntegerLabel: 
        """
        Returns the scope of functions.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the GUID for Scope attribute. Instant methods =============== Constructor (empty).
        """
    def GetLogbook(self) -> TFunction_Logbook: 
        """
        Returns the Logbook used in TFunction_Driver methods. Implementation of Attribute methods ===================================
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def HasFunction(self,L : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns true if the function exists with such an ID.

        Returns true if the label contains a function of this scope.
        """
    @overload
    def HasFunction(self,ID : int) -> bool: ...
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
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveAllFunctions(self) -> None: 
        """
        Removes all functions from the scope of functions.
        """
    @overload
    def RemoveFunction(self,L : OCP.TDF.TDF_Label) -> bool: 
        """
        Removes a function from the scope of functions.

        Removes a function from the scope of functions.
        """
    @overload
    def RemoveFunction(self,ID : int) -> bool: ...
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetFreeID(self,ID : int) -> None: 
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
    def Set_s(Access : OCP.TDF.TDF_Label) -> TFunction_Scope: 
        """
        Static methods ============== Finds or Creates a TFunction_Scope attribute at the root label accessed by <Access>. Returns the attribute.
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
TFunction_ES_Executing: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_Executing: 2>
TFunction_ES_Failed: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_Failed: 4>
TFunction_ES_NotExecuted: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_NotExecuted: 1>
TFunction_ES_Succeeded: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_Succeeded: 3>
TFunction_ES_WrongDefinition: OCP.TFunction.TFunction_ExecutionStatus # value = <TFunction_ExecutionStatus.TFunction_ES_WrongDefinition: 0>
