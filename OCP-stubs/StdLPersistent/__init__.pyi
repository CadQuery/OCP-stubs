import OCP.StdLPersistent
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.StdObjMgt
import OCP.TFunction
import OCP.TDocStd
import OCP.Standard
import OCP.TDataStd
import OCP.TCollection
__all__  = [
"StdLPersistent",
"StdLPersistent_Collection",
"StdLPersistent_Data",
"StdLPersistent_Dependency",
"StdLPersistent_Document",
"StdLPersistent_Function",
"StdLPersistent_HArray1",
"StdLPersistent_HArray1OfPersistent",
"StdLPersistent_HArray2",
"StdLPersistent_HArray2OfPersistent",
"StdLPersistent_HString",
"StdLPersistent_NamedData",
"StdLPersistent_Real",
"StdLPersistent_TreeNode",
"StdLPersistent_Value",
"StdLPersistent_Variable",
"StdLPersistent_Void",
"StdLPersistent_XLink"
]
class StdLPersistent():
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
class StdLPersistent_Collection():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdLPersistent_Data(OCP.StdObjMgt.StdObjMgt_Persistent, OCP.Standard.Standard_Transient):
    """
    None
    """
    def AsciiString(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Get referenced ASCII string (to be overridden by ASCII string class; returns a null handle by default for other classes).
        """
    def CreateAttribute(self) -> OCP.TDF.TDF_Attribute: 
        """
        Create an empty transient attribute (to be overridden by attribute classes; does nothing and returns a null handle by default for other classes).
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
        Returns a type descriptor about this object.
        """
    def ExtString(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Get referenced extended string (to be overridden by extended string class; returns a null handle by default for other classes).
        """
    def GetAttribute(self) -> OCP.TDF.TDF_Attribute: 
        """
        Get transient attribute for the persistent data (to be overridden by attribute classes; returns a null handle by default for non-attribute classes).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Import(self) -> OCP.TDF.TDF_Data: 
        """
        Import transient data from the persistent data.
        """
    def ImportAttribute(self) -> None: 
        """
        Import transient attribute from the persistent data (to be overridden by attribute classes; does nothing by default for non-attribute classes).
        """
    def ImportDocument(self,theDocument : OCP.TDocStd.TDocStd_Document) -> None: 
        """
        Import transient document from the persistent data (to be overridden by document class; does nothing by default for other classes).
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
    def Label(self,theDF : OCP.TDF.TDF_Data) -> OCP.TDF.TDF_Label: 
        """
        Get a label expressed by referenced extended string (to be overridden by extended string class; returns a null label by default for other classes).
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
    @overload
    def RefNum(self,theRefNum : int) -> None: 
        """
        Returns the object reference number

        Sets an object reference number
        """
    @overload
    def RefNum(self) -> int: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def TypeNum(self) -> int: 
        """
        Returns the assigned persistent type number

        Assigns a persistent type number to the object
        """
    @overload
    def TypeNum(self,theTypeNum : int) -> None: ...
    def Write(self,theWriteData : OCP.StdObjMgt.StdObjMgt_WriteData) -> None: 
        """
        Write persistent data to a file.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        Returns type descriptor of Standard_Transient class
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StdLPersistent_Dependency():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdLPersistent_Document(OCP.StdObjMgt.StdObjMgt_Persistent, OCP.Standard.Standard_Transient):
    """
    None
    """
    def AsciiString(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Get referenced ASCII string (to be overridden by ASCII string class; returns a null handle by default for other classes).
        """
    def CreateAttribute(self) -> OCP.TDF.TDF_Attribute: 
        """
        Create an empty transient attribute (to be overridden by attribute classes; does nothing and returns a null handle by default for other classes).
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
        Returns a type descriptor about this object.
        """
    def ExtString(self) -> OCP.TCollection.TCollection_HExtendedString: 
        """
        Get referenced extended string (to be overridden by extended string class; returns a null handle by default for other classes).
        """
    def GetAttribute(self) -> OCP.TDF.TDF_Attribute: 
        """
        Get transient attribute for the persistent data (to be overridden by attribute classes; returns a null handle by default for non-attribute classes).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ImportAttribute(self) -> None: 
        """
        Import transient attribute from the persistent data (to be overridden by attribute classes; does nothing by default for non-attribute classes).
        """
    def ImportDocument(self,theDocument : OCP.TDocStd.TDocStd_Document) -> None: 
        """
        Import transient document from the persistent data.
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
    def Label(self,theDF : OCP.TDF.TDF_Data) -> OCP.TDF.TDF_Label: 
        """
        Get a label expressed by referenced extended string (to be overridden by extended string class; returns a null label by default for other classes).
        """
    def PChildren(self,arg1 : Any) -> None: 
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
    @overload
    def RefNum(self,theRefNum : int) -> None: 
        """
        Returns the object reference number

        Sets an object reference number
        """
    @overload
    def RefNum(self) -> int: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def TypeNum(self) -> int: 
        """
        Returns the assigned persistent type number

        Assigns a persistent type number to the object
        """
    @overload
    def TypeNum(self,theTypeNum : int) -> None: ...
    def Write(self,theWriteData : OCP.StdObjMgt.StdObjMgt_WriteData) -> None: 
        """
        Read persistent data from a file.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        Returns type descriptor of Standard_Transient class
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StdLPersistent_Function():
    """
    None
    """
    def Import(self,theAttribute : OCP.TFunction.TFunction_Function) -> None: 
        """
        Import transient attribute from the persistent data.
        """
    def PChildren(self,arg1 : Any) -> None: 
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
class StdLPersistent_HArray1():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdLPersistent_HArray1OfPersistent(OCP.Standard.Standard_Transient):
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.StdObjMgt.StdObjMgt_Persistent) -> None: ...
    @overload
    def __init__(self,theOther : Any) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
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
class StdLPersistent_HArray2():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdLPersistent_HArray2OfPersistent(OCP.Standard.Standard_Transient):
    def Array2(self) -> Any: 
        """
        None
        """
    def ChangeArray2(self) -> Any: 
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : OCP.StdObjMgt.StdObjMgt_Persistent) -> None: ...
    @overload
    def __init__(self,theOther : Any) -> None: ...
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
class StdLPersistent_HString():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdLPersistent_NamedData():
    """
    None
    """
    def PChildren(self,arg1 : Any) -> None: 
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
class StdLPersistent_Real():
    """
    None
    """
    def Import(self,theAttribute : OCP.TDataStd.TDataStd_Real) -> None: 
        """
        Import transient attribute from the persistent data.
        """
    def PChildren(self,arg1 : Any) -> None: 
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
        Write persistent data from a file.
        """
    def __init__(self) -> None: ...
    pass
class StdLPersistent_TreeNode():
    """
    None
    """
    def CreateAttribute(self) -> OCP.TDF.TDF_Attribute: 
        """
        Create an empty transient attribute
        """
    def ImportAttribute(self) -> None: 
        """
        Import transient attribute from the persistent data.
        """
    def PChildren(self,arg1 : Any) -> None: 
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
class StdLPersistent_Value():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdLPersistent_Variable():
    """
    None
    """
    def Import(self,theAttribute : OCP.TDataStd.TDataStd_Variable) -> None: 
        """
        Import transient attribute from the persistent data.
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
class StdLPersistent_Void():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdLPersistent_XLink():
    """
    None
    """
    def Import(self,theAttribute : OCP.TDocStd.TDocStd_XLink) -> None: 
        """
        Import transient attribute from the persistent data.
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
