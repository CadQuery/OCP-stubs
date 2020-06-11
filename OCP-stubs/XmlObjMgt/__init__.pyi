import OCP.XmlObjMgt
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.LDOM
import OCP.Storage
import OCP.TCollection
import OCP.gp
__all__  = [
"XmlObjMgt",
"XmlObjMgt_Array1",
"XmlObjMgt_GP",
"XmlObjMgt_Persistent",
"XmlObjMgt_RRelocationTable",
"XmlObjMgt_SRelocationTable"
]
class XmlObjMgt():
    """
    This package defines services to manage the storage grain of data produced by applications and those classes to manage persistent extern reference.
    """
    @staticmethod
    def FindChildByName_s(theSource : OCP.LDOM.LDOM_Element,theName : LDOMString) -> OCP.LDOM.LDOM_Element: 
        """
        None
        """
    @staticmethod
    def FindChildByRef_s(theSource : OCP.LDOM.LDOM_Element,theRefName : LDOMString) -> OCP.LDOM.LDOM_Element: 
        """
        None
        """
    @staticmethod
    def FindChildElement_s(theSource : OCP.LDOM.LDOM_Element,theObjId : int) -> OCP.LDOM.LDOM_Element: 
        """
        None
        """
    @staticmethod
    def GetExtendedString_s(theElement : OCP.LDOM.LDOM_Element,theString : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Get attribute <theElement extstring="theString" ...>
        """
    @staticmethod
    def GetReal_s(theString : LDOMString,theValue : float) -> bool: 
        """
        None
        """
    @staticmethod
    def GetStringValue_s(theElement : OCP.LDOM.LDOM_Element) -> LDOMString: 
        """
        Returns the first child text node
        """
    @staticmethod
    def GetTagEntryString_s(theTarget : LDOMString,theTagEntry : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Convert XPath expression (DOMString) into TagEntry string returns False on Error
        """
    @staticmethod
    def IdString_s() -> LDOMString: 
        """
        Define the name of XMLattribute 'ID' (to be used everywhere)
        """
    @staticmethod
    def SetExtendedString_s(theElement : OCP.LDOM.LDOM_Element,theString : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Add attribute <theElement extstring="theString" ...>
        """
    @staticmethod
    def SetStringValue_s(theElement : OCP.LDOM.LDOM_Element,theData : LDOMString,isClearText : bool=False) -> None: 
        """
        Add theData as the last child text node to theElement isClearText(True) avoids analysis of the string and replacement of characters like '<' and '&' during XML file storage. Do NEVER set isClearText unless you have a hell of a reason
        """
    @staticmethod
    def SetTagEntryString_s(theSource : LDOMString,theTagEntry : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Convert XPath expression (DOMString) into TagEntry string returns False on Error
        """
    def __init__(self) -> None: ...
    pass
class XmlObjMgt_Array1():
    """
    The class Array1 represents unidimensionnal array of fixed size known at run time. The range of the index is user defined. Warning: Programs clients of such class must be independant of the range of the first element. Then, a C++ for loop must be written like this for (i = A->Lower(); i <= A->Upper(); i++)
    """
    def CreateArrayElement(self,theParent : OCP.LDOM.LDOM_Element,theName : LDOMString) -> None: 
        """
        Create DOM_Element representing the array, under 'theParent'
        """
    def Element(self) -> OCP.LDOM.LDOM_Element: 
        """
        Returns the DOM element of <me>.

        Returns the DOM element of <me>.
        """
    def Length(self) -> int: 
        """
        Returns the number of elements of <me>.

        Returns the number of elements of <me>.
        """
    def Lower(self) -> int: 
        """
        Returns the lower bound.

        Returns the lower bound.
        """
    def SetValue(self,Index : int,Value : OCP.LDOM.LDOM_Element) -> None: 
        """
        Set the <Index>th element of the array to <Value>.
        """
    def Upper(self) -> int: 
        """
        Returns the upper bound.

        Returns the upper bound.
        """
    def Value(self,Index : int) -> OCP.LDOM.LDOM_Element: 
        """
        Returns the value of <Index>th element of the array.
        """
    @overload
    def __init__(self,Low : int,Up : int) -> None: ...
    @overload
    def __init__(self,theParent : OCP.LDOM.LDOM_Element,theName : LDOMString) -> None: ...
    pass
class XmlObjMgt_GP():
    """
    Translation of gp (simple geometry) objects
    """
    @staticmethod
    @overload
    def Translate_s(aStr : LDOMString,T : OCP.gp.gp_XYZ) -> bool: 
        """
        None

        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def Translate_s(aStr : LDOMString,T : OCP.gp.gp_Trsf) -> bool: ...
    @staticmethod
    @overload
    def Translate_s(aTrsf : OCP.gp.gp_Trsf) -> LDOMString: ...
    @staticmethod
    @overload
    def Translate_s(anXYZ : OCP.gp.gp_XYZ) -> LDOMString: ...
    @staticmethod
    @overload
    def Translate_s(aStr : LDOMString,T : OCP.gp.gp_Mat) -> bool: ...
    @staticmethod
    @overload
    def Translate_s(aMat : OCP.gp.gp_Mat) -> LDOMString: ...
    def __init__(self) -> None: ...
    pass
class XmlObjMgt_Persistent():
    """
    root for XML-persistence
    """
    def CreateElement(self,theParent : OCP.LDOM.LDOM_Element,theType : LDOMString,theID : int) -> None: 
        """
        myElement := <theType id="theID"/>
        """
    def Element(self) -> OCP.LDOM.LDOM_Element: 
        """
        return myElement

        return myElement

        return myElement

        return myElement
        """
    def Id(self) -> int: 
        """
        None

        None
        """
    def SetId(self,theId : int) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theElement : OCP.LDOM.LDOM_Element,theRef : LDOMString) -> None: ...
    @overload
    def __init__(self,theElement : OCP.LDOM.LDOM_Element) -> None: ...
    pass
class XmlObjMgt_RRelocationTable():
    """
    Retrieval relocation table is modeled as a child class of TColStd_DataMapOfIntegerTransient that stores a handle to the file header section. With that attribute drivers have access to the file header section.
    """
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        None
        """
    def GetHeaderData(self) -> OCP.Storage.Storage_HeaderData: 
        """
        Returns a handle to the header data of the file that is begin read
        """
    def SetHeaderData(self,theHeaderData : OCP.Storage.Storage_HeaderData) -> None: 
        """
        Sets the storage header data.
        """
    def __init__(self) -> None: ...
    pass
class XmlObjMgt_SRelocationTable():
    """
    Stored relocation table is modeled as a child class of TColStd_DataMapOfIntegerTransient that stores a handle to the file header section. With that attribute drivers have access to the file header section.
    """
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        None
        """
    def GetHeaderData(self) -> OCP.Storage.Storage_HeaderData: 
        """
        Returns a handle to the header data of the file that is begin read
        """
    def SetHeaderData(self,theHeaderData : OCP.Storage.Storage_HeaderData) -> None: 
        """
        Sets the storage header data.
        """
    def __init__(self) -> None: ...
    pass
