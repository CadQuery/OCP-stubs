import OCP.OSD
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.Standard
import OSD_MemInfo
import io
import OCP.Quantity
__all__  = [
"OSD_Chronometer",
"OSD_FileNode",
"OSD_DirectoryIterator",
"OSD_Disk",
"OSD_Environment",
"OSD_Error",
"OSD_Exception",
"OSD_Exception_ACCESS_VIOLATION",
"OSD_Exception_ARRAY_BOUNDS_EXCEEDED",
"OSD_Exception_CTRL_BREAK",
"OSD_Exception_ILLEGAL_INSTRUCTION",
"OSD_Exception_INT_OVERFLOW",
"OSD_Exception_INVALID_DISPOSITION",
"OSD_Exception_IN_PAGE_ERROR",
"OSD_Exception_NONCONTINUABLE_EXCEPTION",
"OSD_Exception_PRIV_INSTRUCTION",
"OSD_Exception_STACK_OVERFLOW",
"OSD_Exception_STATUS_NO_MEMORY",
"OSD_File",
"OSD_FileIterator",
"OSD_Directory",
"OSD_FileSystem",
"OSD_FromWhere",
"OSD_Host",
"OSD_KindFile",
"OSD_LoadMode",
"OSD_LockType",
"OSD_MAllocHook",
"OSD_MemInfo",
"OSD_OEMType",
"OSD_OSDError",
"OSD_OpenMode",
"OSD_Parallel",
"OSD_Path",
"OSD_PerfMeter",
"OSD_Process",
"OSD_Protection",
"OSD_SIGBUS",
"OSD_SIGHUP",
"OSD_SIGILL",
"OSD_SIGINT",
"OSD_SIGKILL",
"OSD_SIGQUIT",
"OSD_SIGSEGV",
"OSD_SIGSYS",
"OSD_SharedLibrary",
"OSD_Signal",
"OSD_SignalMode",
"OSD_SingleProtection",
"OSD_SysType",
"OSD_Thread",
"OSD_ThreadPool",
"OSD_Timer",
"OSD_WhoAmI",
"OSD_FileStatCTime",
"OSD_OpenFile",
"OSD_OpenFileDescriptor",
"OSD_AIX",
"OSD_Aix",
"OSD_D",
"OSD_DEC",
"OSD_DIRECTORY",
"OSD_Default",
"OSD_ExclusiveLock",
"OSD_FILE",
"OSD_FromBeginning",
"OSD_FromEnd",
"OSD_FromHere",
"OSD_HP",
"OSD_IBM",
"OSD_LIN",
"OSD_LINK",
"OSD_LinuxREDHAT",
"OSD_MAC",
"OSD_MacOs",
"OSD_NEC",
"OSD_NoLock",
"OSD_None",
"OSD_OS2",
"OSD_OSF",
"OSD_PC",
"OSD_R",
"OSD_RD",
"OSD_RTLD_LAZY",
"OSD_RTLD_NOW",
"OSD_RW",
"OSD_RWD",
"OSD_RWX",
"OSD_RWXD",
"OSD_RX",
"OSD_RXD",
"OSD_ReadLock",
"OSD_ReadOnly",
"OSD_ReadWrite",
"OSD_SGI",
"OSD_SOCKET",
"OSD_SUN",
"OSD_SignalMode_AsIs",
"OSD_SignalMode_Set",
"OSD_SignalMode_SetUnhandled",
"OSD_SignalMode_Unset",
"OSD_Taligent",
"OSD_UNKNOWN",
"OSD_Unavailable",
"OSD_UnixBSD",
"OSD_UnixSystemV",
"OSD_Unknown",
"OSD_VAX",
"OSD_VMS",
"OSD_W",
"OSD_WChronometer",
"OSD_WD",
"OSD_WDirectory",
"OSD_WDirectoryIterator",
"OSD_WDisk",
"OSD_WEnvironment",
"OSD_WEnvironmentIterator",
"OSD_WFile",
"OSD_WFileIterator",
"OSD_WFileNode",
"OSD_WHost",
"OSD_WPackage",
"OSD_WPath",
"OSD_WProcess",
"OSD_WProtection",
"OSD_WTimer",
"OSD_WX",
"OSD_WXD",
"OSD_WindowsNT",
"OSD_WriteLock",
"OSD_WriteOnly",
"OSD_X",
"OSD_XD"
]
class OSD_Chronometer():
    """
    This class measures CPU time (both user and system) consumed by current process or thread. The chronometer can be started and stopped multiple times, and measures cumulative time.
    """
    @staticmethod
    def GetProcessCPU_s() -> Tuple[float, float]: 
        """
        Returns CPU time (user and system) consumed by the current process since its start, in seconds. The actual precision of the measurement depends on granularity provided by the system, and is platform-specific.
        """
    @staticmethod
    def GetThreadCPU_s() -> Tuple[float, float]: 
        """
        Returns CPU time (user and system) consumed by the current thread since its start. Note that this measurement is platform-specific, as threads are implemented and managed differently on different platforms and CPUs.
        """
    def IsStarted(self) -> bool: 
        """
        Return true if timer has been started.
        """
    def IsThisThreadOnly(self) -> bool: 
        """
        Return TRUE if current thread CPU time should be measured, and FALSE to measure all threads CPU time; FALSE by default,
        """
    def Reset(self) -> None: 
        """
        Stops and Reinitializes the Chronometer.
        """
    def Restart(self) -> None: 
        """
        Restarts the Chronometer.
        """
    def SetThisThreadOnly(self,theIsThreadOnly : bool) -> None: 
        """
        Set if current thread (TRUE) or all threads (FALSE) CPU time should be measured. Will raise exception if Timer is in started state.
        """
    @overload
    def Show(self) -> Tuple[float]: 
        """
        Shows the current CPU user and system time on the standard output stream <cout>. The chronometer can be running (laps Time) or stopped.

        Shows the current CPU user and system time on the output stream <os>. The chronometer can be running (laps Time) or stopped.

        Returns the current CPU user time in a variable. The chronometer can be running (laps Time) or stopped.

        Returns the current CPU user and system time in variables. The chronometer can be running (laps Time) or stopped.
        """
    @overload
    def Show(self) -> Tuple[float, float]: ...
    @overload
    def Show(self,theOStream : io.BytesIO) -> None: ...
    @overload
    def Show(self) -> None: ...
    def Start(self) -> None: ...
    def Stop(self) -> None: 
        """
        Stops the Chronometer.
        """
    def SystemTimeCPU(self) -> float: 
        """
        Returns the current CPU system time in seconds. The chronometer can be running (laps Time) or stopped.
        """
    def UserTimeCPU(self) -> float: 
        """
        Returns the current CPU user time in seconds. The chronometer can be running (laps Time) or stopped.
        """
    def __init__(self,theThisThreadOnly : bool=False) -> None: ...
    pass
class OSD_FileNode():
    """
    A class for 'File' and 'Directory' grouping common methods (file/directory manipulation tools). The "file oriented" name means files or directories which are in fact hard coded as files.
    """
    def AccessMoment(self) -> OCP.Quantity.Quantity_Date: 
        """
        Returns last write access. On UNIX, AccessMoment and CreationMoment return the same value.
        """
    def Copy(self,ToPath : OSD_Path) -> None: 
        """
        Copies <me> to another FileNode
        """
    def CreationMoment(self) -> OCP.Quantity.Quantity_Date: 
        """
        Returns creation date. On UNIX, AccessMoment and CreationMoment return the same value.
        """
    def Error(self) -> int: 
        """
        Returns error number if 'Failed' is TRUE.
        """
    def Exists(self) -> bool: 
        """
        Returns TRUE if <me> exists.
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs
        """
    def Move(self,NewPath : OSD_Path) -> None: 
        """
        Moves <me> into another directory
        """
    def Path(self,Name : OSD_Path) -> None: 
        """
        Gets file name and path.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error
        """
    def Protection(self) -> OSD_Protection: 
        """
        Returns access mode of <me>.
        """
    def Remove(self) -> None: 
        """
        Erases the FileNode from directory
        """
    def Reset(self) -> None: 
        """
        Resets error counter to zero
        """
    def SetPath(self,Name : OSD_Path) -> None: 
        """
        Sets file name and path. If a name is not found, it raises a program error.
        """
    def SetProtection(self,Prot : OSD_Protection) -> None: 
        """
        Changes protection of the FileNode
        """
    pass
class OSD_DirectoryIterator():
    """
    Manages a breadth-only search for sub-directories in the specified Path. There is no specific order of results.
    """
    def Destroy(self) -> None: 
        """
        None
        """
    def Error(self) -> int: 
        """
        Returns error number if 'Failed' is TRUE.
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs
        """
    def Initialize(self,where : OSD_Path,Mask : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Initializes the current File Directory
        """
    def More(self) -> bool: 
        """
        Returns TRUE if other items are found while using the 'Tree' method.
        """
    def Next(self) -> None: 
        """
        Sets the iterator to the next item. Returns the item value corresponding to the current position of the iterator.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error
        """
    def Reset(self) -> None: 
        """
        Resets error counter to zero
        """
    def Values(self) -> OSD_Directory: 
        """
        Returns the next item found .
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,where : OSD_Path,Mask : OCP.TCollection.TCollection_AsciiString) -> None: ...
    pass
class OSD_Disk():
    """
    Disk management (a set of disk oriented tools)
    """
    def DiskFree(self) -> int: 
        """
        Returns free available 512 bytes blocks on disk.
        """
    def DiskSize(self) -> int: 
        """
        Returns total disk capacity in 512 bytes blocks.
        """
    def Error(self) -> int: 
        """
        Returns error number if 'Failed' is TRUE.
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs
        """
    def Name(self) -> OSD_Path: 
        """
        Returns disk name of <me>.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error
        """
    def Reset(self) -> None: 
        """
        Resets error counter to zero
        """
    def SetName(self,Name : OSD_Path) -> None: 
        """
        Instantiates <me> with <Name>.
        """
    @overload
    def __init__(self,Name : OSD_Path) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,PathName : str) -> None: ...
    pass
class OSD_Environment():
    """
    Management of system environment variables An environment variable is composed of a variable name and its value.
    """
    def Build(self) -> None: 
        """
        Sets the value of an environment variable into system (physically).
        """
    def Error(self) -> int: 
        """
        Returns error number if 'Failed' is TRUE.
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets the name of <me>.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error
        """
    def Remove(self) -> None: ...
    def Reset(self) -> None: 
        """
        Resets error counter to zero
        """
    def SetName(self,name : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Changes environment variable name. Raises ConstructionError either if the string contains characters not in range of ' '...'~' or if the string contains the character '$' which is forbidden.
        """
    def SetValue(self,Value : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Changes environment variable value. Raises ConstructionError either if the string contains characters not in range of ' '...'~' or if the string contains the character '$' which is forbidden.
        """
    def Value(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets the value of an environment variable
        """
    @overload
    def __init__(self,Name : OCP.TCollection.TCollection_AsciiString,Value : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,Name : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class OSD_Error():
    """
    Accurate management of OSD specific errors.
    """
    def Error(self) -> int: 
        """
        Returns an accurate error code. To test these values, you must include "OSD_ErrorList.hxx"
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs This is a way to test if a system call succeeded or not.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error with accurate error message.
        """
    def Reset(self) -> None: 
        """
        Resets error counter to zero This allows the user to ignore an error (WARNING).
        """
    def SetValue(self,Errcode : int,From : int,Message : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Instantiates error This is only used by OSD methods to instantiates an error code. No description is done for the programmer.
        """
    def __init__(self) -> None: ...
    pass
class OSD_Exception(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_ACCESS_VIOLATION(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_ACCESS_VIOLATION' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_ACCESS_VIOLATION' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_ARRAY_BOUNDS_EXCEEDED(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_ARRAY_BOUNDS_EXCEEDED' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_ARRAY_BOUNDS_EXCEEDED' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_CTRL_BREAK(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_CTRL_BREAK' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_CTRL_BREAK' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_ILLEGAL_INSTRUCTION(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_ILLEGAL_INSTRUCTION' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_ILLEGAL_INSTRUCTION' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_INT_OVERFLOW(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_INT_OVERFLOW' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_INT_OVERFLOW' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_INVALID_DISPOSITION(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_INVALID_DISPOSITION' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_INVALID_DISPOSITION' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_IN_PAGE_ERROR(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_IN_PAGE_ERROR' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_IN_PAGE_ERROR' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_NONCONTINUABLE_EXCEPTION(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_NONCONTINUABLE_EXCEPTION' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_NONCONTINUABLE_EXCEPTION' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_PRIV_INSTRUCTION(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_PRIV_INSTRUCTION' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_PRIV_INSTRUCTION' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_STACK_OVERFLOW(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_STACK_OVERFLOW' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_STACK_OVERFLOW' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_Exception_STATUS_NO_MEMORY(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Exception_STATUS_NO_MEMORY' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Exception_STATUS_NO_MEMORY' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_File(OSD_FileNode):
    """
    Basic tools to manage files Warning: 'ProgramError' is raised when somebody wants to use the methods Read, Write, Seek, Close when File is not open.
    """
    def AccessMoment(self) -> OCP.Quantity.Quantity_Date: 
        """
        Returns last write access. On UNIX, AccessMoment and CreationMoment return the same value.
        """
    def Append(self,Mode : OSD_OpenMode,Protect : OSD_Protection) -> None: 
        """
        Appends data to an existing file. If file doesn't exist, creates it first. After 'Append', the file is open. If no name was given, ProgramError is raised.
        """
    def Build(self,Mode : OSD_OpenMode,Protect : OSD_Protection) -> None: 
        """
        CREATES a file if it doesn't already exists or empties an existing file. After 'Build', the file is open. If no name was given, ProgramError is raised.
        """
    def BuildTemporary(self) -> None: 
        """
        Makes a temporary File This temporary file is already open !
        """
    def Close(self) -> None: 
        """
        Closes the file (and deletes a descriptor)
        """
    def Copy(self,ToPath : OSD_Path) -> None: 
        """
        Copies <me> to another FileNode
        """
    def CreationMoment(self) -> OCP.Quantity.Quantity_Date: 
        """
        Returns creation date. On UNIX, AccessMoment and CreationMoment return the same value.
        """
    def Edit(self) -> bool: 
        """
        find an editor on the system and edit the given file
        """
    def Error(self) -> int: 
        """
        Returns error number if 'Failed' is TRUE.
        """
    def Exists(self) -> bool: 
        """
        Returns TRUE if <me> exists.
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs
        """
    def GetLock(self) -> OSD_LockType: 
        """
        Returns the current lock state
        """
    def IsAtEnd(self) -> bool: 
        """
        Returns TRUE if the seek pointer is at end of file.
        """
    def IsExecutable(self) -> bool: 
        """
        returns TRUE if the file can be executed.
        """
    def IsLocked(self) -> bool: 
        """
        Returns TRUE if this file is locked.
        """
    def IsOpen(self) -> bool: 
        """
        Returns TRUE if <me> is open.
        """
    def IsReadable(self) -> bool: 
        """
        returns TRUE if the file exists and if the user has the authorization to read it.
        """
    def IsWriteable(self) -> bool: 
        """
        returns TRUE if the file can be read and overwritten.
        """
    def KindOfFile(self) -> OSD_KindFile: 
        """
        Returns the kind of file. A file can be a file, a directory or a link.
        """
    def Move(self,NewPath : OSD_Path) -> None: 
        """
        Moves <me> into another directory
        """
    def Open(self,Mode : OSD_OpenMode,Protect : OSD_Protection) -> None: 
        """
        Opens a File with specific attributes This works only on already existing file. If no name was given, ProgramError is raised.
        """
    def Path(self,Name : OSD_Path) -> None: 
        """
        Gets file name and path.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error
        """
    def Protection(self) -> OSD_Protection: 
        """
        Returns access mode of <me>.
        """
    @overload
    def Read(self,Buffer : OCP.TCollection.TCollection_AsciiString,Nbyte : int) -> None: 
        """
        Attempts to read Nbyte bytes from the file associated with the object file. Upon successful completion, Read returns the number of bytes actually read and placed in the Buffer. This number may be less than Nbyte if the number of bytes left in the file is less than Nbyte bytes. In this case only number of read bytes will be placed in the buffer.

        Attempts to read Nbyte bytes from the files associated with the object File. Upon successful completion, Read returns the number of bytes actually read and placed in the Buffer. This number may be less than Nbyte if the number of bytes left in the file is less than Nbyte bytes. For this reason the output parameter Readbyte will contain the number of read bytes.
        """
    @overload
    def Read(self,Buffer : capsule,Nbyte : int) -> Tuple[int]: ...
    def ReadLastLine(self,aLine : OCP.TCollection.TCollection_AsciiString,aDelay : int,aNbTries : int) -> bool: 
        """
        Enables to emulate unix "tail -f" command. If a line is available in the file <me> returns it. Otherwise attempts to read again aNbTries times in the file waiting aDelay seconds between each read. If meanwhile the file increases returns the next line, otherwise returns FALSE.
        """
    @overload
    def ReadLine(self,Buffer : OCP.TCollection.TCollection_AsciiString,NByte : int) -> int: 
        """
        Reads bytes from the data pointed to by the object file into the buffer <Buffer>. Data is read until <NByte-1> bytes have been read, until a newline character is read and transferred into <Buffer>, or until an EOF (End-of-File) condition is encountered. Upon successful completion, Read returns the number of bytes actually read and placed into the Buffer <Buffer>.

        Reads bytes from the data pointed to by the object file into the buffer <Buffer>. Data is read until <NByte-1> bytes have been read, until a newline character is read and transferred into <Buffer>, or until an EOF (End-of-File) condition is encountered. Upon successful completion, Read returns the number of bytes actually read into <NByteRead> and placed into the Buffer <Buffer>.
        """
    @overload
    def ReadLine(self,Buffer : OCP.TCollection.TCollection_AsciiString,NByte : int) -> Tuple[int]: ...
    def Remove(self) -> None: 
        """
        Erases the FileNode from directory
        """
    def Reset(self) -> None: 
        """
        Resets error counter to zero
        """
    def Rewind(self) -> None: 
        """
        Set file pointer position to the beginning of the file
        """
    def Seek(self,Offset : int,Whence : OSD_FromWhere) -> None: 
        """
        Sets the seek pointer associated with the open file
        """
    def SetLock(self,Lock : OSD_LockType) -> None: 
        """
        Locks current file
        """
    def SetPath(self,Name : OSD_Path) -> None: 
        """
        Sets file name and path. If a name is not found, it raises a program error.
        """
    def SetProtection(self,Prot : OSD_Protection) -> None: 
        """
        Changes protection of the FileNode
        """
    def Size(self) -> int: 
        """
        Returns actual number of bytes of <me>.
        """
    def UnLock(self) -> None: 
        """
        Unlocks current file
        """
    @overload
    def Write(self,theBuffer : OCP.TCollection.TCollection_AsciiString,theNbBytes : int) -> None: 
        """
        Attempts to write theNbBytes bytes from the AsciiString to the file.

        Attempts to write theNbBytes bytes from the buffer pointed to by theBuffer to the file associated to the object File.
        """
    @overload
    def Write(self,theBuffer : capsule,theNbBytes : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Name : OSD_Path) -> None: ...
    pass
class OSD_FileIterator():
    """
    Manages a breadth-only search for files in the specified Path. There is no specific order of results.
    """
    def Destroy(self) -> None: 
        """
        None
        """
    def Error(self) -> int: 
        """
        Returns error number if 'Failed' is TRUE.
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs
        """
    def Initialize(self,where : OSD_Path,Mask : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Initializes the current File Iterator
        """
    def More(self) -> bool: 
        """
        Returns TRUE if there are other items using the 'Tree' method.
        """
    def Next(self) -> None: 
        """
        Sets the iterator to the next item. Returns the item value corresponding to the current position of the iterator.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error
        """
    def Reset(self) -> None: 
        """
        Resets error counter to zero
        """
    def Values(self) -> OSD_File: 
        """
        Returns the next file found .
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,where : OSD_Path,Mask : OCP.TCollection.TCollection_AsciiString) -> None: ...
    pass
class OSD_Directory(OSD_FileNode):
    """
    Management of directories (a set of directory oriented tools)
    """
    def AccessMoment(self) -> OCP.Quantity.Quantity_Date: 
        """
        Returns last write access. On UNIX, AccessMoment and CreationMoment return the same value.
        """
    def Build(self,Protect : OSD_Protection) -> None: ...
    @staticmethod
    def BuildTemporary_s() -> OSD_Directory: 
        """
        Creates a temporary Directory in current directory. This directory is automatically removed when object dies.
        """
    def Copy(self,ToPath : OSD_Path) -> None: 
        """
        Copies <me> to another FileNode
        """
    def CreationMoment(self) -> OCP.Quantity.Quantity_Date: 
        """
        Returns creation date. On UNIX, AccessMoment and CreationMoment return the same value.
        """
    def Error(self) -> int: 
        """
        Returns error number if 'Failed' is TRUE.
        """
    def Exists(self) -> bool: 
        """
        Returns TRUE if <me> exists.
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs
        """
    def Move(self,NewPath : OSD_Path) -> None: 
        """
        Moves <me> into another directory
        """
    def Path(self,Name : OSD_Path) -> None: 
        """
        Gets file name and path.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error
        """
    def Protection(self) -> OSD_Protection: 
        """
        Returns access mode of <me>.
        """
    def Remove(self) -> None: 
        """
        Erases the FileNode from directory
        """
    def Reset(self) -> None: 
        """
        Resets error counter to zero
        """
    def SetPath(self,Name : OSD_Path) -> None: 
        """
        Sets file name and path. If a name is not found, it raises a program error.
        """
    def SetProtection(self,Prot : OSD_Protection) -> None: 
        """
        Changes protection of the FileNode
        """
    @overload
    def __init__(self,theName : OSD_Path) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class OSD_FileSystem():
    pass
class OSD_FromWhere():
    """
    Used by OSD_File in the method Seek.

    Members:

      OSD_FromBeginning

      OSD_FromHere

      OSD_FromEnd
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
    OSD_FromBeginning: OCP.OSD.OSD_FromWhere # value = <OSD_FromWhere.OSD_FromBeginning: 0>
    OSD_FromEnd: OCP.OSD.OSD_FromWhere # value = <OSD_FromWhere.OSD_FromEnd: 2>
    OSD_FromHere: OCP.OSD.OSD_FromWhere # value = <OSD_FromWhere.OSD_FromHere: 1>
    __entries: dict # value = {'OSD_FromBeginning': (<OSD_FromWhere.OSD_FromBeginning: 0>, None), 'OSD_FromHere': (<OSD_FromWhere.OSD_FromHere: 1>, None), 'OSD_FromEnd': (<OSD_FromWhere.OSD_FromEnd: 2>, None)}
    __members__: dict # value = {'OSD_FromBeginning': <OSD_FromWhere.OSD_FromBeginning: 0>, 'OSD_FromHere': <OSD_FromWhere.OSD_FromHere: 1>, 'OSD_FromEnd': <OSD_FromWhere.OSD_FromEnd: 2>}
    pass
class OSD_Host():
    """
    Carries information about a Host System version ,host name, nodename ...
    """
    def AvailableMemory(self) -> int: 
        """
        Returns available memory in Kilobytes.
        """
    def Error(self) -> int: 
        """
        Returns error number if 'Failed' is TRUE.
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs
        """
    def HostName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns host name.
        """
    def InternetAddress(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Internet address of current host.
        """
    def MachineType(self) -> OSD_OEMType: 
        """
        Returns type of current machine.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error
        """
    def Reset(self) -> None: 
        """
        Resets error counter to zero
        """
    def SystemId(self) -> OSD_SysType: 
        """
        Returns the system type (UNIX System V, UNIX BSD, MS-DOS...)
        """
    def SystemVersion(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns system name and version
        """
    def __init__(self) -> None: ...
    pass
class OSD_KindFile():
    """
    Specifies the type of files.

    Members:

      OSD_FILE

      OSD_DIRECTORY

      OSD_LINK

      OSD_SOCKET

      OSD_UNKNOWN
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
    OSD_DIRECTORY: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_DIRECTORY: 1>
    OSD_FILE: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_FILE: 0>
    OSD_LINK: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_LINK: 2>
    OSD_SOCKET: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_SOCKET: 3>
    OSD_UNKNOWN: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_UNKNOWN: 4>
    __entries: dict # value = {'OSD_FILE': (<OSD_KindFile.OSD_FILE: 0>, None), 'OSD_DIRECTORY': (<OSD_KindFile.OSD_DIRECTORY: 1>, None), 'OSD_LINK': (<OSD_KindFile.OSD_LINK: 2>, None), 'OSD_SOCKET': (<OSD_KindFile.OSD_SOCKET: 3>, None), 'OSD_UNKNOWN': (<OSD_KindFile.OSD_UNKNOWN: 4>, None)}
    __members__: dict # value = {'OSD_FILE': <OSD_KindFile.OSD_FILE: 0>, 'OSD_DIRECTORY': <OSD_KindFile.OSD_DIRECTORY: 1>, 'OSD_LINK': <OSD_KindFile.OSD_LINK: 2>, 'OSD_SOCKET': <OSD_KindFile.OSD_SOCKET: 3>, 'OSD_UNKNOWN': <OSD_KindFile.OSD_UNKNOWN: 4>}
    pass
class OSD_LoadMode():
    """
    This enumeration is used to load shareable libraries.

    Members:

      OSD_RTLD_LAZY

      OSD_RTLD_NOW
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
    OSD_RTLD_LAZY: OCP.OSD.OSD_LoadMode # value = <OSD_LoadMode.OSD_RTLD_LAZY: 0>
    OSD_RTLD_NOW: OCP.OSD.OSD_LoadMode # value = <OSD_LoadMode.OSD_RTLD_NOW: 1>
    __entries: dict # value = {'OSD_RTLD_LAZY': (<OSD_LoadMode.OSD_RTLD_LAZY: 0>, None), 'OSD_RTLD_NOW': (<OSD_LoadMode.OSD_RTLD_NOW: 1>, None)}
    __members__: dict # value = {'OSD_RTLD_LAZY': <OSD_LoadMode.OSD_RTLD_LAZY: 0>, 'OSD_RTLD_NOW': <OSD_LoadMode.OSD_RTLD_NOW: 1>}
    pass
class OSD_LockType():
    """
    locks for files. NoLock is the default value when opening a file.

    Members:

      OSD_NoLock

      OSD_ReadLock

      OSD_WriteLock

      OSD_ExclusiveLock
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
    OSD_ExclusiveLock: OCP.OSD.OSD_LockType # value = <OSD_LockType.OSD_ExclusiveLock: 3>
    OSD_NoLock: OCP.OSD.OSD_LockType # value = <OSD_LockType.OSD_NoLock: 0>
    OSD_ReadLock: OCP.OSD.OSD_LockType # value = <OSD_LockType.OSD_ReadLock: 1>
    OSD_WriteLock: OCP.OSD.OSD_LockType # value = <OSD_LockType.OSD_WriteLock: 2>
    __entries: dict # value = {'OSD_NoLock': (<OSD_LockType.OSD_NoLock: 0>, None), 'OSD_ReadLock': (<OSD_LockType.OSD_ReadLock: 1>, None), 'OSD_WriteLock': (<OSD_LockType.OSD_WriteLock: 2>, None), 'OSD_ExclusiveLock': (<OSD_LockType.OSD_ExclusiveLock: 3>, None)}
    __members__: dict # value = {'OSD_NoLock': <OSD_LockType.OSD_NoLock: 0>, 'OSD_ReadLock': <OSD_LockType.OSD_ReadLock: 1>, 'OSD_WriteLock': <OSD_LockType.OSD_WriteLock: 2>, 'OSD_ExclusiveLock': <OSD_LockType.OSD_ExclusiveLock: 3>}
    pass
class OSD_MAllocHook():
    """
    This class provides the possibility to set callback for memory allocation/deallocation. On MS Windows, it works only in Debug builds. It relies on the debug CRT function _CrtSetAllocHook (see MSDN for help).
    """
    @staticmethod
    def GetCallback_s() -> Any: 
        """
        Get current handler of allocation/deallocation events
        """
    @staticmethod
    def GetCollectBySize_s() -> Any: 
        """
        Get static instance of CollectBySize handler
        """
    @staticmethod
    def GetLogFileHandler_s() -> Any: 
        """
        Get static instance of LogFileHandler handler
        """
    @staticmethod
    def SetCallback_s(theCB : Any) -> None: 
        """
        Set handler of allocation/deallocation events
        """
    def __init__(self) -> None: ...
    pass
class OSD_MemInfo():
    """
    This class provide information about memory utilized by current process. This information includes: - Private Memory - synthetic value that tries to filter out the memory usage only by the process itself (allocated for data and stack), excluding dynamic libraries. These pages may be in RAM or in SWAP. - Virtual Memory - amount of reserved and committed memory in the user-mode portion of the virtual address space. Notice that this counter includes reserved memory (not yet in used) and shared between processes memory (libraries). - Working Set - set of memory pages in the virtual address space of the process that are currently resident in physical memory (RAM). These pages are available for an application to use without triggering a page fault. - Pagefile Usage - space allocated for the pagefile, in bytes. Those pages may or may not be in memory (RAM) thus this counter couldn't be used to estimate how many active pages doesn't present in RAM.
    """
    class Counter_e():
        """
        None

        Members:

          MemPrivate

          MemVirtual

          MemWorkingSet

          MemWorkingSetPeak

          MemSwapUsage

          MemSwapUsagePeak

          MemHeapUsage

          MemCounter_NB
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
        MemCounter_NB: OCP.OSD.Counter_e # value = <Counter_e.MemCounter_NB: 7>
        MemHeapUsage: OCP.OSD.Counter_e # value = <Counter_e.MemHeapUsage: 6>
        MemPrivate: OCP.OSD.Counter_e # value = <Counter_e.MemPrivate: 0>
        MemSwapUsage: OCP.OSD.Counter_e # value = <Counter_e.MemSwapUsage: 4>
        MemSwapUsagePeak: OCP.OSD.Counter_e # value = <Counter_e.MemSwapUsagePeak: 5>
        MemVirtual: OCP.OSD.Counter_e # value = <Counter_e.MemVirtual: 1>
        MemWorkingSet: OCP.OSD.Counter_e # value = <Counter_e.MemWorkingSet: 2>
        MemWorkingSetPeak: OCP.OSD.Counter_e # value = <Counter_e.MemWorkingSetPeak: 3>
        __entries: dict # value = {'MemPrivate': (<Counter_e.MemPrivate: 0>, None), 'MemVirtual': (<Counter_e.MemVirtual: 1>, None), 'MemWorkingSet': (<Counter_e.MemWorkingSet: 2>, None), 'MemWorkingSetPeak': (<Counter_e.MemWorkingSetPeak: 3>, None), 'MemSwapUsage': (<Counter_e.MemSwapUsage: 4>, None), 'MemSwapUsagePeak': (<Counter_e.MemSwapUsagePeak: 5>, None), 'MemHeapUsage': (<Counter_e.MemHeapUsage: 6>, None), 'MemCounter_NB': (<Counter_e.MemCounter_NB: 7>, None)}
        __members__: dict # value = {'MemPrivate': <Counter_e.MemPrivate: 0>, 'MemVirtual': <Counter_e.MemVirtual: 1>, 'MemWorkingSet': <Counter_e.MemWorkingSet: 2>, 'MemWorkingSetPeak': <Counter_e.MemWorkingSetPeak: 3>, 'MemSwapUsage': <Counter_e.MemSwapUsage: 4>, 'MemSwapUsagePeak': <Counter_e.MemSwapUsagePeak: 5>, 'MemHeapUsage': <Counter_e.MemHeapUsage: 6>, 'MemCounter_NB': <Counter_e.MemCounter_NB: 7>}
        pass
    def Clear(self) -> None: 
        """
        Clear counters
        """
    def IsActive(self,theCounter : OSD_MemInfo.Counter_e) -> bool: 
        """
        Return true if the counter is active
        """
    @staticmethod
    def PrintInfo_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return the string representation for all available counter.
        """
    @overload
    def SetActive(self,theCounter : OSD_MemInfo.Counter_e,theActive : bool) -> None: 
        """
        Set all counters active. The information is collected for active counters.

        Set the counter active. The information is collected for active counters.
        """
    @overload
    def SetActive(self,theActive : bool) -> None: ...
    def ToString(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return the string representation for all available counter.
        """
    def Update(self) -> None: 
        """
        Update counters
        """
    def Value(self,theCounter : OSD_MemInfo.Counter_e) -> int: 
        """
        Return value of specified counter in bytes. Notice that NOT all counters are available on various systems. Standard_Size(-1) means invalid (unavailable) value.
        """
    def ValueMiB(self,theCounter : OSD_MemInfo.Counter_e) -> int: 
        """
        Return value of specified counter in MiB. Notice that NOT all counters are available on various systems. Standard_Size(-1) means invalid (unavailable) value.
        """
    def ValuePreciseMiB(self,theCounter : OSD_MemInfo.Counter_e) -> float: 
        """
        Return floating value of specified counter in MiB. Notice that NOT all counters are available on various systems. Standard_Real(-1) means invalid (unavailable) value.
        """
    def __init__(self,theImmediateUpdate : bool=True) -> None: ...
    MemCounter_NB: OCP.OSD.Counter_e # value = <Counter_e.MemCounter_NB: 7>
    MemHeapUsage: OCP.OSD.Counter_e # value = <Counter_e.MemHeapUsage: 6>
    MemPrivate: OCP.OSD.Counter_e # value = <Counter_e.MemPrivate: 0>
    MemSwapUsage: OCP.OSD.Counter_e # value = <Counter_e.MemSwapUsage: 4>
    MemSwapUsagePeak: OCP.OSD.Counter_e # value = <Counter_e.MemSwapUsagePeak: 5>
    MemVirtual: OCP.OSD.Counter_e # value = <Counter_e.MemVirtual: 1>
    MemWorkingSet: OCP.OSD.Counter_e # value = <Counter_e.MemWorkingSet: 2>
    MemWorkingSetPeak: OCP.OSD.Counter_e # value = <Counter_e.MemWorkingSetPeak: 3>
    pass
class OSD_OEMType():
    """
    This is set of possible machine types used in OSD_Host::MachineType

    Members:

      OSD_Unavailable

      OSD_SUN

      OSD_DEC

      OSD_SGI

      OSD_NEC

      OSD_MAC

      OSD_PC

      OSD_HP

      OSD_IBM

      OSD_VAX

      OSD_LIN

      OSD_AIX
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
    OSD_AIX: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_AIX: 11>
    OSD_DEC: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_DEC: 2>
    OSD_HP: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_HP: 7>
    OSD_IBM: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_IBM: 8>
    OSD_LIN: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_LIN: 10>
    OSD_MAC: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_MAC: 5>
    OSD_NEC: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_NEC: 4>
    OSD_PC: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_PC: 6>
    OSD_SGI: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_SGI: 3>
    OSD_SUN: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_SUN: 1>
    OSD_Unavailable: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_Unavailable: 0>
    OSD_VAX: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_VAX: 9>
    __entries: dict # value = {'OSD_Unavailable': (<OSD_OEMType.OSD_Unavailable: 0>, None), 'OSD_SUN': (<OSD_OEMType.OSD_SUN: 1>, None), 'OSD_DEC': (<OSD_OEMType.OSD_DEC: 2>, None), 'OSD_SGI': (<OSD_OEMType.OSD_SGI: 3>, None), 'OSD_NEC': (<OSD_OEMType.OSD_NEC: 4>, None), 'OSD_MAC': (<OSD_OEMType.OSD_MAC: 5>, None), 'OSD_PC': (<OSD_OEMType.OSD_PC: 6>, None), 'OSD_HP': (<OSD_OEMType.OSD_HP: 7>, None), 'OSD_IBM': (<OSD_OEMType.OSD_IBM: 8>, None), 'OSD_VAX': (<OSD_OEMType.OSD_VAX: 9>, None), 'OSD_LIN': (<OSD_OEMType.OSD_LIN: 10>, None), 'OSD_AIX': (<OSD_OEMType.OSD_AIX: 11>, None)}
    __members__: dict # value = {'OSD_Unavailable': <OSD_OEMType.OSD_Unavailable: 0>, 'OSD_SUN': <OSD_OEMType.OSD_SUN: 1>, 'OSD_DEC': <OSD_OEMType.OSD_DEC: 2>, 'OSD_SGI': <OSD_OEMType.OSD_SGI: 3>, 'OSD_NEC': <OSD_OEMType.OSD_NEC: 4>, 'OSD_MAC': <OSD_OEMType.OSD_MAC: 5>, 'OSD_PC': <OSD_OEMType.OSD_PC: 6>, 'OSD_HP': <OSD_OEMType.OSD_HP: 7>, 'OSD_IBM': <OSD_OEMType.OSD_IBM: 8>, 'OSD_VAX': <OSD_OEMType.OSD_VAX: 9>, 'OSD_LIN': <OSD_OEMType.OSD_LIN: 10>, 'OSD_AIX': <OSD_OEMType.OSD_AIX: 11>}
    pass
class OSD_OSDError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_OSDError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_OSDError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_OpenMode():
    """
    Specifies the file open mode.

    Members:

      OSD_ReadOnly

      OSD_WriteOnly

      OSD_ReadWrite
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
    OSD_ReadOnly: OCP.OSD.OSD_OpenMode # value = <OSD_OpenMode.OSD_ReadOnly: 0>
    OSD_ReadWrite: OCP.OSD.OSD_OpenMode # value = <OSD_OpenMode.OSD_ReadWrite: 2>
    OSD_WriteOnly: OCP.OSD.OSD_OpenMode # value = <OSD_OpenMode.OSD_WriteOnly: 1>
    __entries: dict # value = {'OSD_ReadOnly': (<OSD_OpenMode.OSD_ReadOnly: 0>, None), 'OSD_WriteOnly': (<OSD_OpenMode.OSD_WriteOnly: 1>, None), 'OSD_ReadWrite': (<OSD_OpenMode.OSD_ReadWrite: 2>, None)}
    __members__: dict # value = {'OSD_ReadOnly': <OSD_OpenMode.OSD_ReadOnly: 0>, 'OSD_WriteOnly': <OSD_OpenMode.OSD_WriteOnly: 1>, 'OSD_ReadWrite': <OSD_OpenMode.OSD_ReadWrite: 2>}
    pass
class OSD_Parallel():
    """
    Simple tool for code parallelization.
    """
    @staticmethod
    def NbLogicalProcessors_s() -> int: 
        """
        Returns number of logical processors.
        """
    @staticmethod
    def SetUseOcctThreads_s(theToUseOcct : bool) -> None: 
        """
        Sets if OCCT threads should be used instead of auxiliary threads library. Has no effect if OCCT has been built with no auxiliary threads library.
        """
    @staticmethod
    def ToUseOcctThreads_s() -> bool: 
        """
        Returns TRUE if OCCT threads should be used instead of auxiliary threads library; default value is FALSE if alternative library has been enabled while OCCT building and TRUE otherwise.
        """
    def __init__(self) -> None: ...
    pass
class OSD_Path():
    """
    None
    """
    @staticmethod
    def AbsolutePath_s(DirPath : OCP.TCollection.TCollection_AsciiString,RelFilePath : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the absolute file path from the absolute directory path <DirPath> and the relative file path returned by RelativePath(). If the RelFilePath is an absolute path, it is returned and the directory path is ignored. If handling fails, an empty string is returned.
        """
    def Disk(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Disk of <me>.
        """
    def DownTrek(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        This appends a directory name into the Trek. ex: me = "|usr|todo.sh" me.DownTrek("bin") gives me = "|usr|bin|todo.sh".
        """
    def ExpandedName(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Returns system dependent path resolving logical symbols.
        """
    def Extension(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns my extension name. This returns an empty string if path contains no file name.
        """
    @staticmethod
    def FileNameAndExtension_s(theFilePath : OCP.TCollection.TCollection_AsciiString,theName : OCP.TCollection.TCollection_AsciiString,theExtension : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Return file extension from the name in lower case. Extension is expected to be within 20-symbols length, and determined as file name tail after last dot. Example: IN theFilePath ='Image.sbs.JPG' OUT theName ='Image.sbs' OUT theFileName ='jpg'
        """
    @staticmethod
    def FolderAndFileFromPath_s(theFilePath : OCP.TCollection.TCollection_AsciiString,theFolder : OCP.TCollection.TCollection_AsciiString,theFileName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Split absolute filepath into folder path and file name. Example: IN theFilePath ='/media/cdrom/image.jpg' OUT theFolder ='/media/cdrom/' OUT theFileName ='image.jpg'
        """
    def InsertATrek(self,aName : OCP.TCollection.TCollection_AsciiString,where : int) -> None: 
        """
        This inserts <aName> at position <where> into Trek of <me>. ex: me = "|usr|etc|" me.InsertATrek("sys",2) gives me = "|usr|sys|etc"
        """
    @staticmethod
    def IsAbsolutePath_s(thePath : str) -> bool: 
        """
        Method to recognize path is absolute or not. Detection is based on path syntax - no any filesystem / network access performed.
        """
    @staticmethod
    def IsContentProtocolPath_s(thePath : str) -> bool: 
        """
        Detect special URLs on Android platform. Sample path: content://filename
        """
    @staticmethod
    def IsDosPath_s(thePath : str) -> bool: 
        """
        Detect absolute DOS-path also used in Windows. The total path length is limited to 256 characters. Sample path: C:
        """
    @staticmethod
    def IsNtExtendedPath_s(thePath : str) -> bool: 
        """
        Detect extended-length NT path (can be only absolute). Approximate maximum path is 32767 characters. Sample path: \?: long path File I/O functions in the Windows API convert "/" to "\" as part of converting the name to an NT-style name, except when using the "\\?\" prefix.
        """
    @staticmethod
    def IsRelativePath_s(thePath : str) -> bool: 
        """
        Method to recognize path is absolute or not. Detection is based on path syntax - no any filesystem / network access performed.
        """
    @staticmethod
    def IsRemoteProtocolPath_s(thePath : str) -> bool: 
        """
        Detect remote protocol path (http / ftp / ...). Actually shouldn't be remote... Sample path: http://domain/path/file
        """
    @staticmethod
    def IsUncExtendedPath_s(thePath : str) -> bool: 
        """
        Detect extended-length UNC path. Sample path: \?
        """
    @staticmethod
    def IsUncPath_s(thePath : str) -> bool: 
        """
        UNC is a naming convention used primarily to specify and map network drives in Microsoft Windows. Sample path: \server
        """
    @staticmethod
    def IsUnixPath_s(thePath : str) -> bool: 
        """
        Detect absolute UNIX-path. Sample path: /media/cdrom/file
        """
    @staticmethod
    def IsValid_s(theDependentName : OCP.TCollection.TCollection_AsciiString,theSysType : OSD_SysType=OSD_SysType.OSD_Default) -> bool: 
        """
        Returns TRUE if <theDependentName> is valid for this SysType.
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns file name of <me>. If <me> hasn't been initialized, it returns an empty AsciiString.
        """
    def Node(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Node of <me>.
        """
    def Password(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Password of <me>.
        """
    @staticmethod
    def RelativePath_s(DirPath : OCP.TCollection.TCollection_AsciiString,AbsFilePath : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the relative file path between the absolute directory path <DirPath> and the absolute file path <AbsFilePath>. If <DirPath> starts with "/", paths are handled as on Unix, if it starts with a letter followed by ":", as on WNT. In particular on WNT directory names are not key sensitive. If handling fails, an empty string is returned.
        """
    @overload
    def RemoveATrek(self,where : int) -> None: 
        """
        This removes a component of Trek in <me> at position <where>. The first component of Trek is numbered 1. ex: me = "|usr|bin|" me.RemoveATrek(1) gives me = "|bin|" To avoid a 'NumericError' because of a bad <where>, use TrekLength() to know number of components of Trek in <me>.

        This removes <aName> from <me> in Trek. No error is raised if <aName> is not in <me>. ex: me = "|usr|sys|etc|doc" me.RemoveATrek("sys") gives me = "|usr|etc|doc".
        """
    @overload
    def RemoveATrek(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: ...
    def SetDisk(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets Disk of <me>.
        """
    def SetExtension(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets my extension name.
        """
    def SetName(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets file name of <me>. If <me> hasn't been initialized, it returns an empty AsciiString.
        """
    def SetNode(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets Node of <me>.
        """
    def SetPassword(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets Password of <me>.
        """
    def SetTrek(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets Trek of <me>.
        """
    def SetUserName(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets UserName of <me>.
        """
    def SetValues(self,aNode : OCP.TCollection.TCollection_AsciiString,aUsername : OCP.TCollection.TCollection_AsciiString,aPassword : OCP.TCollection.TCollection_AsciiString,aDisk : OCP.TCollection.TCollection_AsciiString,aTrek : OCP.TCollection.TCollection_AsciiString,aName : OCP.TCollection.TCollection_AsciiString,anExtension : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets each component of a path.
        """
    def SystemName(self,FullName : OCP.TCollection.TCollection_AsciiString,aType : OSD_SysType=OSD_SysType.OSD_Default) -> None: 
        """
        Returns system dependent path <aType> is one among Unix,VMS ... This function is not private because you may need to display system dependent path on a front-end. It can be useful when communicating with another system. For instance when you want to communicate between VMS and Unix to transfer files, or to do a remote procedure call using files. example : OSD_Path myPath ("sparc4", "sga", "secret_passwd", "$5$dkb100","|users|examples"); Internal ( Dependent_name ); On UNIX sga"secret_passwd":/users/examples On VMS sparc4"sga secret_passwd"::$5$dkb100:[users.examples] Sets each component of a Path giving its system dependent name.
        """
    def Trek(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Trek of <me>.
        """
    def TrekLength(self) -> int: 
        """
        Returns number of components in Trek of <me>. ex: me = "|usr|sys|etc|bin" me.TrekLength() returns 4.
        """
    def TrekValue(self,where : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns component of Trek in <me> at position <where>. ex: me = "|usr|bin|sys|" me.TrekValue(2) returns "bin"
        """
    def UpTrek(self) -> None: 
        """
        This removes the last directory name in <aTrek> and returns result. ex: me = "|usr|bin|todo.sh" me.UpTrek() gives me = "|usr|todo.sh" if <me> contains "|", me.UpTrek() will give again "|" without any error.
        """
    def UserName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns UserName of <me>.
        """
    def Values(self,aNode : OCP.TCollection.TCollection_AsciiString,aUsername : OCP.TCollection.TCollection_AsciiString,aPassword : OCP.TCollection.TCollection_AsciiString,aDisk : OCP.TCollection.TCollection_AsciiString,aTrek : OCP.TCollection.TCollection_AsciiString,aName : OCP.TCollection.TCollection_AsciiString,anExtension : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Gets each component of a path.
        """
    @overload
    def __init__(self,aDependentName : OCP.TCollection.TCollection_AsciiString,aSysType : OSD_SysType=OSD_SysType.OSD_Default) -> None: ...
    @overload
    def __init__(self,aNode : OCP.TCollection.TCollection_AsciiString,aUsername : OCP.TCollection.TCollection_AsciiString,aPassword : OCP.TCollection.TCollection_AsciiString,aDisk : OCP.TCollection.TCollection_AsciiString,aTrek : OCP.TCollection.TCollection_AsciiString,aName : OCP.TCollection.TCollection_AsciiString,anExtension : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class OSD_PerfMeter():
    """
    This class enables measuring the CPU time between two points of code execution, regardless of the scope of these points of code. A meter is identified by its name (string). So multiple objects in various places of user code may point to the same meter. The results will be printed on stdout upon finish of the program. For details see OSD_PerfMeter.h
    """
    def Flush(self) -> None: 
        """
        Outputs the meter data and resets it to initial state
        """
    def Init(self,theMeter : str) -> None: 
        """
        Prepares the named meter
        """
    def Start(self) -> None: 
        """
        Starts the meter
        """
    def Stop(self) -> None: 
        """
        Stops the meter
        """
    def Tick(self) -> None: 
        """
        Increments the counter w/o time measurement
        """
    @overload
    def __init__(self,theMeter : str,theToAutoStart : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class OSD_Process():
    """
    A set of system process tools
    """
    def CurrentDirectory(self) -> OSD_Path: 
        """
        Returns the current path where the process is.
        """
    def Error(self) -> int: 
        """
        Returns error number if 'Failed' is TRUE.
        """
    @staticmethod
    def ExecutableFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return full path to the folder containing current process executable with trailing separator.
        """
    @staticmethod
    def ExecutablePath_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return full path to the current process executable.
        """
    def Failed(self) -> bool: 
        """
        Returns TRUE if an error occurs
        """
    def IsSuperUser(self) -> bool: 
        """
        Returns True if the process user is the super-user.
        """
    def Perror(self) -> None: 
        """
        Raises OSD_Error
        """
    def ProcessId(self) -> int: 
        """
        Returns the 'Process Id'
        """
    def Reset(self) -> None: 
        """
        Resets error counter to zero
        """
    def SetCurrentDirectory(self,where : OSD_Path) -> None: 
        """
        Changes the current process directory.
        """
    def SystemDate(self) -> OCP.Quantity.Quantity_Date: 
        """
        Gets system date.
        """
    def TerminalType(self,Name : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Returns the terminal used (vt100, vt200 ,sun-cmd ...)
        """
    def UserName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the user name.
        """
    def __init__(self) -> None: ...
    pass
class OSD_Protection():
    """
    This class provides data to manage file protection Example:These rights are treated in a system dependent manner : On UNIX you have User,Group and Other rights On VMS you have Owner,Group,World and System rights An automatic conversion is done between OSD and UNIX/VMS.
    """
    def Add(self,aProt : OSD_SingleProtection,aRight : OSD_SingleProtection) -> None: 
        """
        Add a right to a single protection. ex: aProt = RWD me.Add(aProt,X) -> aProt = RWXD
        """
    def Group(self) -> OSD_SingleProtection: 
        """
        Gets protection of 'Group'
        """
    def SetGroup(self,priv : OSD_SingleProtection) -> None: 
        """
        Sets protection of 'Group'
        """
    def SetSystem(self,priv : OSD_SingleProtection) -> None: 
        """
        Sets protection of 'System'
        """
    def SetUser(self,priv : OSD_SingleProtection) -> None: 
        """
        Sets protection of 'User'
        """
    def SetValues(self,System : OSD_SingleProtection,User : OSD_SingleProtection,Group : OSD_SingleProtection,World : OSD_SingleProtection) -> None: 
        """
        Sets values of fields
        """
    def SetWorld(self,priv : OSD_SingleProtection) -> None: 
        """
        Sets protection of 'World'
        """
    def Sub(self,aProt : OSD_SingleProtection,aRight : OSD_SingleProtection) -> None: 
        """
        Subtract a right to a single protection. ex: aProt = RWD me.Sub(aProt,RW) -> aProt = D But me.Sub(aProt,RWX) is also valid and gives same result.
        """
    def System(self) -> OSD_SingleProtection: 
        """
        Gets protection of 'System'
        """
    def User(self) -> OSD_SingleProtection: 
        """
        Gets protection of 'User'
        """
    def Values(self,System : OSD_SingleProtection,User : OSD_SingleProtection,Group : OSD_SingleProtection,World : OSD_SingleProtection) -> None: 
        """
        Retrieves values of fields
        """
    def World(self) -> OSD_SingleProtection: 
        """
        Gets protection of 'World'
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,System : OSD_SingleProtection,User : OSD_SingleProtection,Group : OSD_SingleProtection,World : OSD_SingleProtection) -> None: ...
    pass
class OSD_SIGBUS(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_SIGBUS' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_SIGBUS' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_SIGHUP(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_SIGHUP' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_SIGHUP' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_SIGILL(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_SIGILL' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_SIGILL' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_SIGINT(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_SIGINT' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_SIGINT' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_SIGKILL(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_SIGKILL' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_SIGKILL' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_SIGQUIT(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_SIGQUIT' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_SIGQUIT' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_SIGSEGV(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_SIGSEGV' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_SIGSEGV' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_SIGSYS(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_SIGSYS' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_SIGSYS' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_SharedLibrary():
    """
    Interface to dynamic library loader. Provides tools to load a shared library and retrieve the address of an entry point.
    """
    def Destroy(self) -> None: 
        """
        Frees memory allocated.
        """
    def DlClose(self) -> None: 
        """
        Deallocates the address space for the library corresponding to the shared object. If any user function continues to call a symbol resolved in the address space of a library that has been since been deallocated by DlClose, the results are undefined.
        """
    def DlError(self) -> str: 
        """
        The dlerror function returns a string describing the last error that occurred from a call to DlOpen, DlClose or DlSym.
        """
    def DlOpen(self,Mode : OSD_LoadMode) -> bool: 
        """
        The DlOpen method provides an interface to the dynamic library loader to allow shared libraries to be loaded and called at runtime. The DlOpen function attempts to load Filename, in the address space of the process, resolving symbols as appropriate. Any libraries that Filename depends upon are also loaded. If MODE is RTLD_LAZY, then the runtime loader does symbol resolution only as needed. Typically, this means that the first call to a function in the newly loaded library will cause the resolution of the address of that function to occur. If Mode is RTLD_NOW, then the runtime loader must do all symbol binding during the DlOpen call. The DlOpen method returns a handle that is used by DlSym or DlClose. If there is an error, Standard_False is returned, Standard_True otherwise. If a NULL Filename is specified, DlOpen returns a handle for the main executable, which allows access to dynamic symbols in the running program.
        """
    def Name(self) -> str: 
        """
        Returns the name associated to the shared object.
        """
    def SetName(self,aName : str) -> None: 
        """
        Sets a name associated to the shared object.
        """
    @overload
    def __init__(self,aFilename : str) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class OSD_Signal(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.OSD', '__weakref__': <attribute '__weakref__' of 'OSD_Signal' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'OSD_Signal' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class OSD_SignalMode():
    """
    Mode of operation for OSD::SetSignal() function

    Members:

      OSD_SignalMode_AsIs

      OSD_SignalMode_Set

      OSD_SignalMode_SetUnhandled

      OSD_SignalMode_Unset
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
    OSD_SignalMode_AsIs: OCP.OSD.OSD_SignalMode # value = <OSD_SignalMode.OSD_SignalMode_AsIs: 0>
    OSD_SignalMode_Set: OCP.OSD.OSD_SignalMode # value = <OSD_SignalMode.OSD_SignalMode_Set: 1>
    OSD_SignalMode_SetUnhandled: OCP.OSD.OSD_SignalMode # value = <OSD_SignalMode.OSD_SignalMode_SetUnhandled: 2>
    OSD_SignalMode_Unset: OCP.OSD.OSD_SignalMode # value = <OSD_SignalMode.OSD_SignalMode_Unset: 3>
    __entries: dict # value = {'OSD_SignalMode_AsIs': (<OSD_SignalMode.OSD_SignalMode_AsIs: 0>, None), 'OSD_SignalMode_Set': (<OSD_SignalMode.OSD_SignalMode_Set: 1>, None), 'OSD_SignalMode_SetUnhandled': (<OSD_SignalMode.OSD_SignalMode_SetUnhandled: 2>, None), 'OSD_SignalMode_Unset': (<OSD_SignalMode.OSD_SignalMode_Unset: 3>, None)}
    __members__: dict # value = {'OSD_SignalMode_AsIs': <OSD_SignalMode.OSD_SignalMode_AsIs: 0>, 'OSD_SignalMode_Set': <OSD_SignalMode.OSD_SignalMode_Set: 1>, 'OSD_SignalMode_SetUnhandled': <OSD_SignalMode.OSD_SignalMode_SetUnhandled: 2>, 'OSD_SignalMode_Unset': <OSD_SignalMode.OSD_SignalMode_Unset: 3>}
    pass
class OSD_SingleProtection():
    """
    Access rights for files. R means Read, W means Write, X means eXecute and D means Delete. On UNIX, the right to Delete is combined with Write access. So if "W"rite is not set and "D"elete is, "W"rite will be set and if "W" is set, "D" will be too.

    Members:

      OSD_None

      OSD_R

      OSD_W

      OSD_RW

      OSD_X

      OSD_RX

      OSD_WX

      OSD_RWX

      OSD_D

      OSD_RD

      OSD_WD

      OSD_RWD

      OSD_XD

      OSD_RXD

      OSD_WXD

      OSD_RWXD
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
    OSD_D: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_D: 8>
    OSD_None: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_None: 0>
    OSD_R: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_R: 1>
    OSD_RD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RD: 9>
    OSD_RW: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RW: 3>
    OSD_RWD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RWD: 11>
    OSD_RWX: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RWX: 7>
    OSD_RWXD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RWXD: 15>
    OSD_RX: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RX: 5>
    OSD_RXD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RXD: 13>
    OSD_W: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_W: 2>
    OSD_WD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_WD: 10>
    OSD_WX: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_WX: 6>
    OSD_WXD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_WXD: 14>
    OSD_X: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_X: 4>
    OSD_XD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_XD: 12>
    __entries: dict # value = {'OSD_None': (<OSD_SingleProtection.OSD_None: 0>, None), 'OSD_R': (<OSD_SingleProtection.OSD_R: 1>, None), 'OSD_W': (<OSD_SingleProtection.OSD_W: 2>, None), 'OSD_RW': (<OSD_SingleProtection.OSD_RW: 3>, None), 'OSD_X': (<OSD_SingleProtection.OSD_X: 4>, None), 'OSD_RX': (<OSD_SingleProtection.OSD_RX: 5>, None), 'OSD_WX': (<OSD_SingleProtection.OSD_WX: 6>, None), 'OSD_RWX': (<OSD_SingleProtection.OSD_RWX: 7>, None), 'OSD_D': (<OSD_SingleProtection.OSD_D: 8>, None), 'OSD_RD': (<OSD_SingleProtection.OSD_RD: 9>, None), 'OSD_WD': (<OSD_SingleProtection.OSD_WD: 10>, None), 'OSD_RWD': (<OSD_SingleProtection.OSD_RWD: 11>, None), 'OSD_XD': (<OSD_SingleProtection.OSD_XD: 12>, None), 'OSD_RXD': (<OSD_SingleProtection.OSD_RXD: 13>, None), 'OSD_WXD': (<OSD_SingleProtection.OSD_WXD: 14>, None), 'OSD_RWXD': (<OSD_SingleProtection.OSD_RWXD: 15>, None)}
    __members__: dict # value = {'OSD_None': <OSD_SingleProtection.OSD_None: 0>, 'OSD_R': <OSD_SingleProtection.OSD_R: 1>, 'OSD_W': <OSD_SingleProtection.OSD_W: 2>, 'OSD_RW': <OSD_SingleProtection.OSD_RW: 3>, 'OSD_X': <OSD_SingleProtection.OSD_X: 4>, 'OSD_RX': <OSD_SingleProtection.OSD_RX: 5>, 'OSD_WX': <OSD_SingleProtection.OSD_WX: 6>, 'OSD_RWX': <OSD_SingleProtection.OSD_RWX: 7>, 'OSD_D': <OSD_SingleProtection.OSD_D: 8>, 'OSD_RD': <OSD_SingleProtection.OSD_RD: 9>, 'OSD_WD': <OSD_SingleProtection.OSD_WD: 10>, 'OSD_RWD': <OSD_SingleProtection.OSD_RWD: 11>, 'OSD_XD': <OSD_SingleProtection.OSD_XD: 12>, 'OSD_RXD': <OSD_SingleProtection.OSD_RXD: 13>, 'OSD_WXD': <OSD_SingleProtection.OSD_WXD: 14>, 'OSD_RWXD': <OSD_SingleProtection.OSD_RWXD: 15>}
    pass
class OSD_SysType():
    """
    Thisd is a set of possible system types. 'Default' means SysType of machine operating this process. This can be used with the Path class. All UNIX-like are grouped under "UnixBSD" or "UnixSystemV". Such systems are Solaris, NexTOS ... A category of systems accept MSDOS-like path such as WindowsNT and OS2.

    Members:

      OSD_Unknown

      OSD_Default

      OSD_UnixBSD

      OSD_UnixSystemV

      OSD_VMS

      OSD_OS2

      OSD_OSF

      OSD_MacOs

      OSD_Taligent

      OSD_WindowsNT

      OSD_LinuxREDHAT

      OSD_Aix
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
    OSD_Aix: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_Aix: 11>
    OSD_Default: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_Default: 1>
    OSD_LinuxREDHAT: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_LinuxREDHAT: 10>
    OSD_MacOs: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_MacOs: 7>
    OSD_OS2: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_OS2: 5>
    OSD_OSF: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_OSF: 6>
    OSD_Taligent: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_Taligent: 8>
    OSD_UnixBSD: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_UnixBSD: 2>
    OSD_UnixSystemV: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_UnixSystemV: 3>
    OSD_Unknown: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_Unknown: 0>
    OSD_VMS: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_VMS: 4>
    OSD_WindowsNT: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_WindowsNT: 9>
    __entries: dict # value = {'OSD_Unknown': (<OSD_SysType.OSD_Unknown: 0>, None), 'OSD_Default': (<OSD_SysType.OSD_Default: 1>, None), 'OSD_UnixBSD': (<OSD_SysType.OSD_UnixBSD: 2>, None), 'OSD_UnixSystemV': (<OSD_SysType.OSD_UnixSystemV: 3>, None), 'OSD_VMS': (<OSD_SysType.OSD_VMS: 4>, None), 'OSD_OS2': (<OSD_SysType.OSD_OS2: 5>, None), 'OSD_OSF': (<OSD_SysType.OSD_OSF: 6>, None), 'OSD_MacOs': (<OSD_SysType.OSD_MacOs: 7>, None), 'OSD_Taligent': (<OSD_SysType.OSD_Taligent: 8>, None), 'OSD_WindowsNT': (<OSD_SysType.OSD_WindowsNT: 9>, None), 'OSD_LinuxREDHAT': (<OSD_SysType.OSD_LinuxREDHAT: 10>, None), 'OSD_Aix': (<OSD_SysType.OSD_Aix: 11>, None)}
    __members__: dict # value = {'OSD_Unknown': <OSD_SysType.OSD_Unknown: 0>, 'OSD_Default': <OSD_SysType.OSD_Default: 1>, 'OSD_UnixBSD': <OSD_SysType.OSD_UnixBSD: 2>, 'OSD_UnixSystemV': <OSD_SysType.OSD_UnixSystemV: 3>, 'OSD_VMS': <OSD_SysType.OSD_VMS: 4>, 'OSD_OS2': <OSD_SysType.OSD_OS2: 5>, 'OSD_OSF': <OSD_SysType.OSD_OSF: 6>, 'OSD_MacOs': <OSD_SysType.OSD_MacOs: 7>, 'OSD_Taligent': <OSD_SysType.OSD_Taligent: 8>, 'OSD_WindowsNT': <OSD_SysType.OSD_WindowsNT: 9>, 'OSD_LinuxREDHAT': <OSD_SysType.OSD_LinuxREDHAT: 10>, 'OSD_Aix': <OSD_SysType.OSD_Aix: 11>}
    pass
class OSD_Thread():
    """
    A simple platform-intependent interface to execute and control threads.
    """
    def Assign(self,other : OSD_Thread) -> None: 
        """
        Copy thread handle from other OSD_Thread object.
        """
    @staticmethod
    def Current_s() -> int: 
        """
        Auxiliary: returns ID of the current thread
        """
    def Detach(self) -> None: 
        """
        Detaches the execution thread from this Thread object, so that it cannot be waited. Note that mechanics of this operation is different on UNIX/Linux (the thread is put to detached state) and Windows (the handle is closed). However, the purpose is the same: to instruct the system to release all thread data upon its completion.
        """
    def GetId(self) -> int: 
        """
        Returns ID of the currently controlled thread ID, or 0 if no thread is run
        """
    def Run(self,data : capsule=None,WNTStackSize : int=0) -> bool: 
        """
        Starts a thread with thread function given in constructor, passing the specified input data (as void *) to it. The parameter WNTStackSize (on Windows only) specifies size of the stack to be allocated for the thread (by default - the same as for the current executable). Returns True if thread started successfully
        """
    def SetPriority(self,thePriority : int) -> None: 
        """
        None
        """
    def Wait(self) -> bool: 
        """
        Waits till the thread finishes execution.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,other : OSD_Thread) -> None: ...
    pass
class OSD_ThreadPool(OCP.Standard.Standard_Transient):
    """
    Class defining a thread pool for executing algorithms in multi-threaded mode. Thread pool allocates requested amount of threads and keep them alive (in sleep mode when unused) during thread pool lifetime. The same pool can be used by multiple consumers, including nested multi-threading algorithms and concurrent threads: - Thread pool can be used either by multi-threaded algorithm by creating OSD_ThreadPool::Launcher. The functor performing a job takes two parameters - Thread Index and Data Index: void operator(int theThreadIndex, int theDataIndex){} Multi-threaded algorithm may rely on Thread Index for allocating thread-local variables in array form, since the Thread Index is guaranteed to be within range OSD_ThreadPool::Lower() and OSD_ThreadPool::Upper(). - Default thread pool (OSD_ThreadPool::DefaultPool()) can be used in general case, but application may prefer creating a dedicated pool for better control. - Default thread pool allocates the amount of threads considering concurrency level of the system (amount of logical processors). This can be overridden during OSD_ThreadPool construction or by calling OSD_ThreadPool::Init() (the pool should not be used!). - OSD_ThreadPool::Launcher reserves specific amount of threads from the pool for executing multi-threaded Job. Normally, single Launcher instance will occupy all threads available in thread pool, so that nested multi-threaded algorithms (within the same thread) and concurrent threads trying to use the same thread pool will run sequentially. This behavior is affected by OSD_ThreadPool::NbDefaultThreadsToLaunch() parameter and Launcher constructor, so that single Launcher instance will occupy not all threads in the pool allowing other threads to be used concurrently. - OSD_ThreadPool::Launcher locks thread one-by-one from thread pool in a thread-safe way. - Each working thread catches exceptions occurred during job execution, and Launcher will throw Standard_Failure in a caller thread on completed execution.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @staticmethod
    def DefaultPool_s(theNbThreads : int=-1) -> OSD_ThreadPool: ...
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
    def HasThreads(self) -> bool: 
        """
        Return TRUE if at least 2 threads are available (including self-thread).
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theNbThreads : int) -> None: 
        """
        Reinitialize the thread pool with a different number of threads. Should be called only with no active jobs, or exception Standard_ProgramError will be thrown!
        """
    def IsInUse(self) -> bool: 
        """
        Checks if thread pools has active consumers.
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
    def LowerThreadIndex(self) -> int: 
        """
        Return the lower thread index.
        """
    def NbDefaultThreadsToLaunch(self) -> int: 
        """
        Return maximum number of threads to be locked by a single Launcher object by default; the entire thread pool size is returned by default.
        """
    def NbThreads(self) -> int: 
        """
        Return the number of threads; >= 1.
        """
    def SetNbDefaultThreadsToLaunch(self,theNbThreads : int) -> None: 
        """
        Set maximum number of threads to be locked by a single Launcher object by default. Should be set BEFORE first usage.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpperThreadIndex(self) -> int: 
        """
        Return the upper thread index (last index is reserved for self-thread).
        """
    def __init__(self,theNbThreads : int=-1) -> None: ...
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
class OSD_Timer(OSD_Chronometer):
    """
    Working on heterogeneous platforms we need to use the system call gettimeofday. This function is portable and it measures ELAPSED time and CPU time in seconds and microseconds. Example: OSD_Timer aTimer; aTimer.Start(); // Start the timers (t1). ..... // Do something. aTimer.Stop(); // Stop the timers (t2). aTimer.Show(); // Give the elapsed time between t1 and t2. // Give also the process CPU time between // t1 and t2.
    """
    def ElapsedTime(self) -> float: 
        """
        Returns elapsed time in seconds.
        """
    @staticmethod
    def GetProcessCPU_s() -> Tuple[float, float]: 
        """
        Returns CPU time (user and system) consumed by the current process since its start, in seconds. The actual precision of the measurement depends on granularity provided by the system, and is platform-specific.
        """
    @staticmethod
    def GetThreadCPU_s() -> Tuple[float, float]: 
        """
        Returns CPU time (user and system) consumed by the current thread since its start. Note that this measurement is platform-specific, as threads are implemented and managed differently on different platforms and CPUs.
        """
    @staticmethod
    def GetWallClockTime_s() -> float: 
        """
        Returns current time in seconds with system-defined precision. The could be a system uptime or a time from some date. Returned value is intended for precise elapsed time measurements as a delta between timestamps. On Windows implemented via QueryPerformanceCounter(), on other systems via gettimeofday().
        """
    def IsStarted(self) -> bool: 
        """
        Return true if timer has been started.
        """
    def IsThisThreadOnly(self) -> bool: 
        """
        Return TRUE if current thread CPU time should be measured, and FALSE to measure all threads CPU time; FALSE by default,
        """
    @overload
    def Reset(self,theTimeElapsedSec : float) -> None: 
        """
        Stops and reinitializes the timer with specified elapsed time.

        Stops and reinitializes the timer with zero elapsed time.
        """
    @overload
    def Reset(self) -> None: ...
    def Restart(self) -> None: 
        """
        Restarts the Timer.
        """
    def SetThisThreadOnly(self,theIsThreadOnly : bool) -> None: 
        """
        Set if current thread (TRUE) or all threads (FALSE) CPU time should be measured. Will raise exception if Timer is in started state.
        """
    @overload
    def Show(self) -> Tuple[float, int, int, float]: 
        """
        Shows both the elapsed time and CPU time on the standard output stream <cout>.The chronometer can be running (Lap Time) or stopped.

        Shows both the elapsed time and CPU time on the output stream <OS>.

        returns both the elapsed time(seconds,minutes,hours) and CPU time.
        """
    @overload
    def Show(self,os : io.BytesIO) -> None: ...
    @overload
    def Show(self) -> None: ...
    def Start(self) -> None: ...
    def Stop(self) -> None: 
        """
        Stops the Timer.
        """
    def SystemTimeCPU(self) -> float: 
        """
        Returns the current CPU system time in seconds. The chronometer can be running (laps Time) or stopped.
        """
    def UserTimeCPU(self) -> float: 
        """
        Returns the current CPU user time in seconds. The chronometer can be running (laps Time) or stopped.
        """
    def __init__(self,theThisThreadOnly : bool=False) -> None: ...
    pass
class OSD_WhoAmI():
    """
    Allows great accuracy for error management. This is private.

    Members:

      OSD_WDirectory

      OSD_WDirectoryIterator

      OSD_WEnvironment

      OSD_WFile

      OSD_WFileNode

      OSD_WFileIterator

      OSD_WPath

      OSD_WProcess

      OSD_WProtection

      OSD_WHost

      OSD_WDisk

      OSD_WChronometer

      OSD_WTimer

      OSD_WPackage

      OSD_WEnvironmentIterator
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
    OSD_WChronometer: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WChronometer: 11>
    OSD_WDirectory: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WDirectory: 0>
    OSD_WDirectoryIterator: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WDirectoryIterator: 1>
    OSD_WDisk: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WDisk: 10>
    OSD_WEnvironment: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WEnvironment: 2>
    OSD_WEnvironmentIterator: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WEnvironmentIterator: 14>
    OSD_WFile: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WFile: 3>
    OSD_WFileIterator: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WFileIterator: 5>
    OSD_WFileNode: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WFileNode: 4>
    OSD_WHost: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WHost: 9>
    OSD_WPackage: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WPackage: 13>
    OSD_WPath: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WPath: 6>
    OSD_WProcess: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WProcess: 7>
    OSD_WProtection: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WProtection: 8>
    OSD_WTimer: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WTimer: 12>
    __entries: dict # value = {'OSD_WDirectory': (<OSD_WhoAmI.OSD_WDirectory: 0>, None), 'OSD_WDirectoryIterator': (<OSD_WhoAmI.OSD_WDirectoryIterator: 1>, None), 'OSD_WEnvironment': (<OSD_WhoAmI.OSD_WEnvironment: 2>, None), 'OSD_WFile': (<OSD_WhoAmI.OSD_WFile: 3>, None), 'OSD_WFileNode': (<OSD_WhoAmI.OSD_WFileNode: 4>, None), 'OSD_WFileIterator': (<OSD_WhoAmI.OSD_WFileIterator: 5>, None), 'OSD_WPath': (<OSD_WhoAmI.OSD_WPath: 6>, None), 'OSD_WProcess': (<OSD_WhoAmI.OSD_WProcess: 7>, None), 'OSD_WProtection': (<OSD_WhoAmI.OSD_WProtection: 8>, None), 'OSD_WHost': (<OSD_WhoAmI.OSD_WHost: 9>, None), 'OSD_WDisk': (<OSD_WhoAmI.OSD_WDisk: 10>, None), 'OSD_WChronometer': (<OSD_WhoAmI.OSD_WChronometer: 11>, None), 'OSD_WTimer': (<OSD_WhoAmI.OSD_WTimer: 12>, None), 'OSD_WPackage': (<OSD_WhoAmI.OSD_WPackage: 13>, None), 'OSD_WEnvironmentIterator': (<OSD_WhoAmI.OSD_WEnvironmentIterator: 14>, None)}
    __members__: dict # value = {'OSD_WDirectory': <OSD_WhoAmI.OSD_WDirectory: 0>, 'OSD_WDirectoryIterator': <OSD_WhoAmI.OSD_WDirectoryIterator: 1>, 'OSD_WEnvironment': <OSD_WhoAmI.OSD_WEnvironment: 2>, 'OSD_WFile': <OSD_WhoAmI.OSD_WFile: 3>, 'OSD_WFileNode': <OSD_WhoAmI.OSD_WFileNode: 4>, 'OSD_WFileIterator': <OSD_WhoAmI.OSD_WFileIterator: 5>, 'OSD_WPath': <OSD_WhoAmI.OSD_WPath: 6>, 'OSD_WProcess': <OSD_WhoAmI.OSD_WProcess: 7>, 'OSD_WProtection': <OSD_WhoAmI.OSD_WProtection: 8>, 'OSD_WHost': <OSD_WhoAmI.OSD_WHost: 9>, 'OSD_WDisk': <OSD_WhoAmI.OSD_WDisk: 10>, 'OSD_WChronometer': <OSD_WhoAmI.OSD_WChronometer: 11>, 'OSD_WTimer': <OSD_WhoAmI.OSD_WTimer: 12>, 'OSD_WPackage': <OSD_WhoAmI.OSD_WPackage: 13>, 'OSD_WEnvironmentIterator': <OSD_WhoAmI.OSD_WEnvironmentIterator: 14>}
    pass
def OSD_FileStatCTime(theName : str) -> int:
    """
    Function retrieves file timestamp.
    """
def OSD_OpenFile(theName : OCP.TCollection.TCollection_ExtendedString,theMode : str) -> _iobuf:
    """
    Function opens the file.
    """
def OSD_OpenFileDescriptor(theName : OCP.TCollection.TCollection_ExtendedString,theMode : int) -> int:
    """
    Open file descriptor for specified UTF-16 file path.
    """
OSD_AIX: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_AIX: 11>
OSD_Aix: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_Aix: 11>
OSD_D: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_D: 8>
OSD_DEC: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_DEC: 2>
OSD_DIRECTORY: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_DIRECTORY: 1>
OSD_Default: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_Default: 1>
OSD_ExclusiveLock: OCP.OSD.OSD_LockType # value = <OSD_LockType.OSD_ExclusiveLock: 3>
OSD_FILE: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_FILE: 0>
OSD_FromBeginning: OCP.OSD.OSD_FromWhere # value = <OSD_FromWhere.OSD_FromBeginning: 0>
OSD_FromEnd: OCP.OSD.OSD_FromWhere # value = <OSD_FromWhere.OSD_FromEnd: 2>
OSD_FromHere: OCP.OSD.OSD_FromWhere # value = <OSD_FromWhere.OSD_FromHere: 1>
OSD_HP: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_HP: 7>
OSD_IBM: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_IBM: 8>
OSD_LIN: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_LIN: 10>
OSD_LINK: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_LINK: 2>
OSD_LinuxREDHAT: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_LinuxREDHAT: 10>
OSD_MAC: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_MAC: 5>
OSD_MacOs: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_MacOs: 7>
OSD_NEC: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_NEC: 4>
OSD_NoLock: OCP.OSD.OSD_LockType # value = <OSD_LockType.OSD_NoLock: 0>
OSD_None: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_None: 0>
OSD_OS2: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_OS2: 5>
OSD_OSF: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_OSF: 6>
OSD_PC: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_PC: 6>
OSD_R: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_R: 1>
OSD_RD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RD: 9>
OSD_RTLD_LAZY: OCP.OSD.OSD_LoadMode # value = <OSD_LoadMode.OSD_RTLD_LAZY: 0>
OSD_RTLD_NOW: OCP.OSD.OSD_LoadMode # value = <OSD_LoadMode.OSD_RTLD_NOW: 1>
OSD_RW: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RW: 3>
OSD_RWD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RWD: 11>
OSD_RWX: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RWX: 7>
OSD_RWXD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RWXD: 15>
OSD_RX: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RX: 5>
OSD_RXD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_RXD: 13>
OSD_ReadLock: OCP.OSD.OSD_LockType # value = <OSD_LockType.OSD_ReadLock: 1>
OSD_ReadOnly: OCP.OSD.OSD_OpenMode # value = <OSD_OpenMode.OSD_ReadOnly: 0>
OSD_ReadWrite: OCP.OSD.OSD_OpenMode # value = <OSD_OpenMode.OSD_ReadWrite: 2>
OSD_SGI: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_SGI: 3>
OSD_SOCKET: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_SOCKET: 3>
OSD_SUN: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_SUN: 1>
OSD_SignalMode_AsIs: OCP.OSD.OSD_SignalMode # value = <OSD_SignalMode.OSD_SignalMode_AsIs: 0>
OSD_SignalMode_Set: OCP.OSD.OSD_SignalMode # value = <OSD_SignalMode.OSD_SignalMode_Set: 1>
OSD_SignalMode_SetUnhandled: OCP.OSD.OSD_SignalMode # value = <OSD_SignalMode.OSD_SignalMode_SetUnhandled: 2>
OSD_SignalMode_Unset: OCP.OSD.OSD_SignalMode # value = <OSD_SignalMode.OSD_SignalMode_Unset: 3>
OSD_Taligent: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_Taligent: 8>
OSD_UNKNOWN: OCP.OSD.OSD_KindFile # value = <OSD_KindFile.OSD_UNKNOWN: 4>
OSD_Unavailable: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_Unavailable: 0>
OSD_UnixBSD: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_UnixBSD: 2>
OSD_UnixSystemV: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_UnixSystemV: 3>
OSD_Unknown: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_Unknown: 0>
OSD_VAX: OCP.OSD.OSD_OEMType # value = <OSD_OEMType.OSD_VAX: 9>
OSD_VMS: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_VMS: 4>
OSD_W: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_W: 2>
OSD_WChronometer: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WChronometer: 11>
OSD_WD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_WD: 10>
OSD_WDirectory: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WDirectory: 0>
OSD_WDirectoryIterator: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WDirectoryIterator: 1>
OSD_WDisk: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WDisk: 10>
OSD_WEnvironment: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WEnvironment: 2>
OSD_WEnvironmentIterator: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WEnvironmentIterator: 14>
OSD_WFile: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WFile: 3>
OSD_WFileIterator: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WFileIterator: 5>
OSD_WFileNode: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WFileNode: 4>
OSD_WHost: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WHost: 9>
OSD_WPackage: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WPackage: 13>
OSD_WPath: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WPath: 6>
OSD_WProcess: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WProcess: 7>
OSD_WProtection: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WProtection: 8>
OSD_WTimer: OCP.OSD.OSD_WhoAmI # value = <OSD_WhoAmI.OSD_WTimer: 12>
OSD_WX: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_WX: 6>
OSD_WXD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_WXD: 14>
OSD_WindowsNT: OCP.OSD.OSD_SysType # value = <OSD_SysType.OSD_WindowsNT: 9>
OSD_WriteLock: OCP.OSD.OSD_LockType # value = <OSD_LockType.OSD_WriteLock: 2>
OSD_WriteOnly: OCP.OSD.OSD_OpenMode # value = <OSD_OpenMode.OSD_WriteOnly: 1>
OSD_X: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_X: 4>
OSD_XD: OCP.OSD.OSD_SingleProtection # value = <OSD_SingleProtection.OSD_XD: 12>
