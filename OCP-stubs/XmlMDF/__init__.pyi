import OCP.XmlMDF
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.LDOM
import OCP.XmlObjMgt
import OCP.TCollection
import OCP.Message
import OCP.Standard
__all__  = [
"XmlMDF",
"XmlMDF_ADriver",
"XmlMDF_ADriverTable",
"XmlMDF_DerivedDriver",
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
    def FromTo_s(aSource : OCP.LDOM.LDOM_Element,aTarget : OCP.TDF.TDF_Data,aReloc : OCP.XmlObjMgt.XmlObjMgt_RRelocationTable,aDrivers : XmlMDF_ADriverTable,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Translates a transient <aSource> into a persistent <aTarget>.

        Translates a persistent <aSource> into a transient <aTarget>. Returns True if completed successfully (False on error)
        """
    @staticmethod
    @overload
    def FromTo_s(aSource : OCP.TDF.TDF_Data,aTarget : OCP.LDOM.LDOM_Element,aReloc : OCP.XmlObjMgt.XmlObjMgt_SRelocationTable,aDrivers : XmlMDF_ADriverTable,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
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
        Returns the current message driver of this driver
        """
    def Namespace(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the namespace string
        """
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
    @overload
    def AddDerivedDriver(self,theInstance : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds a translation driver for the derived attribute. The base driver must be already added.

        Adds a translation driver for the derived attribute. The base driver must be already added.
        """
    @overload
    def AddDerivedDriver(self,theDerivedType : str) -> OCP.Standard.Standard_Type: ...
    def AddDriver(self,anHDriver : XmlMDF_ADriver) -> None: 
        """
        Sets a translation driver: <aDriver>.
        """
    def CreateDrvMap(self,theDriverMap : Any) -> None: 
        """
        Fills the map by all registered drivers.
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
    def GetDriver(self,theType : OCP.Standard.Standard_Type,theDriver : XmlMDF_ADriver) -> bool: 
        """
        Gets a driver <aDriver> according to <aType>
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
class XmlMDF_DerivedDriver(XmlMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    A universal driver for the attribute that inherits another attribute with ready to used persistence mechanism implemented (already has a driver to store/retrieve).
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
    def MessageDriver(self) -> OCP.Message.Message_Messenger: 
        """
        Returns the current message driver of this driver
        """
    def Namespace(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the namespace string
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Creates a new instance of the derivative attribute
        """
    @overload
    def Paste(self,theSource : OCP.TDF.TDF_Attribute,theTarget : OCP.XmlObjMgt.XmlObjMgt_Persistent,theRelocTable : OCP.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: 
        """
        Reuses the base driver to read the base fields

        Reuses the base driver to store the base fields
        """
    @overload
    def Paste(self,theSource : OCP.XmlObjMgt.XmlObjMgt_Persistent,theTarget : OCP.TDF.TDF_Attribute,theRelocTable : OCP.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...
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
    def __init__(self,theDerivative : OCP.TDF.TDF_Attribute,theBaseDriver : XmlMDF_ADriver) -> None: ...
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
        Returns the current message driver of this driver
        """
    def Namespace(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the namespace string
        """
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
        Returns the current message driver of this driver
        """
    def Namespace(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the namespace string
        """
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
