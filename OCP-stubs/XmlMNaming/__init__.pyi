import OCP.XmlMNaming
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.TopTools
import OCP.LDOM
import OCP.TDocStd
import OCP.Standard
import OCP.TopAbs
import OCP.XmlObjMgt
import OCP.Message
import OCP.TopoDS
import OCP.TCollection
import OCP.XmlMDF
__all__  = [
"XmlMNaming",
"XmlMNaming_NamedShapeDriver",
"XmlMNaming_NamingDriver",
"XmlMNaming_Shape1"
]
class XmlMNaming():
    """
    None
    """
    @staticmethod
    def AddDrivers_s(aDriverTable : OCP.XmlMDF.XmlMDF_ADriverTable,aMessageDriver : OCP.Message.Message_Messenger) -> None: 
        """
        Adds the attribute drivers to <aDriverTable>.
        """
    def __init__(self) -> None: ...
    pass
class XmlMNaming_NamedShapeDriver(OCP.XmlMDF.XmlMDF_ADriver, OCP.Standard.Standard_Transient):
    def Clear(self) -> None: 
        """
        Clear myShapeSet
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
    def GetShapesLocations(self) -> OCP.TopTools.TopTools_LocationSet: 
        """
        get the format of topology

        get the format of topology
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
    def Paste(self,theSource : OCP.TDF.TDF_Attribute,theTarget : OCP.XmlObjMgt.XmlObjMgt_Persistent,theRelocTable : OCP.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: 
        """
        None

        None
        """
    @overload
    def Paste(self,theSource : OCP.XmlObjMgt.XmlObjMgt_Persistent,theTarget : OCP.TDF.TDF_Attribute,theRelocTable : OCP.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...
    def ReadShapeSection(self,anElement : OCP.LDOM.LDOM_Element,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Input the shapes from DOM element
        """
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
    def WriteShapeSection(self,anElement : OCP.LDOM.LDOM_Element,theStorageFormatVersion : OCP.TDocStd.TDocStd_FormatVersion,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Output the shapes into DOM element
        """
    def __init__(self,aMessageDriver : OCP.Message.Message_Messenger) -> None: ...
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
class XmlMNaming_NamingDriver(OCP.XmlMDF.XmlMDF_ADriver, OCP.Standard.Standard_Transient):
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def Paste(self,theSource : OCP.TDF.TDF_Attribute,theTarget : OCP.XmlObjMgt.XmlObjMgt_Persistent,theRelocTable : OCP.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: 
        """
        None

        None
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
    def __init__(self,aMessageDriver : OCP.Message.Message_Messenger) -> None: ...
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
class XmlMNaming_Shape1():
    """
    The XmlMNaming_Shape1 is the Persistent view of a TopoDS_Shape.
    """
    def Element(self) -> OCP.LDOM.LDOM_Element: 
        """
        return myElement

        return myElement
        """
    def LocId(self) -> int: 
        """
        None
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def SetShape(self,ID : int,LocID : int,Orient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        None
        """
    def SetVertex(self,theVertex : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def TShapeId(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self,E : OCP.LDOM.LDOM_Element) -> None: ...
    @overload
    def __init__(self,Doc : OCP.LDOM.LDOM_Document) -> None: ...
    pass
