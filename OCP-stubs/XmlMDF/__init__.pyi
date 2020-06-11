import OCP.XmlMDF
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.XmlObjMgt
import OCP.LDOM
import OCP.TCollection
import OCP.Standard
import OCP.Message
import OCP.TDF
__all__  = [
"XmlMDF",
"XmlMDF_ADriver",
"XmlMDF_ADriverTable",
"XmlMDF_ReferenceDriver",
"XmlMDF_TagSourceDriver"
]
class XmlMDF():
    """
    This package provides classes and methods to translate a transient DF into a persistent one and vice versa.
    """
    @staticmethod
    def AddDrivers_s(aDriverTable : XmlMDF_ADriverTable,theMessageDriver : OCP.Message.Message_Messenger) -> None: 
        """
        Adds the attribute storage drivers to <aDriverSeq>.
        """
    @staticmethod
    @overload
    def FromTo_s(aSource : OCP.LDOM.LDOM_Element,aTarget : OCP.TDF.TDF_Data,aReloc : OCP.XmlObjMgt.XmlObjMgt_RRelocationTable,aDrivers : XmlMDF_ADriverTable) -> bool: 
        """
        Translates a transient <aSource> into a persistent <aTarget>.

        Translates a persistent <aSource> into a transient <aTarget>. Returns True if completed successfully (False on error)
        """
    @staticmethod
    @overload
    def FromTo_s(aSource : OCP.TDF.TDF_Data,aTarget : OCP.LDOM.LDOM_Element,aReloc : OCP.XmlObjMgt.XmlObjMgt_SRelocationTable,aDrivers : XmlMDF_ADriverTable) -> None: ...
    def __init__(self) -> None: ...
    pass
class XmlMDF_ADriver(OCP.Standard.Standard_Transient):
    """
    Attribute Storage/Retrieval Driver.Attribute Storage/Retrieval Driver.Attribute Storage/Retrieval Driver.
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
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Creates a new attribute from TDF.
        """
    @overload
    def Paste(self,aSource : OCP.XmlObjMgt.XmlObjMgt_Persistent,aTarget : OCP.TDF.TDF_Attribute,aRelocTable : OCP.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: 
        """
        Translate the contents of <aSource> and put it into <aTarget>, using the relocation table <aRelocTable> to keep the sharings.

        Translate the contents of <aSource> and put it into <aTarget>, using the relocation table <aRelocTable> to keep the sharings.
        """
    @overload
    def Paste(self,aSource : OCP.TDF.TDF_Attribute,aTarget : OCP.XmlObjMgt.XmlObjMgt_Persistent,aRelocTable : OCP.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...
    def SourceType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the type of source object, inheriting from Attribute from TDF.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the full XML tag name (including NS prefix)
        """
    def VersionNumber(self) -> int: 
        """
        Returns the version number from which the driver is available.
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
class XmlMDF_ADriverTable(OCP.Standard.Standard_Transient):
    """
    A driver table is an object building links between object types and object drivers. In the translation process, a driver table is asked to give a translation driver for each current object to be translated.A driver table is an object building links between object types and object drivers. In the translation process, a driver table is asked to give a translation driver for each current object to be translated.A driver table is an object building links between object types and object drivers. In the translation process, a driver table is asked to give a translation driver for each current object to be translated.
    """
    def AddDriver(self,anHDriver : XmlMDF_ADriver) -> None: 
        """
        Sets a translation driver: <aDriver>.
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
    def GetDriver(self,aType : OCP.Standard.Standard_Type,anHDriver : XmlMDF_ADriver) -> bool: 
        """
        Gets a driver <aDriver> according to <aType>
        """
    def GetDrivers(self) -> Any: 
        """
        Gets a map of drivers.
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
class XmlMDF_ReferenceDriver(XmlMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Attribute Driver.Attribute Driver.Attribute Driver.
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
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    @overload
    def Paste(self,Source : OCP.XmlObjMgt.XmlObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.XmlObjMgt.XmlObjMgt_Persistent,RelocTable : OCP.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...
    def SourceType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the type of source object, inheriting from Attribute from TDF.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the full XML tag name (including NS prefix)
        """
    def VersionNumber(self) -> int: 
        """
        Returns the version number from which the driver is available.
        """
    def __init__(self,theMessageDriver : OCP.Message.Message_Messenger) -> None: ...
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
class XmlMDF_TagSourceDriver(XmlMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Attribute Driver.Attribute Driver.Attribute Driver.
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
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.XmlObjMgt.XmlObjMgt_Persistent,RelocTable : OCP.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.XmlObjMgt.XmlObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...
    def SourceType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the type of source object, inheriting from Attribute from TDF.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the full XML tag name (including NS prefix)
        """
    def VersionNumber(self) -> int: 
        """
        Returns the version number from which the driver is available.
        """
    def __init__(self,theMessageDriver : OCP.Message.Message_Messenger) -> None: ...
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
