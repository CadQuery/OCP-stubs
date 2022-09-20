import OCP.Message
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import io
import OCP.Standard
import OCP.OSD.OSD_MemInfo
import OCP.TCollection
import OCP.TColStd
__all__  = [
"Message",
"Message_Alert",
"Message_AlertExtended",
"Message_Algorithm",
"Message_ArrayOfMsg",
"Message_Attribute",
"Message_AttributeMeter",
"Message_AttributeObject",
"Message_AttributeStream",
"Message_CompositeAlerts",
"Message_ConsoleColor",
"Message_ExecStatus",
"Message_Gravity",
"Message_Level",
"Message_ListOfAlert",
"Message_ListOfMsg",
"Message_Messenger",
"Message_MetricType",
"Message_Msg",
"Message_MsgFile",
"Message_Printer",
"Message_PrinterOStream",
"Message_PrinterSystemLog",
"Message_PrinterToReport",
"Message_ProgressIndicator",
"Message_ProgressRange",
"Message_ProgressScope",
"Message_ProgressSentry",
"Message_Report",
"Message_SequenceOfPrinters",
"Message_Status",
"Message_StatusType",
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
"Message_ConsoleColor_Black",
"Message_ConsoleColor_Blue",
"Message_ConsoleColor_Cyan",
"Message_ConsoleColor_Default",
"Message_ConsoleColor_Green",
"Message_ConsoleColor_Magenta",
"Message_ConsoleColor_Red",
"Message_ConsoleColor_White",
"Message_ConsoleColor_Yellow",
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
"Message_MetricType_MemHeapUsage",
"Message_MetricType_MemPrivate",
"Message_MetricType_MemSwapUsage",
"Message_MetricType_MemSwapUsagePeak",
"Message_MetricType_MemVirtual",
"Message_MetricType_MemWorkingSet",
"Message_MetricType_MemWorkingSetPeak",
"Message_MetricType_None",
"Message_MetricType_ProcessCPUSystemTime",
"Message_MetricType_ProcessCPUUserTime",
"Message_MetricType_ThreadCPUSystemTime",
"Message_MetricType_ThreadCPUUserTime",
"Message_MetricType_WallClock",
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
    def DefaultReport_s(theToCreate : bool=False) -> Message_Report: 
        """
        returns the only one instance of Report When theToCreate is true - automatically creates message report when not exist.
        """
    @staticmethod
    def FillTime_s(Hour : int,Minute : int,Second : float) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the string filled with values of hours, minutes and seconds. Example: 1. (5, 12, 26.3345) returns "05h:12m:26.33s", 2. (0, 6, 34.496 ) returns "06m:34.50s", 3. (0, 0, 4.5 ) returns "4.50s"
        """
    @staticmethod
    @overload
    def MetricFromString_s(theString : str,theType : Message_MetricType) -> bool: 
        """
        Determines the metric from the given string identifier.

        Returns the metric type from the given string identifier.
        """
    @staticmethod
    @overload
    def MetricFromString_s(theString : str) -> Message_MetricType: ...
    @staticmethod
    def MetricToString_s(theType : Message_MetricType) -> str: 
        """
        Returns the string name for a given metric type.
        """
    @staticmethod
    @overload
    def SendAlarm_s(theMessage : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def SendAlarm_s() -> Any: ...
    @staticmethod
    @overload
    def SendFail_s() -> Any: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def SendFail_s(theMessage : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @staticmethod
    @overload
    def SendInfo_s(theMessage : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def SendInfo_s() -> Any: ...
    @staticmethod
    @overload
    def SendTrace_s() -> Any: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def SendTrace_s(theMessage : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @staticmethod
    @overload
    def SendWarning_s() -> Any: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def SendWarning_s(theMessage : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @staticmethod
    @overload
    def Send_s(theGravity : Message_Gravity) -> Any: 
        """
        None
        """
    @staticmethod
    @overload
    def Send_s(theMessage : OCP.TCollection.TCollection_AsciiString,theGravity : Message_Gravity) -> None: ...
    @staticmethod
    def ToMessageMetric_s(theMemInfo : OCP.OSD.OSD_MemInfo.Counter_e,theMetric : Message_MetricType) -> bool: 
        """
        Converts OSD memory info type to message metric.
        """
    @staticmethod
    def ToOSDMetric_s(theMetric : Message_MetricType,theMemInfo : OCP.OSD.OSD_MemInfo.Counter_e) -> bool: 
        """
        Converts message metric to OSD memory info type.
        """
    def __init__(self) -> None: ...
    pass
class Message_Alert(OCP.Standard.Standard_Transient):
    """
    Base class of the hierarchy of classes describing various situations occurring during execution of some algorithm or procedure.Base class of the hierarchy of classes describing various situations occurring during execution of some algorithm or procedure.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class Message_AlertExtended(Message_Alert, OCP.Standard.Standard_Transient):
    """
    Inherited class of Message_Alert with some additional information. It has Message_Attributes to provide the alert name, and other custom information It has a container of composite alerts, if the alert might provide sub-alerts collecting.Inherited class of Message_Alert with some additional information. It has Message_Attributes to provide the alert name, and other custom information It has a container of composite alerts, if the alert might provide sub-alerts collecting.
    """
    @staticmethod
    def AddAlert_s(theReport : Message_Report,theAttribute : Message_Attribute,theGravity : Message_Gravity) -> Message_Alert: 
        """
        Creates new instance of the alert and put it into report with Message_Info gravity. It does nothing if such kind of gravity is not active in the report
        """
    def Attribute(self) -> Message_Attribute: 
        """
        Returns container of the alert attributes
        """
    def CompositeAlerts(self,theToCreate : bool=False) -> Message_CompositeAlerts: 
        """
        Returns class provided hierarchy of alerts if created or create if the parameter is true
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Merge(self,theTarget : Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget. Base implementation always returns false.
        """
    def SetAttribute(self,theAttribute : Message_Attribute) -> None: 
        """
        Sets container of the alert attributes
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Hierarchical alerts can not be merged Basis implementation returns true.
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
    def AddStatus(self,theStatus : Message_ExecStatus,theOther : Message_Algorithm) -> None: 
        """
        Add statuses to this algorithm from other algorithm (including messages)

        Add statuses to this algorithm from other algorithm, but only those items are moved that correspond to statuses set in theStatus
        """
    @overload
    def AddStatus(self,theOther : Message_Algorithm) -> None: ...
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @staticmethod
    @overload
    def PrepareReport_s(theReportSeq : OCP.TColStd.TColStd_SequenceOfHExtendedString,theMaxCount : int) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Prepares a string containing a list of integers contained in theError map, but not more than theMaxCount

        Prepares a string containing a list of names contained in theReportSeq sequence, but not more than theMaxCount
        """
    @staticmethod
    @overload
    def PrepareReport_s(theError : OCP.TColStd.TColStd_HPackedMapOfInteger,theMaxCount : int) -> OCP.TCollection.TCollection_ExtendedString: ...
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
    def SetStatus(self,theStat : Message_Status,theStr : str,noRepetitions : bool) -> None: 
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
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_HAsciiString,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theInt : int) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_HAsciiString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_ExtendedString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : str,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_AsciiString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_HExtendedString,noRepetitions : bool=True) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theMsg : Message_Msg) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_ExtendedString,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status,theStr : OCP.TCollection.TCollection_AsciiString,noRepetitions : bool) -> None: ...
    @overload
    def SetStatus(self,theStat : Message_Status) -> None: ...
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
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
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
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : Any,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Message_Attribute(OCP.Standard.Standard_Transient):
    """
    Additional information of extended alert attribute To provide other custom attribute container, it might be redefined.Additional information of extended alert attribute To provide other custom attribute container, it might be redefined.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns custom name of alert if it is set
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
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the custom name of alert
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Message_AttributeMeter(Message_Attribute, OCP.Standard.Standard_Transient):
    """
    Alert object storing alert metrics values. Start and stop values for each metric.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns custom name of alert if it is set
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasMetric(self,theMetric : Message_MetricType) -> bool: 
        """
        Checks whether the attribute has values for the metric
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
    def IsMetricValid(self,theMetric : Message_MetricType) -> bool: 
        """
        Returns true when both values of the metric are set.
        """
    @staticmethod
    def SetAlertMetrics_s(theAlert : Message_AlertExtended,theStartValue : bool) -> None: 
        """
        Sets current values of default report metrics into the alert. Processed only alert with Message_AttributeMeter attribute
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the custom name of alert
        """
    def SetStartValue(self,theMetric : Message_MetricType,theValue : float) -> None: 
        """
        Sets start values for the metric
        """
    def SetStopValue(self,theMetric : Message_MetricType,theValue : float) -> None: 
        """
        Sets stop values for the metric
        """
    @staticmethod
    def StartAlert_s(theAlert : Message_AlertExtended) -> None: 
        """
        Sets start values of default report metrics into the alert
        """
    def StartValue(self,theMetric : Message_MetricType) -> float: 
        """
        Returns start value for the metric
        """
    @staticmethod
    def StopAlert_s(theAlert : Message_AlertExtended) -> None: 
        """
        Sets stop values of default report metrics into the alert
        """
    def StopValue(self,theMetric : Message_MetricType) -> float: 
        """
        Returns stop value for the metric
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @staticmethod
    def UndefinedMetricValue_s() -> float: 
        """
        Returns default value of the metric when it is not defined
        """
    def __init__(self,theName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Message_AttributeObject(Message_Attribute, OCP.Standard.Standard_Transient):
    """
    Alert object storing a transient object
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns custom name of alert if it is set
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
    def Object(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns object
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the custom name of alert
        """
    def SetObject(self,theObject : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets the object
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theObject : OCP.Standard.Standard_Transient,theName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Message_AttributeStream(Message_Attribute, OCP.Standard.Standard_Transient):
    """
    Alert object storing stream value
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns custom name of alert if it is set
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
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the custom name of alert
        """
    def SetStream(self,theStream : Any) -> None: 
        """
        Sets stream value
        """
    def Stream(self) -> Any: 
        """
        Returns stream value
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theStream : Any,theName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Message_CompositeAlerts(OCP.Standard.Standard_Transient):
    """
    Class providing container of alertsClass providing container of alerts
    """
    def AddAlert(self,theGravity : Message_Gravity,theAlert : Message_Alert) -> bool: 
        """
        Add alert with specified gravity. If the alert supports merge it will be merged.
        """
    def Alerts(self,theGravity : Message_Gravity) -> Message_ListOfAlert: 
        """
        Returns list of collected alerts with specified gravity
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
    @overload
    def HasAlert(self,theAlert : Message_Alert) -> bool: 
        """
        Returns true if the alert belong the list of the child alerts.

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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def RemoveAlert(self,theGravity : Message_Gravity,theAlert : Message_Alert) -> bool: 
        """
        Removes alert with specified gravity.
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
class Message_ConsoleColor():
    """
    Color definition for console/terminal output (limited palette).

    Members:

      Message_ConsoleColor_Default

      Message_ConsoleColor_Black

      Message_ConsoleColor_White

      Message_ConsoleColor_Red

      Message_ConsoleColor_Blue

      Message_ConsoleColor_Green

      Message_ConsoleColor_Yellow

      Message_ConsoleColor_Cyan

      Message_ConsoleColor_Magenta
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
    Message_ConsoleColor_Black: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Black: 1>
    Message_ConsoleColor_Blue: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Blue: 4>
    Message_ConsoleColor_Cyan: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Cyan: 7>
    Message_ConsoleColor_Default: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Default: 0>
    Message_ConsoleColor_Green: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Green: 5>
    Message_ConsoleColor_Magenta: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Magenta: 8>
    Message_ConsoleColor_Red: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Red: 3>
    Message_ConsoleColor_White: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_White: 2>
    Message_ConsoleColor_Yellow: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Yellow: 6>
    __entries: dict # value = {'Message_ConsoleColor_Default': (<Message_ConsoleColor.Message_ConsoleColor_Default: 0>, None), 'Message_ConsoleColor_Black': (<Message_ConsoleColor.Message_ConsoleColor_Black: 1>, None), 'Message_ConsoleColor_White': (<Message_ConsoleColor.Message_ConsoleColor_White: 2>, None), 'Message_ConsoleColor_Red': (<Message_ConsoleColor.Message_ConsoleColor_Red: 3>, None), 'Message_ConsoleColor_Blue': (<Message_ConsoleColor.Message_ConsoleColor_Blue: 4>, None), 'Message_ConsoleColor_Green': (<Message_ConsoleColor.Message_ConsoleColor_Green: 5>, None), 'Message_ConsoleColor_Yellow': (<Message_ConsoleColor.Message_ConsoleColor_Yellow: 6>, None), 'Message_ConsoleColor_Cyan': (<Message_ConsoleColor.Message_ConsoleColor_Cyan: 7>, None), 'Message_ConsoleColor_Magenta': (<Message_ConsoleColor.Message_ConsoleColor_Magenta: 8>, None)}
    __members__: dict # value = {'Message_ConsoleColor_Default': <Message_ConsoleColor.Message_ConsoleColor_Default: 0>, 'Message_ConsoleColor_Black': <Message_ConsoleColor.Message_ConsoleColor_Black: 1>, 'Message_ConsoleColor_White': <Message_ConsoleColor.Message_ConsoleColor_White: 2>, 'Message_ConsoleColor_Red': <Message_ConsoleColor.Message_ConsoleColor_Red: 3>, 'Message_ConsoleColor_Blue': <Message_ConsoleColor.Message_ConsoleColor_Blue: 4>, 'Message_ConsoleColor_Green': <Message_ConsoleColor.Message_ConsoleColor_Green: 5>, 'Message_ConsoleColor_Yellow': <Message_ConsoleColor.Message_ConsoleColor_Yellow: 6>, 'Message_ConsoleColor_Cyan': <Message_ConsoleColor.Message_ConsoleColor_Cyan: 7>, 'Message_ConsoleColor_Magenta': <Message_ConsoleColor.Message_ConsoleColor_Magenta: 8>}
    pass
class Message_ExecStatus():
    """
    Tiny class for extended handling of error / execution status of algorithm in universal way.
    """
    class StatusRange_e():
        """
        Definitions of range of available statuses

        Members:

          FirstStatus

          StatusesPerType

          NbStatuses

          LastStatus
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
        FirstStatus: OCP.Message.StatusRange_e # value = <StatusRange_e.FirstStatus: 1>
        LastStatus: OCP.Message.StatusRange_e # value = <StatusRange_e.LastStatus: 129>
        NbStatuses: OCP.Message.StatusRange_e # value = <StatusRange_e.NbStatuses: 128>
        StatusesPerType: OCP.Message.StatusRange_e # value = <StatusRange_e.StatusesPerType: 32>
        __entries: dict # value = {'FirstStatus': (<StatusRange_e.FirstStatus: 1>, None), 'StatusesPerType': (<StatusRange_e.StatusesPerType: 32>, None), 'NbStatuses': (<StatusRange_e.NbStatuses: 128>, None), 'LastStatus': (<StatusRange_e.LastStatus: 129>, None)}
        __members__: dict # value = {'FirstStatus': <StatusRange_e.FirstStatus: 1>, 'StatusesPerType': <StatusRange_e.StatusesPerType: 32>, 'NbStatuses': <StatusRange_e.NbStatuses: 128>, 'LastStatus': <StatusRange_e.LastStatus: 129>}
        pass
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
    def __init__(self,status : Message_Status) -> None: ...
    @overload
    def __init__(self) -> None: ...
    FirstStatus: OCP.Message.StatusRange_e # value = <StatusRange_e.FirstStatus: 1>
    LastStatus: OCP.Message.StatusRange_e # value = <StatusRange_e.LastStatus: 129>
    NbStatuses: OCP.Message.StatusRange_e # value = <StatusRange_e.NbStatuses: 128>
    StatusesPerType: OCP.Message.StatusRange_e # value = <StatusRange_e.StatusesPerType: 32>
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
    Message_Alarm: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Alarm: 3>
    Message_Fail: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Fail: 4>
    Message_Info: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Info: 1>
    Message_Trace: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Trace: 0>
    Message_Warning: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Warning: 2>
    __entries: dict # value = {'Message_Trace': (<Message_Gravity.Message_Trace: 0>, None), 'Message_Info': (<Message_Gravity.Message_Info: 1>, None), 'Message_Warning': (<Message_Gravity.Message_Warning: 2>, None), 'Message_Alarm': (<Message_Gravity.Message_Alarm: 3>, None), 'Message_Fail': (<Message_Gravity.Message_Fail: 4>, None)}
    __members__: dict # value = {'Message_Trace': <Message_Gravity.Message_Trace: 0>, 'Message_Info': <Message_Gravity.Message_Info: 1>, 'Message_Warning': <Message_Gravity.Message_Warning: 2>, 'Message_Alarm': <Message_Gravity.Message_Alarm: 3>, 'Message_Fail': <Message_Gravity.Message_Fail: 4>}
    pass
class Message_Level():
    """
    This class is an instance of Sentry to create a level in a message report Constructor of the class add new (active) level in the report, destructor removes it While the level is active in the report, new alerts are added below the level root alert.
    """
    def AddAlert(self,theGravity : Message_Gravity,theAlert : Message_Alert) -> bool: 
        """
        Adds new alert on the level. Stops the last alert metric, appends the alert and starts the alert metrics collecting. Sets root alert beforehand this method using, if the root is NULL, it does nothing.
        """
    def RootAlert(self) -> Message_AlertExtended: 
        """
        Returns root alert of the level
        """
    def SetRootAlert(self,theAlert : Message_AlertExtended,isRequiredToStart : bool) -> None: 
        """
        Sets the root alert. Starts collects alert metrics if active.
        """
    def __init__(self,theName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
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
    def Append(self,theItem : Message_Alert,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : Message_ListOfAlert) -> None: ...
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
    def Prepend(self,theOther : Message_ListOfAlert) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : Message_Alert) -> Message_Alert: ...
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
    def __init__(self,theOther : Message_ListOfAlert) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
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
    def Append(self,theItem : Message_Msg,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : Message_Msg) -> Message_Msg: ...
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
    def InsertAfter(self,theItem : Message_Msg,theIter : Any) -> Message_Msg: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : Message_ListOfMsg,theIter : Any) -> None: ...
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
    def Prepend(self,theOther : Message_ListOfMsg) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : Message_Msg) -> Message_Msg: ...
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
    def __init__(self,theOther : Message_ListOfMsg) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
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
    def Send(self,theString : OCP.TCollection.TCollection_ExtendedString,theGravity : Message_Gravity=Message_Gravity.Message_Warning) -> None: 
        """
        Dispatch a message to all the printers in the list. Three versions of string representations are accepted for convenience, by default all are converted to ExtendedString.

        See above

        See above

        See above

        Create string buffer for message of specified type

        See above
        """
    @overload
    def Send(self,theGravity : Message_Gravity) -> Any: ...
    @overload
    def Send(self,theObject : OCP.Standard.Standard_Transient,theGravity : Message_Gravity=Message_Gravity.Message_Warning) -> None: ...
    @overload
    def Send(self,theString : str,theGravity : Message_Gravity=Message_Gravity.Message_Warning) -> None: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_AsciiString,theGravity : Message_Gravity=Message_Gravity.Message_Warning) -> None: ...
    @overload
    def Send(self,theStream : Any,theGravity : Message_Gravity=Message_Gravity.Message_Warning) -> None: ...
    @overload
    def SendAlarm(self,theMessage : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Create string buffer for sending Alarm message

        Short-cut to Send (theMessage, Message_Alarm)
        """
    @overload
    def SendAlarm(self) -> Any: ...
    @overload
    def SendFail(self,theMessage : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Create string buffer for sending Fail message

        Short-cut to Send (theMessage, Message_Fail)
        """
    @overload
    def SendFail(self) -> Any: ...
    @overload
    def SendInfo(self,theMessage : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Create string buffer for sending Info message

        Short-cut to Send (theMessage, Message_Info)
        """
    @overload
    def SendInfo(self) -> Any: ...
    @overload
    def SendTrace(self,theMessage : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Create string buffer for sending Trace message

        Short-cut to Send (theMessage, Message_Trace)
        """
    @overload
    def SendTrace(self) -> Any: ...
    @overload
    def SendWarning(self,theMessage : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Create string buffer for sending Warning message

        Short-cut to Send (theMessage, Message_Warning)
        """
    @overload
    def SendWarning(self) -> Any: ...
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
class Message_MetricType():
    """
    Specifies kind of report information to collect

    Members:

      Message_MetricType_None

      Message_MetricType_ThreadCPUUserTime

      Message_MetricType_ThreadCPUSystemTime

      Message_MetricType_ProcessCPUUserTime

      Message_MetricType_ProcessCPUSystemTime

      Message_MetricType_WallClock

      Message_MetricType_MemPrivate

      Message_MetricType_MemVirtual

      Message_MetricType_MemWorkingSet

      Message_MetricType_MemWorkingSetPeak

      Message_MetricType_MemSwapUsage

      Message_MetricType_MemSwapUsagePeak

      Message_MetricType_MemHeapUsage
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
    Message_MetricType_MemHeapUsage: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemHeapUsage: 12>
    Message_MetricType_MemPrivate: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemPrivate: 6>
    Message_MetricType_MemSwapUsage: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemSwapUsage: 10>
    Message_MetricType_MemSwapUsagePeak: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemSwapUsagePeak: 11>
    Message_MetricType_MemVirtual: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemVirtual: 7>
    Message_MetricType_MemWorkingSet: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemWorkingSet: 8>
    Message_MetricType_MemWorkingSetPeak: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemWorkingSetPeak: 9>
    Message_MetricType_None: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_None: 0>
    Message_MetricType_ProcessCPUSystemTime: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_ProcessCPUSystemTime: 4>
    Message_MetricType_ProcessCPUUserTime: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_ProcessCPUUserTime: 3>
    Message_MetricType_ThreadCPUSystemTime: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_ThreadCPUSystemTime: 2>
    Message_MetricType_ThreadCPUUserTime: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_ThreadCPUUserTime: 1>
    Message_MetricType_WallClock: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_WallClock: 5>
    __entries: dict # value = {'Message_MetricType_None': (<Message_MetricType.Message_MetricType_None: 0>, None), 'Message_MetricType_ThreadCPUUserTime': (<Message_MetricType.Message_MetricType_ThreadCPUUserTime: 1>, None), 'Message_MetricType_ThreadCPUSystemTime': (<Message_MetricType.Message_MetricType_ThreadCPUSystemTime: 2>, None), 'Message_MetricType_ProcessCPUUserTime': (<Message_MetricType.Message_MetricType_ProcessCPUUserTime: 3>, None), 'Message_MetricType_ProcessCPUSystemTime': (<Message_MetricType.Message_MetricType_ProcessCPUSystemTime: 4>, None), 'Message_MetricType_WallClock': (<Message_MetricType.Message_MetricType_WallClock: 5>, None), 'Message_MetricType_MemPrivate': (<Message_MetricType.Message_MetricType_MemPrivate: 6>, None), 'Message_MetricType_MemVirtual': (<Message_MetricType.Message_MetricType_MemVirtual: 7>, None), 'Message_MetricType_MemWorkingSet': (<Message_MetricType.Message_MetricType_MemWorkingSet: 8>, None), 'Message_MetricType_MemWorkingSetPeak': (<Message_MetricType.Message_MetricType_MemWorkingSetPeak: 9>, None), 'Message_MetricType_MemSwapUsage': (<Message_MetricType.Message_MetricType_MemSwapUsage: 10>, None), 'Message_MetricType_MemSwapUsagePeak': (<Message_MetricType.Message_MetricType_MemSwapUsagePeak: 11>, None), 'Message_MetricType_MemHeapUsage': (<Message_MetricType.Message_MetricType_MemHeapUsage: 12>, None)}
    __members__: dict # value = {'Message_MetricType_None': <Message_MetricType.Message_MetricType_None: 0>, 'Message_MetricType_ThreadCPUUserTime': <Message_MetricType.Message_MetricType_ThreadCPUUserTime: 1>, 'Message_MetricType_ThreadCPUSystemTime': <Message_MetricType.Message_MetricType_ThreadCPUSystemTime: 2>, 'Message_MetricType_ProcessCPUUserTime': <Message_MetricType.Message_MetricType_ProcessCPUUserTime: 3>, 'Message_MetricType_ProcessCPUSystemTime': <Message_MetricType.Message_MetricType_ProcessCPUSystemTime: 4>, 'Message_MetricType_WallClock': <Message_MetricType.Message_MetricType_WallClock: 5>, 'Message_MetricType_MemPrivate': <Message_MetricType.Message_MetricType_MemPrivate: 6>, 'Message_MetricType_MemVirtual': <Message_MetricType.Message_MetricType_MemVirtual: 7>, 'Message_MetricType_MemWorkingSet': <Message_MetricType.Message_MetricType_MemWorkingSet: 8>, 'Message_MetricType_MemWorkingSetPeak': <Message_MetricType.Message_MetricType_MemWorkingSetPeak: 9>, 'Message_MetricType_MemSwapUsage': <Message_MetricType.Message_MetricType_MemSwapUsage: 10>, 'Message_MetricType_MemSwapUsagePeak': <Message_MetricType.Message_MetricType_MemSwapUsagePeak: 11>, 'Message_MetricType_MemHeapUsage': <Message_MetricType.Message_MetricType_MemHeapUsage: 12>}
    pass
class Message_Msg():
    """
    This class provides a tool for constructing the parametrized message basing on resources loaded by Message_MsgFile tool.
    """
    @overload
    def Arg(self,theString : OCP.TCollection.TCollection_AsciiString) -> Message_Msg: 
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
    def Arg(self,theString : str) -> Message_Msg: ...
    @overload
    def Arg(self,theInt : int) -> Message_Msg: ...
    @overload
    def Arg(self,theString : OCP.TCollection.TCollection_HExtendedString) -> Message_Msg: ...
    @overload
    def Arg(self,theReal : float) -> Message_Msg: ...
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
    def __init__(self,theMsg : Message_Msg) -> None: ...
    @overload
    def __init__(self,theKey : OCP.TCollection.TCollection_ExtendedString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theKey : str) -> None: ...
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

        Gives the text for the message identified by the keyword <key>. If there are no messages with such keyword defined, the error message is returned. In that case reference to static string is returned, it can be changed with next call(s) to Msg(). Note: The error message is constructed like 'Unknown message: <key>', and can itself be customized by defining message with key Message_Msg_BadKeyword.
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_AsciiString,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().

        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().

        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().
        """
    @overload
    def Send(self,theString : str,theGravity : Message_Gravity) -> None: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_ExtendedString,theGravity : Message_Gravity) -> None: ...
    def SendObject(self,theObject : OCP.Standard.Standard_Transient,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. The object is converted to string in format: <object kind> : <object pointer>. Default implementation calls first method Send().
        """
    def SendStringStream(self,theStream : Any,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. Stream is converted to string value. Default implementation calls first method Send().
        """
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
    def GetStream(self) -> io.BytesIO: 
        """
        Returns reference to the output stream
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_AsciiString,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().

        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().

        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().
        """
    @overload
    def Send(self,theString : str,theGravity : Message_Gravity) -> None: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_ExtendedString,theGravity : Message_Gravity) -> None: ...
    def SendObject(self,theObject : OCP.Standard.Standard_Transient,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. The object is converted to string in format: <object kind> : <object pointer>. Default implementation calls first method Send().
        """
    def SendStringStream(self,theStream : Any,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. Stream is converted to string value. Default implementation calls first method Send().
        """
    @staticmethod
    def SetConsoleTextColor_s(theOStream : io.BytesIO,theTextColor : Message_ConsoleColor,theIsIntenseText : bool=False) -> None: 
        """
        Setup console text color.
        """
    def SetToColorize(self,theToColorize : bool) -> None: 
        """
        Set if text output into console should be colorized depending on message gravity.
        """
    def SetTraceLevel(self,theTraceLevel : Message_Gravity) -> None: 
        """
        Set trace level used for filtering messages. By default, trace level is Message_Info, so that all messages are output
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToColorize(self) -> bool: 
        """
        Returns TRUE if text output into console should be colorized depending on message gravity; TRUE by default.
        """
    @overload
    def __init__(self,theTraceLevel : Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def __init__(self,theFileName : str,theDoAppend : bool,theTraceLevel : Message_Gravity=Message_Gravity.Message_Info) -> None: ...
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
class Message_PrinterSystemLog(Message_Printer, OCP.Standard.Standard_Transient):
    """
    Implementation of a message printer associated with system log. Implemented for the following systems: - Windows, through ReportEventW(). - Android, through __android_log_write(). - UNIX/Linux, through syslog().Implementation of a message printer associated with system log. Implemented for the following systems: - Windows, through ReportEventW(). - Android, through __android_log_write(). - UNIX/Linux, through syslog().
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_AsciiString,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().

        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().

        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().
        """
    @overload
    def Send(self,theString : str,theGravity : Message_Gravity) -> None: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_ExtendedString,theGravity : Message_Gravity) -> None: ...
    def SendObject(self,theObject : OCP.Standard.Standard_Transient,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. The object is converted to string in format: <object kind> : <object pointer>. Default implementation calls first method Send().
        """
    def SendStringStream(self,theStream : Any,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. Stream is converted to string value. Default implementation calls first method Send().
        """
    def SetTraceLevel(self,theTraceLevel : Message_Gravity) -> None: 
        """
        Set trace level used for filtering messages. By default, trace level is Message_Info, so that all messages are output
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theEventSourceName : OCP.TCollection.TCollection_AsciiString,theTraceLevel : Message_Gravity=Message_Gravity.Message_Info) -> None: ...
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
class Message_PrinterToReport(Message_Printer, OCP.Standard.Standard_Transient):
    """
    Implementation of a message printer associated with Message_Report Send will create a new alert of the report. If string is sent, an alert is created by Eol only. The alerts are sent into set report or default report of Message.Implementation of a message printer associated with Message_Report Send will create a new alert of the report. If string is sent, an alert is created by Eol only. The alerts are sent into set report or default report of Message.
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Report(self) -> Message_Report: 
        """
        Returns the current or default report
        """
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_AsciiString,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().

        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().

        Send a string message with specified trace level. The last Boolean argument is deprecated and unused. Default implementation redirects to send().
        """
    @overload
    def Send(self,theString : str,theGravity : Message_Gravity) -> None: ...
    @overload
    def Send(self,theString : OCP.TCollection.TCollection_ExtendedString,theGravity : Message_Gravity) -> None: ...
    def SendObject(self,theObject : OCP.Standard.Standard_Transient,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. The object is converted to string in format: <object kind> : <object pointer>. The parameter theToPutEol specified whether end-of-line should be added to the end of the message. Default implementation calls first method Send().
        """
    def SendStringStream(self,theStream : Any,theGravity : Message_Gravity) -> None: 
        """
        Send a string message with specified trace level. Stream is converted to string value. Default implementation calls first method Send().
        """
    def SetReport(self,theReport : Message_Report) -> None: 
        """
        Sets the printer report
        """
    def SetTraceLevel(self,theTraceLevel : Message_Gravity) -> None: 
        """
        Set trace level used for filtering messages. By default, trace level is Message_Info, so that all messages are output
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
class Message_ProgressIndicator(OCP.Standard.Standard_Transient):
    """
    Defines abstract interface from program to the user. This includes progress indication and user break mechanisms.Defines abstract interface from program to the user. This includes progress indication and user break mechanisms.
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
    def GetPosition(self) -> float: 
        """
        Returns total progress position ranged from 0 to 1. Should not be called concurrently while the progress is advancing, except from implementation of method Show().
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
    def Start(self) -> Message_ProgressRange: 
        """
        Resets the indicator to zero, calls Reset(), and returns the range. This range refers to the scope that has no name and is initialized with max value 1 and step 1. Use this method to get the top level range for progress indication.
        """
    @staticmethod
    def Start_s(theProgress : Message_ProgressIndicator) -> Message_ProgressRange: 
        """
        If argument is non-null handle, returns theProgress->Start(). Otherwise, returns dummy range that can be safely used in the algorithms but not bound to progress indicator.
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
class Message_ProgressRange():
    """
    Auxiliary class representing a part of the global progress scale allocated by a step of the progress scope, see Message_ProgressScope::Next().
    """
    def Close(self) -> None: 
        """
        Closes the current range and advances indicator

        Closes the current range and advances indicator
        """
    def IsActive(self) -> bool: 
        """
        Returns true if this progress range is attached to some indicator.

        Returns true if this progress range is attached to some indicator.
        """
    def More(self) -> bool: 
        """
        Returns false if ProgressIndicator signals UserBreak
        """
    def UserBreak(self) -> bool: 
        """
        Returns true if ProgressIndicator signals UserBreak

        Returns true if ProgressIndicator signals UserBreak
        """
    @overload
    def __init__(self,theOther : Message_ProgressRange) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Message_ProgressScope():
    """
    Message_ProgressScope class provides convenient way to advance progress indicator in context of complex program organized in hierarchical way, where usually it is difficult (or even not possible) to consider process as linear with fixed step.
    """
    def Close(self) -> None: 
        """
        Closes the scope and advances the progress to its end. Closed scope should not be used.

        Closes the scope and advances the progress to its end. Closed scope should not be used.
        """
    def GetPortion(self) -> float: 
        """
        Get the portion of the indicator covered by this scope (from 0 to 1)
        """
    def IsActive(self) -> bool: 
        """
        Returns true if this progress scope is attached to some indicator.
        """
    def IsInfinite(self) -> bool: 
        """
        Returns the infinite flag
        """
    def MaxValue(self) -> float: 
        """
        Returns the maximal value of progress in this scope
        """
    def More(self) -> bool: 
        """
        Returns false if ProgressIndicator signals UserBreak
        """
    def Name(self) -> str: 
        """
        Returns the name of the scope (may be null). Scopes with null name (e.g. root scope) should be bypassed when reporting progress to the user.
        """
    @overload
    def Next(self,theStep : float=1.0) -> Message_ProgressRange: 
        """
        Advances position by specified step and returns the range covering this step

        Advances position by specified step and returns the range covering this step
        """
    @overload
    def Next(self,theStep : float) -> Message_ProgressRange: ...
    def Parent(self) -> Message_ProgressScope: 
        """
        Returns parent scope (null for top-level scope)
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the name of the scope.
        """
    def Show(self) -> None: 
        """
        Force update of presentation of the progress indicator. Should not be called concurrently.

        Force update of presentation of the progress indicator. Should not be called concurrently.
        """
    def UserBreak(self) -> bool: 
        """
        Returns true if ProgressIndicator signals UserBreak

        Returns true if ProgressIndicator signals UserBreak
        """
    def Value(self) -> float: 
        """
        Returns the current value of progress in this scope.

        Returns the current value of progress in this scope.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theRange : Message_ProgressRange,theName : OCP.TCollection.TCollection_AsciiString,theMax : float,isInfinite : bool=False) -> None: ...
    pass
class Message_ProgressSentry(Message_ProgressScope):
    """
    Functionality of this class (Message_ProgressSentry) has been superseded by Message_ProgressScope. This class is kept just to simplify transition of an old code and will be removed in future.
    """
    def Close(self) -> None: 
        """
        Closes the scope and advances the progress to its end. Closed scope should not be used.

        Closes the scope and advances the progress to its end. Closed scope should not be used.
        """
    def GetPortion(self) -> float: 
        """
        Get the portion of the indicator covered by this scope (from 0 to 1)
        """
    def IsActive(self) -> bool: 
        """
        Returns true if this progress scope is attached to some indicator.
        """
    def IsInfinite(self) -> bool: 
        """
        Returns the infinite flag
        """
    def MaxValue(self) -> float: 
        """
        Returns the maximal value of progress in this scope
        """
    def More(self) -> bool: 
        """
        Returns false if ProgressIndicator signals UserBreak
        """
    def Name(self) -> str: 
        """
        Returns the name of the scope (may be null). Scopes with null name (e.g. root scope) should be bypassed when reporting progress to the user.
        """
    @overload
    def Next(self,theStep : float=1.0) -> Message_ProgressRange: 
        """
        Advances position by specified step and returns the range covering this step

        Advances position by specified step and returns the range covering this step
        """
    @overload
    def Next(self,theStep : float) -> Message_ProgressRange: ...
    def Parent(self) -> Message_ProgressScope: 
        """
        Returns parent scope (null for top-level scope)
        """
    def Relieve(self) -> None: 
        """
        Method Relieve() was replaced by Close() in Message_ProgressScope
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the name of the scope.
        """
    def Show(self) -> None: 
        """
        Force update of presentation of the progress indicator. Should not be called concurrently.

        Force update of presentation of the progress indicator. Should not be called concurrently.
        """
    def UserBreak(self) -> bool: 
        """
        Returns true if ProgressIndicator signals UserBreak

        Returns true if ProgressIndicator signals UserBreak
        """
    def Value(self) -> float: 
        """
        Returns the current value of progress in this scope.

        Returns the current value of progress in this scope.
        """
    def __init__(self,theRange : Message_ProgressRange,theName : str,theMin : float,theMax : float,theStep : float,theIsInf : bool=False,theNewScopeSpan : float=0.0) -> None: ...
    pass
class Message_Report(OCP.Standard.Standard_Transient):
    """
    Container for alert messages, sorted according to their gravity.Container for alert messages, sorted according to their gravity.Container for alert messages, sorted according to their gravity.
    """
    def ActivateInMessenger(self,toActivate : bool,theMessenger : Message_Messenger=None) -> None: 
        """
        Creates an instance of Message_PrinterToReport with the current report and register it in messenger
        """
    def ActiveMetrics(self) -> Any: 
        """
        Returns computed metrics when alerts are performed
        """
    def AddAlert(self,theGravity : Message_Gravity,theAlert : Message_Alert) -> None: 
        """
        Add alert with specified gravity. This method is thread-safe, i.e. alerts can be added from parallel threads safely.
        """
    def AddLevel(self,theLevel : Message_Level,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Add new level of alerts
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
    def ClearMetrics(self) -> None: 
        """
        Removes all activated metrics
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Dump(self,theOS : io.BytesIO) -> None: 
        """
        Dumps all collected alerts to stream

        Dumps collected alerts with specified gravity to stream
        """
    @overload
    def Dump(self,theOS : io.BytesIO,theGravity : Message_Gravity) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
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
    def IsActiveInMessenger(self,theMessenger : Message_Messenger=None) -> bool: 
        """
        Returns true if a report printer for the current report is registered in the messenger
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
    def Limit(self) -> int: 
        """
        Returns maximum number of collecting alerts. If the limit is achieved, first alert is removed, the new alert is added in the container.
        """
    @overload
    def Merge(self,theOther : Message_Report) -> None: 
        """
        Merges data from theOther report into this

        Merges alerts with specified gravity from theOther report into this
        """
    @overload
    def Merge(self,theOther : Message_Report,theGravity : Message_Gravity) -> None: ...
    def RemoveLevel(self,theLevel : Message_Level) -> None: 
        """
        Remove level of alerts
        """
    @overload
    def SendMessages(self,theMessenger : Message_Messenger) -> None: 
        """
        Sends all collected alerts to messenger.

        Dumps collected alerts with specified gravity to messenger. Default implementation creates Message_Msg object with a message key returned by alert, and sends it in the messenger.
        """
    @overload
    def SendMessages(self,theMessenger : Message_Messenger,theGravity : Message_Gravity) -> None: ...
    def SetActiveMetric(self,theMetricType : Message_MetricType,theActivate : bool) -> None: 
        """
        Sets metrics to compute when alerts are performed
        """
    def SetLimit(self,theLimit : int) -> None: 
        """
        Sets maximum number of collecting alerts.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateActiveInMessenger(self,theMessenger : Message_Messenger=None) -> None: 
        """
        Updates internal flag IsActiveInMessenger. It becomes true if messenger contains at least one instance of Message_PrinterToReport.
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
    def InsertAfter(self,theIndex : int,theItem : Message_Printer) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Message_SequenceOfPrinters) -> None: ...
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
    def Prepend(self,theItem : Message_Printer) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Message_SequenceOfPrinters) -> None: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Message_SequenceOfPrinters) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
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
    Message_Alarm1: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm1: 1024>
    Message_Alarm10: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm10: 1033>
    Message_Alarm11: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm11: 1034>
    Message_Alarm12: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm12: 1035>
    Message_Alarm13: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm13: 1036>
    Message_Alarm14: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm14: 1037>
    Message_Alarm15: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm15: 1038>
    Message_Alarm16: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm16: 1039>
    Message_Alarm17: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm17: 1040>
    Message_Alarm18: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm18: 1041>
    Message_Alarm19: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm19: 1042>
    Message_Alarm2: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm2: 1025>
    Message_Alarm20: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm20: 1043>
    Message_Alarm21: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm21: 1044>
    Message_Alarm22: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm22: 1045>
    Message_Alarm23: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm23: 1046>
    Message_Alarm24: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm24: 1047>
    Message_Alarm25: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm25: 1048>
    Message_Alarm26: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm26: 1049>
    Message_Alarm27: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm27: 1050>
    Message_Alarm28: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm28: 1051>
    Message_Alarm29: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm29: 1052>
    Message_Alarm3: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm3: 1026>
    Message_Alarm30: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm30: 1053>
    Message_Alarm31: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm31: 1054>
    Message_Alarm32: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm32: 1055>
    Message_Alarm4: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm4: 1027>
    Message_Alarm5: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm5: 1028>
    Message_Alarm6: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm6: 1029>
    Message_Alarm7: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm7: 1030>
    Message_Alarm8: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm8: 1031>
    Message_Alarm9: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm9: 1032>
    Message_Done1: OCP.Message.Message_Status # value = <Message_Status.Message_Done1: 256>
    Message_Done10: OCP.Message.Message_Status # value = <Message_Status.Message_Done10: 265>
    Message_Done11: OCP.Message.Message_Status # value = <Message_Status.Message_Done11: 266>
    Message_Done12: OCP.Message.Message_Status # value = <Message_Status.Message_Done12: 267>
    Message_Done13: OCP.Message.Message_Status # value = <Message_Status.Message_Done13: 268>
    Message_Done14: OCP.Message.Message_Status # value = <Message_Status.Message_Done14: 269>
    Message_Done15: OCP.Message.Message_Status # value = <Message_Status.Message_Done15: 270>
    Message_Done16: OCP.Message.Message_Status # value = <Message_Status.Message_Done16: 271>
    Message_Done17: OCP.Message.Message_Status # value = <Message_Status.Message_Done17: 272>
    Message_Done18: OCP.Message.Message_Status # value = <Message_Status.Message_Done18: 273>
    Message_Done19: OCP.Message.Message_Status # value = <Message_Status.Message_Done19: 274>
    Message_Done2: OCP.Message.Message_Status # value = <Message_Status.Message_Done2: 257>
    Message_Done20: OCP.Message.Message_Status # value = <Message_Status.Message_Done20: 275>
    Message_Done21: OCP.Message.Message_Status # value = <Message_Status.Message_Done21: 276>
    Message_Done22: OCP.Message.Message_Status # value = <Message_Status.Message_Done22: 277>
    Message_Done23: OCP.Message.Message_Status # value = <Message_Status.Message_Done23: 278>
    Message_Done24: OCP.Message.Message_Status # value = <Message_Status.Message_Done24: 279>
    Message_Done25: OCP.Message.Message_Status # value = <Message_Status.Message_Done25: 280>
    Message_Done26: OCP.Message.Message_Status # value = <Message_Status.Message_Done26: 281>
    Message_Done27: OCP.Message.Message_Status # value = <Message_Status.Message_Done27: 282>
    Message_Done28: OCP.Message.Message_Status # value = <Message_Status.Message_Done28: 283>
    Message_Done29: OCP.Message.Message_Status # value = <Message_Status.Message_Done29: 284>
    Message_Done3: OCP.Message.Message_Status # value = <Message_Status.Message_Done3: 258>
    Message_Done30: OCP.Message.Message_Status # value = <Message_Status.Message_Done30: 285>
    Message_Done31: OCP.Message.Message_Status # value = <Message_Status.Message_Done31: 286>
    Message_Done32: OCP.Message.Message_Status # value = <Message_Status.Message_Done32: 287>
    Message_Done4: OCP.Message.Message_Status # value = <Message_Status.Message_Done4: 259>
    Message_Done5: OCP.Message.Message_Status # value = <Message_Status.Message_Done5: 260>
    Message_Done6: OCP.Message.Message_Status # value = <Message_Status.Message_Done6: 261>
    Message_Done7: OCP.Message.Message_Status # value = <Message_Status.Message_Done7: 262>
    Message_Done8: OCP.Message.Message_Status # value = <Message_Status.Message_Done8: 263>
    Message_Done9: OCP.Message.Message_Status # value = <Message_Status.Message_Done9: 264>
    Message_Fail1: OCP.Message.Message_Status # value = <Message_Status.Message_Fail1: 2048>
    Message_Fail10: OCP.Message.Message_Status # value = <Message_Status.Message_Fail10: 2057>
    Message_Fail11: OCP.Message.Message_Status # value = <Message_Status.Message_Fail11: 2058>
    Message_Fail12: OCP.Message.Message_Status # value = <Message_Status.Message_Fail12: 2059>
    Message_Fail13: OCP.Message.Message_Status # value = <Message_Status.Message_Fail13: 2060>
    Message_Fail14: OCP.Message.Message_Status # value = <Message_Status.Message_Fail14: 2061>
    Message_Fail15: OCP.Message.Message_Status # value = <Message_Status.Message_Fail15: 2062>
    Message_Fail16: OCP.Message.Message_Status # value = <Message_Status.Message_Fail16: 2063>
    Message_Fail17: OCP.Message.Message_Status # value = <Message_Status.Message_Fail17: 2064>
    Message_Fail18: OCP.Message.Message_Status # value = <Message_Status.Message_Fail18: 2065>
    Message_Fail19: OCP.Message.Message_Status # value = <Message_Status.Message_Fail19: 2066>
    Message_Fail2: OCP.Message.Message_Status # value = <Message_Status.Message_Fail2: 2049>
    Message_Fail20: OCP.Message.Message_Status # value = <Message_Status.Message_Fail20: 2067>
    Message_Fail21: OCP.Message.Message_Status # value = <Message_Status.Message_Fail21: 2068>
    Message_Fail22: OCP.Message.Message_Status # value = <Message_Status.Message_Fail22: 2069>
    Message_Fail23: OCP.Message.Message_Status # value = <Message_Status.Message_Fail23: 2070>
    Message_Fail24: OCP.Message.Message_Status # value = <Message_Status.Message_Fail24: 2071>
    Message_Fail25: OCP.Message.Message_Status # value = <Message_Status.Message_Fail25: 2072>
    Message_Fail26: OCP.Message.Message_Status # value = <Message_Status.Message_Fail26: 2073>
    Message_Fail27: OCP.Message.Message_Status # value = <Message_Status.Message_Fail27: 2074>
    Message_Fail28: OCP.Message.Message_Status # value = <Message_Status.Message_Fail28: 2075>
    Message_Fail29: OCP.Message.Message_Status # value = <Message_Status.Message_Fail29: 2076>
    Message_Fail3: OCP.Message.Message_Status # value = <Message_Status.Message_Fail3: 2050>
    Message_Fail30: OCP.Message.Message_Status # value = <Message_Status.Message_Fail30: 2077>
    Message_Fail31: OCP.Message.Message_Status # value = <Message_Status.Message_Fail31: 2078>
    Message_Fail32: OCP.Message.Message_Status # value = <Message_Status.Message_Fail32: 2079>
    Message_Fail4: OCP.Message.Message_Status # value = <Message_Status.Message_Fail4: 2051>
    Message_Fail5: OCP.Message.Message_Status # value = <Message_Status.Message_Fail5: 2052>
    Message_Fail6: OCP.Message.Message_Status # value = <Message_Status.Message_Fail6: 2053>
    Message_Fail7: OCP.Message.Message_Status # value = <Message_Status.Message_Fail7: 2054>
    Message_Fail8: OCP.Message.Message_Status # value = <Message_Status.Message_Fail8: 2055>
    Message_Fail9: OCP.Message.Message_Status # value = <Message_Status.Message_Fail9: 2056>
    Message_None: OCP.Message.Message_Status # value = <Message_Status.Message_None: 0>
    Message_Warn1: OCP.Message.Message_Status # value = <Message_Status.Message_Warn1: 512>
    Message_Warn10: OCP.Message.Message_Status # value = <Message_Status.Message_Warn10: 521>
    Message_Warn11: OCP.Message.Message_Status # value = <Message_Status.Message_Warn11: 522>
    Message_Warn12: OCP.Message.Message_Status # value = <Message_Status.Message_Warn12: 523>
    Message_Warn13: OCP.Message.Message_Status # value = <Message_Status.Message_Warn13: 524>
    Message_Warn14: OCP.Message.Message_Status # value = <Message_Status.Message_Warn14: 525>
    Message_Warn15: OCP.Message.Message_Status # value = <Message_Status.Message_Warn15: 526>
    Message_Warn16: OCP.Message.Message_Status # value = <Message_Status.Message_Warn16: 527>
    Message_Warn17: OCP.Message.Message_Status # value = <Message_Status.Message_Warn17: 528>
    Message_Warn18: OCP.Message.Message_Status # value = <Message_Status.Message_Warn18: 529>
    Message_Warn19: OCP.Message.Message_Status # value = <Message_Status.Message_Warn19: 530>
    Message_Warn2: OCP.Message.Message_Status # value = <Message_Status.Message_Warn2: 513>
    Message_Warn20: OCP.Message.Message_Status # value = <Message_Status.Message_Warn20: 531>
    Message_Warn21: OCP.Message.Message_Status # value = <Message_Status.Message_Warn21: 532>
    Message_Warn22: OCP.Message.Message_Status # value = <Message_Status.Message_Warn22: 533>
    Message_Warn23: OCP.Message.Message_Status # value = <Message_Status.Message_Warn23: 534>
    Message_Warn24: OCP.Message.Message_Status # value = <Message_Status.Message_Warn24: 535>
    Message_Warn25: OCP.Message.Message_Status # value = <Message_Status.Message_Warn25: 536>
    Message_Warn26: OCP.Message.Message_Status # value = <Message_Status.Message_Warn26: 537>
    Message_Warn27: OCP.Message.Message_Status # value = <Message_Status.Message_Warn27: 538>
    Message_Warn28: OCP.Message.Message_Status # value = <Message_Status.Message_Warn28: 539>
    Message_Warn29: OCP.Message.Message_Status # value = <Message_Status.Message_Warn29: 540>
    Message_Warn3: OCP.Message.Message_Status # value = <Message_Status.Message_Warn3: 514>
    Message_Warn30: OCP.Message.Message_Status # value = <Message_Status.Message_Warn30: 541>
    Message_Warn31: OCP.Message.Message_Status # value = <Message_Status.Message_Warn31: 542>
    Message_Warn32: OCP.Message.Message_Status # value = <Message_Status.Message_Warn32: 543>
    Message_Warn4: OCP.Message.Message_Status # value = <Message_Status.Message_Warn4: 515>
    Message_Warn5: OCP.Message.Message_Status # value = <Message_Status.Message_Warn5: 516>
    Message_Warn6: OCP.Message.Message_Status # value = <Message_Status.Message_Warn6: 517>
    Message_Warn7: OCP.Message.Message_Status # value = <Message_Status.Message_Warn7: 518>
    Message_Warn8: OCP.Message.Message_Status # value = <Message_Status.Message_Warn8: 519>
    Message_Warn9: OCP.Message.Message_Status # value = <Message_Status.Message_Warn9: 520>
    __entries: dict # value = {'Message_None': (<Message_Status.Message_None: 0>, None), 'Message_Done1': (<Message_Status.Message_Done1: 256>, None), 'Message_Done2': (<Message_Status.Message_Done2: 257>, None), 'Message_Done3': (<Message_Status.Message_Done3: 258>, None), 'Message_Done4': (<Message_Status.Message_Done4: 259>, None), 'Message_Done5': (<Message_Status.Message_Done5: 260>, None), 'Message_Done6': (<Message_Status.Message_Done6: 261>, None), 'Message_Done7': (<Message_Status.Message_Done7: 262>, None), 'Message_Done8': (<Message_Status.Message_Done8: 263>, None), 'Message_Done9': (<Message_Status.Message_Done9: 264>, None), 'Message_Done10': (<Message_Status.Message_Done10: 265>, None), 'Message_Done11': (<Message_Status.Message_Done11: 266>, None), 'Message_Done12': (<Message_Status.Message_Done12: 267>, None), 'Message_Done13': (<Message_Status.Message_Done13: 268>, None), 'Message_Done14': (<Message_Status.Message_Done14: 269>, None), 'Message_Done15': (<Message_Status.Message_Done15: 270>, None), 'Message_Done16': (<Message_Status.Message_Done16: 271>, None), 'Message_Done17': (<Message_Status.Message_Done17: 272>, None), 'Message_Done18': (<Message_Status.Message_Done18: 273>, None), 'Message_Done19': (<Message_Status.Message_Done19: 274>, None), 'Message_Done20': (<Message_Status.Message_Done20: 275>, None), 'Message_Done21': (<Message_Status.Message_Done21: 276>, None), 'Message_Done22': (<Message_Status.Message_Done22: 277>, None), 'Message_Done23': (<Message_Status.Message_Done23: 278>, None), 'Message_Done24': (<Message_Status.Message_Done24: 279>, None), 'Message_Done25': (<Message_Status.Message_Done25: 280>, None), 'Message_Done26': (<Message_Status.Message_Done26: 281>, None), 'Message_Done27': (<Message_Status.Message_Done27: 282>, None), 'Message_Done28': (<Message_Status.Message_Done28: 283>, None), 'Message_Done29': (<Message_Status.Message_Done29: 284>, None), 'Message_Done30': (<Message_Status.Message_Done30: 285>, None), 'Message_Done31': (<Message_Status.Message_Done31: 286>, None), 'Message_Done32': (<Message_Status.Message_Done32: 287>, None), 'Message_Warn1': (<Message_Status.Message_Warn1: 512>, None), 'Message_Warn2': (<Message_Status.Message_Warn2: 513>, None), 'Message_Warn3': (<Message_Status.Message_Warn3: 514>, None), 'Message_Warn4': (<Message_Status.Message_Warn4: 515>, None), 'Message_Warn5': (<Message_Status.Message_Warn5: 516>, None), 'Message_Warn6': (<Message_Status.Message_Warn6: 517>, None), 'Message_Warn7': (<Message_Status.Message_Warn7: 518>, None), 'Message_Warn8': (<Message_Status.Message_Warn8: 519>, None), 'Message_Warn9': (<Message_Status.Message_Warn9: 520>, None), 'Message_Warn10': (<Message_Status.Message_Warn10: 521>, None), 'Message_Warn11': (<Message_Status.Message_Warn11: 522>, None), 'Message_Warn12': (<Message_Status.Message_Warn12: 523>, None), 'Message_Warn13': (<Message_Status.Message_Warn13: 524>, None), 'Message_Warn14': (<Message_Status.Message_Warn14: 525>, None), 'Message_Warn15': (<Message_Status.Message_Warn15: 526>, None), 'Message_Warn16': (<Message_Status.Message_Warn16: 527>, None), 'Message_Warn17': (<Message_Status.Message_Warn17: 528>, None), 'Message_Warn18': (<Message_Status.Message_Warn18: 529>, None), 'Message_Warn19': (<Message_Status.Message_Warn19: 530>, None), 'Message_Warn20': (<Message_Status.Message_Warn20: 531>, None), 'Message_Warn21': (<Message_Status.Message_Warn21: 532>, None), 'Message_Warn22': (<Message_Status.Message_Warn22: 533>, None), 'Message_Warn23': (<Message_Status.Message_Warn23: 534>, None), 'Message_Warn24': (<Message_Status.Message_Warn24: 535>, None), 'Message_Warn25': (<Message_Status.Message_Warn25: 536>, None), 'Message_Warn26': (<Message_Status.Message_Warn26: 537>, None), 'Message_Warn27': (<Message_Status.Message_Warn27: 538>, None), 'Message_Warn28': (<Message_Status.Message_Warn28: 539>, None), 'Message_Warn29': (<Message_Status.Message_Warn29: 540>, None), 'Message_Warn30': (<Message_Status.Message_Warn30: 541>, None), 'Message_Warn31': (<Message_Status.Message_Warn31: 542>, None), 'Message_Warn32': (<Message_Status.Message_Warn32: 543>, None), 'Message_Alarm1': (<Message_Status.Message_Alarm1: 1024>, None), 'Message_Alarm2': (<Message_Status.Message_Alarm2: 1025>, None), 'Message_Alarm3': (<Message_Status.Message_Alarm3: 1026>, None), 'Message_Alarm4': (<Message_Status.Message_Alarm4: 1027>, None), 'Message_Alarm5': (<Message_Status.Message_Alarm5: 1028>, None), 'Message_Alarm6': (<Message_Status.Message_Alarm6: 1029>, None), 'Message_Alarm7': (<Message_Status.Message_Alarm7: 1030>, None), 'Message_Alarm8': (<Message_Status.Message_Alarm8: 1031>, None), 'Message_Alarm9': (<Message_Status.Message_Alarm9: 1032>, None), 'Message_Alarm10': (<Message_Status.Message_Alarm10: 1033>, None), 'Message_Alarm11': (<Message_Status.Message_Alarm11: 1034>, None), 'Message_Alarm12': (<Message_Status.Message_Alarm12: 1035>, None), 'Message_Alarm13': (<Message_Status.Message_Alarm13: 1036>, None), 'Message_Alarm14': (<Message_Status.Message_Alarm14: 1037>, None), 'Message_Alarm15': (<Message_Status.Message_Alarm15: 1038>, None), 'Message_Alarm16': (<Message_Status.Message_Alarm16: 1039>, None), 'Message_Alarm17': (<Message_Status.Message_Alarm17: 1040>, None), 'Message_Alarm18': (<Message_Status.Message_Alarm18: 1041>, None), 'Message_Alarm19': (<Message_Status.Message_Alarm19: 1042>, None), 'Message_Alarm20': (<Message_Status.Message_Alarm20: 1043>, None), 'Message_Alarm21': (<Message_Status.Message_Alarm21: 1044>, None), 'Message_Alarm22': (<Message_Status.Message_Alarm22: 1045>, None), 'Message_Alarm23': (<Message_Status.Message_Alarm23: 1046>, None), 'Message_Alarm24': (<Message_Status.Message_Alarm24: 1047>, None), 'Message_Alarm25': (<Message_Status.Message_Alarm25: 1048>, None), 'Message_Alarm26': (<Message_Status.Message_Alarm26: 1049>, None), 'Message_Alarm27': (<Message_Status.Message_Alarm27: 1050>, None), 'Message_Alarm28': (<Message_Status.Message_Alarm28: 1051>, None), 'Message_Alarm29': (<Message_Status.Message_Alarm29: 1052>, None), 'Message_Alarm30': (<Message_Status.Message_Alarm30: 1053>, None), 'Message_Alarm31': (<Message_Status.Message_Alarm31: 1054>, None), 'Message_Alarm32': (<Message_Status.Message_Alarm32: 1055>, None), 'Message_Fail1': (<Message_Status.Message_Fail1: 2048>, None), 'Message_Fail2': (<Message_Status.Message_Fail2: 2049>, None), 'Message_Fail3': (<Message_Status.Message_Fail3: 2050>, None), 'Message_Fail4': (<Message_Status.Message_Fail4: 2051>, None), 'Message_Fail5': (<Message_Status.Message_Fail5: 2052>, None), 'Message_Fail6': (<Message_Status.Message_Fail6: 2053>, None), 'Message_Fail7': (<Message_Status.Message_Fail7: 2054>, None), 'Message_Fail8': (<Message_Status.Message_Fail8: 2055>, None), 'Message_Fail9': (<Message_Status.Message_Fail9: 2056>, None), 'Message_Fail10': (<Message_Status.Message_Fail10: 2057>, None), 'Message_Fail11': (<Message_Status.Message_Fail11: 2058>, None), 'Message_Fail12': (<Message_Status.Message_Fail12: 2059>, None), 'Message_Fail13': (<Message_Status.Message_Fail13: 2060>, None), 'Message_Fail14': (<Message_Status.Message_Fail14: 2061>, None), 'Message_Fail15': (<Message_Status.Message_Fail15: 2062>, None), 'Message_Fail16': (<Message_Status.Message_Fail16: 2063>, None), 'Message_Fail17': (<Message_Status.Message_Fail17: 2064>, None), 'Message_Fail18': (<Message_Status.Message_Fail18: 2065>, None), 'Message_Fail19': (<Message_Status.Message_Fail19: 2066>, None), 'Message_Fail20': (<Message_Status.Message_Fail20: 2067>, None), 'Message_Fail21': (<Message_Status.Message_Fail21: 2068>, None), 'Message_Fail22': (<Message_Status.Message_Fail22: 2069>, None), 'Message_Fail23': (<Message_Status.Message_Fail23: 2070>, None), 'Message_Fail24': (<Message_Status.Message_Fail24: 2071>, None), 'Message_Fail25': (<Message_Status.Message_Fail25: 2072>, None), 'Message_Fail26': (<Message_Status.Message_Fail26: 2073>, None), 'Message_Fail27': (<Message_Status.Message_Fail27: 2074>, None), 'Message_Fail28': (<Message_Status.Message_Fail28: 2075>, None), 'Message_Fail29': (<Message_Status.Message_Fail29: 2076>, None), 'Message_Fail30': (<Message_Status.Message_Fail30: 2077>, None), 'Message_Fail31': (<Message_Status.Message_Fail31: 2078>, None), 'Message_Fail32': (<Message_Status.Message_Fail32: 2079>, None)}
    __members__: dict # value = {'Message_None': <Message_Status.Message_None: 0>, 'Message_Done1': <Message_Status.Message_Done1: 256>, 'Message_Done2': <Message_Status.Message_Done2: 257>, 'Message_Done3': <Message_Status.Message_Done3: 258>, 'Message_Done4': <Message_Status.Message_Done4: 259>, 'Message_Done5': <Message_Status.Message_Done5: 260>, 'Message_Done6': <Message_Status.Message_Done6: 261>, 'Message_Done7': <Message_Status.Message_Done7: 262>, 'Message_Done8': <Message_Status.Message_Done8: 263>, 'Message_Done9': <Message_Status.Message_Done9: 264>, 'Message_Done10': <Message_Status.Message_Done10: 265>, 'Message_Done11': <Message_Status.Message_Done11: 266>, 'Message_Done12': <Message_Status.Message_Done12: 267>, 'Message_Done13': <Message_Status.Message_Done13: 268>, 'Message_Done14': <Message_Status.Message_Done14: 269>, 'Message_Done15': <Message_Status.Message_Done15: 270>, 'Message_Done16': <Message_Status.Message_Done16: 271>, 'Message_Done17': <Message_Status.Message_Done17: 272>, 'Message_Done18': <Message_Status.Message_Done18: 273>, 'Message_Done19': <Message_Status.Message_Done19: 274>, 'Message_Done20': <Message_Status.Message_Done20: 275>, 'Message_Done21': <Message_Status.Message_Done21: 276>, 'Message_Done22': <Message_Status.Message_Done22: 277>, 'Message_Done23': <Message_Status.Message_Done23: 278>, 'Message_Done24': <Message_Status.Message_Done24: 279>, 'Message_Done25': <Message_Status.Message_Done25: 280>, 'Message_Done26': <Message_Status.Message_Done26: 281>, 'Message_Done27': <Message_Status.Message_Done27: 282>, 'Message_Done28': <Message_Status.Message_Done28: 283>, 'Message_Done29': <Message_Status.Message_Done29: 284>, 'Message_Done30': <Message_Status.Message_Done30: 285>, 'Message_Done31': <Message_Status.Message_Done31: 286>, 'Message_Done32': <Message_Status.Message_Done32: 287>, 'Message_Warn1': <Message_Status.Message_Warn1: 512>, 'Message_Warn2': <Message_Status.Message_Warn2: 513>, 'Message_Warn3': <Message_Status.Message_Warn3: 514>, 'Message_Warn4': <Message_Status.Message_Warn4: 515>, 'Message_Warn5': <Message_Status.Message_Warn5: 516>, 'Message_Warn6': <Message_Status.Message_Warn6: 517>, 'Message_Warn7': <Message_Status.Message_Warn7: 518>, 'Message_Warn8': <Message_Status.Message_Warn8: 519>, 'Message_Warn9': <Message_Status.Message_Warn9: 520>, 'Message_Warn10': <Message_Status.Message_Warn10: 521>, 'Message_Warn11': <Message_Status.Message_Warn11: 522>, 'Message_Warn12': <Message_Status.Message_Warn12: 523>, 'Message_Warn13': <Message_Status.Message_Warn13: 524>, 'Message_Warn14': <Message_Status.Message_Warn14: 525>, 'Message_Warn15': <Message_Status.Message_Warn15: 526>, 'Message_Warn16': <Message_Status.Message_Warn16: 527>, 'Message_Warn17': <Message_Status.Message_Warn17: 528>, 'Message_Warn18': <Message_Status.Message_Warn18: 529>, 'Message_Warn19': <Message_Status.Message_Warn19: 530>, 'Message_Warn20': <Message_Status.Message_Warn20: 531>, 'Message_Warn21': <Message_Status.Message_Warn21: 532>, 'Message_Warn22': <Message_Status.Message_Warn22: 533>, 'Message_Warn23': <Message_Status.Message_Warn23: 534>, 'Message_Warn24': <Message_Status.Message_Warn24: 535>, 'Message_Warn25': <Message_Status.Message_Warn25: 536>, 'Message_Warn26': <Message_Status.Message_Warn26: 537>, 'Message_Warn27': <Message_Status.Message_Warn27: 538>, 'Message_Warn28': <Message_Status.Message_Warn28: 539>, 'Message_Warn29': <Message_Status.Message_Warn29: 540>, 'Message_Warn30': <Message_Status.Message_Warn30: 541>, 'Message_Warn31': <Message_Status.Message_Warn31: 542>, 'Message_Warn32': <Message_Status.Message_Warn32: 543>, 'Message_Alarm1': <Message_Status.Message_Alarm1: 1024>, 'Message_Alarm2': <Message_Status.Message_Alarm2: 1025>, 'Message_Alarm3': <Message_Status.Message_Alarm3: 1026>, 'Message_Alarm4': <Message_Status.Message_Alarm4: 1027>, 'Message_Alarm5': <Message_Status.Message_Alarm5: 1028>, 'Message_Alarm6': <Message_Status.Message_Alarm6: 1029>, 'Message_Alarm7': <Message_Status.Message_Alarm7: 1030>, 'Message_Alarm8': <Message_Status.Message_Alarm8: 1031>, 'Message_Alarm9': <Message_Status.Message_Alarm9: 1032>, 'Message_Alarm10': <Message_Status.Message_Alarm10: 1033>, 'Message_Alarm11': <Message_Status.Message_Alarm11: 1034>, 'Message_Alarm12': <Message_Status.Message_Alarm12: 1035>, 'Message_Alarm13': <Message_Status.Message_Alarm13: 1036>, 'Message_Alarm14': <Message_Status.Message_Alarm14: 1037>, 'Message_Alarm15': <Message_Status.Message_Alarm15: 1038>, 'Message_Alarm16': <Message_Status.Message_Alarm16: 1039>, 'Message_Alarm17': <Message_Status.Message_Alarm17: 1040>, 'Message_Alarm18': <Message_Status.Message_Alarm18: 1041>, 'Message_Alarm19': <Message_Status.Message_Alarm19: 1042>, 'Message_Alarm20': <Message_Status.Message_Alarm20: 1043>, 'Message_Alarm21': <Message_Status.Message_Alarm21: 1044>, 'Message_Alarm22': <Message_Status.Message_Alarm22: 1045>, 'Message_Alarm23': <Message_Status.Message_Alarm23: 1046>, 'Message_Alarm24': <Message_Status.Message_Alarm24: 1047>, 'Message_Alarm25': <Message_Status.Message_Alarm25: 1048>, 'Message_Alarm26': <Message_Status.Message_Alarm26: 1049>, 'Message_Alarm27': <Message_Status.Message_Alarm27: 1050>, 'Message_Alarm28': <Message_Status.Message_Alarm28: 1051>, 'Message_Alarm29': <Message_Status.Message_Alarm29: 1052>, 'Message_Alarm30': <Message_Status.Message_Alarm30: 1053>, 'Message_Alarm31': <Message_Status.Message_Alarm31: 1054>, 'Message_Alarm32': <Message_Status.Message_Alarm32: 1055>, 'Message_Fail1': <Message_Status.Message_Fail1: 2048>, 'Message_Fail2': <Message_Status.Message_Fail2: 2049>, 'Message_Fail3': <Message_Status.Message_Fail3: 2050>, 'Message_Fail4': <Message_Status.Message_Fail4: 2051>, 'Message_Fail5': <Message_Status.Message_Fail5: 2052>, 'Message_Fail6': <Message_Status.Message_Fail6: 2053>, 'Message_Fail7': <Message_Status.Message_Fail7: 2054>, 'Message_Fail8': <Message_Status.Message_Fail8: 2055>, 'Message_Fail9': <Message_Status.Message_Fail9: 2056>, 'Message_Fail10': <Message_Status.Message_Fail10: 2057>, 'Message_Fail11': <Message_Status.Message_Fail11: 2058>, 'Message_Fail12': <Message_Status.Message_Fail12: 2059>, 'Message_Fail13': <Message_Status.Message_Fail13: 2060>, 'Message_Fail14': <Message_Status.Message_Fail14: 2061>, 'Message_Fail15': <Message_Status.Message_Fail15: 2062>, 'Message_Fail16': <Message_Status.Message_Fail16: 2063>, 'Message_Fail17': <Message_Status.Message_Fail17: 2064>, 'Message_Fail18': <Message_Status.Message_Fail18: 2065>, 'Message_Fail19': <Message_Status.Message_Fail19: 2066>, 'Message_Fail20': <Message_Status.Message_Fail20: 2067>, 'Message_Fail21': <Message_Status.Message_Fail21: 2068>, 'Message_Fail22': <Message_Status.Message_Fail22: 2069>, 'Message_Fail23': <Message_Status.Message_Fail23: 2070>, 'Message_Fail24': <Message_Status.Message_Fail24: 2071>, 'Message_Fail25': <Message_Status.Message_Fail25: 2072>, 'Message_Fail26': <Message_Status.Message_Fail26: 2073>, 'Message_Fail27': <Message_Status.Message_Fail27: 2074>, 'Message_Fail28': <Message_Status.Message_Fail28: 2075>, 'Message_Fail29': <Message_Status.Message_Fail29: 2076>, 'Message_Fail30': <Message_Status.Message_Fail30: 2077>, 'Message_Fail31': <Message_Status.Message_Fail31: 2078>, 'Message_Fail32': <Message_Status.Message_Fail32: 2079>}
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
    Message_ALARM: OCP.Message.Message_StatusType # value = <Message_StatusType.Message_ALARM: 1024>
    Message_DONE: OCP.Message.Message_StatusType # value = <Message_StatusType.Message_DONE: 256>
    Message_FAIL: OCP.Message.Message_StatusType # value = <Message_StatusType.Message_FAIL: 2048>
    Message_WARN: OCP.Message.Message_StatusType # value = <Message_StatusType.Message_WARN: 512>
    __entries: dict # value = {'Message_DONE': (<Message_StatusType.Message_DONE: 256>, None), 'Message_WARN': (<Message_StatusType.Message_WARN: 512>, None), 'Message_ALARM': (<Message_StatusType.Message_ALARM: 1024>, None), 'Message_FAIL': (<Message_StatusType.Message_FAIL: 2048>, None)}
    __members__: dict # value = {'Message_DONE': <Message_StatusType.Message_DONE: 256>, 'Message_WARN': <Message_StatusType.Message_WARN: 512>, 'Message_ALARM': <Message_StatusType.Message_ALARM: 1024>, 'Message_FAIL': <Message_StatusType.Message_FAIL: 2048>}
    pass
Message_ALARM: OCP.Message.Message_StatusType # value = <Message_StatusType.Message_ALARM: 1024>
Message_Alarm: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Alarm: 3>
Message_Alarm1: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm1: 1024>
Message_Alarm10: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm10: 1033>
Message_Alarm11: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm11: 1034>
Message_Alarm12: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm12: 1035>
Message_Alarm13: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm13: 1036>
Message_Alarm14: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm14: 1037>
Message_Alarm15: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm15: 1038>
Message_Alarm16: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm16: 1039>
Message_Alarm17: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm17: 1040>
Message_Alarm18: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm18: 1041>
Message_Alarm19: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm19: 1042>
Message_Alarm2: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm2: 1025>
Message_Alarm20: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm20: 1043>
Message_Alarm21: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm21: 1044>
Message_Alarm22: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm22: 1045>
Message_Alarm23: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm23: 1046>
Message_Alarm24: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm24: 1047>
Message_Alarm25: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm25: 1048>
Message_Alarm26: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm26: 1049>
Message_Alarm27: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm27: 1050>
Message_Alarm28: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm28: 1051>
Message_Alarm29: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm29: 1052>
Message_Alarm3: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm3: 1026>
Message_Alarm30: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm30: 1053>
Message_Alarm31: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm31: 1054>
Message_Alarm32: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm32: 1055>
Message_Alarm4: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm4: 1027>
Message_Alarm5: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm5: 1028>
Message_Alarm6: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm6: 1029>
Message_Alarm7: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm7: 1030>
Message_Alarm8: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm8: 1031>
Message_Alarm9: OCP.Message.Message_Status # value = <Message_Status.Message_Alarm9: 1032>
Message_ConsoleColor_Black: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Black: 1>
Message_ConsoleColor_Blue: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Blue: 4>
Message_ConsoleColor_Cyan: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Cyan: 7>
Message_ConsoleColor_Default: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Default: 0>
Message_ConsoleColor_Green: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Green: 5>
Message_ConsoleColor_Magenta: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Magenta: 8>
Message_ConsoleColor_Red: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Red: 3>
Message_ConsoleColor_White: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_White: 2>
Message_ConsoleColor_Yellow: OCP.Message.Message_ConsoleColor # value = <Message_ConsoleColor.Message_ConsoleColor_Yellow: 6>
Message_DONE: OCP.Message.Message_StatusType # value = <Message_StatusType.Message_DONE: 256>
Message_Done1: OCP.Message.Message_Status # value = <Message_Status.Message_Done1: 256>
Message_Done10: OCP.Message.Message_Status # value = <Message_Status.Message_Done10: 265>
Message_Done11: OCP.Message.Message_Status # value = <Message_Status.Message_Done11: 266>
Message_Done12: OCP.Message.Message_Status # value = <Message_Status.Message_Done12: 267>
Message_Done13: OCP.Message.Message_Status # value = <Message_Status.Message_Done13: 268>
Message_Done14: OCP.Message.Message_Status # value = <Message_Status.Message_Done14: 269>
Message_Done15: OCP.Message.Message_Status # value = <Message_Status.Message_Done15: 270>
Message_Done16: OCP.Message.Message_Status # value = <Message_Status.Message_Done16: 271>
Message_Done17: OCP.Message.Message_Status # value = <Message_Status.Message_Done17: 272>
Message_Done18: OCP.Message.Message_Status # value = <Message_Status.Message_Done18: 273>
Message_Done19: OCP.Message.Message_Status # value = <Message_Status.Message_Done19: 274>
Message_Done2: OCP.Message.Message_Status # value = <Message_Status.Message_Done2: 257>
Message_Done20: OCP.Message.Message_Status # value = <Message_Status.Message_Done20: 275>
Message_Done21: OCP.Message.Message_Status # value = <Message_Status.Message_Done21: 276>
Message_Done22: OCP.Message.Message_Status # value = <Message_Status.Message_Done22: 277>
Message_Done23: OCP.Message.Message_Status # value = <Message_Status.Message_Done23: 278>
Message_Done24: OCP.Message.Message_Status # value = <Message_Status.Message_Done24: 279>
Message_Done25: OCP.Message.Message_Status # value = <Message_Status.Message_Done25: 280>
Message_Done26: OCP.Message.Message_Status # value = <Message_Status.Message_Done26: 281>
Message_Done27: OCP.Message.Message_Status # value = <Message_Status.Message_Done27: 282>
Message_Done28: OCP.Message.Message_Status # value = <Message_Status.Message_Done28: 283>
Message_Done29: OCP.Message.Message_Status # value = <Message_Status.Message_Done29: 284>
Message_Done3: OCP.Message.Message_Status # value = <Message_Status.Message_Done3: 258>
Message_Done30: OCP.Message.Message_Status # value = <Message_Status.Message_Done30: 285>
Message_Done31: OCP.Message.Message_Status # value = <Message_Status.Message_Done31: 286>
Message_Done32: OCP.Message.Message_Status # value = <Message_Status.Message_Done32: 287>
Message_Done4: OCP.Message.Message_Status # value = <Message_Status.Message_Done4: 259>
Message_Done5: OCP.Message.Message_Status # value = <Message_Status.Message_Done5: 260>
Message_Done6: OCP.Message.Message_Status # value = <Message_Status.Message_Done6: 261>
Message_Done7: OCP.Message.Message_Status # value = <Message_Status.Message_Done7: 262>
Message_Done8: OCP.Message.Message_Status # value = <Message_Status.Message_Done8: 263>
Message_Done9: OCP.Message.Message_Status # value = <Message_Status.Message_Done9: 264>
Message_FAIL: OCP.Message.Message_StatusType # value = <Message_StatusType.Message_FAIL: 2048>
Message_Fail: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Fail: 4>
Message_Fail1: OCP.Message.Message_Status # value = <Message_Status.Message_Fail1: 2048>
Message_Fail10: OCP.Message.Message_Status # value = <Message_Status.Message_Fail10: 2057>
Message_Fail11: OCP.Message.Message_Status # value = <Message_Status.Message_Fail11: 2058>
Message_Fail12: OCP.Message.Message_Status # value = <Message_Status.Message_Fail12: 2059>
Message_Fail13: OCP.Message.Message_Status # value = <Message_Status.Message_Fail13: 2060>
Message_Fail14: OCP.Message.Message_Status # value = <Message_Status.Message_Fail14: 2061>
Message_Fail15: OCP.Message.Message_Status # value = <Message_Status.Message_Fail15: 2062>
Message_Fail16: OCP.Message.Message_Status # value = <Message_Status.Message_Fail16: 2063>
Message_Fail17: OCP.Message.Message_Status # value = <Message_Status.Message_Fail17: 2064>
Message_Fail18: OCP.Message.Message_Status # value = <Message_Status.Message_Fail18: 2065>
Message_Fail19: OCP.Message.Message_Status # value = <Message_Status.Message_Fail19: 2066>
Message_Fail2: OCP.Message.Message_Status # value = <Message_Status.Message_Fail2: 2049>
Message_Fail20: OCP.Message.Message_Status # value = <Message_Status.Message_Fail20: 2067>
Message_Fail21: OCP.Message.Message_Status # value = <Message_Status.Message_Fail21: 2068>
Message_Fail22: OCP.Message.Message_Status # value = <Message_Status.Message_Fail22: 2069>
Message_Fail23: OCP.Message.Message_Status # value = <Message_Status.Message_Fail23: 2070>
Message_Fail24: OCP.Message.Message_Status # value = <Message_Status.Message_Fail24: 2071>
Message_Fail25: OCP.Message.Message_Status # value = <Message_Status.Message_Fail25: 2072>
Message_Fail26: OCP.Message.Message_Status # value = <Message_Status.Message_Fail26: 2073>
Message_Fail27: OCP.Message.Message_Status # value = <Message_Status.Message_Fail27: 2074>
Message_Fail28: OCP.Message.Message_Status # value = <Message_Status.Message_Fail28: 2075>
Message_Fail29: OCP.Message.Message_Status # value = <Message_Status.Message_Fail29: 2076>
Message_Fail3: OCP.Message.Message_Status # value = <Message_Status.Message_Fail3: 2050>
Message_Fail30: OCP.Message.Message_Status # value = <Message_Status.Message_Fail30: 2077>
Message_Fail31: OCP.Message.Message_Status # value = <Message_Status.Message_Fail31: 2078>
Message_Fail32: OCP.Message.Message_Status # value = <Message_Status.Message_Fail32: 2079>
Message_Fail4: OCP.Message.Message_Status # value = <Message_Status.Message_Fail4: 2051>
Message_Fail5: OCP.Message.Message_Status # value = <Message_Status.Message_Fail5: 2052>
Message_Fail6: OCP.Message.Message_Status # value = <Message_Status.Message_Fail6: 2053>
Message_Fail7: OCP.Message.Message_Status # value = <Message_Status.Message_Fail7: 2054>
Message_Fail8: OCP.Message.Message_Status # value = <Message_Status.Message_Fail8: 2055>
Message_Fail9: OCP.Message.Message_Status # value = <Message_Status.Message_Fail9: 2056>
Message_Info: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Info: 1>
Message_MetricType_MemHeapUsage: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemHeapUsage: 12>
Message_MetricType_MemPrivate: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemPrivate: 6>
Message_MetricType_MemSwapUsage: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemSwapUsage: 10>
Message_MetricType_MemSwapUsagePeak: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemSwapUsagePeak: 11>
Message_MetricType_MemVirtual: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemVirtual: 7>
Message_MetricType_MemWorkingSet: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemWorkingSet: 8>
Message_MetricType_MemWorkingSetPeak: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_MemWorkingSetPeak: 9>
Message_MetricType_None: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_None: 0>
Message_MetricType_ProcessCPUSystemTime: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_ProcessCPUSystemTime: 4>
Message_MetricType_ProcessCPUUserTime: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_ProcessCPUUserTime: 3>
Message_MetricType_ThreadCPUSystemTime: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_ThreadCPUSystemTime: 2>
Message_MetricType_ThreadCPUUserTime: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_ThreadCPUUserTime: 1>
Message_MetricType_WallClock: OCP.Message.Message_MetricType # value = <Message_MetricType.Message_MetricType_WallClock: 5>
Message_None: OCP.Message.Message_Status # value = <Message_Status.Message_None: 0>
Message_Trace: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Trace: 0>
Message_WARN: OCP.Message.Message_StatusType # value = <Message_StatusType.Message_WARN: 512>
Message_Warn1: OCP.Message.Message_Status # value = <Message_Status.Message_Warn1: 512>
Message_Warn10: OCP.Message.Message_Status # value = <Message_Status.Message_Warn10: 521>
Message_Warn11: OCP.Message.Message_Status # value = <Message_Status.Message_Warn11: 522>
Message_Warn12: OCP.Message.Message_Status # value = <Message_Status.Message_Warn12: 523>
Message_Warn13: OCP.Message.Message_Status # value = <Message_Status.Message_Warn13: 524>
Message_Warn14: OCP.Message.Message_Status # value = <Message_Status.Message_Warn14: 525>
Message_Warn15: OCP.Message.Message_Status # value = <Message_Status.Message_Warn15: 526>
Message_Warn16: OCP.Message.Message_Status # value = <Message_Status.Message_Warn16: 527>
Message_Warn17: OCP.Message.Message_Status # value = <Message_Status.Message_Warn17: 528>
Message_Warn18: OCP.Message.Message_Status # value = <Message_Status.Message_Warn18: 529>
Message_Warn19: OCP.Message.Message_Status # value = <Message_Status.Message_Warn19: 530>
Message_Warn2: OCP.Message.Message_Status # value = <Message_Status.Message_Warn2: 513>
Message_Warn20: OCP.Message.Message_Status # value = <Message_Status.Message_Warn20: 531>
Message_Warn21: OCP.Message.Message_Status # value = <Message_Status.Message_Warn21: 532>
Message_Warn22: OCP.Message.Message_Status # value = <Message_Status.Message_Warn22: 533>
Message_Warn23: OCP.Message.Message_Status # value = <Message_Status.Message_Warn23: 534>
Message_Warn24: OCP.Message.Message_Status # value = <Message_Status.Message_Warn24: 535>
Message_Warn25: OCP.Message.Message_Status # value = <Message_Status.Message_Warn25: 536>
Message_Warn26: OCP.Message.Message_Status # value = <Message_Status.Message_Warn26: 537>
Message_Warn27: OCP.Message.Message_Status # value = <Message_Status.Message_Warn27: 538>
Message_Warn28: OCP.Message.Message_Status # value = <Message_Status.Message_Warn28: 539>
Message_Warn29: OCP.Message.Message_Status # value = <Message_Status.Message_Warn29: 540>
Message_Warn3: OCP.Message.Message_Status # value = <Message_Status.Message_Warn3: 514>
Message_Warn30: OCP.Message.Message_Status # value = <Message_Status.Message_Warn30: 541>
Message_Warn31: OCP.Message.Message_Status # value = <Message_Status.Message_Warn31: 542>
Message_Warn32: OCP.Message.Message_Status # value = <Message_Status.Message_Warn32: 543>
Message_Warn4: OCP.Message.Message_Status # value = <Message_Status.Message_Warn4: 515>
Message_Warn5: OCP.Message.Message_Status # value = <Message_Status.Message_Warn5: 516>
Message_Warn6: OCP.Message.Message_Status # value = <Message_Status.Message_Warn6: 517>
Message_Warn7: OCP.Message.Message_Status # value = <Message_Status.Message_Warn7: 518>
Message_Warn8: OCP.Message.Message_Status # value = <Message_Status.Message_Warn8: 519>
Message_Warn9: OCP.Message.Message_Status # value = <Message_Status.Message_Warn9: 520>
Message_Warning: OCP.Message.Message_Gravity # value = <Message_Gravity.Message_Warning: 2>
