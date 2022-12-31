import OCP.TNaming
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopLoc
import OCP.TopoDS
import OCP.NCollection
import OCP.gp
import OCP.TopAbs
import OCP.TDF
import OCP.TopTools
import OCP.Standard
import io
__all__  = [
"TNaming",
"TNaming_Builder",
"TNaming_CopyShape",
"TNaming_DataMapOfShapeMapOfShape",
"TNaming_DataMapOfShapeShapesSet",
"TNaming_DeltaOnModification",
"TNaming_DeltaOnRemoval",
"TNaming_Evolution",
"TNaming_Identifier",
"TNaming_Iterator",
"TNaming_IteratorOnShapesSet",
"TNaming_ListOfIndexedDataMapOfShapeListOfShape",
"TNaming_ListOfMapOfShape",
"TNaming_ListOfNamedShape",
"TNaming_Localizer",
"TNaming_MapOfNamedShape",
"TNaming_MapOfShape",
"TNaming_Name",
"TNaming_NameType",
"TNaming_NamedShape",
"TNaming_NamedShapeHasher",
"TNaming_Naming",
"TNaming_NamingTool",
"TNaming_NewShapeIterator",
"TNaming_OldShapeIterator",
"TNaming_RefShape",
"TNaming_SameShapeIterator",
"TNaming_Scope",
"TNaming_Selector",
"TNaming_ShapesSet",
"TNaming_Tool",
"TNaming_TranslateTool",
"TNaming_Translator",
"TNaming_UsedShapes",
"TNaming_CONSTSHAPE",
"TNaming_DELETE",
"TNaming_FILTERBYNEIGHBOURGS",
"TNaming_GENERATED",
"TNaming_GENERATION",
"TNaming_IDENTITY",
"TNaming_INTERSECTION",
"TNaming_MODIFUNTIL",
"TNaming_MODIFY",
"TNaming_ORIENTATION",
"TNaming_PRIMITIVE",
"TNaming_REPLACE",
"TNaming_SELECTED",
"TNaming_SHELLIN",
"TNaming_SUBSTRACTION",
"TNaming_UNION",
"TNaming_UNKNOWN",
"TNaming_WIREIN"
]
class TNaming():
    """
    A topological attribute can be seen as a hook into the topological structure. To this hook, data can be attached and references defined. It is used for keeping and access to topological objects and their evolution. All topological objects are stored in the one user-protected TNaming_UsedShapes attribute at the root label of the data framework. This attribute contains map with all topological shapes, used in this document. To all other labels TNaming_NamedShape attribute can be added. This attribute contains references (hooks) to shapes from the TNaming_UsedShapes attribute and evolution of these shapes. TNaming_NamedShape attribute contains a set of pairs of hooks: old shape and new shape (see the figure below). It allows not only get the topological shapes by the labels, but also trace evolution of the shapes and correctly resolve dependent shapes by the changed one. If shape is just-created, then the old shape for accorded named shape is an empty shape. If a shape is deleted, then the new shape in this named shape is empty. Different algorithms may dispose sub-shapes of the result shape at the individual label depending on necessity: - If a sub-shape must have some extra attributes (material of each face or color of each edge). In this case a specific sub-shape is placed to the separate label (usually, sub-label of the result shape label) with all attributes of this sub-shape. - If topological naming is needed, a necessary and sufficient (for selected sub-shapes identification) set of sub-shapes is placed to the child labels of the result shape label. As usual, as far as basic solids and closed shells are concerned, all faces of the shape are disposed. Edges and vertices sub-shapes can be identified as intersection of contiguous faces. Modified/generated shapes may be placed to one named shape and identified as this named shape and source named shape that also can be identified with used algorithms. TNaming_NamedShape may contain a few pairs of hooks with the same evolution. In this case topology shape, which belongs to the named shape, is a compound of new shapes. The data model contains both the topology and the hooks, and functions handle both topological entities and hooks. Consider the case of a box function, which creates a solid with six faces and six hooks. Each hook is attached to a face. If you want, you can also have this function create hooks for edges and vertices as well as for faces. For the sake of simplicity though, let's limit the example. Not all functions can define explicit hooks for all topological entities they create, but all topological entities can be turned into hooks when necessary. This is where topological naming is necessary.
    """
    @staticmethod
    def ChangeShapes_s(label : OCP.TDF.TDF_Label,M : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        Remplace les shapes du label et des sous-labels par des copies.
        """
    @staticmethod
    def Displace_s(label : OCP.TDF.TDF_Label,aLocation : OCP.TopLoc.TopLoc_Location,WithOld : bool=True) -> None: 
        """
        Application de la Location sur les shapes du label et de ses sous labels.
        """
    @staticmethod
    def FindUniqueContextSet_s(S : OCP.TopoDS.TopoDS_Shape,Context : OCP.TopoDS.TopoDS_Shape,Arr : OCP.TopTools.TopTools_HArray1OfShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Find unique context of shape <S>,which is pure concatenation of atomic shapes (Compound). The result is concatenation of single contexts
        """
    @staticmethod
    def FindUniqueContext_s(S : OCP.TopoDS.TopoDS_Shape,Context : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Find unique context of shape <S>
        """
    @staticmethod
    def IDList_s(anIDList : OCP.TDF.TDF_IDList) -> None: 
        """
        Appends to <anIDList> the list of the attributes IDs of this package. CAUTION: <anIDList> is NOT cleared before use.
        """
    @staticmethod
    def MakeShape_s(MS : OCP.TopTools.TopTools_MapOfShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Builds shape from map content
        """
    @staticmethod
    def OuterShell_s(theSolid : OCP.TopoDS.TopoDS_Solid,theShell : OCP.TopoDS.TopoDS_Shell) -> bool: 
        """
        Returns True if outer Shell is found and the found shell in <theShell>. Print of TNaming enumeration =============================
        """
    @staticmethod
    def OuterWire_s(theFace : OCP.TopoDS.TopoDS_Face,theWire : OCP.TopoDS.TopoDS_Wire) -> bool: 
        """
        Returns True if outer wire is found and the found wire in <theWire>.
        """
    @staticmethod
    @overload
    def Print_s(NAME : TNaming_NameType,S : io.BytesIO) -> io.BytesIO: 
        """
        Prints the evolution <EVOL> as a String on the Stream <S> and returns <S>.

        Prints the name of name type <NAME> as a String on the Stream <S> and returns <S>.

        Prints the content of UsedShapes private attribute as a String Table on the Stream <S> and returns <S>.
        """
    @staticmethod
    @overload
    def Print_s(ACCESS : OCP.TDF.TDF_Label,S : io.BytesIO) -> io.BytesIO: ...
    @staticmethod
    @overload
    def Print_s(EVOL : TNaming_Evolution,S : io.BytesIO) -> io.BytesIO: ...
    @staticmethod
    @overload
    def Replicate_s(NS : TNaming_NamedShape,T : OCP.gp.gp_Trsf,L : OCP.TDF.TDF_Label) -> None: 
        """
        Replicates the named shape with the transformation <T> on the label <L> (and sub-labels if necessary) (TNaming_GENERATED is set)

        Replicates the shape with the transformation <T> on the label <L> (and sub-labels if necessary) (TNaming_GENERATED is set)
        """
    @staticmethod
    @overload
    def Replicate_s(SH : OCP.TopoDS.TopoDS_Shape,T : OCP.gp.gp_Trsf,L : OCP.TDF.TDF_Label) -> None: ...
    @staticmethod
    def SubstituteSShape_s(accesslabel : OCP.TDF.TDF_Label,From : OCP.TopoDS.TopoDS_Shape,To : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Substitutes shape in source structure
        """
    @staticmethod
    def Substitute_s(labelsource : OCP.TDF.TDF_Label,labelcible : OCP.TDF.TDF_Label,mapOldNew : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        Subtituter les shapes sur les structures de source vers cible
        """
    @staticmethod
    def Transform_s(label : OCP.TDF.TDF_Label,aTransformation : OCP.gp.gp_Trsf) -> None: 
        """
        Application de la transformation sur les shapes du label et de ses sous labels. Warning: le remplacement du shape est fait dans tous les attributs qui le contiennent meme si ceux ci ne sont pas associees a des sous-labels de <Label>.
        """
    @staticmethod
    def Update_s(label : OCP.TDF.TDF_Label,mapOldNew : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        Mise a jour des shapes du label et de ses fils en tenant compte des substitutions decrite par mapOldNew.
        """
    def __init__(self) -> None: ...
    pass
class TNaming_Builder():
    """
    A tool to create and maintain topological attributes. Constructor creates an empty TNaming_NamedShape attribute at the given label. It allows adding "old shape" and "new shape" pairs with the specified evolution to this named shape. One evolution type per one builder must be used.
    """
    def Delete(self,oldShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Records the shape oldShape which was deleted from the current label. As an example, consider the case of a face removed by a Boolean operation.
        """
    @overload
    def Generated(self,newShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Records the shape newShape which was generated during a topological construction. As an example, consider the case of a face generated in construction of a box.

        Records the shape newShape which was generated from the shape oldShape during a topological construction. As an example, consider the case of a face generated from an edge in construction of a prism.
        """
    @overload
    def Generated(self,oldShape : OCP.TopoDS.TopoDS_Shape,newShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def Modify(self,oldShape : OCP.TopoDS.TopoDS_Shape,newShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Records the shape newShape which is a modification of the shape oldShape. As an example, consider the case of a face split or merged in a Boolean operation.
        """
    def NamedShape(self) -> TNaming_NamedShape: 
        """
        Returns the NamedShape which has been built or is under construction.
        """
    def Select(self,aShape : OCP.TopoDS.TopoDS_Shape,inShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Add a Shape to the current label , This Shape is unmodified. Used for example to define a set of shapes under a label.
        """
    def __init__(self,aLabel : OCP.TDF.TDF_Label) -> None: ...
    pass
class TNaming_CopyShape():
    """
    None
    """
    @staticmethod
    def CopyTool_s(aShape : OCP.TopoDS.TopoDS_Shape,aMap : Any,aResult : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Makes copy a set of shape(s), using the aMap
        """
    @staticmethod
    @overload
    def Translate_s(L : OCP.TopLoc.TopLoc_Location,aMap : Any) -> OCP.TopLoc.TopLoc_Location: 
        """
        Translates a Transient shape(s) to Transient

        Translates a Topological Location to an other Top. Location
        """
    @staticmethod
    @overload
    def Translate_s(aShape : OCP.TopoDS.TopoDS_Shape,aMap : Any,aResult : OCP.TopoDS.TopoDS_Shape,TrTool : TNaming_TranslateTool) -> None: ...
    def __init__(self) -> None: ...
    pass
class TNaming_DataMapOfShapeMapOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TNaming_DataMapOfShapeMapOfShape) -> TNaming_DataMapOfShapeMapOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TNaming_MapOfShape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TNaming_MapOfShape) -> TNaming_MapOfShape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TNaming_MapOfShape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TNaming_MapOfShape: 
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
    def Exchange(self,theOther : TNaming_DataMapOfShapeMapOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TNaming_MapOfShape: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : TNaming_MapOfShape) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TNaming_MapOfShape: 
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
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TNaming_DataMapOfShapeMapOfShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TNaming_DataMapOfShapeShapesSet(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TNaming_DataMapOfShapeShapesSet) -> TNaming_DataMapOfShapeShapesSet: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TNaming_ShapesSet) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TNaming_ShapesSet) -> TNaming_ShapesSet: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TNaming_ShapesSet: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TNaming_ShapesSet: 
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
    def Exchange(self,theOther : TNaming_DataMapOfShapeShapesSet) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TNaming_ShapesSet: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : TNaming_ShapesSet) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TNaming_ShapesSet: 
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TNaming_DataMapOfShapeShapesSet) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TNaming_DeltaOnModification(OCP.TDF.TDF_DeltaOnModification, OCP.TDF.TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    """
    This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.This class provides default services for an AttributeDelta on a MODIFICATION action.
    """
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,NS : TNaming_NamedShape) -> None: ...
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
class TNaming_DeltaOnRemoval(OCP.TDF.TDF_DeltaOnRemoval, OCP.TDF.TDF_AttributeDelta, OCP.Standard.Standard_Transient):
    def Apply(self) -> None: 
        """
        Applies the delta to the attribute.
        """
    def Attribute(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns the reference attribute.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the contents.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute concerned by <me>.
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
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label concerned by <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,NS : TNaming_NamedShape) -> None: ...
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
class TNaming_Evolution():
    """
    Defines the type of evolution in old shape - new shape pairs. The definitions - in the form of the terms of the enumeration - are needed by the TNaming_NamedShape attribute and indicate what entities this attribute records as follows: - PRIMITIVE - New entities; in each pair, old shape is a null shape and new shape is a created entity. - GENERATED - Entities created from other entities; in each pair, old shape is the generator and new shape is the created entity. - MODIFY - Split or merged entities, in each pair, old shape is the entity before the operation and new shape is the new entity after the operation. - DELETE - Deletion of entities; in each pair, old shape is a deleted entity and new shape is null. - SELECTED - Named topological entities; in each pair, the new shape is a named entity and the old shape is not used.

    Members:

      TNaming_PRIMITIVE

      TNaming_GENERATED

      TNaming_MODIFY

      TNaming_DELETE

      TNaming_REPLACE

      TNaming_SELECTED
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
    TNaming_DELETE: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_DELETE: 3>
    TNaming_GENERATED: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_GENERATED: 1>
    TNaming_MODIFY: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_MODIFY: 2>
    TNaming_PRIMITIVE: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_PRIMITIVE: 0>
    TNaming_REPLACE: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_REPLACE: 4>
    TNaming_SELECTED: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_SELECTED: 5>
    __entries: dict # value = {'TNaming_PRIMITIVE': (<TNaming_Evolution.TNaming_PRIMITIVE: 0>, None), 'TNaming_GENERATED': (<TNaming_Evolution.TNaming_GENERATED: 1>, None), 'TNaming_MODIFY': (<TNaming_Evolution.TNaming_MODIFY: 2>, None), 'TNaming_DELETE': (<TNaming_Evolution.TNaming_DELETE: 3>, None), 'TNaming_REPLACE': (<TNaming_Evolution.TNaming_REPLACE: 4>, None), 'TNaming_SELECTED': (<TNaming_Evolution.TNaming_SELECTED: 5>, None)}
    __members__: dict # value = {'TNaming_PRIMITIVE': <TNaming_Evolution.TNaming_PRIMITIVE: 0>, 'TNaming_GENERATED': <TNaming_Evolution.TNaming_GENERATED: 1>, 'TNaming_MODIFY': <TNaming_Evolution.TNaming_MODIFY: 2>, 'TNaming_DELETE': <TNaming_Evolution.TNaming_DELETE: 3>, 'TNaming_REPLACE': <TNaming_Evolution.TNaming_REPLACE: 4>, 'TNaming_SELECTED': <TNaming_Evolution.TNaming_SELECTED: 5>}
    pass
class TNaming_Identifier():
    """
    None
    """
    def AncestorIdentification(self,Localizer : TNaming_Localizer,Context : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def ArgIsFeature(self) -> bool: 
        """
        None
        """
    def Feature(self) -> TNaming_NamedShape: 
        """
        None
        """
    def FeatureArg(self) -> TNaming_NamedShape: 
        """
        None
        """
    def GeneratedIdentification(self,Localizer : TNaming_Localizer,NS : TNaming_NamedShape) -> None: 
        """
        None
        """
    def Identification(self,Localizer : TNaming_Localizer,NS : TNaming_NamedShape) -> None: 
        """
        None
        """
    def InitArgs(self) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsFeature(self) -> bool: 
        """
        None
        """
    def MoreArgs(self) -> bool: 
        """
        None
        """
    def NamedShapeOfGeneration(self) -> TNaming_NamedShape: 
        """
        None
        """
    def NextArg(self) -> None: 
        """
        None
        """
    def PrimitiveIdentification(self,Localizer : TNaming_Localizer,NS : TNaming_NamedShape) -> None: 
        """
        None
        """
    def ShapeArg(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def ShapeContext(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Type(self) -> TNaming_NameType: 
        """
        None
        """
    @overload
    def __init__(self,Lab : OCP.TDF.TDF_Label,S : OCP.TopoDS.TopoDS_Shape,ContextNS : TNaming_NamedShape,Geom : bool) -> None: ...
    @overload
    def __init__(self,Lab : OCP.TDF.TDF_Label,S : OCP.TopoDS.TopoDS_Shape,Context : OCP.TopoDS.TopoDS_Shape,Geom : bool) -> None: ...
    pass
class TNaming_Iterator():
    """
    A tool to visit the contents of a named shape attribute. Pairs of shapes in the attribute are iterated, one being the pre-modification or the old shape, and the other the post-modification or the new shape. This allows you to have a full access to all contents of an attribute. If, on the other hand, you are only interested in topological entities stored in the attribute, you can use the functions GetShape and CurrentShape in TNaming_Tool.
    """
    def Evolution(self) -> TNaming_Evolution: 
        """
        None
        """
    def IsModification(self) -> bool: 
        """
        Returns true if the new shape is a modification (split, fuse,etc...) of the old shape.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Item in the iteration.

        Returns True if there is a current Item in the iteration.
        """
    def NewShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the new shape in this iterator object.
        """
    def Next(self) -> None: 
        """
        Moves the iteration to the next Item
        """
    def OldShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the old shape in this iterator object. This shape can be a null one.
        """
    @overload
    def __init__(self,anAtt : TNaming_NamedShape) -> None: ...
    @overload
    def __init__(self,aLabel : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def __init__(self,aLabel : OCP.TDF.TDF_Label,aTrans : int) -> None: ...
    pass
class TNaming_IteratorOnShapesSet():
    """
    None
    """
    def Init(self,S : TNaming_ShapesSet) -> None: 
        """
        Initialize the iteration

        Initialize the iteration
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Item in the iteration.

        Returns True if there is a current Item in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Item

        Move to the next Item
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : TNaming_ShapesSet) -> None: ...
    pass
class TNaming_ListOfIndexedDataMapOfShapeListOfShape(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape) -> OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TNaming_ListOfIndexedDataMapOfShapeListOfShape) -> None: ...
    @overload
    def Append(self,theItem : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape,theIter : Any) -> None: ...
    def Assign(self,theOther : TNaming_ListOfIndexedDataMapOfShapeListOfShape) -> TNaming_ListOfIndexedDataMapOfShapeListOfShape: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape,theIter : Any) -> OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TNaming_ListOfIndexedDataMapOfShapeListOfShape,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape,theIter : Any) -> OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TNaming_ListOfIndexedDataMapOfShapeListOfShape,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape) -> OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TNaming_ListOfIndexedDataMapOfShapeListOfShape) -> None: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TNaming_ListOfIndexedDataMapOfShapeListOfShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TNaming_ListOfMapOfShape(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TopTools.TopTools_MapOfShape) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TNaming_ListOfMapOfShape) -> None: ...
    @overload
    def Append(self,theItem : OCP.TopTools.TopTools_MapOfShape,theIter : Any) -> None: ...
    def Assign(self,theOther : TNaming_ListOfMapOfShape) -> TNaming_ListOfMapOfShape: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.TopTools.TopTools_MapOfShape,theIter : Any) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TNaming_ListOfMapOfShape,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : OCP.TopTools.TopTools_MapOfShape,theIter : Any) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TNaming_ListOfMapOfShape,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TNaming_ListOfMapOfShape) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OCP.TopTools.TopTools_MapOfShape) -> OCP.TopTools.TopTools_MapOfShape: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self,theOther : TNaming_ListOfMapOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TNaming_ListOfNamedShape(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TNaming_NamedShape,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TNaming_ListOfNamedShape) -> None: ...
    @overload
    def Append(self,theItem : TNaming_NamedShape) -> TNaming_NamedShape: ...
    def Assign(self,theOther : TNaming_ListOfNamedShape) -> TNaming_ListOfNamedShape: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> TNaming_NamedShape: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TNaming_ListOfNamedShape,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : TNaming_NamedShape,theIter : Any) -> TNaming_NamedShape: ...
    @overload
    def InsertBefore(self,theOther : TNaming_ListOfNamedShape,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : TNaming_NamedShape,theIter : Any) -> TNaming_NamedShape: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TNaming_NamedShape: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : TNaming_NamedShape) -> TNaming_NamedShape: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TNaming_ListOfNamedShape) -> None: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TNaming_ListOfNamedShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TNaming_Localizer():
    """
    None
    """
    def Ancestors(self,S : OCP.TopoDS.TopoDS_Shape,Type : OCP.TopAbs.TopAbs_ShapeEnum) -> OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape: 
        """
        None
        """
    def Backward(self,NS : TNaming_NamedShape,S : OCP.TopoDS.TopoDS_Shape,Primitives : TNaming_MapOfNamedShape,ValidShapes : OCP.TopTools.TopTools_MapOfShape) -> None: 
        """
        None
        """
    def FindFeaturesInAncestors(self,S : OCP.TopoDS.TopoDS_Shape,In : OCP.TopoDS.TopoDS_Shape,AncInFeatures : OCP.TopTools.TopTools_MapOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def FindGenerator_s(NS : TNaming_NamedShape,S : OCP.TopoDS.TopoDS_Shape,theListOfGenerators : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def FindNeighbourg(self,Cont : OCP.TopoDS.TopoDS_Shape,S : OCP.TopoDS.TopoDS_Shape,Neighbourg : OCP.TopTools.TopTools_MapOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def FindShapeContext_s(NS : TNaming_NamedShape,theS : OCP.TopoDS.TopoDS_Shape,theSC : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Finds context of the shape <S>.
        """
    def GoBack(self,S : OCP.TopoDS.TopoDS_Shape,Lab : OCP.TDF.TDF_Label,Evol : TNaming_Evolution,OldS : OCP.TopTools.TopTools_ListOfShape,OldLab : TNaming_ListOfNamedShape) -> None: 
        """
        None
        """
    def Init(self,US : TNaming_UsedShapes,CurTrans : int) -> None: 
        """
        None
        """
    @staticmethod
    def IsNew_s(S : OCP.TopoDS.TopoDS_Shape,NS : TNaming_NamedShape) -> bool: 
        """
        None
        """
    def SubShapes(self,S : OCP.TopoDS.TopoDS_Shape,Type : OCP.TopAbs.TopAbs_ShapeEnum) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TNaming_MapOfNamedShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : TNaming_NamedShape) -> bool: 
        """
        Add
        """
    def Added(self,K : TNaming_NamedShape) -> TNaming_NamedShape: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TNaming_MapOfNamedShape) -> TNaming_MapOfNamedShape: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,theOther : TNaming_MapOfNamedShape) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : TNaming_NamedShape) -> bool: ...
    def Differ(self,theOther : TNaming_MapOfNamedShape) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TNaming_MapOfNamedShape,theRight : TNaming_MapOfNamedShape) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TNaming_MapOfNamedShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TNaming_MapOfNamedShape) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TNaming_MapOfNamedShape) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TNaming_MapOfNamedShape,theRight : TNaming_MapOfNamedShape) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TNaming_MapOfNamedShape) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : TNaming_NamedShape) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TNaming_MapOfNamedShape) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TNaming_MapOfNamedShape,theRight : TNaming_MapOfNamedShape) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TNaming_MapOfNamedShape,theRight : TNaming_MapOfNamedShape) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TNaming_MapOfNamedShape) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TNaming_MapOfNamedShape) -> None: ...
    pass
class TNaming_MapOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Add
        """
    def Added(self,K : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TNaming_MapOfShape) -> TNaming_MapOfShape: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,K : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : TNaming_MapOfShape) -> bool: ...
    def Differ(self,theOther : TNaming_MapOfShape) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TNaming_MapOfShape,theRight : TNaming_MapOfShape) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TNaming_MapOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TNaming_MapOfShape) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TNaming_MapOfShape) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TNaming_MapOfShape,theRight : TNaming_MapOfShape) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TNaming_MapOfShape) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TNaming_MapOfShape) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TNaming_MapOfShape,theRight : TNaming_MapOfShape) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TNaming_MapOfShape,theRight : TNaming_MapOfShape) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TNaming_MapOfShape) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TNaming_MapOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TNaming_Name():
    """
    store the arguments of Naming.
    """
    def Append(self,arg1 : TNaming_NamedShape) -> None: 
        """
        None
        """
    def Arguments(self) -> TNaming_ListOfNamedShape: 
        """
        None
        """
    @overload
    def ContextLabel(self,theLab : OCP.TDF.TDF_Label) -> None: 
        """
        None

        None
        """
    @overload
    def ContextLabel(self) -> OCP.TDF.TDF_Label: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    @overload
    def Index(self,I : int) -> None: 
        """
        None

        None
        """
    @overload
    def Index(self) -> int: ...
    @overload
    def Orientation(self,theOrientation : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        None

        None
        """
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: ...
    def Paste(self,into : TNaming_Name,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    @overload
    def Shape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        None

        None
        """
    @overload
    def ShapeType(self,aType : OCP.TopAbs.TopAbs_ShapeEnum) -> None: ...
    def Solve(self,aLab : OCP.TDF.TDF_Label,Valid : OCP.TDF.TDF_LabelMap) -> bool: 
        """
        None
        """
    @overload
    def StopNamedShape(self) -> TNaming_NamedShape: 
        """
        None

        None
        """
    @overload
    def StopNamedShape(self,arg1 : TNaming_NamedShape) -> None: ...
    @overload
    def Type(self,aType : TNaming_NameType) -> None: 
        """
        None

        None
        """
    @overload
    def Type(self) -> TNaming_NameType: ...
    def __init__(self) -> None: ...
    pass
class TNaming_NameType():
    """
    to store naming characteristcs

    Members:

      TNaming_UNKNOWN

      TNaming_IDENTITY

      TNaming_MODIFUNTIL

      TNaming_GENERATION

      TNaming_INTERSECTION

      TNaming_UNION

      TNaming_SUBSTRACTION

      TNaming_CONSTSHAPE

      TNaming_FILTERBYNEIGHBOURGS

      TNaming_ORIENTATION

      TNaming_WIREIN

      TNaming_SHELLIN
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
    TNaming_CONSTSHAPE: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_CONSTSHAPE: 7>
    TNaming_FILTERBYNEIGHBOURGS: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_FILTERBYNEIGHBOURGS: 8>
    TNaming_GENERATION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_GENERATION: 3>
    TNaming_IDENTITY: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_IDENTITY: 1>
    TNaming_INTERSECTION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_INTERSECTION: 4>
    TNaming_MODIFUNTIL: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_MODIFUNTIL: 2>
    TNaming_ORIENTATION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_ORIENTATION: 9>
    TNaming_SHELLIN: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_SHELLIN: 11>
    TNaming_SUBSTRACTION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_SUBSTRACTION: 6>
    TNaming_UNION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_UNION: 5>
    TNaming_UNKNOWN: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_UNKNOWN: 0>
    TNaming_WIREIN: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_WIREIN: 10>
    __entries: dict # value = {'TNaming_UNKNOWN': (<TNaming_NameType.TNaming_UNKNOWN: 0>, None), 'TNaming_IDENTITY': (<TNaming_NameType.TNaming_IDENTITY: 1>, None), 'TNaming_MODIFUNTIL': (<TNaming_NameType.TNaming_MODIFUNTIL: 2>, None), 'TNaming_GENERATION': (<TNaming_NameType.TNaming_GENERATION: 3>, None), 'TNaming_INTERSECTION': (<TNaming_NameType.TNaming_INTERSECTION: 4>, None), 'TNaming_UNION': (<TNaming_NameType.TNaming_UNION: 5>, None), 'TNaming_SUBSTRACTION': (<TNaming_NameType.TNaming_SUBSTRACTION: 6>, None), 'TNaming_CONSTSHAPE': (<TNaming_NameType.TNaming_CONSTSHAPE: 7>, None), 'TNaming_FILTERBYNEIGHBOURGS': (<TNaming_NameType.TNaming_FILTERBYNEIGHBOURGS: 8>, None), 'TNaming_ORIENTATION': (<TNaming_NameType.TNaming_ORIENTATION: 9>, None), 'TNaming_WIREIN': (<TNaming_NameType.TNaming_WIREIN: 10>, None), 'TNaming_SHELLIN': (<TNaming_NameType.TNaming_SHELLIN: 11>, None)}
    __members__: dict # value = {'TNaming_UNKNOWN': <TNaming_NameType.TNaming_UNKNOWN: 0>, 'TNaming_IDENTITY': <TNaming_NameType.TNaming_IDENTITY: 1>, 'TNaming_MODIFUNTIL': <TNaming_NameType.TNaming_MODIFUNTIL: 2>, 'TNaming_GENERATION': <TNaming_NameType.TNaming_GENERATION: 3>, 'TNaming_INTERSECTION': <TNaming_NameType.TNaming_INTERSECTION: 4>, 'TNaming_UNION': <TNaming_NameType.TNaming_UNION: 5>, 'TNaming_SUBSTRACTION': <TNaming_NameType.TNaming_SUBSTRACTION: 6>, 'TNaming_CONSTSHAPE': <TNaming_NameType.TNaming_CONSTSHAPE: 7>, 'TNaming_FILTERBYNEIGHBOURGS': <TNaming_NameType.TNaming_FILTERBYNEIGHBOURGS: 8>, 'TNaming_ORIENTATION': <TNaming_NameType.TNaming_ORIENTATION: 9>, 'TNaming_WIREIN': <TNaming_NameType.TNaming_WIREIN: 10>, 'TNaming_SHELLIN': <TNaming_NameType.TNaming_SHELLIN: 11>}
    pass
class TNaming_NamedShape(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    The basis to define an attribute for the storage of topology and naming data. This attribute contains two parts: - The type of evolution, a term of the enumeration TNaming_Evolution - A list of pairs of shapes called the "old" shape and the "new" shape. The meaning depends on the type of evolution.The basis to define an attribute for the storage of topology and naming data. This attribute contains two parts: - The type of evolution, a term of the enumeration TNaming_Evolution - A list of pairs of shapes called the "old" shape and the "new" shape. The meaning depends on the type of evolution.The basis to define an attribute for the storage of topology and naming data. This attribute contains two parts: - The type of evolution, a term of the enumeration TNaming_Evolution - A list of pairs of shapes called the "old" shape and the "new" shape. The meaning depends on the type of evolution.
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
        Something to do after applying <anAttDelta>.
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
        None
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>
        """
    def Clear(self) -> None: 
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
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
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
        Dumps the attribute on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evolution(self) -> TNaming_Evolution: 
        """
        Returns the Evolution of the attribute.

        Returns the Evolution of the attribute.
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
    def Get(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shapes contained in <NS>. Returns a null shape if IsEmpty.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class method ============ Returns the GUID for named shapes.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.

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
        Returns an new empty attribute from the good end type. It is used by the copy algorithm.
        """
    def Paste(self,intoAttribute : OCP.TDF.TDF_Attribute,aRelocTationable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is different from the "Copy" one, because it is used when copying an attribute from a source structure into a target structure. This method pastes the current attribute to the label corresponding to the insertor. The pasted attribute may be a brand new one or a new version of the previous one.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the directly referenced attributes and labels to <aDataSet>. "Directly" means we have only to look at the first level of references.
        """
    def Restore(self,anAttribute : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the contents from <anAttribute> into this one. It is used when aborting a transaction.
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
    def SetVersion(self,version : int) -> None: 
        """
        Set the Version of the attribute.

        Set the Version of the attribute.
        """
    @overload
    def SetVersion(self,v : int) -> None: ...
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
    def Version(self) -> int: 
        """
        Returns the Version of the attribute.

        Returns the Version of the attribute.
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
class TNaming_NamedShapeHasher():
    """
    Purpose: The DefaultHasher is a Hasher that is used by default in NCollection maps. To compute the hash code of the key is used the global function HashCode. To compare two keys is used the global function IsEqual.
    """
    @staticmethod
    def HashCode_s(theKey : TNaming_NamedShape,theUpperBound : int) -> int: 
        """
        Returns hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theKey1 : TNaming_NamedShape,theKey2 : TNaming_NamedShape) -> bool: 
        """
        None
        """
    pass
class TNaming_Naming(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    This attribute store the topological naming of any selected shape, when this shape is not already attached to a specific label. This class is also used to solve it when the argumentsof the toipological naming are modified.This attribute store the topological naming of any selected shape, when this shape is not already attached to a specific label. This class is also used to solve it when the argumentsof the toipological naming are modified.This attribute store the topological naming of any selected shape, when this shape is not already attached to a specific label. This class is also used to solve it when the argumentsof the toipological naming are modified.
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
    def ChangeName(self) -> TNaming_Name: 
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
        None
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
        following code from TDesignStd ==============================
        """
    def GetName(self) -> TNaming_Name: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Deferred methods from TDF_Attribute ===================================
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @staticmethod
    def Insert_s(under : OCP.TDF.TDF_Label) -> TNaming_Naming: 
        """
        None
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
    def IsDefined(self) -> bool: 
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
    @staticmethod
    def Name_s(where : OCP.TDF.TDF_Label,Selection : OCP.TopoDS.TopoDS_Shape,Context : OCP.TopoDS.TopoDS_Shape,Geometry : bool=False,KeepOrientation : bool=False,BNproblem : bool=False) -> TNaming_NamedShape: 
        """
        Creates a Namimg attribute at label <where> to identify the shape <Selection>. Geometry is Standard_True if we are only interested by the underlying geometry (e.g. setting a constraint). <Context> is used to find neighbours of <S> when required by the naming. If KeepOrientation is True the Selection orientation is taken into account. BNproblem == True points out that Context sub-shapes in DF have orientation differences with Context shape itself. instance method ===============
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
        None
        """
    def Regenerate(self,scope : OCP.TDF.TDF_LabelMap) -> bool: 
        """
        regenerate only the Name associated to me
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
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
    def Solve(self,scope : OCP.TDF.TDF_LabelMap) -> bool: 
        """
        Regenerate recursively the whole name with scope. If scope is empty it means that all the labels of the framework are valid.
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
class TNaming_NamingTool():
    """
    None
    """
    @staticmethod
    def BuildDescendants_s(NS : TNaming_NamedShape,Labels : OCP.TDF.TDF_LabelMap) -> None: 
        """
        None
        """
    @staticmethod
    def CurrentShapeFromShape_s(Valid : OCP.TDF.TDF_LabelMap,Forbiden : OCP.TDF.TDF_LabelMap,Acces : OCP.TDF.TDF_Label,S : OCP.TopoDS.TopoDS_Shape,MS : OCP.TopTools.TopTools_IndexedMapOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def CurrentShape_s(Valid : OCP.TDF.TDF_LabelMap,Forbiden : OCP.TDF.TDF_LabelMap,NS : TNaming_NamedShape,MS : OCP.TopTools.TopTools_IndexedMapOfShape) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TNaming_NewShapeIterator():
    """
    Iterates on all the descendants of a shape
    """
    def IsModification(self) -> bool: 
        """
        True if the new shape is a modification (split, fuse,etc...) of the old shape.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None

        None
        """
    def NamedShape(self) -> TNaming_NamedShape: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Warning! Can be a Null Shape if a descendant is deleted.
        """
    @overload
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape,access : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape,Transaction : int,access : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def __init__(self,anIterator : TNaming_NewShapeIterator) -> None: ...
    @overload
    def __init__(self,anIterator : TNaming_Iterator) -> None: ...
    pass
class TNaming_OldShapeIterator():
    """
    Iterates on all the ascendants of a shape
    """
    def IsModification(self) -> bool: 
        """
        True if the new shape is a modification (split, fuse,etc...) of the old shape.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None

        None
        """
    def NamedShape(self) -> TNaming_NamedShape: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self,anIterator : TNaming_OldShapeIterator) -> None: ...
    @overload
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape,access : OCP.TDF.TDF_Label) -> None: ...
    @overload
    def __init__(self,anIterator : TNaming_Iterator) -> None: ...
    @overload
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape,Transaction : int,access : OCP.TDF.TDF_Label) -> None: ...
    pass
class TNaming_RefShape():
    """
    None
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        None
        """
    def NamedShape(self) -> TNaming_NamedShape: 
        """
        None
        """
    @overload
    def Shape(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class TNaming_SameShapeIterator():
    """
    To iterate on all the label which contained a given shape.
    """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None

        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape,access : OCP.TDF.TDF_Label) -> None: ...
    pass
class TNaming_Scope():
    """
    this class manage a scope of labels ===================================
    """
    def ChangeValid(self) -> OCP.TDF.TDF_LabelMap: 
        """
        None
        """
    def ClearValid(self) -> None: 
        """
        None
        """
    def CurrentShape(self,NS : TNaming_NamedShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the current value of <NS> according to the Valid Scope.
        """
    def GetValid(self) -> OCP.TDF.TDF_LabelMap: 
        """
        None
        """
    def IsValid(self,L : OCP.TDF.TDF_Label) -> bool: 
        """
        None
        """
    def Unvalid(self,L : OCP.TDF.TDF_Label) -> None: 
        """
        None
        """
    def UnvalidChildren(self,L : OCP.TDF.TDF_Label,withroot : bool=True) -> None: 
        """
        None
        """
    def Valid(self,L : OCP.TDF.TDF_Label) -> None: 
        """
        None
        """
    def ValidChildren(self,L : OCP.TDF.TDF_Label,withroot : bool=True) -> None: 
        """
        None
        """
    @overload
    def WithValid(self,mode : bool) -> None: 
        """
        None

        None
        """
    @overload
    def WithValid(self) -> bool: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,WithValid : bool) -> None: ...
    @overload
    def __init__(self,valid : OCP.TDF.TDF_LabelMap) -> None: ...
    pass
class TNaming_Selector():
    """
    This class provides a single API for selection of shapes. This involves both identification and selection of shapes in the data framework. If the selected shape is modified, this selector will solve its identifications. This class is the user interface for topological naming resources. * The <IsIdentified> method returns (if exists) the NamedShape which contains a given shape. The definition of an identified shape is : a Shape handled by a NamedShape (this shape is the only one stored) , which has the TNaming_PRImITIVE evolution
    """
    def Arguments(self,args : OCP.TDF.TDF_AttributeMap) -> None: 
        """
        Returns the attribute list args. This list contains the named shape on which the topological naming was built.
        """
    @staticmethod
    def IsIdentified_s(access : OCP.TDF.TDF_Label,selection : OCP.TopoDS.TopoDS_Shape,NS : TNaming_NamedShape,Geometry : bool=False) -> bool: 
        """
        To know if a shape is already identified (not selected) =======================================================
        """
    def NamedShape(self) -> TNaming_NamedShape: 
        """
        Returns the NamedShape build or under construction, which contains the topological naming..
        """
    @overload
    def Select(self,Selection : OCP.TopoDS.TopoDS_Shape,Context : OCP.TopoDS.TopoDS_Shape,Geometry : bool=False,KeepOrientatation : bool=False) -> bool: 
        """
        Creates a topological naming on the label aLabel given as an argument at construction time. If successful, the shape Selection - found in the shape Context - is now identified in the named shape returned in NamedShape. If Geometry is true, NamedShape contains the first appearance of Selection. This syntax is more robust than the previous syntax for this method.

        Creates a topological naming on the label aLabel given as an argument at construction time. If successful, the shape Selection is now identified in the named shape returned in NamedShape. If Geometry is true, NamedShape contains the first appearance of Selection.
        """
    @overload
    def Select(self,Selection : OCP.TopoDS.TopoDS_Shape,Geometry : bool=False,KeepOrientatation : bool=False) -> bool: ...
    def Solve(self,Valid : OCP.TDF.TDF_LabelMap) -> bool: 
        """
        Updates the topological naming on the label aLabel given as an argument at construction time. The underlying shape returned in the method NamedShape is updated. To read this shape, use the method TNaming_Tool::GetShape
        """
    def __init__(self,aLabel : OCP.TDF.TDF_Label) -> None: ...
    pass
class TNaming_ShapesSet():
    """
    None
    """
    @overload
    def Add(self,Shapes : TNaming_ShapesSet) -> None: 
        """
        Adds the Shape <S>

        Adds the shapes contained in <Shapes>.

        Adds the Shape <S>
        """
    @overload
    def Add(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def ChangeMap(self) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        None

        None
        """
    def Clear(self) -> None: 
        """
        Removes all Shapes

        Removes all Shapes
        """
    def Contains(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns True if <S> is in <me>

        Returns True if <S> is in <me>
        """
    def Filter(self,Shapes : TNaming_ShapesSet) -> None: 
        """
        Erases in <me> the shapes not contained in <Shapes>
        """
    def IsEmpty(self) -> bool: 
        """
        None

        None
        """
    def Map(self) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        None

        None
        """
    def NbShapes(self) -> int: 
        """
        None

        None
        """
    @overload
    def Remove(self,Shapes : TNaming_ShapesSet) -> None: 
        """
        Removes <S> in <me>.

        Removes in <me> the shapes contained in <Shapes>

        Removes <S> in <me>.
        """
    @overload
    def Remove(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,Type : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...
    pass
class TNaming_Tool():
    """
    A tool to get information on the topology of a named shape attribute. This information is typically a TopoDS_Shape object. Using this tool, relations between named shapes are also accessible.
    """
    @staticmethod
    def Collect_s(NS : TNaming_NamedShape,Labels : TNaming_MapOfNamedShape,OnlyModif : bool=True) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def CurrentNamedShape_s(NS : TNaming_NamedShape) -> TNaming_NamedShape: 
        """
        Returns the NamedShape of the last Modification of <NS>. This shape is identified by a label.

        Returns NamedShape the last Modification of <NS>.
        """
    @staticmethod
    @overload
    def CurrentNamedShape_s(NS : TNaming_NamedShape,Updated : OCP.TDF.TDF_LabelMap) -> TNaming_NamedShape: ...
    @staticmethod
    @overload
    def CurrentShape_s(NS : TNaming_NamedShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the last Modification of <NS>. Returns the shape CurrentShape contained in the named shape attribute NS. CurrentShape is the current state of the entities if they have been modified in other attributes of the same data structure. Each call to this function creates a new compound.

        Returns the shape CurrentShape contained in the named shape attribute NS, and present in the updated attribute map Updated. CurrentShape is the current state of the entities if they have been modified in other attributes of the same data structure. Each call to this function creates a new compound. Warning Only the contents of Updated are searched.R
        """
    @staticmethod
    @overload
    def CurrentShape_s(NS : TNaming_NamedShape,Updated : OCP.TDF.TDF_LabelMap) -> OCP.TopoDS.TopoDS_Shape: ...
    @staticmethod
    def FindShape_s(Valid : OCP.TDF.TDF_LabelMap,Forbiden : OCP.TDF.TDF_LabelMap,Arg : TNaming_NamedShape,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Returns the current shape (a Wire or a Shell) built (in the data framework) from the shapes of the argument named shape. It is used for IDENTITY name type computation.
        """
    @staticmethod
    def GeneratedShape_s(S : OCP.TopoDS.TopoDS_Shape,Generation : TNaming_NamedShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape generated from S or by a modification of S and contained in the named shape Generation.
        """
    @staticmethod
    def GetShape_s(NS : TNaming_NamedShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the entities stored in the named shape attribute NS. If there is only one old-new pair, the new shape is returned. Otherwise, a Compound is returned. This compound is made out of all the new shapes found. Each call to this function creates a new compound.
        """
    @staticmethod
    def HasLabel_s(access : OCP.TDF.TDF_Label,aShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns True if <aShape> appears under a label.(DP)
        """
    @staticmethod
    def InitialShape_s(aShape : OCP.TopoDS.TopoDS_Shape,anAcces : OCP.TDF.TDF_Label,Labels : OCP.TDF.TDF_LabelList) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape created from the shape aShape contained in the attribute anAcces.
        """
    @staticmethod
    def Label_s(access : OCP.TDF.TDF_Label,aShape : OCP.TopoDS.TopoDS_Shape,TransDef : int) -> OCP.TDF.TDF_Label: 
        """
        Returns the label of the first apparition of <aShape>. Transdef is a value of the transaction of the first apparition of <aShape>.
        """
    @staticmethod
    def NamedShape_s(aShape : OCP.TopoDS.TopoDS_Shape,anAcces : OCP.TDF.TDF_Label) -> TNaming_NamedShape: 
        """
        Returns the named shape attribute defined by the shape aShape and the label anAccess. This attribute is returned as a new shape. You call this function, if you need to create a topological attribute for existing data. Example class MyPkg_MyClass { public: Standard_Boolean SameEdge(const Handle(OCafTest_Line)& , const Handle(CafTest_Line)& ); };
        """
    @staticmethod
    def OriginalShape_s(NS : TNaming_NamedShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape contained as OldShape in <NS>
        """
    @staticmethod
    def ValidUntil_s(access : OCP.TDF.TDF_Label,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Returns the last transaction where the creation of S is valid.
        """
    def __init__(self) -> None: ...
    pass
class TNaming_TranslateTool(OCP.Standard.Standard_Transient):
    """
    tool to copy underlying TShape of a Shape. The TranslateTool class is provided to support the translation of topological data structures Transient to Transient.tool to copy underlying TShape of a Shape. The TranslateTool class is provided to support the translation of topological data structures Transient to Transient.tool to copy underlying TShape of a Shape. The TranslateTool class is provided to support the translation of topological data structures Transient to Transient.
    """
    def Add(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def MakeCompSolid(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MakeCompound(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MakeEdge(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MakeFace(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MakeShell(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MakeSolid(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MakeVertex(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MakeWire(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateEdge(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,M : Any) -> None: 
        """
        None
        """
    def UpdateFace(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,M : Any) -> None: 
        """
        None
        """
    def UpdateShape(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def UpdateVertex(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,M : Any) -> None: 
        """
        None
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
class TNaming_Translator():
    """
    only for Shape Copy test - to move in DNaming
    """
    def Add(self,aShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @overload
    def Copied(self,aShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns copied shape

        returns DataMap of results; (shape <-> copied shape)
        """
    @overload
    def Copied(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: ...
    def DumpMap(self,isWrite : bool=False) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Perform(self) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TNaming_UsedShapes(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Global attribute located under root label to store all the shapes handled by the framework Set of Shapes Used in a Data from TDF Only one instance by Data, it always Stored as Attribute of The Root.Global attribute located under root label to store all the shapes handled by the framework Set of Shapes Used in a Data from TDF Only one instance by Data, it always Stored as Attribute of The Root.Global attribute located under root label to store all the shapes handled by the framework Set of Shapes Used in a Data from TDF Only one instance by Data, it always Stored as Attribute of The Root.
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
        Something to do after applying <anAttDelta>.
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
        Clears the table.
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
        this method returns a null handle (no delta).
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
        this method returns a null handle (no delta).
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the attribute on <aStream>.
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
        Returns the ID: 2a96b614-ec8b-11d0-bee7-080009dc3333.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.

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
    def Map(self) -> Any: 
        """
        None

        None
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty attribute from the good end type. It is used by the copy algorithm.
        """
    def Paste(self,intoAttribute : OCP.TDF.TDF_Attribute,aRelocTationable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is different from the "Copy" one, because it is used when copying an attribute from a source structure into a target structure. This method pastes the current attribute to the label corresponding to the insertor. The pasted attribute may be a brand new one or a new version of the previous one.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the directly referenced attributes and labels to <aDataSet>. "Directly" means we have only to look at the first level of references.
        """
    def Restore(self,anAttribute : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the contents from <anAttribute> into this one. It is used when aborting a transaction.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
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
TNaming_CONSTSHAPE: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_CONSTSHAPE: 7>
TNaming_DELETE: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_DELETE: 3>
TNaming_FILTERBYNEIGHBOURGS: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_FILTERBYNEIGHBOURGS: 8>
TNaming_GENERATED: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_GENERATED: 1>
TNaming_GENERATION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_GENERATION: 3>
TNaming_IDENTITY: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_IDENTITY: 1>
TNaming_INTERSECTION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_INTERSECTION: 4>
TNaming_MODIFUNTIL: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_MODIFUNTIL: 2>
TNaming_MODIFY: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_MODIFY: 2>
TNaming_ORIENTATION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_ORIENTATION: 9>
TNaming_PRIMITIVE: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_PRIMITIVE: 0>
TNaming_REPLACE: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_REPLACE: 4>
TNaming_SELECTED: OCP.TNaming.TNaming_Evolution # value = <TNaming_Evolution.TNaming_SELECTED: 5>
TNaming_SHELLIN: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_SHELLIN: 11>
TNaming_SUBSTRACTION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_SUBSTRACTION: 6>
TNaming_UNION: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_UNION: 5>
TNaming_UNKNOWN: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_UNKNOWN: 0>
TNaming_WIREIN: OCP.TNaming.TNaming_NameType # value = <TNaming_NameType.TNaming_WIREIN: 10>
