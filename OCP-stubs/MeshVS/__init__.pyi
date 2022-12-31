import OCP.MeshVS
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Graphic3d
import OCP.AIS
import OCP.Aspect
import OCP.TopLoc
import OCP.SelectBasics
import OCP.TCollection
import OCP.PrsMgr
import OCP.Standard
import OCP.TColStd
import OCP.SelectMgr
import OCP.Prs3d
import OCP.V3d
import OCP.Select3D
import OCP.NCollection
import OCP.gp
import OCP.TColgp
import OCP.Bnd
import io
import OCP.Quantity
__all__  = [
"MeshVS_Array1OfSequenceOfInteger",
"MeshVS_Buffer",
"MeshVS_CommonSensitiveEntity",
"MeshVS_DataMapOfColorMapOfInteger",
"MeshVS_DataMapOfIntegerAsciiString",
"MeshVS_DataMapOfIntegerBoolean",
"MeshVS_DataMapOfIntegerColor",
"MeshVS_DataMapOfIntegerMaterial",
"MeshVS_DataMapOfIntegerTwoColors",
"MeshVS_DataMapOfIntegerVector",
"MeshVS_DataMapOfTwoColorsMapOfInteger",
"MeshVS_DataSource",
"MeshVS_DataSource3D",
"MeshVS_DeformedDataSource",
"MeshVS_Drawer",
"MeshVS_DrawerAttribute",
"MeshVS_DummySensitiveEntity",
"MeshVS_PrsBuilder",
"MeshVS_EntityType",
"MeshVS_HArray1OfSequenceOfInteger",
"MeshVS_MapOfTwoNodes",
"MeshVS_Mesh",
"MeshVS_MeshEntityOwner",
"MeshVS_MeshOwner",
"MeshVS_MeshPrsBuilder",
"MeshVS_MeshSelectionMethod",
"MeshVS_NodalColorPrsBuilder",
"MeshVS_PolyhedronVerts",
"MeshVS_ElementalColorPrsBuilder",
"MeshVS_SelectionModeFlags",
"MeshVS_SensitiveFace",
"MeshVS_SensitiveMesh",
"MeshVS_SensitivePolyhedron",
"MeshVS_SensitiveQuad",
"MeshVS_SensitiveSegment",
"MeshVS_SequenceOfPrsBuilder",
"MeshVS_SymmetricPairHasher",
"MeshVS_TextPrsBuilder",
"MeshVS_Tool",
"MeshVS_TwoColors",
"MeshVS_TwoColorsHasher",
"MeshVS_TwoNodes",
"MeshVS_TwoNodesHasher",
"MeshVS_VectorPrsBuilder",
"BindTwoColors",
"ExtractColor",
"ExtractColors",
"HashCode",
"IsEqual",
"MeshVS_BP_Default",
"MeshVS_BP_ElemColor",
"MeshVS_BP_Mesh",
"MeshVS_BP_NodalColor",
"MeshVS_BP_Text",
"MeshVS_BP_User",
"MeshVS_BP_Vector",
"MeshVS_DA_BackInteriorColor",
"MeshVS_DA_BackMaterial",
"MeshVS_DA_BeamColor",
"MeshVS_DA_BeamType",
"MeshVS_DA_BeamWidth",
"MeshVS_DA_ColorReflection",
"MeshVS_DA_ComputeSelectionTime",
"MeshVS_DA_ComputeTime",
"MeshVS_DA_DisplayNodes",
"MeshVS_DA_EdgeColor",
"MeshVS_DA_EdgeType",
"MeshVS_DA_EdgeWidth",
"MeshVS_DA_FrontMaterial",
"MeshVS_DA_HatchStyle",
"MeshVS_DA_InteriorColor",
"MeshVS_DA_InteriorStyle",
"MeshVS_DA_IsAllowOverlapped",
"MeshVS_DA_MarkerColor",
"MeshVS_DA_MarkerScale",
"MeshVS_DA_MarkerType",
"MeshVS_DA_MaxFaceNodes",
"MeshVS_DA_Reflection",
"MeshVS_DA_SelectableAuto",
"MeshVS_DA_ShowEdges",
"MeshVS_DA_ShrinkCoeff",
"MeshVS_DA_SmoothShading",
"MeshVS_DA_SupressBackFaces",
"MeshVS_DA_TextColor",
"MeshVS_DA_TextDisplayType",
"MeshVS_DA_TextExpansionFactor",
"MeshVS_DA_TextFont",
"MeshVS_DA_TextFontAspect",
"MeshVS_DA_TextHeight",
"MeshVS_DA_TextSpace",
"MeshVS_DA_TextStyle",
"MeshVS_DA_TextTexFont",
"MeshVS_DA_User",
"MeshVS_DA_VectorArrowPart",
"MeshVS_DA_VectorColor",
"MeshVS_DA_VectorMaxLength",
"MeshVS_DMF_DeformedMask",
"MeshVS_DMF_DeformedPrsShading",
"MeshVS_DMF_DeformedPrsShrink",
"MeshVS_DMF_DeformedPrsWireFrame",
"MeshVS_DMF_ElementalColorDataPrs",
"MeshVS_DMF_EntitiesWithData",
"MeshVS_DMF_HilightPrs",
"MeshVS_DMF_NodalColorDataPrs",
"MeshVS_DMF_OCCMask",
"MeshVS_DMF_SelectionPrs",
"MeshVS_DMF_Shading",
"MeshVS_DMF_Shrink",
"MeshVS_DMF_TextDataPrs",
"MeshVS_DMF_User",
"MeshVS_DMF_VectorDataPrs",
"MeshVS_DMF_WireFrame",
"MeshVS_ET_0D",
"MeshVS_ET_All",
"MeshVS_ET_Element",
"MeshVS_ET_Face",
"MeshVS_ET_Link",
"MeshVS_ET_NONE",
"MeshVS_ET_Node",
"MeshVS_ET_Volume",
"MeshVS_MSM_BOX",
"MeshVS_MSM_NODES",
"MeshVS_MSM_PRECISE",
"MeshVS_SMF_0D",
"MeshVS_SMF_All",
"MeshVS_SMF_Element",
"MeshVS_SMF_Face",
"MeshVS_SMF_Group",
"MeshVS_SMF_Link",
"MeshVS_SMF_Mesh",
"MeshVS_SMF_Node",
"MeshVS_SMF_Volume"
]
class MeshVS_Array1OfSequenceOfInteger():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : MeshVS_Array1OfSequenceOfInteger) -> MeshVS_Array1OfSequenceOfInteger: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Variable value access
        """
    def First(self) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.TColStd.TColStd_SequenceOfInteger) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : MeshVS_Array1OfSequenceOfInteger) -> MeshVS_Array1OfSequenceOfInteger: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TColStd.TColStd_SequenceOfInteger) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : OCP.TColStd.TColStd_SequenceOfInteger,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : MeshVS_Array1OfSequenceOfInteger) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_Buffer():
    """
    None
    """
    def __init__(self,theSize : int) -> None: ...
    pass
class MeshVS_CommonSensitiveEntity(OCP.Select3D.Select3D_SensitiveSet, OCP.Select3D.Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    Sensitive entity covering entire mesh for global selection.Sensitive entity covering entire mesh for global selection.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for sensitive set. Must be called manually to build BVH tree for any sensitive set in case if its content was initialized not in a constructor, but element by element
        """
    def BoundingBox(self) -> Any: 
        """
        Returns bounding box of the triangulation. If location transformation is set, it will be applied
        """
    def Box(self,theIdx : int) -> Any: 
        """
        Returns bounding box of sub-entity with index theIdx in sub-entity list
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of sensitive entity index theIdx along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of a mesh
        """
    def Clear(self) -> None: 
        """
        Destroys cross-reference to avoid memory leak
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @staticmethod
    def DefaultBVHBuilder_s() -> OCP.Select3D.Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        Create a copy.
        """
    def GetLeafNodeSize(self) -> int: 
        """
        Returns a number of nodes in 1 BVH leaf
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasInitLocation(self) -> bool: 
        """
        Returns true if the shape corresponding to the entity has init location
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvInitLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns inversed location transformation matrix if the shape corresponding to this entity has init location set. Otherwise, returns identity matrix.
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
    def MarkDirty(self) -> None: 
        """
        Marks BVH tree of the set as outdated. It will be rebuild at the next call of BVH()
        """
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks whether one or more entities of the set overlap current selecting volume. Implements the traverse of BVH tree built for the set
        """
    def NbSubElements(self) -> int: 
        """
        Number of elements.
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetBuilder(self,theBuilder : OCP.Select3D.Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : OCP.Select3D.Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    def Size(self) -> int: 
        """
        Returns the amount of sub-entities of the complex entity
        """
    def Swap(self,theIdx1 : int,theIdx2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToBuildBVH(self) -> bool: 
        """
        Returns TRUE if BVH tree is in invalidated state
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    def __init__(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theParentMesh : MeshVS_Mesh,theSelMethod : MeshVS_MeshSelectionMethod) -> None: ...
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
class MeshVS_DataMapOfColorMapOfInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MeshVS_DataMapOfColorMapOfInteger) -> MeshVS_DataMapOfColorMapOfInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.Quantity.Quantity_Color,theItem : OCP.TColStd.TColStd_MapOfInteger) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.Quantity.Quantity_Color,theItem : OCP.TColStd.TColStd_MapOfInteger) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.Quantity.Quantity_Color) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.Quantity.Quantity_Color) -> OCP.TColStd.TColStd_MapOfInteger: 
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
    def Exchange(self,theOther : MeshVS_DataMapOfColorMapOfInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.Quantity.Quantity_Color,theValue : OCP.TColStd.TColStd_MapOfInteger) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.Quantity.Quantity_Color) -> OCP.TColStd.TColStd_MapOfInteger: ...
    def IsBound(self,theKey : OCP.Quantity.Quantity_Color) -> bool: 
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
    def Seek(self,theKey : OCP.Quantity.Quantity_Color) -> OCP.TColStd.TColStd_MapOfInteger: 
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
    def UnBind(self,theKey : OCP.Quantity.Quantity_Color) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : MeshVS_DataMapOfColorMapOfInteger) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_DataMapOfIntegerAsciiString(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MeshVS_DataMapOfIntegerAsciiString) -> MeshVS_DataMapOfIntegerAsciiString: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> OCP.TCollection.TCollection_AsciiString: 
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
    def Exchange(self,theOther : MeshVS_DataMapOfIntegerAsciiString) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> OCP.TCollection.TCollection_AsciiString: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> OCP.TCollection.TCollection_AsciiString: 
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
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : MeshVS_DataMapOfIntegerAsciiString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_DataMapOfIntegerBoolean(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MeshVS_DataMapOfIntegerBoolean) -> MeshVS_DataMapOfIntegerBoolean: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : bool) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : bool) -> bool: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> bool: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> bool: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : MeshVS_DataMapOfIntegerBoolean) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : bool) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> bool: 
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
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : MeshVS_DataMapOfIntegerBoolean) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_DataMapOfIntegerColor(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MeshVS_DataMapOfIntegerColor) -> MeshVS_DataMapOfIntegerColor: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : OCP.Quantity.Quantity_Color) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : OCP.Quantity.Quantity_Color) -> OCP.Quantity.Quantity_Color: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> OCP.Quantity.Quantity_Color: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> OCP.Quantity.Quantity_Color: 
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
    def Exchange(self,theOther : MeshVS_DataMapOfIntegerColor) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : OCP.Quantity.Quantity_Color) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> OCP.Quantity.Quantity_Color: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> OCP.Quantity.Quantity_Color: 
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
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : MeshVS_DataMapOfIntegerColor) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_DataMapOfIntegerMaterial(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MeshVS_DataMapOfIntegerMaterial) -> MeshVS_DataMapOfIntegerMaterial: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : OCP.Graphic3d.Graphic3d_MaterialAspect) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : OCP.Graphic3d.Graphic3d_MaterialAspect) -> OCP.Graphic3d.Graphic3d_MaterialAspect: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> OCP.Graphic3d.Graphic3d_MaterialAspect: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> OCP.Graphic3d.Graphic3d_MaterialAspect: 
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
    def Exchange(self,theOther : MeshVS_DataMapOfIntegerMaterial) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> OCP.Graphic3d.Graphic3d_MaterialAspect: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : OCP.Graphic3d.Graphic3d_MaterialAspect) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> OCP.Graphic3d.Graphic3d_MaterialAspect: 
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
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : MeshVS_DataMapOfIntegerMaterial) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_DataMapOfIntegerTwoColors(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MeshVS_DataMapOfIntegerTwoColors) -> MeshVS_DataMapOfIntegerTwoColors: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : MeshVS_TwoColors) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : MeshVS_TwoColors) -> MeshVS_TwoColors: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> MeshVS_TwoColors: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> MeshVS_TwoColors: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : MeshVS_DataMapOfIntegerTwoColors) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : MeshVS_TwoColors) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> MeshVS_TwoColors: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> MeshVS_TwoColors: 
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
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : MeshVS_DataMapOfIntegerTwoColors) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_DataMapOfIntegerVector(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MeshVS_DataMapOfIntegerVector) -> MeshVS_DataMapOfIntegerVector: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : OCP.gp.gp_Vec) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : OCP.gp.gp_Vec) -> OCP.gp.gp_Vec: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> OCP.gp.gp_Vec: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> OCP.gp.gp_Vec: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : MeshVS_DataMapOfIntegerVector) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : OCP.gp.gp_Vec) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> OCP.gp.gp_Vec: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> OCP.gp.gp_Vec: 
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
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : MeshVS_DataMapOfIntegerVector) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_DataMapOfTwoColorsMapOfInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MeshVS_DataMapOfTwoColorsMapOfInteger) -> MeshVS_DataMapOfTwoColorsMapOfInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : MeshVS_TwoColors,theItem : OCP.TColStd.TColStd_MapOfInteger) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : MeshVS_TwoColors,theItem : OCP.TColStd.TColStd_MapOfInteger) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : MeshVS_TwoColors) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : MeshVS_TwoColors) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : MeshVS_DataMapOfTwoColorsMapOfInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : MeshVS_TwoColors,theValue : OCP.TColStd.TColStd_MapOfInteger) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : MeshVS_TwoColors) -> OCP.TColStd.TColStd_MapOfInteger: ...
    def IsBound(self,theKey : MeshVS_TwoColors) -> bool: 
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
    def Seek(self,theKey : MeshVS_TwoColors) -> OCP.TColStd.TColStd_MapOfInteger: 
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
    def UnBind(self,theKey : MeshVS_TwoColors) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : MeshVS_DataMapOfTwoColorsMapOfInteger) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_DataSource(OCP.Standard.Standard_Transient):
    """
    The deferred class using for the following tasks: 1) Receiving geometry data about single element of node by its number; 2) Receiving type of element or node by its number; 3) Receiving topological information about links between element and nodes it consist of; 4) Receiving information about what element cover this node; 5) Receiving information about all nodes and elements the object consist of 6) Activation of advanced mesh selection. In the advanced mesh selection mode there is created: - one owner for the whole mesh and for all selection modes - one sensitive entity for the whole mesh and for each selection mode Receiving of IDs of detected entities (nodes and elements) in a viewer is achieved by implementation of a group of methods GetDetectedEntities.The deferred class using for the following tasks: 1) Receiving geometry data about single element of node by its number; 2) Receiving type of element or node by its number; 3) Receiving topological information about links between element and nodes it consist of; 4) Receiving information about what element cover this node; 5) Receiving information about all nodes and elements the object consist of 6) Activation of advanced mesh selection. In the advanced mesh selection mode there is created: - one owner for the whole mesh and for all selection modes - one sensitive entity for the whole mesh and for each selection mode Receiving of IDs of detected entities (nodes and elements) in a viewer is achieved by implementation of a group of methods GetDetectedEntities.The deferred class using for the following tasks: 1) Receiving geometry data about single element of node by its number; 2) Receiving type of element or node by its number; 3) Receiving topological information about links between element and nodes it consist of; 4) Receiving information about what element cover this node; 5) Receiving information about all nodes and elements the object consist of 6) Activation of advanced mesh selection. In the advanced mesh selection mode there is created: - one owner for the whole mesh and for all selection modes - one sensitive entity for the whole mesh and for each selection mode Receiving of IDs of detected entities (nodes and elements) in a viewer is achieved by implementation of a group of methods GetDetectedEntities.
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
    def Get3DGeom(self,ID : int,NbNodes : int,Data : MeshVS_HArray1OfSequenceOfInteger) -> bool: 
        """
        This method returns topology information about 3D-element Returns false if element with ID isn't 3D or because other troubles
        """
    def GetAddr(self,ID : int,IsElement : bool) -> capsule: 
        """
        This method returns pointer which represents element or node data structure. This address will be saved in MeshVS_MeshEntityOwner, so that you can access to data structure fast by the method Owner(). In the redefined method you can return NULL. ID is the numerical identificator of node or element IsElement indicates this ID describe node ( if Standard_False ) or element ( if Standard_True )
        """
    def GetAllElements(self) -> OCP.TColStd.TColStd_PackedMapOfInteger: 
        """
        This method returns map of all elements the object consist of.
        """
    def GetAllGroups(self,Ids : OCP.TColStd.TColStd_PackedMapOfInteger) -> None: 
        """
        This method returns map of all groups the object contains.
        """
    def GetAllNodes(self) -> OCP.TColStd.TColStd_PackedMapOfInteger: 
        """
        This method returns map of all nodes the object consist of.
        """
    def GetBoundingBox(self) -> OCP.Bnd.Bnd_Box: 
        """
        Returns the bounding box of the whole mesh. It is used in advanced selection mode to define roughly the sensitive area of the mesh. It can be redefined to get access to a box computed in advance.
        """
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,X : float,Y : float,aTol : float,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger,DMin : float) -> bool: 
        """
        Returns maps of entities (nodes and elements) detected by mouse click at the point (X,Y) on the current view plane, with the tolerance aTol. DMin - is out argument should return actual detection tolerance. Returns True if something is detected. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.

        Returns maps of entities (nodes and elements) detected by mouse selection with rectangular box (XMin, YMin, XMax, YMax) on the current view plane, with the tolerance aTol. Returns True if something is detected. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.

        Returns maps of entities (nodes and elements) detected by mouse selection with the polyline <Polyline> on the current view plane, with the tolerance aTol. Returns True if something is detected. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.

        Filter out the maps of mesh entities so as to keep only the entities that are allowed to be selected according to the current context. Returns True if any of the maps has been changed. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.
        """
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,Polyline : OCP.TColgp.TColgp_Array1OfPnt2d,aBox : OCP.Bnd.Bnd_Box2d,aTol : float,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,XMin : float,YMin : float,XMax : float,YMax : float,aTol : float,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    def GetGeom(self,ID : int,IsElement : bool,Coords : OCP.TColStd.TColStd_Array1OfReal,NbNodes : int,Type : MeshVS_EntityType) -> bool: 
        """
        Returns geometry information about node or element ID is the numerical identificator of node or element IsElement indicates this ID describe node ( if Standard_False ) or element ( if Standard_True ) Coords is an array of coordinates of node(s). For node it is only 3 numbers: X, Y, Z in the strict order For element it is 3*n numbers, where n is number of this element vertices The order is strict also: X1, Y1, Z1, X2,...., where Xi, Yi, Zi are coordinates of vertices NbNodes is number of nodes. It is recommended this parameter to be set to 1 for node. Type is type of node or element (from enumeration). It is recommended this parameter to be set to MeshVS_ET_Node for node.
        """
    def GetGeomType(self,ID : int,IsElement : bool,Type : MeshVS_EntityType) -> bool: 
        """
        This method is similar to GetGeom, but returns only element or node type.
        """
    def GetGroup(self,Id : int,Type : MeshVS_EntityType,Ids : OCP.TColStd.TColStd_PackedMapOfInteger) -> bool: 
        """
        This method returns map of all group elements.
        """
    def GetGroupAddr(self,ID : int) -> capsule: 
        """
        This method returns pointer which represents group data structure. This address will be saved in MeshVS_MeshOwner, so that you can access to data structure fast by the method Owner(). In the redefined method you can return NULL. ID is the numerical identificator of group
        """
    def GetNodeNormal(self,ranknode : int,ElementId : int,nx : float,ny : float,nz : float) -> bool: 
        """
        This method return normal of node ranknode of face Id, which is using for smooth shading presentation. Returns false if normal isn't defined.
        """
    def GetNodesByElement(self,ID : int,NodeIDs : OCP.TColStd.TColStd_Array1OfInteger,NbNodes : int) -> bool: 
        """
        This method returns information about nodes this element consist of. ID is the numerical identificator of element. NodeIDs is the output array of nodes IDs in correct order, the same as coordinates returned by GetGeom(). NbNodes is number of nodes (number of items set in NodeIDs). Returns False if element does not exist
        """
    def GetNormal(self,Id : int,Max : int,nx : float,ny : float,nz : float) -> bool: 
        """
        This method calculates normal of face, which is using for correct reflection presentation. There is default method, for advance reflection this method can be redefined. Id is the numerical identificator of only element! Max is maximal number of nodes an element can consist of nx, ny, nz are values whose represent coordinates of normal (will be returned) In the redefined method you can return normal with length more then 1, but in this case the appearance of element will be more bright than usual. For ordinary brightness you must return normal with length 1
        """
    def GetNormalsByElement(self,Id : int,IsNodal : bool,MaxNodes : int,Normals : OCP.TColStd.TColStd_HArray1OfReal) -> bool: 
        """
        This method puts components of normal vectors at each node of a mesh face (at each face of a mesh volume) into the output array. Returns false if some problem was detected during calculation of normals. Id is an identifier of the mesh element. IsNodal, when true, means that normals at mesh element nodes are needed. If nodal normals are not available, or IsNodal is false, or the mesh element is a volume, then the output array contents depend on the element type: face: a normal calculated by GetNormal() is duplicated for each node of the face; volume: normals to all faces of the volume are computed (not for each node!). MaxNodes is maximal number of nodes an element can consist of. Normals contains the result.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAdvancedSelectionEnabled(self) -> bool: 
        """
        Returns True if advanced mesh selection is enabled. Default implementation returns False. It should be redefined to return True for advanced mesh selection activation.
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class MeshVS_DataSource3D(MeshVS_DataSource, OCP.Standard.Standard_Transient):
    @staticmethod
    def CreatePrismTopology_s(BasePoints : int) -> MeshVS_HArray1OfSequenceOfInteger: 
        """
        None
        """
    @staticmethod
    def CreatePyramidTopology_s(BasePoints : int) -> MeshVS_HArray1OfSequenceOfInteger: 
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
    def Get3DGeom(self,ID : int,NbNodes : int,Data : MeshVS_HArray1OfSequenceOfInteger) -> bool: 
        """
        This method returns topology information about 3D-element Returns false if element with ID isn't 3D or because other troubles
        """
    def GetAddr(self,ID : int,IsElement : bool) -> capsule: 
        """
        This method returns pointer which represents element or node data structure. This address will be saved in MeshVS_MeshEntityOwner, so that you can access to data structure fast by the method Owner(). In the redefined method you can return NULL. ID is the numerical identificator of node or element IsElement indicates this ID describe node ( if Standard_False ) or element ( if Standard_True )
        """
    def GetAllElements(self) -> OCP.TColStd.TColStd_PackedMapOfInteger: 
        """
        This method returns map of all elements the object consist of.
        """
    def GetAllGroups(self,Ids : OCP.TColStd.TColStd_PackedMapOfInteger) -> None: 
        """
        This method returns map of all groups the object contains.
        """
    def GetAllNodes(self) -> OCP.TColStd.TColStd_PackedMapOfInteger: 
        """
        This method returns map of all nodes the object consist of.
        """
    def GetBoundingBox(self) -> OCP.Bnd.Bnd_Box: 
        """
        Returns the bounding box of the whole mesh. It is used in advanced selection mode to define roughly the sensitive area of the mesh. It can be redefined to get access to a box computed in advance.
        """
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,X : float,Y : float,aTol : float,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger,DMin : float) -> bool: 
        """
        Returns maps of entities (nodes and elements) detected by mouse click at the point (X,Y) on the current view plane, with the tolerance aTol. DMin - is out argument should return actual detection tolerance. Returns True if something is detected. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.

        Returns maps of entities (nodes and elements) detected by mouse selection with rectangular box (XMin, YMin, XMax, YMax) on the current view plane, with the tolerance aTol. Returns True if something is detected. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.

        Returns maps of entities (nodes and elements) detected by mouse selection with the polyline <Polyline> on the current view plane, with the tolerance aTol. Returns True if something is detected. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.

        Filter out the maps of mesh entities so as to keep only the entities that are allowed to be selected according to the current context. Returns True if any of the maps has been changed. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.
        """
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,Polyline : OCP.TColgp.TColgp_Array1OfPnt2d,aBox : OCP.Bnd.Bnd_Box2d,aTol : float,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,XMin : float,YMin : float,XMax : float,YMax : float,aTol : float,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    def GetGeom(self,ID : int,IsElement : bool,Coords : OCP.TColStd.TColStd_Array1OfReal,NbNodes : int,Type : MeshVS_EntityType) -> bool: 
        """
        Returns geometry information about node or element ID is the numerical identificator of node or element IsElement indicates this ID describe node ( if Standard_False ) or element ( if Standard_True ) Coords is an array of coordinates of node(s). For node it is only 3 numbers: X, Y, Z in the strict order For element it is 3*n numbers, where n is number of this element vertices The order is strict also: X1, Y1, Z1, X2,...., where Xi, Yi, Zi are coordinates of vertices NbNodes is number of nodes. It is recommended this parameter to be set to 1 for node. Type is type of node or element (from enumeration). It is recommended this parameter to be set to MeshVS_ET_Node for node.
        """
    def GetGeomType(self,ID : int,IsElement : bool,Type : MeshVS_EntityType) -> bool: 
        """
        This method is similar to GetGeom, but returns only element or node type.
        """
    def GetGroup(self,Id : int,Type : MeshVS_EntityType,Ids : OCP.TColStd.TColStd_PackedMapOfInteger) -> bool: 
        """
        This method returns map of all group elements.
        """
    def GetGroupAddr(self,ID : int) -> capsule: 
        """
        This method returns pointer which represents group data structure. This address will be saved in MeshVS_MeshOwner, so that you can access to data structure fast by the method Owner(). In the redefined method you can return NULL. ID is the numerical identificator of group
        """
    def GetNodeNormal(self,ranknode : int,ElementId : int,nx : float,ny : float,nz : float) -> bool: 
        """
        This method return normal of node ranknode of face Id, which is using for smooth shading presentation. Returns false if normal isn't defined.
        """
    def GetNodesByElement(self,ID : int,NodeIDs : OCP.TColStd.TColStd_Array1OfInteger,NbNodes : int) -> bool: 
        """
        This method returns information about nodes this element consist of. ID is the numerical identificator of element. NodeIDs is the output array of nodes IDs in correct order, the same as coordinates returned by GetGeom(). NbNodes is number of nodes (number of items set in NodeIDs). Returns False if element does not exist
        """
    def GetNormal(self,Id : int,Max : int,nx : float,ny : float,nz : float) -> bool: 
        """
        This method calculates normal of face, which is using for correct reflection presentation. There is default method, for advance reflection this method can be redefined. Id is the numerical identificator of only element! Max is maximal number of nodes an element can consist of nx, ny, nz are values whose represent coordinates of normal (will be returned) In the redefined method you can return normal with length more then 1, but in this case the appearance of element will be more bright than usual. For ordinary brightness you must return normal with length 1
        """
    def GetNormalsByElement(self,Id : int,IsNodal : bool,MaxNodes : int,Normals : OCP.TColStd.TColStd_HArray1OfReal) -> bool: 
        """
        This method puts components of normal vectors at each node of a mesh face (at each face of a mesh volume) into the output array. Returns false if some problem was detected during calculation of normals. Id is an identifier of the mesh element. IsNodal, when true, means that normals at mesh element nodes are needed. If nodal normals are not available, or IsNodal is false, or the mesh element is a volume, then the output array contents depend on the element type: face: a normal calculated by GetNormal() is duplicated for each node of the face; volume: normals to all faces of the volume are computed (not for each node!). MaxNodes is maximal number of nodes an element can consist of. Normals contains the result.
        """
    def GetPrismTopology(self,BasePoints : int) -> MeshVS_HArray1OfSequenceOfInteger: 
        """
        None
        """
    def GetPyramidTopology(self,BasePoints : int) -> MeshVS_HArray1OfSequenceOfInteger: 
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
    def IsAdvancedSelectionEnabled(self) -> bool: 
        """
        Returns True if advanced mesh selection is enabled. Default implementation returns False. It should be redefined to return True for advanced mesh selection activation.
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class MeshVS_DeformedDataSource(MeshVS_DataSource, OCP.Standard.Standard_Transient):
    """
    The class provides default class which helps to represent node displacements by deformed mesh This class has an internal handle to canonical non-deformed mesh data source and map of displacement vectors. The displacement can be magnified to useful size. All methods is implemented with calling the corresponding methods of non-deformed data source.The class provides default class which helps to represent node displacements by deformed mesh This class has an internal handle to canonical non-deformed mesh data source and map of displacement vectors. The displacement can be magnified to useful size. All methods is implemented with calling the corresponding methods of non-deformed data source.The class provides default class which helps to represent node displacements by deformed mesh This class has an internal handle to canonical non-deformed mesh data source and map of displacement vectors. The displacement can be magnified to useful size. All methods is implemented with calling the corresponding methods of non-deformed data source.
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
    def Get3DGeom(self,ID : int,NbNodes : int,Data : MeshVS_HArray1OfSequenceOfInteger) -> bool: 
        """
        None
        """
    def GetAddr(self,ID : int,IsElement : bool) -> capsule: 
        """
        None
        """
    def GetAllElements(self) -> OCP.TColStd.TColStd_PackedMapOfInteger: 
        """
        None
        """
    def GetAllGroups(self,Ids : OCP.TColStd.TColStd_PackedMapOfInteger) -> None: 
        """
        This method returns map of all groups the object contains.
        """
    def GetAllNodes(self) -> OCP.TColStd.TColStd_PackedMapOfInteger: 
        """
        None
        """
    def GetBoundingBox(self) -> OCP.Bnd.Bnd_Box: 
        """
        Returns the bounding box of the whole mesh. It is used in advanced selection mode to define roughly the sensitive area of the mesh. It can be redefined to get access to a box computed in advance.
        """
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,X : float,Y : float,aTol : float,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger,DMin : float) -> bool: 
        """
        Returns maps of entities (nodes and elements) detected by mouse click at the point (X,Y) on the current view plane, with the tolerance aTol. DMin - is out argument should return actual detection tolerance. Returns True if something is detected. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.

        Returns maps of entities (nodes and elements) detected by mouse selection with rectangular box (XMin, YMin, XMax, YMax) on the current view plane, with the tolerance aTol. Returns True if something is detected. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.

        Returns maps of entities (nodes and elements) detected by mouse selection with the polyline <Polyline> on the current view plane, with the tolerance aTol. Returns True if something is detected. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.

        Filter out the maps of mesh entities so as to keep only the entities that are allowed to be selected according to the current context. Returns True if any of the maps has been changed. It should be redefined if the advanced mesh selection is activated. Default implementation returns False.
        """
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,Polyline : OCP.TColgp.TColgp_Array1OfPnt2d,aBox : OCP.Bnd.Bnd_Box2d,aTol : float,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,XMin : float,YMin : float,XMax : float,YMax : float,aTol : float,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    @overload
    def GetDetectedEntities(self,Prs : MeshVS_Mesh,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elements : OCP.TColStd.TColStd_HPackedMapOfInteger) -> bool: ...
    def GetGeom(self,ID : int,IsElement : bool,Coords : OCP.TColStd.TColStd_Array1OfReal,NbNodes : int,Type : MeshVS_EntityType) -> bool: 
        """
        None
        """
    def GetGeomType(self,ID : int,IsElement : bool,Type : MeshVS_EntityType) -> bool: 
        """
        None
        """
    def GetGroup(self,Id : int,Type : MeshVS_EntityType,Ids : OCP.TColStd.TColStd_PackedMapOfInteger) -> bool: 
        """
        This method returns map of all group elements.
        """
    def GetGroupAddr(self,ID : int) -> capsule: 
        """
        This method returns pointer which represents group data structure. This address will be saved in MeshVS_MeshOwner, so that you can access to data structure fast by the method Owner(). In the redefined method you can return NULL. ID is the numerical identificator of group
        """
    def GetMagnify(self) -> float: 
        """
        With this methods you can read and change magnify coefficient of nodal displacements
        """
    def GetNodeNormal(self,ranknode : int,ElementId : int,nx : float,ny : float,nz : float) -> bool: 
        """
        This method return normal of node ranknode of face Id, which is using for smooth shading presentation. Returns false if normal isn't defined.
        """
    def GetNodesByElement(self,ID : int,NodeIDs : OCP.TColStd.TColStd_Array1OfInteger,NbNodes : int) -> bool: 
        """
        None
        """
    def GetNonDeformedDataSource(self) -> MeshVS_DataSource: 
        """
        With this methods you can read and change internal canonical data source
        """
    def GetNormal(self,Id : int,Max : int,nx : float,ny : float,nz : float) -> bool: 
        """
        This method calculates normal of face, which is using for correct reflection presentation. There is default method, for advance reflection this method can be redefined. Id is the numerical identificator of only element! Max is maximal number of nodes an element can consist of nx, ny, nz are values whose represent coordinates of normal (will be returned) In the redefined method you can return normal with length more then 1, but in this case the appearance of element will be more bright than usual. For ordinary brightness you must return normal with length 1
        """
    def GetNormalsByElement(self,Id : int,IsNodal : bool,MaxNodes : int,Normals : OCP.TColStd.TColStd_HArray1OfReal) -> bool: 
        """
        This method puts components of normal vectors at each node of a mesh face (at each face of a mesh volume) into the output array. Returns false if some problem was detected during calculation of normals. Id is an identifier of the mesh element. IsNodal, when true, means that normals at mesh element nodes are needed. If nodal normals are not available, or IsNodal is false, or the mesh element is a volume, then the output array contents depend on the element type: face: a normal calculated by GetNormal() is duplicated for each node of the face; volume: normals to all faces of the volume are computed (not for each node!). MaxNodes is maximal number of nodes an element can consist of. Normals contains the result.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetVector(self,ID : int,Vect : OCP.gp.gp_Vec) -> bool: 
        """
        This method returns vector ( Vect ) assigned to node number ID.
        """
    def GetVectors(self) -> MeshVS_DataMapOfIntegerVector: 
        """
        This method returns map of nodal displacement vectors
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAdvancedSelectionEnabled(self) -> bool: 
        """
        Returns True if advanced mesh selection is enabled. Default implementation returns False. It should be redefined to return True for advanced mesh selection activation.
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
    def SetMagnify(self,theMagnify : float) -> None: 
        """
        None
        """
    def SetNonDeformedDataSource(self,theDS : MeshVS_DataSource) -> None: 
        """
        None
        """
    def SetVector(self,ID : int,Vect : OCP.gp.gp_Vec) -> None: 
        """
        This method sets vector ( Vect ) assigned to node number ID.
        """
    def SetVectors(self,Map : MeshVS_DataMapOfIntegerVector) -> None: 
        """
        This method sets map of nodal displacement vectors (Map).
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theNonDeformDS : MeshVS_DataSource,theMagnify : float) -> None: ...
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
class MeshVS_Drawer(OCP.Standard.Standard_Transient):
    """
    This class provided the common interface to share between classes big set of constants affecting to object appearance. By default, this class can store integers, doubles, OCC colors, OCC materials. Each of OCC enum members can be stored as integers.This class provided the common interface to share between classes big set of constants affecting to object appearance. By default, this class can store integers, doubles, OCC colors, OCC materials. Each of OCC enum members can be stored as integers.This class provided the common interface to share between classes big set of constants affecting to object appearance. By default, this class can store integers, doubles, OCC colors, OCC materials. Each of OCC enum members can be stored as integers.
    """
    def Assign(self,aDrawer : MeshVS_Drawer) -> None: 
        """
        This method copies other drawer contents to this.
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
    def GetAsciiString(self,Key : int,Value : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        None
        """
    def GetBoolean(self,Key : int,Value : bool) -> bool: 
        """
        None
        """
    def GetColor(self,Key : int,Value : OCP.Quantity.Quantity_Color) -> bool: 
        """
        None
        """
    def GetDouble(self,Key : int,Value : float) -> bool: 
        """
        None
        """
    def GetInteger(self,Key : int,Value : int) -> bool: 
        """
        None
        """
    def GetMaterial(self,Key : int,Value : OCP.Graphic3d.Graphic3d_MaterialAspect) -> bool: 
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
    def RemoveAsciiString(self,Key : int) -> bool: 
        """
        None
        """
    def RemoveBoolean(self,Key : int) -> bool: 
        """
        None
        """
    def RemoveColor(self,Key : int) -> bool: 
        """
        None
        """
    def RemoveDouble(self,Key : int) -> bool: 
        """
        None
        """
    def RemoveInteger(self,Key : int) -> bool: 
        """
        None
        """
    def RemoveMaterial(self,Key : int) -> bool: 
        """
        None
        """
    def SetAsciiString(self,Key : int,Value : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetBoolean(self,Key : int,Value : bool) -> None: 
        """
        None
        """
    def SetColor(self,Key : int,Value : OCP.Quantity.Quantity_Color) -> None: 
        """
        None
        """
    def SetDouble(self,Key : int,Value : float) -> None: 
        """
        None
        """
    def SetInteger(self,Key : int,Value : int) -> None: 
        """
        None
        """
    def SetMaterial(self,Key : int,Value : OCP.Graphic3d.Graphic3d_MaterialAspect) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class MeshVS_DrawerAttribute():
    """
    Is it allowed to draw beam and face's edge overlapping with this beam. Is mesh drawn with reflective material Is colored mesh data representation drawn with reflective material What part of face or link will be shown if shrink mode. It is recommended this coeff to be between 0 and 1. How many nodes is possible to be in face If this parameter is true, the compute method CPU time will be displayed in console window If this parameter is true, the compute selection method CPU time will be displayed in console window If this parameter is false, the nodes won't be shown in viewer, otherwise will be.//! If this parameter is true, the selectable nodes map will be updated automatically when hidden elements change//! If this parameter is false, the face's edges are not shown Warning: in wireframe mode this parameter is ignored Is mesh drawing in smooth shading mode Is back faces of volume elements should be suppressed The integer keys for most useful constants attuning mesh presentation appearance WARNING: DA_TextExpansionFactor, DA_TextSpace, DA_TextDisplayType have no effect and might be removed in the future.

    Members:

      MeshVS_DA_InteriorStyle

      MeshVS_DA_InteriorColor

      MeshVS_DA_BackInteriorColor

      MeshVS_DA_EdgeColor

      MeshVS_DA_EdgeType

      MeshVS_DA_EdgeWidth

      MeshVS_DA_HatchStyle

      MeshVS_DA_FrontMaterial

      MeshVS_DA_BackMaterial

      MeshVS_DA_BeamType

      MeshVS_DA_BeamWidth

      MeshVS_DA_BeamColor

      MeshVS_DA_MarkerType

      MeshVS_DA_MarkerColor

      MeshVS_DA_MarkerScale

      MeshVS_DA_TextColor

      MeshVS_DA_TextHeight

      MeshVS_DA_TextFont

      MeshVS_DA_TextExpansionFactor

      MeshVS_DA_TextSpace

      MeshVS_DA_TextStyle

      MeshVS_DA_TextDisplayType

      MeshVS_DA_TextTexFont

      MeshVS_DA_TextFontAspect

      MeshVS_DA_VectorColor

      MeshVS_DA_VectorMaxLength

      MeshVS_DA_VectorArrowPart

      MeshVS_DA_IsAllowOverlapped

      MeshVS_DA_Reflection

      MeshVS_DA_ColorReflection

      MeshVS_DA_ShrinkCoeff

      MeshVS_DA_MaxFaceNodes

      MeshVS_DA_ComputeTime

      MeshVS_DA_ComputeSelectionTime

      MeshVS_DA_DisplayNodes

      MeshVS_DA_SelectableAuto

      MeshVS_DA_ShowEdges

      MeshVS_DA_SmoothShading

      MeshVS_DA_SupressBackFaces

      MeshVS_DA_User
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
    MeshVS_DA_BackInteriorColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BackInteriorColor: 2>
    MeshVS_DA_BackMaterial: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BackMaterial: 8>
    MeshVS_DA_BeamColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BeamColor: 11>
    MeshVS_DA_BeamType: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BeamType: 9>
    MeshVS_DA_BeamWidth: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BeamWidth: 10>
    MeshVS_DA_ColorReflection: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ColorReflection: 29>
    MeshVS_DA_ComputeSelectionTime: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ComputeSelectionTime: 33>
    MeshVS_DA_ComputeTime: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ComputeTime: 32>
    MeshVS_DA_DisplayNodes: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_DisplayNodes: 34>
    MeshVS_DA_EdgeColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_EdgeColor: 3>
    MeshVS_DA_EdgeType: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_EdgeType: 4>
    MeshVS_DA_EdgeWidth: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_EdgeWidth: 5>
    MeshVS_DA_FrontMaterial: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_FrontMaterial: 7>
    MeshVS_DA_HatchStyle: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_HatchStyle: 6>
    MeshVS_DA_InteriorColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor: 1>
    MeshVS_DA_InteriorStyle: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_InteriorStyle: 0>
    MeshVS_DA_IsAllowOverlapped: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_IsAllowOverlapped: 27>
    MeshVS_DA_MarkerColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_MarkerColor: 13>
    MeshVS_DA_MarkerScale: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_MarkerScale: 14>
    MeshVS_DA_MarkerType: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_MarkerType: 12>
    MeshVS_DA_MaxFaceNodes: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_MaxFaceNodes: 31>
    MeshVS_DA_Reflection: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_Reflection: 28>
    MeshVS_DA_SelectableAuto: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_SelectableAuto: 35>
    MeshVS_DA_ShowEdges: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ShowEdges: 36>
    MeshVS_DA_ShrinkCoeff: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ShrinkCoeff: 30>
    MeshVS_DA_SmoothShading: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_SmoothShading: 37>
    MeshVS_DA_SupressBackFaces: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_SupressBackFaces: 38>
    MeshVS_DA_TextColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextColor: 15>
    MeshVS_DA_TextDisplayType: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextDisplayType: 21>
    MeshVS_DA_TextExpansionFactor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextExpansionFactor: 18>
    MeshVS_DA_TextFont: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextFont: 17>
    MeshVS_DA_TextFontAspect: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextFontAspect: 23>
    MeshVS_DA_TextHeight: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextHeight: 16>
    MeshVS_DA_TextSpace: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextSpace: 19>
    MeshVS_DA_TextStyle: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextStyle: 20>
    MeshVS_DA_TextTexFont: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextTexFont: 22>
    MeshVS_DA_User: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_User: 39>
    MeshVS_DA_VectorArrowPart: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_VectorArrowPart: 26>
    MeshVS_DA_VectorColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_VectorColor: 24>
    MeshVS_DA_VectorMaxLength: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_VectorMaxLength: 25>
    __entries: dict # value = {'MeshVS_DA_InteriorStyle': (<MeshVS_DrawerAttribute.MeshVS_DA_InteriorStyle: 0>, None), 'MeshVS_DA_InteriorColor': (<MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor: 1>, None), 'MeshVS_DA_BackInteriorColor': (<MeshVS_DrawerAttribute.MeshVS_DA_BackInteriorColor: 2>, None), 'MeshVS_DA_EdgeColor': (<MeshVS_DrawerAttribute.MeshVS_DA_EdgeColor: 3>, None), 'MeshVS_DA_EdgeType': (<MeshVS_DrawerAttribute.MeshVS_DA_EdgeType: 4>, None), 'MeshVS_DA_EdgeWidth': (<MeshVS_DrawerAttribute.MeshVS_DA_EdgeWidth: 5>, None), 'MeshVS_DA_HatchStyle': (<MeshVS_DrawerAttribute.MeshVS_DA_HatchStyle: 6>, None), 'MeshVS_DA_FrontMaterial': (<MeshVS_DrawerAttribute.MeshVS_DA_FrontMaterial: 7>, None), 'MeshVS_DA_BackMaterial': (<MeshVS_DrawerAttribute.MeshVS_DA_BackMaterial: 8>, None), 'MeshVS_DA_BeamType': (<MeshVS_DrawerAttribute.MeshVS_DA_BeamType: 9>, None), 'MeshVS_DA_BeamWidth': (<MeshVS_DrawerAttribute.MeshVS_DA_BeamWidth: 10>, None), 'MeshVS_DA_BeamColor': (<MeshVS_DrawerAttribute.MeshVS_DA_BeamColor: 11>, None), 'MeshVS_DA_MarkerType': (<MeshVS_DrawerAttribute.MeshVS_DA_MarkerType: 12>, None), 'MeshVS_DA_MarkerColor': (<MeshVS_DrawerAttribute.MeshVS_DA_MarkerColor: 13>, None), 'MeshVS_DA_MarkerScale': (<MeshVS_DrawerAttribute.MeshVS_DA_MarkerScale: 14>, None), 'MeshVS_DA_TextColor': (<MeshVS_DrawerAttribute.MeshVS_DA_TextColor: 15>, None), 'MeshVS_DA_TextHeight': (<MeshVS_DrawerAttribute.MeshVS_DA_TextHeight: 16>, None), 'MeshVS_DA_TextFont': (<MeshVS_DrawerAttribute.MeshVS_DA_TextFont: 17>, None), 'MeshVS_DA_TextExpansionFactor': (<MeshVS_DrawerAttribute.MeshVS_DA_TextExpansionFactor: 18>, None), 'MeshVS_DA_TextSpace': (<MeshVS_DrawerAttribute.MeshVS_DA_TextSpace: 19>, None), 'MeshVS_DA_TextStyle': (<MeshVS_DrawerAttribute.MeshVS_DA_TextStyle: 20>, None), 'MeshVS_DA_TextDisplayType': (<MeshVS_DrawerAttribute.MeshVS_DA_TextDisplayType: 21>, None), 'MeshVS_DA_TextTexFont': (<MeshVS_DrawerAttribute.MeshVS_DA_TextTexFont: 22>, None), 'MeshVS_DA_TextFontAspect': (<MeshVS_DrawerAttribute.MeshVS_DA_TextFontAspect: 23>, None), 'MeshVS_DA_VectorColor': (<MeshVS_DrawerAttribute.MeshVS_DA_VectorColor: 24>, None), 'MeshVS_DA_VectorMaxLength': (<MeshVS_DrawerAttribute.MeshVS_DA_VectorMaxLength: 25>, None), 'MeshVS_DA_VectorArrowPart': (<MeshVS_DrawerAttribute.MeshVS_DA_VectorArrowPart: 26>, None), 'MeshVS_DA_IsAllowOverlapped': (<MeshVS_DrawerAttribute.MeshVS_DA_IsAllowOverlapped: 27>, None), 'MeshVS_DA_Reflection': (<MeshVS_DrawerAttribute.MeshVS_DA_Reflection: 28>, None), 'MeshVS_DA_ColorReflection': (<MeshVS_DrawerAttribute.MeshVS_DA_ColorReflection: 29>, None), 'MeshVS_DA_ShrinkCoeff': (<MeshVS_DrawerAttribute.MeshVS_DA_ShrinkCoeff: 30>, None), 'MeshVS_DA_MaxFaceNodes': (<MeshVS_DrawerAttribute.MeshVS_DA_MaxFaceNodes: 31>, None), 'MeshVS_DA_ComputeTime': (<MeshVS_DrawerAttribute.MeshVS_DA_ComputeTime: 32>, None), 'MeshVS_DA_ComputeSelectionTime': (<MeshVS_DrawerAttribute.MeshVS_DA_ComputeSelectionTime: 33>, None), 'MeshVS_DA_DisplayNodes': (<MeshVS_DrawerAttribute.MeshVS_DA_DisplayNodes: 34>, None), 'MeshVS_DA_SelectableAuto': (<MeshVS_DrawerAttribute.MeshVS_DA_SelectableAuto: 35>, None), 'MeshVS_DA_ShowEdges': (<MeshVS_DrawerAttribute.MeshVS_DA_ShowEdges: 36>, None), 'MeshVS_DA_SmoothShading': (<MeshVS_DrawerAttribute.MeshVS_DA_SmoothShading: 37>, None), 'MeshVS_DA_SupressBackFaces': (<MeshVS_DrawerAttribute.MeshVS_DA_SupressBackFaces: 38>, None), 'MeshVS_DA_User': (<MeshVS_DrawerAttribute.MeshVS_DA_User: 39>, None)}
    __members__: dict # value = {'MeshVS_DA_InteriorStyle': <MeshVS_DrawerAttribute.MeshVS_DA_InteriorStyle: 0>, 'MeshVS_DA_InteriorColor': <MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor: 1>, 'MeshVS_DA_BackInteriorColor': <MeshVS_DrawerAttribute.MeshVS_DA_BackInteriorColor: 2>, 'MeshVS_DA_EdgeColor': <MeshVS_DrawerAttribute.MeshVS_DA_EdgeColor: 3>, 'MeshVS_DA_EdgeType': <MeshVS_DrawerAttribute.MeshVS_DA_EdgeType: 4>, 'MeshVS_DA_EdgeWidth': <MeshVS_DrawerAttribute.MeshVS_DA_EdgeWidth: 5>, 'MeshVS_DA_HatchStyle': <MeshVS_DrawerAttribute.MeshVS_DA_HatchStyle: 6>, 'MeshVS_DA_FrontMaterial': <MeshVS_DrawerAttribute.MeshVS_DA_FrontMaterial: 7>, 'MeshVS_DA_BackMaterial': <MeshVS_DrawerAttribute.MeshVS_DA_BackMaterial: 8>, 'MeshVS_DA_BeamType': <MeshVS_DrawerAttribute.MeshVS_DA_BeamType: 9>, 'MeshVS_DA_BeamWidth': <MeshVS_DrawerAttribute.MeshVS_DA_BeamWidth: 10>, 'MeshVS_DA_BeamColor': <MeshVS_DrawerAttribute.MeshVS_DA_BeamColor: 11>, 'MeshVS_DA_MarkerType': <MeshVS_DrawerAttribute.MeshVS_DA_MarkerType: 12>, 'MeshVS_DA_MarkerColor': <MeshVS_DrawerAttribute.MeshVS_DA_MarkerColor: 13>, 'MeshVS_DA_MarkerScale': <MeshVS_DrawerAttribute.MeshVS_DA_MarkerScale: 14>, 'MeshVS_DA_TextColor': <MeshVS_DrawerAttribute.MeshVS_DA_TextColor: 15>, 'MeshVS_DA_TextHeight': <MeshVS_DrawerAttribute.MeshVS_DA_TextHeight: 16>, 'MeshVS_DA_TextFont': <MeshVS_DrawerAttribute.MeshVS_DA_TextFont: 17>, 'MeshVS_DA_TextExpansionFactor': <MeshVS_DrawerAttribute.MeshVS_DA_TextExpansionFactor: 18>, 'MeshVS_DA_TextSpace': <MeshVS_DrawerAttribute.MeshVS_DA_TextSpace: 19>, 'MeshVS_DA_TextStyle': <MeshVS_DrawerAttribute.MeshVS_DA_TextStyle: 20>, 'MeshVS_DA_TextDisplayType': <MeshVS_DrawerAttribute.MeshVS_DA_TextDisplayType: 21>, 'MeshVS_DA_TextTexFont': <MeshVS_DrawerAttribute.MeshVS_DA_TextTexFont: 22>, 'MeshVS_DA_TextFontAspect': <MeshVS_DrawerAttribute.MeshVS_DA_TextFontAspect: 23>, 'MeshVS_DA_VectorColor': <MeshVS_DrawerAttribute.MeshVS_DA_VectorColor: 24>, 'MeshVS_DA_VectorMaxLength': <MeshVS_DrawerAttribute.MeshVS_DA_VectorMaxLength: 25>, 'MeshVS_DA_VectorArrowPart': <MeshVS_DrawerAttribute.MeshVS_DA_VectorArrowPart: 26>, 'MeshVS_DA_IsAllowOverlapped': <MeshVS_DrawerAttribute.MeshVS_DA_IsAllowOverlapped: 27>, 'MeshVS_DA_Reflection': <MeshVS_DrawerAttribute.MeshVS_DA_Reflection: 28>, 'MeshVS_DA_ColorReflection': <MeshVS_DrawerAttribute.MeshVS_DA_ColorReflection: 29>, 'MeshVS_DA_ShrinkCoeff': <MeshVS_DrawerAttribute.MeshVS_DA_ShrinkCoeff: 30>, 'MeshVS_DA_MaxFaceNodes': <MeshVS_DrawerAttribute.MeshVS_DA_MaxFaceNodes: 31>, 'MeshVS_DA_ComputeTime': <MeshVS_DrawerAttribute.MeshVS_DA_ComputeTime: 32>, 'MeshVS_DA_ComputeSelectionTime': <MeshVS_DrawerAttribute.MeshVS_DA_ComputeSelectionTime: 33>, 'MeshVS_DA_DisplayNodes': <MeshVS_DrawerAttribute.MeshVS_DA_DisplayNodes: 34>, 'MeshVS_DA_SelectableAuto': <MeshVS_DrawerAttribute.MeshVS_DA_SelectableAuto: 35>, 'MeshVS_DA_ShowEdges': <MeshVS_DrawerAttribute.MeshVS_DA_ShowEdges: 36>, 'MeshVS_DA_SmoothShading': <MeshVS_DrawerAttribute.MeshVS_DA_SmoothShading: 37>, 'MeshVS_DA_SupressBackFaces': <MeshVS_DrawerAttribute.MeshVS_DA_SupressBackFaces: 38>, 'MeshVS_DA_User': <MeshVS_DrawerAttribute.MeshVS_DA_User: 39>}
    pass
class MeshVS_DummySensitiveEntity(OCP.Select3D.Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    This class allows to create owners to all elements or nodes, both hidden and shown, but these owners user cannot select "by hands" in viewer. They means for internal application tasks, for example, receiving all owners, both for hidden and shown entities.This class allows to create owners to all elements or nodes, both hidden and shown, but these owners user cannot select "by hands" in viewer. They means for internal application tasks, for example, receiving all owners, both for hidden and shown entities.
    """
    def BVH(self) -> None: 
        """
        None
        """
    def BoundingBox(self) -> Any: 
        """
        None
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        None
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        Originally this method intended to return sensitive entity with new location aLocation, but currently sensitive entities do not hold a location, instead HasLocation() and Location() methods call corresponding entity owner's methods. Thus all entities returned by GetConnected() share the same location propagated from corresponding selectable object. You must redefine this function for any type of sensitive entity which can accept another connected sensitive entity.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasInitLocation(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvInitLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        None
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
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        None
        """
    def NbSubElements(self) -> int: 
        """
        None
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToBuildBVH(self) -> bool: 
        """
        None
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: ...
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
class MeshVS_PrsBuilder(OCP.Standard.Standard_Transient):
    """
    This class is parent for all builders using in MeshVS_Mesh. It provides base fields and methods all buildes need.This class is parent for all builders using in MeshVS_Mesh. It provides base fields and methods all buildes need.
    """
    def Build(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,IsElement : bool,DisplayMode : int) -> None: 
        """
        Builds presentation of certain type of data. Prs is presentation object which this method constructs. IDs is set of numeric identificators forming object appearance. IDsToExclude is set of IDs to exclude from processing. If some entity has been excluded, it is not processed by other builders. IsElement indicates, IDs is identificators of nodes or elements. DisplayMode is numeric constant describing display mode (see MeshVS_DisplayModeFlags.hxx)
        """
    def CustomBuild(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,DisplayMode : int) -> None: 
        """
        This method is called to build presentation of custom elements (they have MeshVS_ET_0D type). IDs is set of numeric identificators of elements for custom building. IDsToExclude is set of IDs to exclude from processing. If some entity has been excluded, it is not processed by other builders. DisplayMode is numeric constant describing display mode (see MeshVS_DisplayModeFlags.hxx)
        """
    def CustomSensitiveEntity(self,Owner : OCP.SelectMgr.SelectMgr_EntityOwner,SelectMode : int) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        This method is called to build sensitive of custom elements ( they have MeshVS_ET_0D type )
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
    def GetDataSource(self) -> MeshVS_DataSource: 
        """
        Returns custom data source or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetDrawer(self) -> MeshVS_Drawer: 
        """
        Returns custom drawer or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetFlags(self) -> int: 
        """
        Returns flags, assigned with builder during creation
        """
    def GetId(self) -> int: 
        """
        Returns builder ID
        """
    def GetPresentationManager(self) -> OCP.PrsMgr.PrsMgr_PresentationManager: 
        """
        Get presentation manager of builder
        """
    def GetPriority(self) -> int: 
        """
        Returns priority; as priority bigger, as soon builder will be called.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsExcludingOn(self) -> bool: 
        """
        Read excluding state
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
    def SetDataSource(self,newDS : MeshVS_DataSource) -> None: 
        """
        Change custom data source
        """
    def SetDrawer(self,newDr : MeshVS_Drawer) -> None: 
        """
        Change custom drawer
        """
    def SetExcluding(self,state : bool) -> None: 
        """
        Set excluding state. If it is Standard_True, the nodes or elements, processed by current builder will be noted and next builder won't process its.
        """
    def SetPresentationManager(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> None: 
        """
        Set presentation manager for builder
        """
    def TestFlags(self,DisplayMode : int) -> bool: 
        """
        Test whether display mode has flags assigned with this builder. This method has default implementation and can be redefined for advance behavior Returns Standard_True only if display mode is appropriate for this builder
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class MeshVS_EntityType():
    """
    None

    Members:

      MeshVS_ET_NONE

      MeshVS_ET_Node

      MeshVS_ET_0D

      MeshVS_ET_Link

      MeshVS_ET_Face

      MeshVS_ET_Volume

      MeshVS_ET_Element

      MeshVS_ET_All
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
    MeshVS_ET_0D: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_0D: 2>
    MeshVS_ET_All: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_All: 31>
    MeshVS_ET_Element: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Element: 30>
    MeshVS_ET_Face: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Face: 8>
    MeshVS_ET_Link: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Link: 4>
    MeshVS_ET_NONE: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_NONE: 0>
    MeshVS_ET_Node: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Node: 1>
    MeshVS_ET_Volume: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Volume: 16>
    __entries: dict # value = {'MeshVS_ET_NONE': (<MeshVS_EntityType.MeshVS_ET_NONE: 0>, None), 'MeshVS_ET_Node': (<MeshVS_EntityType.MeshVS_ET_Node: 1>, None), 'MeshVS_ET_0D': (<MeshVS_EntityType.MeshVS_ET_0D: 2>, None), 'MeshVS_ET_Link': (<MeshVS_EntityType.MeshVS_ET_Link: 4>, None), 'MeshVS_ET_Face': (<MeshVS_EntityType.MeshVS_ET_Face: 8>, None), 'MeshVS_ET_Volume': (<MeshVS_EntityType.MeshVS_ET_Volume: 16>, None), 'MeshVS_ET_Element': (<MeshVS_EntityType.MeshVS_ET_Element: 30>, None), 'MeshVS_ET_All': (<MeshVS_EntityType.MeshVS_ET_All: 31>, None)}
    __members__: dict # value = {'MeshVS_ET_NONE': <MeshVS_EntityType.MeshVS_ET_NONE: 0>, 'MeshVS_ET_Node': <MeshVS_EntityType.MeshVS_ET_Node: 1>, 'MeshVS_ET_0D': <MeshVS_EntityType.MeshVS_ET_0D: 2>, 'MeshVS_ET_Link': <MeshVS_EntityType.MeshVS_ET_Link: 4>, 'MeshVS_ET_Face': <MeshVS_EntityType.MeshVS_ET_Face: 8>, 'MeshVS_ET_Volume': <MeshVS_EntityType.MeshVS_ET_Volume: 16>, 'MeshVS_ET_Element': <MeshVS_EntityType.MeshVS_ET_Element: 30>, 'MeshVS_ET_All': <MeshVS_EntityType.MeshVS_ET_All: 31>}
    pass
class MeshVS_HArray1OfSequenceOfInteger(MeshVS_Array1OfSequenceOfInteger, OCP.Standard.Standard_Transient):
    def Array1(self) -> MeshVS_Array1OfSequenceOfInteger: 
        """
        None
        """
    def Assign(self,theOther : MeshVS_Array1OfSequenceOfInteger) -> MeshVS_Array1OfSequenceOfInteger: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> MeshVS_Array1OfSequenceOfInteger: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Variable value access
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
    def First(self) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : OCP.TColStd.TColStd_SequenceOfInteger) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : MeshVS_Array1OfSequenceOfInteger) -> MeshVS_Array1OfSequenceOfInteger: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TColStd.TColStd_SequenceOfInteger) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : MeshVS_Array1OfSequenceOfInteger) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.TColStd.TColStd_SequenceOfInteger) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class MeshVS_MapOfTwoNodes(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : MeshVS_TwoNodes) -> bool: 
        """
        Add
        """
    def Added(self,K : MeshVS_TwoNodes) -> MeshVS_TwoNodes: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MeshVS_MapOfTwoNodes) -> MeshVS_MapOfTwoNodes: 
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
    def Contains(self,K : MeshVS_TwoNodes) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : MeshVS_MapOfTwoNodes) -> bool: ...
    def Differ(self,theOther : MeshVS_MapOfTwoNodes) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : MeshVS_MapOfTwoNodes,theRight : MeshVS_MapOfTwoNodes) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : MeshVS_MapOfTwoNodes) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : MeshVS_MapOfTwoNodes) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : MeshVS_MapOfTwoNodes) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : MeshVS_MapOfTwoNodes,theRight : MeshVS_MapOfTwoNodes) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : MeshVS_MapOfTwoNodes) -> bool: 
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
    def Remove(self,K : MeshVS_TwoNodes) -> bool: 
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
    def Subtract(self,theOther : MeshVS_MapOfTwoNodes) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : MeshVS_MapOfTwoNodes,theRight : MeshVS_MapOfTwoNodes) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : MeshVS_MapOfTwoNodes,theRight : MeshVS_MapOfTwoNodes) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : MeshVS_MapOfTwoNodes) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theOther : MeshVS_MapOfTwoNodes) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class MeshVS_Mesh(OCP.AIS.AIS_InteractiveObject, OCP.SelectMgr.SelectMgr_SelectableObject, OCP.PrsMgr.PrsMgr_PresentableObject, OCP.Standard.Standard_Transient):
    """
    the main class provides interface to create mesh presentation as a wholethe main class provides interface to create mesh presentation as a whole
    """
    def AcceptDisplayMode(self,theMode : int) -> bool: 
        """
        Returns true for supported display modes basing on a list of defined builders.
        """
    def AcceptShapeDecomposition(self) -> bool: 
        """
        Informs the graphic context that the interactive Object may be decomposed into sub-shapes for dynamic selection. The most used Interactive Object is AIS_Shape.
        """
    def AddBuilder(self,Builder : MeshVS_PrsBuilder,TreatAsHilighter : bool=False) -> None: 
        """
        Adds builder to tale of sequence. PrsBuilder is builder to be added If TreatAsHilighter is true, MeshVS_Mesh will use this builder to create presentation of hilighted and selected owners. Only one builder can be hilighter, so that if you call this method with TreatAsHilighter = Standard_True some times, only last builder will be hilighter WARNING: As minimum one builder must be added as hilighter, otherwise selection cannot be computed
        """
    def AddChild(self,theObject : OCP.PrsMgr.PrsMgr_PresentableObject) -> None: 
        """
        Makes theObject child of current object in scene hierarchy.
        """
    def AddChildWithCurrentTransformation(self,theObject : OCP.PrsMgr.PrsMgr_PresentableObject) -> None: 
        """
        Makes theObject child of current object in scene hierarchy with keeping the current global transformation So the object keeps the same position/orientation in the global CS.
        """
    def AddClipPlane(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> None: 
        """
        Adds clip plane for graphical clipping for all display mode presentations. The composition of clip planes truncates the rendering space to convex volume. Please be aware that number of supported clip plane is limited. The planes which exceed the limit are ignored. Besides of this, some planes can be already set in view where the object is shown: the number of these planes should be subtracted from limit to predict the maximum possible number of object clipping planes.
        """
    def AddSelection(self,aSelection : OCP.SelectMgr.SelectMgr_Selection,aMode : int) -> None: 
        """
        Adds the selection aSelection with the selection mode index aMode to this framework.
        """
    def Attributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Returns the attributes settings.
        """
    def BndBoxOfSelected(self,theOwners : Any) -> OCP.Bnd.Bnd_Box: 
        """
        Returns a bounding box of sensitive entities with the owners given if they are a part of activated selection
        """
    def BoundingBox(self,theBndBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        Returns bounding box of object correspondingly to its current display mode. This method requires presentation to be already computed, since it relies on bounding box of presentation structures, which are supposed to be same/close amongst different display modes of this object.
        """
    def Children(self) -> OCP.PrsMgr.PrsMgr_ListOfPresentableObjects: 
        """
        Returns children of the current object.
        """
    def ClearDynamicHighlight(self,theMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> None: 
        """
        Method that needs to be implemented when the object manages selection and dynamic highlighting on its own. Clears or invalidates dynamic highlight presentation. By default it clears immediate draw of given presentation manager.
        """
    def ClearOwner(self) -> None: 
        """
        Each Interactive Object has methods which allow us to attribute an Owner to it in the form of a Transient. This method removes the owner from the graphic entity.
        """
    def ClearSelected(self) -> None: 
        """
        Clears internal selection presentation
        """
    def ClearSelections(self,update : bool=False) -> None: 
        """
        Empties all the selections in the SelectableObject <update> parameter defines whether all object's selections should be flagged for further update or not. This improved method can be used to recompute an object's selection (without redisplaying the object completely) when some selection mode is activated not for the first time.
        """
    def ClipPlanes(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Get clip planes.
        """
    def Color(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns the color setting of the Interactive Object.
        """
    def CombinedParentTransformation(self) -> OCP.TopLoc.TopLoc_Datum3D: 
        """
        Return combined parent transformation.
        """
    def Compute(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,thePrs : OCP.Graphic3d.Graphic3d_Structure,theDispMode : int) -> None: 
        """
        Computes presentation using builders added to sequence. Each builder computes own part of mesh presentation according to its type.
        """
    def ComputeSelection(self,theSel : OCP.SelectMgr.SelectMgr_Selection,theSelMode : int) -> None: 
        """
        Computes selection according to SelectMode
        """
    def CurrentFacingModel(self) -> OCP.Aspect.Aspect_TypeOfFacingModel: 
        """
        Returns the current facing model which is in effect.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultDisplayMode(self) -> int: 
        """
        Returns the default display mode.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisplayMode(self) -> int: 
        """
        Returns the display mode setting of the Interactive Object. The range of supported display mode indexes should be specified within object definition and filtered by AccepDisplayMode().
        """
    def DisplayStatus(self) -> OCP.PrsMgr.PrsMgr_DisplayStatus: 
        """
        Return presentation display status; PrsMgr_DisplayStatus_None by default.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicHilightAttributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Returns the hilight attributes settings. When not NULL, overrides both Prs3d_TypeOfHighlight_LocalDynamic and Prs3d_TypeOfHighlight_Dynamic defined within AIS_InteractiveContext::HighlightStyle().
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ErasePresentations(self,theToRemove : bool) -> None: 
        """
        Removes presentations returned by GetHilightPresentation() and GetSelectPresentation().
        """
    def FindBuilder(self,TypeString : str) -> MeshVS_PrsBuilder: 
        """
        Finds builder by its type the string represents
        """
    def GetAssemblyOwner(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns common entity owner if the object is an assembly
        """
    def GetBuilder(self,Index : int) -> MeshVS_PrsBuilder: 
        """
        Returns builder by its index in sequence
        """
    def GetBuilderById(self,Id : int) -> MeshVS_PrsBuilder: 
        """
        Returns builder by its ID
        """
    def GetBuildersCount(self) -> int: 
        """
        How many builders there are in sequence
        """
    def GetContext(self) -> OCP.AIS.AIS_InteractiveContext: 
        """
        Returns the context pointer to the interactive context.
        """
    def GetDataSource(self) -> MeshVS_DataSource: 
        """
        Returns default builders' data source
        """
    def GetDrawer(self) -> MeshVS_Drawer: 
        """
        Returns default builders' drawer
        """
    def GetFreeId(self) -> int: 
        """
        Returns the smallest positive ID, not occupied by any builder. This method using when builder is created with ID = -1
        """
    def GetHiddenElems(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Returns map of hidden elements (may be null handle)
        """
    def GetHiddenNodes(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Returns map of hidden nodes (may be null handle)
        """
    def GetHilightPresentation(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Creates or returns existing presentation for highlighting detected object.
        """
    def GetHilighter(self) -> MeshVS_PrsBuilder: 
        """
        Returns hilighter
        """
    def GetMeshSelMethod(self) -> MeshVS_MeshSelectionMethod: 
        """
        Returns set mesh selection method (see MeshVS.cdl)
        """
    def GetOwner(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the owner of the Interactive Object. The owner can be a shape for a set of sub-shapes or a sub-shape for sub-shapes which it is composed of, and takes the form of a transient. There are two types of owners: - Direct owners, decomposition shapes such as edges, wires, and faces. - Users, presentable objects connecting to sensitive primitives, or a shape which has been decomposed.
        """
    def GetOwnerMaps(self,IsElement : bool) -> Any: 
        """
        Returns map of owners.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectPresentation(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Creates or returns existing presentation for highlighting selected object.
        """
    def GetSelectableNodes(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Returns map of selectable elements (may be null handle)
        """
    def GlobalSelOwner(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns the owner of mode for selection of object as a whole
        """
    def GlobalSelectionMode(self) -> int: 
        """
        Returns the mode for selection of object as a whole; 0 by default.
        """
    def HasColor(self) -> bool: 
        """
        Returns true if the Interactive Object has color.
        """
    def HasDisplayMode(self) -> bool: 
        """
        Returns true if the Interactive Object has display mode setting overriding global setting (within Interactive Context).
        """
    def HasHilightMode(self) -> bool: 
        """
        Returns true if the Interactive Object is in highlight mode.
        """
    def HasInteractiveContext(self) -> bool: 
        """
        Indicates whether the Interactive Object has a pointer to an interactive context.
        """
    def HasMaterial(self) -> bool: 
        """
        Returns true if the Interactive Object has a setting for material.
        """
    def HasOwnPresentations(self) -> bool: 
        """
        Returns true if object should have own presentations.
        """
    def HasOwner(self) -> bool: 
        """
        Returns true if the object has an owner attributed to it. The owner can be a shape for a set of sub-shapes or a sub-shape for sub-shapes which it is composed of, and takes the form of a transient.
        """
    def HasPolygonOffsets(self) -> bool: 
        """
        Returns Standard_True if <myDrawer> has non-null shading aspect
        """
    def HasPresentation(self) -> bool: 
        """
        Returns TRUE when this object has a presentation in the current DisplayMode()
        """
    def HasSelection(self,theMode : int) -> bool: 
        """
        Returns true if a selection corresponding to the selection mode theMode was computed for this object.
        """
    def HasTransformation(self) -> bool: 
        """
        Returns true if object has a transformation that is different from the identity.
        """
    def HasWidth(self) -> bool: 
        """
        Returns true if the Interactive Object has width.
        """
    def HilightAttributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Returns the hilight attributes settings. When not NULL, overrides both Prs3d_TypeOfHighlight_LocalSelected and Prs3d_TypeOfHighlight_Selected defined within AIS_InteractiveContext::HighlightStyle().
        """
    def HilightMode(self) -> int: 
        """
        Returns highlight display mode. This is obsolete method for backward compatibility - use ::HilightAttributes() and ::DynamicHilightAttributes() instead.
        """
    def HilightOwnerWithColor(self,thePM : OCP.PrsMgr.PrsMgr_PresentationManager,theColor : OCP.Prs3d.Prs3d_Drawer,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Draw hilighted owner presentation
        """
    def HilightSelected(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,theOwners : OCP.SelectMgr.SelectMgr_SequenceOfOwner) -> None: 
        """
        Draw selected owners presentation
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InteractiveContext(self) -> OCP.AIS.AIS_InteractiveContext: 
        """
        Returns the context pointer to the interactive context.
        """
    def InversedTransformation(self) -> OCP.gp.gp_GTrsf: 
        """
        Return inversed transformation.
        """
    def IsAutoHilight(self) -> bool: 
        """
        If returns True, the old mechanism for highlighting selected objects is used (HilightSelected Method may be empty). If returns False, the HilightSelected method will be fully responsible for highlighting selected entity owners belonging to this selectable object.
        """
    def IsHiddenElem(self,ID : int) -> bool: 
        """
        Returns True if specified element is hidden By default no elements are hidden
        """
    def IsHiddenNode(self,ID : int) -> bool: 
        """
        Returns True if specified node is hidden. By default all nodes are hidden
        """
    def IsInfinite(self) -> bool: 
        """
        Returns true if the interactive object is infinite; FALSE by default. This flag affects various operations operating on bounding box of graphic presentations of this object. For instance, infinite objects are not taken in account for View FitAll. This does not necessarily means that object is actually infinite, auxiliary objects might be also marked with this flag to achieve desired behavior.
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
    def IsMutable(self) -> bool: 
        """
        Returns true if object has mutable nature (content or location are be changed regularly). Mutable object will be managed in different way than static onces (another optimizations).
        """
    def IsSelectableElem(self,ID : int) -> bool: 
        """
        Returns True if specified element is not hidden
        """
    def IsSelectableNode(self,ID : int) -> bool: 
        """
        Returns True if specified node is specified as selectable.
        """
    def IsTransparent(self) -> bool: 
        """
        Returns true if there is a transparency setting.
        """
    def IsWholeMeshOwner(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner) -> bool: 
        """
        Returns True if the given owner represents a whole mesh.
        """
    def LocalTransformation(self) -> OCP.gp.gp_Trsf: 
        """
        Return the local transformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def LocalTransformationGeom(self) -> OCP.TopLoc.TopLoc_Datum3D: 
        """
        Return the local transformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def Material(self) -> OCP.Graphic3d.Graphic3d_NameOfMaterial: 
        """
        Returns the current material setting as enumeration value.
        """
    def Parent(self) -> OCP.PrsMgr.PrsMgr_PresentableObject: 
        """
        Returns parent of current object in scene hierarchy.
        """
    def PolygonOffsets(self,aFactor : float,aUnits : float) -> Tuple[int]: 
        """
        Retrieves current polygon offsets settings from <myDrawer>.
        """
    def Presentation(self) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Returns the current presentation of this object according to the current DisplayMode()
        """
    def Presentations(self) -> OCP.PrsMgr.PrsMgr_Presentations: 
        """
        Return presentations.
        """
    def ProcessDragging(self,theCtx : OCP.AIS.AIS_InteractiveContext,theView : OCP.V3d.V3d_View,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theDragFrom : OCP.Graphic3d.Graphic3d_Vec2i,theDragTo : OCP.Graphic3d.Graphic3d_Vec2i,theAction : OCP.AIS.AIS_DragAction) -> bool: 
        """
        Drag object in the viewer.
        """
    @overload
    def RecomputePrimitives(self) -> None: 
        """
        Re-computes the sensitive primitives for all modes. IMPORTANT: Do not use this method to update selection primitives except implementing custom selection manager! This method does not take into account necessary BVH updates, but may invalidate the pointers it refers to. TO UPDATE SELECTION properly from outside classes, use method UpdateSelection.

        Re-computes the sensitive primitives which correspond to the <theMode>th selection mode. IMPORTANT: Do not use this method to update selection primitives except implementing custom selection manager! selection manager! This method does not take into account necessary BVH updates, but may invalidate the pointers it refers to. TO UPDATE SELECTION properly from outside classes, use method UpdateSelection.
        """
    @overload
    def RecomputePrimitives(self,theMode : int) -> None: ...
    def Redisplay(self,AllModes : bool=False) -> None: 
        """
        Updates the active presentation; if <AllModes> = Standard_True all the presentations inside are recomputed. IMPORTANT: It is preferable to call Redisplay method of corresponding AIS_InteractiveContext instance for cases when it is accessible. This method just redirects call to myCTXPtr, so this class field must be up to date for proper result.
        """
    def RemoveBuilder(self,Index : int) -> None: 
        """
        Removes builder from sequence. If it is hilighter, hilighter will be NULL ( Don't remember to set it to other after!!! )
        """
    def RemoveBuilderById(self,Id : int) -> None: 
        """
        Removes builder with identificator Id
        """
    def RemoveChild(self,theObject : OCP.PrsMgr.PrsMgr_PresentableObject) -> None: 
        """
        Removes theObject from children of current object in scene hierarchy.
        """
    def RemoveChildWithRestoreTransformation(self,theObject : OCP.PrsMgr.PrsMgr_PresentableObject) -> None: 
        """
        Removes theObject from children of current object in scene hierarchy with keeping the current global transformation. So the object keeps the same position/orientation in the global CS.
        """
    def RemoveClipPlane(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> None: 
        """
        Removes previously added clip plane.
        """
    def ResetTransformation(self) -> None: 
        """
        None
        """
    def Selection(self,theMode : int) -> OCP.SelectMgr.SelectMgr_Selection: 
        """
        Returns the selection having specified selection mode or NULL.
        """
    def Selections(self) -> OCP.SelectMgr.SelectMgr_SequenceOfSelection: 
        """
        Return the sequence of selections.
        """
    def SetAspect(self,anAspect : OCP.Prs3d.Prs3d_BasicAspect) -> None: 
        """
        Sets the graphic basic aspect to the current presentation.
        """
    def SetAssemblyOwner(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theMode : int=-1) -> None: 
        """
        Sets common entity owner for assembly sensitive object entities
        """
    def SetAttributes(self,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Initializes the drawing tool theDrawer.
        """
    def SetAutoHilight(self,theAutoHilight : bool) -> None: 
        """
        Set AutoHilight property to true or false.
        """
    def SetClipPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Set clip planes for graphical clipping for all display mode presentations. The composition of clip planes truncates the rendering space to convex volume. Please be aware that number of supported clip plane is limited. The planes which exceed the limit are ignored. Besides of this, some planes can be already set in view where the object is shown: the number of these planes should be subtracted from limit to predict the maximum possible number of object clipping planes.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Only the interactive object knowns which Drawer attribute is affected by the color, if any (ex: for a wire,it's the wireaspect field of the drawer, but for a vertex, only the point aspect field is affected by the color). WARNING : Do not forget to set the corresponding fields here (hasOwnColor and myDrawer->SetColor())
        """
    def SetContext(self,aCtx : OCP.AIS.AIS_InteractiveContext) -> None: 
        """
        Sets the interactive context aCtx and provides a link to the default drawing tool or "Drawer" if there is none.
        """
    def SetCurrentFacingModel(self,theModel : OCP.Aspect.Aspect_TypeOfFacingModel=Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None: 
        """
        change the current facing model apply on polygons for SetColor(), SetTransparency(), SetMaterial() methods default facing model is Aspect_TOFM_TWO_SIDE. This mean that attributes is applying both on the front and back face.
        """
    def SetDataSource(self,aDataSource : MeshVS_DataSource) -> None: 
        """
        Sets default builders' data source
        """
    def SetDisplayMode(self,theMode : int) -> None: 
        """
        Sets the display mode for the interactive object. An object can have its own temporary display mode, which is different from that proposed by the interactive context.
        """
    def SetDrawer(self,aDrawer : MeshVS_Drawer) -> None: 
        """
        Sets default builders' drawer
        """
    def SetDynamicHilightAttributes(self,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Initializes the dynamic hilight drawing tool.
        """
    def SetHiddenElems(self,Ids : OCP.TColStd.TColStd_HPackedMapOfInteger) -> None: 
        """
        Sets map of hidden elements
        """
    def SetHiddenNodes(self,Ids : OCP.TColStd.TColStd_HPackedMapOfInteger) -> None: 
        """
        Sets map of hidden nodes, which shall not be displayed individually. If nodes shared by some elements shall not be drawn, they should be included into that map
        """
    def SetHilightAttributes(self,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Initializes the hilight drawing tool theDrawer.
        """
    def SetHilightMode(self,theMode : int) -> None: 
        """
        Sets highlight display mode. This is obsolete method for backward compatibility - use ::HilightAttributes() and ::DynamicHilightAttributes() instead.
        """
    @overload
    def SetHilighter(self,Index : int) -> bool: 
        """
        Changes hilighter ( see above )

        Sets builder with sequence index "Index" as hilighter
        """
    @overload
    def SetHilighter(self,Builder : MeshVS_PrsBuilder) -> None: ...
    def SetHilighterById(self,Id : int) -> bool: 
        """
        Sets builder with identificator "Id" as hilighter
        """
    def SetInfiniteState(self,theFlag : bool=True) -> None: 
        """
        Sets if object should be considered as infinite.
        """
    def SetIsoOnTriangulation(self,theIsEnabled : bool) -> None: 
        """
        Enables or disables on-triangulation build of isolines according to the flag given.
        """
    @overload
    def SetLocalTransformation(self,theTrsf : OCP.gp.gp_Trsf) -> None: 
        """
        Sets local transformation to theTransformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.

        Sets local transformation to theTransformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    @overload
    def SetLocalTransformation(self,theTrsf : OCP.TopLoc.TopLoc_Datum3D) -> None: ...
    def SetMaterial(self,aName : OCP.Graphic3d.Graphic3d_MaterialAspect) -> None: 
        """
        Sets the material aMat defining this display attribute for the interactive object. Material aspect determines shading aspect, color and transparency of visible entities.
        """
    def SetMeshSelMethod(self,M : MeshVS_MeshSelectionMethod) -> None: 
        """
        Sets mesh selection method (see MeshVS.cdl)
        """
    def SetMutable(self,theIsMutable : bool) -> None: 
        """
        Sets if the object has mutable nature (content or location will be changed regularly). This method should be called before object displaying to take effect.
        """
    def SetOwner(self,theApplicativeEntity : OCP.Standard.Standard_Transient) -> None: 
        """
        Allows you to attribute the owner theApplicativeEntity to an Interactive Object. This can be a shape for a set of sub-shapes or a sub-shape for sub-shapes which it is composed of. The owner takes the form of a transient.
        """
    def SetPolygonOffsets(self,aMode : int,aFactor : float=1.0,aUnits : float=0.0) -> None: 
        """
        Sets up polygon offsets for this object.
        """
    def SetPropagateVisualState(self,theFlag : bool) -> None: 
        """
        Change the value of the flag "propagate visual state"
        """
    def SetSelectableNodes(self,Ids : OCP.TColStd.TColStd_HPackedMapOfInteger) -> None: 
        """
        Sets map of selectable nodes.
        """
    @overload
    def SetToUpdate(self) -> None: 
        """
        Flags presentation to be updated; UpdatePresentations() will recompute these presentations.

        flags all the Presentations to be Updated.
        """
    @overload
    def SetToUpdate(self,theMode : int) -> None: ...
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Sets up Transform Persistence defining a special Local Coordinate system where this object should be located. Note that management of Transform Persistence object is more expensive than of the normal one, because it requires its position being recomputed basing on camera position within each draw call / traverse.
        """
    def SetTransparency(self,aValue : float=0.6) -> None: 
        """
        Attributes a setting aValue for transparency. The transparency value should be between 0.0 and 1.0. At 0.0 an object will be totally opaque, and at 1.0, fully transparent. Warning At a value of 1.0, there may be nothing visible.
        """
    def SetTypeOfPresentation(self,theType : OCP.PrsMgr.PrsMgr_TypeOfPresentation3d) -> None: 
        """
        Set type of presentation.
        """
    def SetWidth(self,theWidth : float) -> None: 
        """
        Allows you to provide the setting aValue for width. Only the Interactive Object knows which Drawer attribute is affected by the width setting.
        """
    def SetZLayer(self,theLayerId : int) -> None: 
        """
        Set Z layer ID and update all presentations of the selectable object. The layers mechanism allows drawing objects in higher layers in overlay of objects in lower layers.
        """
    def Signature(self) -> int: 
        """
        Specifies additional characteristics of Interactive Object of Type(); -1 by default. Among the datums, this signature is attributed to the shape. The remaining datums have the following default signatures: - Point signature 1 - Axis signature 2 - Trihedron signature 3 - PlaneTrihedron signature 4 - Line signature 5 - Circle signature 6 - Plane signature 7.
        """
    def SynchronizeAspects(self) -> None: 
        """
        Synchronize presentation aspects after their modification.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def ToBeUpdated(self,ListOfMode : OCP.TColStd.TColStd_ListOfInteger) -> None: 
        """
        Returns TRUE if any active presentation has invalidation flag.

        gives the list of modes which are flagged "to be updated".
        """
    @overload
    def ToBeUpdated(self,theToIncludeHidden : bool=False) -> bool: ...
    def ToPropagateVisualState(self) -> bool: 
        """
        Get value of the flag "propagate visual state" It means that the display/erase/color visual state is propagated automatically to all children; by default, the flag is true
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Returns Transformation Persistence defining a special Local Coordinate system where this presentable object is located or NULL handle if not defined. Position of the object having Transformation Persistence is mutable and depends on camera position. The same applies to a bounding box of the object.
        """
    def Transformation(self) -> OCP.gp.gp_Trsf: 
        """
        Return the transformation taking into account transformation of parent object(s). Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def TransformationGeom(self) -> OCP.TopLoc.TopLoc_Datum3D: 
        """
        Return the transformation taking into account transformation of parent object(s). Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def Transparency(self) -> float: 
        """
        Returns the transparency setting. This will be between 0.0 and 1.0. At 0.0 an object will be totally opaque, and at 1.0, fully transparent.
        """
    def Type(self) -> OCP.AIS.AIS_KindOfInteractive: 
        """
        Returns the kind of Interactive Object; AIS_KindOfInteractive_None by default.
        """
    def TypeOfPresentation3d(self) -> OCP.PrsMgr.PrsMgr_TypeOfPresentation3d: 
        """
        Returns information on whether the object accepts display in HLR mode or not.
        """
    def UnsetAttributes(self) -> None: 
        """
        Clears settings provided by the drawing tool aDrawer.
        """
    def UnsetColor(self) -> None: 
        """
        Removes color settings. Only the Interactive Object knows which Drawer attribute is affected by the color setting. For a wire, for example, wire aspect is the attribute affected. For a vertex, however, only point aspect is affected by the color setting.
        """
    def UnsetDisplayMode(self) -> None: 
        """
        Removes display mode settings from the interactive object.
        """
    def UnsetHilightAttributes(self) -> None: 
        """
        Clears settings provided by the hilight drawing tool theDrawer.
        """
    def UnsetHilightMode(self) -> None: 
        """
        Unsets highlight display mode.
        """
    def UnsetMaterial(self) -> None: 
        """
        Removes the setting for material.
        """
    def UnsetTransparency(self) -> None: 
        """
        Removes the transparency setting. The object is opaque by default.
        """
    def UnsetWidth(self) -> None: 
        """
        Reset width to default value.
        """
    def UpdateSelectableNodes(self) -> None: 
        """
        Automatically computes selectable nodes; the node is considered as being selectable if it is either not hidden, or is hidden but referred by at least one non-hidden element. Thus all nodes that are visible (either individually, or as ends or corners of elements) are selectable by default.
        """
    def UpdateSelection(self,theMode : int=-1) -> None: 
        """
        Sets update status FULL to selections of the object. Must be used as the only method of UpdateSelection from outer classes to prevent BVH structures from being outdated.
        """
    def UpdateTransformation(self) -> None: 
        """
        Recomputes the location of the selection aSelection.
        """
    def UpdateTransformations(self,aSelection : OCP.SelectMgr.SelectMgr_Selection) -> None: 
        """
        Updates locations in all sensitive entities from <aSelection> and in corresponding entity owners.
        """
    def ViewAffinity(self) -> OCP.Graphic3d.Graphic3d_ViewAffinity: 
        """
        Return view affinity mask.
        """
    def Width(self) -> float: 
        """
        Returns the width setting of the Interactive Object.
        """
    def ZLayer(self) -> int: 
        """
        Get ID of Z layer for main presentation.
        """
    def __init__(self,theIsAllowOverlapped : bool=False) -> None: ...
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
class MeshVS_MeshEntityOwner(OCP.SelectMgr.SelectMgr_EntityOwner, OCP.Standard.Standard_Transient):
    """
    The custom owner. This class provides methods to store owner information: 1) An address of element or node data structure 2) Type of node or element owner assigned 3) ID of node or element owner assignedThe custom owner. This class provides methods to store owner information: 1) An address of element or node data structure 2) Type of node or element owner assigned 3) ID of node or element owner assignedThe custom owner. This class provides methods to store owner information: 1) An address of element or node data structure 2) Type of node or element owner assigned 3) ID of node or element owner assigned
    """
    def Clear(self,PM : OCP.PrsMgr.PrsMgr_PresentationManager,Mode : int=0) -> None: 
        """
        None
        """
    def ComesFromDecomposition(self) -> bool: 
        """
        Returns TRUE if this owner points to a part of object and FALSE for entire object.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
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
    def HandleMouseClick(self,thePoint : OCP.Graphic3d.Graphic3d_Vec2i,theButton : int,theModifiers : int,theIsDoubleClick : bool) -> bool: 
        """
        Handle mouse button click event. Does nothing by default and returns FALSE.
        """
    def HasLocation(self) -> bool: 
        """
        Returns TRUE if selectable has transformation.
        """
    def HasSelectable(self) -> bool: 
        """
        Returns true if there is a selectable object to serve as an owner.
        """
    def HilightWithColor(self,thePM : OCP.PrsMgr.PrsMgr_PresentationManager,theStyle : OCP.Prs3d.Prs3d_Drawer,theMode : int) -> None: 
        """
        Hilights owner with the certain color
        """
    def ID(self) -> int: 
        """
        Returns ID of element or node data structure
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAutoHilight(self) -> bool: 
        """
        if owner is not auto hilighted, for group contains many such owners will be called one method HilightSelected of SelectableObject
        """
    def IsForcedHilight(self) -> bool: 
        """
        if this method returns TRUE the owner will always call method Hilight for SelectableObject when the owner is detected. By default it always return FALSE.
        """
    def IsGroup(self) -> bool: 
        """
        Returns true if owner represents group of nodes or elements
        """
    def IsHilighted(self,PM : OCP.PrsMgr.PrsMgr_PresentationManager,Mode : int=0) -> bool: 
        """
        Returns true if owner is hilighted
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
    def IsSameSelectable(self,theOther : OCP.SelectMgr.SelectMgr_SelectableObject) -> bool: 
        """
        Returns true if pointer to selectable object of this owner is equal to the given one
        """
    def IsSelected(self) -> bool: 
        """
        Returns Standard_True if the owner is selected.
        """
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Returns transformation of selectable.
        """
    def Owner(self) -> capsule: 
        """
        Returns an address of element or node data structure
        """
    def Priority(self) -> int: 
        """
        Return selection priority (within range [0-9]) for results with the same depth; 0 by default. Example - selection of shapes: the owners are selectable objects (presentations) a user can give vertex priority [3], edges [2] faces [1] shape [0], so that if during selection one vertex one edge and one face are simultaneously detected, the vertex will only be hilighted.
        """
    def Selectable(self) -> OCP.SelectMgr.SelectMgr_SelectableObject: 
        """
        Returns a selectable object detected in the working context.
        """
    @overload
    def Set(self,theSelObj : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: 
        """
        Sets the selectable object.

        sets the selectable priority of the owner
        """
    @overload
    def Set(self,thePriority : int) -> None: ...
    def SetComesFromDecomposition(self,theIsFromDecomposition : bool) -> None: 
        """
        Sets flag indicating this owner points to a part of object (TRUE) or to entire object (FALSE).
        """
    def SetLocation(self,theLocation : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Change owner location (callback for handling change of location of selectable object).
        """
    def SetPriority(self,thePriority : int) -> None: 
        """
        Sets the selectable priority of the owner within range [0-9].
        """
    def SetSelectable(self,theSelObj : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: 
        """
        Sets the selectable object.
        """
    def SetSelected(self,theIsSelected : bool) -> None: 
        """
        Set the state of the owner.
        """
    def SetZLayer(self,theLayerId : int) -> None: 
        """
        Set Z layer ID and update all presentations.
        """
    @overload
    def State(self) -> int: 
        """
        Returns selection state.

        Set the state of the owner. The method is deprecated. Use SetSelected() instead.
        """
    @overload
    def State(self,theStatus : int) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> MeshVS_EntityType: 
        """
        Returns type of element or node data structure
        """
    def Unhilight(self,PM : OCP.PrsMgr.PrsMgr_PresentationManager,Mode : int=0) -> None: 
        """
        Strip hilight of owner
        """
    def UpdateHighlightTrsf(self,theViewer : OCP.V3d.V3d_Viewer,theManager : OCP.PrsMgr.PrsMgr_PresentationManager,theDispMode : int) -> None: 
        """
        Implements immediate application of location transformation of parent object to dynamic highlight structure
        """
    def __init__(self,SelObj : OCP.SelectMgr.SelectMgr_SelectableObject,ID : int,MeshEntity : capsule,Type : MeshVS_EntityType,Priority : int=0,IsGroup : bool=False) -> None: ...
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
class MeshVS_MeshOwner(OCP.SelectMgr.SelectMgr_EntityOwner, OCP.Standard.Standard_Transient):
    """
    The custom mesh owner used for advanced mesh selection. This class provides methods to store information: 1) IDs of hilighted mesh nodes and elements 2) IDs of mesh nodes and elements selected on the meshThe custom mesh owner used for advanced mesh selection. This class provides methods to store information: 1) IDs of hilighted mesh nodes and elements 2) IDs of mesh nodes and elements selected on the meshThe custom mesh owner used for advanced mesh selection. This class provides methods to store information: 1) IDs of hilighted mesh nodes and elements 2) IDs of mesh nodes and elements selected on the mesh
    """
    def AddSelectedEntities(self,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elems : OCP.TColStd.TColStd_HPackedMapOfInteger) -> None: 
        """
        Saves ids of selected mesh entities
        """
    def Clear(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,theMode : int=0) -> None: 
        """
        Clears the owners matching the value of the selection mode aMode from the presentation manager object aPM.
        """
    def ClearSelectedEntities(self) -> None: 
        """
        Clears ids of selected mesh entities
        """
    def ComesFromDecomposition(self) -> bool: 
        """
        Returns TRUE if this owner points to a part of object and FALSE for entire object.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetDataSource(self) -> MeshVS_DataSource: 
        """
        None
        """
    def GetDetectedElements(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Returns ids of hilighted mesh elements
        """
    def GetDetectedNodes(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Returns ids of hilighted mesh nodes
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectedElements(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Returns ids of selected mesh elements
        """
    def GetSelectedNodes(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Returns ids of selected mesh nodes
        """
    def HandleMouseClick(self,thePoint : OCP.Graphic3d.Graphic3d_Vec2i,theButton : int,theModifiers : int,theIsDoubleClick : bool) -> bool: 
        """
        Handle mouse button click event. Does nothing by default and returns FALSE.
        """
    def HasLocation(self) -> bool: 
        """
        Returns TRUE if selectable has transformation.
        """
    def HasSelectable(self) -> bool: 
        """
        Returns true if there is a selectable object to serve as an owner.
        """
    def HilightWithColor(self,thePM : OCP.PrsMgr.PrsMgr_PresentationManager,theColor : OCP.Prs3d.Prs3d_Drawer,theMode : int) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAutoHilight(self) -> bool: 
        """
        if owner is not auto hilighted, for group contains many such owners will be called one method HilightSelected of SelectableObject
        """
    def IsForcedHilight(self) -> bool: 
        """
        None
        """
    def IsHilighted(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,theMode : int=0) -> bool: 
        """
        Returns true if the presentation manager highlights selections corresponding to the selection mode.
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
    def IsSameSelectable(self,theOther : OCP.SelectMgr.SelectMgr_SelectableObject) -> bool: 
        """
        Returns true if pointer to selectable object of this owner is equal to the given one
        """
    def IsSelected(self) -> bool: 
        """
        Returns Standard_True if the owner is selected.
        """
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Returns transformation of selectable.
        """
    def Priority(self) -> int: 
        """
        Return selection priority (within range [0-9]) for results with the same depth; 0 by default. Example - selection of shapes: the owners are selectable objects (presentations) a user can give vertex priority [3], edges [2] faces [1] shape [0], so that if during selection one vertex one edge and one face are simultaneously detected, the vertex will only be hilighted.
        """
    def Selectable(self) -> OCP.SelectMgr.SelectMgr_SelectableObject: 
        """
        Returns a selectable object detected in the working context.
        """
    @overload
    def Set(self,theSelObj : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: 
        """
        Sets the selectable object.

        sets the selectable priority of the owner
        """
    @overload
    def Set(self,thePriority : int) -> None: ...
    def SetComesFromDecomposition(self,theIsFromDecomposition : bool) -> None: 
        """
        Sets flag indicating this owner points to a part of object (TRUE) or to entire object (FALSE).
        """
    def SetDetectedEntities(self,Nodes : OCP.TColStd.TColStd_HPackedMapOfInteger,Elems : OCP.TColStd.TColStd_HPackedMapOfInteger) -> None: 
        """
        Saves ids of hilighted mesh entities
        """
    def SetLocation(self,theLocation : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Change owner location (callback for handling change of location of selectable object).
        """
    def SetPriority(self,thePriority : int) -> None: 
        """
        Sets the selectable priority of the owner within range [0-9].
        """
    def SetSelectable(self,theSelObj : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: 
        """
        Sets the selectable object.
        """
    def SetSelected(self,theIsSelected : bool) -> None: 
        """
        Set the state of the owner.
        """
    def SetZLayer(self,theLayerId : int) -> None: 
        """
        Set Z layer ID and update all presentations.
        """
    @overload
    def State(self) -> int: 
        """
        Returns selection state.

        Set the state of the owner. The method is deprecated. Use SetSelected() instead.
        """
    @overload
    def State(self,theStatus : int) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unhilight(self,PM : OCP.PrsMgr.PrsMgr_PresentationManager,Mode : int=0) -> None: 
        """
        None
        """
    def UpdateHighlightTrsf(self,theViewer : OCP.V3d.V3d_Viewer,theManager : OCP.PrsMgr.PrsMgr_PresentationManager,theDispMode : int) -> None: 
        """
        Implements immediate application of location transformation of parent object to dynamic highlight structure
        """
    def __init__(self,theSelObj : OCP.SelectMgr.SelectMgr_SelectableObject,theDS : MeshVS_DataSource,thePriority : int=0) -> None: ...
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
class MeshVS_MeshPrsBuilder(MeshVS_PrsBuilder, OCP.Standard.Standard_Transient):
    """
    This class provides methods to compute base mesh presentationThis class provides methods to compute base mesh presentation
    """
    @staticmethod
    def AddVolumePrs_s(Topo : MeshVS_HArray1OfSequenceOfInteger,Nodes : OCP.TColStd.TColStd_Array1OfReal,NbNodes : int,Array : OCP.Graphic3d.Graphic3d_ArrayOfPrimitives,IsReflected : bool,IsShrinked : bool,IsSelect : bool,ShrinkCoef : float) -> None: 
        """
        Add to array polygons or polylines representing volume
        """
    def Build(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,IsElement : bool,DisplayMode : int) -> None: 
        """
        Builds base mesh presentation by calling the methods below
        """
    def BuildElements(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,DisplayMode : int) -> None: 
        """
        Builds elements presentation
        """
    def BuildHilightPrs(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IsElement : bool) -> None: 
        """
        Builds presentation of hilighted entity
        """
    def BuildNodes(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,DisplayMode : int) -> None: 
        """
        Builds nodes presentation
        """
    def CustomBuild(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,DisplayMode : int) -> None: 
        """
        This method is called to build presentation of custom elements (they have MeshVS_ET_0D type). IDs is set of numeric identificators of elements for custom building. IDsToExclude is set of IDs to exclude from processing. If some entity has been excluded, it is not processed by other builders. DisplayMode is numeric constant describing display mode (see MeshVS_DisplayModeFlags.hxx)
        """
    def CustomSensitiveEntity(self,Owner : OCP.SelectMgr.SelectMgr_EntityOwner,SelectMode : int) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        This method is called to build sensitive of custom elements ( they have MeshVS_ET_0D type )
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
    def GetDataSource(self) -> MeshVS_DataSource: 
        """
        Returns custom data source or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetDrawer(self) -> MeshVS_Drawer: 
        """
        Returns custom drawer or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetFlags(self) -> int: 
        """
        Returns flags, assigned with builder during creation
        """
    def GetId(self) -> int: 
        """
        Returns builder ID
        """
    def GetPresentationManager(self) -> OCP.PrsMgr.PrsMgr_PresentationManager: 
        """
        Get presentation manager of builder
        """
    def GetPriority(self) -> int: 
        """
        Returns priority; as priority bigger, as soon builder will be called.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def HowManyPrimitives_s(Topo : MeshVS_HArray1OfSequenceOfInteger,AsPolygons : bool,IsSelect : bool,NbNodes : int) -> Tuple[int, int]: 
        """
        Calculate how many polygons or polylines are necessary to draw passed topology
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsExcludingOn(self) -> bool: 
        """
        Read excluding state
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
    def SetDataSource(self,newDS : MeshVS_DataSource) -> None: 
        """
        Change custom data source
        """
    def SetDrawer(self,newDr : MeshVS_Drawer) -> None: 
        """
        Change custom drawer
        """
    def SetExcluding(self,state : bool) -> None: 
        """
        Set excluding state. If it is Standard_True, the nodes or elements, processed by current builder will be noted and next builder won't process its.
        """
    def SetPresentationManager(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> None: 
        """
        Set presentation manager for builder
        """
    def TestFlags(self,DisplayMode : int) -> bool: 
        """
        Test whether display mode has flags assigned with this builder. This method has default implementation and can be redefined for advance behavior Returns Standard_True only if display mode is appropriate for this builder
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Parent : MeshVS_Mesh,Flags : int=3,DS : MeshVS_DataSource=None,Id : int=-1,Priority : int=5) -> None: ...
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
class MeshVS_MeshSelectionMethod():
    """
    this enumeration describe what type of sensitive entity will be built in 0-th selection mode (it means that whole mesh is selected )

    Members:

      MeshVS_MSM_PRECISE

      MeshVS_MSM_NODES

      MeshVS_MSM_BOX
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
    MeshVS_MSM_BOX: OCP.MeshVS.MeshVS_MeshSelectionMethod # value = <MeshVS_MeshSelectionMethod.MeshVS_MSM_BOX: 2>
    MeshVS_MSM_NODES: OCP.MeshVS.MeshVS_MeshSelectionMethod # value = <MeshVS_MeshSelectionMethod.MeshVS_MSM_NODES: 1>
    MeshVS_MSM_PRECISE: OCP.MeshVS.MeshVS_MeshSelectionMethod # value = <MeshVS_MeshSelectionMethod.MeshVS_MSM_PRECISE: 0>
    __entries: dict # value = {'MeshVS_MSM_PRECISE': (<MeshVS_MeshSelectionMethod.MeshVS_MSM_PRECISE: 0>, None), 'MeshVS_MSM_NODES': (<MeshVS_MeshSelectionMethod.MeshVS_MSM_NODES: 1>, None), 'MeshVS_MSM_BOX': (<MeshVS_MeshSelectionMethod.MeshVS_MSM_BOX: 2>, None)}
    __members__: dict # value = {'MeshVS_MSM_PRECISE': <MeshVS_MeshSelectionMethod.MeshVS_MSM_PRECISE: 0>, 'MeshVS_MSM_NODES': <MeshVS_MeshSelectionMethod.MeshVS_MSM_NODES: 1>, 'MeshVS_MSM_BOX': <MeshVS_MeshSelectionMethod.MeshVS_MSM_BOX: 2>}
    pass
class MeshVS_NodalColorPrsBuilder(MeshVS_PrsBuilder, OCP.Standard.Standard_Transient):
    """
    This class provides methods to create presentation of nodes with assigned color. There are two ways of presentation building 1. Without using texture. In this case colors of nodes are specified with DataMapOfIntegerColor and presentation is built with gradient fill between these nodes (default behaviour) 2. Using texture. In this case presentation is built with spectrum filling between nodes. For example, if one node has blue color and second one has violet color, parameters of this class may be set to fill presentation between nodes with solar spectrum. Methods: UseTexture - activates/deactivates this way SetColorMap - sets colors used for generation of texture SetColorindices - specifies correspondence between node IDs and indices of colors from color mapThis class provides methods to create presentation of nodes with assigned color. There are two ways of presentation building 1. Without using texture. In this case colors of nodes are specified with DataMapOfIntegerColor and presentation is built with gradient fill between these nodes (default behaviour) 2. Using texture. In this case presentation is built with spectrum filling between nodes. For example, if one node has blue color and second one has violet color, parameters of this class may be set to fill presentation between nodes with solar spectrum. Methods: UseTexture - activates/deactivates this way SetColorMap - sets colors used for generation of texture SetColorindices - specifies correspondence between node IDs and indices of colors from color map
    """
    def AddVolumePrs(self,theTopo : MeshVS_HArray1OfSequenceOfInteger,theNodes : OCP.TColStd.TColStd_Array1OfInteger,theCoords : OCP.TColStd.TColStd_Array1OfReal,theArray : OCP.Graphic3d.Graphic3d_ArrayOfPrimitives,theIsShaded : bool,theNbColors : int,theNbTexColors : int,theColorRatio : float) -> None: 
        """
        Add to array polygons or polylines representing volume
        """
    def Build(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,IsElement : bool,DisplayMode : int) -> None: 
        """
        Builds presentation of nodes with assigned color.
        """
    def CustomBuild(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,DisplayMode : int) -> None: 
        """
        This method is called to build presentation of custom elements (they have MeshVS_ET_0D type). IDs is set of numeric identificators of elements for custom building. IDsToExclude is set of IDs to exclude from processing. If some entity has been excluded, it is not processed by other builders. DisplayMode is numeric constant describing display mode (see MeshVS_DisplayModeFlags.hxx)
        """
    def CustomSensitiveEntity(self,Owner : OCP.SelectMgr.SelectMgr_EntityOwner,SelectMode : int) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        This method is called to build sensitive of custom elements ( they have MeshVS_ET_0D type )
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
    def GetColor(self,ID : int,theColor : OCP.Quantity.Quantity_Color) -> bool: 
        """
        Returns color assigned to single node
        """
    def GetColorMap(self) -> OCP.Aspect.Aspect_SequenceOfColor: 
        """
        Return colors used for texrture presentation
        """
    def GetColors(self) -> MeshVS_DataMapOfIntegerColor: 
        """
        Returns map of colors assigned to nodes.
        """
    def GetDataSource(self) -> MeshVS_DataSource: 
        """
        Returns custom data source or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetDrawer(self) -> MeshVS_Drawer: 
        """
        Returns custom drawer or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetFlags(self) -> int: 
        """
        Returns flags, assigned with builder during creation
        """
    def GetId(self) -> int: 
        """
        Returns builder ID
        """
    def GetInvalidColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return color representing invalid texture coordinate (laying outside range [0, 1])
        """
    def GetPresentationManager(self) -> OCP.PrsMgr.PrsMgr_PresentationManager: 
        """
        Get presentation manager of builder
        """
    def GetPriority(self) -> int: 
        """
        Returns priority; as priority bigger, as soon builder will be called.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTextureCoord(self,theID : int) -> float: 
        """
        Return correspondence between node IDs and texture coordinate (range [0, 1])
        """
    def GetTextureCoords(self) -> OCP.TColStd.TColStd_DataMapOfIntegerReal: 
        """
        Get correspondence between node IDs and texture coordinates (range [0, 1])
        """
    def HasColors(self) -> bool: 
        """
        Returns true, if map isn't empty
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsExcludingOn(self) -> bool: 
        """
        Read excluding state
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
    def IsUseTexture(self) -> bool: 
        """
        Verify whether texture is used to build presentation
        """
    def SetColor(self,ID : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Sets color assigned to single node
        """
    def SetColorMap(self,theColors : OCP.Aspect.Aspect_SequenceOfColor) -> None: 
        """
        Set colors to be used for texrture presentation theColors - colors for valid coordinates (laying in range [0, 1])
        """
    def SetColors(self,Map : MeshVS_DataMapOfIntegerColor) -> None: 
        """
        Sets map of colors assigned to nodes.
        """
    def SetDataSource(self,newDS : MeshVS_DataSource) -> None: 
        """
        Change custom data source
        """
    def SetDrawer(self,newDr : MeshVS_Drawer) -> None: 
        """
        Change custom drawer
        """
    def SetExcluding(self,state : bool) -> None: 
        """
        Set excluding state. If it is Standard_True, the nodes or elements, processed by current builder will be noted and next builder won't process its.
        """
    def SetInvalidColor(self,theInvalidColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Set color representing invalid texture coordinate (laying outside range [0, 1])
        """
    def SetPresentationManager(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> None: 
        """
        Set presentation manager for builder
        """
    def SetTextureCoord(self,theID : int,theCoord : float) -> None: 
        """
        Specify correspondence between node ID and texture coordinate (range [0, 1])
        """
    def SetTextureCoords(self,theMap : OCP.TColStd.TColStd_DataMapOfIntegerReal) -> None: 
        """
        Specify correspondence between node IDs and texture coordinates (range [0, 1])
        """
    def TestFlags(self,DisplayMode : int) -> bool: 
        """
        Test whether display mode has flags assigned with this builder. This method has default implementation and can be redefined for advance behavior Returns Standard_True only if display mode is appropriate for this builder
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UseTexture(self,theToUse : bool) -> None: 
        """
        Specify whether texture must be used to build presentation
        """
    def __init__(self,Parent : MeshVS_Mesh,Flags : int=8,DS : MeshVS_DataSource=None,Id : int=-1,Priority : int=10) -> None: ...
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
class MeshVS_PolyhedronVerts(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TColgp.TColgp_HArray1OfPnt,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.TColgp.TColgp_HArray1OfPnt) -> OCP.TColgp.TColgp_HArray1OfPnt: ...
    @overload
    def Append(self,theOther : MeshVS_PolyhedronVerts) -> None: ...
    def Assign(self,theOther : MeshVS_PolyhedronVerts) -> MeshVS_PolyhedronVerts: 
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
    def First(self) -> OCP.TColgp.TColgp_HArray1OfPnt: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : MeshVS_PolyhedronVerts,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OCP.TColgp.TColgp_HArray1OfPnt,theIter : Any) -> OCP.TColgp.TColgp_HArray1OfPnt: ...
    @overload
    def InsertBefore(self,theItem : OCP.TColgp.TColgp_HArray1OfPnt,theIter : Any) -> OCP.TColgp.TColgp_HArray1OfPnt: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : MeshVS_PolyhedronVerts,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.TColgp.TColgp_HArray1OfPnt: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.TColgp.TColgp_HArray1OfPnt) -> OCP.TColgp.TColgp_HArray1OfPnt: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : MeshVS_PolyhedronVerts) -> None: ...
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
    def __init__(self,theOther : MeshVS_PolyhedronVerts) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class MeshVS_ElementalColorPrsBuilder(MeshVS_PrsBuilder, OCP.Standard.Standard_Transient):
    """
    This class provides methods to create presentation of elements with assigned colors. The class contains two color maps: map of same colors for front and back side of face and map of different ones,This class provides methods to create presentation of elements with assigned colors. The class contains two color maps: map of same colors for front and back side of face and map of different ones,This class provides methods to create presentation of elements with assigned colors. The class contains two color maps: map of same colors for front and back side of face and map of different ones,
    """
    def Build(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,IsElement : bool,DisplayMode : int) -> None: 
        """
        Builds presentation of elements with assigned colors.
        """
    def CustomBuild(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,DisplayMode : int) -> None: 
        """
        This method is called to build presentation of custom elements (they have MeshVS_ET_0D type). IDs is set of numeric identificators of elements for custom building. IDsToExclude is set of IDs to exclude from processing. If some entity has been excluded, it is not processed by other builders. DisplayMode is numeric constant describing display mode (see MeshVS_DisplayModeFlags.hxx)
        """
    def CustomSensitiveEntity(self,Owner : OCP.SelectMgr.SelectMgr_EntityOwner,SelectMode : int) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        This method is called to build sensitive of custom elements ( they have MeshVS_ET_0D type )
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
    def GetColor1(self,ID : int,theColor : OCP.Quantity.Quantity_Color) -> bool: 
        """
        Returns color assigned with element number ID
        """
    @overload
    def GetColor2(self,ID : int,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color) -> bool: 
        """
        Returns colors assigned with element number ID

        Returns colors assigned with element number ID theColor1 is the front element color theColor2 is the back element color
        """
    @overload
    def GetColor2(self,ID : int,theColor : MeshVS_TwoColors) -> bool: ...
    def GetColors1(self) -> MeshVS_DataMapOfIntegerColor: 
        """
        Returns map of colors same for front and back side of face.
        """
    def GetColors2(self) -> MeshVS_DataMapOfIntegerTwoColors: 
        """
        Returns map of different colors for front and back side of face
        """
    def GetDataSource(self) -> MeshVS_DataSource: 
        """
        Returns custom data source or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetDrawer(self) -> MeshVS_Drawer: 
        """
        Returns custom drawer or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetFlags(self) -> int: 
        """
        Returns flags, assigned with builder during creation
        """
    def GetId(self) -> int: 
        """
        Returns builder ID
        """
    def GetPresentationManager(self) -> OCP.PrsMgr.PrsMgr_PresentationManager: 
        """
        Get presentation manager of builder
        """
    def GetPriority(self) -> int: 
        """
        Returns priority; as priority bigger, as soon builder will be called.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasColors1(self) -> bool: 
        """
        Returns true, if map of colors isn't empty
        """
    def HasColors2(self) -> bool: 
        """
        Returns true, if map isn't empty
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsExcludingOn(self) -> bool: 
        """
        Read excluding state
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
    def SetColor1(self,ID : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Sets color assigned with element number ID
        """
    @overload
    def SetColor2(self,ID : int,theTwoColors : MeshVS_TwoColors) -> None: 
        """
        Sets colors assigned with element number ID

        Sets color assigned with element number ID theColor1 is the front element color theColor2 is the back element color
        """
    @overload
    def SetColor2(self,ID : int,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color) -> None: ...
    def SetColors1(self,Map : MeshVS_DataMapOfIntegerColor) -> None: 
        """
        Sets map of colors same for front and back side of face.
        """
    def SetColors2(self,Map : MeshVS_DataMapOfIntegerTwoColors) -> None: 
        """
        Sets map of different colors for front and back side of face
        """
    def SetDataSource(self,newDS : MeshVS_DataSource) -> None: 
        """
        Change custom data source
        """
    def SetDrawer(self,newDr : MeshVS_Drawer) -> None: 
        """
        Change custom drawer
        """
    def SetExcluding(self,state : bool) -> None: 
        """
        Set excluding state. If it is Standard_True, the nodes or elements, processed by current builder will be noted and next builder won't process its.
        """
    def SetPresentationManager(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> None: 
        """
        Set presentation manager for builder
        """
    def TestFlags(self,DisplayMode : int) -> bool: 
        """
        Test whether display mode has flags assigned with this builder. This method has default implementation and can be redefined for advance behavior Returns Standard_True only if display mode is appropriate for this builder
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Parent : MeshVS_Mesh,Flags : int=16,DS : MeshVS_DataSource=None,Id : int=-1,Priority : int=15) -> None: ...
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
class MeshVS_SelectionModeFlags():
    """
    None

    Members:

      MeshVS_SMF_Mesh

      MeshVS_SMF_Node

      MeshVS_SMF_0D

      MeshVS_SMF_Link

      MeshVS_SMF_Face

      MeshVS_SMF_Volume

      MeshVS_SMF_Element

      MeshVS_SMF_All

      MeshVS_SMF_Group
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
    MeshVS_SMF_0D: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_0D: 2>
    MeshVS_SMF_All: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_All: 31>
    MeshVS_SMF_Element: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Element: 30>
    MeshVS_SMF_Face: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Face: 8>
    MeshVS_SMF_Group: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Group: 256>
    MeshVS_SMF_Link: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Link: 4>
    MeshVS_SMF_Mesh: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Mesh: 0>
    MeshVS_SMF_Node: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Node: 1>
    MeshVS_SMF_Volume: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Volume: 16>
    __entries: dict # value = {'MeshVS_SMF_Mesh': (<MeshVS_SelectionModeFlags.MeshVS_SMF_Mesh: 0>, None), 'MeshVS_SMF_Node': (<MeshVS_SelectionModeFlags.MeshVS_SMF_Node: 1>, None), 'MeshVS_SMF_0D': (<MeshVS_SelectionModeFlags.MeshVS_SMF_0D: 2>, None), 'MeshVS_SMF_Link': (<MeshVS_SelectionModeFlags.MeshVS_SMF_Link: 4>, None), 'MeshVS_SMF_Face': (<MeshVS_SelectionModeFlags.MeshVS_SMF_Face: 8>, None), 'MeshVS_SMF_Volume': (<MeshVS_SelectionModeFlags.MeshVS_SMF_Volume: 16>, None), 'MeshVS_SMF_Element': (<MeshVS_SelectionModeFlags.MeshVS_SMF_Element: 30>, None), 'MeshVS_SMF_All': (<MeshVS_SelectionModeFlags.MeshVS_SMF_All: 31>, None), 'MeshVS_SMF_Group': (<MeshVS_SelectionModeFlags.MeshVS_SMF_Group: 256>, None)}
    __members__: dict # value = {'MeshVS_SMF_Mesh': <MeshVS_SelectionModeFlags.MeshVS_SMF_Mesh: 0>, 'MeshVS_SMF_Node': <MeshVS_SelectionModeFlags.MeshVS_SMF_Node: 1>, 'MeshVS_SMF_0D': <MeshVS_SelectionModeFlags.MeshVS_SMF_0D: 2>, 'MeshVS_SMF_Link': <MeshVS_SelectionModeFlags.MeshVS_SMF_Link: 4>, 'MeshVS_SMF_Face': <MeshVS_SelectionModeFlags.MeshVS_SMF_Face: 8>, 'MeshVS_SMF_Volume': <MeshVS_SelectionModeFlags.MeshVS_SMF_Volume: 16>, 'MeshVS_SMF_Element': <MeshVS_SelectionModeFlags.MeshVS_SMF_Element: 30>, 'MeshVS_SMF_All': <MeshVS_SelectionModeFlags.MeshVS_SMF_All: 31>, 'MeshVS_SMF_Group': <MeshVS_SelectionModeFlags.MeshVS_SMF_Group: 256>}
    pass
class MeshVS_SensitiveFace(OCP.Select3D.Select3D_SensitiveFace, OCP.Select3D.Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    This class provides custom sensitive face, which will be selected if it center is in rectangle.This class provides custom sensitive face, which will be selected if it center is in rectangle.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for the face
        """
    def BoundingBox(self) -> Any: 
        """
        Returns bounding box of the face. If location transformation is set, it will be applied
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the face. If location transformation is set, it will be applied
        """
    def Clear(self) -> None: 
        """
        Clears up all resources and memory
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        None
        """
    def GetPoints(self,theHArrayOfPnt : OCP.TColgp.TColgp_HArray1OfPnt) -> Any: 
        """
        Initializes the given array theHArrayOfPnt by 3d coordinates of vertices of the face
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasInitLocation(self) -> bool: 
        """
        Returns true if the shape corresponding to the entity has init location
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvInitLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns inversed location transformation matrix if the shape corresponding to this entity has init location set. Otherwise, returns identity matrix.
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
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks whether the face overlaps current selecting volume
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of sub-entities (points or planar convex polygons)
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToBuildBVH(self) -> bool: 
        """
        Returns TRUE if BVH tree is in invalidated state
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    def __init__(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,thePoints : OCP.TColgp.TColgp_Array1OfPnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity=Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR) -> None: ...
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
class MeshVS_SensitiveMesh(OCP.Select3D.Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    This class provides custom mesh sensitive entity used in advanced mesh selection.This class provides custom mesh sensitive entity used in advanced mesh selection.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a sensitive if needed
        """
    def BoundingBox(self) -> Any: 
        """
        Returns bounding box of mesh
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of mesh
        """
    def Clear(self) -> None: 
        """
        Clears up all resources and memory
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        None
        """
    def GetMode(self) -> int: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasInitLocation(self) -> bool: 
        """
        Returns true if the shape corresponding to the entity has init location
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvInitLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns inversed location transformation matrix if the shape corresponding to this entity has init location set. Otherwise, returns identity matrix.
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
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks whether sensitive overlaps current selecting volume.
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of mesh nodes
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToBuildBVH(self) -> bool: 
        """
        Returns TRUE if BVH tree is in invalidated state
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    def __init__(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theMode : int=0) -> None: ...
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
class MeshVS_SensitivePolyhedron(OCP.Select3D.Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    This class is used to detect selection of a polyhedron. The main principle of detection algorithm is to search for overlap with each polyhedron's face separately, treating them as planar convex polygons.This class is used to detect selection of a polyhedron. The main principle of detection algorithm is to search for overlap with each polyhedron's face separately, treating them as planar convex polygons.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a sensitive if needed
        """
    def BoundingBox(self) -> Any: 
        """
        None
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Clears up all resources and memory
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasInitLocation(self) -> bool: 
        """
        Returns true if the shape corresponding to the entity has init location
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvInitLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns inversed location transformation matrix if the shape corresponding to this entity has init location set. Otherwise, returns identity matrix.
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
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        None
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of nodes of polyhedron
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToBuildBVH(self) -> bool: 
        """
        Returns TRUE if BVH tree is in invalidated state
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    def __init__(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theNodes : OCP.TColgp.TColgp_Array1OfPnt,theTopo : MeshVS_HArray1OfSequenceOfInteger) -> None: ...
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
class MeshVS_SensitiveQuad(OCP.Select3D.Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    This class contains description of planar quadrangle and defines methods for its detection by OCCT BVH selection mechanismThis class contains description of planar quadrangle and defines methods for its detection by OCCT BVH selection mechanism
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a sensitive if needed
        """
    def BoundingBox(self) -> Any: 
        """
        Returns coordinates of the box
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the box
        """
    def Clear(self) -> None: 
        """
        Clears up all resources and memory
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        Returns a copy of this sensitive quadrangle
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasInitLocation(self) -> bool: 
        """
        Returns true if the shape corresponding to the entity has init location
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvInitLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns inversed location transformation matrix if the shape corresponding to this entity has init location set. Otherwise, returns identity matrix.
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
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks whether the box overlaps current selecting volume
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of sub-entities in sensitive
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToBuildBVH(self) -> bool: 
        """
        Returns TRUE if BVH tree is in invalidated state
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    @overload
    def __init__(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theQuadVerts : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,thePnt4 : OCP.gp.gp_Pnt) -> None: ...
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
class MeshVS_SensitiveSegment(OCP.Select3D.Select3D_SensitiveSegment, OCP.Select3D.Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    This class provides custom sensitive face, which will be selected if it center is in rectangle.This class provides custom sensitive face, which will be selected if it center is in rectangle.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a sensitive if needed
        """
    def BoundingBox(self) -> Any: 
        """
        Returns bounding box of the segment. If location transformation is set, it will be applied
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the segment. If location transformation is set, it will be applied
        """
    def Clear(self) -> None: 
        """
        Clears up all resources and memory
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def EndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        changes the end point of the segment

        gives the 3D End Point of the Segment
        """
    @overload
    def EndPoint(self,thePnt : OCP.gp.gp_Pnt) -> None: ...
    def GetConnected(self) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasInitLocation(self) -> bool: 
        """
        Returns true if the shape corresponding to the entity has init location
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvInitLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns inversed location transformation matrix if the shape corresponding to this entity has init location set. Otherwise, returns identity matrix.
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
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks whether the segment overlaps current selecting volume
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of points
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetEndPoint(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        changes the end point of the segment
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def SetStartPoint(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        changes the start Point of the Segment;
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    @overload
    def StartPoint(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        changes the start Point of the Segment;

        gives the 3D start Point of the Segment
        """
    @overload
    def StartPoint(self) -> OCP.gp.gp_Pnt: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToBuildBVH(self) -> bool: 
        """
        Returns TRUE if BVH tree is in invalidated state
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    def __init__(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theFirstPnt : OCP.gp.gp_Pnt,theLastPnt : OCP.gp.gp_Pnt) -> None: ...
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
class MeshVS_SequenceOfPrsBuilder(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : MeshVS_PrsBuilder) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : MeshVS_SequenceOfPrsBuilder) -> None: ...
    def Assign(self,theOther : MeshVS_SequenceOfPrsBuilder) -> MeshVS_SequenceOfPrsBuilder: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> MeshVS_PrsBuilder: 
        """
        First item access
        """
    def ChangeLast(self) -> MeshVS_PrsBuilder: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> MeshVS_PrsBuilder: 
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
    def First(self) -> MeshVS_PrsBuilder: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : MeshVS_SequenceOfPrsBuilder) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : MeshVS_PrsBuilder) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : MeshVS_SequenceOfPrsBuilder) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : MeshVS_PrsBuilder) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> MeshVS_PrsBuilder: 
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
    def Prepend(self,theSeq : MeshVS_SequenceOfPrsBuilder) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : MeshVS_PrsBuilder) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : MeshVS_PrsBuilder) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : MeshVS_SequenceOfPrsBuilder) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> MeshVS_PrsBuilder: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : MeshVS_SequenceOfPrsBuilder) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class MeshVS_SymmetricPairHasher():
    """
    Provides symmetric hash methods pair of integers.
    """
    @staticmethod
    def HashCode_s(theNodePair : Tuple[intint],theUpperBound : int) -> int: 
        """
        Computes a hash code for the node pair, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(thePair1 : Tuple[intint],thePair2 : Tuple[intint]) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class MeshVS_TextPrsBuilder(MeshVS_PrsBuilder, OCP.Standard.Standard_Transient):
    """
    This class provides methods to create text data presentation. It store map of texts assigned with nodes or elements.This class provides methods to create text data presentation. It store map of texts assigned with nodes or elements.
    """
    def Build(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,IsElement : bool,theDisplayMode : int) -> None: 
        """
        Builds presentation of text data
        """
    def CustomBuild(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,DisplayMode : int) -> None: 
        """
        This method is called to build presentation of custom elements (they have MeshVS_ET_0D type). IDs is set of numeric identificators of elements for custom building. IDsToExclude is set of IDs to exclude from processing. If some entity has been excluded, it is not processed by other builders. DisplayMode is numeric constant describing display mode (see MeshVS_DisplayModeFlags.hxx)
        """
    def CustomSensitiveEntity(self,Owner : OCP.SelectMgr.SelectMgr_EntityOwner,SelectMode : int) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        This method is called to build sensitive of custom elements ( they have MeshVS_ET_0D type )
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
    def GetDataSource(self) -> MeshVS_DataSource: 
        """
        Returns custom data source or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetDrawer(self) -> MeshVS_Drawer: 
        """
        Returns custom drawer or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetFlags(self) -> int: 
        """
        Returns flags, assigned with builder during creation
        """
    def GetId(self) -> int: 
        """
        Returns builder ID
        """
    def GetPresentationManager(self) -> OCP.PrsMgr.PrsMgr_PresentationManager: 
        """
        Get presentation manager of builder
        """
    def GetPriority(self) -> int: 
        """
        Returns priority; as priority bigger, as soon builder will be called.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetText(self,IsElement : bool,ID : int,Text : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Returns text assigned with single node or element
        """
    def GetTexts(self,IsElement : bool) -> MeshVS_DataMapOfIntegerAsciiString: 
        """
        Returns map of text assigned with nodes ( IsElement = False ) or elements ( IsElement = True )
        """
    def HasTexts(self,IsElement : bool) -> bool: 
        """
        Returns True if map isn't empty
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsExcludingOn(self) -> bool: 
        """
        Read excluding state
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
    def SetDataSource(self,newDS : MeshVS_DataSource) -> None: 
        """
        Change custom data source
        """
    def SetDrawer(self,newDr : MeshVS_Drawer) -> None: 
        """
        Change custom drawer
        """
    def SetExcluding(self,state : bool) -> None: 
        """
        Set excluding state. If it is Standard_True, the nodes or elements, processed by current builder will be noted and next builder won't process its.
        """
    def SetPresentationManager(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> None: 
        """
        Set presentation manager for builder
        """
    def SetText(self,IsElement : bool,ID : int,Text : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets text assigned with single node or element
        """
    def SetTexts(self,IsElement : bool,Map : MeshVS_DataMapOfIntegerAsciiString) -> None: 
        """
        Sets map of text assigned with nodes or elements
        """
    def TestFlags(self,DisplayMode : int) -> bool: 
        """
        Test whether display mode has flags assigned with this builder. This method has default implementation and can be redefined for advance behavior Returns Standard_True only if display mode is appropriate for this builder
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Parent : MeshVS_Mesh,Height : float,Color : OCP.Quantity.Quantity_Color,Flags : int=32,DS : MeshVS_DataSource=None,Id : int=-1,Priority : int=20) -> None: ...
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
class MeshVS_Tool():
    """
    This class provides auxiliary methods to create different aspects
    """
    @staticmethod
    @overload
    def CreateAspectFillArea3d_s(theDr : MeshVS_Drawer,Mat : OCP.Graphic3d.Graphic3d_MaterialAspect,UseDefaults : bool=True) -> OCP.Graphic3d.Graphic3d_AspectFillArea3d: 
        """
        Creates fill area aspect with values from Drawer according to keys from DrawerAttribute

        Creates fill aspect with values from Drawer according to keys from DrawerAttribute and specific material aspect
        """
    @staticmethod
    @overload
    def CreateAspectFillArea3d_s(theDr : MeshVS_Drawer,UseDefaults : bool=True) -> OCP.Graphic3d.Graphic3d_AspectFillArea3d: ...
    @staticmethod
    def CreateAspectLine3d_s(theDr : MeshVS_Drawer,UseDefaults : bool=True) -> OCP.Graphic3d.Graphic3d_AspectLine3d: 
        """
        Creates line aspect with values from Drawer according to keys from DrawerAttribute
        """
    @staticmethod
    def CreateAspectMarker3d_s(theDr : MeshVS_Drawer,UseDefaults : bool=True) -> OCP.Graphic3d.Graphic3d_AspectMarker3d: 
        """
        Creates marker aspect with values from Drawer according to keys from DrawerAttribute
        """
    @staticmethod
    def CreateAspectText3d_s(theDr : MeshVS_Drawer,UseDefaults : bool=True) -> OCP.Graphic3d.Graphic3d_AspectText3d: 
        """
        Creates text aspect with values from Drawer according to keys from DrawerAttribute
        """
    @staticmethod
    def GetAverageNormal_s(Nodes : OCP.TColStd.TColStd_Array1OfReal,Norm : OCP.gp.gp_Vec) -> bool: 
        """
        Get an average of normals to non-planar polygon described by these points or compute normal of planar polygon. If the polygon isn't planar, function returns false
        """
    @staticmethod
    def GetNormal_s(Nodes : OCP.TColStd.TColStd_Array1OfReal,Norm : OCP.gp.gp_Vec) -> bool: 
        """
        Get one of normals to polygon described by these points. If the polygon isn't planar, function returns false
        """
    def __init__(self) -> None: ...
    pass
class MeshVS_TwoColors():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class MeshVS_TwoColorsHasher():
    """
    Purpose: The DefaultHasher is a Hasher that is used by default in NCollection maps. To compute the hash code of the key is used the global function HashCode. To compare two keys is used the global function IsEqual.
    """
    @staticmethod
    def HashCode_s(theKey : MeshVS_TwoColors,theUpperBound : int) -> int: 
        """
        Returns hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theKey1 : MeshVS_TwoColors,theKey2 : MeshVS_TwoColors) -> bool: 
        """
        None
        """
    pass
class MeshVS_TwoNodes():
    """
    Structure containing two IDs (of nodes) for using as a key in a map (as representation of a mesh link)
    """
    def __init__(self,aFirst : int=0,aSecond : int=0) -> None: ...
    @property
    def First(self) -> int:
        """
        :type: int
        """
    @First.setter
    def First(self, arg0: int) -> None:
        pass
    @property
    def Second(self) -> int:
        """
        :type: int
        """
    @Second.setter
    def Second(self, arg0: int) -> None:
        pass
    pass
class MeshVS_TwoNodesHasher():
    """
    Purpose: The DefaultHasher is a Hasher that is used by default in NCollection maps. To compute the hash code of the key is used the global function HashCode. To compare two keys is used the global function IsEqual.
    """
    @staticmethod
    def HashCode_s(theKey : MeshVS_TwoNodes,theUpperBound : int) -> int: 
        """
        Returns hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theKey1 : MeshVS_TwoNodes,theKey2 : MeshVS_TwoNodes) -> bool: 
        """
        None
        """
    pass
class MeshVS_VectorPrsBuilder(MeshVS_PrsBuilder, OCP.Standard.Standard_Transient):
    """
    This class provides methods to create vector data presentation. It store map of vectors assigned with nodes or elements. In simplified mode vectors draws with thickened ends instead of arrowsThis class provides methods to create vector data presentation. It store map of vectors assigned with nodes or elements. In simplified mode vectors draws with thickened ends instead of arrows
    """
    def Build(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,IsElement : bool,theDisplayMode : int) -> None: 
        """
        Builds vector data presentation
        """
    def CustomBuild(self,Prs : OCP.Graphic3d.Graphic3d_Structure,IDs : OCP.TColStd.TColStd_PackedMapOfInteger,IDsToExclude : OCP.TColStd.TColStd_PackedMapOfInteger,DisplayMode : int) -> None: 
        """
        This method is called to build presentation of custom elements (they have MeshVS_ET_0D type). IDs is set of numeric identificators of elements for custom building. IDsToExclude is set of IDs to exclude from processing. If some entity has been excluded, it is not processed by other builders. DisplayMode is numeric constant describing display mode (see MeshVS_DisplayModeFlags.hxx)
        """
    def CustomSensitiveEntity(self,Owner : OCP.SelectMgr.SelectMgr_EntityOwner,SelectMode : int) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        This method is called to build sensitive of custom elements ( they have MeshVS_ET_0D type )
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DrawVector(self,theTrsf : OCP.gp.gp_Trsf,Length : float,MaxLength : float,ArrowPoints : OCP.TColgp.TColgp_Array1OfPnt,Lines : OCP.Graphic3d.Graphic3d_ArrayOfPrimitives,ArrowLines : OCP.Graphic3d.Graphic3d_ArrayOfPrimitives,Triangles : OCP.Graphic3d.Graphic3d_ArrayOfPrimitives) -> None: 
        """
        Adds to array of polygons and polylines some primitive representing single vector
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetDataSource(self) -> MeshVS_DataSource: 
        """
        Returns custom data source or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetDrawer(self) -> MeshVS_Drawer: 
        """
        Returns custom drawer or default ( from MeshVS_Mesh ) if custom is NULL
        """
    def GetFlags(self) -> int: 
        """
        Returns flags, assigned with builder during creation
        """
    def GetId(self) -> int: 
        """
        Returns builder ID
        """
    def GetMinMaxVectorValue(self,IsElement : bool) -> Tuple[float, float]: 
        """
        Calculates minimal and maximal length of vectors in map ( nodal, if IsElement = False or elemental, if IsElement = True )
        """
    def GetPresentationManager(self) -> OCP.PrsMgr.PrsMgr_PresentationManager: 
        """
        Get presentation manager of builder
        """
    def GetPriority(self) -> int: 
        """
        Returns priority; as priority bigger, as soon builder will be called.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetVector(self,IsElement : bool,ID : int,Vect : OCP.gp.gp_Vec) -> bool: 
        """
        Returns vector assigned with certain node or element
        """
    def GetVectors(self,IsElement : bool) -> MeshVS_DataMapOfIntegerVector: 
        """
        Returns map of vectors assigned with nodes or elements
        """
    def HasVectors(self,IsElement : bool) -> bool: 
        """
        Returns true, if map isn't empty
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsExcludingOn(self) -> bool: 
        """
        Read excluding state
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
    def SetDataSource(self,newDS : MeshVS_DataSource) -> None: 
        """
        Change custom data source
        """
    def SetDrawer(self,newDr : MeshVS_Drawer) -> None: 
        """
        Change custom drawer
        """
    def SetExcluding(self,state : bool) -> None: 
        """
        Set excluding state. If it is Standard_True, the nodes or elements, processed by current builder will be noted and next builder won't process its.
        """
    def SetPresentationManager(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> None: 
        """
        Set presentation manager for builder
        """
    def SetSimplePrsMode(self,IsSimpleArrow : bool) -> None: 
        """
        Sets flag that indicates is simple vector arrow mode uses or not default value is False
        """
    def SetSimplePrsParams(self,theLineWidthParam : float,theStartParam : float,theEndParam : float) -> None: 
        """
        Sets parameters of simple vector arrwo presentation theLineWidthParam - coefficient of vector line width (to draw line instead of arrow) theStartParam and theEndParam parameters of start and end of thickened ends position of thickening calculates according to parameters and maximum vector length default values are: theLineWidthParam = 2.5 theStartParam = 0.85 theEndParam = 0.95
        """
    def SetVector(self,IsElement : bool,ID : int,Vect : OCP.gp.gp_Vec) -> None: 
        """
        Sets vector assigned with certain node or element
        """
    def SetVectors(self,IsElement : bool,Map : MeshVS_DataMapOfIntegerVector) -> None: 
        """
        Sets map of vectors assigned with nodes or elements
        """
    def TestFlags(self,DisplayMode : int) -> bool: 
        """
        Test whether display mode has flags assigned with this builder. This method has default implementation and can be redefined for advance behavior Returns Standard_True only if display mode is appropriate for this builder
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Parent : MeshVS_Mesh,MaxLength : float,VectorColor : OCP.Quantity.Quantity_Color,Flags : int=4,DS : MeshVS_DataSource=None,Id : int=-1,Priority : int=25,IsSimplePrs : bool=False) -> None: ...
    @staticmethod
    def calculateArrow_s(Points : OCP.TColgp.TColgp_Array1OfPnt,Length : float,ArrowPart : float) -> float: 
        """
        Calculates points of arrow presentation
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
def BindTwoColors(arg0 : OCP.Quantity.Quantity_Color,arg1 : OCP.Quantity.Quantity_Color) -> MeshVS_TwoColors:
    """
    None
    """
def ExtractColor(arg0 : MeshVS_TwoColors,arg1 : int) -> OCP.Quantity.Quantity_Color:
    """
    None
    """
def ExtractColors(arg0 : MeshVS_TwoColors,arg1 : OCP.Quantity.Quantity_Color,arg2 : OCP.Quantity.Quantity_Color) -> None:
    """
    None
    """
@overload
def HashCode(theKey : MeshVS_TwoColors,theUpperBound : int) -> int:
    """
    Computes a hash code for the key, in the range [1, theUpperBound]

    Computes a hash code for two nodes, in the range [1, theUpperBound]
    """
@overload
def HashCode(theTwoNodes : MeshVS_TwoNodes,theUpperBound : int) -> int:
    pass
def IsEqual(K1 : MeshVS_TwoColors,K2 : MeshVS_TwoColors) -> bool:
    """
    None
    """
MeshVS_BP_Default = 30
MeshVS_BP_ElemColor = 15
MeshVS_BP_Mesh = 5
MeshVS_BP_NodalColor = 10
MeshVS_BP_Text = 20
MeshVS_BP_User = 30
MeshVS_BP_Vector = 25
MeshVS_DA_BackInteriorColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BackInteriorColor: 2>
MeshVS_DA_BackMaterial: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BackMaterial: 8>
MeshVS_DA_BeamColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BeamColor: 11>
MeshVS_DA_BeamType: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BeamType: 9>
MeshVS_DA_BeamWidth: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_BeamWidth: 10>
MeshVS_DA_ColorReflection: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ColorReflection: 29>
MeshVS_DA_ComputeSelectionTime: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ComputeSelectionTime: 33>
MeshVS_DA_ComputeTime: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ComputeTime: 32>
MeshVS_DA_DisplayNodes: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_DisplayNodes: 34>
MeshVS_DA_EdgeColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_EdgeColor: 3>
MeshVS_DA_EdgeType: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_EdgeType: 4>
MeshVS_DA_EdgeWidth: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_EdgeWidth: 5>
MeshVS_DA_FrontMaterial: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_FrontMaterial: 7>
MeshVS_DA_HatchStyle: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_HatchStyle: 6>
MeshVS_DA_InteriorColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor: 1>
MeshVS_DA_InteriorStyle: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_InteriorStyle: 0>
MeshVS_DA_IsAllowOverlapped: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_IsAllowOverlapped: 27>
MeshVS_DA_MarkerColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_MarkerColor: 13>
MeshVS_DA_MarkerScale: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_MarkerScale: 14>
MeshVS_DA_MarkerType: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_MarkerType: 12>
MeshVS_DA_MaxFaceNodes: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_MaxFaceNodes: 31>
MeshVS_DA_Reflection: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_Reflection: 28>
MeshVS_DA_SelectableAuto: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_SelectableAuto: 35>
MeshVS_DA_ShowEdges: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ShowEdges: 36>
MeshVS_DA_ShrinkCoeff: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_ShrinkCoeff: 30>
MeshVS_DA_SmoothShading: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_SmoothShading: 37>
MeshVS_DA_SupressBackFaces: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_SupressBackFaces: 38>
MeshVS_DA_TextColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextColor: 15>
MeshVS_DA_TextDisplayType: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextDisplayType: 21>
MeshVS_DA_TextExpansionFactor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextExpansionFactor: 18>
MeshVS_DA_TextFont: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextFont: 17>
MeshVS_DA_TextFontAspect: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextFontAspect: 23>
MeshVS_DA_TextHeight: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextHeight: 16>
MeshVS_DA_TextSpace: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextSpace: 19>
MeshVS_DA_TextStyle: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextStyle: 20>
MeshVS_DA_TextTexFont: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_TextTexFont: 22>
MeshVS_DA_User: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_User: 39>
MeshVS_DA_VectorArrowPart: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_VectorArrowPart: 26>
MeshVS_DA_VectorColor: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_VectorColor: 24>
MeshVS_DA_VectorMaxLength: OCP.MeshVS.MeshVS_DrawerAttribute # value = <MeshVS_DrawerAttribute.MeshVS_DA_VectorMaxLength: 25>
MeshVS_DMF_DeformedMask = 384
MeshVS_DMF_DeformedPrsShading = 256
MeshVS_DMF_DeformedPrsShrink = 384
MeshVS_DMF_DeformedPrsWireFrame = 128
MeshVS_DMF_ElementalColorDataPrs = 16
MeshVS_DMF_EntitiesWithData = 64
MeshVS_DMF_HilightPrs = 1024
MeshVS_DMF_NodalColorDataPrs = 8
MeshVS_DMF_OCCMask = 3
MeshVS_DMF_SelectionPrs = 512
MeshVS_DMF_Shading = 2
MeshVS_DMF_Shrink = 3
MeshVS_DMF_TextDataPrs = 32
MeshVS_DMF_User = 2048
MeshVS_DMF_VectorDataPrs = 4
MeshVS_DMF_WireFrame = 1
MeshVS_ET_0D: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_0D: 2>
MeshVS_ET_All: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_All: 31>
MeshVS_ET_Element: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Element: 30>
MeshVS_ET_Face: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Face: 8>
MeshVS_ET_Link: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Link: 4>
MeshVS_ET_NONE: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_NONE: 0>
MeshVS_ET_Node: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Node: 1>
MeshVS_ET_Volume: OCP.MeshVS.MeshVS_EntityType # value = <MeshVS_EntityType.MeshVS_ET_Volume: 16>
MeshVS_MSM_BOX: OCP.MeshVS.MeshVS_MeshSelectionMethod # value = <MeshVS_MeshSelectionMethod.MeshVS_MSM_BOX: 2>
MeshVS_MSM_NODES: OCP.MeshVS.MeshVS_MeshSelectionMethod # value = <MeshVS_MeshSelectionMethod.MeshVS_MSM_NODES: 1>
MeshVS_MSM_PRECISE: OCP.MeshVS.MeshVS_MeshSelectionMethod # value = <MeshVS_MeshSelectionMethod.MeshVS_MSM_PRECISE: 0>
MeshVS_SMF_0D: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_0D: 2>
MeshVS_SMF_All: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_All: 31>
MeshVS_SMF_Element: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Element: 30>
MeshVS_SMF_Face: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Face: 8>
MeshVS_SMF_Group: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Group: 256>
MeshVS_SMF_Link: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Link: 4>
MeshVS_SMF_Mesh: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Mesh: 0>
MeshVS_SMF_Node: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Node: 1>
MeshVS_SMF_Volume: OCP.MeshVS.MeshVS_SelectionModeFlags # value = <MeshVS_SelectionModeFlags.MeshVS_SMF_Volume: 16>
