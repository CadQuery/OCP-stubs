import OCP.XmlMDocStd
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.XmlMDF
import OCP.TCollection
import OCP.XmlObjMgt
import OCP.Standard
import OCP.Message
import OCP.TDF
__all__  = [
"XmlMDocStd",
"XmlMDocStd_XLinkDriver"
]
class XmlMDocStd():
    """
    Driver for TDocStd_XLink
    """
    @staticmethod
    def AddDrivers_s(aDriverTable : OCP.XmlMDF.XmlMDF_ADriverTable,theMessageDriver : OCP.Message.Message_Messenger) -> None: 
        """
        Adds the attribute drivers to <aDriverTable>.
        """
    def __init__(self) -> None: ...
    pass
class XmlMDocStd_XLinkDriver(OCP.XmlMDF.XmlMDF_ADriver, OCP.Standard.Standard_Transient):
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
