import OCP.LDOM
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import io
import LDOM_Node
import LDOM_OSStream
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
    class NodeType_e():
        pass
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self,anOther : LDOM_Node) -> None: ...
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
    def getNextSibling(self) -> LDOM_Node: 
        """
        None
        """
    def getNodeName(self) -> LDOMString: 
        """
        None
        """
    def getNodeType(self) -> LDOM_Node.NodeType_e: 
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
    ATTRIBUTE_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ATTRIBUTE_NODE: 2>
    CDATA_SECTION_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.CDATA_SECTION_NODE: 4>
    COMMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.COMMENT_NODE: 8>
    ELEMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ELEMENT_NODE: 1>
    TEXT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.TEXT_NODE: 3>
    UNKNOWN: OCP.LDOM.NodeType_e # value = <NodeType_e.UNKNOWN: 0>
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
    class NodeType_e():
        pass
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
    def getNodeType(self) -> LDOM_Node.NodeType_e: 
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
    ATTRIBUTE_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ATTRIBUTE_NODE: 2>
    CDATA_SECTION_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.CDATA_SECTION_NODE: 4>
    COMMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.COMMENT_NODE: 8>
    ELEMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ELEMENT_NODE: 1>
    TEXT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.TEXT_NODE: 3>
    UNKNOWN: OCP.LDOM.NodeType_e # value = <NodeType_e.UNKNOWN: 0>
    pass
class LDOM_CharReference():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class LDOM_Text(LDOM_CharacterData, LDOM_Node):
    """
    None
    """
    class NodeType_e():
        pass
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
    def getNodeType(self) -> LDOM_Node.NodeType_e: 
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
    ATTRIBUTE_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ATTRIBUTE_NODE: 2>
    CDATA_SECTION_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.CDATA_SECTION_NODE: 4>
    COMMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.COMMENT_NODE: 8>
    ELEMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ELEMENT_NODE: 1>
    TEXT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.TEXT_NODE: 3>
    UNKNOWN: OCP.LDOM.NodeType_e # value = <NodeType_e.UNKNOWN: 0>
    pass
class LDOM_Comment(LDOM_CharacterData, LDOM_Node):
    """
    None
    """
    class NodeType_e():
        pass
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
    def getNodeType(self) -> LDOM_Node.NodeType_e: 
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
    ATTRIBUTE_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ATTRIBUTE_NODE: 2>
    CDATA_SECTION_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.CDATA_SECTION_NODE: 4>
    COMMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.COMMENT_NODE: 8>
    ELEMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ELEMENT_NODE: 1>
    TEXT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.TEXT_NODE: 3>
    UNKNOWN: OCP.LDOM.NodeType_e # value = <NodeType_e.UNKNOWN: 0>
    pass
class LDOM_Document():
    """
    None
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aMemManager : LDOM_MemManager) -> None: ...
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
    class NodeType_e():
        pass
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
    def getNodeType(self) -> LDOM_Node.NodeType_e: 
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
    ATTRIBUTE_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ATTRIBUTE_NODE: 2>
    CDATA_SECTION_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.CDATA_SECTION_NODE: 4>
    COMMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.COMMENT_NODE: 8>
    ELEMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ELEMENT_NODE: 1>
    TEXT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.TEXT_NODE: 3>
    UNKNOWN: OCP.LDOM.NodeType_e # value = <NodeType_e.UNKNOWN: 0>
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
    class NodeType_e():
        """
        None

        Members:

          UNKNOWN

          ELEMENT_NODE

          ATTRIBUTE_NODE

          TEXT_NODE

          CDATA_SECTION_NODE

          COMMENT_NODE
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ATTRIBUTE_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ATTRIBUTE_NODE: 2>
        CDATA_SECTION_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.CDATA_SECTION_NODE: 4>
        COMMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.COMMENT_NODE: 8>
        ELEMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ELEMENT_NODE: 1>
        TEXT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.TEXT_NODE: 3>
        UNKNOWN: OCP.LDOM.NodeType_e # value = <NodeType_e.UNKNOWN: 0>
        __entries: dict # value = {'UNKNOWN': (<NodeType_e.UNKNOWN: 0>, None), 'ELEMENT_NODE': (<NodeType_e.ELEMENT_NODE: 1>, None), 'ATTRIBUTE_NODE': (<NodeType_e.ATTRIBUTE_NODE: 2>, None), 'TEXT_NODE': (<NodeType_e.TEXT_NODE: 3>, None), 'CDATA_SECTION_NODE': (<NodeType_e.CDATA_SECTION_NODE: 4>, None), 'COMMENT_NODE': (<NodeType_e.COMMENT_NODE: 8>, None)}
        __members__: dict # value = {'UNKNOWN': <NodeType_e.UNKNOWN: 0>, 'ELEMENT_NODE': <NodeType_e.ELEMENT_NODE: 1>, 'ATTRIBUTE_NODE': <NodeType_e.ATTRIBUTE_NODE: 2>, 'TEXT_NODE': <NodeType_e.TEXT_NODE: 3>, 'CDATA_SECTION_NODE': <NodeType_e.CDATA_SECTION_NODE: 4>, 'COMMENT_NODE': <NodeType_e.COMMENT_NODE: 8>}
        pass
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,anOther : LDOM_Attr) -> None: ...
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
    def getNodeType(self) -> LDOM_Node.NodeType_e: 
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
    ATTRIBUTE_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ATTRIBUTE_NODE: 2>
    CDATA_SECTION_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.CDATA_SECTION_NODE: 4>
    COMMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.COMMENT_NODE: 8>
    ELEMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ELEMENT_NODE: 1>
    TEXT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.TEXT_NODE: 3>
    UNKNOWN: OCP.LDOM.NodeType_e # value = <NodeType_e.UNKNOWN: 0>
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
    class BOMType_e():
        """
        None

        Members:

          BOM_UNDEFINED

          BOM_UTF8

          BOM_UTF16BE

          BOM_UTF16LE

          BOM_UTF32BE

          BOM_UTF32LE

          BOM_UTF7

          BOM_UTF1

          BOM_UTFEBCDIC

          BOM_SCSU

          BOM_BOCU1

          BOM_GB18030
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        BOM_BOCU1: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_BOCU1: 10>
        BOM_GB18030: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_GB18030: 11>
        BOM_SCSU: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_SCSU: 9>
        BOM_UNDEFINED: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UNDEFINED: 0>
        BOM_UTF1: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF1: 7>
        BOM_UTF16BE: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF16BE: 2>
        BOM_UTF16LE: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF16LE: 3>
        BOM_UTF32BE: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF32BE: 4>
        BOM_UTF32LE: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF32LE: 5>
        BOM_UTF7: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF7: 6>
        BOM_UTF8: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF8: 1>
        BOM_UTFEBCDIC: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTFEBCDIC: 8>
        __entries: dict # value = {'BOM_UNDEFINED': (<BOMType_e.BOM_UNDEFINED: 0>, None), 'BOM_UTF8': (<BOMType_e.BOM_UTF8: 1>, None), 'BOM_UTF16BE': (<BOMType_e.BOM_UTF16BE: 2>, None), 'BOM_UTF16LE': (<BOMType_e.BOM_UTF16LE: 3>, None), 'BOM_UTF32BE': (<BOMType_e.BOM_UTF32BE: 4>, None), 'BOM_UTF32LE': (<BOMType_e.BOM_UTF32LE: 5>, None), 'BOM_UTF7': (<BOMType_e.BOM_UTF7: 6>, None), 'BOM_UTF1': (<BOMType_e.BOM_UTF1: 7>, None), 'BOM_UTFEBCDIC': (<BOMType_e.BOM_UTFEBCDIC: 8>, None), 'BOM_SCSU': (<BOMType_e.BOM_SCSU: 9>, None), 'BOM_BOCU1': (<BOMType_e.BOM_BOCU1: 10>, None), 'BOM_GB18030': (<BOMType_e.BOM_GB18030: 11>, None)}
        __members__: dict # value = {'BOM_UNDEFINED': <BOMType_e.BOM_UNDEFINED: 0>, 'BOM_UTF8': <BOMType_e.BOM_UTF8: 1>, 'BOM_UTF16BE': <BOMType_e.BOM_UTF16BE: 2>, 'BOM_UTF16LE': <BOMType_e.BOM_UTF16LE: 3>, 'BOM_UTF32BE': <BOMType_e.BOM_UTF32BE: 4>, 'BOM_UTF32LE': <BOMType_e.BOM_UTF32LE: 5>, 'BOM_UTF7': <BOMType_e.BOM_UTF7: 6>, 'BOM_UTF1': <BOMType_e.BOM_UTF1: 7>, 'BOM_UTFEBCDIC': <BOMType_e.BOM_UTFEBCDIC: 8>, 'BOM_SCSU': <BOMType_e.BOM_SCSU: 9>, 'BOM_BOCU1': <BOMType_e.BOM_BOCU1: 10>, 'BOM_GB18030': <BOMType_e.BOM_GB18030: 11>}
        pass
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
    BOM_BOCU1: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_BOCU1: 10>
    BOM_GB18030: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_GB18030: 11>
    BOM_SCSU: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_SCSU: 9>
    BOM_UNDEFINED: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UNDEFINED: 0>
    BOM_UTF1: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF1: 7>
    BOM_UTF16BE: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF16BE: 2>
    BOM_UTF16LE: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF16LE: 3>
    BOM_UTF32BE: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF32BE: 4>
    BOM_UTF32LE: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF32LE: 5>
    BOM_UTF7: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF7: 6>
    BOM_UTF8: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTF8: 1>
    BOM_UTFEBCDIC: OCP.LDOM.BOMType_e # value = <BOMType_e.BOM_UTFEBCDIC: 8>
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
    class NodeType_e():
        pass
    def SetValueClear(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self,theOther : LDOM_CDATASection) -> None: ...
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
    def getNodeType(self) -> LDOM_Node.NodeType_e: 
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
    ATTRIBUTE_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ATTRIBUTE_NODE: 2>
    CDATA_SECTION_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.CDATA_SECTION_NODE: 4>
    COMMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.COMMENT_NODE: 8>
    ELEMENT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.ELEMENT_NODE: 1>
    TEXT_NODE: OCP.LDOM.NodeType_e # value = <NodeType_e.TEXT_NODE: 3>
    UNKNOWN: OCP.LDOM.NodeType_e # value = <NodeType_e.UNKNOWN: 0>
    pass
class LDOM_XmlReader():
    """
    None
    """
    class RecordType_e():
        """
        None

        Members:

          XML_UNKNOWN

          XML_HEADER

          XML_DOCTYPE

          XML_COMMENT

          XML_START_ELEMENT

          XML_END_ELEMENT

          XML_FULL_ELEMENT

          XML_TEXT

          XML_CDATA

          XML_EOF
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        XML_CDATA: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_CDATA: 8>
        XML_COMMENT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_COMMENT: 3>
        XML_DOCTYPE: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_DOCTYPE: 2>
        XML_END_ELEMENT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_END_ELEMENT: 5>
        XML_EOF: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_EOF: 9>
        XML_FULL_ELEMENT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_FULL_ELEMENT: 6>
        XML_HEADER: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_HEADER: 1>
        XML_START_ELEMENT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_START_ELEMENT: 4>
        XML_TEXT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_TEXT: 7>
        XML_UNKNOWN: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_UNKNOWN: 0>
        __entries: dict # value = {'XML_UNKNOWN': (<RecordType_e.XML_UNKNOWN: 0>, None), 'XML_HEADER': (<RecordType_e.XML_HEADER: 1>, None), 'XML_DOCTYPE': (<RecordType_e.XML_DOCTYPE: 2>, None), 'XML_COMMENT': (<RecordType_e.XML_COMMENT: 3>, None), 'XML_START_ELEMENT': (<RecordType_e.XML_START_ELEMENT: 4>, None), 'XML_END_ELEMENT': (<RecordType_e.XML_END_ELEMENT: 5>, None), 'XML_FULL_ELEMENT': (<RecordType_e.XML_FULL_ELEMENT: 6>, None), 'XML_TEXT': (<RecordType_e.XML_TEXT: 7>, None), 'XML_CDATA': (<RecordType_e.XML_CDATA: 8>, None), 'XML_EOF': (<RecordType_e.XML_EOF: 9>, None)}
        __members__: dict # value = {'XML_UNKNOWN': <RecordType_e.XML_UNKNOWN: 0>, 'XML_HEADER': <RecordType_e.XML_HEADER: 1>, 'XML_DOCTYPE': <RecordType_e.XML_DOCTYPE: 2>, 'XML_COMMENT': <RecordType_e.XML_COMMENT: 3>, 'XML_START_ELEMENT': <RecordType_e.XML_START_ELEMENT: 4>, 'XML_END_ELEMENT': <RecordType_e.XML_END_ELEMENT: 5>, 'XML_FULL_ELEMENT': <RecordType_e.XML_FULL_ELEMENT: 6>, 'XML_TEXT': <RecordType_e.XML_TEXT: 7>, 'XML_CDATA': <RecordType_e.XML_CDATA: 8>, 'XML_EOF': <RecordType_e.XML_EOF: 9>}
        pass
    def GetBOM(self) -> LDOM_OSStream.BOMType_e: 
        """
        None
        """
    def GetElement(self) -> LDOM_BasicElement: 
        """
        None
        """
    XML_CDATA: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_CDATA: 8>
    XML_COMMENT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_COMMENT: 3>
    XML_DOCTYPE: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_DOCTYPE: 2>
    XML_END_ELEMENT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_END_ELEMENT: 5>
    XML_EOF: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_EOF: 9>
    XML_FULL_ELEMENT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_FULL_ELEMENT: 6>
    XML_HEADER: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_HEADER: 1>
    XML_START_ELEMENT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_START_ELEMENT: 4>
    XML_TEXT: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_TEXT: 7>
    XML_UNKNOWN: OCP.LDOM.RecordType_e # value = <RecordType_e.XML_UNKNOWN: 0>
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
    def Write(self,theOStream : io.BytesIO,theNode : LDOM_Node) -> None: 
        """
        None

        None
        """
    @overload
    def Write(self,theOStream : io.BytesIO,theDoc : LDOM_Document) -> None: ...
    def __init__(self,theEncoding : str=None) -> None: ...
    pass
