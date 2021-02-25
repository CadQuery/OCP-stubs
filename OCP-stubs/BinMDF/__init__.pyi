import OCP.BinMDF
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.TColStd
import OCP.TCollection
import OCP.BinObjMgt
import OCP.Message
import OCP.Standard
__all__  = [
"BinMDF",
"BinMDF_ADriver",
"BinMDF_ADriverTable",
"BinMDF_DerivedDriver",
"BinMDF_ReferenceDriver",
"BinMDF_TagSourceDriver"
]
class BinMDF():
    """
    This package provides classes and methods to translate a transient DF into a persistent one and vice versa.
    """
    @staticmethod
    def AddDrivers_s(aDriverTable : BinMDF_ADriverTable,aMsgDrv : OCP.Message.Message_Messenger) -> None: 
        """
        Adds the attribute storage drivers to <aDriverTable>.
        """
    def __init__(self) -> None: ...
    pass
class BinMDF_ADriver(OCP.Standard.Standard_Transient):
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
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Creates a new attribute from TDF.
        """
    @overload
    def Paste(self,aSource : OCP.BinObjMgt.BinObjMgt_Persistent,aTarget : OCP.TDF.TDF_Attribute,aRelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: 
        """
        Translate the contents of <aSource> and put it into <aTarget>, using the relocation table <aRelocTable> to keep the sharings.

        Translate the contents of <aSource> and put it into <aTarget>, using the relocation table <aRelocTable> to keep the sharings.
        """
    @overload
    def Paste(self,aSource : OCP.TDF.TDF_Attribute,aTarget : OCP.BinObjMgt.BinObjMgt_Persistent,aRelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: ...
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
        Returns the type name of the attribute object

        Returns the type name of the attribute object
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
class BinMDF_ADriverTable(OCP.Standard.Standard_Transient):
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
    def AddDriver(self,theDriver : BinMDF_ADriver) -> None: 
        """
        Adds a translation driver <theDriver>.
        """
    @overload
    def AssignIds(self,theTypeNames : OCP.TColStd.TColStd_SequenceOfAsciiString) -> None: 
        """
        Assigns the IDs to the drivers of the given Types. It uses indices in the map as IDs. Useful in storage procedure.

        Assigns the IDs to the drivers of the given Type Names; It uses indices in the sequence as IDs. Useful in retrieval procedure.
        """
    @overload
    def AssignIds(self,theTypes : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: ...
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
    @overload
    def GetDriver(self,theType : OCP.Standard.Standard_Type,theDriver : BinMDF_ADriver) -> int: 
        """
        Gets a driver <theDriver> according to <theType>. Returns Type ID if the driver was assigned an ID; 0 otherwise.

        Returns a driver according to <theTypeId>. Returns null handle if a driver is not found

        Gets a driver <theDriver> according to <theType>. Returns Type ID if the driver was assigned an ID; 0 otherwise.

        Returns a driver according to <theTypeId>. Returns null handle if a driver is not found
        """
    @overload
    def GetDriver(self,theTypeId : int) -> BinMDF_ADriver: ...
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
class BinMDF_DerivedDriver(BinMDF_ADriver, OCP.Standard.Standard_Transient):
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
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Creates a new instance of the derivative attribute
        """
    @overload
    def Paste(self,theSource : OCP.TDF.TDF_Attribute,theTarget : OCP.BinObjMgt.BinObjMgt_Persistent,theRelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: 
        """
        Reuses the base driver to read the base fields

        Reuses the base driver to store the base fields
        """
    @overload
    def Paste(self,theSource : OCP.BinObjMgt.BinObjMgt_Persistent,theTarget : OCP.TDF.TDF_Attribute,theRelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...
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
        Returns the type name of the attribute object

        Returns the type name of the attribute object
        """
    def __init__(self,theDerivative : OCP.TDF.TDF_Attribute,theBaseDriver : BinMDF_ADriver) -> None: ...
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
class BinMDF_ReferenceDriver(BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Reference attribute Driver.Reference attribute Driver.Reference attribute Driver.
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
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.BinObjMgt.BinObjMgt_Persistent,RelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.BinObjMgt.BinObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...
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
        Returns the type name of the attribute object

        Returns the type name of the attribute object
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
class BinMDF_TagSourceDriver(BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    TDF_TagSource Driver.TDF_TagSource Driver.TDF_TagSource Driver.
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
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.BinObjMgt.BinObjMgt_Persistent,RelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.BinObjMgt.BinObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...
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
        Returns the type name of the attribute object

        Returns the type name of the attribute object
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
