import OCP.LDOM
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
__all__  = [
"LDOM_Node",
"LDOM_BasicNode",
"LDOM_BasicElement",
"LDOM_BasicAttribute",
"LDOM_CharacterData",
"LDOM_CharReference",
"LDOM_Text",
"LDOM_Comment",
"LDOM_Document",
"LDOM_DocumentType",
"LDOM_Element",
"LDOM_LDOMImplementation",
"LDOM_Attr",
"LDOM_NodeList",
"LDOM_OSStream",
"LDOM_SBuffer",
"LDOM_CDATASection",
"LDOM_XmlReader",
"LDOM_XmlWriter"
]
class LDOM_Node():
    """
    None
    """
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,anOther : LDOM_Node) -> None: ...
    def appendChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def getFirstChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLastChild(self) -> LDOM_Node: 
        """
        None
        """
    def getNextSibling(self) -> LDOM_Node: 
        """
        None
        """
    def getNodeName(self) -> LDOMString: 
        """
        None
        """
    def getNodeType(self) -> Any: 
        """
        None
        """
    def getNodeValue(self) -> LDOMString: 
        """
        None
        """
    def getOwnerDocument(self) -> LDOM_MemManager: 
        """
        None
        """
    def hasChildNodes(self) -> bool: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    def removeChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    pass
class LDOM_BasicNode():
    """
    None
    """
    def GetSibling(self) -> LDOM_BasicNode: 
        """
        None
        """
    def getNodeType(self) -> Any: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    pass
class LDOM_BasicElement(LDOM_BasicNode):
    """
    None
    """
    @staticmethod
    def Create_s(aName : str,aLength : int,aDoc : LDOM_MemManager) -> LDOM_BasicElement: 
        """
        None
        """
    def GetAttribute(self,aName : LDOMBasicString,aLastCh : LDOM_BasicNode) -> LDOM_BasicAttribute: 
        """
        None
        """
    def GetFirstChild(self) -> LDOM_BasicNode: 
        """
        None
        """
    def GetLastChild(self) -> LDOM_BasicNode: 
        """
        None
        """
    def GetSibling(self) -> LDOM_BasicNode: 
        """
        None
        """
    def GetTagName(self) -> str: 
        """
        None
        """
    def __init__(self) -> None: ...
    def getNodeType(self) -> Any: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    pass
class LDOM_BasicAttribute(LDOM_BasicNode):
    """
    None
    """
    def GetName(self) -> str: 
        """
        None
        """
    def GetSibling(self) -> LDOM_BasicNode: 
        """
        None
        """
    def GetValue(self) -> LDOMBasicString: 
        """
        None
        """
    def __init__(self) -> None: ...
    def getNodeType(self) -> Any: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    pass
class LDOM_CharacterData(LDOM_Node):
    """
    None
    """
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self,theOther : LDOM_CharacterData) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def appendChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def getData(self) -> LDOMString: 
        """
        None
        """
    def getFirstChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLastChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLength(self) -> int: 
        """
        None
        """
    def getNextSibling(self) -> LDOM_Node: 
        """
        None
        """
    def getNodeName(self) -> LDOMString: 
        """
        None
        """
    def getNodeType(self) -> Any: 
        """
        None
        """
    def getNodeValue(self) -> LDOMString: 
        """
        None
        """
    def getOwnerDocument(self) -> LDOM_MemManager: 
        """
        None
        """
    def hasChildNodes(self) -> bool: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    def removeChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def setData(self,aValue : LDOMString) -> None: 
        """
        None
        """
    pass
class LDOM_CharReference():
    """
    None
    """
    @staticmethod
    def Decode_s(theSrc : str,theLen : int) -> str: 
        """
        None
        """
    @staticmethod
    def Encode_s(theSrc : str,theLen : int,isAttribute : bool) -> str: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class LDOM_Text(LDOM_CharacterData, LDOM_Node):
    """
    None
    """
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self,anOther : LDOM_Text) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def appendChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def getData(self) -> LDOMString: 
        """
        None
        """
    def getFirstChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLastChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLength(self) -> int: 
        """
        None
        """
    def getNextSibling(self) -> LDOM_Node: 
        """
        None
        """
    def getNodeName(self) -> LDOMString: 
        """
        None
        """
    def getNodeType(self) -> Any: 
        """
        None
        """
    def getNodeValue(self) -> LDOMString: 
        """
        None
        """
    def getOwnerDocument(self) -> LDOM_MemManager: 
        """
        None
        """
    def hasChildNodes(self) -> bool: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    def removeChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def setData(self,aValue : LDOMString) -> None: 
        """
        None
        """
    pass
class LDOM_Comment(LDOM_CharacterData, LDOM_Node):
    """
    None
    """
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self,theOther : LDOM_Comment) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def appendChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def getData(self) -> LDOMString: 
        """
        None
        """
    def getFirstChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLastChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLength(self) -> int: 
        """
        None
        """
    def getNextSibling(self) -> LDOM_Node: 
        """
        None
        """
    def getNodeName(self) -> LDOMString: 
        """
        None
        """
    def getNodeType(self) -> Any: 
        """
        None
        """
    def getNodeValue(self) -> LDOMString: 
        """
        None
        """
    def getOwnerDocument(self) -> LDOM_MemManager: 
        """
        None
        """
    def hasChildNodes(self) -> bool: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    def removeChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def setData(self,aValue : LDOMString) -> None: 
        """
        None
        """
    pass
class LDOM_Document():
    """
    None
    """
    @overload
    def __init__(self,aMemManager : LDOM_MemManager) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def createCDATASection(self,theData : LDOMString) -> LDOM_CDATASection: 
        """
        None
        """
    def createComment(self,theData : LDOMString) -> LDOM_Comment: 
        """
        None
        """
    @staticmethod
    def createDocument_s(theQualifiedName : LDOMString) -> LDOM_Document: 
        """
        None
        """
    def createElement(self,theTagName : LDOMString) -> LDOM_Element: 
        """
        None
        """
    def createTextNode(self,theData : LDOMString) -> LDOM_Text: 
        """
        None
        """
    def getDocumentElement(self) -> LDOM_Element: 
        """
        None
        """
    def getElementsByTagName(self,theTagName : LDOMString) -> LDOM_NodeList: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    pass
class LDOM_DocumentType():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class LDOM_Element(LDOM_Node):
    """
    None
    """
    def GetAttributesList(self) -> LDOM_NodeList: 
        """
        None
        """
    def GetChildByTagName(self,aTagName : LDOMString) -> LDOM_Element: 
        """
        None
        """
    def GetSiblingByTagName(self) -> LDOM_Element: 
        """
        None
        """
    def ReplaceElement(self,anOther : LDOM_Element) -> None: 
        """
        None
        """
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self,anOther : LDOM_Element) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def appendChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def getAttribute(self,aName : LDOMString) -> LDOMString: 
        """
        None
        """
    def getAttributeNode(self,aName : LDOMString) -> LDOM_Attr: 
        """
        None
        """
    def getElementsByTagName(self,aName : LDOMString) -> LDOM_NodeList: 
        """
        None
        """
    def getFirstChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLastChild(self) -> LDOM_Node: 
        """
        None
        """
    def getNextSibling(self) -> LDOM_Node: 
        """
        None
        """
    def getNodeName(self) -> LDOMString: 
        """
        None
        """
    def getNodeType(self) -> Any: 
        """
        None
        """
    def getNodeValue(self) -> LDOMString: 
        """
        None
        """
    def getOwnerDocument(self) -> LDOM_MemManager: 
        """
        None
        """
    def getTagName(self) -> LDOMString: 
        """
        None
        """
    def hasChildNodes(self) -> bool: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    def removeAttribute(self,aName : LDOMString) -> None: 
        """
        None
        """
    def removeChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def setAttribute(self,aName : LDOMString,aValue : LDOMString) -> None: 
        """
        None
        """
    def setAttributeNode(self,aNewAttr : LDOM_Attr) -> None: 
        """
        None
        """
    pass
class LDOM_LDOMImplementation():
    """
    None
    """
    def __init__(self) -> None: ...
    @staticmethod
    def createDocument_s(aNamespaceURI : LDOMString,aQualifiedName : LDOMString,aDocType : LDOM_DocumentType) -> LDOM_Document: 
        """
        None
        """
    pass
class LDOM_Attr(LDOM_Node):
    """
    None
    """
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self,anOther : LDOM_Attr) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def appendChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def getFirstChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLastChild(self) -> LDOM_Node: 
        """
        None
        """
    def getName(self) -> LDOMString: 
        """
        None
        """
    def getNextSibling(self) -> LDOM_Node: 
        """
        None
        """
    def getNodeName(self) -> LDOMString: 
        """
        None
        """
    def getNodeType(self) -> Any: 
        """
        None
        """
    def getNodeValue(self) -> LDOMString: 
        """
        None
        """
    def getOwnerDocument(self) -> LDOM_MemManager: 
        """
        None
        """
    def getValue(self) -> LDOMString: 
        """
        None
        """
    def hasChildNodes(self) -> bool: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    def removeChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def setValue(self,aValue : LDOMString) -> None: 
        """
        None
        """
    pass
class LDOM_NodeList():
    """
    None
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : LDOM_NodeList) -> None: ...
    def getLength(self) -> int: 
        """
        None
        """
    def item(self,arg1 : int) -> LDOM_Node: 
        """
        None
        """
    pass
class LDOM_OSStream():
    """
    Subclass if std::ostream allowing to increase performance of outputting data into a string avoiding reallocation of buffer. Class LDOM_OSStream implements output into a sequence of strings and getting the result as a string. It inherits Standard_OStream (std::ostream). Beside methods of std::ostream, it also has additional useful methods: str(), Length() and Clear().
    """
    def Clear(self) -> None: 
        """
        None
        """
    def Length(self) -> int: 
        """
        None
        """
    def __init__(self,theMaxBuf : int) -> None: ...
    def str(self) -> str: 
        """
        None
        """
    pass
class LDOM_SBuffer():
    """
    Class LDOM_SBuffer inherits std::streambuf and redefines some virtual methods of it (overflow() and xsputn()). This class contains pointers on first and current element of sequence, also it has methods for the sequence management.
    """
    def Clear(self) -> None: 
        """
        Clears first element of sequence and removes all others
        """
    def Length(self) -> int: 
        """
        Returns full length of data contained
        """
    def __init__(self,theMaxBuf : int) -> None: ...
    def overflow(self,c : int=-1) -> int: 
        """
        None
        """
    def str(self) -> str: 
        """
        Concatenates strings of all sequence elements into one string. Space for output string is allocated with operator new. Caller of this function is responsible for memory release after the string usage.
        """
    def underflow(self) -> int: 
        """
        None
        """
    def xsputn(self,s : str,n : int) -> int: 
        """
        None
        """
    pass
class LDOM_CDATASection(LDOM_Text, LDOM_CharacterData, LDOM_Node):
    """
    None
    """
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : LDOM_CDATASection) -> None: ...
    def appendChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def getData(self) -> LDOMString: 
        """
        None
        """
    def getFirstChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLastChild(self) -> LDOM_Node: 
        """
        None
        """
    def getLength(self) -> int: 
        """
        None
        """
    def getNextSibling(self) -> LDOM_Node: 
        """
        None
        """
    def getNodeName(self) -> LDOMString: 
        """
        None
        """
    def getNodeType(self) -> Any: 
        """
        None
        """
    def getNodeValue(self) -> LDOMString: 
        """
        None
        """
    def getOwnerDocument(self) -> LDOM_MemManager: 
        """
        None
        """
    def hasChildNodes(self) -> bool: 
        """
        None
        """
    def isNull(self) -> bool: 
        """
        None
        """
    def removeChild(self,aChild : LDOM_Node) -> None: 
        """
        None
        """
    def setData(self,aValue : LDOMString) -> None: 
        """
        None
        """
    pass
class LDOM_XmlReader():
    """
    None
    """
    def CreateElement(self,theName : str,theLen : int) -> None: 
        """
        None
        """
    def GetElement(self) -> LDOM_BasicElement: 
        """
        None
        """
    def ReadRecord(self,theIStream : Any,theData : LDOM_OSStream) -> Any: 
        """
        None
        """
    def __init__(self,aDocument : LDOM_MemManager,anErrorString : OCP.TCollection.TCollection_AsciiString,theTagPerStep : bool=False) -> None: ...
    @staticmethod
    def getInteger_s(theValue : LDOMBasicString,theStart : str,theEnd : str) -> bool: 
        """
        None
        """
    pass
class LDOM_XmlWriter():
    """
    None
    """
    def SetIndentation(self,theIndent : int) -> None: 
        """
        None
        """
    @overload
    def Write(self,theOStream : Any,theNode : LDOM_Node) -> None: 
        """
        None

        None
        """
    @overload
    def Write(self,theOStream : Any,theDoc : LDOM_Document) -> None: ...
    def __init__(self,theEncoding : str=None) -> None: ...
    pass
