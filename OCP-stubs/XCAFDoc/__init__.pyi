import OCP.XCAFDoc
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Graphic3d
import XCAFDoc_AssemblyGraph
import OCP.TopLoc
import OCP.TopoDS
import OCP.TDocStd
import OCP.TCollection
import OCP.XCAFNoteObjects
import OCP.Standard
import OCP.TColStd
import OCP.XCAFView
import OCP.TDataStd
import OCP.NCollection
import OCP.OSD
import OCP.gp
import OCP.TDF
import OCP.XCAFDimTolObjects
import OCP.TopTools
import io
import OCP.Quantity
__all__  = [
"XCAFDoc",
"XCAFDoc_Area",
"XCAFDoc_AssemblyGraph",
"XCAFDoc_AssemblyItemId",
"XCAFDoc_AssemblyItemRef",
"XCAFDoc_AssemblyIterator",
"XCAFDoc_AssemblyTool",
"XCAFDoc_Centroid",
"XCAFDoc_ClippingPlaneTool",
"XCAFDoc_Color",
"XCAFDoc_ColorTool",
"XCAFDoc_ColorType",
"XCAFDoc_DataMapOfShapeLabel",
"XCAFDoc_Datum",
"XCAFDoc_DimTol",
"XCAFDoc_DimTolTool",
"XCAFDoc_Dimension",
"XCAFDoc_DocumentTool",
"XCAFDoc_Editor",
"XCAFDoc_GeomTolerance",
"XCAFDoc_GraphNode",
"XCAFDoc_GraphNodeSequence",
"XCAFDoc_LayerTool",
"XCAFDoc_LengthUnit",
"XCAFDoc_Location",
"XCAFDoc_Material",
"XCAFDoc_MaterialTool",
"XCAFDoc_Note",
"XCAFDoc_NoteComment",
"XCAFDoc_NoteBinData",
"XCAFDoc_NoteBalloon",
"XCAFDoc_NotesTool",
"XCAFDoc_ShapeMapTool",
"XCAFDoc_ShapeTool",
"XCAFDoc_View",
"XCAFDoc_ViewTool",
"XCAFDoc_VisMaterial",
"XCAFDoc_VisMaterialCommon",
"XCAFDoc_VisMaterialPBR",
"XCAFDoc_VisMaterialTool",
"XCAFDoc_Volume",
"XCAFDoc_ColorCurv",
"XCAFDoc_ColorGen",
"XCAFDoc_ColorSurf"
]
class XCAFDoc():
    """
    Definition of general structure of DECAF document and tools to work with it
    """
    @staticmethod
    def AssemblyGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        class for containing GraphNodes. Returns GUID for UAttribute identifying assembly
        """
    @staticmethod
    def AttributeInfo_s(theAtt : OCP.TDF.TDF_Attribute) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Prints attribute information into a string.
        """
    @staticmethod
    def ColorByLayerGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    def ColorRefGUID_s(type : XCAFDoc_ColorType) -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of colors
        """
    @staticmethod
    def DatumRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of datum
        """
    @staticmethod
    def DatumTolRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing connections Datum-Toler
        """
    @staticmethod
    def DimTolRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of DGT
        """
    @staticmethod
    def DimensionRefFirstGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of Dimension
        """
    @staticmethod
    def DimensionRefSecondGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of Dimension
        """
    @staticmethod
    def ExternRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns GUID for UAttribute identifying external reference on no-step file
        """
    @staticmethod
    def GeomToleranceRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of GeomTolerance
        """
    @staticmethod
    def InvisibleGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    def LayerRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    def LockGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns GUID for UAttribute identifying lock flag
        """
    @staticmethod
    def MaterialRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    def NoteRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for representing notes
        """
    @staticmethod
    def SHUORefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns GUID for UAttribute identifying specified higher usage occurrence
        """
    @staticmethod
    def ShapeRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns GUID for TreeNode representing assembly link
        """
    @staticmethod
    def ViewRefAnnotationGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    def ViewRefGDTGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of View
        """
    @staticmethod
    def ViewRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of View
        """
    @staticmethod
    def ViewRefNoteGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for GraphNode representing specified types of View
        """
    @staticmethod
    def ViewRefPlaneGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of View
        """
    @staticmethod
    def ViewRefShapeGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUIDs for TreeNode representing specified types of View
        """
    @staticmethod
    def VisMaterialRefGUID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return GUID for TreeNode representing Visualization Material.
        """
    def __init__(self) -> None: ...
    pass
class XCAFDoc_Area(OCP.TDataStd.TDataStd_Real, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    attribute to store areaattribute to store areaattribute to store area
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> float: 
        """
        None
        """
    def GetDimension(self) -> OCP.TDataStd.TDataStd_RealEnum: 
        """
        Obsolete method that will be removed in next versions. This field is not supported in the persistence mechanism.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(label : OCP.TDF.TDF_Label,area : float) -> bool: 
        """
        Returns volume of area as argument and success status returns false if no such attribute at the <label>
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsCaptured(self) -> bool: 
        """
        Returns True if there is a reference on the same label
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,vol : float) -> None: 
        """
        Sets a value of volume
        """
    def SetDimension(self,DIM : OCP.TDataStd.TDataStd_RealEnum) -> None: 
        """
        Obsolete method that will be removed in next versions. This field is not supported in the persistence mechanism.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,guid : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label,area : float) -> XCAFDoc_Area: 
        """
        Find, or create, an Area attribute and set its value
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_AssemblyGraph(OCP.Standard.Standard_Transient):
    class NodeType_e():
        """
        Type of the graph node.

        Members:

          NodeType_UNDEFINED

          NodeType_AssemblyRoot

          NodeType_Subassembly

          NodeType_Occurrence

          NodeType_Part

          NodeType_Subshape
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
        NodeType_AssemblyRoot: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_AssemblyRoot: 1>
        NodeType_Occurrence: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_Occurrence: 3>
        NodeType_Part: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_Part: 4>
        NodeType_Subassembly: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_Subassembly: 2>
        NodeType_Subshape: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_Subshape: 5>
        NodeType_UNDEFINED: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_UNDEFINED: 0>
        __entries: dict # value = {'NodeType_UNDEFINED': (<NodeType_e.NodeType_UNDEFINED: 0>, None), 'NodeType_AssemblyRoot': (<NodeType_e.NodeType_AssemblyRoot: 1>, None), 'NodeType_Subassembly': (<NodeType_e.NodeType_Subassembly: 2>, None), 'NodeType_Occurrence': (<NodeType_e.NodeType_Occurrence: 3>, None), 'NodeType_Part': (<NodeType_e.NodeType_Part: 4>, None), 'NodeType_Subshape': (<NodeType_e.NodeType_Subshape: 5>, None)}
        __members__: dict # value = {'NodeType_UNDEFINED': <NodeType_e.NodeType_UNDEFINED: 0>, 'NodeType_AssemblyRoot': <NodeType_e.NodeType_AssemblyRoot: 1>, 'NodeType_Subassembly': <NodeType_e.NodeType_Subassembly: 2>, 'NodeType_Occurrence': <NodeType_e.NodeType_Occurrence: 3>, 'NodeType_Part': <NodeType_e.NodeType_Part: 4>, 'NodeType_Subshape': <NodeType_e.NodeType_Subshape: 5>}
        pass
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
    def GetChildren(self,theNode : int) -> OCP.TColStd.TColStd_PackedMapOfInteger: 
        """
        Returns IDs of child nodes for the given node.
        """
    def GetLinks(self) -> Any: 
        """
        Returns the collection of graph links in the form of adjacency matrix.
        """
    def GetNode(self,theNode : int) -> OCP.TDF.TDF_Label: 
        """
        returns object ID by node ID.
        """
    def GetNodeType(self,theNode : int) -> XCAFDoc_AssemblyGraph.NodeType_e: 
        """
        Returns the node type from NodeType enum.
        """
    def GetNodes(self) -> OCP.TDF.TDF_LabelIndexedMap: 
        """
        Returns the unordered set of graph nodes.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRoots(self) -> OCP.TColStd.TColStd_PackedMapOfInteger: 
        """
        Returns IDs of the root nodes.
        """
    def GetShapeTool(self) -> XCAFDoc_ShapeTool: 
        """
        Returns Document shape tool.
        """
    def HasChildren(self,theNode : int) -> bool: 
        """
        Checks whether direct children exist for the given node.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDirectLink(self,theNode1 : int,theNode2 : int) -> bool: 
        """
        Checks whether the assembly graph contains (n1, n2) directed link.
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
    def NbLinks(self) -> int: 
        """
        Returns the number of graph links.
        """
    def NbNodes(self) -> int: 
        """
        Returns the number of graph nodes.
        """
    def NbOccurrences(self,theNode : int) -> int: 
        """
        Returns quantity of part usage occurrences.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theLabel : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def __init__(self,theDoc : OCP.TDocStd.TDocStd_Document) -> None: ...
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
    NodeType_AssemblyRoot: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_AssemblyRoot: 1>
    NodeType_Occurrence: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_Occurrence: 3>
    NodeType_Part: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_Part: 4>
    NodeType_Subassembly: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_Subassembly: 2>
    NodeType_Subshape: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_Subshape: 5>
    NodeType_UNDEFINED: OCP.XCAFDoc.NodeType_e # value = <NodeType_e.NodeType_UNDEFINED: 0>
    pass
class XCAFDoc_AssemblyItemId():
    """
    Unique item identifier in the hierarchical product structure. A full path to an assembly component in the "part-of" graph starting from the root node.
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetPath(self) -> OCP.TColStd.TColStd_ListOfAsciiString: 
        """
        Returns the full path as a list of label entries.
        """
    @overload
    def Init(self,theString : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Initializes the item ID from a list of strings, where every string is a label entry.

        Initializes the item ID from a formatted path, where label entries are separated by '/' symbol.
        """
    @overload
    def Init(self,thePath : OCP.TColStd.TColStd_ListOfAsciiString) -> None: ...
    def IsChild(self,theOther : XCAFDoc_AssemblyItemId) -> bool: 
        """
        Checks if this item is a child of the given item.
        """
    def IsDirectChild(self,theOther : XCAFDoc_AssemblyItemId) -> bool: 
        """
        Checks if this item is a direct child of the given item.
        """
    def IsEqual(self,theOther : XCAFDoc_AssemblyItemId) -> bool: 
        """
        Checks for item IDs equality.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if the full path is empty, otherwise - false.
        """
    def Nullify(self) -> None: 
        """
        Clears the full path.
        """
    def ToString(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the full pass as a formatted string.
        """
    @overload
    def __init__(self,theString : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,thePath : OCP.TColStd.TColStd_ListOfAsciiString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class XCAFDoc_AssemblyItemRef(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    An attribute that describes a weak reference to an assembly item or to a subshape or to an assembly label attribute.An attribute that describes a weak reference to an assembly item or to a subshape or to an assembly label attribute.An attribute that describes a weak reference to an assembly item or to a subshape or to an assembly label attribute.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def ClearExtraRef(self) -> None: 
        """
        Reverts the reference to empty state.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,theOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetGUID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the assembly item's attribute that the reference points to. If the reference doesn't point to an attribute, returns an empty GUID.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetItem(self) -> XCAFDoc_AssemblyItemId: 
        """
        Returns the assembly item ID that the reference points to.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSubshapeIndex(self) -> int: 
        """
        Returns the assembly item's subshape that the reference points to. If the reference doesn't point to a subshape, returns 0.
        """
    @staticmethod
    def Get_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_AssemblyItemRef: 
        """
        Finds a reference attribute on the given label and returns it, if it is found
        """
    def HasExtraRef(self) -> bool: 
        """
        Checks if the reference points on an item's shapeindex or attribute.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
        """
    def IsGUID(self) -> bool: 
        """
        Checks is the reference points to an item's attribute.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsOrphan(self) -> bool: 
        """
        Checks if the reference points to a really existing item in XDE document.
        """
    def IsSubshapeIndex(self) -> bool: 
        """
        Checks is the reference points to an item's subshape.
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,theAttrInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theAttrFrom : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetGUID(self,theAttrGUID : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the assembly item's label attribute that the reference points to. The base assembly item will not change.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @overload
    def SetItem(self,theItemId : XCAFDoc_AssemblyItemId) -> None: 
        """
        Sets the assembly item ID that the reference points to. Extra reference data (if any) will be cleared.

        Sets the assembly item ID from a list of label entries that the reference points to. Extra reference data (if any) will be cleared.

        Sets the assembly item ID from a formatted path that the reference points to. Extra reference data (if any) will be cleared.
        """
    @overload
    def SetItem(self,theString : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def SetItem(self,thePath : OCP.TColStd.TColStd_ListOfAsciiString) -> None: ...
    def SetSubshapeIndex(self,theShapeIndex : int) -> None: 
        """
        Sets the assembly item's subshape that the reference points to. The base assembly item will not change.
        """
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label,theItemId : XCAFDoc_AssemblyItemId) -> XCAFDoc_AssemblyItemRef: ...
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label,theItemId : XCAFDoc_AssemblyItemId,theGUID : OCP.Standard.Standard_GUID) -> XCAFDoc_AssemblyItemRef: ...
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label,theItemId : XCAFDoc_AssemblyItemId,theShapeIndex : int) -> XCAFDoc_AssemblyItemRef: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_AssemblyIterator():
    """
    Iterator in depth along the assembly tree.
    """
    def Current(self) -> XCAFDoc_AssemblyItemId: 
        """
        Returns current item.
        """
    def More(self) -> bool: 
        """
        Returns true if there is still something to iterate, false -- otherwise.
        """
    def Next(self) -> None: 
        """
        Moves depth-first iterator to the next position.
        """
    @overload
    def __init__(self,theDoc : OCP.TDocStd.TDocStd_Document,theLevel : int=2147483647) -> None: ...
    @overload
    def __init__(self,theDoc : OCP.TDocStd.TDocStd_Document,theRoot : XCAFDoc_AssemblyItemId,theLevel : int=2147483647) -> None: ...
    pass
class XCAFDoc_AssemblyTool():
    """
    Provides generic methods for traversing assembly tree and graph
    """
    def __init__(self) -> None: ...
    pass
class XCAFDoc_Centroid(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    attribute to store centroidattribute to store centroidattribute to store centroid
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(label : OCP.TDF.TDF_Label,pnt : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns point as argument returns false if no such attribute at the <label>
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,pnt : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label,pnt : OCP.gp.gp_Pnt) -> XCAFDoc_Centroid: 
        """
        Find, or create, a Location attribute and set it's value the Location attribute is returned. Location methods ===============
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_ClippingPlaneTool(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Provide tool for management of ClippingPlane section of document. Provide tool to store, retrieve, remove and modify clipping planes. Each clipping plane consists of gp_Pln and its name.Provide tool for management of ClippingPlane section of document. Provide tool to store, retrieve, remove and modify clipping planes. Each clipping plane consists of gp_Pln and its name.Provide tool for management of ClippingPlane section of document. Provide tool to store, retrieve, remove and modify clipping planes. Each clipping plane consists of gp_Pln and its name.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    @overload
    def AddClippingPlane(self,thePlane : OCP.gp.gp_Pln,theName : OCP.TCollection.TCollection_HAsciiString) -> OCP.TDF.TDF_Label: 
        """
        Adds a clipping plane definition to a ClippingPlane table and returns its label (returns existing label if the same clipping plane is already defined)

        Adds a clipping plane definition to a ClippingPlane table and returns its label (returns existing label if the same clipping plane is already defined)

        Adds a clipping plane definition to a ClippingPlane table and returns its label (returns existing label if the same clipping plane is already defined)

        Adds a clipping plane definition to a ClippingPlane table and returns its label (returns existing label if the same clipping plane is already defined)
        """
    @overload
    def AddClippingPlane(self,thePlane : OCP.gp.gp_Pln,theName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TDF.TDF_Label: ...
    @overload
    def AddClippingPlane(self,thePlane : OCP.gp.gp_Pln,theName : OCP.TCollection.TCollection_ExtendedString,theCapping : bool) -> OCP.TDF.TDF_Label: ...
    @overload
    def AddClippingPlane(self,thePlane : OCP.gp.gp_Pln,theName : OCP.TCollection.TCollection_HAsciiString,theCapping : bool) -> OCP.TDF.TDF_Label: ...
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BaseLabel(self) -> OCP.TDF.TDF_Label: 
        """
        returns the label under which ClippingPlanes are stored
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @overload
    def GetCapping(self,theClippingPlaneL : OCP.TDF.TDF_Label) -> bool: 
        """
        Get capping value for given clipping plane label Return capping value

        Get capping value for given clipping plane label Return true if Label is valid abd capping is exist.
        """
    @overload
    def GetCapping(self,theClippingPlaneL : OCP.TDF.TDF_Label,theCapping : bool) -> bool: ...
    @overload
    def GetClippingPlane(self,theLabel : OCP.TDF.TDF_Label,thePlane : OCP.gp.gp_Pln,theName : OCP.TCollection.TCollection_ExtendedString,theCapping : bool) -> bool: 
        """
        Returns ClippingPlane defined by label lab Returns False if the label is not in ClippingPlane table or does not define a ClippingPlane

        Returns ClippingPlane defined by label lab Returns False if the label is not in ClippingPlane table or does not define a ClippingPlane
        """
    @overload
    def GetClippingPlane(self,theLabel : OCP.TDF.TDF_Label,thePlane : OCP.gp.gp_Pln,theName : OCP.TCollection.TCollection_HAsciiString,theCapping : bool) -> bool: ...
    def GetClippingPlanes(self,Labels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of clipping planes currently stored in the ClippingPlane table
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsClippingPlane(self,theLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if label belongs to a ClippingPlane table and is a ClippingPlane definition
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveClippingPlane(self,theLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Removes clipping plane from the ClippingPlane table Return false and do nothing if clipping plane is referenced in at least one View
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetCapping(self,theClippingPlaneL : OCP.TDF.TDF_Label,theCapping : bool) -> None: 
        """
        Set new value of capping for given clipping plane label
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_ClippingPlaneTool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def UpdateClippingPlane(self,theLabelL : OCP.TDF.TDF_Label,thePlane : OCP.gp.gp_Pln,theName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Sets new value of plane and name to the given clipping plane label or do nothing, if the given label is not a clipping plane label
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_Color(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    attribute to store colorattribute to store colorattribute to store color
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetAlpha(self) -> float: 
        """
        None
        """
    def GetColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        None
        """
    def GetColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetNOC(self) -> OCP.Quantity.Quantity_NameOfColor: 
        """
        None
        """
    def GetRGB(self) -> Tuple[float, float, float]: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def Set(self,C : OCP.Quantity.Quantity_Color) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Set(self,C : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    @overload
    def Set(self,R : float,G : float,B : float,alpha : float=1.0) -> None: ...
    @overload
    def Set(self,C : OCP.Quantity.Quantity_NameOfColor) -> None: ...
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,C : OCP.Quantity.Quantity_ColorRGBA) -> XCAFDoc_Color: 
        """
        None

        None

        None

        Find, or create, a Color attribute and set it's value the Color attribute is returned.
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,R : float,G : float,B : float,alpha : float=1.0) -> XCAFDoc_Color: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,C : OCP.Quantity.Quantity_NameOfColor) -> XCAFDoc_Color: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,C : OCP.Quantity.Quantity_Color) -> XCAFDoc_Color: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_ColorTool(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Provides tools to store and retrieve attributes (colors) of TopoDS_Shape in and from TDocStd_Document A Document is intended to hold different attributes of ONE shape and it's sub-shapes Provide tools for management of Colors section of document.Provides tools to store and retrieve attributes (colors) of TopoDS_Shape in and from TDocStd_Document A Document is intended to hold different attributes of ONE shape and it's sub-shapes Provide tools for management of Colors section of document.Provides tools to store and retrieve attributes (colors) of TopoDS_Shape in and from TDocStd_Document A Document is intended to hold different attributes of ONE shape and it's sub-shapes Provide tools for management of Colors section of document.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    @overload
    def AddColor(self,col : OCP.Quantity.Quantity_ColorRGBA) -> OCP.TDF.TDF_Label: 
        """
        Adds a color definition to a colortable and returns its label (returns existing label if the same color is already defined)

        Adds a color definition to a colortable and returns its label (returns existing label if the same color is already defined)
        """
    @overload
    def AddColor(self,col : OCP.Quantity.Quantity_Color) -> OCP.TDF.TDF_Label: ...
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    @staticmethod
    def AutoNaming_s() -> bool: 
        """
        Returns current auto-naming mode; TRUE by default. If TRUE then for added colors the TDataStd_Name attribute will be automatically added. This setting is global.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BaseLabel(self) -> OCP.TDF.TDF_Label: 
        """
        returns the label under which colors are stored
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    @overload
    def FindColor(self,col : OCP.Quantity.Quantity_ColorRGBA,lab : OCP.TDF.TDF_Label) -> bool: 
        """
        Finds a color definition in a colortable and returns its label if found Returns False if color is not found in colortable

        Finds a color definition in a colortable and returns its label if found Returns False if color is not found in colortable

        Finds a color definition in a colortable and returns its label if found (or Null label else)

        Finds a color definition in a colortable and returns its label if found (or Null label else)
        """
    @overload
    def FindColor(self,col : OCP.Quantity.Quantity_Color) -> OCP.TDF.TDF_Label: ...
    @overload
    def FindColor(self,col : OCP.Quantity.Quantity_Color,lab : OCP.TDF.TDF_Label) -> bool: ...
    @overload
    def FindColor(self,col : OCP.Quantity.Quantity_ColorRGBA) -> OCP.TDF.TDF_Label: ...
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @overload
    def GetColor(self,L : OCP.TDF.TDF_Label,type : XCAFDoc_ColorType,color : OCP.Quantity.Quantity_ColorRGBA) -> bool: 
        """
        Returns color defined by label lab Returns False if the label is not in colortable or does not define a color

        Returns color defined by label lab Returns False if the label is not in colortable or does not define a color

        Returns color assigned to <L> as <type> Returns False if no such color is assigned

        Returns color assigned to <L> as <type> Returns False if no such color is assigned

        Returns label with color assigned to <L> as <type> Returns False if no such color is assigned

        Returns color assigned to <L> as <type> Returns False if no such color is assigned

        Returns color assigned to <L> as <type> Returns False if no such color is assigned
        """
    @overload
    def GetColor(self,S : OCP.TopoDS.TopoDS_Shape,type : XCAFDoc_ColorType,color : OCP.Quantity.Quantity_ColorRGBA) -> bool: ...
    @overload
    def GetColor(self,lab : OCP.TDF.TDF_Label,col : OCP.Quantity.Quantity_ColorRGBA) -> bool: ...
    @overload
    def GetColor(self,lab : OCP.TDF.TDF_Label,col : OCP.Quantity.Quantity_Color) -> bool: ...
    @overload
    def GetColor(self,S : OCP.TopoDS.TopoDS_Shape,type : XCAFDoc_ColorType,colorL : OCP.TDF.TDF_Label) -> bool: ...
    @overload
    def GetColor(self,L : OCP.TDF.TDF_Label,type : XCAFDoc_ColorType,color : OCP.Quantity.Quantity_Color) -> bool: ...
    @overload
    def GetColor(self,S : OCP.TopoDS.TopoDS_Shape,type : XCAFDoc_ColorType,color : OCP.Quantity.Quantity_Color) -> bool: ...
    @staticmethod
    def GetColor_s(L : OCP.TDF.TDF_Label,type : XCAFDoc_ColorType,colorL : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns label with color assigned to <L> as <type> Returns False if no such color is assigned
        """
    def GetColors(self,Labels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of colors currently stored in the colortable
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @overload
    def GetInstanceColor(self,theShape : OCP.TopoDS.TopoDS_Shape,type : XCAFDoc_ColorType,color : OCP.Quantity.Quantity_ColorRGBA) -> bool: 
        """
        Gets the color of component that styled with SHUO structure Returns FALSE if no sush component or color type

        Gets the color of component that styled with SHUO structure Returns FALSE if no sush component or color type
        """
    @overload
    def GetInstanceColor(self,theShape : OCP.TopoDS.TopoDS_Shape,type : XCAFDoc_ColorType,color : OCP.Quantity.Quantity_Color) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsColor(self,lab : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if label belongs to a colortable and is a color definition
        """
    def IsColorByLayer(self,L : OCP.TDF.TDF_Label) -> bool: 
        """
        Return TRUE if object color defined by its Layer, FALSE if not.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInstanceVisible(self,theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Gets the visibility status of component that styled with SHUO structure Returns FALSE if no sush component
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    @overload
    def IsSet(self,L : OCP.TDF.TDF_Label,type : XCAFDoc_ColorType) -> bool: 
        """
        Returns True if label <L> has a color assignment of the type <type>

        Returns True if label <L> has a color assignment of the type <type>
        """
    @overload
    def IsSet(self,S : OCP.TopoDS.TopoDS_Shape,type : XCAFDoc_ColorType) -> bool: ...
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def IsVisible(self,L : OCP.TDF.TDF_Label) -> bool: 
        """
        Return TRUE if object on this label is visible, FALSE if invisible.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveColor(self,lab : OCP.TDF.TDF_Label) -> None: 
        """
        Removes color from the colortable
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def ReverseChainsOfTreeNodes(self) -> bool: 
        """
        Reverses order in chains of TreeNodes (from Last to First) under each Color Label since we became to use function ::Prepend() instead of ::Append() in method SetColor() for acceleration
        """
    @staticmethod
    def SetAutoNaming_s(theIsAutoNaming : bool) -> None: 
        """
        See also AutoNaming().
        """
    @overload
    def SetColor(self,S : OCP.TopoDS.TopoDS_Shape,colorL : OCP.TDF.TDF_Label,type : XCAFDoc_ColorType) -> bool: 
        """
        Sets a link with GUID defined by <type> (see XCAFDoc::ColorRefGUID()) from label <L> to color defined by <colorL>. Color of shape is defined following way in dependance with type of color. If type of color is XCAFDoc_ColorGen - then this color defines default color for surfaces and curves. If for shape color with types XCAFDoc_ColorSurf or XCAFDoc_ColorCurv is specified then such color overrides generic color.

        Sets a link with GUID defined by <type> (see XCAFDoc::ColorRefGUID()) from label <L> to color <Color> in the colortable Adds a color as necessary

        Sets a link with GUID defined by <type> (see XCAFDoc::ColorRefGUID()) from label <L> to color <Color> in the colortable Adds a color as necessary

        Sets a link with GUID defined by <type> (see XCAFDoc::ColorRefGUID()) from label <L> to color defined by <colorL> Returns False if cannot find a label for shape S

        Sets a link with GUID defined by <type> (see XCAFDoc::ColorRefGUID()) from label <L> to color <Color> in the colortable Adds a color as necessary Returns False if cannot find a label for shape S

        Sets a link with GUID defined by <type> (see XCAFDoc::ColorRefGUID()) from label <L> to color <Color> in the colortable Adds a color as necessary Returns False if cannot find a label for shape S
        """
    @overload
    def SetColor(self,L : OCP.TDF.TDF_Label,colorL : OCP.TDF.TDF_Label,type : XCAFDoc_ColorType) -> None: ...
    @overload
    def SetColor(self,L : OCP.TDF.TDF_Label,Color : OCP.Quantity.Quantity_Color,type : XCAFDoc_ColorType) -> None: ...
    @overload
    def SetColor(self,L : OCP.TDF.TDF_Label,Color : OCP.Quantity.Quantity_ColorRGBA,type : XCAFDoc_ColorType) -> None: ...
    @overload
    def SetColor(self,S : OCP.TopoDS.TopoDS_Shape,Color : OCP.Quantity.Quantity_Color,type : XCAFDoc_ColorType) -> bool: ...
    @overload
    def SetColor(self,S : OCP.TopoDS.TopoDS_Shape,Color : OCP.Quantity.Quantity_ColorRGBA,type : XCAFDoc_ColorType) -> bool: ...
    def SetColorByLayer(self,shapeLabel : OCP.TDF.TDF_Label,isColorByLayer : bool=False) -> None: 
        """
        Set the Color defined by Layer flag on label. Do nothing if there no any object. Set UAttribute with corresponding GUID.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @overload
    def SetInstanceColor(self,theShape : OCP.TopoDS.TopoDS_Shape,type : XCAFDoc_ColorType,color : OCP.Quantity.Quantity_ColorRGBA,isCreateSHUO : bool=True) -> bool: 
        """
        Sets the color of component that styled with SHUO structure Returns FALSE if no sush component found NOTE: create SHUO structeure if it is necessary and if <isCreateSHUO>

        Sets the color of component that styled with SHUO structure Returns FALSE if no sush component found NOTE: create SHUO structeure if it is necessary and if <isCreateSHUO>
        """
    @overload
    def SetInstanceColor(self,theShape : OCP.TopoDS.TopoDS_Shape,type : XCAFDoc_ColorType,color : OCP.Quantity.Quantity_Color,isCreateSHUO : bool=True) -> bool: ...
    def SetVisibility(self,shapeLabel : OCP.TDF.TDF_Label,isvisible : bool=True) -> None: 
        """
        Set the visibility of object on label. Do nothing if there no any object. Set UAttribute with corresponding GUID.
        """
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> XCAFDoc_ColorTool: ...
    def ShapeTool(self) -> XCAFDoc_ShapeTool: 
        """
        Returns internal XCAFDoc_ShapeTool tool
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    @overload
    def UnSetColor(self,L : OCP.TDF.TDF_Label,type : XCAFDoc_ColorType) -> None: 
        """
        Removes a link with GUID defined by <type> (see XCAFDoc::ColorRefGUID()) from label <L> to color

        Removes a link with GUID defined by <type> (see XCAFDoc::ColorRefGUID()) from label <L> to color Returns True if such link existed
        """
    @overload
    def UnSetColor(self,S : OCP.TopoDS.TopoDS_Shape,type : XCAFDoc_ColorType) -> bool: ...
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_ColorType():
    """
    Defines types of color assignments Color of shape is defined following way in dependance with type of color. If type of color is XCAFDoc_ColorGen - then this color defines default color for surfaces and curves. If for shape color with types XCAFDoc_ColorSurf or XCAFDoc_ColorCurv is specified then such color overrides generic color. simple color color of surfaces color of curves

    Members:

      XCAFDoc_ColorGen

      XCAFDoc_ColorSurf

      XCAFDoc_ColorCurv
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
    XCAFDoc_ColorCurv: OCP.XCAFDoc.XCAFDoc_ColorType # value = <XCAFDoc_ColorType.XCAFDoc_ColorCurv: 2>
    XCAFDoc_ColorGen: OCP.XCAFDoc.XCAFDoc_ColorType # value = <XCAFDoc_ColorType.XCAFDoc_ColorGen: 0>
    XCAFDoc_ColorSurf: OCP.XCAFDoc.XCAFDoc_ColorType # value = <XCAFDoc_ColorType.XCAFDoc_ColorSurf: 1>
    __entries: dict # value = {'XCAFDoc_ColorGen': (<XCAFDoc_ColorType.XCAFDoc_ColorGen: 0>, None), 'XCAFDoc_ColorSurf': (<XCAFDoc_ColorType.XCAFDoc_ColorSurf: 1>, None), 'XCAFDoc_ColorCurv': (<XCAFDoc_ColorType.XCAFDoc_ColorCurv: 2>, None)}
    __members__: dict # value = {'XCAFDoc_ColorGen': <XCAFDoc_ColorType.XCAFDoc_ColorGen: 0>, 'XCAFDoc_ColorSurf': <XCAFDoc_ColorType.XCAFDoc_ColorSurf: 1>, 'XCAFDoc_ColorCurv': <XCAFDoc_ColorType.XCAFDoc_ColorCurv: 2>}
    pass
class XCAFDoc_DataMapOfShapeLabel(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : XCAFDoc_DataMapOfShapeLabel) -> XCAFDoc_DataMapOfShapeLabel: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TDF.TDF_Label) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TDF.TDF_Label: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TDF.TDF_Label: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : XCAFDoc_DataMapOfShapeLabel) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TDF.TDF_Label: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TDF.TDF_Label) -> bool: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TDF.TDF_Label: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : XCAFDoc_DataMapOfShapeLabel) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class XCAFDoc_Datum(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    attribute to store datumattribute to store datumattribute to store datum
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDescription(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetIdentification(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetObject(self) -> OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumObject: 
        """
        Returns dimension object data taken from the paren's label and its sub-labels.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,anIdentification : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetObject(self,theDatumObject : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumObject) -> None: 
        """
        Updates parent's label and its sub-labels with data taken from theDatumObject. Old data associated with the label will be lost.
        """
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_Datum: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,anIdentification : OCP.TCollection.TCollection_HAsciiString) -> XCAFDoc_Datum: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_DimTol(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    attribute to store dimension and toleranceattribute to store dimension and toleranceattribute to store dimension and tolerance
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDescription(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetKind(self) -> int: 
        """
        None
        """
    def GetName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetVal(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,kind : int,aVal : OCP.TColStd.TColStd_HArray1OfReal,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label,kind : int,aVal : OCP.TColStd.TColStd_HArray1OfReal,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString) -> XCAFDoc_DimTol: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_DimTolTool(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Attribute containing GD&T section of XCAF document. Provide tools for GD&T section management.Attribute containing GD&T section of XCAF document. Provide tools for GD&T section management.Attribute containing GD&T section of XCAF document. Provide tools for GD&T section management.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    @overload
    def AddDatum(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theIdentification : OCP.TCollection.TCollection_HAsciiString) -> OCP.TDF.TDF_Label: 
        """
        Adds a datum definition to the GD&T table and returns its label.

        Adds a datum definition to the GD&T table and returns its label.
        """
    @overload
    def AddDatum(self) -> OCP.TDF.TDF_Label: ...
    def AddDimTol(self,theKind : int,theVal : OCP.TColStd.TColStd_HArray1OfReal,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString) -> OCP.TDF.TDF_Label: 
        """
        Adds a dimension tolerance definition with the specified kind, value, name and description to the GD&T table and returns its label.
        """
    def AddDimension(self) -> OCP.TDF.TDF_Label: 
        """
        Adds a dimension definition to the GD&T table and returns its label.
        """
    def AddGeomTolerance(self) -> OCP.TDF.TDF_Label: 
        """
        Adds a GeomTolerance definition to the GD&T table and returns its label.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BaseLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label under which GD&T table is stored.
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def FindDatum(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theIdentification : OCP.TCollection.TCollection_HAsciiString,lab : OCP.TDF.TDF_Label) -> bool: 
        """
        Finds a datum satisfying the specified name, description and identification and returns its label if found.
        """
    @overload
    def FindDimTol(self,theKind : int,theVal : OCP.TColStd.TColStd_HArray1OfReal,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,lab : OCP.TDF.TDF_Label) -> bool: 
        """
        Finds a dimension tolerance definition in the GD&T table satisfying the specified kind, values, name and description and returns its label if found. Returns False if dimension tolerance is not found in DGTtable.

        Finds a dimension tolerance in the GD&T table satisfying the specified kind, values, name and description and returns its label if found (or Null label else).
        """
    @overload
    def FindDimTol(self,theKind : int,theVal : OCP.TColStd.TColStd_HArray1OfReal,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString) -> OCP.TDF.TDF_Label: ...
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDatum(self,theDatumL : OCP.TDF.TDF_Label,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theIdentification : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        Returns datum assigned to theDatumL label. Returns False if no such datum is assigned.
        """
    def GetDatumLabels(self,Labels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of Datums currently stored in the GD&T table.
        """
    def GetDatumOfTolerLabels(self,theDimTolL : OCP.TDF.TDF_Label,theDatums : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all Datum labels defined for theDimTolL label.
        """
    def GetDatumWithObjectOfTolerLabels(self,theDimTolL : OCP.TDF.TDF_Label,theDatums : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all Datum labels with XCAFDimTolObjects_DatumObject defined for label theDimTolL.
        """
    def GetDimTol(self,theDimTolL : OCP.TDF.TDF_Label,theKind : int,theVal : OCP.TColStd.TColStd_HArray1OfReal,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        Returns dimension tolerance assigned to theDimTolL label. Returns False if no such dimension tolerance is assigned.
        """
    def GetDimTolLabels(self,Labels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of D&GTs currently stored in the GD&T table.
        """
    def GetDimensionLabels(self,theLabels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of Dimension labels currently stored in the GD&T table.
        """
    def GetGDTPresentations(self,theGDTLabelToShape : Any) -> None: 
        """
        fill the map GDT label -> shape presentation
        """
    def GetGeomToleranceLabels(self,theLabels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of Tolerance labels currently stored in the GD&T table.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the standard GD&T tool GUID.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRefDatumLabel(self,theShapeL : OCP.TDF.TDF_Label,theDatum : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns Datum label defined for theShapeL label.
        """
    def GetRefDimensionLabels(self,theShapeL : OCP.TDF.TDF_Label,theDimensions : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all Dimension labels defined for theShapeL.
        """
    def GetRefGeomToleranceLabels(self,theShapeL : OCP.TDF.TDF_Label,theDimTols : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all GeomTolerance labels defined for theShapeL.
        """
    def GetRefShapeLabel(self,theL : OCP.TDF.TDF_Label,theShapeLFirst : OCP.TDF.TDF_LabelSequence,theShapeLSecond : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Gets all shape labels referred by theL label of the GD&T table. Returns False if there are no shape labels added to the sequences.
        """
    def GetTolerOfDatumLabels(self,theDatumL : OCP.TDF.TDF_Label,theTols : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all GeomToleranses labels defined for theDatumL label.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsDatum(self,lab : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if label belongs to the GD&T table and is a Datum definition.
        """
    def IsDimTol(self,theLab : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if theLab belongs to the GD&T table and is a dmension tolerance.
        """
    def IsDimension(self,theLab : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if the label belongs to a GD&T table and is a Dimension definition.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
        """
    def IsGeomTolerance(self,theLab : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if the label belongs to the GD&T table and is a dimension tolerance.
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
    def IsLocked(self,theViewL : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns true if the given GDT is marked as locked.
        """
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def Lock(self,theViewL : OCP.TDF.TDF_Label) -> None: 
        """
        Mark the given GDT as locked.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetDatum(self,theShapeLabels : OCP.TDF.TDF_LabelSequence,theDatumL : OCP.TDF.TDF_Label) -> None: 
        """
        Sets a datum to the sequence of shape labels.

        Sets a datum to theL label and binds it with theTolerL label. A datum with the specified name, description and identification is created if it isn't found in the GD&T table.
        """
    @overload
    def SetDatum(self,theL : OCP.TDF.TDF_Label,theTolerL : OCP.TDF.TDF_Label,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theIdentification : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def SetDatumToGeomTol(self,theDatumL : OCP.TDF.TDF_Label,theTolerL : OCP.TDF.TDF_Label) -> None: 
        """
        Sets a datum from theDatumL label to theToletL label.
        """
    @overload
    def SetDimTol(self,theL : OCP.TDF.TDF_Label,theKind : int,theVal : OCP.TColStd.TColStd_HArray1OfReal,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString) -> OCP.TDF.TDF_Label: 
        """
        Sets existing dimension tolerance to theL label.

        Creates a dimension tolerance and sets it to theL label.
        """
    @overload
    def SetDimTol(self,theL : OCP.TDF.TDF_Label,theDimTolL : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def SetDimension(self,theFirstL : OCP.TDF.TDF_Label,theSecondL : OCP.TDF.TDF_Label,theDimL : OCP.TDF.TDF_Label) -> None: 
        """
        Sets a dimension to sequences target labels.

        Sets a dimension to target labels.

        Sets a dimension to the target label.
        """
    @overload
    def SetDimension(self,theFirstLS : OCP.TDF.TDF_LabelSequence,theSecondLS : OCP.TDF.TDF_LabelSequence,theDimL : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def SetDimension(self,theL : OCP.TDF.TDF_Label,theDimL : OCP.TDF.TDF_Label) -> None: ...
    def SetGDTPresentations(self,theGDTLabelToPrs : Any) -> None: 
        """
        Set shape presentation for GDT labels according to given map (theGDTLabelToPrs) theGDTLabelToPrsName map is an additional argument, can be used to set presentation names. If label is not in the theGDTLabelToPrsName map, the presentation name will be empty
        """
    @overload
    def SetGeomTolerance(self,theL : OCP.TDF.TDF_Label,theGeomTolL : OCP.TDF.TDF_Label) -> None: 
        """
        Sets a geometry tolerance from theGeomTolL to theL label. Checks if theGeomTolL is a geometry tolerance definition first.

        Sets a geometry tolerance from theGeomTolL to sequence of labels theL. Checks if theGeomTolL is a geometry tolerance definition first.
        """
    @overload
    def SetGeomTolerance(self,theL : OCP.TDF.TDF_LabelSequence,theGeomTolL : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> XCAFDoc_DimTolTool: ...
    def ShapeTool(self) -> XCAFDoc_ShapeTool: 
        """
        Returns internal XCAFDoc_ShapeTool tool
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def Unlock(self,theViewL : OCP.TDF.TDF_Label) -> None: 
        """
        Unlock the given GDT.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_Dimension(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Attribute that identifies a dimension in the GD&T table. Its parent label is used as a container to store data provided by XCAFDimTolObjects_DimensionObject.Attribute that identifies a dimension in the GD&T table. Its parent label is used as a container to store data provided by XCAFDimTolObjects_DimensionObject.Attribute that identifies a dimension in the GD&T table. Its parent label is used as a container to store data provided by XCAFDimTolObjects_DimensionObject.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetObject(self) -> OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionObject: 
        """
        Returns dimension object data taken from the parent's label and its sub-labels.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetObject(self,theDimensionObject : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionObject) -> None: 
        """
        Updates parent's label and its sub-labels with data taken from theDimensionObject. Old data associated with the label will be lost.
        """
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_Dimension: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_DocumentTool(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Defines sections structure of an XDE document. attribute marking CAF document as being DECAF document. Creates the sections structure of the document.Defines sections structure of an XDE document. attribute marking CAF document as being DECAF document. Creates the sections structure of the document.Defines sections structure of an XDE document. attribute marking CAF document as being DECAF document. Creates the sections structure of the document.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        To init this derived attribute after the attribute restore using the base restore-methods
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    @staticmethod
    def CheckClippingPlaneTool_s(theAcces : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks for the ClippingPlaneTool attribute on the label's document Returns TRUE if Tool exists, ELSE if it has not been created
        """
    @staticmethod
    def CheckColorTool_s(theAcces : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks for the ColorTool attribute on the label's document Returns TRUE if Tool exists, ELSE if it has not been created
        """
    @staticmethod
    def CheckDimTolTool_s(theAcces : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks for the DimTolTool attribute on the label's document Returns TRUE if Tool exists, ELSE if it has not been created
        """
    @staticmethod
    def CheckLayerTool_s(theAcces : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks for the LayerTool attribute on the label's document Returns TRUE if Tool exists, ELSE if it has not been created
        """
    @staticmethod
    def CheckMaterialTool_s(theAcces : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks for the MaterialTool attribute on the label's document Returns TRUE if Tool exists, ELSE if it has not been created
        """
    @staticmethod
    def CheckNotesTool_s(theAcces : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks for the NotesTool attribute on the label's document Returns TRUE if Tool exists, ELSE if it has not been created
        """
    @staticmethod
    def CheckShapeTool_s(theAcces : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks for the ShapeTool attribute on the label's document Returns TRUE if Tool exists, ELSE if it has not been created
        """
    @staticmethod
    def CheckViewTool_s(theAcces : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks for the ViewTool attribute on the label's document Returns TRUE if Tool exists, ELSE if it has not been created
        """
    @staticmethod
    def CheckVisMaterialTool_s(theAcces : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks for the VisMaterialTool attribute on the label's document Returns TRUE if Tool exists, ELSE if it has not been created
        """
    @staticmethod
    def ClippingPlaneTool_s(acces : OCP.TDF.TDF_Label) -> XCAFDoc_ClippingPlaneTool: ...
    @staticmethod
    def ClippingPlanesLabel_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns sub-label of DocLabel() with tag 8.
        """
    @staticmethod
    def ColorTool_s(acces : OCP.TDF.TDF_Label) -> XCAFDoc_ColorTool: ...
    @staticmethod
    def ColorsLabel_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns sub-label of DocLabel() with tag 2.
        """
    @staticmethod
    def DGTsLabel_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns sub-label of DocLabel() with tag 4.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    @staticmethod
    def DimTolTool_s(acces : OCP.TDF.TDF_Label) -> XCAFDoc_DimTolTool: ...
    @staticmethod
    def DocLabel_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns label where the DocumentTool attribute is or 0.1 if DocumentTool is not yet set.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    @overload
    def GetLengthUnit_s(theDoc : OCP.TDocStd.TDocStd_Document,theResut : float) -> bool: 
        """
        Returns value of current internal unit for the document converted to base unit type.

        Returns value of current internal unit for the document in meter
        """
    @staticmethod
    @overload
    def GetLengthUnit_s(theDoc : OCP.TDocStd.TDocStd_Document,theResut : float,theBaseUnit : UnitsMethods_LengthUnit) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        to be called when reading this attribute from file
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    @staticmethod
    def IsXCAFDocument_s(Doc : OCP.TDocStd.TDocStd_Document) -> bool: 
        """
        None
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    @staticmethod
    def LayerTool_s(acces : OCP.TDF.TDF_Label) -> XCAFDoc_LayerTool: ...
    @staticmethod
    def LayersLabel_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns sub-label of DocLabel() with tag 3.
        """
    @staticmethod
    def MaterialTool_s(acces : OCP.TDF.TDF_Label) -> XCAFDoc_MaterialTool: ...
    @staticmethod
    def MaterialsLabel_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns sub-label of DocLabel() with tag 5.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    @staticmethod
    def NotesLabel_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns sub-label of DocLabel() with tag 9.
        """
    @staticmethod
    def NotesTool_s(acces : OCP.TDF.TDF_Label) -> XCAFDoc_NotesTool: ...
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def SetLengthUnit_s(theDoc : OCP.TDocStd.TDocStd_Document,theUnitValue : float,theBaseUnit : UnitsMethods_LengthUnit) -> None: 
        """
        Sets value of current internal unit to the document in meter

        Sets value of current internal unit to the document
        """
    @staticmethod
    @overload
    def SetLengthUnit_s(theDoc : OCP.TDocStd.TDocStd_Document,theUnitValue : float) -> None: ...
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label,IsAcces : bool=True) -> XCAFDoc_DocumentTool: ...
    @staticmethod
    def ShapeTool_s(acces : OCP.TDF.TDF_Label) -> XCAFDoc_ShapeTool: ...
    @staticmethod
    def ShapesLabel_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns sub-label of DocLabel() with tag 1.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    @staticmethod
    def ViewTool_s(acces : OCP.TDF.TDF_Label) -> XCAFDoc_ViewTool: ...
    @staticmethod
    def ViewsLabel_s(acces : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns sub-label of DocLabel() with tag 7.
        """
    @staticmethod
    def VisMaterialLabel_s(theLabel : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: 
        """
        Returns sub-label of DocLabel() with tag 10.
        """
    @staticmethod
    def VisMaterialTool_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_VisMaterialTool: ...
    def __init__(self) -> None: ...
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
class XCAFDoc_Editor():
    """
    Tool for edit structure of document.
    """
    @staticmethod
    def CloneMetaData_s(theSrcLabel : OCP.TDF.TDF_Label,theDstLabel : OCP.TDF.TDF_Label,theVisMatMap : Any,theToCopyColor : bool=True,theToCopyLayer : bool=True,theToCopyMaterial : bool=True,theToCopyVisMaterial : bool=True,theToCopyAttributes : bool=True) -> None: 
        """
        Copies metadata contains from the source label to the destination label. Protected against creating a new label for non-existent tools
        """
    @staticmethod
    def CloneShapeLabel_s(theSrcLabel : OCP.TDF.TDF_Label,theSrcShapeTool : XCAFDoc_ShapeTool,theDstShapeTool : XCAFDoc_ShapeTool,theMap : OCP.TDF.TDF_LabelDataMap) -> OCP.TDF.TDF_Label: 
        """
        Copies shapes label with keeping of shape structure (recursively)
        """
    @staticmethod
    @overload
    def Expand_s(theDoc : OCP.TDF.TDF_Label,theRecursively : bool=True) -> bool: 
        """
        Converts shape (compound/compsolid/shell/wire) to assembly.

        Converts all compounds shapes in the document to assembly
        """
    @staticmethod
    @overload
    def Expand_s(theDoc : OCP.TDF.TDF_Label,theShape : OCP.TDF.TDF_Label,theRecursively : bool=True) -> bool: ...
    @staticmethod
    @overload
    def Extract_s(theSrcLabels : OCP.TDF.TDF_LabelSequence,theDstLabel : OCP.TDF.TDF_Label,theIsNoVisMat : bool=False) -> bool: 
        """
        Clones all labels to a new position, keeping the structure with all the attributes

        Clones the label to a new position, keeping the structure with all the attributes
        """
    @staticmethod
    @overload
    def Extract_s(theSrcLabel : OCP.TDF.TDF_Label,theDstLabel : OCP.TDF.TDF_Label,theIsNoVisMat : bool=False) -> bool: ...
    @staticmethod
    def RescaleGeometry_s(theLabel : OCP.TDF.TDF_Label,theScaleFactor : float,theForceIfNotRoot : bool=False) -> bool: 
        """
        Applies geometrical scaling to the following assembly components: - part geometry - sub-assembly/part occurrence location - part's centroid, area and volume attributes - PMIs (warnings and errors are reported if it is impossible to make changes) Normally, should start from a root sub-assembly, but if theForceIfNotRoot true scaling will be applied forcibly. If theLabel corresponds to the shape tool scaling is applied to the whole assembly.
        """
    def __init__(self) -> None: ...
    pass
class XCAFDoc_GeomTolerance(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Attribute to store dimension and toleranceAttribute to store dimension and toleranceAttribute to store dimension and tolerance
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetObject(self) -> OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceObject: 
        """
        Returns geometry tolerance object data taken from the paren's label and its sub-labels.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetObject(self,theGeomToleranceObject : OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceObject) -> None: 
        """
        Updates parent's label and its sub-labels with data taken from theGeomToleranceObject. Old data associated with the label will be lost.
        """
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_GeomTolerance: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_GraphNode(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    This attribute allow user multirelation tree of labels. This GraphNode is experimental Graph that not control looping and redundance. Attribute containing sequence of father's and child's labels. Provide create and work with Graph in XCAFDocument.This attribute allow user multirelation tree of labels. This GraphNode is experimental Graph that not control looping and redundance. Attribute containing sequence of father's and child's labels. Provide create and work with Graph in XCAFDocument.This attribute allow user multirelation tree of labels. This GraphNode is experimental Graph that not control looping and redundance. Attribute containing sequence of father's and child's labels. Provide create and work with Graph in XCAFDocument.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        None
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def ChildIndex(self,Ch : XCAFDoc_GraphNode) -> int: 
        """
        Return index of <Ch>, or zero if there is no such Graphnode.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FatherIndex(self,F : XCAFDoc_GraphNode) -> int: 
        """
        Return index of <F>, or zero if there is no such Graphnode.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    @staticmethod
    def Find_s(L : OCP.TDF.TDF_Label,G : XCAFDoc_GraphNode) -> bool: 
        """
        class methods working on the node =================================== Shortcut to search a Graph node attribute with default GraphID. Returns true if found.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetChild(self,Chindex : int) -> XCAFDoc_GraphNode: 
        """
        Return GraphNode by index from GraphNodeSequence.
        """
    @staticmethod
    def GetDefaultGraphID_s() -> OCP.Standard.Standard_GUID: 
        """
        returns a default Graph ID. this ID is used by the <Set> method without explicit tree ID. Instance methods: ================
        """
    def GetFather(self,Findex : int) -> XCAFDoc_GraphNode: 
        """
        Return GraphNode by index from GraphNodeSequence.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the Graph ID (default or explicit one depending on the Set method used).
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsChild(self,F : XCAFDoc_GraphNode) -> bool: 
        """
        returns TRUE if <me> is child of <F>.
        """
    def IsFather(self,Ch : XCAFDoc_GraphNode) -> bool: 
        """
        returns TRUE if <me> is father of <Ch>.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NbChildren(self) -> int: 
        """
        return Number of Childrens GraphNodes. Implementation of Attribute methods: ===================================
        """
    def NbFathers(self) -> int: 
        """
        return Number of Fathers GraphNodes.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetChild(self,Ch : XCAFDoc_GraphNode) -> int: 
        """
        Set GraphNode <Ch> as child of me and returns index of <Ch> in Sequence that containing Children GraphNodes. return index of <Ch> from GraphNodeSequnece
        """
    def SetFather(self,F : XCAFDoc_GraphNode) -> int: 
        """
        Set GraphNode <F> as father of me and returns index of <F> in Sequence that containing Fathers GraphNodes. return index of <F> from GraphNodeSequnece
        """
    def SetGraphID(self,explicitID : OCP.Standard.Standard_GUID) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(L : OCP.TDF.TDF_Label) -> XCAFDoc_GraphNode: 
        """
        Finds or Creates a GraphNode attribute on the label <L> with the default Graph ID, returned by the method <GetDefaultGraphID>. Returns the created/found GraphNode attribute.

        Finds or Creates a GraphNode attribute on the label <L>, with an explicit tree ID. <ExplicitGraphID> is the ID returned by <TDF_Attribute::ID> method. Returns the found/created GraphNode attribute.
        """
    @staticmethod
    @overload
    def Set_s(L : OCP.TDF.TDF_Label,ExplicitGraphID : OCP.Standard.Standard_GUID) -> XCAFDoc_GraphNode: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    @overload
    def UnSetChild(self,Ch : XCAFDoc_GraphNode) -> None: 
        """
        Remove <Ch> from GraphNodeSequence. and remove link between father and child.

        Remove Child GraphNode by index from Children GraphNodeSequence. and remove link between father and child.
        """
    @overload
    def UnSetChild(self,Chindex : int) -> None: ...
    @overload
    def UnSetFather(self,Findex : int) -> None: 
        """
        Remove <F> from Fathers GraphNodeSequence. and remove link between father and child.

        Remove Father GraphNode by index from Fathers GraphNodeSequence. and remove link between father and child.
        """
    @overload
    def UnSetFather(self,F : XCAFDoc_GraphNode) -> None: ...
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_GraphNodeSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : XCAFDoc_GraphNode) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : XCAFDoc_GraphNodeSequence) -> None: ...
    def Assign(self,theOther : XCAFDoc_GraphNodeSequence) -> XCAFDoc_GraphNodeSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> XCAFDoc_GraphNode: 
        """
        First item access
        """
    def ChangeLast(self) -> XCAFDoc_GraphNode: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> XCAFDoc_GraphNode: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> XCAFDoc_GraphNode: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : XCAFDoc_GraphNodeSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : XCAFDoc_GraphNode) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDoc_GraphNode) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : XCAFDoc_GraphNodeSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> XCAFDoc_GraphNode: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theSeq : XCAFDoc_GraphNodeSequence) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : XCAFDoc_GraphNode) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : XCAFDoc_GraphNode) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : XCAFDoc_GraphNodeSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> XCAFDoc_GraphNode: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDoc_GraphNodeSequence) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class XCAFDoc_LayerTool(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Provides tools to store and retrieve attributes (Layers) of TopoDS_Shape in and from TDocStd_Document A Document is intended to hold different attributes of ONE shape and it's sub-shapes Provide tools for management of Layers section of document.Provides tools to store and retrieve attributes (Layers) of TopoDS_Shape in and from TDocStd_Document A Document is intended to hold different attributes of ONE shape and it's sub-shapes Provide tools for management of Layers section of document.Provides tools to store and retrieve attributes (Layers) of TopoDS_Shape in and from TDocStd_Document A Document is intended to hold different attributes of ONE shape and it's sub-shapes Provide tools for management of Layers section of document.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    @overload
    def AddLayer(self,theLayer : OCP.TCollection.TCollection_ExtendedString,theToFindVisible : bool) -> OCP.TDF.TDF_Label: 
        """
        Adds a Layer definition to a Layertable and returns its label (returns existing label if the same Layer is already defined)

        Adds a Layer definition to a Layertable and returns its label Returns existing label (if it is already defined) of visible or invisible layer, according to <theToFindVisible> parameter
        """
    @overload
    def AddLayer(self,theLayer : OCP.TCollection.TCollection_ExtendedString) -> OCP.TDF.TDF_Label: ...
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BaseLabel(self) -> OCP.TDF.TDF_Label: 
        """
        returns the label under which Layers are stored
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    @overload
    def FindLayer(self,aLayer : OCP.TCollection.TCollection_ExtendedString,theToFindWithProperty : bool=False,theToFindVisible : bool=True) -> OCP.TDF.TDF_Label: 
        """
        Finds a Layer definition in a Layertable and returns its label if found Returns False if Layer is not found in Layertable

        Finds a Layer definition in a Layertable by name Returns first founded label with the same name if <theToFindWithProperty> is false If <theToFindWithProperty> is true returns first label that contains or not contains visible attr, according to the <theToFindVisible> parameter
        """
    @overload
    def FindLayer(self,aLayer : OCP.TCollection.TCollection_ExtendedString,lab : OCP.TDF.TDF_Label) -> bool: ...
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetLayer(self,lab : OCP.TDF.TDF_Label,aLayer : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Returns Layer defined by label lab Returns False if the label is not in Layertable or does not define a Layer
        """
    def GetLayerLabels(self,Labels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of Layers currently stored in the Layertable
        """
    @overload
    def GetLayers(self,L : OCP.TDF.TDF_Label) -> OCP.TColStd.TColStd_HSequenceOfExtendedString: 
        """
        Return sequence of strings <aLayerS> that associated with label <L>.

        Return sequence of labels <aLayerSL> that associated with label <L>.

        Return sequence of strings that associated with label <L>.

        Return sequence of strings <aLayerS> that associated with shape <Sh>.

        Return sequence of labels <aLayerLS> that associated with shape <Sh>.

        Return sequence of strings that associated with shape <Sh>.
        """
    @overload
    def GetLayers(self,Sh : OCP.TopoDS.TopoDS_Shape,aLayerLS : OCP.TDF.TDF_LabelSequence) -> bool: ...
    @overload
    def GetLayers(self,L : OCP.TDF.TDF_Label,aLayerS : OCP.TColStd.TColStd_HSequenceOfExtendedString) -> bool: ...
    @overload
    def GetLayers(self,Sh : OCP.TopoDS.TopoDS_Shape,aLayerS : OCP.TColStd.TColStd_HSequenceOfExtendedString) -> bool: ...
    @overload
    def GetLayers(self,Sh : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_HSequenceOfExtendedString: ...
    @overload
    def GetLayers(self,L : OCP.TDF.TDF_Label,aLayerLS : OCP.TDF.TDF_LabelSequence) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShapesOfLayer(self,layerL : OCP.TDF.TDF_Label,ShLabels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Return sequanese of shape labels that assigned with layers to <ShLabels>.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsLayer(self,lab : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if label belongs to a Layertable and is a Layer definition
        """
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    @overload
    def IsSet(self,Sh : OCP.TopoDS.TopoDS_Shape,aLayer : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Returns True if label <L> has a Layer associated with the <aLayer>.

        Returns True if label <L> has a Layer associated with the <aLayerL> label.

        Returns True if shape <Sh> has a Layer associated with the <aLayer>.

        Returns True if shape <Sh> has a Layer associated with the <aLayerL>.
        """
    @overload
    def IsSet(self,L : OCP.TDF.TDF_Label,aLayer : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    @overload
    def IsSet(self,L : OCP.TDF.TDF_Label,aLayerL : OCP.TDF.TDF_Label) -> bool: ...
    @overload
    def IsSet(self,Sh : OCP.TopoDS.TopoDS_Shape,aLayerL : OCP.TDF.TDF_Label) -> bool: ...
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def IsVisible(self,layerL : OCP.TDF.TDF_Label) -> bool: 
        """
        Return TRUE if layer is visible, FALSE if invisible.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveLayer(self,lab : OCP.TDF.TDF_Label) -> None: 
        """
        Removes Layer from the Layertable
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @overload
    def SetLayer(self,Sh : OCP.TopoDS.TopoDS_Shape,aLayer : OCP.TCollection.TCollection_ExtendedString,shapeInOneLayer : bool=False) -> bool: 
        """
        Sets a link from label <L> to Layer defined by <LayerL> optional parameter <shapeInOneLayer> show could shape be in number of layers or only in one.

        Sets a link from label <L> to Layer <aLayer> in the Layertable Adds a Layer as necessary optional parameter <shapeInOneLayer> show could shape be in number of layers or only in one.

        Sets a link from label that containing shape <Sh> with layer that situated at label <LayerL>. optional parameter <shapeInOneLayer> show could shape be in number of layers or only in one. return FALSE if no such shape <Sh> or label <LayerL>

        Sets a link from label that containing shape <Sh> with layer <aLayer>. Add <aLayer> to LayerTable if nessesery. optional parameter <shapeInOneLayer> show could shape be in number of layers or only in one. return FALSE if no such shape <Sh>.
        """
    @overload
    def SetLayer(self,L : OCP.TDF.TDF_Label,aLayer : OCP.TCollection.TCollection_ExtendedString,shapeInOneLayer : bool=False) -> None: ...
    @overload
    def SetLayer(self,L : OCP.TDF.TDF_Label,LayerL : OCP.TDF.TDF_Label,shapeInOneLayer : bool=False) -> None: ...
    @overload
    def SetLayer(self,Sh : OCP.TopoDS.TopoDS_Shape,LayerL : OCP.TDF.TDF_Label,shapeInOneLayer : bool=False) -> bool: ...
    def SetVisibility(self,layerL : OCP.TDF.TDF_Label,isvisible : bool=True) -> None: 
        """
        Set the visibility of layer. If layer is invisible when on it's layer will set UAttribute with corresponding GUID.
        """
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> XCAFDoc_LayerTool: ...
    def ShapeTool(self) -> XCAFDoc_ShapeTool: 
        """
        Returns internal XCAFDoc_ShapeTool tool
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    @overload
    def UnSetLayers(self,Sh : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Removes a link from label <L> to all layers

        Remove link between shape <Sh> and all Layers at LayerTable. return FALSE if no such shape <Sh> in XCAF Document.
        """
    @overload
    def UnSetLayers(self,L : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def UnSetOneLayer(self,Sh : OCP.TopoDS.TopoDS_Shape,aLayer : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        Remove link from label <L> and Layer <aLayer>. returns FALSE if no such layer.

        Remove link from label <L> and Layer <aLayerL>. returns FALSE if <aLayerL> is not a layer label.

        Remove link between shape <Sh> and layer <aLayer>. returns FALSE if no such layer <aLayer> or shape <Sh>.

        Remove link between shape <Sh> and layer <aLayerL>. returns FALSE if no such layer <aLayerL> or shape <Sh>.
        """
    @overload
    def UnSetOneLayer(self,L : OCP.TDF.TDF_Label,aLayer : OCP.TCollection.TCollection_ExtendedString) -> bool: ...
    @overload
    def UnSetOneLayer(self,Sh : OCP.TopoDS.TopoDS_Shape,aLayerL : OCP.TDF.TDF_Label) -> bool: ...
    @overload
    def UnSetOneLayer(self,L : OCP.TDF.TDF_Label,aLayerL : OCP.TDF.TDF_Label) -> bool: ...
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_LengthUnit(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Used to define a Length Unit attribute containing a length unit infoUsed to define a Length Unit attribute containing a length unit infoUsed to define a Length Unit attribute containing a length unit info
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the GUID of the attribute.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetUnitName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Length unit description (could be arbitrary text)
        """
    def GetUnitValue(self) -> float: 
        """
        Returns length unit scale factor to meter
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,theInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theWith : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,theUnitName : OCP.TCollection.TCollection_AsciiString,theUnitValue : float) -> None: 
        """
        Creates a LengthUnit attribute
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label,theGUID : OCP.Standard.Standard_GUID,theUnitName : OCP.TCollection.TCollection_AsciiString,theUnitValue : float) -> XCAFDoc_LengthUnit: 
        """
        Finds or creates a LengthUnit attribute

        Finds or creates a LengthUnit attribute

        Finds, or creates, a LengthUnit attribute with explicit user defined GUID
        """
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label,theUnitValue : float) -> XCAFDoc_LengthUnit: ...
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label,theUnitName : OCP.TCollection.TCollection_AsciiString,theUnitValue : float) -> XCAFDoc_LengthUnit: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_Location(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    attribute to store TopLoc_Locationattribute to store TopLoc_Locationattribute to store TopLoc_Location
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Returns True if there is a reference on the same label
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,Loc : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label,Loc : OCP.TopLoc.TopLoc_Location) -> XCAFDoc_Location: 
        """
        Find, or create, a Location attribute and set it's value the Location attribute is returned. Location methods ===============
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_Material(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    attribute to store materialattribute to store materialattribute to store material
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDensName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetDensValType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetDensity(self) -> float: 
        """
        None
        """
    def GetDescription(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aDensity : float,aDensName : OCP.TCollection.TCollection_HAsciiString,aDensValType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aDensity : float,aDensName : OCP.TCollection.TCollection_HAsciiString,aDensValType : OCP.TCollection.TCollection_HAsciiString) -> XCAFDoc_Material: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_MaterialTool(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Provides tools to store and retrieve attributes (materials) of TopoDS_Shape in and from TDocStd_Document A Document is intended to hold different attributes of ONE shape and it's sub-shapes Provide tools for management of Materialss section of document.Provides tools to store and retrieve attributes (materials) of TopoDS_Shape in and from TDocStd_Document A Document is intended to hold different attributes of ONE shape and it's sub-shapes Provide tools for management of Materialss section of document.Provides tools to store and retrieve attributes (materials) of TopoDS_Shape in and from TDocStd_Document A Document is intended to hold different attributes of ONE shape and it's sub-shapes Provide tools for management of Materialss section of document.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AddMaterial(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aDensity : float,aDensName : OCP.TCollection.TCollection_HAsciiString,aDensValType : OCP.TCollection.TCollection_HAsciiString) -> OCP.TDF.TDF_Label: 
        """
        Adds a Material definition to a table and returns its label
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BaseLabel(self) -> OCP.TDF.TDF_Label: 
        """
        returns the label under which colors are stored
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetDensityForShape_s(ShapeL : OCP.TDF.TDF_Label) -> float: 
        """
        Find referred material and return density from it if no material --> return 0
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetMaterial(self,MatL : OCP.TDF.TDF_Label,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aDensity : float,aDensName : OCP.TCollection.TCollection_HAsciiString,aDensValType : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        Returns Material assigned to <MatL> Returns False if no such Material is assigned
        """
    def GetMaterialLabels(self,Labels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of materials currently stored in the material table
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsMaterial(self,lab : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if label belongs to a material table and is a Material definition
        """
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @overload
    def SetMaterial(self,L : OCP.TDF.TDF_Label,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aDensity : float,aDensName : OCP.TCollection.TCollection_HAsciiString,aDensValType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a link with GUID

        Sets a link with GUID Adds a Material as necessary
        """
    @overload
    def SetMaterial(self,L : OCP.TDF.TDF_Label,MatL : OCP.TDF.TDF_Label) -> None: ...
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> XCAFDoc_MaterialTool: ...
    def ShapeTool(self) -> XCAFDoc_ShapeTool: 
        """
        Returns internal XCAFDoc_ShapeTool tool
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_Note(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    A base note attribute. Any note contains the name of the user created the note and the creation timestamp.A base note attribute. Any note contains the name of the user created the note and the creation timestamp.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,theOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetObject(self) -> OCP.XCAFNoteObjects.XCAFNoteObjects_NoteObject: 
        """
        Returns auxiliary data object
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_Note: 
        """
        Finds a reference attribute on the given label and returns it, if it is found
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    @staticmethod
    def IsMine_s(theLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks if the given label represents a note.
        """
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsOrphan(self) -> bool: 
        """
        Checks if the note isn't linked to annotated items.
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty attribute from the good end type. It is used by the copy algorithm.
        """
    def Paste(self,theAttrInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theAttrFrom : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,theUserName : OCP.TCollection.TCollection_ExtendedString,theTimeStamp : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Sets the user name and the timestamp of the note.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetObject(self,theObject : OCP.XCAFNoteObjects.XCAFNoteObjects_NoteObject) -> None: 
        """
        Updates auxiliary data
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TimeStamp(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the timestamp of the note.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def UserName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the user name, who created the note.
        """
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
class XCAFDoc_NoteComment(XCAFDoc_Note, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    A comment note attribute. Contains a textual comment.A comment note attribute. Contains a textual comment.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Comment(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the comment text.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,theOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns default attribute GUID
        """
    def GetObject(self) -> OCP.XCAFNoteObjects.XCAFNoteObjects_NoteObject: 
        """
        Returns auxiliary data object
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_NoteComment: 
        """
        Finds a reference attribute on the given label and returns it, if it is found
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    @staticmethod
    def IsMine_s(theLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks if the given label represents a note.
        """
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsOrphan(self) -> bool: 
        """
        Checks if the note isn't linked to annotated items.
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,theAttrInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theAttrFrom : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,theComment : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Sets the comment text.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetObject(self,theObject : OCP.XCAFNoteObjects.XCAFNoteObjects_NoteObject) -> None: 
        """
        Updates auxiliary data
        """
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label,theUserName : OCP.TCollection.TCollection_ExtendedString,theTimeStamp : OCP.TCollection.TCollection_ExtendedString,theComment : OCP.TCollection.TCollection_ExtendedString) -> XCAFDoc_NoteComment: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TimeStamp(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the timestamp of the note.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def UserName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the user name, who created the note.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_NoteBinData(XCAFDoc_Note, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Data(self) -> OCP.TColStd.TColStd_HArray1OfByte: 
        """
        Returns byte data array.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,theOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns default attribute GUID
        """
    def GetObject(self) -> OCP.XCAFNoteObjects.XCAFNoteObjects_NoteObject: 
        """
        Returns auxiliary data object
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_NoteBinData: 
        """
        Finds a binary data attribute on the given label and returns it, if it is found
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    @staticmethod
    def IsMine_s(theLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks if the given label represents a note.
        """
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsOrphan(self) -> bool: 
        """
        Checks if the note isn't linked to annotated items.
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def MIMEtype(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns data MIME type.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,theAttrInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theAttrFrom : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def Set(self,theTitle : OCP.TCollection.TCollection_ExtendedString,theMIMEtype : OCP.TCollection.TCollection_AsciiString,theFile : OCP.OSD.OSD_File) -> bool: 
        """
        Sets title, MIME type and data from a binary file.

        Sets title, MIME type and data from a byte array.
        """
    @overload
    def Set(self,theTitle : OCP.TCollection.TCollection_ExtendedString,theMIMEtype : OCP.TCollection.TCollection_AsciiString,theData : OCP.TColStd.TColStd_HArray1OfByte) -> None: ...
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetObject(self,theObject : OCP.XCAFNoteObjects.XCAFNoteObjects_NoteObject) -> None: 
        """
        Updates auxiliary data
        """
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label,theUserName : OCP.TCollection.TCollection_ExtendedString,theTimeStamp : OCP.TCollection.TCollection_ExtendedString,theTitle : OCP.TCollection.TCollection_ExtendedString,theMIMEtype : OCP.TCollection.TCollection_AsciiString,theData : OCP.TColStd.TColStd_HArray1OfByte) -> XCAFDoc_NoteBinData: ...
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label,theUserName : OCP.TCollection.TCollection_ExtendedString,theTimeStamp : OCP.TCollection.TCollection_ExtendedString,theTitle : OCP.TCollection.TCollection_ExtendedString,theMIMEtype : OCP.TCollection.TCollection_AsciiString,theFile : OCP.OSD.OSD_File) -> XCAFDoc_NoteBinData: ...
    def Size(self) -> int: 
        """
        Size of data in bytes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TimeStamp(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the timestamp of the note.
        """
    def Title(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the note title.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def UserName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the user name, who created the note.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_NoteBalloon(XCAFDoc_NoteComment, XCAFDoc_Note, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    A comment note attribute. Contains a textual comment.A comment note attribute. Contains a textual comment.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Comment(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the comment text.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,theOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns default attribute GUID
        """
    def GetObject(self) -> OCP.XCAFNoteObjects.XCAFNoteObjects_NoteObject: 
        """
        Returns auxiliary data object
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_NoteBalloon: 
        """
        Finds a reference attribute on the given label and returns it, if it is found
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    @staticmethod
    def IsMine_s(theLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Checks if the given label represents a note.
        """
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsOrphan(self) -> bool: 
        """
        Checks if the note isn't linked to annotated items.
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,theAttrInto : OCP.TDF.TDF_Attribute,theRT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theAttrFrom : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,theComment : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Sets the comment text.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetObject(self,theObject : OCP.XCAFNoteObjects.XCAFNoteObjects_NoteObject) -> None: 
        """
        Updates auxiliary data
        """
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label,theUserName : OCP.TCollection.TCollection_ExtendedString,theTimeStamp : OCP.TCollection.TCollection_ExtendedString,theComment : OCP.TCollection.TCollection_ExtendedString) -> XCAFDoc_NoteBalloon: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TimeStamp(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the timestamp of the note.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def UserName(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        Returns the user name, who created the note.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_NotesTool(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    A tool to annotate items in the hierarchical product structure. There are two basic entities, which operates the notes tool: notes and annotated items. A note is a user defined data structure derived from XCAFDoc_Note attribute that is attached to a separate label under the notes hive. An annotated item is represented by XCAFDoc_AssemblyItemRef attribute attached to a separate label under the annotated items hive. Notes are linked with annotated items by means of XCAFDoc_GraphNode attribute. Notes play parent roles and annotated items - child roles.A tool to annotate items in the hierarchical product structure. There are two basic entities, which operates the notes tool: notes and annotated items. A note is a user defined data structure derived from XCAFDoc_Note attribute that is attached to a separate label under the notes hive. An annotated item is represented by XCAFDoc_AssemblyItemRef attribute attached to a separate label under the annotated items hive. Notes are linked with annotated items by means of XCAFDoc_GraphNode attribute. Notes play parent roles and annotated items - child roles.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    @overload
    def AddNote(self,theNoteLabel : OCP.TDF.TDF_Label,theItemId : XCAFDoc_AssemblyItemId) -> XCAFDoc_AssemblyItemRef: 
        """
        Adds the given note to the assembly item.

        Adds the given note to the labeled item.
        """
    @overload
    def AddNote(self,theNoteLabel : OCP.TDF.TDF_Label,theItemLabel : OCP.TDF.TDF_Label) -> XCAFDoc_AssemblyItemRef: ...
    @overload
    def AddNoteToAttr(self,theNoteLabel : OCP.TDF.TDF_Label,theItemLabel : OCP.TDF.TDF_Label,theGUID : OCP.Standard.Standard_GUID) -> XCAFDoc_AssemblyItemRef: 
        """
        Adds the given note to the assembly item's attribute.

        Adds the given note to the labeled item's attribute.
        """
    @overload
    def AddNoteToAttr(self,theNoteLabel : OCP.TDF.TDF_Label,theItemId : XCAFDoc_AssemblyItemId,theGUID : OCP.Standard.Standard_GUID) -> XCAFDoc_AssemblyItemRef: ...
    @overload
    def AddNoteToSubshape(self,theNoteLabel : OCP.TDF.TDF_Label,theItemId : XCAFDoc_AssemblyItemId,theSubshapeIndex : int) -> XCAFDoc_AssemblyItemRef: 
        """
        Adds the given note to the assembly item's subshape.

        Adds the given note to the labeled item's subshape.
        """
    @overload
    def AddNoteToSubshape(self,theNoteLabel : OCP.TDF.TDF_Label,theItemLabel : OCP.TDF.TDF_Label,theSubshapeIndex : int) -> XCAFDoc_AssemblyItemRef: ...
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def CreateBalloon(self,theUserName : OCP.TCollection.TCollection_ExtendedString,theTimeStamp : OCP.TCollection.TCollection_ExtendedString,theComment : OCP.TCollection.TCollection_ExtendedString) -> XCAFDoc_Note: 
        """
        Create a new 'balloon' note. Creates a new label under the notes hive and attaches XCAFDoc_NoteBalloon attribute (derived ftom XCAFDoc_Note).
        """
    @overload
    def CreateBinData(self,theUserName : OCP.TCollection.TCollection_ExtendedString,theTimeStamp : OCP.TCollection.TCollection_ExtendedString,theTitle : OCP.TCollection.TCollection_ExtendedString,theMIMEtype : OCP.TCollection.TCollection_AsciiString,theData : OCP.TColStd.TColStd_HArray1OfByte) -> XCAFDoc_Note: 
        """
        Create a new note with data loaded from a binary file. Creates a new label under the notes hive and attaches XCAFDoc_NoteComment attribute (derived ftom XCAFDoc_Note).

        Create a new note with data loaded from a byte data array. Creates a new label under the notes hive and attaches XCAFDoc_NoteComment attribute (derived ftom XCAFDoc_Note).
        """
    @overload
    def CreateBinData(self,theUserName : OCP.TCollection.TCollection_ExtendedString,theTimeStamp : OCP.TCollection.TCollection_ExtendedString,theTitle : OCP.TCollection.TCollection_ExtendedString,theMIMEtype : OCP.TCollection.TCollection_AsciiString,theFile : OCP.OSD.OSD_File) -> XCAFDoc_Note: ...
    def CreateComment(self,theUserName : OCP.TCollection.TCollection_ExtendedString,theTimeStamp : OCP.TCollection.TCollection_ExtendedString,theComment : OCP.TCollection.TCollection_ExtendedString) -> XCAFDoc_Note: 
        """
        Create a new comment note. Creates a new label under the notes hive and attaches XCAFDoc_NoteComment attribute (derived ftom XCAFDoc_Note).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeleteAllNotes(self) -> int: 
        """
        Deletes all notes. Clears all annotations.
        """
    def DeleteNote(self,theNoteLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Deletes the given note. Removes all links with items annotated by the note.
        """
    def DeleteNotes(self,theNoteLabels : OCP.TDF.TDF_LabelSequence) -> int: 
        """
        Deletes the given notes. Removes all links with items annotated by the notes.
        """
    def DeleteOrphanNotes(self) -> int: 
        """
        Deletes all notes that aren't linked to annotated items.
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,theOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    @overload
    def FindAnnotatedItem(self,theItemId : XCAFDoc_AssemblyItemId) -> OCP.TDF.TDF_Label: 
        """
        Finds a label of the given assembly item ID in the annotated items hive.

        Finds a label of the given labeled item in the annotated items hive.
        """
    @overload
    def FindAnnotatedItem(self,theItemLabel : OCP.TDF.TDF_Label) -> OCP.TDF.TDF_Label: ...
    @overload
    def FindAnnotatedItemAttr(self,theItemLabel : OCP.TDF.TDF_Label,theGUID : OCP.Standard.Standard_GUID) -> OCP.TDF.TDF_Label: 
        """
        Finds a label of the given assembly item's attribute in the annotated items hive.

        Finds a label of the given labeled item's attribute in the annotated items hive.
        """
    @overload
    def FindAnnotatedItemAttr(self,theItemId : XCAFDoc_AssemblyItemId,theGUID : OCP.Standard.Standard_GUID) -> OCP.TDF.TDF_Label: ...
    @overload
    def FindAnnotatedItemSubshape(self,theItemId : XCAFDoc_AssemblyItemId,theSubshapeIndex : int) -> OCP.TDF.TDF_Label: 
        """
        Finds a label of the given assembly item's subshape in the annotated items hive.

        Finds a label of the given labeled item's subshape in the annotated items hive.
        """
    @overload
    def FindAnnotatedItemSubshape(self,theItemLabel : OCP.TDF.TDF_Label,theSubshapeIndex : int) -> OCP.TDF.TDF_Label: ...
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetAnnotatedItems(self,theLabels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns all labels from the annotated items hive. The label sequence isn't cleared beforehand.
        """
    def GetAnnotatedItemsLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label of the annotated items hive.
        """
    @overload
    def GetAttrNotes(self,theItemId : XCAFDoc_AssemblyItemId,theGUID : OCP.Standard.Standard_GUID,theNoteLabels : OCP.TDF.TDF_LabelSequence) -> int: 
        """
        Gets all note labels of the assembly item's attribute. Notes linked to the item itself or to item's subshapes aren't taken into account. The label sequence isn't cleared beforehand.

        Gets all note labels of the labeled item's attribute. Notes linked to the item itself or to item's subshapes aren't taken into account. The label sequence isn't cleared beforehand.
        """
    @overload
    def GetAttrNotes(self,theItemLabel : OCP.TDF.TDF_Label,theGUID : OCP.Standard.Standard_GUID,theNoteLabels : OCP.TDF.TDF_LabelSequence) -> int: ...
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns default attribute GUID
        """
    @overload
    def GetNotes(self,theItemLabel : OCP.TDF.TDF_Label,theNoteLabels : OCP.TDF.TDF_LabelSequence) -> int: 
        """
        Returns all labels from the notes hive. The label sequence isn't cleared beforehand.

        Gets all note labels of the assembly item. Notes linked to item's subshapes or attributes aren't taken into account. The label sequence isn't cleared beforehand.

        Gets all note labels of the labeled item. Notes linked to item's attributes aren't taken into account. The label sequence isn't cleared beforehand.
        """
    @overload
    def GetNotes(self,theItemId : XCAFDoc_AssemblyItemId,theNoteLabels : OCP.TDF.TDF_LabelSequence) -> int: ...
    @overload
    def GetNotes(self,theNoteLabels : OCP.TDF.TDF_LabelSequence) -> None: ...
    def GetNotesLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label of the notes hive.
        """
    def GetOrphanNotes(self,theNoteLabels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns note labels that aren't linked to annotated items. The label sequence isn't cleared beforehand.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSubshapeNotes(self,theItemId : XCAFDoc_AssemblyItemId,theSubshapeIndex : int,theNoteLabels : OCP.TDF.TDF_LabelSequence) -> int: 
        """
        Gets all note labels of the annotated item. Notes linked to the item itself or to item's attributes taken into account. The label sequence isn't cleared beforehand.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        @}
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IsAnnotatedItem(self,theItemId : XCAFDoc_AssemblyItemId) -> bool: 
        """
        Checks if the given assembly item is annotated.

        Checks if the given labeled item is annotated.
        """
    @overload
    def IsAnnotatedItem(self,theItemLabel : OCP.TDF.TDF_Label) -> bool: ...
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NbAnnotatedItems(self) -> int: 
        """
        Returns the number of labels in the annotated items hive.
        """
    def NbNotes(self) -> int: 
        """
        Returns the number of labels in the notes hive.
        """
    def NbOrphanNotes(self) -> int: 
        """
        Returns number of notes that aren't linked to annotated items.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    @overload
    def RemoveAllAttrNotes(self,theItemId : XCAFDoc_AssemblyItemId,theGUID : OCP.Standard.Standard_GUID,theDelIfOrphan : bool=False) -> bool: 
        """
        Removes all notes from the assembly item's attribute.

        Removes all notes from the labeled item's attribute.
        """
    @overload
    def RemoveAllAttrNotes(self,theItemLabel : OCP.TDF.TDF_Label,theGUID : OCP.Standard.Standard_GUID,theDelIfOrphan : bool=False) -> bool: ...
    @overload
    def RemoveAllNotes(self,theItemId : XCAFDoc_AssemblyItemId,theDelIfOrphan : bool=False) -> bool: 
        """
        Removes all notes from the assembly item.

        Removes all notes from the labeled item.
        """
    @overload
    def RemoveAllNotes(self,theItemLabel : OCP.TDF.TDF_Label,theDelIfOrphan : bool=False) -> bool: ...
    def RemoveAllSubshapeNotes(self,theItemId : XCAFDoc_AssemblyItemId,theSubshapeIndex : int,theDelIfOrphan : bool=False) -> bool: 
        """
        Removes all notes from the assembly item's subshape.
        """
    @overload
    def RemoveAttrNote(self,theNoteLabel : OCP.TDF.TDF_Label,theItemId : XCAFDoc_AssemblyItemId,theGUID : OCP.Standard.Standard_GUID,theDelIfOrphan : bool=False) -> bool: 
        """
        Removes a note from the assembly item's attribute.

        Removes a note from the labeled item's attribute.
        """
    @overload
    def RemoveAttrNote(self,theNoteLabel : OCP.TDF.TDF_Label,theItemLabel : OCP.TDF.TDF_Label,theGUID : OCP.Standard.Standard_GUID,theDelIfOrphan : bool=False) -> bool: ...
    @overload
    def RemoveNote(self,theNoteLabel : OCP.TDF.TDF_Label,theItemId : XCAFDoc_AssemblyItemId,theDelIfOrphan : bool=False) -> bool: 
        """
        Removes the given note from the assembly item.

        Removes the given note from the labeled item.
        """
    @overload
    def RemoveNote(self,theNoteLabel : OCP.TDF.TDF_Label,theItemLabel : OCP.TDF.TDF_Label,theDelIfOrphan : bool=False) -> bool: ...
    @overload
    def RemoveSubshapeNote(self,theNoteLabel : OCP.TDF.TDF_Label,theItemLabel : OCP.TDF.TDF_Label,theSubshapeIndex : int,theDelIfOrphan : bool=False) -> bool: 
        """
        Removes the given note from the assembly item's subshape.

        Removes the given note from the labeled item's subshape.
        """
    @overload
    def RemoveSubshapeNote(self,theNoteLabel : OCP.TDF.TDF_Label,theItemId : XCAFDoc_AssemblyItemId,theSubshapeIndex : int,theDelIfOrphan : bool=False) -> bool: ...
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_NotesTool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_ShapeMapTool(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    attribute containing map of sub shapesattribute containing map of sub shapesattribute containing map of sub shapes
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetMap(self) -> OCP.TopTools.TopTools_IndexedMapOfShape: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsSubShape(self,sub : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks whether shape is subshape of shape stored on label shapeL
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetShape(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets representation (TopoDS_Shape) for top-level shape
        """
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> XCAFDoc_ShapeMapTool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_ShapeTool(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    A tool to store shapes in an XDE document in the form of assembly structure, and to maintain this structure. Attribute containing Shapes section of DECAF document. Provide tools for management of Shapes section. The API provided by this class allows to work with this structure regardless of its low-level implementation. All the shapes are stored on child labels of a main label which is XCAFDoc_DocumentTool::LabelShapes(). The label for assembly also has sub-labels, each of which represents the instance of another shape in that assembly (component). Such sub-label stores reference to the label of the original shape in the form of TDataStd_TreeNode with GUID XCAFDoc::ShapeRefGUID(), and its location encapsulated into the NamedShape. For correct work with an XDE document, it is necessary to use methods for analysis and methods for working with shapes. For example: if ( STool->IsAssembly(aLabel) ) { Standard_Boolean subchilds = Standard_False; (default) Standard_Integer nbc = STool->NbComponents (aLabel[,subchilds]); } If subchilds is True, commands also consider sub-levels. By default, only level one is checked. In this example, number of children from the first level of assembly will be returned. Methods for creation and initialization: Constructor: XCAFDoc_ShapeTool::XCAFDoc_ShapeTool() Getting a guid: Standard_GUID GetID (); Creation (if does not exist) of ShapeTool on label L: Handle(XCAFDoc_ShapeTool) XCAFDoc_ShapeTool::Set(const TDF_Label& L) Analyze whether shape is a simple shape or an instance or a component of an assembly or it is an assembly ( methods of analysis). For example: STool->IsShape(aLabel) ; Analyze that the label represents a shape (simple shape, assembly or reference) or STool->IsTopLevel(aLabel); Analyze that the label is a label of a top-level shape. Work with simple shapes, assemblies and instances ( methods for work with shapes). For example: Add shape: Standard_Boolean makeAssembly; // True to interpret a Compound as an Assembly, False to take it as a whole aLabel = STool->AddShape(aShape, makeAssembly); Get shape: TDF_Label aLabel... // A label must be present if (aLabel.IsNull()) { ... no such label : abandon .. } TopoDS_Shape aShape; aShape = STool->GetShape(aLabel); if (aShape.IsNull()) { ... this label is not for a Shape ... } To get a label from shape. Standard_Boolean findInstance = Standard_False; (this is default value) aLabel = STool->FindShape(aShape [,findInstance]); if (aLabel.IsNull()) { ... no label found for this shape ... }A tool to store shapes in an XDE document in the form of assembly structure, and to maintain this structure. Attribute containing Shapes section of DECAF document. Provide tools for management of Shapes section. The API provided by this class allows to work with this structure regardless of its low-level implementation. All the shapes are stored on child labels of a main label which is XCAFDoc_DocumentTool::LabelShapes(). The label for assembly also has sub-labels, each of which represents the instance of another shape in that assembly (component). Such sub-label stores reference to the label of the original shape in the form of TDataStd_TreeNode with GUID XCAFDoc::ShapeRefGUID(), and its location encapsulated into the NamedShape. For correct work with an XDE document, it is necessary to use methods for analysis and methods for working with shapes. For example: if ( STool->IsAssembly(aLabel) ) { Standard_Boolean subchilds = Standard_False; (default) Standard_Integer nbc = STool->NbComponents (aLabel[,subchilds]); } If subchilds is True, commands also consider sub-levels. By default, only level one is checked. In this example, number of children from the first level of assembly will be returned. Methods for creation and initialization: Constructor: XCAFDoc_ShapeTool::XCAFDoc_ShapeTool() Getting a guid: Standard_GUID GetID (); Creation (if does not exist) of ShapeTool on label L: Handle(XCAFDoc_ShapeTool) XCAFDoc_ShapeTool::Set(const TDF_Label& L) Analyze whether shape is a simple shape or an instance or a component of an assembly or it is an assembly ( methods of analysis). For example: STool->IsShape(aLabel) ; Analyze that the label represents a shape (simple shape, assembly or reference) or STool->IsTopLevel(aLabel); Analyze that the label is a label of a top-level shape. Work with simple shapes, assemblies and instances ( methods for work with shapes). For example: Add shape: Standard_Boolean makeAssembly; // True to interpret a Compound as an Assembly, False to take it as a whole aLabel = STool->AddShape(aShape, makeAssembly); Get shape: TDF_Label aLabel... // A label must be present if (aLabel.IsNull()) { ... no such label : abandon .. } TopoDS_Shape aShape; aShape = STool->GetShape(aLabel); if (aShape.IsNull()) { ... this label is not for a Shape ... } To get a label from shape. Standard_Boolean findInstance = Standard_False; (this is default value) aLabel = STool->FindShape(aShape [,findInstance]); if (aLabel.IsNull()) { ... no label found for this shape ... }A tool to store shapes in an XDE document in the form of assembly structure, and to maintain this structure. Attribute containing Shapes section of DECAF document. Provide tools for management of Shapes section. The API provided by this class allows to work with this structure regardless of its low-level implementation. All the shapes are stored on child labels of a main label which is XCAFDoc_DocumentTool::LabelShapes(). The label for assembly also has sub-labels, each of which represents the instance of another shape in that assembly (component). Such sub-label stores reference to the label of the original shape in the form of TDataStd_TreeNode with GUID XCAFDoc::ShapeRefGUID(), and its location encapsulated into the NamedShape. For correct work with an XDE document, it is necessary to use methods for analysis and methods for working with shapes. For example: if ( STool->IsAssembly(aLabel) ) { Standard_Boolean subchilds = Standard_False; (default) Standard_Integer nbc = STool->NbComponents (aLabel[,subchilds]); } If subchilds is True, commands also consider sub-levels. By default, only level one is checked. In this example, number of children from the first level of assembly will be returned. Methods for creation and initialization: Constructor: XCAFDoc_ShapeTool::XCAFDoc_ShapeTool() Getting a guid: Standard_GUID GetID (); Creation (if does not exist) of ShapeTool on label L: Handle(XCAFDoc_ShapeTool) XCAFDoc_ShapeTool::Set(const TDF_Label& L) Analyze whether shape is a simple shape or an instance or a component of an assembly or it is an assembly ( methods of analysis). For example: STool->IsShape(aLabel) ; Analyze that the label represents a shape (simple shape, assembly or reference) or STool->IsTopLevel(aLabel); Analyze that the label is a label of a top-level shape. Work with simple shapes, assemblies and instances ( methods for work with shapes). For example: Add shape: Standard_Boolean makeAssembly; // True to interpret a Compound as an Assembly, False to take it as a whole aLabel = STool->AddShape(aShape, makeAssembly); Get shape: TDF_Label aLabel... // A label must be present if (aLabel.IsNull()) { ... no such label : abandon .. } TopoDS_Shape aShape; aShape = STool->GetShape(aLabel); if (aShape.IsNull()) { ... this label is not for a Shape ... } To get a label from shape. Standard_Boolean findInstance = Standard_False; (this is default value) aLabel = STool->FindShape(aShape [,findInstance]); if (aLabel.IsNull()) { ... no label found for this shape ... }
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    @overload
    def AddComponent(self,assembly : OCP.TDF.TDF_Label,comp : OCP.TopoDS.TopoDS_Shape,expand : bool=False) -> OCP.TDF.TDF_Label: 
        """
        Adds a component given by its label and location to the assembly Note: assembly must be IsAssembly() or IsSimpleShape()

        Adds a shape (located) as a component to the assembly If necessary, creates an additional top-level shape for component and return the Label of component. If expand is True and component is Compound, it will be created as assembly also Note: assembly must be IsAssembly() or IsSimpleShape()
        """
    @overload
    def AddComponent(self,assembly : OCP.TDF.TDF_Label,comp : OCP.TDF.TDF_Label,Loc : OCP.TopLoc.TopLoc_Location) -> OCP.TDF.TDF_Label: ...
    def AddShape(self,S : OCP.TopoDS.TopoDS_Shape,makeAssembly : bool=True,makePrepare : bool=True) -> OCP.TDF.TDF_Label: 
        """
        Adds a new top-level (creates and returns a new label) If makeAssembly is True, treats TopAbs_COMPOUND shapes as assemblies (creates assembly structure). NOTE: <makePrepare> replace components without location in assembly by located components to avoid some problems. If AutoNaming() is True then automatically attaches names.
        """
    @overload
    def AddSubShape(self,shapeL : OCP.TDF.TDF_Label,sub : OCP.TopoDS.TopoDS_Shape,addedSubShapeL : OCP.TDF.TDF_Label) -> bool: 
        """
        Adds a label for subshape of shape stored on label shapeL Returns Null label if it is not subshape
        """
    @overload
    def AddSubShape(self,shapeL : OCP.TDF.TDF_Label,sub : OCP.TopoDS.TopoDS_Shape) -> OCP.TDF.TDF_Label: ...
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    @staticmethod
    def AutoNaming_s() -> bool: 
        """
        Returns current auto-naming mode. See SetAutoNaming() for description.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BaseLabel(self) -> OCP.TDF.TDF_Label: 
        """
        returns the label under which shapes are stored
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def ComputeShapes(self,L : OCP.TDF.TDF_Label) -> None: 
        """
        recursive
        """
    def ComputeSimpleShapes(self) -> None: 
        """
        Compute a sequence of simple shapes
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    @overload
    def Dump(self,theDumpLog : io.BytesIO,deep : bool) -> io.BytesIO: 
        """
        None

        None
        """
    @overload
    def Dump(self,theDumpLog : io.BytesIO) -> io.BytesIO: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    @staticmethod
    def DumpShape_s(theDumpLog : io.BytesIO,L : OCP.TDF.TDF_Label,level : int=0,deep : bool=False) -> None: 
        """
        Print to std::ostream <theDumpLog> type of shape found on <L> label and the entry of <L>, with <level> tabs before. If <deep>, print also TShape and Location addresses
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Expand(self,Shape : OCP.TDF.TDF_Label) -> bool: 
        """
        Convert Shape (compound/compsolid/shell/wire) to assembly
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def FindComponent(self,theShape : OCP.TopoDS.TopoDS_Shape,Labels : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Search the path of labels in the document, that corresponds the component from any assembly Try to search the sequence of labels with location that produce this shape as component of any assembly NOTE: Clear sequence of labels before filling
        """
    def FindMainShape(self,sub : OCP.TopoDS.TopoDS_Shape) -> OCP.TDF.TDF_Label: 
        """
        Performs a search among top-level shapes to find the shape containing as subshape Checks only simple shapes, and returns the first found label (which should be the only one for valid model)
        """
    def FindMainShapeUsingMap(self,sub : OCP.TopoDS.TopoDS_Shape) -> OCP.TDF.TDF_Label: 
        """
        None
        """
    @staticmethod
    def FindSHUO_s(Labels : OCP.TDF.TDF_LabelSequence,theSHUOAttr : XCAFDoc_GraphNode) -> bool: 
        """
        Searches the SHUO by labels of components from upper_usage component to next_usage Returns null attribute if no SHUO found
        """
    @overload
    def FindShape(self,S : OCP.TopoDS.TopoDS_Shape,L : OCP.TDF.TDF_Label,findInstance : bool=False) -> bool: 
        """
        Returns the label corresponding to shape S (searches among top-level shapes, not including subcomponents of assemblies and subshapes) If findInstance is False (default), search for the input shape without location If findInstance is True, searches for the input shape as is. Return True if <S> is found.

        Does the same as previous method Returns Null label if not found
        """
    @overload
    def FindShape(self,S : OCP.TopoDS.TopoDS_Shape,findInstance : bool=False) -> OCP.TDF.TDF_Label: ...
    def FindSubShape(self,shapeL : OCP.TDF.TDF_Label,sub : OCP.TopoDS.TopoDS_Shape,L : OCP.TDF.TDF_Label) -> bool: 
        """
        Finds a label for subshape of shape stored on label shapeL Returns Null label if it is not found
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetAllComponentSHUO_s(CompLabel : OCP.TDF.TDF_Label,SHUOAttrs : OCP.TDF.TDF_AttributeSequence) -> bool: 
        """
        Returns founded SHUO GraphNodes of indicated component Returns false in other case
        """
    def GetAllSHUOInstances(self,theSHUO : XCAFDoc_GraphNode,theSHUOShapeSeq : OCP.TopTools.TopTools_SequenceOfShape) -> bool: 
        """
        Searching for component shapes that styled by shuo Returns empty sequence of shape if no any shape is found.
        """
    @staticmethod
    def GetComponents_s(L : OCP.TDF.TDF_Label,Labels : OCP.TDF.TDF_LabelSequence,getsubchilds : bool=False) -> bool: 
        """
        Returns list of components of assembly Returns False if label is not assembly
        """
    @staticmethod
    def GetExternRefs_s(L : OCP.TDF.TDF_Label,SHAS : OCP.TColStd.TColStd_SequenceOfHAsciiString) -> None: 
        """
        Gets the names of references on the no-step files
        """
    def GetFreeShapes(self,FreeLabels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of all top-level shapes which are free (i.e. not referred by any other)
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    def GetLocation_s(L : OCP.TDF.TDF_Label) -> OCP.TopLoc.TopLoc_Location: 
        """
        Returns location of instance
        """
    @overload
    def GetNamedProperties(self,theLabel : OCP.TDF.TDF_Label,theToCreate : bool=False) -> OCP.TDataStd.TDataStd_NamedData: 
        """
        Method to get NamedData attribute assigned to the given shape label.

        Method to get NamedData attribute assigned to a label of the given shape.
        """
    @overload
    def GetNamedProperties(self,theShape : OCP.TopoDS.TopoDS_Shape,theToCreate : bool=False) -> OCP.TDataStd.TDataStd_NamedData: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def GetReferredShape_s(L : OCP.TDF.TDF_Label,Label : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns label which corresponds to a shape referred by L Returns False if label is not reference
        """
    def GetSHUOInstance(self,theSHUO : XCAFDoc_GraphNode) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Search for the component shape that styled by shuo Returns null shape if no any shape is found.
        """
    @staticmethod
    def GetSHUONextUsage_s(UpperUsageL : OCP.TDF.TDF_Label,Labels : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns the sequence of labels of SHUO attributes, which is next_usage for this upper_usage SHUO attribute (that indicated by label) NOTE: returns next_usages only on one level (not recurse) NOTE: do not clear the sequence before filling
        """
    @staticmethod
    def GetSHUOUpperUsage_s(NextUsageL : OCP.TDF.TDF_Label,Labels : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns the sequence of labels of SHUO attributes, which is upper_usage for this next_usage SHUO attribute (that indicated by label) NOTE: returns upper_usages only on one level (not recurse) NOTE: do not clear the sequence before filling
        """
    @staticmethod
    def GetSHUO_s(SHUOLabel : OCP.TDF.TDF_Label,aSHUOAttr : XCAFDoc_GraphNode) -> bool: 
        """
        Returns founded SHUO GraphNode attribute <aSHUOAttr> Returns false in other case
        """
    @staticmethod
    @overload
    def GetShape_s(L : OCP.TDF.TDF_Label) -> OCP.TopoDS.TopoDS_Shape: 
        """
        To get TopoDS_Shape from shape's label For component, returns new shape with correct location Returns False if label does not contain shape

        To get TopoDS_Shape from shape's label For component, returns new shape with correct location Returns Null shape if label does not contain shape
        """
    @staticmethod
    @overload
    def GetShape_s(L : OCP.TDF.TDF_Label,S : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def GetShapes(self,Labels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of all top-level shapes
        """
    @staticmethod
    def GetSubShapes_s(L : OCP.TDF.TDF_Label,Labels : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns list of labels identifying subshapes of the given shape Returns False if no subshapes are placed on that label
        """
    @staticmethod
    def GetUsers_s(L : OCP.TDF.TDF_Label,Labels : OCP.TDF.TDF_LabelSequence,getsubchilds : bool=False) -> int: 
        """
        Returns list of labels which refer shape L as component Returns number of users (0 if shape is free)
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        set hasComponents into false
        """
    @staticmethod
    def IsAssembly_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if the label is a label of assembly, i.e. contains sublabels which are assembly components This is relevant only if IsShape() is True
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    @staticmethod
    def IsComponent_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Return true if <L> is reference serving as component of assembly
        """
    @staticmethod
    def IsCompound_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if the label is a label of compound, i.e. contains some sublabels This is relevant only if IsShape() is True
        """
    @staticmethod
    def IsExternRef_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if the label is a label of external references, i.e. there are some reference on the no-step files, which are described in document only their names
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
        """
    @staticmethod
    def IsFree_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if the label is not used by any assembly, i.e. contains sublabels which are assembly components This is relevant only if IsShape() is True (There is no Father TreeNode on this <L>)
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    @staticmethod
    def IsReference_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Return true if <L> is a located instance of other shape i.e. reference
        """
    @staticmethod
    def IsShape_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if the label represents a shape (simple shape, assembly or reference)
        """
    @staticmethod
    def IsSimpleShape_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if the label is a label of simple shape
        """
    def IsSubShape(self,shapeL : OCP.TDF.TDF_Label,sub : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks whether shape is subshape of shape stored on label shapeL
        """
    @staticmethod
    def IsSubShape_s(L : OCP.TDF.TDF_Label) -> bool: 
        """
        Return true if <L> is subshape of the top-level shape
        """
    def IsTopLevel(self,L : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if the label is a label of top-level shape, as opposed to component of assembly or subshape
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    @staticmethod
    def NbComponents_s(L : OCP.TDF.TDF_Label,getsubchilds : bool=False) -> int: 
        """
        Returns number of Assembles components
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def NewShape(self) -> OCP.TDF.TDF_Label: 
        """
        Creates new (empty) top-level shape. Initially it holds empty TopoDS_Compound
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveComponent(self,comp : OCP.TDF.TDF_Label) -> None: 
        """
        Removes a component from its assembly
        """
    def RemoveSHUO(self,SHUOLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Remove SHUO from component sublabel, remove all dependencies on other SHUO. Returns FALSE if cannot remove SHUO dependencies. NOTE: remove any styles that associated with this SHUO.
        """
    def RemoveShape(self,L : OCP.TDF.TDF_Label,removeCompletely : bool=True) -> bool: 
        """
        Removes shape (whole label and all its sublabels) If removeCompletely is true, removes complete shape If removeCompletely is false, removes instance(location) only Returns False (and does nothing) if shape is not free or is not top-level shape
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Search(self,S : OCP.TopoDS.TopoDS_Shape,L : OCP.TDF.TDF_Label,findInstance : bool=True,findComponent : bool=True,findSubshape : bool=True) -> bool: 
        """
        General tool to find a (sub) shape in the document * If findInstance is True, and S has a non-null location, first tries to find the shape among the top-level shapes with this location * If not found, and findComponent is True, tries to find the shape among the components of assemblies * If not found, tries to find the shape without location among top-level shapes * If not found and findSubshape is True, tries to find a shape as a subshape of top-level simple shapes Returns False if nothing is found
        """
    def SearchUsingMap(self,S : OCP.TopoDS.TopoDS_Shape,L : OCP.TDF.TDF_Label,findWithoutLoc : bool,findSubshape : bool) -> bool: 
        """
        None
        """
    @staticmethod
    def SetAutoNaming_s(V : bool) -> None: 
        """
        Sets auto-naming mode to <V>. If True then for added shapes, links, assemblies and SHUO's, the TDataStd_Name attribute is automatically added. For shapes it contains a shape type (e.g. "SOLID", "SHELL", etc); for links it has a form "=>[0:1:1:2]" (where a tag is a label containing a shape without a location); for assemblies it is "ASSEMBLY", and "SHUO" for SHUO's. This setting is global; it cannot be made a member function as it is used by static methods as well. By default, auto-naming is enabled. See also AutoNaming().
        """
    @overload
    def SetExternRefs(self,L : OCP.TDF.TDF_Label,SHAS : OCP.TColStd.TColStd_SequenceOfHAsciiString) -> None: 
        """
        Sets the names of references on the no-step files

        Sets the names of references on the no-step files
        """
    @overload
    def SetExternRefs(self,SHAS : OCP.TColStd.TColStd_SequenceOfHAsciiString) -> OCP.TDF.TDF_Label: ...
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetInstanceSHUO(self,theShape : OCP.TopoDS.TopoDS_Shape) -> XCAFDoc_GraphNode: 
        """
        Search for the component shape by labelks path and set SHUO structure for founded label structure Returns null attribute if no component in any assembly found.
        """
    def SetLocation(self,theShapeLabel : OCP.TDF.TDF_Label,theLoc : OCP.TopLoc.TopLoc_Location,theRefLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Sets location to the shape label If label is reference -> changes location attribute If label is free shape -> creates reference with location to it
        """
    def SetSHUO(self,Labels : OCP.TDF.TDF_LabelSequence,MainSHUOAttr : XCAFDoc_GraphNode) -> bool: 
        """
        Sets the SHUO structure between upper_usage and next_usage create multy-level (if number of labels > 2) SHUO from first to last Initialise out <MainSHUOAttr> by main upper_usage SHUO attribute. Returns FALSE if some of labels in not component label
        """
    def SetShape(self,L : OCP.TDF.TDF_Label,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets representation (TopoDS_Shape) for top-level shape.
        """
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> XCAFDoc_ShapeTool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def UpdateAssemblies(self) -> None: 
        """
        Top-down update for all assembly compounds stored in the document.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_View(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Attribute to store viewAttribute to store viewAttribute to store view
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetObject(self) -> OCP.XCAFView.XCAFView_Object: 
        """
        Returns view object data taken from the paren's label and its sub-labels.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetObject(self,theViewObject : OCP.XCAFView.XCAFView_Object) -> None: 
        """
        Updates parent's label and its sub-labels with data taken from theViewObject. Old data associated with the label will be lost.
        """
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label) -> XCAFDoc_View: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_ViewTool(OCP.TDataStd.TDataStd_GenericEmpty, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Provides tools to store and retrieve Views in and from TDocStd_Document Each View contains parts XCAFDoc_View attribute with all information about camera and view window. Also each view contain information of displayed shapes and GDTs as sets of shape and GDT labels.Provides tools to store and retrieve Views in and from TDocStd_Document Each View contains parts XCAFDoc_View attribute with all information about camera and view window. Also each view contain information of displayed shapes and GDTs as sets of shape and GDT labels.Provides tools to store and retrieve Views in and from TDocStd_Document Each View contains parts XCAFDoc_View attribute with all information about camera and view window. Also each view contain information of displayed shapes and GDTs as sets of shape and GDT labels.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AddView(self) -> OCP.TDF.TDF_Label: 
        """
        Adds a view definition to a View table and returns its label
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BaseLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label under which Views are stored
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetRefAnnotationLabel(self,theViewL : OCP.TDF.TDF_Label,theAnnotationLabels : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns Annotation labels defined for label theViewL Returns False if the theViewL is not in View table
        """
    def GetRefClippingPlaneLabel(self,theViewL : OCP.TDF.TDF_Label,theClippingPlaneLabels : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns ClippingPlane labels defined for label theViewL Returns False if the theViewL is not in View table
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRefGDTLabel(self,theViewL : OCP.TDF.TDF_Label,theGDTLabels : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns GDT labels defined for label theViewL Returns False if the theViewL is not in View table
        """
    def GetRefNoteLabel(self,theViewL : OCP.TDF.TDF_Label,theNoteLabels : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns Notes labels defined for label theViewL Returns False if the theViewL is not in View table
        """
    def GetRefShapeLabel(self,theViewL : OCP.TDF.TDF_Label,theShapeLabels : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns shape labels defined for label theViewL Returns False if the theViewL is not in View table
        """
    def GetViewLabels(self,theLabels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of View labels currently stored in the View table
        """
    def GetViewLabelsForAnnotation(self,theAnnotationL : OCP.TDF.TDF_Label,theViews : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all View labels defined for label AnnotationL
        """
    def GetViewLabelsForClippingPlane(self,theClippingPlaneL : OCP.TDF.TDF_Label,theViews : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all View labels defined for label ClippingPlaneL
        """
    def GetViewLabelsForGDT(self,theGDTL : OCP.TDF.TDF_Label,theViews : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all View labels defined for label GDTL
        """
    def GetViewLabelsForNote(self,theNoteL : OCP.TDF.TDF_Label,theViews : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all View labels defined for label NoteL
        """
    def GetViewLabelsForShape(self,theShapeL : OCP.TDF.TDF_Label,theViews : OCP.TDF.TDF_LabelSequence) -> bool: 
        """
        Returns all View labels defined for label ShapeL
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsLocked(self,theViewL : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns true if the given View is marked as locked
        """
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def IsView(self,theLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns True if label belongs to a View table and is a View definition
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def Lock(self,theViewL : OCP.TDF.TDF_Label) -> None: 
        """
        Mark the given View as locked
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveView(self,theViewL : OCP.TDF.TDF_Label) -> None: 
        """
        Remove View
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SetClippingPlanes(self,theClippingPlaneLabels : OCP.TDF.TDF_LabelSequence,theViewL : OCP.TDF.TDF_Label) -> None: 
        """
        Set Clipping planes to given View
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @overload
    def SetView(self,theShapes : OCP.TDF.TDF_LabelSequence,theGDTs : OCP.TDF.TDF_LabelSequence,theClippingPlanes : OCP.TDF.TDF_LabelSequence,theViewL : OCP.TDF.TDF_Label) -> None: 
        """
        Sets a link with GUID

        Sets a link with GUID

        Sets a link with GUID
        """
    @overload
    def SetView(self,theShapes : OCP.TDF.TDF_LabelSequence,theGDTs : OCP.TDF.TDF_LabelSequence,theClippingPlanes : OCP.TDF.TDF_LabelSequence,theNotes : OCP.TDF.TDF_LabelSequence,theAnnotations : OCP.TDF.TDF_LabelSequence,theViewL : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def SetView(self,theShapes : OCP.TDF.TDF_LabelSequence,theGDTs : OCP.TDF.TDF_LabelSequence,theViewL : OCP.TDF.TDF_Label) -> None: ...
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> XCAFDoc_ViewTool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def Unlock(self,theViewL : OCP.TDF.TDF_Label) -> None: 
        """
        Unlock the given View
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_VisMaterial(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Attribute storing Material definition for visualization purposes.Attribute storing Material definition for visualization purposes.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AlphaCutOff(self) -> float: 
        """
        Return alpha cutoff value; 0.5 by default.
        """
    def AlphaMode(self) -> OCP.Graphic3d.Graphic3d_AlphaMode: 
        """
        Return alpha mode; Graphic3d_AlphaMode_BlendAuto by default.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BaseColor(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return base color.
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def CommonMaterial(self) -> XCAFDoc_VisMaterialCommon: 
        """
        Return common material. Note that default constructor creates an empty material (
        """
    def ConvertToCommonMaterial(self) -> XCAFDoc_VisMaterialCommon: 
        """
        Return Common material or convert PBR into Common material.
        """
    def ConvertToPbrMaterial(self) -> XCAFDoc_VisMaterialPBR: 
        """
        Return PBR material or convert Common into PBR material.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FaceCulling(self) -> OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel: 
        """
        Returns if the material is double or single sided; Graphic3d_TypeOfBackfacingModel_Auto by default.
        """
    def FillAspect(self,theAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: 
        """
        Fill in graphic aspects.
        """
    def FillMaterialAspect(self,theAspect : OCP.Graphic3d.Graphic3d_MaterialAspect) -> None: 
        """
        Fill in material aspect.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Return attribute GUID.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasCommonMaterial(self) -> bool: 
        """
        Return TRUE if common material is defined; FALSE by default.
        """
    def HasPbrMaterial(self) -> bool: 
        """
        Return TRUE if metal-roughness PBR material is defined; FALSE by default.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Return GUID of this attribute type.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsDoubleSided(self) -> bool: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if material definition is empty.
        """
    def IsEqual(self,theOther : XCAFDoc_VisMaterial) -> bool: 
        """
        Compare two materials. Performs deep comparison by actual values - e.g. can be useful for merging materials.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Create a new empty attribute.
        """
    def Paste(self,theInto : OCP.TDF.TDF_Attribute,theRelTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Paste this attribute into another one.
        """
    def PbrMaterial(self) -> XCAFDoc_VisMaterialPBR: 
        """
        Return metal-roughness PBR material. Note that default constructor creates an empty material (
        """
    def RawName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Return material name / tag (transient data, not stored in the document).
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,theWith : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restore attribute from specified state.
        """
    def SetAlphaMode(self,theMode : OCP.Graphic3d.Graphic3d_AlphaMode,theCutOff : float=0.5) -> None: 
        """
        Set alpha mode.
        """
    def SetCommonMaterial(self,theMaterial : XCAFDoc_VisMaterialCommon) -> None: 
        """
        Setup common material.
        """
    def SetDoubleSided(self,theIsDoubleSided : bool) -> None: 
        """
        None
        """
    def SetFaceCulling(self,theFaceCulling : OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel) -> None: 
        """
        Specifies whether the material is double or single sided.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetPbrMaterial(self,theMaterial : XCAFDoc_VisMaterialPBR) -> None: 
        """
        Setup metal-roughness PBR material.
        """
    def SetRawName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set material name / tag (transient data, not stored in the document).
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UnsetCommonMaterial(self) -> None: 
        """
        Setup undefined common material.
        """
    def UnsetPbrMaterial(self) -> None: 
        """
        Setup undefined metal-roughness PBR material.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_VisMaterialCommon():
    """
    Common (obsolete) material definition.
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def IsEqual(self,theOther : XCAFDoc_VisMaterialCommon) -> bool: 
        """
        Compare two materials.
        """
    def __init__(self) -> None: ...
    @property
    def AmbientColor(self) -> OCP.Quantity.Quantity_Color:
        """
        :type: OCP.Quantity.Quantity_Color
        """
    @AmbientColor.setter
    def AmbientColor(self, arg0: OCP.Quantity.Quantity_Color) -> None:
        pass
    @property
    def DiffuseColor(self) -> OCP.Quantity.Quantity_Color:
        """
        :type: OCP.Quantity.Quantity_Color
        """
    @DiffuseColor.setter
    def DiffuseColor(self, arg0: OCP.Quantity.Quantity_Color) -> None:
        pass
    @property
    def EmissiveColor(self) -> OCP.Quantity.Quantity_Color:
        """
        :type: OCP.Quantity.Quantity_Color
        """
    @EmissiveColor.setter
    def EmissiveColor(self, arg0: OCP.Quantity.Quantity_Color) -> None:
        pass
    @property
    def IsDefined(self) -> bool:
        """
        :type: bool
        """
    @IsDefined.setter
    def IsDefined(self, arg0: bool) -> None:
        pass
    @property
    def Shininess(self) -> float:
        """
        :type: float
        """
    @Shininess.setter
    def Shininess(self, arg0: float) -> None:
        pass
    @property
    def SpecularColor(self) -> OCP.Quantity.Quantity_Color:
        """
        :type: OCP.Quantity.Quantity_Color
        """
    @SpecularColor.setter
    def SpecularColor(self, arg0: OCP.Quantity.Quantity_Color) -> None:
        pass
    @property
    def Transparency(self) -> float:
        """
        :type: float
        """
    @Transparency.setter
    def Transparency(self, arg0: float) -> None:
        pass
    pass
class XCAFDoc_VisMaterialPBR():
    """
    Metallic-roughness PBR material definition.
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def IsEqual(self,theOther : XCAFDoc_VisMaterialPBR) -> bool: 
        """
        Compare two materials.
        """
    def __init__(self) -> None: ...
    @property
    def BaseColor(self) -> OCP.Quantity.Quantity_ColorRGBA:
        """
        :type: OCP.Quantity.Quantity_ColorRGBA
        """
    @BaseColor.setter
    def BaseColor(self, arg0: OCP.Quantity.Quantity_ColorRGBA) -> None:
        pass
    @property
    def EmissiveFactor(self) -> OCP.gp.gp_Vec3f:
        """
        :type: OCP.gp.gp_Vec3f
        """
    @EmissiveFactor.setter
    def EmissiveFactor(self, arg0: OCP.gp.gp_Vec3f) -> None:
        pass
    @property
    def IsDefined(self) -> bool:
        """
        :type: bool
        """
    @IsDefined.setter
    def IsDefined(self, arg0: bool) -> None:
        pass
    @property
    def Metallic(self) -> float:
        """
        :type: float
        """
    @Metallic.setter
    def Metallic(self, arg0: float) -> None:
        pass
    @property
    def RefractionIndex(self) -> float:
        """
        :type: float
        """
    @RefractionIndex.setter
    def RefractionIndex(self, arg0: float) -> None:
        pass
    @property
    def Roughness(self) -> float:
        """
        :type: float
        """
    @Roughness.setter
    def Roughness(self, arg0: float) -> None:
        pass
    pass
class XCAFDoc_VisMaterialTool(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Provides tools to store and retrieve attributes (visualization materials) of TopoDS_Shape in and from TDocStd_Document.Provides tools to store and retrieve attributes (visualization materials) of TopoDS_Shape in and from TDocStd_Document.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    @overload
    def AddMaterial(self,theName : OCP.TCollection.TCollection_AsciiString) -> OCP.TDF.TDF_Label: 
        """
        Adds Material definition to a Material Table and returns its Label.

        Adds Material definition to a Material Table and returns its Label.
        """
    @overload
    def AddMaterial(self,theMat : XCAFDoc_VisMaterial,theName : OCP.TCollection.TCollection_AsciiString) -> OCP.TDF.TDF_Label: ...
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BaseLabel(self) -> OCP.TDF.TDF_Label: 
        """
        returns the label under which colors are stored
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetMaterial(self,theMatLabel : OCP.TDF.TDF_Label) -> XCAFDoc_VisMaterial: 
        """
        Returns Material defined by specified Label, or NULL if the label is not in Material Table.
        """
    def GetMaterials(self,Labels : OCP.TDF.TDF_LabelSequence) -> None: 
        """
        Returns a sequence of Materials currently stored in the Material Table.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def GetShapeMaterial(self,theShape : OCP.TopoDS.TopoDS_Shape,theMaterialLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns material assigned to the shape label.

        Returns label with material assigned to shape.

        Returns material assigned to shape or NULL if not assigned.
        """
    @overload
    def GetShapeMaterial(self,theShapeLabel : OCP.TDF.TDF_Label) -> XCAFDoc_VisMaterial: ...
    @overload
    def GetShapeMaterial(self,theShape : OCP.TopoDS.TopoDS_Shape) -> XCAFDoc_VisMaterial: ...
    @staticmethod
    def GetShapeMaterial_s(theShapeLabel : OCP.TDF.TDF_Label,theMaterialLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns label with material assigned to shape label.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns GUID of this attribute type.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsMaterial(self,theLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Returns TRUE if Label belongs to a Material Table.
        """
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    @overload
    def IsSetShapeMaterial(self,theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns TRUE if label has a material assignment.

        Returns TRUE if shape has a material assignment.
        """
    @overload
    def IsSetShapeMaterial(self,theLabel : OCP.TDF.TDF_Label) -> bool: ...
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Creates new instance of this tool.
        """
    def Paste(self,arg1 : OCP.TDF.TDF_Attribute,arg2 : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        Does nothing.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveMaterial(self,theLabel : OCP.TDF.TDF_Label) -> None: 
        """
        Removes Material from the Material Table
        """
    def Restore(self,arg1 : OCP.TDF.TDF_Attribute) -> None: 
        """
        Does nothing.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @overload
    def SetShapeMaterial(self,theShape : OCP.TopoDS.TopoDS_Shape,theMaterialLabel : OCP.TDF.TDF_Label) -> bool: 
        """
        Sets new material to the shape.

        Sets a link with GUID XCAFDoc::VisMaterialRefGUID() from shape label to material label.
        """
    @overload
    def SetShapeMaterial(self,theShapeLabel : OCP.TDF.TDF_Label,theMaterialLabel : OCP.TDF.TDF_Label) -> None: ...
    @staticmethod
    def Set_s(L : OCP.TDF.TDF_Label) -> XCAFDoc_VisMaterialTool: ...
    def ShapeTool(self) -> XCAFDoc_ShapeTool: 
        """
        Returns internal XCAFDoc_ShapeTool tool
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    @overload
    def UnSetShapeMaterial(self,theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Removes a link with GUID XCAFDoc::VisMaterialRefGUID() from shape label to material.

        Removes a link with GUID XCAFDoc::VisMaterialRefGUID() from shape label to material.
        """
    @overload
    def UnSetShapeMaterial(self,theShapeLabel : OCP.TDF.TDF_Label) -> None: ...
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
class XCAFDoc_Volume(OCP.TDataStd.TDataStd_Real, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    attribute to store volumeattribute to store volumeattribute to store volume
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> float: 
        """
        None
        """
    def GetDimension(self) -> OCP.TDataStd.TDataStd_RealEnum: 
        """
        Obsolete method that will be removed in next versions. This field is not supported in the persistence mechanism.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(label : OCP.TDF.TDF_Label,vol : float) -> bool: 
        """
        Returns volume as argument returns false if no such attribute at the <label>
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsCaptured(self) -> bool: 
        """
        Returns True if there is a reference on the same label
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,vol : float) -> None: 
        """
        Sets a value of volume
        """
    def SetDimension(self,DIM : OCP.TDataStd.TDataStd_RealEnum) -> None: 
        """
        Obsolete method that will be removed in next versions. This field is not supported in the persistence mechanism.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets the explicit GUID for the attribute.

        Sets default GUID for the attribute.
        """
    @overload
    def SetID(self,guid : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label,vol : float) -> XCAFDoc_Volume: 
        """
        Find, or create, an Volume attribute and set its value
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def __init__(self) -> None: ...
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
XCAFDoc_ColorCurv: OCP.XCAFDoc.XCAFDoc_ColorType # value = <XCAFDoc_ColorType.XCAFDoc_ColorCurv: 2>
XCAFDoc_ColorGen: OCP.XCAFDoc.XCAFDoc_ColorType # value = <XCAFDoc_ColorType.XCAFDoc_ColorGen: 0>
XCAFDoc_ColorSurf: OCP.XCAFDoc.XCAFDoc_ColorType # value = <XCAFDoc_ColorType.XCAFDoc_ColorSurf: 1>
