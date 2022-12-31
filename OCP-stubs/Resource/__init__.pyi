import OCP.Resource
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import io
import OCP.TCollection
import OCP.NCollection
import OCP.Standard
__all__  = [
"Resource_DataMapOfAsciiStringAsciiString",
"Resource_DataMapOfAsciiStringExtendedString",
"Resource_FormatType",
"Resource_LexicalCompare",
"Resource_Manager",
"Resource_Unicode",
"Resource_ANSI",
"Resource_EUC",
"Resource_FormatType_ANSI",
"Resource_FormatType_Big5",
"Resource_FormatType_CP1250",
"Resource_FormatType_CP1251",
"Resource_FormatType_CP1252",
"Resource_FormatType_CP1253",
"Resource_FormatType_CP1254",
"Resource_FormatType_CP1255",
"Resource_FormatType_CP1256",
"Resource_FormatType_CP1257",
"Resource_FormatType_CP1258",
"Resource_FormatType_CP850",
"Resource_FormatType_EUC",
"Resource_FormatType_GB",
"Resource_FormatType_GBK",
"Resource_FormatType_NoConversion",
"Resource_FormatType_SJIS",
"Resource_FormatType_SystemLocale",
"Resource_FormatType_UTF8",
"Resource_FormatType_iso8859_1",
"Resource_FormatType_iso8859_2",
"Resource_FormatType_iso8859_3",
"Resource_FormatType_iso8859_4",
"Resource_FormatType_iso8859_5",
"Resource_FormatType_iso8859_6",
"Resource_FormatType_iso8859_7",
"Resource_FormatType_iso8859_8",
"Resource_FormatType_iso8859_9",
"Resource_GB",
"Resource_SJIS"
]
class Resource_DataMapOfAsciiStringAsciiString(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Resource_DataMapOfAsciiStringAsciiString) -> Resource_DataMapOfAsciiStringAsciiString: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
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
    def Exchange(self,theOther : Resource_DataMapOfAsciiStringAsciiString) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString,theValue : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
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
    def Seek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
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
    def UnBind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : Resource_DataMapOfAsciiStringAsciiString) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Resource_DataMapOfAsciiStringExtendedString(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Resource_DataMapOfAsciiStringExtendedString) -> Resource_DataMapOfAsciiStringExtendedString: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def Exchange(self,theOther : Resource_DataMapOfAsciiStringExtendedString) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString,theValue : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
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
    def Seek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_ExtendedString: 
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
    def UnBind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : Resource_DataMapOfAsciiStringExtendedString) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Resource_FormatType():
    """
    List of non ASCII format types which may be converted into the Unicode 16 bits format type. Use the functions provided by the Resource_Unicode class to convert a string from one of these non ASCII format to Unicode, and vice versa.

    Members:

      Resource_FormatType_SJIS

      Resource_FormatType_EUC

      Resource_FormatType_NoConversion

      Resource_FormatType_GB

      Resource_FormatType_UTF8

      Resource_FormatType_SystemLocale

      Resource_FormatType_CP1250

      Resource_FormatType_CP1251

      Resource_FormatType_CP1252

      Resource_FormatType_CP1253

      Resource_FormatType_CP1254

      Resource_FormatType_CP1255

      Resource_FormatType_CP1256

      Resource_FormatType_CP1257

      Resource_FormatType_CP1258

      Resource_FormatType_iso8859_1

      Resource_FormatType_iso8859_2

      Resource_FormatType_iso8859_3

      Resource_FormatType_iso8859_4

      Resource_FormatType_iso8859_5

      Resource_FormatType_iso8859_6

      Resource_FormatType_iso8859_7

      Resource_FormatType_iso8859_8

      Resource_FormatType_iso8859_9

      Resource_FormatType_CP850

      Resource_FormatType_GBK

      Resource_FormatType_Big5

      Resource_FormatType_ANSI

      Resource_SJIS

      Resource_EUC

      Resource_ANSI

      Resource_GB
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
    Resource_ANSI: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_NoConversion: 2>
    Resource_EUC: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_EUC: 1>
    Resource_FormatType_ANSI: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_NoConversion: 2>
    Resource_FormatType_Big5: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_Big5: 26>
    Resource_FormatType_CP1250: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1250: 6>
    Resource_FormatType_CP1251: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1251: 7>
    Resource_FormatType_CP1252: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1252: 8>
    Resource_FormatType_CP1253: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1253: 9>
    Resource_FormatType_CP1254: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1254: 10>
    Resource_FormatType_CP1255: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1255: 11>
    Resource_FormatType_CP1256: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1256: 12>
    Resource_FormatType_CP1257: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1257: 13>
    Resource_FormatType_CP1258: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1258: 14>
    Resource_FormatType_CP850: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP850: 24>
    Resource_FormatType_EUC: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_EUC: 1>
    Resource_FormatType_GB: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_GB: 3>
    Resource_FormatType_GBK: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_GBK: 25>
    Resource_FormatType_NoConversion: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_NoConversion: 2>
    Resource_FormatType_SJIS: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_SJIS: 0>
    Resource_FormatType_SystemLocale: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_SystemLocale: 5>
    Resource_FormatType_UTF8: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_UTF8: 4>
    Resource_FormatType_iso8859_1: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_1: 15>
    Resource_FormatType_iso8859_2: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_2: 16>
    Resource_FormatType_iso8859_3: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_3: 17>
    Resource_FormatType_iso8859_4: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_4: 18>
    Resource_FormatType_iso8859_5: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_5: 19>
    Resource_FormatType_iso8859_6: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_6: 20>
    Resource_FormatType_iso8859_7: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_7: 21>
    Resource_FormatType_iso8859_8: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_8: 22>
    Resource_FormatType_iso8859_9: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_9: 23>
    Resource_GB: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_GB: 3>
    Resource_SJIS: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_SJIS: 0>
    __entries: dict # value = {'Resource_FormatType_SJIS': (<Resource_FormatType.Resource_FormatType_SJIS: 0>, None), 'Resource_FormatType_EUC': (<Resource_FormatType.Resource_FormatType_EUC: 1>, None), 'Resource_FormatType_NoConversion': (<Resource_FormatType.Resource_FormatType_NoConversion: 2>, None), 'Resource_FormatType_GB': (<Resource_FormatType.Resource_FormatType_GB: 3>, None), 'Resource_FormatType_UTF8': (<Resource_FormatType.Resource_FormatType_UTF8: 4>, None), 'Resource_FormatType_SystemLocale': (<Resource_FormatType.Resource_FormatType_SystemLocale: 5>, None), 'Resource_FormatType_CP1250': (<Resource_FormatType.Resource_FormatType_CP1250: 6>, None), 'Resource_FormatType_CP1251': (<Resource_FormatType.Resource_FormatType_CP1251: 7>, None), 'Resource_FormatType_CP1252': (<Resource_FormatType.Resource_FormatType_CP1252: 8>, None), 'Resource_FormatType_CP1253': (<Resource_FormatType.Resource_FormatType_CP1253: 9>, None), 'Resource_FormatType_CP1254': (<Resource_FormatType.Resource_FormatType_CP1254: 10>, None), 'Resource_FormatType_CP1255': (<Resource_FormatType.Resource_FormatType_CP1255: 11>, None), 'Resource_FormatType_CP1256': (<Resource_FormatType.Resource_FormatType_CP1256: 12>, None), 'Resource_FormatType_CP1257': (<Resource_FormatType.Resource_FormatType_CP1257: 13>, None), 'Resource_FormatType_CP1258': (<Resource_FormatType.Resource_FormatType_CP1258: 14>, None), 'Resource_FormatType_iso8859_1': (<Resource_FormatType.Resource_FormatType_iso8859_1: 15>, None), 'Resource_FormatType_iso8859_2': (<Resource_FormatType.Resource_FormatType_iso8859_2: 16>, None), 'Resource_FormatType_iso8859_3': (<Resource_FormatType.Resource_FormatType_iso8859_3: 17>, None), 'Resource_FormatType_iso8859_4': (<Resource_FormatType.Resource_FormatType_iso8859_4: 18>, None), 'Resource_FormatType_iso8859_5': (<Resource_FormatType.Resource_FormatType_iso8859_5: 19>, None), 'Resource_FormatType_iso8859_6': (<Resource_FormatType.Resource_FormatType_iso8859_6: 20>, None), 'Resource_FormatType_iso8859_7': (<Resource_FormatType.Resource_FormatType_iso8859_7: 21>, None), 'Resource_FormatType_iso8859_8': (<Resource_FormatType.Resource_FormatType_iso8859_8: 22>, None), 'Resource_FormatType_iso8859_9': (<Resource_FormatType.Resource_FormatType_iso8859_9: 23>, None), 'Resource_FormatType_CP850': (<Resource_FormatType.Resource_FormatType_CP850: 24>, None), 'Resource_FormatType_GBK': (<Resource_FormatType.Resource_FormatType_GBK: 25>, None), 'Resource_FormatType_Big5': (<Resource_FormatType.Resource_FormatType_Big5: 26>, None), 'Resource_FormatType_ANSI': (<Resource_FormatType.Resource_FormatType_NoConversion: 2>, None), 'Resource_SJIS': (<Resource_FormatType.Resource_FormatType_SJIS: 0>, None), 'Resource_EUC': (<Resource_FormatType.Resource_FormatType_EUC: 1>, None), 'Resource_ANSI': (<Resource_FormatType.Resource_FormatType_NoConversion: 2>, None), 'Resource_GB': (<Resource_FormatType.Resource_FormatType_GB: 3>, None)}
    __members__: dict # value = {'Resource_FormatType_SJIS': <Resource_FormatType.Resource_FormatType_SJIS: 0>, 'Resource_FormatType_EUC': <Resource_FormatType.Resource_FormatType_EUC: 1>, 'Resource_FormatType_NoConversion': <Resource_FormatType.Resource_FormatType_NoConversion: 2>, 'Resource_FormatType_GB': <Resource_FormatType.Resource_FormatType_GB: 3>, 'Resource_FormatType_UTF8': <Resource_FormatType.Resource_FormatType_UTF8: 4>, 'Resource_FormatType_SystemLocale': <Resource_FormatType.Resource_FormatType_SystemLocale: 5>, 'Resource_FormatType_CP1250': <Resource_FormatType.Resource_FormatType_CP1250: 6>, 'Resource_FormatType_CP1251': <Resource_FormatType.Resource_FormatType_CP1251: 7>, 'Resource_FormatType_CP1252': <Resource_FormatType.Resource_FormatType_CP1252: 8>, 'Resource_FormatType_CP1253': <Resource_FormatType.Resource_FormatType_CP1253: 9>, 'Resource_FormatType_CP1254': <Resource_FormatType.Resource_FormatType_CP1254: 10>, 'Resource_FormatType_CP1255': <Resource_FormatType.Resource_FormatType_CP1255: 11>, 'Resource_FormatType_CP1256': <Resource_FormatType.Resource_FormatType_CP1256: 12>, 'Resource_FormatType_CP1257': <Resource_FormatType.Resource_FormatType_CP1257: 13>, 'Resource_FormatType_CP1258': <Resource_FormatType.Resource_FormatType_CP1258: 14>, 'Resource_FormatType_iso8859_1': <Resource_FormatType.Resource_FormatType_iso8859_1: 15>, 'Resource_FormatType_iso8859_2': <Resource_FormatType.Resource_FormatType_iso8859_2: 16>, 'Resource_FormatType_iso8859_3': <Resource_FormatType.Resource_FormatType_iso8859_3: 17>, 'Resource_FormatType_iso8859_4': <Resource_FormatType.Resource_FormatType_iso8859_4: 18>, 'Resource_FormatType_iso8859_5': <Resource_FormatType.Resource_FormatType_iso8859_5: 19>, 'Resource_FormatType_iso8859_6': <Resource_FormatType.Resource_FormatType_iso8859_6: 20>, 'Resource_FormatType_iso8859_7': <Resource_FormatType.Resource_FormatType_iso8859_7: 21>, 'Resource_FormatType_iso8859_8': <Resource_FormatType.Resource_FormatType_iso8859_8: 22>, 'Resource_FormatType_iso8859_9': <Resource_FormatType.Resource_FormatType_iso8859_9: 23>, 'Resource_FormatType_CP850': <Resource_FormatType.Resource_FormatType_CP850: 24>, 'Resource_FormatType_GBK': <Resource_FormatType.Resource_FormatType_GBK: 25>, 'Resource_FormatType_Big5': <Resource_FormatType.Resource_FormatType_Big5: 26>, 'Resource_FormatType_ANSI': <Resource_FormatType.Resource_FormatType_NoConversion: 2>, 'Resource_SJIS': <Resource_FormatType.Resource_FormatType_SJIS: 0>, 'Resource_EUC': <Resource_FormatType.Resource_FormatType_EUC: 1>, 'Resource_ANSI': <Resource_FormatType.Resource_FormatType_NoConversion: 2>, 'Resource_GB': <Resource_FormatType.Resource_FormatType_GB: 3>}
    pass
class Resource_LexicalCompare():
    """
    None
    """
    def IsLower(self,Left : OCP.TCollection.TCollection_AsciiString,Right : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Returns True if <Left> is lower than <Right>.
        """
    def __init__(self) -> None: ...
    pass
class Resource_Manager(OCP.Standard.Standard_Transient):
    """
    Defines a resource structure and its management methods.Defines a resource structure and its management methods.Defines a resource structure and its management methods.
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
    def ExtValue(self,aResourceName : str) -> str: 
        """
        Gets the value of an ExtString resource according to its instance and its type.
        """
    @overload
    def Find(self,theResource : OCP.TCollection.TCollection_AsciiString,theValue : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        returns True if the Resource does exist.

        returns True if the Resource does exist.
        """
    @overload
    def Find(self,aResource : str) -> bool: ...
    def GetMap(self,theRefMap : bool=True) -> Resource_DataMapOfAsciiStringAsciiString: 
        """
        Returns internal Ref or User map with parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def GetResourcePath_s(aPath : OCP.TCollection.TCollection_AsciiString,aName : str,isUserDefaults : bool) -> None: 
        """
        Gets the resource file full path by its name. If corresponding environment variable is not set or file doesn't exist returns empty string.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Integer(self,aResourceName : str) -> int: 
        """
        Gets the value of an integer resource according to its instance and its type.
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
    def Real(self,aResourceName : str) -> float: 
        """
        Gets the value of a real resource according to its instance and its type.
        """
    def Save(self) -> bool: 
        """
        Save the user resource structure in the specified file. Creates the file if it does not exist.
        """
    @overload
    def SetResource(self,aResourceName : str,aValue : float) -> None: 
        """
        Sets the new value of an integer resource. If the resource does not exist, it is created.

        Sets the new value of a real resource. If the resource does not exist, it is created.

        Sets the new value of an CString resource. If the resource does not exist, it is created.

        Sets the new value of an ExtString resource. If the resource does not exist, it is created.
        """
    @overload
    def SetResource(self,aResourceName : str,aValue : int) -> None: ...
    @overload
    def SetResource(self,aResourceName : str,aValue : str) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,aResourceName : str) -> str: 
        """
        Gets the value of a CString resource according to its instance and its type.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theName : OCP.TCollection.TCollection_AsciiString,theDefaultsDirectory : OCP.TCollection.TCollection_AsciiString,theUserDefaultsDirectory : OCP.TCollection.TCollection_AsciiString,theIsVerbose : bool=False) -> None: ...
    @overload
    def __init__(self,aName : str,Verbose : bool=False) -> None: ...
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
class Resource_Unicode():
    """
    This class provides functions used to convert a non-ASCII C string given in ANSI, EUC, GB or SJIS format, to a Unicode string of extended characters, and vice versa.
    """
    @staticmethod
    def ConvertBig5ToUnicode_s(fromstr : str,tostr : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Converts non-ASCII CString <fromstr> in Big5 format to Unicode ExtendedString <tostr>.
        """
    @staticmethod
    def ConvertEUCToUnicode_s(fromstr : str,tostr : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Converts non-ASCII CString <fromstr> in EUC format to Unicode ExtendedString <tostr>.
        """
    @staticmethod
    @overload
    def ConvertFormatToUnicode_s(theFromStr : str,theToStr : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Converts the non-ASCII C string (as specified by GetFormat()) to the Unicode string of extended characters.

        Converts the non-ASCII C string in specified format to the Unicode string of extended characters.
        """
    @staticmethod
    @overload
    def ConvertFormatToUnicode_s(theFormat : Resource_FormatType,theFromStr : str,theToStr : OCP.TCollection.TCollection_ExtendedString) -> None: ...
    @staticmethod
    def ConvertGBKToUnicode_s(fromstr : str,tostr : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Converts non-ASCII CString <fromstr> in GBK format to Unicode ExtendedString <tostr>.
        """
    @staticmethod
    def ConvertGBToUnicode_s(fromstr : str,tostr : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Converts non-ASCII CString <fromstr> in GB format to Unicode ExtendedString <tostr>.
        """
    @staticmethod
    def ConvertSJISToUnicode_s(fromstr : str,tostr : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Converts non-ASCII CString <fromstr> in SJIS format to Unicode ExtendedString <tostr>.
        """
    @staticmethod
    def GetFormat_s() -> Resource_FormatType: 
        """
        Returns the current conversion format (either ANSI, EUC, GB or SJIS). The current converting format must be defined in advance with the SetFormat function.
        """
    @staticmethod
    def ReadFormat_s() -> None: 
        """
        Reads converting format from resource "FormatType" in Resource Manager "CharSet"
        """
    @staticmethod
    def SetFormat_s(typecode : Resource_FormatType) -> None: 
        """
        Defines the current conversion format as typecode. This conversion format will then be used by the functions ConvertFormatToUnicode and ConvertUnicodeToFormat to convert the strings.
        """
    def __init__(self) -> None: ...
    pass
Resource_ANSI: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_NoConversion: 2>
Resource_EUC: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_EUC: 1>
Resource_FormatType_ANSI: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_NoConversion: 2>
Resource_FormatType_Big5: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_Big5: 26>
Resource_FormatType_CP1250: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1250: 6>
Resource_FormatType_CP1251: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1251: 7>
Resource_FormatType_CP1252: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1252: 8>
Resource_FormatType_CP1253: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1253: 9>
Resource_FormatType_CP1254: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1254: 10>
Resource_FormatType_CP1255: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1255: 11>
Resource_FormatType_CP1256: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1256: 12>
Resource_FormatType_CP1257: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1257: 13>
Resource_FormatType_CP1258: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP1258: 14>
Resource_FormatType_CP850: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_CP850: 24>
Resource_FormatType_EUC: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_EUC: 1>
Resource_FormatType_GB: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_GB: 3>
Resource_FormatType_GBK: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_GBK: 25>
Resource_FormatType_NoConversion: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_NoConversion: 2>
Resource_FormatType_SJIS: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_SJIS: 0>
Resource_FormatType_SystemLocale: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_SystemLocale: 5>
Resource_FormatType_UTF8: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_UTF8: 4>
Resource_FormatType_iso8859_1: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_1: 15>
Resource_FormatType_iso8859_2: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_2: 16>
Resource_FormatType_iso8859_3: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_3: 17>
Resource_FormatType_iso8859_4: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_4: 18>
Resource_FormatType_iso8859_5: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_5: 19>
Resource_FormatType_iso8859_6: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_6: 20>
Resource_FormatType_iso8859_7: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_7: 21>
Resource_FormatType_iso8859_8: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_8: 22>
Resource_FormatType_iso8859_9: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_iso8859_9: 23>
Resource_GB: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_GB: 3>
Resource_SJIS: OCP.Resource.Resource_FormatType # value = <Resource_FormatType.Resource_FormatType_SJIS: 0>
