import OCP.Message
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TColStd
import OCP.Standard
import OCP.TCollection
__all__  = [
"Message",
"Message_Alert",
"Message_Algorithm",
"Message_ArrayOfMsg",
"Message_ExecStatus",
"Message_Gravity",
"Message_ListOfAlert",
"Message_ListOfMsg",
"Message_Messenger",
"Message_Msg",
"Message_MsgFile",
"Message_Printer",
"Message_PrinterOStream",
"Message_ProgressIndicator",
"Message_ProgressScale",
"Message_ProgressSentry",
"Message_Report",
"Message_SequenceOfPrinters",
"Message_SequenceOfProgressScale",
"Message_Status",
"Message_StatusType",
"Message_EndLine",
"Message_ALARM",
"Message_Alarm",
"Message_Alarm1",
"Message_Alarm10",
"Message_Alarm11",
"Message_Alarm12",
"Message_Alarm13",
"Message_Alarm14",
"Message_Alarm15",
"Message_Alarm16",
"Message_Alarm17",
"Message_Alarm18",
"Message_Alarm19",
"Message_Alarm2",
"Message_Alarm20",
"Message_Alarm21",
"Message_Alarm22",
"Message_Alarm23",
"Message_Alarm24",
"Message_Alarm25",
"Message_Alarm26",
"Message_Alarm27",
"Message_Alarm28",
"Message_Alarm29",
"Message_Alarm3",
"Message_Alarm30",
"Message_Alarm31",
"Message_Alarm32",
"Message_Alarm4",
"Message_Alarm5",
"Message_Alarm6",
"Message_Alarm7",
"Message_Alarm8",
"Message_Alarm9",
"Message_DONE",
"Message_Done1",
"Message_Done10",
"Message_Done11",
"Message_Done12",
"Message_Done13",
"Message_Done14",
"Message_Done15",
"Message_Done16",
"Message_Done17",
"Message_Done18",
"Message_Done19",
"Message_Done2",
"Message_Done20",
"Message_Done21",
"Message_Done22",
"Message_Done23",
"Message_Done24",
"Message_Done25",
"Message_Done26",
"Message_Done27",
"Message_Done28",
"Message_Done29",
"Message_Done3",
"Message_Done30",
"Message_Done31",
"Message_Done32",
"Message_Done4",
"Message_Done5",
"Message_Done6",
"Message_Done7",
"Message_Done8",
"Message_Done9",
"Message_FAIL",
"Message_Fail",
"Message_Fail1",
"Message_Fail10",
"Message_Fail11",
"Message_Fail12",
"Message_Fail13",
"Message_Fail14",
"Message_Fail15",
"Message_Fail16",
"Message_Fail17",
"Message_Fail18",
"Message_Fail19",
"Message_Fail2",
"Message_Fail20",
"Message_Fail21",
"Message_Fail22",
"Message_Fail23",
"Message_Fail24",
"Message_Fail25",
"Message_Fail26",
"Message_Fail27",
"Message_Fail28",
"Message_Fail29",
"Message_Fail3",
"Message_Fail30",
"Message_Fail31",
"Message_Fail32",
"Message_Fail4",
"Message_Fail5",
"Message_Fail6",
"Message_Fail7",
"Message_Fail8",
"Message_Fail9",
"Message_Info",
"Message_None",
"Message_Trace",
"Message_WARN",
"Message_Warn1",
"Message_Warn10",
"Message_Warn11",
"Message_Warn12",
"Message_Warn13",
"Message_Warn14",
"Message_Warn15",
"Message_Warn16",
"Message_Warn17",
"Message_Warn18",
"Message_Warn19",
"Message_Warn2",
"Message_Warn20",
"Message_Warn21",
"Message_Warn22",
"Message_Warn23",
"Message_Warn24",
"Message_Warn25",
"Message_Warn26",
"Message_Warn27",
"Message_Warn28",
"Message_Warn29",
"Message_Warn3",
"Message_Warn30",
"Message_Warn31",
"Message_Warn32",
"Message_Warn4",
"Message_Warn5",
"Message_Warn6",
"Message_Warn7",
"Message_Warn8",
"Message_Warn9",
"Message_Warning"
]
class Message():
    """
    Defines - tools to work with messages - basic tools intended for progress indication
    """
    @staticmethod
    def DefaultMessenger_s() -> Message_Messenger: 
        """
        Defines default messenger for OCCT applications. This is global static instance of the messenger. By default, it contains single printer directed to std::cout. It can be customized according to the application needs.
        """
    @staticmethod
    def FillTime_s(Hour : int,Minute : int,Second : float) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the string filled with values of hours, minutes and seconds. Example: 1. (5, 12, 26.3345) returns "05h:12m:26.33s", 2. (0, 6, 34.496 ) returns "06m:34.50s", 3. (0, 0, 4.5 ) returns "4.50s"
        """
    def __init__(self) -> None: ...
    pass
class Message_Alert(OCP.Standard.Standard_Transient):
    """
    Base class of the hierarchy of classes describing various situations occurring during execution of some algorithm or procedure.Base class of the hierarchy of classes describing various situations occurring during execution of some algorithm or procedure.Base class of the hierarchy of classes describing various situations occurring during execution of some algorithm or procedure.
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class Message_Algorithm(OCP.Standard.Standard_Transient):
    """
    Class Message_Algorithm is intended to be the base class for classes implementing algorithms or any operations that need to provide extended information on its execution to the caller / user.Class Message_Algorithm is intended to be the base class for classes implementing algorithms or any operations that need to provide extended information on its execution to the caller / user.Class Message_Algorithm is intended to be the base class for classes implementing algorithms or any operations that need to provide extended information on its execution to the caller / user.
    """
    @overload
    def AddStatus(self,theOther : Message_Algorithm) -> None: 
        """
        Add statuses to this algorithm from other algorithm (including messages)

        Add statuses to this algorithm from other algorithm, but only those items are moved that correspond to statuses set in theStatus
        """
    @overload
    def AddStatus(self,theStatus : Message_ExecStatus,theOther : Message_Algorithm) -> None: ...
    def ChangeStatus(self) -> Message_ExecStatus: 
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
    def GetMessageNumbers(self,theStatus : Message_Status) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Return the numbers associated with the indicated status; Null handle if no such status or no numbers associated with it
        """
    def GetMessageStrings(self,theStatus : Message_Status) -> OCP.TColStd.TColStd_HSequenceOfHExtendedString: 
        """
        Return the strings associated with the indicated status; Null handle if no such status or no strings associated with it
        """
    def GetMessenger(self) -> Message_Messenger: 
        """
        Returns messenger of algorithm. The returned handle is always non-null and can be used for sending messages.

        Returns messenger of algorithm. The returned handle is always non-null and can be used for sending messages.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> Message_ExecStatus: 
        """
        Returns copy of exec status of algorithm

        Returns copy of exec status of algorithm
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
    def SendMessages(self,theTraceLevel : Message_Gravity=Message_Gravity.Message_Warning,theMaxCount : int=20) -> None: 
        """
        Convenient variant of SendStatusMessages() with theFilter having defined all WARN, ALARM, and FAIL (but not DONE) status flags
        """
    def SendStatusMessages(self,theFilter : Message_ExecStatus,theTraceLevel : Message_Gravity=Message_Gravity.Message_Warning,theMaxCount : int=20) -> None: 
        """
        Print messages for all status flags that have been set during algorithm execution, excluding statuses that are NOT set in theFilter.
        """
    def SetMessenger(self,theMsgr : Message_Messenger) -> None: 
        """
        Sets messenger to algorithm
        """
    @overload
    def SetStatus(self,theStat : Message_Status,theMsg : Message_Msg) -> None: 
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
    def SetStatus(self,theStat : Message_Status) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_AsciiString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_AsciiString,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_HAsciiString,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_ExtendedString,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : str,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : str,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_HAsciiString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theInt : int) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_HExtendedString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_ExtendedString,noRepetitions : bool=True) -> None: ...
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
class Message_ArrayOfMsg():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Message_ArrayOfMsg) -> Message_ArrayOfMsg: 
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
    def Move(self,theOther : Message_ArrayOfMsg) -> Message_ArrayOfMsg: 
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
    def __init__(self,theOther : Message_ArrayOfMsg) -> None: ...
    @overload
    def __init__(self,theBegin : Any,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Message_ExecStatus():
    """
    Tiny class for extended handling of error / execution status of algorithm in universal way.
    """
    def Add(self,theOther : Message_ExecStatus) -> None: 
        """
        Add statuses to me from theOther execution status
        """
    def And(self,theOther : Message_ExecStatus) -> None: 
        """
        Leave only the statuses common with theOther
        """
    @overload
    def Clear(self,status : Message_Status) -> None: 
        """
        Clear one status

        Clear all statuses
        """
    @overload
    def Clear(self) -> None: ...
    def ClearAllAlarm(self) -> None: 
        """
        None
        """
    def ClearAllDone(self) -> None: 
        """
        Clear all statuses of each type
        """
    def ClearAllFail(self) -> None: 
        """
        None
        """
    def ClearAllWarn(self) -> None: 
        """
        None
        """
    def IsAlarm(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        Check if at least one status of each type is set
        """
    def IsFail(self) -> bool: 
        """
        None
        """
    def IsSet(self,status : Message_Status) -> bool: 
        """
        Check status for being set
        """
    def IsWarn(self) -> bool: 
        """
        None
        """
    @staticmethod
    def LocalStatusIndex_s(status : Message_Status) -> int: 
        """
        Returns index of status inside type of status (Done or Warn or, etc) in range [1, StatusesPerType]
        """
    def Set(self,status : Message_Status) -> None: 
        """
        Sets a status flag
        """
    def SetAllAlarm(self) -> None: 
        """
        None
        """
    def SetAllDone(self) -> None: 
        """
        Set all statuses of each type
        """
    def SetAllFail(self) -> None: 
        """
        None
        """
    def SetAllWarn(self) -> None: 
        """
        None
        """
    @staticmethod
    def StatusByIndex_s(theIndex : int) -> Message_Status: 
        """
        Returns status with index theIndex in whole range [FirstStatus, LastStatus]
        """
    @staticmethod
    def StatusIndex_s(status : Message_Status) -> int: 
        """
        Returns index of status in whole range [FirstStatus, LastStatus]
        """
    @staticmethod
    def TypeOfStatus_s(status : Message_Status) -> Message_StatusType: 
        """
        Returns status type (DONE, WARN, ALARM, or FAIL)
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,status : Message_Status) -> None: ...
    pass
class Message_Gravity():
    """
    Defines gravity level of messages - Trace: low-level details on algorithm execution (usually for debug purposes) - Info: informative message - Warning: warning message - Alarm: non-critical error - Fail: fatal error

    Members:

      Message_Trace

      Message_Info

      Message_Warning

      Message_Alarm

      Message_Fail
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Message_Alarm: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Alarm
    Message_Fail: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Fail
    Message_Info: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Info
    Message_Trace: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Trace
    Message_Warning: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Warning
    __entries: dict # value = {'Message_Trace': (Message_Gravity.Message_Trace, None), 'Message_Info': (Message_Gravity.Message_Info, None), 'Message_Warning': (Message_Gravity.Message_Warning, None), 'Message_Alarm': (Message_Gravity.Message_Alarm, None), 'Message_Fail': (Message_Gravity.Message_Fail, None)}
    __members__: dict # value = {'Message_Trace': Message_Gravity.Message_Trace, 'Message_Info': Message_Gravity.Message_Info, 'Message_Warning': Message_Gravity.Message_Warning, 'Message_Alarm': Message_Gravity.Message_Alarm, 'Message_Fail': Message_Gravity.Message_Fail}
    pass
class Message_ListOfAlert(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : Message_ListOfAlert) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : Message_Alert,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : Message_Alert) -> Message_Alert: ...
    def Assign(self,theOther : Message_ListOfAlert) -> Message_ListOfAlert: 
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
    def First(self) -> Message_Alert: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : Message_ListOfAlert,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : Message_Alert,theIter : Any) -> Message_Alert: ...
    @overload
    def InsertBefore(self,theOther : Message_ListOfAlert,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : Message_Alert,theIter : Any) -> Message_Alert: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> Message_Alert: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : Message_Alert) -> Message_Alert: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : Message_ListOfAlert) -> None: ...
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
    def __init__(self,theOther : Message_ListOfAlert) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Message_ListOfMsg(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : Message_ListOfMsg) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : Message_Msg) -> Message_Msg: ...
    @overload
    def Append(self,theItem : Message_Msg,theIter : Any) -> None: ...
    def Assign(self,theOther : Message_ListOfMsg) -> Message_ListOfMsg: 
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
    def First(self) -> Message_Msg: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : Message_ListOfMsg,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : Message_Msg,theIter : Any) -> Message_Msg: ...
    @overload
    def InsertBefore(self,theItem : Message_Msg,theIter : Any) -> Message_Msg: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : Message_ListOfMsg,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> Message_Msg: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : Message_Msg) -> Message_Msg: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : Message_ListOfMsg) -> None: ...
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
    def __init__(self,theOther : Message_ListOfMsg) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Message_Messenger(OCP.Standard.Standard_Transient):
    """
    Messenger is API class providing general-purpose interface for libraries that may issue text messages without knowledge of how these messages will be further processed.Messenger is API class providing general-purpose interface for libraries that may issue text messages without knowledge of how these messages will be further processed.Messenger is API class providing general-purpose interface for libraries that may issue text messages without knowledge of how these messages will be further processed.
    """
    def AddPrinter(self,thePrinter : Message_Printer) -> bool: 
        """
        Add a printer to the messenger. The printer will be added only if it is not yet in the list. Returns True if printer has been added.
        """
    def ChangePrinters(self) -> Message_SequenceOfPrinters: 
        """
        Returns sequence of printers The sequence can be modified.
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
    def Printers(self) -> Message_SequenceOfPrinters: 
        """
        Returns current sequence of printers
        """
    def RemovePrinter(self,thePrinter : Message_Printer) -> bool: 
        """
        Removes specified printer from the messenger. Returns True if this printer has been found in the list and removed.
        """
    def RemovePrinters(self,theType : OCP.Standard.Standard_Type) -> int: 
        """
        Removes printers of specified type (including derived classes) from the messenger. Returns number of removed printers.
        """
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_ExtendedString,theGravity : Message_Gravity=Message_Gravity.Message_Warning,putEndl : bool=True) -> None: 
        """
        Dispatch a message to all the printers in the list. Three versions of string representations are accepted for convenience, by default all are converted to ExtendedString. The parameter putEndl specifies whether the new line should be started after this message (default) or not (may have sense in some conditions).

        See above

        See above
        """
    @overload
    def Send(self,theString : str,theGravity : Message_Gravity=Message_Gravity.Message_Warning,putEndl : bool=True) -> None: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_AsciiString,theGravity : Message_Gravity=Message_Gravity.Message_Warning,putEndl : bool=True) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,thePrinter : Message_Printer) -> None: ...
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
class Message_Msg():
    """
    This class provides a tool for constructing the parametrized message basing on resources loaded by Message_MsgFile tool.
    """
    @overload
    def Arg(self,theString : str) -> Message_Msg: 
        """
        Set a value for %..s conversion

        Set a value for %..s conversion

        Set a value for %..s conversion

        Set a value for %..s conversion

        Set a value for %..s conversion

        Set a value for %..d, %..i, %..o, %..u, %..x or %..X conversion

        Set a value for %..f, %..e, %..E, %..g or %..G conversion

        Set a value for %..s conversion

        Set a value for %..s conversion

        Set a value for %..s conversion
        """
    @overload
    def Arg(self,theString : OCP.TCollection.TCollection_AsciiString) -> Message_Msg: ...
    @overload
    def Arg(self,theReal : float) -> Message_Msg: ...
    @overload
    def Arg(self,theString : OCP.TCollection.TCollection_HExtendedString) -> Message_Msg: ...
    @overload
    def Arg(self,theInt : int) -> Message_Msg: ...
    @overload
    def Arg(self,theString : OCP.TCollection.TCollection_ExtendedString) -> Message_Msg: ...
    @overload
    def Arg(self,theString : OCP.TCollection.TCollection_HAsciiString) -> Message_Msg: ...
    def Get(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Return the resulting message string with all parameters filled. If some parameters were not yet filled by calls to methods Arg (or <<), these parameters are filled by the word UNKNOWN
        """
    def IsEdited(self) -> bool: 
        """
        Tells if Value differs from Original

        Tells if Value differs from Original
        """
    def Original(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the original message text

        Returns the original message text
        """
    @overload
    def Set(self,theMsg : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Set a message body text -- can be used as alternative to using messages from resource file

        Set a message body text -- can be used as alternative to using messages from resource file
        """
    @overload
    def Set(self,theMsg : str) -> None: ...
    def Value(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns current state of the message text with parameters to the moment

        Returns current state of the message text with parameters to the moment
        """
    @overload
    def __init__(self,theKey : str) -> None: ...
    @overload
    def __init__(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> None: ...
    @overload
    def __init__(self,theMsg : Message_Msg) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Message_MsgFile():
    """
    A tool providing facility to load definitions of message strings from resource file(s).
    """
    @staticmethod
    def AddMsg_s(key : OCP.TCollection.TCollection_AsciiString,text : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Adds new message to the map. Parameter <key> gives the key of the message, <text> defines the message itself. If there already was defined the message identified by the same keyword, it is replaced with the new one.
        """
    @staticmethod
    def HasMsg_s(key : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Returns True if message with specified keyword is registered
        """
    @staticmethod
    def LoadFile_s(theFName : str) -> bool: 
        """
        Load the messages from the given file, additive to any previously loaded messages. Messages with same keywords, if already present, are replaced with the new ones.
        """
    @staticmethod
    def LoadFromEnv_s(theEnvName : str,theFileName : str,theLangExt : str='') -> bool: 
        """
        Loads the messages from the file with name (without extension) given by environment variable. Extension of the file name is given separately. If its not defined, it is taken: - by default from environment CSF_LANGUAGE, - if not defined either, as "us".
        """
    @staticmethod
    def LoadFromString_s(theContent : str,theLength : int=-1) -> bool: 
        """
        Loads the messages from the given text buffer.
        """
    @staticmethod
    def Load_s(theDirName : str,theFileName : str) -> bool: 
        """
        Load message file <theFileName> from directory <theDirName> or its sub-directory
        """
    @staticmethod
    @overload
    def Msg_s(key : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None

        Gives the text for the message identified by the keyword <key> If there are no messages with such keyword defined, the error message is returned. In that case reference to static string is returned, it can be chenged with next call(s) to Msg(). Note: The error message is constructed like 'Unknown message: <key>', and can itself be customized by defining message with key Message_Msg_BadKeyword.
        """
    @staticmethod
    @overload
    def Msg_s(key : str) -> OCP.TCollection.TCollection_ExtendedString: ...
    def __init__(self) -> None: ...
    pass
class Message_Printer(OCP.Standard.Standard_Transient):
    """
    Abstract interface class defining printer as output context for text messagesAbstract interface class defining printer as output context for text messagesAbstract interface class defining printer as output context for text messages
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
    def GetTraceLevel(self) -> Message_Gravity: 
        """
        Return trace level used for filtering messages; messages with lover gravity will be ignored.
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
    def Send(self,theString : OCP.TCollection.TCollection_AsciiString,theGravity : Message_Gravity,theToPutEol : bool) -> None: 
        """
        Send a string message with specified trace level. The parameter theToPutEol specified whether end-of-line should be added to the end of the message. This method must be redefined in descentant.

        Send a string message with specified trace level. The parameter theToPutEol specified whether end-of-line should be added to the end of the message. Default implementation calls first method Send().

        Send a string message with specified trace level. The parameter theToPutEol specified whether end-of-line should be added to the end of the message. Default implementation calls first method Send().
        """
    @overload
    def Send(self,theString : str,theGravity : Message_Gravity,theToPutEol : bool) -> None: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_ExtendedString,theGravity : Message_Gravity,theToPutEol : bool) -> None: ...
    def SetTraceLevel(self,theTraceLevel : Message_Gravity) -> None: 
        """
        Set trace level used for filtering messages. By default, trace level is Message_Info, so that all messages are output
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
class Message_PrinterOStream(Message_Printer, OCP.Standard.Standard_Transient):
    """
    Implementation of a message printer associated with an std::ostream The std::ostream may be either externally defined one (e.g. std::cout), or file stream maintained internally (depending on constructor).Implementation of a message printer associated with an std::ostream The std::ostream may be either externally defined one (e.g. std::cout), or file stream maintained internally (depending on constructor).Implementation of a message printer associated with an std::ostream The std::ostream may be either externally defined one (e.g. std::cout), or file stream maintained internally (depending on constructor).
    """
    def Close(self) -> None: 
        """
        Flushes the output stream and destroys it if it has been specified externally with option doFree (or if it is internal file stream)
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
    def GetStream(self) -> Any: 
        """
        Returns reference to the output stream
        """
    def GetTraceLevel(self) -> Message_Gravity: 
        """
        Return trace level used for filtering messages; messages with lover gravity will be ignored.
        """
    def GetUseUtf8(self) -> bool: 
        """
        Returns option to convert non-Ascii symbols to UTF8 encoding
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
    def Send(self,theString : OCP.TCollection.TCollection_ExtendedString,theGravity : Message_Gravity,putEndl : bool=True) -> None: 
        """
        Puts a message to the current stream if its gravity is equal or greater to the trace level set by SetTraceLevel()

        Puts a message to the current stream if its gravity is equal or greater to the trace level set by SetTraceLevel()

        Puts a message to the current stream if its gravity is equal or greater to the trace level set by SetTraceLevel() Non-Ascii symbols are converted to UTF-8 if UseUtf8 option is set, else replaced by symbols '?'
        """
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_AsciiString,theGravity : Message_Gravity,putEndl : bool=True) -> None: ...
    @overload
    def Send(self,theString : str,theGravity : Message_Gravity,putEndl : bool=True) -> None: ...
    def SetTraceLevel(self,theTraceLevel : Message_Gravity) -> None: 
        """
        Set trace level used for filtering messages. By default, trace level is Message_Info, so that all messages are output
        """
    def SetUseUtf8(self,useUtf8 : bool) -> None: 
        """
        Sets option to convert non-Ascii symbols to UTF8 encoding
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theFileName : str,theDoAppend : bool,theTraceLevel : Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def __init__(self,theTraceLevel : Message_Gravity=Message_Gravity.Message_Info) -> None: ...
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
class Message_ProgressIndicator(OCP.Standard.Standard_Transient):
    """
    Defines abstract interface from program to the "user". This includes progress indication and user break mechanisms.Defines abstract interface from program to the "user". This includes progress indication and user break mechanisms.Defines abstract interface from program to the "user". This includes progress indication and user break mechanisms.
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
    def EndScope(self) -> bool: 
        """
        Close the current scope and thus return to previous scale Updates position to be at the end of the closing scope Returns False if no scope is opened
        """
    def GetNbScopes(self) -> int: 
        """
        Returns current number of opened scopes This number is always >=1 as top-level scale is always present

        Returns current number of opened scopes This number is always >=1 as top-level scale is always present
        """
    def GetPosition(self) -> float: 
        """
        Returns total progress position on the basic scale ranged from 0. to 1.

        Returns total progress position on the basic scale ranged from 0. to 1.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetScale(self) -> Tuple[float, float, float, bool]: 
        """
        Returns all parameters for current scale
        """
    def GetScope(self,index : int) -> Message_ProgressScale: 
        """
        Returns data for scale of index-th scope The first scope is current one, the last is the top-level one

        Returns data for scale of index-th scope The first scope is current one, the last is the top-level one
        """
    def GetValue(self) -> float: 
        """
        Set and get progress value at current scale If the value to be set is more than currently set one, or out of range for the current scale, it is limited by that range
        """
    @overload
    def Increment(self) -> None: 
        """
        None

        Increment the progress value by the default of specified step

        None

        Increment the progress value by the default of specified step
        """
    @overload
    def Increment(self,step : float) -> None: ...
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
    def NewScope(self,name : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        None

        None

        None

        Creates new scope on a part of a current scale from current position with span either equal to default step, or specified The scale for the new scope will have specified name and ranged from 0 to 100 with step 1 Returns False if something is wrong in arguments or in current position of progress indicator; scope is opened anyway

        None

        None

        None
        """
    @overload
    def NewScope(self,name : str) -> bool: ...
    @overload
    def NewScope(self,span : float,name : str=None) -> bool: ...
    @overload
    def NewScope(self,name : str=None) -> bool: ...
    @overload
    def NewScope(self,span : float,name : OCP.TCollection.TCollection_HAsciiString) -> bool: ...
    @overload
    def NewScope(self,span : float,name : str) -> bool: ...
    @overload
    def NextScope(self,name : str=None) -> bool: 
        """
        None

        Optimized version of { return EndScope() && NewScope(); }

        None
        """
    @overload
    def NextScope(self,span : float,name : str=None) -> bool: ...
    @overload
    def NextScope(self,name : str) -> bool: ...
    def Reset(self) -> None: 
        """
        Drops all scopes and sets scale from 0 to 100, step 1 This scale has name "Step"
        """
    @overload
    def SetInfinite(self,isInf : bool) -> None: 
        """
        Set or drop infinite mode for the current scale

        Set or drop infinite mode for the current scale
        """
    @overload
    def SetInfinite(self,isInf : bool=True) -> None: ...
    @overload
    def SetName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None

        None
        """
    @overload
    def SetName(self,name : str) -> None: ...
    def SetRange(self,min : float,max : float) -> None: 
        """
        Set range for current scale

        Set range for current scale
        """
    @overload
    def SetScale(self,name : str,min : float,max : float,step : float,isInf : bool=False) -> None: 
        """
        None

        Set all parameters for current scale

        None
        """
    @overload
    def SetScale(self,name : str,min : float,max : float,step : float,isInf : bool) -> None: ...
    @overload
    def SetScale(self,min : float,max : float,step : float,isInf : bool=False) -> None: ...
    def SetStep(self,step : float) -> None: 
        """
        Set step for current scale

        Set step for current scale
        """
    def SetValue(self,val : float) -> None: 
        """
        None
        """
    def Show(self,force : bool=True) -> bool: 
        """
        Update presentation of the progress indicator Called when progress position is changed Flag force is intended for forcing update in case if it is optimized; all internal calls from ProgressIndicator are done with this flag equal to False
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UserBreak(self) -> bool: 
        """
        Should return True if user has send a break signal. Default implementation returns False.
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
class Message_ProgressScale():
    """
    Internal data structure for scale in ProgressIndicator
    """
    def BaseToLocal(self,val : float) -> float: 
        """
        Convert value from this scale to base one and back
        """
    def GetFirst(self) -> float: 
        """
        None

        None
        """
    def GetInfinite(self) -> bool: 
        """
        Gets flag for infinite scale

        Gets flag for infinite scale
        """
    def GetLast(self) -> float: 
        """
        Return information on span occupied by the scale on the base scale

        Return information on span occupied by the scale on the base scale
        """
    def GetMax(self) -> float: 
        """
        Gets minimum value of scale

        Gets minimum value of scale
        """
    def GetMin(self) -> float: 
        """
        Gets minimum value of scale

        Gets minimum value of scale
        """
    def GetName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Gets scale name Name may be Null handle if not set

        Gets scale name Name may be Null handle if not set
        """
    def GetStep(self) -> float: 
        """
        Gets default step

        Gets default step
        """
    def LocalToBase(self,val : float) -> float: 
        """
        None
        """
    @overload
    def SetInfinite(self,theInfinite : bool) -> None: 
        """
        Sets flag for infinite scale

        Sets flag for infinite scale
        """
    @overload
    def SetInfinite(self,theInfinite : bool=True) -> None: ...
    def SetMax(self,theMax : float) -> None: 
        """
        Sets minimum value of scale

        Sets minimum value of scale
        """
    def SetMin(self,theMin : float) -> None: 
        """
        Sets minimum value of scale

        Sets minimum value of scale
        """
    @overload
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None

        Sets scale name

        None

        Sets scale name
        """
    @overload
    def SetName(self,theName : str) -> None: ...
    @overload
    def SetRange(self,theMin : float,theMax : float) -> None: 
        """
        Set both min and max

        Set both min and max
        """
    @overload
    def SetRange(self,min : float,max : float) -> None: ...
    @overload
    def SetScale(self,min : float,max : float,step : float,theInfinite : bool=True) -> None: 
        """
        Set all scale parameters

        Set all scale parameters
        """
    @overload
    def SetScale(self,theMin : float,theMax : float,theStep : float,theInfinite : bool) -> None: ...
    @overload
    def SetSpan(self,first : float,last : float) -> None: 
        """
        Defines span occupied by the scale on the basis scale

        Defines span occupied by the scale on the basis scale
        """
    @overload
    def SetSpan(self,theFirst : float,theLast : float) -> None: ...
    def SetStep(self,theStep : float) -> None: 
        """
        Sets default step

        Sets default step
        """
    def __init__(self) -> None: ...
    pass
class Message_ProgressSentry():
    """
    This class is a tool allowing to manage opening/closing scopes in the ProgressIndicator in convenient and safe way.
    """
    def More(self) -> bool: 
        """
        Returns False if ProgressIndicator signals UserBreak

        Returns False if ProgressIndicator signals UserBreak
        """
    @overload
    def Next(self,span : float,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None

        None

        Closes current scope and opens next one with either specified or default span

        None

        None

        Closes current scope and opens next one with either specified or default span
        """
    @overload
    def Next(self,name : str=None) -> None: ...
    @overload
    def Next(self,name : str) -> None: ...
    @overload
    def Next(self,span : float,name : str=None) -> None: ...
    @overload
    def Next(self,span : float,name : str) -> None: ...
    def Relieve(self) -> None: 
        """
        Moves progress indicator to the end of the current scale and relieves sentry from its duty. Methods other than Show() will do nothing after this one is called.

        Moves progress indicator to the end of the current scale and relieves sentry from its duty. Methods other than Show() will do nothing after this one is called.
        """
    def Show(self) -> None: 
        """
        Forces update of progress indicator display

        Forces update of progress indicator display
        """
    @overload
    def __init__(self,PI : Message_ProgressIndicator,name : str,min : float,max : float,step : float,isInf : bool=False,newScopeSpan : float=0.0) -> None: ...
    @overload
    def __init__(self,PI : Message_ProgressIndicator,name : OCP.TCollection.TCollection_HAsciiString,min : float,max : float,step : float,isInf : bool=False,newScopeSpan : float=0.0) -> None: ...
    pass
class Message_Report(OCP.Standard.Standard_Transient):
    """
    Container for alert messages, sorted according to their gravity.Container for alert messages, sorted according to their gravity.Container for alert messages, sorted according to their gravity.
    """
    def AddAlert(self,theGravity : Message_Gravity,theAlert : Message_Alert) -> None: 
        """
        Add alert with specified gravity. This method is thread-safe, i.e. alerts can be added from parallel threads safely.
        """
    @overload
    def Clear(self,theType : OCP.Standard.Standard_Type) -> None: 
        """
        Clears all collected alerts

        Clears collected alerts with specified gravity

        Clears collected alerts with specified type
        """
    @overload
    def Clear(self) -> None: ...
    @overload
    def Clear(self,theGravity : Message_Gravity) -> None: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Dump(self,theOS : Any) -> None: 
        """
        Dumps all collected alerts to stream

        Dumps collected alerts with specified gravity to stream
        """
    @overload
    def Dump(self,theOS : Any,theGravity : Message_Gravity) -> None: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetAlerts(self,theGravity : Message_Gravity) -> Message_ListOfAlert: 
        """
        Returns list of collected alerts with specified gravity
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def HasAlert(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if specific type of alert is recorded

        Returns true if specific type of alert is recorded with specified gravity
        """
    @overload
    def HasAlert(self,theType : OCP.Standard.Standard_Type,theGravity : Message_Gravity) -> bool: ...
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
    def Merge(self,theOther : Message_Report) -> None: 
        """
        Merges data from theOther report into this

        Merges alerts with specified gravity from theOther report into this
        """
    @overload
    def Merge(self,theOther : Message_Report,theGravity : Message_Gravity) -> None: ...
    @overload
    def SendMessages(self,theMessenger : Message_Messenger) -> None: 
        """
        Sends all collected alerts to messenger

        Dumps collected alerts with specified gravity to messenger
        """
    @overload
    def SendMessages(self,theMessenger : Message_Messenger,theGravity : Message_Gravity) -> None: ...
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
class Message_SequenceOfPrinters(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Message_Printer) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Message_SequenceOfPrinters) -> None: ...
    def Assign(self,theOther : Message_SequenceOfPrinters) -> Message_SequenceOfPrinters: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Message_Printer: 
        """
        First item access
        """
    def ChangeLast(self) -> Message_Printer: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Message_Printer: 
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
    def First(self) -> Message_Printer: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Message_SequenceOfPrinters) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Message_Printer) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Message_Printer) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Message_SequenceOfPrinters) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Message_Printer: 
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
    def Prepend(self,theSeq : Message_SequenceOfPrinters) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Message_Printer) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Message_Printer) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Message_SequenceOfPrinters) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Message_Printer: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Message_SequenceOfPrinters) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Message_SequenceOfProgressScale(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Message_ProgressScale) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Message_SequenceOfProgressScale) -> None: ...
    def Assign(self,theOther : Message_SequenceOfProgressScale) -> Message_SequenceOfProgressScale: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Message_ProgressScale: 
        """
        First item access
        """
    def ChangeLast(self) -> Message_ProgressScale: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Message_ProgressScale: 
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
    def First(self) -> Message_ProgressScale: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Message_SequenceOfProgressScale) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Message_ProgressScale) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Message_ProgressScale) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Message_SequenceOfProgressScale) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Message_ProgressScale: 
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
    def Prepend(self,theSeq : Message_SequenceOfProgressScale) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Message_ProgressScale) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Message_ProgressScale) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Message_SequenceOfProgressScale) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Message_ProgressScale: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Message_SequenceOfProgressScale) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Message_Status():
    """
    Enumeration covering all execution statuses supported by the class Message_ExecStatus: 32 statuses per each of 4 types (DONE, WARN, ALARM, FAIL)

    Members:

      Message_None

      Message_Done1

      Message_Done2

      Message_Done3

      Message_Done4

      Message_Done5

      Message_Done6

      Message_Done7

      Message_Done8

      Message_Done9

      Message_Done10

      Message_Done11

      Message_Done12

      Message_Done13

      Message_Done14

      Message_Done15

      Message_Done16

      Message_Done17

      Message_Done18

      Message_Done19

      Message_Done20

      Message_Done21

      Message_Done22

      Message_Done23

      Message_Done24

      Message_Done25

      Message_Done26

      Message_Done27

      Message_Done28

      Message_Done29

      Message_Done30

      Message_Done31

      Message_Done32

      Message_Warn1

      Message_Warn2

      Message_Warn3

      Message_Warn4

      Message_Warn5

      Message_Warn6

      Message_Warn7

      Message_Warn8

      Message_Warn9

      Message_Warn10

      Message_Warn11

      Message_Warn12

      Message_Warn13

      Message_Warn14

      Message_Warn15

      Message_Warn16

      Message_Warn17

      Message_Warn18

      Message_Warn19

      Message_Warn20

      Message_Warn21

      Message_Warn22

      Message_Warn23

      Message_Warn24

      Message_Warn25

      Message_Warn26

      Message_Warn27

      Message_Warn28

      Message_Warn29

      Message_Warn30

      Message_Warn31

      Message_Warn32

      Message_Alarm1

      Message_Alarm2

      Message_Alarm3

      Message_Alarm4

      Message_Alarm5

      Message_Alarm6

      Message_Alarm7

      Message_Alarm8

      Message_Alarm9

      Message_Alarm10

      Message_Alarm11

      Message_Alarm12

      Message_Alarm13

      Message_Alarm14

      Message_Alarm15

      Message_Alarm16

      Message_Alarm17

      Message_Alarm18

      Message_Alarm19

      Message_Alarm20

      Message_Alarm21

      Message_Alarm22

      Message_Alarm23

      Message_Alarm24

      Message_Alarm25

      Message_Alarm26

      Message_Alarm27

      Message_Alarm28

      Message_Alarm29

      Message_Alarm30

      Message_Alarm31

      Message_Alarm32

      Message_Fail1

      Message_Fail2

      Message_Fail3

      Message_Fail4

      Message_Fail5

      Message_Fail6

      Message_Fail7

      Message_Fail8

      Message_Fail9

      Message_Fail10

      Message_Fail11

      Message_Fail12

      Message_Fail13

      Message_Fail14

      Message_Fail15

      Message_Fail16

      Message_Fail17

      Message_Fail18

      Message_Fail19

      Message_Fail20

      Message_Fail21

      Message_Fail22

      Message_Fail23

      Message_Fail24

      Message_Fail25

      Message_Fail26

      Message_Fail27

      Message_Fail28

      Message_Fail29

      Message_Fail30

      Message_Fail31

      Message_Fail32
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Message_Alarm1: OCP.Message.Message_Status # value = Message_Status.Message_Alarm1
    Message_Alarm10: OCP.Message.Message_Status # value = Message_Status.Message_Alarm10
    Message_Alarm11: OCP.Message.Message_Status # value = Message_Status.Message_Alarm11
    Message_Alarm12: OCP.Message.Message_Status # value = Message_Status.Message_Alarm12
    Message_Alarm13: OCP.Message.Message_Status # value = Message_Status.Message_Alarm13
    Message_Alarm14: OCP.Message.Message_Status # value = Message_Status.Message_Alarm14
    Message_Alarm15: OCP.Message.Message_Status # value = Message_Status.Message_Alarm15
    Message_Alarm16: OCP.Message.Message_Status # value = Message_Status.Message_Alarm16
    Message_Alarm17: OCP.Message.Message_Status # value = Message_Status.Message_Alarm17
    Message_Alarm18: OCP.Message.Message_Status # value = Message_Status.Message_Alarm18
    Message_Alarm19: OCP.Message.Message_Status # value = Message_Status.Message_Alarm19
    Message_Alarm2: OCP.Message.Message_Status # value = Message_Status.Message_Alarm2
    Message_Alarm20: OCP.Message.Message_Status # value = Message_Status.Message_Alarm20
    Message_Alarm21: OCP.Message.Message_Status # value = Message_Status.Message_Alarm21
    Message_Alarm22: OCP.Message.Message_Status # value = Message_Status.Message_Alarm22
    Message_Alarm23: OCP.Message.Message_Status # value = Message_Status.Message_Alarm23
    Message_Alarm24: OCP.Message.Message_Status # value = Message_Status.Message_Alarm24
    Message_Alarm25: OCP.Message.Message_Status # value = Message_Status.Message_Alarm25
    Message_Alarm26: OCP.Message.Message_Status # value = Message_Status.Message_Alarm26
    Message_Alarm27: OCP.Message.Message_Status # value = Message_Status.Message_Alarm27
    Message_Alarm28: OCP.Message.Message_Status # value = Message_Status.Message_Alarm28
    Message_Alarm29: OCP.Message.Message_Status # value = Message_Status.Message_Alarm29
    Message_Alarm3: OCP.Message.Message_Status # value = Message_Status.Message_Alarm3
    Message_Alarm30: OCP.Message.Message_Status # value = Message_Status.Message_Alarm30
    Message_Alarm31: OCP.Message.Message_Status # value = Message_Status.Message_Alarm31
    Message_Alarm32: OCP.Message.Message_Status # value = Message_Status.Message_Alarm32
    Message_Alarm4: OCP.Message.Message_Status # value = Message_Status.Message_Alarm4
    Message_Alarm5: OCP.Message.Message_Status # value = Message_Status.Message_Alarm5
    Message_Alarm6: OCP.Message.Message_Status # value = Message_Status.Message_Alarm6
    Message_Alarm7: OCP.Message.Message_Status # value = Message_Status.Message_Alarm7
    Message_Alarm8: OCP.Message.Message_Status # value = Message_Status.Message_Alarm8
    Message_Alarm9: OCP.Message.Message_Status # value = Message_Status.Message_Alarm9
    Message_Done1: OCP.Message.Message_Status # value = Message_Status.Message_Done1
    Message_Done10: OCP.Message.Message_Status # value = Message_Status.Message_Done10
    Message_Done11: OCP.Message.Message_Status # value = Message_Status.Message_Done11
    Message_Done12: OCP.Message.Message_Status # value = Message_Status.Message_Done12
    Message_Done13: OCP.Message.Message_Status # value = Message_Status.Message_Done13
    Message_Done14: OCP.Message.Message_Status # value = Message_Status.Message_Done14
    Message_Done15: OCP.Message.Message_Status # value = Message_Status.Message_Done15
    Message_Done16: OCP.Message.Message_Status # value = Message_Status.Message_Done16
    Message_Done17: OCP.Message.Message_Status # value = Message_Status.Message_Done17
    Message_Done18: OCP.Message.Message_Status # value = Message_Status.Message_Done18
    Message_Done19: OCP.Message.Message_Status # value = Message_Status.Message_Done19
    Message_Done2: OCP.Message.Message_Status # value = Message_Status.Message_Done2
    Message_Done20: OCP.Message.Message_Status # value = Message_Status.Message_Done20
    Message_Done21: OCP.Message.Message_Status # value = Message_Status.Message_Done21
    Message_Done22: OCP.Message.Message_Status # value = Message_Status.Message_Done22
    Message_Done23: OCP.Message.Message_Status # value = Message_Status.Message_Done23
    Message_Done24: OCP.Message.Message_Status # value = Message_Status.Message_Done24
    Message_Done25: OCP.Message.Message_Status # value = Message_Status.Message_Done25
    Message_Done26: OCP.Message.Message_Status # value = Message_Status.Message_Done26
    Message_Done27: OCP.Message.Message_Status # value = Message_Status.Message_Done27
    Message_Done28: OCP.Message.Message_Status # value = Message_Status.Message_Done28
    Message_Done29: OCP.Message.Message_Status # value = Message_Status.Message_Done29
    Message_Done3: OCP.Message.Message_Status # value = Message_Status.Message_Done3
    Message_Done30: OCP.Message.Message_Status # value = Message_Status.Message_Done30
    Message_Done31: OCP.Message.Message_Status # value = Message_Status.Message_Done31
    Message_Done32: OCP.Message.Message_Status # value = Message_Status.Message_Done32
    Message_Done4: OCP.Message.Message_Status # value = Message_Status.Message_Done4
    Message_Done5: OCP.Message.Message_Status # value = Message_Status.Message_Done5
    Message_Done6: OCP.Message.Message_Status # value = Message_Status.Message_Done6
    Message_Done7: OCP.Message.Message_Status # value = Message_Status.Message_Done7
    Message_Done8: OCP.Message.Message_Status # value = Message_Status.Message_Done8
    Message_Done9: OCP.Message.Message_Status # value = Message_Status.Message_Done9
    Message_Fail1: OCP.Message.Message_Status # value = Message_Status.Message_Fail1
    Message_Fail10: OCP.Message.Message_Status # value = Message_Status.Message_Fail10
    Message_Fail11: OCP.Message.Message_Status # value = Message_Status.Message_Fail11
    Message_Fail12: OCP.Message.Message_Status # value = Message_Status.Message_Fail12
    Message_Fail13: OCP.Message.Message_Status # value = Message_Status.Message_Fail13
    Message_Fail14: OCP.Message.Message_Status # value = Message_Status.Message_Fail14
    Message_Fail15: OCP.Message.Message_Status # value = Message_Status.Message_Fail15
    Message_Fail16: OCP.Message.Message_Status # value = Message_Status.Message_Fail16
    Message_Fail17: OCP.Message.Message_Status # value = Message_Status.Message_Fail17
    Message_Fail18: OCP.Message.Message_Status # value = Message_Status.Message_Fail18
    Message_Fail19: OCP.Message.Message_Status # value = Message_Status.Message_Fail19
    Message_Fail2: OCP.Message.Message_Status # value = Message_Status.Message_Fail2
    Message_Fail20: OCP.Message.Message_Status # value = Message_Status.Message_Fail20
    Message_Fail21: OCP.Message.Message_Status # value = Message_Status.Message_Fail21
    Message_Fail22: OCP.Message.Message_Status # value = Message_Status.Message_Fail22
    Message_Fail23: OCP.Message.Message_Status # value = Message_Status.Message_Fail23
    Message_Fail24: OCP.Message.Message_Status # value = Message_Status.Message_Fail24
    Message_Fail25: OCP.Message.Message_Status # value = Message_Status.Message_Fail25
    Message_Fail26: OCP.Message.Message_Status # value = Message_Status.Message_Fail26
    Message_Fail27: OCP.Message.Message_Status # value = Message_Status.Message_Fail27
    Message_Fail28: OCP.Message.Message_Status # value = Message_Status.Message_Fail28
    Message_Fail29: OCP.Message.Message_Status # value = Message_Status.Message_Fail29
    Message_Fail3: OCP.Message.Message_Status # value = Message_Status.Message_Fail3
    Message_Fail30: OCP.Message.Message_Status # value = Message_Status.Message_Fail30
    Message_Fail31: OCP.Message.Message_Status # value = Message_Status.Message_Fail31
    Message_Fail32: OCP.Message.Message_Status # value = Message_Status.Message_Fail32
    Message_Fail4: OCP.Message.Message_Status # value = Message_Status.Message_Fail4
    Message_Fail5: OCP.Message.Message_Status # value = Message_Status.Message_Fail5
    Message_Fail6: OCP.Message.Message_Status # value = Message_Status.Message_Fail6
    Message_Fail7: OCP.Message.Message_Status # value = Message_Status.Message_Fail7
    Message_Fail8: OCP.Message.Message_Status # value = Message_Status.Message_Fail8
    Message_Fail9: OCP.Message.Message_Status # value = Message_Status.Message_Fail9
    Message_None: OCP.Message.Message_Status # value = Message_Status.Message_None
    Message_Warn1: OCP.Message.Message_Status # value = Message_Status.Message_Warn1
    Message_Warn10: OCP.Message.Message_Status # value = Message_Status.Message_Warn10
    Message_Warn11: OCP.Message.Message_Status # value = Message_Status.Message_Warn11
    Message_Warn12: OCP.Message.Message_Status # value = Message_Status.Message_Warn12
    Message_Warn13: OCP.Message.Message_Status # value = Message_Status.Message_Warn13
    Message_Warn14: OCP.Message.Message_Status # value = Message_Status.Message_Warn14
    Message_Warn15: OCP.Message.Message_Status # value = Message_Status.Message_Warn15
    Message_Warn16: OCP.Message.Message_Status # value = Message_Status.Message_Warn16
    Message_Warn17: OCP.Message.Message_Status # value = Message_Status.Message_Warn17
    Message_Warn18: OCP.Message.Message_Status # value = Message_Status.Message_Warn18
    Message_Warn19: OCP.Message.Message_Status # value = Message_Status.Message_Warn19
    Message_Warn2: OCP.Message.Message_Status # value = Message_Status.Message_Warn2
    Message_Warn20: OCP.Message.Message_Status # value = Message_Status.Message_Warn20
    Message_Warn21: OCP.Message.Message_Status # value = Message_Status.Message_Warn21
    Message_Warn22: OCP.Message.Message_Status # value = Message_Status.Message_Warn22
    Message_Warn23: OCP.Message.Message_Status # value = Message_Status.Message_Warn23
    Message_Warn24: OCP.Message.Message_Status # value = Message_Status.Message_Warn24
    Message_Warn25: OCP.Message.Message_Status # value = Message_Status.Message_Warn25
    Message_Warn26: OCP.Message.Message_Status # value = Message_Status.Message_Warn26
    Message_Warn27: OCP.Message.Message_Status # value = Message_Status.Message_Warn27
    Message_Warn28: OCP.Message.Message_Status # value = Message_Status.Message_Warn28
    Message_Warn29: OCP.Message.Message_Status # value = Message_Status.Message_Warn29
    Message_Warn3: OCP.Message.Message_Status # value = Message_Status.Message_Warn3
    Message_Warn30: OCP.Message.Message_Status # value = Message_Status.Message_Warn30
    Message_Warn31: OCP.Message.Message_Status # value = Message_Status.Message_Warn31
    Message_Warn32: OCP.Message.Message_Status # value = Message_Status.Message_Warn32
    Message_Warn4: OCP.Message.Message_Status # value = Message_Status.Message_Warn4
    Message_Warn5: OCP.Message.Message_Status # value = Message_Status.Message_Warn5
    Message_Warn6: OCP.Message.Message_Status # value = Message_Status.Message_Warn6
    Message_Warn7: OCP.Message.Message_Status # value = Message_Status.Message_Warn7
    Message_Warn8: OCP.Message.Message_Status # value = Message_Status.Message_Warn8
    Message_Warn9: OCP.Message.Message_Status # value = Message_Status.Message_Warn9
    __entries: dict # value = {'Message_None': (Message_Status.Message_None, None), 'Message_Done1': (Message_Status.Message_Done1, None), 'Message_Done2': (Message_Status.Message_Done2, None), 'Message_Done3': (Message_Status.Message_Done3, None), 'Message_Done4': (Message_Status.Message_Done4, None), 'Message_Done5': (Message_Status.Message_Done5, None), 'Message_Done6': (Message_Status.Message_Done6, None), 'Message_Done7': (Message_Status.Message_Done7, None), 'Message_Done8': (Message_Status.Message_Done8, None), 'Message_Done9': (Message_Status.Message_Done9, None), 'Message_Done10': (Message_Status.Message_Done10, None), 'Message_Done11': (Message_Status.Message_Done11, None), 'Message_Done12': (Message_Status.Message_Done12, None), 'Message_Done13': (Message_Status.Message_Done13, None), 'Message_Done14': (Message_Status.Message_Done14, None), 'Message_Done15': (Message_Status.Message_Done15, None), 'Message_Done16': (Message_Status.Message_Done16, None), 'Message_Done17': (Message_Status.Message_Done17, None), 'Message_Done18': (Message_Status.Message_Done18, None), 'Message_Done19': (Message_Status.Message_Done19, None), 'Message_Done20': (Message_Status.Message_Done20, None), 'Message_Done21': (Message_Status.Message_Done21, None), 'Message_Done22': (Message_Status.Message_Done22, None), 'Message_Done23': (Message_Status.Message_Done23, None), 'Message_Done24': (Message_Status.Message_Done24, None), 'Message_Done25': (Message_Status.Message_Done25, None), 'Message_Done26': (Message_Status.Message_Done26, None), 'Message_Done27': (Message_Status.Message_Done27, None), 'Message_Done28': (Message_Status.Message_Done28, None), 'Message_Done29': (Message_Status.Message_Done29, None), 'Message_Done30': (Message_Status.Message_Done30, None), 'Message_Done31': (Message_Status.Message_Done31, None), 'Message_Done32': (Message_Status.Message_Done32, None), 'Message_Warn1': (Message_Status.Message_Warn1, None), 'Message_Warn2': (Message_Status.Message_Warn2, None), 'Message_Warn3': (Message_Status.Message_Warn3, None), 'Message_Warn4': (Message_Status.Message_Warn4, None), 'Message_Warn5': (Message_Status.Message_Warn5, None), 'Message_Warn6': (Message_Status.Message_Warn6, None), 'Message_Warn7': (Message_Status.Message_Warn7, None), 'Message_Warn8': (Message_Status.Message_Warn8, None), 'Message_Warn9': (Message_Status.Message_Warn9, None), 'Message_Warn10': (Message_Status.Message_Warn10, None), 'Message_Warn11': (Message_Status.Message_Warn11, None), 'Message_Warn12': (Message_Status.Message_Warn12, None), 'Message_Warn13': (Message_Status.Message_Warn13, None), 'Message_Warn14': (Message_Status.Message_Warn14, None), 'Message_Warn15': (Message_Status.Message_Warn15, None), 'Message_Warn16': (Message_Status.Message_Warn16, None), 'Message_Warn17': (Message_Status.Message_Warn17, None), 'Message_Warn18': (Message_Status.Message_Warn18, None), 'Message_Warn19': (Message_Status.Message_Warn19, None), 'Message_Warn20': (Message_Status.Message_Warn20, None), 'Message_Warn21': (Message_Status.Message_Warn21, None), 'Message_Warn22': (Message_Status.Message_Warn22, None), 'Message_Warn23': (Message_Status.Message_Warn23, None), 'Message_Warn24': (Message_Status.Message_Warn24, None), 'Message_Warn25': (Message_Status.Message_Warn25, None), 'Message_Warn26': (Message_Status.Message_Warn26, None), 'Message_Warn27': (Message_Status.Message_Warn27, None), 'Message_Warn28': (Message_Status.Message_Warn28, None), 'Message_Warn29': (Message_Status.Message_Warn29, None), 'Message_Warn30': (Message_Status.Message_Warn30, None), 'Message_Warn31': (Message_Status.Message_Warn31, None), 'Message_Warn32': (Message_Status.Message_Warn32, None), 'Message_Alarm1': (Message_Status.Message_Alarm1, None), 'Message_Alarm2': (Message_Status.Message_Alarm2, None), 'Message_Alarm3': (Message_Status.Message_Alarm3, None), 'Message_Alarm4': (Message_Status.Message_Alarm4, None), 'Message_Alarm5': (Message_Status.Message_Alarm5, None), 'Message_Alarm6': (Message_Status.Message_Alarm6, None), 'Message_Alarm7': (Message_Status.Message_Alarm7, None), 'Message_Alarm8': (Message_Status.Message_Alarm8, None), 'Message_Alarm9': (Message_Status.Message_Alarm9, None), 'Message_Alarm10': (Message_Status.Message_Alarm10, None), 'Message_Alarm11': (Message_Status.Message_Alarm11, None), 'Message_Alarm12': (Message_Status.Message_Alarm12, None), 'Message_Alarm13': (Message_Status.Message_Alarm13, None), 'Message_Alarm14': (Message_Status.Message_Alarm14, None), 'Message_Alarm15': (Message_Status.Message_Alarm15, None), 'Message_Alarm16': (Message_Status.Message_Alarm16, None), 'Message_Alarm17': (Message_Status.Message_Alarm17, None), 'Message_Alarm18': (Message_Status.Message_Alarm18, None), 'Message_Alarm19': (Message_Status.Message_Alarm19, None), 'Message_Alarm20': (Message_Status.Message_Alarm20, None), 'Message_Alarm21': (Message_Status.Message_Alarm21, None), 'Message_Alarm22': (Message_Status.Message_Alarm22, None), 'Message_Alarm23': (Message_Status.Message_Alarm23, None), 'Message_Alarm24': (Message_Status.Message_Alarm24, None), 'Message_Alarm25': (Message_Status.Message_Alarm25, None), 'Message_Alarm26': (Message_Status.Message_Alarm26, None), 'Message_Alarm27': (Message_Status.Message_Alarm27, None), 'Message_Alarm28': (Message_Status.Message_Alarm28, None), 'Message_Alarm29': (Message_Status.Message_Alarm29, None), 'Message_Alarm30': (Message_Status.Message_Alarm30, None), 'Message_Alarm31': (Message_Status.Message_Alarm31, None), 'Message_Alarm32': (Message_Status.Message_Alarm32, None), 'Message_Fail1': (Message_Status.Message_Fail1, None), 'Message_Fail2': (Message_Status.Message_Fail2, None), 'Message_Fail3': (Message_Status.Message_Fail3, None), 'Message_Fail4': (Message_Status.Message_Fail4, None), 'Message_Fail5': (Message_Status.Message_Fail5, None), 'Message_Fail6': (Message_Status.Message_Fail6, None), 'Message_Fail7': (Message_Status.Message_Fail7, None), 'Message_Fail8': (Message_Status.Message_Fail8, None), 'Message_Fail9': (Message_Status.Message_Fail9, None), 'Message_Fail10': (Message_Status.Message_Fail10, None), 'Message_Fail11': (Message_Status.Message_Fail11, None), 'Message_Fail12': (Message_Status.Message_Fail12, None), 'Message_Fail13': (Message_Status.Message_Fail13, None), 'Message_Fail14': (Message_Status.Message_Fail14, None), 'Message_Fail15': (Message_Status.Message_Fail15, None), 'Message_Fail16': (Message_Status.Message_Fail16, None), 'Message_Fail17': (Message_Status.Message_Fail17, None), 'Message_Fail18': (Message_Status.Message_Fail18, None), 'Message_Fail19': (Message_Status.Message_Fail19, None), 'Message_Fail20': (Message_Status.Message_Fail20, None), 'Message_Fail21': (Message_Status.Message_Fail21, None), 'Message_Fail22': (Message_Status.Message_Fail22, None), 'Message_Fail23': (Message_Status.Message_Fail23, None), 'Message_Fail24': (Message_Status.Message_Fail24, None), 'Message_Fail25': (Message_Status.Message_Fail25, None), 'Message_Fail26': (Message_Status.Message_Fail26, None), 'Message_Fail27': (Message_Status.Message_Fail27, None), 'Message_Fail28': (Message_Status.Message_Fail28, None), 'Message_Fail29': (Message_Status.Message_Fail29, None), 'Message_Fail30': (Message_Status.Message_Fail30, None), 'Message_Fail31': (Message_Status.Message_Fail31, None), 'Message_Fail32': (Message_Status.Message_Fail32, None)}
    __members__: dict # value = {'Message_None': Message_Status.Message_None, 'Message_Done1': Message_Status.Message_Done1, 'Message_Done2': Message_Status.Message_Done2, 'Message_Done3': Message_Status.Message_Done3, 'Message_Done4': Message_Status.Message_Done4, 'Message_Done5': Message_Status.Message_Done5, 'Message_Done6': Message_Status.Message_Done6, 'Message_Done7': Message_Status.Message_Done7, 'Message_Done8': Message_Status.Message_Done8, 'Message_Done9': Message_Status.Message_Done9, 'Message_Done10': Message_Status.Message_Done10, 'Message_Done11': Message_Status.Message_Done11, 'Message_Done12': Message_Status.Message_Done12, 'Message_Done13': Message_Status.Message_Done13, 'Message_Done14': Message_Status.Message_Done14, 'Message_Done15': Message_Status.Message_Done15, 'Message_Done16': Message_Status.Message_Done16, 'Message_Done17': Message_Status.Message_Done17, 'Message_Done18': Message_Status.Message_Done18, 'Message_Done19': Message_Status.Message_Done19, 'Message_Done20': Message_Status.Message_Done20, 'Message_Done21': Message_Status.Message_Done21, 'Message_Done22': Message_Status.Message_Done22, 'Message_Done23': Message_Status.Message_Done23, 'Message_Done24': Message_Status.Message_Done24, 'Message_Done25': Message_Status.Message_Done25, 'Message_Done26': Message_Status.Message_Done26, 'Message_Done27': Message_Status.Message_Done27, 'Message_Done28': Message_Status.Message_Done28, 'Message_Done29': Message_Status.Message_Done29, 'Message_Done30': Message_Status.Message_Done30, 'Message_Done31': Message_Status.Message_Done31, 'Message_Done32': Message_Status.Message_Done32, 'Message_Warn1': Message_Status.Message_Warn1, 'Message_Warn2': Message_Status.Message_Warn2, 'Message_Warn3': Message_Status.Message_Warn3, 'Message_Warn4': Message_Status.Message_Warn4, 'Message_Warn5': Message_Status.Message_Warn5, 'Message_Warn6': Message_Status.Message_Warn6, 'Message_Warn7': Message_Status.Message_Warn7, 'Message_Warn8': Message_Status.Message_Warn8, 'Message_Warn9': Message_Status.Message_Warn9, 'Message_Warn10': Message_Status.Message_Warn10, 'Message_Warn11': Message_Status.Message_Warn11, 'Message_Warn12': Message_Status.Message_Warn12, 'Message_Warn13': Message_Status.Message_Warn13, 'Message_Warn14': Message_Status.Message_Warn14, 'Message_Warn15': Message_Status.Message_Warn15, 'Message_Warn16': Message_Status.Message_Warn16, 'Message_Warn17': Message_Status.Message_Warn17, 'Message_Warn18': Message_Status.Message_Warn18, 'Message_Warn19': Message_Status.Message_Warn19, 'Message_Warn20': Message_Status.Message_Warn20, 'Message_Warn21': Message_Status.Message_Warn21, 'Message_Warn22': Message_Status.Message_Warn22, 'Message_Warn23': Message_Status.Message_Warn23, 'Message_Warn24': Message_Status.Message_Warn24, 'Message_Warn25': Message_Status.Message_Warn25, 'Message_Warn26': Message_Status.Message_Warn26, 'Message_Warn27': Message_Status.Message_Warn27, 'Message_Warn28': Message_Status.Message_Warn28, 'Message_Warn29': Message_Status.Message_Warn29, 'Message_Warn30': Message_Status.Message_Warn30, 'Message_Warn31': Message_Status.Message_Warn31, 'Message_Warn32': Message_Status.Message_Warn32, 'Message_Alarm1': Message_Status.Message_Alarm1, 'Message_Alarm2': Message_Status.Message_Alarm2, 'Message_Alarm3': Message_Status.Message_Alarm3, 'Message_Alarm4': Message_Status.Message_Alarm4, 'Message_Alarm5': Message_Status.Message_Alarm5, 'Message_Alarm6': Message_Status.Message_Alarm6, 'Message_Alarm7': Message_Status.Message_Alarm7, 'Message_Alarm8': Message_Status.Message_Alarm8, 'Message_Alarm9': Message_Status.Message_Alarm9, 'Message_Alarm10': Message_Status.Message_Alarm10, 'Message_Alarm11': Message_Status.Message_Alarm11, 'Message_Alarm12': Message_Status.Message_Alarm12, 'Message_Alarm13': Message_Status.Message_Alarm13, 'Message_Alarm14': Message_Status.Message_Alarm14, 'Message_Alarm15': Message_Status.Message_Alarm15, 'Message_Alarm16': Message_Status.Message_Alarm16, 'Message_Alarm17': Message_Status.Message_Alarm17, 'Message_Alarm18': Message_Status.Message_Alarm18, 'Message_Alarm19': Message_Status.Message_Alarm19, 'Message_Alarm20': Message_Status.Message_Alarm20, 'Message_Alarm21': Message_Status.Message_Alarm21, 'Message_Alarm22': Message_Status.Message_Alarm22, 'Message_Alarm23': Message_Status.Message_Alarm23, 'Message_Alarm24': Message_Status.Message_Alarm24, 'Message_Alarm25': Message_Status.Message_Alarm25, 'Message_Alarm26': Message_Status.Message_Alarm26, 'Message_Alarm27': Message_Status.Message_Alarm27, 'Message_Alarm28': Message_Status.Message_Alarm28, 'Message_Alarm29': Message_Status.Message_Alarm29, 'Message_Alarm30': Message_Status.Message_Alarm30, 'Message_Alarm31': Message_Status.Message_Alarm31, 'Message_Alarm32': Message_Status.Message_Alarm32, 'Message_Fail1': Message_Status.Message_Fail1, 'Message_Fail2': Message_Status.Message_Fail2, 'Message_Fail3': Message_Status.Message_Fail3, 'Message_Fail4': Message_Status.Message_Fail4, 'Message_Fail5': Message_Status.Message_Fail5, 'Message_Fail6': Message_Status.Message_Fail6, 'Message_Fail7': Message_Status.Message_Fail7, 'Message_Fail8': Message_Status.Message_Fail8, 'Message_Fail9': Message_Status.Message_Fail9, 'Message_Fail10': Message_Status.Message_Fail10, 'Message_Fail11': Message_Status.Message_Fail11, 'Message_Fail12': Message_Status.Message_Fail12, 'Message_Fail13': Message_Status.Message_Fail13, 'Message_Fail14': Message_Status.Message_Fail14, 'Message_Fail15': Message_Status.Message_Fail15, 'Message_Fail16': Message_Status.Message_Fail16, 'Message_Fail17': Message_Status.Message_Fail17, 'Message_Fail18': Message_Status.Message_Fail18, 'Message_Fail19': Message_Status.Message_Fail19, 'Message_Fail20': Message_Status.Message_Fail20, 'Message_Fail21': Message_Status.Message_Fail21, 'Message_Fail22': Message_Status.Message_Fail22, 'Message_Fail23': Message_Status.Message_Fail23, 'Message_Fail24': Message_Status.Message_Fail24, 'Message_Fail25': Message_Status.Message_Fail25, 'Message_Fail26': Message_Status.Message_Fail26, 'Message_Fail27': Message_Status.Message_Fail27, 'Message_Fail28': Message_Status.Message_Fail28, 'Message_Fail29': Message_Status.Message_Fail29, 'Message_Fail30': Message_Status.Message_Fail30, 'Message_Fail31': Message_Status.Message_Fail31, 'Message_Fail32': Message_Status.Message_Fail32}
    pass
class Message_StatusType():
    """
    Definition of types of execution status supported by the class Message_ExecStatus

    Members:

      Message_DONE

      Message_WARN

      Message_ALARM

      Message_FAIL
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Message_ALARM: OCP.Message.Message_StatusType # value = Message_StatusType.Message_ALARM
    Message_DONE: OCP.Message.Message_StatusType # value = Message_StatusType.Message_DONE
    Message_FAIL: OCP.Message.Message_StatusType # value = Message_StatusType.Message_FAIL
    Message_WARN: OCP.Message.Message_StatusType # value = Message_StatusType.Message_WARN
    __entries: dict # value = {'Message_DONE': (Message_StatusType.Message_DONE, None), 'Message_WARN': (Message_StatusType.Message_WARN, None), 'Message_ALARM': (Message_StatusType.Message_ALARM, None), 'Message_FAIL': (Message_StatusType.Message_FAIL, None)}
    __members__: dict # value = {'Message_DONE': Message_StatusType.Message_DONE, 'Message_WARN': Message_StatusType.Message_WARN, 'Message_ALARM': Message_StatusType.Message_ALARM, 'Message_FAIL': Message_StatusType.Message_FAIL}
    pass
def Message_EndLine(theMessenger : Message_Messenger) -> Message_Messenger:
    """
    None
    """
Message_ALARM: OCP.Message.Message_StatusType # value = Message_StatusType.Message_ALARM
Message_Alarm: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Alarm
Message_Alarm1: OCP.Message.Message_Status # value = Message_Status.Message_Alarm1
Message_Alarm10: OCP.Message.Message_Status # value = Message_Status.Message_Alarm10
Message_Alarm11: OCP.Message.Message_Status # value = Message_Status.Message_Alarm11
Message_Alarm12: OCP.Message.Message_Status # value = Message_Status.Message_Alarm12
Message_Alarm13: OCP.Message.Message_Status # value = Message_Status.Message_Alarm13
Message_Alarm14: OCP.Message.Message_Status # value = Message_Status.Message_Alarm14
Message_Alarm15: OCP.Message.Message_Status # value = Message_Status.Message_Alarm15
Message_Alarm16: OCP.Message.Message_Status # value = Message_Status.Message_Alarm16
Message_Alarm17: OCP.Message.Message_Status # value = Message_Status.Message_Alarm17
Message_Alarm18: OCP.Message.Message_Status # value = Message_Status.Message_Alarm18
Message_Alarm19: OCP.Message.Message_Status # value = Message_Status.Message_Alarm19
Message_Alarm2: OCP.Message.Message_Status # value = Message_Status.Message_Alarm2
Message_Alarm20: OCP.Message.Message_Status # value = Message_Status.Message_Alarm20
Message_Alarm21: OCP.Message.Message_Status # value = Message_Status.Message_Alarm21
Message_Alarm22: OCP.Message.Message_Status # value = Message_Status.Message_Alarm22
Message_Alarm23: OCP.Message.Message_Status # value = Message_Status.Message_Alarm23
Message_Alarm24: OCP.Message.Message_Status # value = Message_Status.Message_Alarm24
Message_Alarm25: OCP.Message.Message_Status # value = Message_Status.Message_Alarm25
Message_Alarm26: OCP.Message.Message_Status # value = Message_Status.Message_Alarm26
Message_Alarm27: OCP.Message.Message_Status # value = Message_Status.Message_Alarm27
Message_Alarm28: OCP.Message.Message_Status # value = Message_Status.Message_Alarm28
Message_Alarm29: OCP.Message.Message_Status # value = Message_Status.Message_Alarm29
Message_Alarm3: OCP.Message.Message_Status # value = Message_Status.Message_Alarm3
Message_Alarm30: OCP.Message.Message_Status # value = Message_Status.Message_Alarm30
Message_Alarm31: OCP.Message.Message_Status # value = Message_Status.Message_Alarm31
Message_Alarm32: OCP.Message.Message_Status # value = Message_Status.Message_Alarm32
Message_Alarm4: OCP.Message.Message_Status # value = Message_Status.Message_Alarm4
Message_Alarm5: OCP.Message.Message_Status # value = Message_Status.Message_Alarm5
Message_Alarm6: OCP.Message.Message_Status # value = Message_Status.Message_Alarm6
Message_Alarm7: OCP.Message.Message_Status # value = Message_Status.Message_Alarm7
Message_Alarm8: OCP.Message.Message_Status # value = Message_Status.Message_Alarm8
Message_Alarm9: OCP.Message.Message_Status # value = Message_Status.Message_Alarm9
Message_DONE: OCP.Message.Message_StatusType # value = Message_StatusType.Message_DONE
Message_Done1: OCP.Message.Message_Status # value = Message_Status.Message_Done1
Message_Done10: OCP.Message.Message_Status # value = Message_Status.Message_Done10
Message_Done11: OCP.Message.Message_Status # value = Message_Status.Message_Done11
Message_Done12: OCP.Message.Message_Status # value = Message_Status.Message_Done12
Message_Done13: OCP.Message.Message_Status # value = Message_Status.Message_Done13
Message_Done14: OCP.Message.Message_Status # value = Message_Status.Message_Done14
Message_Done15: OCP.Message.Message_Status # value = Message_Status.Message_Done15
Message_Done16: OCP.Message.Message_Status # value = Message_Status.Message_Done16
Message_Done17: OCP.Message.Message_Status # value = Message_Status.Message_Done17
Message_Done18: OCP.Message.Message_Status # value = Message_Status.Message_Done18
Message_Done19: OCP.Message.Message_Status # value = Message_Status.Message_Done19
Message_Done2: OCP.Message.Message_Status # value = Message_Status.Message_Done2
Message_Done20: OCP.Message.Message_Status # value = Message_Status.Message_Done20
Message_Done21: OCP.Message.Message_Status # value = Message_Status.Message_Done21
Message_Done22: OCP.Message.Message_Status # value = Message_Status.Message_Done22
Message_Done23: OCP.Message.Message_Status # value = Message_Status.Message_Done23
Message_Done24: OCP.Message.Message_Status # value = Message_Status.Message_Done24
Message_Done25: OCP.Message.Message_Status # value = Message_Status.Message_Done25
Message_Done26: OCP.Message.Message_Status # value = Message_Status.Message_Done26
Message_Done27: OCP.Message.Message_Status # value = Message_Status.Message_Done27
Message_Done28: OCP.Message.Message_Status # value = Message_Status.Message_Done28
Message_Done29: OCP.Message.Message_Status # value = Message_Status.Message_Done29
Message_Done3: OCP.Message.Message_Status # value = Message_Status.Message_Done3
Message_Done30: OCP.Message.Message_Status # value = Message_Status.Message_Done30
Message_Done31: OCP.Message.Message_Status # value = Message_Status.Message_Done31
Message_Done32: OCP.Message.Message_Status # value = Message_Status.Message_Done32
Message_Done4: OCP.Message.Message_Status # value = Message_Status.Message_Done4
Message_Done5: OCP.Message.Message_Status # value = Message_Status.Message_Done5
Message_Done6: OCP.Message.Message_Status # value = Message_Status.Message_Done6
Message_Done7: OCP.Message.Message_Status # value = Message_Status.Message_Done7
Message_Done8: OCP.Message.Message_Status # value = Message_Status.Message_Done8
Message_Done9: OCP.Message.Message_Status # value = Message_Status.Message_Done9
Message_FAIL: OCP.Message.Message_StatusType # value = Message_StatusType.Message_FAIL
Message_Fail: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Fail
Message_Fail1: OCP.Message.Message_Status # value = Message_Status.Message_Fail1
Message_Fail10: OCP.Message.Message_Status # value = Message_Status.Message_Fail10
Message_Fail11: OCP.Message.Message_Status # value = Message_Status.Message_Fail11
Message_Fail12: OCP.Message.Message_Status # value = Message_Status.Message_Fail12
Message_Fail13: OCP.Message.Message_Status # value = Message_Status.Message_Fail13
Message_Fail14: OCP.Message.Message_Status # value = Message_Status.Message_Fail14
Message_Fail15: OCP.Message.Message_Status # value = Message_Status.Message_Fail15
Message_Fail16: OCP.Message.Message_Status # value = Message_Status.Message_Fail16
Message_Fail17: OCP.Message.Message_Status # value = Message_Status.Message_Fail17
Message_Fail18: OCP.Message.Message_Status # value = Message_Status.Message_Fail18
Message_Fail19: OCP.Message.Message_Status # value = Message_Status.Message_Fail19
Message_Fail2: OCP.Message.Message_Status # value = Message_Status.Message_Fail2
Message_Fail20: OCP.Message.Message_Status # value = Message_Status.Message_Fail20
Message_Fail21: OCP.Message.Message_Status # value = Message_Status.Message_Fail21
Message_Fail22: OCP.Message.Message_Status # value = Message_Status.Message_Fail22
Message_Fail23: OCP.Message.Message_Status # value = Message_Status.Message_Fail23
Message_Fail24: OCP.Message.Message_Status # value = Message_Status.Message_Fail24
Message_Fail25: OCP.Message.Message_Status # value = Message_Status.Message_Fail25
Message_Fail26: OCP.Message.Message_Status # value = Message_Status.Message_Fail26
Message_Fail27: OCP.Message.Message_Status # value = Message_Status.Message_Fail27
Message_Fail28: OCP.Message.Message_Status # value = Message_Status.Message_Fail28
Message_Fail29: OCP.Message.Message_Status # value = Message_Status.Message_Fail29
Message_Fail3: OCP.Message.Message_Status # value = Message_Status.Message_Fail3
Message_Fail30: OCP.Message.Message_Status # value = Message_Status.Message_Fail30
Message_Fail31: OCP.Message.Message_Status # value = Message_Status.Message_Fail31
Message_Fail32: OCP.Message.Message_Status # value = Message_Status.Message_Fail32
Message_Fail4: OCP.Message.Message_Status # value = Message_Status.Message_Fail4
Message_Fail5: OCP.Message.Message_Status # value = Message_Status.Message_Fail5
Message_Fail6: OCP.Message.Message_Status # value = Message_Status.Message_Fail6
Message_Fail7: OCP.Message.Message_Status # value = Message_Status.Message_Fail7
Message_Fail8: OCP.Message.Message_Status # value = Message_Status.Message_Fail8
Message_Fail9: OCP.Message.Message_Status # value = Message_Status.Message_Fail9
Message_Info: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Info
Message_None: OCP.Message.Message_Status # value = Message_Status.Message_None
Message_Trace: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Trace
Message_WARN: OCP.Message.Message_StatusType # value = Message_StatusType.Message_WARN
Message_Warn1: OCP.Message.Message_Status # value = Message_Status.Message_Warn1
Message_Warn10: OCP.Message.Message_Status # value = Message_Status.Message_Warn10
Message_Warn11: OCP.Message.Message_Status # value = Message_Status.Message_Warn11
Message_Warn12: OCP.Message.Message_Status # value = Message_Status.Message_Warn12
Message_Warn13: OCP.Message.Message_Status # value = Message_Status.Message_Warn13
Message_Warn14: OCP.Message.Message_Status # value = Message_Status.Message_Warn14
Message_Warn15: OCP.Message.Message_Status # value = Message_Status.Message_Warn15
Message_Warn16: OCP.Message.Message_Status # value = Message_Status.Message_Warn16
Message_Warn17: OCP.Message.Message_Status # value = Message_Status.Message_Warn17
Message_Warn18: OCP.Message.Message_Status # value = Message_Status.Message_Warn18
Message_Warn19: OCP.Message.Message_Status # value = Message_Status.Message_Warn19
Message_Warn2: OCP.Message.Message_Status # value = Message_Status.Message_Warn2
Message_Warn20: OCP.Message.Message_Status # value = Message_Status.Message_Warn20
Message_Warn21: OCP.Message.Message_Status # value = Message_Status.Message_Warn21
Message_Warn22: OCP.Message.Message_Status # value = Message_Status.Message_Warn22
Message_Warn23: OCP.Message.Message_Status # value = Message_Status.Message_Warn23
Message_Warn24: OCP.Message.Message_Status # value = Message_Status.Message_Warn24
Message_Warn25: OCP.Message.Message_Status # value = Message_Status.Message_Warn25
Message_Warn26: OCP.Message.Message_Status # value = Message_Status.Message_Warn26
Message_Warn27: OCP.Message.Message_Status # value = Message_Status.Message_Warn27
Message_Warn28: OCP.Message.Message_Status # value = Message_Status.Message_Warn28
Message_Warn29: OCP.Message.Message_Status # value = Message_Status.Message_Warn29
Message_Warn3: OCP.Message.Message_Status # value = Message_Status.Message_Warn3
Message_Warn30: OCP.Message.Message_Status # value = Message_Status.Message_Warn30
Message_Warn31: OCP.Message.Message_Status # value = Message_Status.Message_Warn31
Message_Warn32: OCP.Message.Message_Status # value = Message_Status.Message_Warn32
Message_Warn4: OCP.Message.Message_Status # value = Message_Status.Message_Warn4
Message_Warn5: OCP.Message.Message_Status # value = Message_Status.Message_Warn5
Message_Warn6: OCP.Message.Message_Status # value = Message_Status.Message_Warn6
Message_Warn7: OCP.Message.Message_Status # value = Message_Status.Message_Warn7
Message_Warn8: OCP.Message.Message_Status # value = Message_Status.Message_Warn8
Message_Warn9: OCP.Message.Message_Status # value = Message_Status.Message_Warn9
Message_Warning: OCP.Message.Message_Gravity # value = Message_Gravity.Message_Warning
