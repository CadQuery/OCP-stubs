import OCP.StdPersistent
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
import OCP.TopLoc
import OCP.StdObjMgt
import OCP.TDataXtd
import OCP.StdObject
__all__  = [
"StdPersistent",
"StdPersistent_DataXtd",
"StdPersistent_DataXtd_Constraint",
"StdPersistent_DataXtd_PatternStd",
"StdPersistent_HArray1",
"StdPersistent_HArray1OfShape1",
"StdPersistent_Naming",
"StdPersistent_PPrsStd",
"StdPersistent_TopLoc",
"StdPersistent_TopoDS"
]
class StdPersistent():
    """
    None
    """
    @staticmethod
    def BindTypes_s(theMap : OCP.StdObjMgt.StdObjMgt_MapOfInstantiators) -> None: 
        """
        Register types.
        """
    def __init__(self) -> None: ...
    pass
class StdPersistent_DataXtd():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdPersistent_DataXtd_Constraint():
    """
    None
    """
    def Import(self,theAttribute : OCP.TDataXtd.TDataXtd_Constraint) -> None: 
        """
        Import transient attribuite from the persistent data.
        """
    def PChildren(self,theChildren : Any) -> None: 
        """
        Gets persistent child objects
        """
    def PName(self) -> str: 
        """
        Returns persistent type name
        """
    def Read(self,theReadData : OCP.StdObjMgt.StdObjMgt_ReadData) -> None: 
        """
        Read persistent data from a file.
        """
    def Write(self,theWriteData : OCP.StdObjMgt.StdObjMgt_WriteData) -> None: 
        """
        Write persistent data to a file.
        """
    def __init__(self) -> None: ...
    pass
class StdPersistent_DataXtd_PatternStd():
    """
    None
    """
    def Import(self,theAttribute : OCP.TDataXtd.TDataXtd_PatternStd) -> None: 
        """
        Import transient attribuite from the persistent data.
        """
    def PChildren(self,theChildren : Any) -> None: 
        """
        Gets persistent child objects
        """
    def PName(self) -> str: 
        """
        Returns persistent type name
        """
    def Read(self,theReadData : OCP.StdObjMgt.StdObjMgt_ReadData) -> None: 
        """
        Read persistent data from a file.
        """
    def Write(self,theWriteData : OCP.StdObjMgt.StdObjMgt_WriteData) -> None: 
        """
        Write persistent data to a file.
        """
    def __init__(self) -> None: ...
    pass
class StdPersistent_HArray1():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdPersistent_HArray1OfShape1(OCP.Standard.Standard_Transient):
    def Array1(self) -> Any: 
        """
        None
        """
    def ChangeArray1(self) -> Any: 
        """
        None
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOther : Any) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.StdObject.StdObject_Shape) -> None: ...
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
class StdPersistent_Naming():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdPersistent_PPrsStd():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdPersistent_TopLoc():
    """
    None
    """
    @staticmethod
    @overload
    def Translate_s(theLoc : OCP.TopLoc.TopLoc_Location,theMap : Any) -> Any: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Translate_s(theDatum : OCP.TopLoc.TopLoc_Datum3D,theMap : Any) -> Any: ...
    def __init__(self) -> None: ...
    pass
class StdPersistent_TopoDS():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
