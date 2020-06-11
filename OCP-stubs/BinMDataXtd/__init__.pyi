import OCP.BinMDataXtd
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.Standard
import OCP.BinMDF
import OCP.BinObjMgt
import OCP.Message
import OCP.TColStd
import OCP.TDF
__all__  = [
"BinMDataXtd",
"BinMDataXtd_AxisDriver",
"BinMDataXtd_ConstraintDriver",
"BinMDataXtd_GeometryDriver",
"BinMDataXtd_PatternStdDriver",
"BinMDataXtd_PlacementDriver",
"BinMDataXtd_PlaneDriver",
"BinMDataXtd_PointDriver",
"BinMDataXtd_PositionDriver",
"BinMDataXtd_PresentationDriver",
"BinMDataXtd_ShapeDriver",
"BinMDataXtd_TriangulationDriver"
]
class BinMDataXtd():
    """
    Storage and Retrieval drivers for modelling attributes.
    """
    @staticmethod
    def AddDrivers_s(theDriverTable : OCP.BinMDF.BinMDF_ADriverTable,aMsgDrv : OCP.Message.Message_Messenger) -> None: 
        """
        Adds the attribute drivers to <theDriverTable>.
        """
    @staticmethod
    def DocumentVersion_s() -> int: 
        """
        None
        """
    @staticmethod
    def SetDocumentVersion_s(DocVersion : int) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BinMDataXtd_AxisDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Axis attribute Driver.Axis attribute Driver.Axis attribute Driver.
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
    def Paste(self,Source : OCP.BinObjMgt.BinObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.BinObjMgt.BinObjMgt_Persistent,RelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: ...
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
class BinMDataXtd_ConstraintDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
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
class BinMDataXtd_GeometryDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
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
class BinMDataXtd_PatternStdDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
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
class BinMDataXtd_PlacementDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Placement attribute Driver.Placement attribute Driver.Placement attribute Driver.
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
class BinMDataXtd_PlaneDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Plane attribute Driver.Plane attribute Driver.Plane attribute Driver.
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
    def Paste(self,Source : OCP.BinObjMgt.BinObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.BinObjMgt.BinObjMgt_Persistent,RelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: ...
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
class BinMDataXtd_PointDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Point attribute Driver.Point attribute Driver.Point attribute Driver.
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
    def Paste(self,Source : OCP.BinObjMgt.BinObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.BinObjMgt.BinObjMgt_Persistent,RelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: ...
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
class BinMDataXtd_PositionDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Position Attribute Driver.Position Attribute Driver.Position Attribute Driver.
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
    def Paste(self,Source : OCP.BinObjMgt.BinObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.BinObjMgt.BinObjMgt_Persistent,RelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: ...
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
class BinMDataXtd_PresentationDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Presentation Attribute Driver.Presentation Attribute Driver.Presentation Attribute Driver.
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
    def Paste(self,Source : OCP.BinObjMgt.BinObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.BinObjMgt.BinObjMgt_Persistent,RelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: ...
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
class BinMDataXtd_ShapeDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    Shape attribute Driver.Shape attribute Driver.Shape attribute Driver.
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
    def Paste(self,Source : OCP.BinObjMgt.BinObjMgt_Persistent,Target : OCP.TDF.TDF_Attribute,RelocTable : OCP.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: 
        """
        None

        None
        """
    @overload
    def Paste(self,Source : OCP.TDF.TDF_Attribute,Target : OCP.BinObjMgt.BinObjMgt_Persistent,RelocTable : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: ...
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
class BinMDataXtd_TriangulationDriver(OCP.BinMDF.BinMDF_ADriver, OCP.Standard.Standard_Transient):
    """
    TDataXtd_Triangulation attribute bin Driver.TDataXtd_Triangulation attribute bin Driver.
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
