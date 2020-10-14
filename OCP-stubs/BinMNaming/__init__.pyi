import OCP.BinMNaming
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.TCollection
import OCP.TColStd
import OCP.Message
import OCP.Standard
import OCP.BinObjMgt
import OCP.BinMDF
import OCP.BinTools
__all__  = [
"BinMNaming",
"BinMNaming_NamedShapeDriver",
"BinMNaming_NamingDriver"
]
class BinMNaming():
    """
    Storage/Retrieval drivers for TNaming attributes
    """
    @staticmethod
    def AddDrivers_s(theDriverTable : OCP.BinMDF.BinMDF_ADriverTable,aMsgDrv : OCP.Message.Message_Messenger) -> None: 
        """
        Adds the attribute drivers to <theDriverTable>.
        """
    def __init__(self) -> None: ...
    pass
class BinMNaming_NamedShapeDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    NamedShape Attribute Driver.NamedShape Attribute Driver.NamedShape Attribute Driver.
    """
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
    def GetFormatNb(self) -> int: 
        """
        get the format of topology

        get the format of topology
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShapesLocations(self) -> OCP.BinTools.BinTools_LocationSet: 
        """
        get the format of topology

        get the format of topology
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
    def IsWithTriangles(self) -> bool: 
        """
        Return true if shape should be stored with triangles.
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
    def ReadShapeSection(self,theIS : Any) -> None: 
        """
        Input the shapes from Bin Document file
        """
    @overload
    def SetFormatNb(self,theFormat : int) -> None: 
        """
        set the format of topology First : does not write CurveOnSurface UV Points into the file on reading calls Check() method. Second: stores CurveOnSurface UV Points.

        set the format of topology First : does not write CurveOnSurface UV Points into the file on reading calls Check() method. Second: stores CurveOnSurface UV Points.
        """
    @overload
    def SetFormatNb(self,theFormatNb : int) -> None: ...
    def SetWithTriangles(self,isWithTriangles : bool) -> None: 
        """
        set whether to store triangulation

        set whether to store triangulation
        """
    def SourceType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the type of source object, inheriting from Attribute from TDF.

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
    def WriteShapeSection(self,theOS : Any) -> None: 
        """
        Output the shapes into Bin Document file
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
class BinMNaming_NamingDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Naming Attribute Driver.Naming Attribute Driver.Naming Attribute Driver.
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
