import OCP.Standard
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.TColStd
import io
__all__  = [
"Standard",
"Standard_AbortiveTransaction",
"Standard_ArrayStreamBuffer",
"Standard_CLocaleSentry",
"Standard_Condition",
"Standard_ConstructionError",
"Standard_DimensionError",
"Standard_DimensionMismatch",
"Standard_DivideByZero",
"Standard_DomainError",
"Standard_Dump",
"Standard_DumpValue",
"Standard_ErrorHandler",
"Standard_Failure",
"Standard_GUID",
"Standard_HandlerStatus",
"Standard_ImmutableObject",
"Standard_JsonKey",
"Standard_LicenseError",
"Standard_LicenseNotFound",
"Standard_MMgrRoot",
"Standard_MMgrRaw",
"Standard_MMgrOpt",
"Standard_MMgrTBBalloc",
"Standard_MultiplyDefined",
"Standard_Mutex",
"Standard_NegativeValue",
"Standard_NoMoreObject",
"Standard_NoSuchObject",
"Standard_NotImplemented",
"Standard_NullObject",
"Standard_NullValue",
"Standard_NumericError",
"Standard_OutOfMemory",
"Standard_OutOfRange",
"Standard_Overflow",
"Standard_Transient",
"Standard_ProgramError",
"Standard_RangeError",
"Standard_ReadBuffer",
"Standard_ReadLineBuffer",
"Standard_Static_Assert_true",
"Standard_Persistent",
"Standard_Type",
"Standard_TypeMismatch",
"Standard_UUID",
"Standard_Underflow",
"ACos",
"ACosApprox",
"ACosh",
"ASin",
"ASinh",
"ATan",
"ATan2",
"ATanh",
"Abs",
"Ceiling",
"Cos",
"Cosh",
"Epsilon",
"Exp",
"Floor",
"HashCodes",
"IntToReal",
"IntegerFirst",
"IntegerLast",
"IntegerPart",
"IntegerSize",
"IsAlphabetic",
"IsAlphanumeric",
"IsAnAscii",
"IsControl",
"IsDigit",
"IsEqual",
"IsEven",
"IsGraphic",
"IsLowerCase",
"IsOdd",
"IsPrintable",
"IsPunctuation",
"IsSpace",
"IsUpperCase",
"IsXDigit",
"Log",
"Log10",
"LowerCase",
"Max",
"Min",
"Modulus",
"NextAfter",
"Pow",
"RealDigits",
"RealEpsilon",
"RealFirst",
"RealFirst10Exp",
"RealLast",
"RealLast10Exp",
"RealMantissa",
"RealPart",
"RealRadix",
"RealSize",
"RealSmall",
"RealToInt",
"RealToShortReal",
"Round",
"ShortRealDigits",
"ShortRealEpsilon",
"ShortRealFirst",
"ShortRealFirst10Exp",
"ShortRealLast",
"ShortRealLast10Exp",
"ShortRealMantissa",
"ShortRealRadix",
"ShortRealSize",
"ShortRealSmall",
"Sign",
"Sin",
"Sinh",
"Sqrt",
"Square",
"Standard_ASSERT_DO_NOTHING",
"Standard_Atomic_CompareAndSwap",
"Standard_Atomic_Decrement",
"Standard_Atomic_Increment",
"Tan",
"Tanh",
"ToCharacter",
"ToExtCharacter",
"UpperCase",
"Standard_HandlerJumped",
"Standard_HandlerProcessed",
"Standard_HandlerVoid",
"Standard_JsonKey_CloseChild",
"Standard_JsonKey_CloseContainer",
"Standard_JsonKey_None",
"Standard_JsonKey_OpenChild",
"Standard_JsonKey_OpenContainer",
"Standard_JsonKey_Quote",
"Standard_JsonKey_SeparatorKeyToValue",
"Standard_JsonKey_SeparatorValueToValue"
]
class Standard():
    """
    The package Standard provides global memory allocator and other basic services used by other OCCT components.
    """
    @staticmethod
    def AllocateAligned_s(theSize : int,theAlign : int) -> capsule: 
        """
        Allocates aligned memory blocks. Should be used with CPU instructions which require specific alignment. For example: SSE requires 16 bytes, AVX requires 32 bytes.
        """
    @staticmethod
    def Allocate_s(aSize : int) -> capsule: 
        """
        Allocates memory blocks aSize - bytes to allocate
        """
    @staticmethod
    def FreeAligned_s(thePtrAligned : capsule) -> None: 
        """
        Deallocates memory blocks
        """
    @staticmethod
    def Free_s(thePtr : capsule) -> None: 
        """
        Deallocates memory blocks
        """
    @staticmethod
    def Purge_s() -> int: 
        """
        Deallocates the storage retained on the free list and clears the list. Returns non-zero if some memory has been actually freed.
        """
    @staticmethod
    def Reallocate_s(aStorage : capsule,aNewSize : int) -> capsule: 
        """
        Reallocates memory blocks aStorage - previously allocated memory block aNewSize - new size in bytes
        """
    @staticmethod
    def StackTrace_s(theBuffer : str,theBufferSize : int,theNbTraces : int,theContext : capsule=None,theNbTopSkip : int=0) -> bool: 
        """
        Appends backtrace to a message buffer. Stack information might be incomplete in case of stripped binaries. Implementation details: - Not implemented for Android, iOS, QNX and UWP platforms. - On non-Windows platform, this function is a wrapper to backtrace() system call. - On Windows (Win32) platform, the function loads DbgHelp.dll dynamically, and no stack will be provided if this or companion libraries (SymSrv.dll, SrcSrv.dll, etc.) will not be found; .pdb symbols should be provided on Windows platform to retrieve a meaningful stack; only x86_64 CPU architecture is currently implemented.
        """
    def __init__(self) -> None: ...
    pass
class Standard_AbortiveTransaction(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_AbortiveTransaction' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_AbortiveTransaction' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_ArrayStreamBuffer():
    """
    Custom buffer object implementing STL interface std::streambuf for streamed reading from allocated memory block. Implements minimal sub-set of methods for passing buffer to std::istream, including seek support.
    """
    def Init(self,theBegin : str,theSize : int) -> None: 
        """
        (Re)-initialize the stream. Passed pointer is stored as is (memory is NOT copied nor released with destructor).
        """
    def __init__(self,theBegin : str,theSize : int) -> None: ...
    def xsgetn(self,thePtr : str,theCount : int) -> int: 
        """
        Read a bunch of bytes at once.
        """
    pass
class Standard_CLocaleSentry():
    """
    This class intended to temporary switch C locale and logically equivalent to setlocale(LC_ALL, "C"). It is intended to format text regardless of user locale settings (for import/export functionality). Thus following calls to sprintf, atoi and other functions will use "C" locale. Destructor of this class will return original locale.
    """
    def __init__(self) -> None: ...
    pass
class Standard_Condition():
    """
    This is boolean flag intended for communication between threads. One thread sets this flag to TRUE to indicate some event happened and another thread either waits this event or checks periodically its state to perform job.
    """
    def Check(self) -> bool: 
        """
        Do not wait for signal - just test it state.
        """
    def CheckReset(self) -> bool: 
        """
        Method perform two steps at-once - reset the event object and returns true if it was in signaling state.
        """
    def Reset(self) -> None: 
        """
        Reset event (unset signaling state)
        """
    def Set(self) -> None: 
        """
        Set event into signaling state.
        """
    @overload
    def Wait(self) -> None: 
        """
        Wait for Event (infinity).

        Wait for signal requested time.
        """
    @overload
    def Wait(self,theTimeMilliseconds : int) -> bool: ...
    def __init__(self,theIsSet : bool) -> None: ...
    def getHandle(self) -> capsule: 
        """
        Access native HANDLE to Event object.
        """
    pass
class Standard_ConstructionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_ConstructionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_ConstructionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_DimensionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_DimensionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_DimensionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_DimensionMismatch(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_DimensionMismatch' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_DimensionMismatch' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_DivideByZero(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_DivideByZero' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_DivideByZero' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_DomainError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_DomainError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_DomainError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_Dump():
    """
    This interface has some tool methods for stream (in JSON format) processing.
    """
    @staticmethod
    def AddValuesSeparator_s(theOStream : io.BytesIO) -> None: ...
    @staticmethod
    def DumpFieldToName_s(theField : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Convert field name into dump text value, removes "&" and "my" prefixes An example, for field myValue, theName is Value, for &myCLass, the name is Class
        """
    @staticmethod
    def DumpKeyToClass_s(theOStream : io.BytesIO,theKey : OCP.TCollection.TCollection_AsciiString,theField : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Append into output value: "Name": { Field }
        """
    @staticmethod
    def FormatJson_s(theStream : Any,theIndent : int=3) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Converts stream value to string value. Improves the text presentation with the following cases: - for '{' append after '' and indent to the next value, increment current indent value - for '}' append '' and current indent before it, decrement indent value - for ',' append after '' and indent to the next value. If the current symbol is in massive container [], do nothing Covers result with opened and closed brackets on the top level, if it has no symbols there.
        """
    @staticmethod
    @overload
    def GetPointerInfo_s(thePointer : Standard_Transient,isShortInfo : bool=True) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Convert handle pointer to address of the pointer. If the handle is NULL, the result is an empty string.

        Convert pointer to address of the pointer. If the handle is NULL, the result is an empty string.
        """
    @staticmethod
    @overload
    def GetPointerInfo_s(thePointer : capsule,isShortInfo : bool=True) -> OCP.TCollection.TCollection_AsciiString: ...
    @staticmethod
    def GetPointerPrefix_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns default prefix added for each pointer info string if short presentation of pointer used
        """
    @staticmethod
    def HasChildKey_s(theSourceValue : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Returns true if the value has bracket key
        """
    @staticmethod
    def HierarchicalValueIndices_s(theValues : Any) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Returns container of indices in values, that has hierarchical value
        """
    @staticmethod
    def InitValue_s(theStreamStr : OCP.TCollection.TCollection_AsciiString,theStreamPos : int,theValue : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Returns real value
        """
    @staticmethod
    def JsonKeyLength_s(theKey : Standard_JsonKey) -> int: 
        """
        Returns length value for enum type
        """
    @staticmethod
    def JsonKeyToString_s(theKey : Standard_JsonKey) -> str: 
        """
        Returns key value for enum type
        """
    @staticmethod
    def ProcessFieldName_s(theStreamStr : OCP.TCollection.TCollection_AsciiString,theName : OCP.TCollection.TCollection_AsciiString,theStreamPos : int) -> bool: 
        """
        Check whether the field name is equal to the name in the stream at position
        """
    @staticmethod
    def ProcessStreamName_s(theStreamStr : OCP.TCollection.TCollection_AsciiString,theName : OCP.TCollection.TCollection_AsciiString,theStreamPos : int) -> bool: 
        """
        Check whether the parameter name is equal to the name in the stream at position
        """
    @staticmethod
    def SplitJson_s(theStreamStr : OCP.TCollection.TCollection_AsciiString,theKeyToValues : Any) -> bool: 
        """
        Converts stream into map of values.
        """
    @staticmethod
    def Text_s(theStream : Any) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Converts stream value to string value. The result is original stream value.
        """
    def __init__(self) -> None: ...
    pass
class Standard_DumpValue():
    """
    Type for storing a dump value with the stream position
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theValue : OCP.TCollection.TCollection_AsciiString,theStartPos : int) -> None: ...
    @property
    def myStartPosition(self) -> int:
        """
        :type: int
        """
    @myStartPosition.setter
    def myStartPosition(self, arg0: int) -> None:
        pass
    @property
    def myValue(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @myValue.setter
    def myValue(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    pass
class Standard_ErrorHandler():
    """
    Class implementing mechanics of conversion of signals to exceptions.
    """
    def Catches(self,aType : Standard_Type) -> bool: 
        """
        Returns "True" if the caught exception has the same type or inherits from "aType"
        """
    def Destroy(self) -> None: 
        """
        Unlinks and checks if there is a raised exception.
        """
    def Error(self) -> Standard_Failure: 
        """
        Returns the current Error.
        """
    @staticmethod
    def IsInTryBlock_s() -> bool: 
        """
        Test if the code is currently running in a try block
        """
    def Label(self) -> _SETJMP_FLOAT128: 
        """
        Returns label for jump
        """
    @staticmethod
    def LastCaughtError_s() -> Standard_Failure: 
        """
        Returns the caught exception.
        """
    def Unlink(self) -> None: 
        """
        Removes handler from the handlers list
        """
    def __init__(self) -> None: ...
    pass
class Standard_Failure(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_Failure' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_Failure' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_GUID():
    """
    None
    """
    @overload
    def Assign(self,uid : Standard_GUID) -> None: 
        """
        None

        None
        """
    @overload
    def Assign(self,uid : Standard_UUID) -> None: ...
    @staticmethod
    def CheckGUIDFormat_s(aGuid : str) -> bool: 
        """
        Check the format of a GUID string. It checks the size, the position of the '-' and the correct size of fields.
        """
    def Hash(self,Upper : int) -> int: 
        """
        Hash function for GUID.
        """
    @staticmethod
    def HashCode_s(theGUID : Standard_GUID,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given GUID of the Standard_Integer type, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(string1 : Standard_GUID,string2 : Standard_GUID) -> bool: 
        """
        Returns True when the two GUID are the same.
        """
    def IsNotSame(self,uid : Standard_GUID) -> bool: 
        """
        None
        """
    def IsSame(self,uid : Standard_GUID) -> bool: 
        """
        None
        """
    def ShallowDump(self,aStream : io.BytesIO) -> None: 
        """
        Display the GUID with the following format:
        """
    def ToCString(self,aStrGuid : str) -> None: 
        """
        translate the GUID into ascii string the aStrGuid is allocated by user. the guid have the following format:
        """
    def ToExtString(self,aStrGuid : str) -> None: 
        """
        translate the GUID into unicode string the aStrGuid is allocated by user. the guid have the following format:
        """
    def ToUUID(self) -> Standard_UUID: 
        """
        None
        """
    @overload
    def __init__(self,aGuid : str) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aGuid : Standard_UUID) -> None: ...
    @overload
    def __init__(self,a32b : int,a16b1 : str,a16b2 : str,a16b3 : str,a8b1 : int,a8b2 : int,a8b3 : int,a8b4 : int,a8b5 : int,a8b6 : int) -> None: ...
    @overload
    def __init__(self,aGuid : Standard_GUID) -> None: ...
    pass
class Standard_HandlerStatus():
    """
    None

    Members:

      Standard_HandlerVoid

      Standard_HandlerJumped

      Standard_HandlerProcessed
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
    Standard_HandlerJumped: OCP.Standard.Standard_HandlerStatus # value = <Standard_HandlerStatus.Standard_HandlerJumped: 1>
    Standard_HandlerProcessed: OCP.Standard.Standard_HandlerStatus # value = <Standard_HandlerStatus.Standard_HandlerProcessed: 2>
    Standard_HandlerVoid: OCP.Standard.Standard_HandlerStatus # value = <Standard_HandlerStatus.Standard_HandlerVoid: 0>
    __entries: dict # value = {'Standard_HandlerVoid': (<Standard_HandlerStatus.Standard_HandlerVoid: 0>, None), 'Standard_HandlerJumped': (<Standard_HandlerStatus.Standard_HandlerJumped: 1>, None), 'Standard_HandlerProcessed': (<Standard_HandlerStatus.Standard_HandlerProcessed: 2>, None)}
    __members__: dict # value = {'Standard_HandlerVoid': <Standard_HandlerStatus.Standard_HandlerVoid: 0>, 'Standard_HandlerJumped': <Standard_HandlerStatus.Standard_HandlerJumped: 1>, 'Standard_HandlerProcessed': <Standard_HandlerStatus.Standard_HandlerProcessed: 2>}
    pass
class Standard_ImmutableObject(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_ImmutableObject' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_ImmutableObject' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_JsonKey():
    """
    Kind of key in Json string

    Members:

      Standard_JsonKey_None

      Standard_JsonKey_OpenChild

      Standard_JsonKey_CloseChild

      Standard_JsonKey_OpenContainer

      Standard_JsonKey_CloseContainer

      Standard_JsonKey_Quote

      Standard_JsonKey_SeparatorKeyToValue

      Standard_JsonKey_SeparatorValueToValue
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
    Standard_JsonKey_CloseChild: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_CloseChild: 2>
    Standard_JsonKey_CloseContainer: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_CloseContainer: 4>
    Standard_JsonKey_None: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_None: 0>
    Standard_JsonKey_OpenChild: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_OpenChild: 1>
    Standard_JsonKey_OpenContainer: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_OpenContainer: 3>
    Standard_JsonKey_Quote: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_Quote: 5>
    Standard_JsonKey_SeparatorKeyToValue: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_SeparatorKeyToValue: 6>
    Standard_JsonKey_SeparatorValueToValue: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_SeparatorValueToValue: 7>
    __entries: dict # value = {'Standard_JsonKey_None': (<Standard_JsonKey.Standard_JsonKey_None: 0>, None), 'Standard_JsonKey_OpenChild': (<Standard_JsonKey.Standard_JsonKey_OpenChild: 1>, None), 'Standard_JsonKey_CloseChild': (<Standard_JsonKey.Standard_JsonKey_CloseChild: 2>, None), 'Standard_JsonKey_OpenContainer': (<Standard_JsonKey.Standard_JsonKey_OpenContainer: 3>, None), 'Standard_JsonKey_CloseContainer': (<Standard_JsonKey.Standard_JsonKey_CloseContainer: 4>, None), 'Standard_JsonKey_Quote': (<Standard_JsonKey.Standard_JsonKey_Quote: 5>, None), 'Standard_JsonKey_SeparatorKeyToValue': (<Standard_JsonKey.Standard_JsonKey_SeparatorKeyToValue: 6>, None), 'Standard_JsonKey_SeparatorValueToValue': (<Standard_JsonKey.Standard_JsonKey_SeparatorValueToValue: 7>, None)}
    __members__: dict # value = {'Standard_JsonKey_None': <Standard_JsonKey.Standard_JsonKey_None: 0>, 'Standard_JsonKey_OpenChild': <Standard_JsonKey.Standard_JsonKey_OpenChild: 1>, 'Standard_JsonKey_CloseChild': <Standard_JsonKey.Standard_JsonKey_CloseChild: 2>, 'Standard_JsonKey_OpenContainer': <Standard_JsonKey.Standard_JsonKey_OpenContainer: 3>, 'Standard_JsonKey_CloseContainer': <Standard_JsonKey.Standard_JsonKey_CloseContainer: 4>, 'Standard_JsonKey_Quote': <Standard_JsonKey.Standard_JsonKey_Quote: 5>, 'Standard_JsonKey_SeparatorKeyToValue': <Standard_JsonKey.Standard_JsonKey_SeparatorKeyToValue: 6>, 'Standard_JsonKey_SeparatorValueToValue': <Standard_JsonKey.Standard_JsonKey_SeparatorValueToValue: 7>}
    pass
class Standard_LicenseError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_LicenseError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_LicenseError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_LicenseNotFound(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_LicenseNotFound' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_LicenseNotFound' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_MMgrRoot():
    """
    Root class for Open CASCADE mmemory managers. Defines only abstract interface functions.
    """
    def Allocate(self,theSize : int) -> capsule: 
        """
        Allocate specified number of bytes. The actually allocated space should be rounded up to double word size (4 bytes), as this is expected by implementation of some classes in OCC (e.g. TCollection_AsciiString)
        """
    def Free(self,thePtr : capsule) -> None: 
        """
        Frees previously allocated memory at specified address.
        """
    def Purge(self,isDestroyed : bool=False) -> int: 
        """
        Purge internally cached unused memory blocks (if any) by releasing them to the operating system. Must return non-zero if some memory has been actually released, or zero otherwise.
        """
    def Reallocate(self,thePtr : capsule,theSize : int) -> capsule: 
        """
        Reallocate previously allocated memory to contain at least theSize bytes. In case of success, new pointer is returned.
        """
    pass
class Standard_MMgrRaw(Standard_MMgrRoot):
    """
    Implementation of raw OCC memory manager which uses standard C functions: malloc (or calloc), free and realloc without any optimization
    """
    def Allocate(self,aSize : int) -> capsule: 
        """
        Allocate aSize bytes
        """
    def Free(self,thePtr : capsule) -> None: 
        """
        Free allocated memory. The pointer is nullified.
        """
    def Purge(self,isDestroyed : bool=False) -> int: 
        """
        Purge internally cached unused memory blocks (if any) by releasing them to the operating system. Must return non-zero if some memory has been actually released, or zero otherwise.
        """
    def Reallocate(self,thePtr : capsule,theSize : int) -> capsule: 
        """
        Reallocate aPtr to the size aSize. The new pointer is returned.
        """
    def __init__(self,aClear : bool=False) -> None: ...
    pass
class Standard_MMgrOpt(Standard_MMgrRoot):
    """
    Open CASCADE memory manager optimized for speed.
    """
    def Allocate(self,aSize : int) -> capsule: 
        """
        Allocate aSize bytes; see class description above
        """
    def Free(self,thePtr : capsule) -> None: 
        """
        Free previously allocated block. Note that block can not all blocks are released to the OS by this method (see class description)
        """
    def Purge(self,isDestroyed : bool) -> int: 
        """
        Release medium-sized blocks of memory in free lists to the system. Returns number of actually freed blocks
        """
    def Reallocate(self,thePtr : capsule,theSize : int) -> capsule: 
        """
        Reallocate previously allocated aPtr to a new size; new address is returned. In case that aPtr is null, the function behaves exactly as Allocate.
        """
    @staticmethod
    def SetCallBackFunction_s(pFunc : Any) -> None: 
        """
        SetCallBackFunction_s(pFunc: void __cdecl(bool,void * __ptr64,unsigned __int64,unsigned __int64)) -> None

        Set the callback function. You may pass 0 there to turn off the callback. The callback function, if set, will be automatically called from within Allocate and Free methods.
        """
    def __init__(self,aClear : bool=True,aMMap : bool=True,aCellSize : int=200,aNbPages : int=10000,aThreshold : int=40000) -> None: ...
    pass
class Standard_MMgrTBBalloc(Standard_MMgrRoot):
    """
    Implementation of OCC memory manager which uses Intel TBB scalable allocator.
    """
    def Allocate(self,aSize : int) -> capsule: 
        """
        Allocate aSize bytes
        """
    def Free(self,thePtr : capsule) -> None: 
        """
        Free allocated memory
        """
    def Purge(self,isDestroyed : bool=False) -> int: 
        """
        Purge internally cached unused memory blocks (if any) by releasing them to the operating system. Must return non-zero if some memory has been actually released, or zero otherwise.
        """
    def Reallocate(self,thePtr : capsule,theSize : int) -> capsule: 
        """
        Reallocate aPtr to the size aSize. The new pointer is returned.
        """
    def __init__(self,aClear : bool=False) -> None: ...
    pass
class Standard_MultiplyDefined(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_MultiplyDefined' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_MultiplyDefined' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_Mutex():
    """
    Mutex: a class to synchronize access to shared data.
    """
    def Lock(self) -> None: 
        """
        Method to lock the mutex; waits until the mutex is released by other threads, locks it and then returns
        """
    def TryLock(self) -> bool: 
        """
        Method to test the mutex; if the mutex is not hold by other thread, locks it and returns True; otherwise returns False without waiting mutex to be released.
        """
    def Unlock(self) -> None: 
        """
        Method to unlock the mutex; releases it to other users

        Method to unlock the mutex; releases it to other users
        """
    def __init__(self) -> None: ...
    pass
class Standard_NegativeValue(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_NegativeValue' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_NegativeValue' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_NoMoreObject(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_NoMoreObject' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_NoMoreObject' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_NoSuchObject(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_NoSuchObject' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_NoSuchObject' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_NotImplemented(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_NotImplemented' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_NotImplemented' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_NullObject(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_NullObject' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_NullObject' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_NullValue(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_NullValue' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_NullValue' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_NumericError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_NumericError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_NumericError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_OutOfMemory(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_OutOfMemory' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_OutOfMemory' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_OutOfRange(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_OutOfRange' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_OutOfRange' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_Overflow(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_Overflow' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_Overflow' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_Transient():
    """
    Abstract class which forms the root of the entire Transient class hierarchy.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> Standard_Type: 
        """
        Returns a type descriptor about this object.
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
    def IsInstance(self,theType : Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : Standard_Type) -> bool: ...
    def This(self) -> Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,arg1 : Standard_Transient) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> Standard_Type: 
        """
        Returns type descriptor of Standard_Transient class
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class Standard_ProgramError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_ProgramError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_ProgramError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_RangeError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_RangeError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_RangeError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_ReadBuffer():
    """
    Auxiliary tool for buffered reading from input stream within chunks of constant size.
    """
    def Init(self,theDataLen : int,theChunkLen : int,theIsPartialPayload : bool=False) -> None: 
        """
        Initialize the buffer.
        """
    def IsDone(self) -> bool: 
        """
        Return TRUE if amount of read bytes is equal to requested length of entire data.
        """
    def __init__(self,theDataLen : int,theChunkLen : int,theIsPartialPayload : bool=False) -> None: ...
    pass
class Standard_ReadLineBuffer():
    """
    Auxiliary tool for buffered reading of lines from input stream.
    """
    def Clear(self) -> None: 
        """
        Clear buffer and cached values.
        """
    def IsMultilineMode(self) -> bool: 
        """
        Returns TRUE when the Multiline Mode is on; FALSE by default. Multiline modes joins several lines in file having \ at the end of line:
        """
    def SetMultilineMode(self,theMultilineMode : bool,theToPutGap : bool=True) -> None: 
        """
        Sets or unsets the multi-line mode.
        """
    def ToPutGapInMultiline(self) -> bool: 
        """
        Put gap space while merging lines within multiline syntax, so that the following sample: Will become "1/2/3 4/5/6" when flag is TRUE, and "1/2/35/5/6" otherwise.
        """
    def __init__(self,theMaxBufferSizeBytes : int) -> None: ...
    pass
class Standard_Static_Assert_true():
    """
    Static assert -- specialization for condition being true
    """
    def __init__(self) -> None: ...
    @staticmethod
    def assert_ok_s() -> None: 
        """
        None
        """
    pass
class Standard_Persistent(Standard_Transient):
    """
    Root of "persistent" classes, a legacy support of object oriented databases, now outdated.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> Standard_Type: 
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
    def IsInstance(self,theType : Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : Standard_Type) -> bool: ...
    def This(self) -> Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    @property
    def TypeNum(self) -> int:
        """
        None

        :type: int
        """
    @TypeNum.setter
    def TypeNum(self, arg1: int) -> None:
        """
        None
        """
    pass
class Standard_Type(Standard_Transient):
    """
    This class provides legacy interface (type descriptor) to run-time type information (RTTI) for OCCT classes inheriting from Standard_Transient.This class provides legacy interface (type descriptor) to run-time type information (RTTI) for OCCT classes inheriting from Standard_Transient.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> Standard_Type: 
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
    def IsInstance(self,theType : Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : Standard_Type) -> bool: ...
    def Name(self) -> str: 
        """
        Returns the given name of the class type (get_type_name)
        """
    def Parent(self) -> Standard_Type: 
        """
        Returns descriptor of the base class in the hierarchy
        """
    def Print(self,theStream : io.BytesIO) -> None: 
        """
        Prints type (address of descriptor + name) to a stream
        """
    @staticmethod
    def Register_s(theSystemName : str,theName : str,theSize : int,theParent : Standard_Type) -> Standard_Type: 
        """
        Register a type; returns either new or existing descriptor.
        """
    def Size(self) -> int: 
        """
        Returns the size of the class instance in bytes
        """
    @overload
    def SubType(self,theOther : str) -> bool: 
        """
        Returns True if this type is the same as theOther, or inherits from theOther. Note that multiple inheritance is not supported.

        Returns True if this type is the same as theOther, or inherits from theOther. Note that multiple inheritance is not supported.
        """
    @overload
    def SubType(self,theOther : Standard_Type) -> bool: ...
    def SystemName(self) -> str: 
        """
        Returns the system type name of the class (typeinfo.name)
        """
    def This(self) -> Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @staticmethod
    def get_type_descriptor_s() -> Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class Standard_TypeMismatch(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_TypeMismatch' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_TypeMismatch' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Standard_UUID():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Standard_Underflow(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Standard', '__weakref__': <attribute '__weakref__' of 'Standard_Underflow' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Standard_Underflow' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
def ACos(arg0 : float) -> float:
    """
    None
    """
def ACosApprox(arg0 : float) -> float:
    """
    None
    """
def ACosh(arg0 : float) -> float:
    """
    None
    """
def ASin(arg0 : float) -> float:
    """
    None
    """
def ASinh(Value : float) -> float:
    """
    None
    """
def ATan(Value : float) -> float:
    """
    None
    """
def ATan2(arg0 : float,arg1 : float) -> float:
    """
    None
    """
def ATanh(arg0 : float) -> float:
    """
    None
    """
@overload
def Abs(Value : int) -> int:
    """
    None

    None

    None
    """
@overload
def Abs(Value : float) -> float:
    pass
def Ceiling(Value : float) -> float:
    """
    None
    """
def Cos(Value : float) -> float:
    """
    None
    """
def Cosh(arg0 : float) -> float:
    """
    None
    """
def Epsilon(Value : float) -> float:
    """
    None
    """
def Exp(Value : float) -> float:
    """
    None
    """
def Floor(Value : float) -> float:
    """
    None
    """
def HashCodes(theString : str,theLength : int) -> int:
    """
    Returns 32-bit hash code for the first theLen characters in the string theStr. The result is unbound (may be not only positive, but also negative)
    """
def IntToReal(Value : int) -> float:
    """
    None
    """
def IntegerFirst() -> int:
    """
    None
    """
def IntegerLast() -> int:
    """
    None
    """
def IntegerPart(Value : float) -> float:
    """
    None
    """
def IntegerSize() -> int:
    """
    None
    """
def IsAlphabetic(me : str) -> bool:
    """
    None
    """
def IsAlphanumeric(me : str) -> bool:
    """
    None
    """
def IsAnAscii(achar : str) -> bool:
    """
    None
    """
def IsControl(me : str) -> bool:
    """
    None
    """
def IsDigit(me : str) -> bool:
    """
    None
    """
@overload
def IsEqual(Value1 : float,Value2 : float) -> bool:
    """
    Returns Standard_True if two strings are equal

    None

    None

    None

    None

    None

    None

    None

    None
    """
@overload
def IsEqual(theOne : int,theTwo : int) -> bool:
    pass
@overload
def IsEqual(One : capsule,Two : capsule) -> bool:
    pass
@overload
def IsEqual(One : str,Two : str) -> bool:
    pass
@overload
def IsEqual(theOne : str,theTwo : str) -> bool:
    pass
@overload
def IsEqual(One : int,Two : int) -> bool:
    pass
def IsEven(Value : int) -> bool:
    """
    None
    """
def IsGraphic(me : str) -> bool:
    """
    None
    """
def IsLowerCase(me : str) -> bool:
    """
    None
    """
def IsOdd(Value : int) -> bool:
    """
    None
    """
def IsPrintable(me : str) -> bool:
    """
    None
    """
def IsPunctuation(me : str) -> bool:
    """
    None
    """
def IsSpace(me : str) -> bool:
    """
    None
    """
def IsUpperCase(me : str) -> bool:
    """
    None
    """
def IsXDigit(me : str) -> bool:
    """
    None
    """
def Log(arg0 : float) -> float:
    """
    None
    """
def Log10(Value : float) -> float:
    """
    None
    """
def LowerCase(me : str) -> str:
    """
    None
    """
@overload
def Max(Val1 : float,Val2 : float) -> float:
    """
    None

    None

    None
    """
@overload
def Max(Val1 : int,Val2 : int) -> int:
    pass
@overload
def Min(Val1 : float,Val2 : float) -> float:
    """
    None

    None

    None
    """
@overload
def Min(Val1 : int,Val2 : int) -> int:
    pass
def Modulus(Value : int,Divisor : int) -> int:
    """
    None
    """
def NextAfter(arg0 : float,arg1 : float) -> float:
    """
    None
    """
def Pow(Value : float,P : float) -> float:
    """
    None
    """
def RealDigits() -> int:
    """
    None
    """
def RealEpsilon() -> float:
    """
    None
    """
def RealFirst() -> float:
    """
    None
    """
def RealFirst10Exp() -> int:
    """
    None
    """
def RealLast() -> float:
    """
    None
    """
def RealLast10Exp() -> int:
    """
    None
    """
def RealMantissa() -> int:
    """
    None
    """
def RealPart(Value : float) -> float:
    """
    None
    """
def RealRadix() -> int:
    """
    None
    """
def RealSize() -> int:
    """
    None
    """
def RealSmall() -> float:
    """
    None
    """
def RealToInt(theValue : float) -> int:
    """
    None
    """
def RealToShortReal(theVal : float) -> float:
    """
    None
    """
def Round(Value : float) -> float:
    """
    None
    """
def ShortRealDigits() -> int:
    """
    None
    """
def ShortRealEpsilon() -> float:
    """
    None
    """
def ShortRealFirst() -> float:
    """
    None
    """
def ShortRealFirst10Exp() -> int:
    """
    None
    """
def ShortRealLast() -> float:
    """
    None
    """
def ShortRealLast10Exp() -> int:
    """
    None
    """
def ShortRealMantissa() -> int:
    """
    None
    """
def ShortRealRadix() -> int:
    """
    None
    """
def ShortRealSize() -> int:
    """
    None
    """
def ShortRealSmall() -> float:
    """
    None
    """
def Sign(a : float,b : float) -> float:
    """
    Returns |a| if b >= 0; -|a| if b < 0.
    """
def Sin(Value : float) -> float:
    """
    None
    """
def Sinh(arg0 : float) -> float:
    """
    None
    """
def Sqrt(arg0 : float) -> float:
    """
    None
    """
@overload
def Square(Value : int) -> int:
    """
    None

    None
    """
@overload
def Square(Value : float) -> float:
    pass
def Standard_ASSERT_DO_NOTHING() -> None:
    """
    This header file defines a set of ASSERT macros intended for use in algorithms for debugging purposes and as a tool to organise checks for abnormal situations in the uniform way.
    """
def Standard_Atomic_CompareAndSwap(theValue : int,theOldValue : int,theNewValue : int) -> bool:
    """
    Perform an atomic compare and swap. That is, if the current value of *theValue is theOldValue, then write theNewValue into *theValue.

    Perform an atomic compare and swap. That is, if the current value of *theValue is theOldValue, then write theNewValue into *theValue.
    """
def Standard_Atomic_Decrement(theValue : int) -> int:
    """
    Decrements atomically integer variable pointed by theValue and returns resulting decremented value.

    Decrements atomically integer variable pointed by theValue and returns resulting decremented value.
    """
def Standard_Atomic_Increment(theValue : int) -> int:
    """
    Increments atomically integer variable pointed by theValue and returns resulting incremented value.

    Increments atomically integer variable pointed by theValue and returns resulting incremented value.
    """
def Tan(Value : float) -> float:
    """
    None
    """
def Tanh(Value : float) -> float:
    """
    None
    """
def ToCharacter(achar : str) -> str:
    """
    None
    """
def ToExtCharacter(achar : str) -> str:
    """
    None
    """
def UpperCase(me : str) -> str:
    """
    None
    """
Standard_HandlerJumped: OCP.Standard.Standard_HandlerStatus # value = <Standard_HandlerStatus.Standard_HandlerJumped: 1>
Standard_HandlerProcessed: OCP.Standard.Standard_HandlerStatus # value = <Standard_HandlerStatus.Standard_HandlerProcessed: 2>
Standard_HandlerVoid: OCP.Standard.Standard_HandlerStatus # value = <Standard_HandlerStatus.Standard_HandlerVoid: 0>
Standard_JsonKey_CloseChild: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_CloseChild: 2>
Standard_JsonKey_CloseContainer: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_CloseContainer: 4>
Standard_JsonKey_None: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_None: 0>
Standard_JsonKey_OpenChild: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_OpenChild: 1>
Standard_JsonKey_OpenContainer: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_OpenContainer: 3>
Standard_JsonKey_Quote: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_Quote: 5>
Standard_JsonKey_SeparatorKeyToValue: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_SeparatorKeyToValue: 6>
Standard_JsonKey_SeparatorValueToValue: OCP.Standard.Standard_JsonKey # value = <Standard_JsonKey.Standard_JsonKey_SeparatorValueToValue: 7>
