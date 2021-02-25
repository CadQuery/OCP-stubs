import OCP.StdObjMgt
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.TDocStd
import OCP.TCollection
import OCP.Storage
import OCP.Standard
__all__  = [
"StdObjMgt_MapOfInstantiators",
"StdObjMgt_Persistent",
"StdObjMgt_ReadData",
"StdObjMgt_SharedObject",
"StdObjMgt_WriteData"
]
class StdObjMgt_MapOfInstantiators():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdObjMgt_Persistent(OCP.Standard.Standard_Transient):
    """
    Root class for a temporary persistent object that reads data from a file and then creates transient object using the data.
    """
    def AsciiString(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Get referenced ASCII string (to be overriden by ASCII string class; returns a null handle by default for other classes).
        """
    def CreateAttribute(self) -> OCP.TDF.TDF_Attribute: 
        """
        Create an empty transient attribuite (to be overriden by attribute classes; does nothing and returns a null handle by default for other classes).
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
        Get referenced extended string (to be overriden by extended string class; returns a null handle by default for other classes).
        """
    def GetAttribute(self) -> OCP.TDF.TDF_Attribute: 
        """
        Get transient attribuite for the persistent data (to be overriden by attribute classes; returns a null handle by default for non-attribute classes).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ImportAttribute(self) -> None: 
        """
        Import transient attribuite from the persistent data (to be overriden by attribute classes; does nothing by default for non-attribute classes).
        """
    def ImportDocument(self,theDocument : OCP.TDocStd.TDocStd_Document) -> None: 
        """
        Import transient document from the persistent data (to be overriden by document class; does nothing by default for other classes).
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
    def Label(self,theDF : OCP.TDF.TDF_Data) -> OCP.TDF.TDF_Label: 
        """
        Get a label expressed by referenced extended string (to be overriden by extended string class; returns a null label by default for other classes).
        """
    def PChildren(self,arg1 : Any) -> None: 
        """
        Gets persistent child objects
        """
    def PName(self) -> str: 
        """
        Returns persistent type name
        """
    def Read(self,theReadData : StdObjMgt_ReadData) -> None: 
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
    def TypeNum(self,theTypeNum : int) -> None: 
        """
        Returns the assigned persistent type number

        Assigns a persistent type number to the object
        """
    @overload
    def TypeNum(self) -> int: ...
    def Write(self,theWriteData : StdObjMgt_WriteData) -> None: 
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
class StdObjMgt_ReadData():
    """
    Auxiliary data used to read persistent objects from a file.
    """
    def PersistentObject(self,theRef : int) -> StdObjMgt_Persistent: 
        """
        None
        """
    def ReadPersistentObject(self,theRef : int) -> None: 
        """
        None
        """
    def ReadReference(self) -> StdObjMgt_Persistent: 
        """
        None
        """
    def __init__(self,theDriver : OCP.Storage.Storage_BaseDriver,theNumberOfObjects : int) -> None: ...
    pass
class StdObjMgt_SharedObject():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class StdObjMgt_WriteData():
    """
    Auxiliary data used to write persistent objects to a file.
    """
    def WritePersistentObject(self,thePersistent : StdObjMgt_Persistent) -> None: 
        """
        None
        """
    def __init__(self,theDriver : OCP.Storage.Storage_BaseDriver) -> None: ...
    pass
