import OCP.Select3D
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.Poly
import OCP.SelectBasics
import OCP.SelectMgr
import OCP.BVH
import OCP.Bnd
import OCP.TColgp
import OCP.Graphic3d
import OCP.Standard
import OCP.Geom
import OCP.NCollection
import OCP.TopLoc
import OCP.gp
__all__  = [
"Select3D_BVHBuilder3d",
"Select3D_BVHIndexBuffer",
"Select3D_EntitySequence",
"Select3D_SensitiveEntity",
"Select3D_Pnt",
"Select3D_PointData",
"Select3D_SensitiveBox",
"Select3D_SensitiveSet",
"Select3D_SensitivePoly",
"Select3D_InteriorSensitivePointSet",
"Select3D_SensitiveFace",
"Select3D_SensitiveGroup",
"Select3D_SensitivePoint",
"Select3D_SensitiveCircle",
"Select3D_SensitivePrimitiveArray",
"Select3D_SensitiveSegment",
"Select3D_SensitiveCurve",
"Select3D_SensitiveTriangle",
"Select3D_SensitiveTriangulation",
"Select3D_SensitiveWire",
"Select3D_TypeOfSensitivity",
"Select3D_VectorOfHPoly",
"Select3D_TOS_BOUNDARY",
"Select3D_TOS_INTERIOR"
]
class Select3D_BVHBuilder3d(OCP.BVH.BVH_BuilderTransient, OCP.Standard.Standard_Transient):
    """
    Performs construction of BVH tree using bounding boxes (AABBs) of abstract objects.
    """
    def Build(self,theSet : Any,theBVH : Any,theBox : OCP.Graphic3d.Graphic3d_BndBox3d) -> None: 
        """
        Builds BVH using specific algorithm.
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
    def IsParallel(self) -> bool: 
        """
        Returns parallel flag.
        """
    def LeafNodeSize(self) -> int: 
        """
        Returns the maximum number of sub-elements in the leaf.
        """
    def MaxTreeDepth(self) -> int: 
        """
        Returns the maximum depth of constructed BVH.
        """
    def SetParallel(self,isParallel : bool) -> None: 
        """
        Set parallel flag contolling possibility of parallel execution.
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
class Select3D_BVHIndexBuffer(OCP.Graphic3d.Graphic3d_Buffer, OCP.NCollection.NCollection_Buffer, OCP.Standard.Standard_Transient):
    """
    Index buffer for BVH tree.Index buffer for BVH tree.
    """
    def Allocate(self,theSize : int) -> bool: 
        """
        Allocate the buffer.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns buffer allocator
        """
    def Attribute(self,theAttribIndex : int) -> OCP.Graphic3d.Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def AttributeData(self,theAttrib : OCP.Graphic3d.Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def AttributeOffset(self,theAttribIndex : int) -> int: 
        """
        Returns data offset to specified attribute
        """
    def AttributesArray(self) -> OCP.Graphic3d.Graphic3d_Attribute: 
        """
        Returns array of attributes definitions
        """
    def ChangeAttribute(self,theAttribIndex : int) -> OCP.Graphic3d.Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def ChangeAttributeData(self,theAttrib : OCP.Graphic3d.Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def ChangeData(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
        """
    def Data(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
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
    def FindAttribute(self,theAttrib : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> int: 
        """
        Find attribute index.
        """
    def Free(self) -> None: 
        """
        De-allocate buffer.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPatches(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self,theIndex : int) -> int: 
        """
        Access index at specified position
        """
    def Init(self,theNbElems : int,theHasPatches : bool) -> bool: 
        """
        Allocates new empty index array
        """
    def Invalidate(self) -> None: 
        """
        Invalidate entire buffer.
        """
    def InvalidatedRange(self) -> OCP.Graphic3d.Graphic3d_BufferRange: 
        """
        Return invalidated range; EMPTY by default. Requires sub-classing for creating a mutable buffer (advanced usage).
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if buffer is not allocated
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInterleaved(self) -> bool: 
        """
        Flag indicating that attributes in the buffer are interleaved; TRUE by default. Requires sub-classing for creating a non-interleaved buffer (advanced usage).
        """
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
        Return TRUE if data can be invalidated; FALSE by default. Requires sub-classing for creating a mutable buffer (advanced usage).
        """
    def NbMaxElements(self) -> int: 
        """
        Return number of initially allocated elements which can fit into this buffer, while NbElements can be overwritten to smaller value.
        """
    def PatchSize(self,theIndex : int) -> int: 
        """
        Access index at specified position
        """
    def SetAllocator(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Assign new buffer allocator with de-allocation of buffer.
        """
    @overload
    def SetIndex(self,theIndex : int,theValue : int,thePatchSize : int) -> None: 
        """
        Change index at specified position

        Change index at specified position
        """
    @overload
    def SetIndex(self,theIndex : int,theValue : int) -> None: ...
    def Size(self) -> int: 
        """
        Return buffer length in bytes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Validate(self) -> None: 
        """
        Reset invalidated range. Requires sub-classing for creating a mutable buffer (advanced usage).
        """
    def __init__(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def changeValue(self,theElem : int) -> int: 
        """
        Access specified element.
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
    def release(self) -> None: 
        """
        Release buffer.
        """
    def value(self,theElem : int) -> int: 
        """
        Access specified element.
        """
    @property
    def NbAttributes(self) -> int:
        """
        :type: int
        """
    @NbAttributes.setter
    def NbAttributes(self, arg0: int) -> None:
        pass
    @property
    def NbElements(self) -> int:
        """
        :type: int
        """
    @NbElements.setter
    def NbElements(self, arg0: int) -> None:
        pass
    @property
    def Stride(self) -> int:
        """
        :type: int
        """
    @Stride.setter
    def Stride(self, arg0: int) -> None:
        pass
    pass
class Select3D_EntitySequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Select3D_EntitySequence) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Select3D_SensitiveEntity) -> None: ...
    def Assign(self,theOther : Select3D_EntitySequence) -> Select3D_EntitySequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Select3D_SensitiveEntity: 
        """
        First item access
        """
    def ChangeLast(self) -> Select3D_SensitiveEntity: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Select3D_SensitiveEntity: 
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
    def First(self) -> Select3D_SensitiveEntity: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Select3D_EntitySequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Select3D_SensitiveEntity) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Select3D_SensitiveEntity) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Select3D_EntitySequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Select3D_SensitiveEntity: 
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
    def Prepend(self,theItem : Select3D_SensitiveEntity) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Select3D_EntitySequence) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Select3D_SensitiveEntity) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Select3D_EntitySequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Select3D_SensitiveEntity: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Select3D_EntitySequence) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Select3D_SensitiveEntity(OCP.Standard.Standard_Transient):
    """
    Abstract framework to define 3D sensitive entities.Abstract framework to define 3D sensitive entities.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a sensitive if needed
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of a sensitive with transformation applied
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of a sensitive with transformation applied
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
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        Originally this method intended to return sensitive entity with new location aLocation, but currently sensitive entities do not hold a location, instead HasLocation() and Location() methods call corresponding entity owner's methods. Thus all entities returned by GetConnected() share the same location propagated from corresponding selectable object. You must redefine this function for any type of sensitive entity which can accept another connected sensitive entity.
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
        Checks whether sensitive overlaps current selecting volume. Stores minimum depth, distance to center of geometry and closest point detected into thePickResult
        """
    def NbSubElements(self) -> int: 
        """
        Returns the number of sub-entities or elements in sensitive entity. Is used to determine if entity is complex and needs to pre-build BVH at the creation of sensitive entity step or is light-weighted so the tree can be build on demand with unnoticeable delay.
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
class Select3D_Pnt():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def x(self) -> float:
        """
        :type: float
        """
    @x.setter
    def x(self, arg0: float) -> None:
        pass
    @property
    def y(self) -> float:
        """
        :type: float
        """
    @y.setter
    def y(self, arg0: float) -> None:
        pass
    @property
    def z(self) -> float:
        """
        :type: float
        """
    @z.setter
    def z(self, arg0: float) -> None:
        pass
    pass
class Select3D_PointData():
    """
    None
    """
    def Pnt(self,theIndex : int) -> Select3D_Pnt: 
        """
        None
        """
    def Pnt3d(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @overload
    def SetPnt(self,theIndex : int,theValue : OCP.gp.gp_Pnt) -> None: 
        """
        None

        None
        """
    @overload
    def SetPnt(self,theIndex : int,theValue : Select3D_Pnt) -> None: ...
    def Size(self) -> int: 
        """
        None
        """
    def __init__(self,theNbPoints : int) -> None: ...
    pass
class Select3D_SensitiveBox(Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    A framework to define selection by a sensitive box.A framework to define selection by a sensitive box.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a sensitive if needed
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns coordinates of the box. If location transformation is set, it will be applied
        """
    def Box(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the box. If location transformation is set, it will be applied
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
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theBox : OCP.Bnd.Bnd_Box) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theXMin : float,theYMin : float,theZMin : float,theXMax : float,theYMax : float,theZMax : float) -> None: ...
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
class Select3D_SensitiveSet(Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    This class is base class for handling overlap detection of complex sensitive entities. It provides an interface for building BVH tree for some set of entities. Thereby, each iteration of overlap detection is a traverse of BVH tree in fact. To use speed-up hierarchical structure in a custom complex sensitive entity, it is necessary to make that custom entity a descendant of this class and organize sub-entities in some container which allows referencing to elements by index. Note that methods taking index as a parameter are used for BVH build and the range of given index is [0; Size() - 1]. For example of usage see Select3D_SensitiveTriangulation.This class is base class for handling overlap detection of complex sensitive entities. It provides an interface for building BVH tree for some set of entities. Thereby, each iteration of overlap detection is a traverse of BVH tree in fact. To use speed-up hierarchical structure in a custom complex sensitive entity, it is necessary to make that custom entity a descendant of this class and organize sub-entities in some container which allows referencing to elements by index. Note that methods taking index as a parameter are used for BVH build and the range of given index is [0; Size() - 1]. For example of usage see Select3D_SensitiveTriangulation.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for sensitive set. Must be called manually to build BVH tree for any sensitive set in case if its content was initialized not in a constructor, but element by element
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of the whole set. This method should be redefined in Select3D_SensitiveSet descendants
        """
    def Box(self,theIdx : int) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of sub-entity with index theIdx in sub-entity list
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of sensitive entity index theIdx along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the whole set. This method should be redefined in Select3D_SensitiveSet descendants
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
    def DefaultBVHBuilder_s() -> Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        Originally this method intended to return sensitive entity with new location aLocation, but currently sensitive entities do not hold a location, instead HasLocation() and Location() methods call corresponding entity owner's methods. Thus all entities returned by GetConnected() share the same location propagated from corresponding selectable object. You must redefine this function for any type of sensitive entity which can accept another connected sensitive entity.
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
        Returns the number of sub-entities or elements in sensitive entity. Is used to determine if entity is complex and needs to pre-build BVH at the creation of sensitive entity step or is light-weighted so the tree can be build on demand with unnoticeable delay.
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
    def SetBuilder(self,theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
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
class Select3D_SensitivePoly(Select3D_SensitiveSet, Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    Sensitive Entity to make a face selectable. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions from its member Select3D_PointData myPolyg.Sensitive Entity to make a face selectable. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions from its member Select3D_PointData myPolyg.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for sensitive set. Must be called manually to build BVH tree for any sensitive set in case if its content was initialized not in a constructor, but element by element
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of a polygon. If location transformation is set, it will be applied
        """
    def Box(self,theIdx : int) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of segment with index theIdx
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of sensitive entity index theIdx in the vector along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the point set. If location transformation is set, it will be applied
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
    def DefaultBVHBuilder_s() -> Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        Originally this method intended to return sensitive entity with new location aLocation, but currently sensitive entities do not hold a location, instead HasLocation() and Location() methods call corresponding entity owner's methods. Thus all entities returned by GetConnected() share the same location propagated from corresponding selectable object. You must redefine this function for any type of sensitive entity which can accept another connected sensitive entity.
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
        Returns the amount of segments in poly
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def Points3D(self,theHArrayOfPnt : OCP.TColgp.TColgp_HArray1OfPnt) -> Any: 
        """
        Returns the 3D points of the array used at construction time.
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetBuilder(self,theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def Size(self) -> int: 
        """
        Returns the amount of segments of the poly
        """
    def Swap(self,theIdx1 : int,theIdx2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2 in the vector
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theIsBVHEnabled : bool,theNbPnts : int=6) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePoints : OCP.TColgp.TColgp_HArray1OfPnt,theIsBVHEnabled : bool) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePoints : OCP.TColgp.TColgp_Array1OfPnt,theIsBVHEnabled : bool) -> None: ...
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
class Select3D_InteriorSensitivePointSet(Select3D_SensitiveSet, Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    This class handles the selection of arbitrary point set with internal type of sensitivity. The main principle is to split the point set given onto planar convex polygons and search for the overlap with one or more of them through traverse of BVH tree.This class handles the selection of arbitrary point set with internal type of sensitivity. The main principle is to split the point set given onto planar convex polygons and search for the overlap with one or more of them through traverse of BVH tree.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for sensitive set. Must be called manually to build BVH tree for any sensitive set in case if its content was initialized not in a constructor, but element by element
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of the point set. If location transformation is set, it will be applied
        """
    def Box(self,theIdx : int) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of planar convex polygon with index theIdx
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of planar convex polygon with index theIdx in the vector along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the point set. If location transformation is set, it will be applied
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
    def DefaultBVHBuilder_s() -> Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        Originally this method intended to return sensitive entity with new location aLocation, but currently sensitive entities do not hold a location, instead HasLocation() and Location() methods call corresponding entity owner's methods. Thus all entities returned by GetConnected() share the same location propagated from corresponding selectable object. You must redefine this function for any type of sensitive entity which can accept another connected sensitive entity.
        """
    def GetLeafNodeSize(self) -> int: 
        """
        Returns a number of nodes in 1 BVH leaf
        """
    def GetPoints(self,theHArrayOfPnt : OCP.TColgp.TColgp_HArray1OfPnt) -> Any: 
        """
        Initializes the given array theHArrayOfPnt by 3d coordinates of vertices of the whole point set
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
        Returns the amount of points in set
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
    def SetBuilder(self,theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def Size(self) -> int: 
        """
        Returns the length of vector of planar convex polygons
        """
    def Swap(self,theIdx1 : int,theIdx2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2 in the vector
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePoints : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
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
class Select3D_SensitiveFace(Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    Sensitive Entity to make a face selectable. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.Sensitive Entity to make a face selectable. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for the face
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
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
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePoints : OCP.TColgp.TColgp_Array1OfPnt,theType : Select3D_TypeOfSensitivity) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePoints : OCP.TColgp.TColgp_HArray1OfPnt,theType : Select3D_TypeOfSensitivity) -> None: ...
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
class Select3D_SensitiveGroup(Select3D_SensitiveSet, Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    A framework to define selection of a sensitive group by a sensitive entity which is a set of 3D sensitive entities. Remark: 2 modes are possible for rectangle selection the group is considered selected 1) when all the entities inside are selected in the rectangle 2) only one entity inside is selected by the rectangle By default the "Match All entities" mode is set.A framework to define selection of a sensitive group by a sensitive entity which is a set of 3D sensitive entities. Remark: 2 modes are possible for rectangle selection the group is considered selected 1) when all the entities inside are selected in the rectangle 2) only one entity inside is selected by the rectangle By default the "Match All entities" mode is set.
    """
    @overload
    def Add(self,theSensitive : Select3D_SensitiveEntity) -> None: 
        """
        Adds the list of sensitive entities LL to the empty sensitive group object created at construction time.

        Adds the sensitive entity aSensitive to the non-empty sensitive group object created at construction time.
        """
    @overload
    def Add(self,theEntities : Select3D_EntitySequence) -> None: ...
    def BVH(self) -> None: 
        """
        Builds BVH tree for sensitive set. Must be called manually to build BVH tree for any sensitive set in case if its content was initialized not in a constructor, but element by element
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of the group. If location transformation is set, it will be applied
        """
    def Box(self,theIdx : int) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of sensitive entity with index theIdx
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of sensitive entity index theIdx in the vector along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of entity set. If location transformation is set, it will be applied
        """
    def Clear(self) -> None: 
        """
        Removes all sensitive entities from the list used at the time of construction, or added using the function Add.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @staticmethod
    def DefaultBVHBuilder_s() -> Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Entities(self) -> Any: 
        """
        Gets group content
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        None
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
    def IsIn(self,theSensitive : Select3D_SensitiveEntity) -> bool: 
        """
        Returns true if the sensitive entity aSensitive is in the list used at the time of construction, or added using the function Add.
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
    def LastDetectedEntity(self) -> Select3D_SensitiveEntity: 
        """
        Return last detected entity.
        """
    def LastDetectedEntityIndex(self) -> int: 
        """
        Return index of last detected entity.
        """
    def MarkDirty(self) -> None: 
        """
        Marks BVH tree of the set as outdated. It will be rebuild at the next call of BVH()
        """
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks whether the group overlaps current selecting volume
        """
    def MustMatchAll(self) -> bool: 
        """
        Returns true if all sensitive entities in the list used at the time of construction, or added using the function Add must be matched.
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of sub-entities
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def Remove(self,theSensitive : Select3D_SensitiveEntity) -> None: 
        """
        None
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets the owner for all entities in group
        """
    def SetBuilder(self,theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    def SetCheckOverlapAll(self,theToCheckAll : bool) -> None: 
        """
        Returns TRUE if all sensitive entities should be checked within rectangular/polygonal selection, FALSE by default. Can be useful for sensitive entities holding detection results as class property.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetMatchType(self,theIsMustMatchAll : bool) -> None: 
        """
        Sets the requirement that all sensitive entities in the list used at the time of construction, or added using the function Add must be matched.
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def Size(self) -> int: 
        """
        Returns the length of vector of sensitive entities
        """
    def SubEntity(self,theIndex : int) -> Select3D_SensitiveEntity: 
        """
        Access entity by index [1, NbSubElements()].
        """
    def Swap(self,theIdx1 : int,theIdx2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2 in the vector
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToCheckOverlapAll(self) -> bool: 
        """
        Returns TRUE if all sensitive entities should be checked within rectangular/polygonal selection, FALSE by default. Can be useful for sensitive entities holding detection results as class property.
        """
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theIsMustMatchAll : bool=True) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theEntities : Select3D_EntitySequence,theIsMustMatchAll : bool=True) -> None: ...
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
class Select3D_SensitivePoint(Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    A framework to define sensitive 3D points.A framework to define sensitive 3D points.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a sensitive if needed
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of the point. If location transformation is set, it will be applied
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of point. If location transformation is set, it will be applied
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
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
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
        Checks whether the point overlaps current selecting volume
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of sub-entities in sensitive
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point used at the time of construction.
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePoint : OCP.gp.gp_Pnt) -> None: ...
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
class Select3D_SensitiveCircle(Select3D_SensitivePoly, Select3D_SensitiveSet, Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    A framework to define sensitive 3D arcs and circles. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.A framework to define sensitive 3D arcs and circles. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.
    """
    def ArrayBounds(self) -> Tuple[int, int]: 
        """
        None
        """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a circle's edge segments if needed
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of a polygon. If location transformation is set, it will be applied
        """
    def Box(self,theIdx : int) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of segment with index theIdx
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of sensitive entity index theIdx in the vector along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the circle. If location transformation is set, it will be applied
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
    def DefaultBVHBuilder_s() -> Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        None
        """
    def GetLeafNodeSize(self) -> int: 
        """
        Returns a number of nodes in 1 BVH leaf
        """
    def GetPoint3d(self,thePntIdx : int) -> OCP.gp.gp_Pnt: 
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
    def MarkDirty(self) -> None: 
        """
        Marks BVH tree of the set as outdated. It will be rebuild at the next call of BVH()
        """
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks whether the circle overlaps current selecting volume
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of segments in poly
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def Points3D(self,theHArrayOfPnt : OCP.TColgp.TColgp_HArray1OfPnt) -> Any: 
        """
        Returns the 3D points of the array used at construction time.
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetBuilder(self,theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def Size(self) -> int: 
        """
        Returns the amount of segments of the poly
        """
    def Swap(self,theIdx1 : int,theIdx2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2 in the vector
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePnts3d : OCP.TColgp.TColgp_HArray1OfPnt,theIsFilled : bool=False) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theCircle : OCP.Geom.Geom_Circle,theU1 : float,theU2 : float,theIsFilled : bool=False,theNbPnts : int=12) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePnts3d : OCP.TColgp.TColgp_Array1OfPnt,theIsFilled : bool=False) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theCircle : OCP.Geom.Geom_Circle,theIsFilled : bool=False,theNbPnts : int=12) -> None: ...
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
class Select3D_SensitivePrimitiveArray(Select3D_SensitiveSet, Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    Sensitive for triangulation or point set defined by Primitive Array. The primitives can be optionally combined into patches within BVH tree to reduce its building time in expense of extra traverse time.Sensitive for triangulation or point set defined by Primitive Array. The primitives can be optionally combined into patches within BVH tree to reduce its building time in expense of extra traverse time.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for sensitive set.
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of the triangulation. If location transformation is set, it will be applied
        """
    def Box(self,theIdx : int) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of triangle/edge with index theIdx
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of triangle/edge with index theIdx in array along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of triangulation. If location transformation is set, it will be applied
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
    def DefaultBVHBuilder_s() -> Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        None
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
    @overload
    def InitPoints(self,theVerts : OCP.Graphic3d.Graphic3d_Buffer,theIndices : OCP.Graphic3d.Graphic3d_IndexBuffer,theInitLoc : OCP.TopLoc.TopLoc_Location,theToEvalMinMax : bool=True,theNbGroups : int=1) -> bool: 
        """
        Initialize the sensitive object from point set. The sub-set of points can be specified by arguments theIndexLower and theIndexUpper (these are for iterating theIndices, not to restrict the actual index values!).

        Initialize the sensitive object from point set.

        Initialize the sensitive object from point set.
        """
    @overload
    def InitPoints(self,theVerts : OCP.Graphic3d.Graphic3d_Buffer,theInitLoc : OCP.TopLoc.TopLoc_Location,theToEvalMinMax : bool=True,theNbGroups : int=1) -> bool: ...
    @overload
    def InitPoints(self,theVerts : OCP.Graphic3d.Graphic3d_Buffer,theIndices : OCP.Graphic3d.Graphic3d_IndexBuffer,theInitLoc : OCP.TopLoc.TopLoc_Location,theIndexLower : int,theIndexUpper : int,theToEvalMinMax : bool=True,theNbGroups : int=1) -> bool: ...
    @overload
    def InitTriangulation(self,theVerts : OCP.Graphic3d.Graphic3d_Buffer,theIndices : OCP.Graphic3d.Graphic3d_IndexBuffer,theInitLoc : OCP.TopLoc.TopLoc_Location,theToEvalMinMax : bool=True,theNbGroups : int=1) -> bool: 
        """
        Initialize the sensitive object from triangualtion. The sub-triangulation can be specified by arguments theIndexLower and theIndexUpper (these are for iterating theIndices, not to restrict the actual index values!).

        Initialize the sensitive object from triangualtion.
        """
    @overload
    def InitTriangulation(self,theVerts : OCP.Graphic3d.Graphic3d_Buffer,theIndices : OCP.Graphic3d.Graphic3d_IndexBuffer,theInitLoc : OCP.TopLoc.TopLoc_Location,theIndexLower : int,theIndexUpper : int,theToEvalMinMax : bool=True,theNbGroups : int=1) -> bool: ...
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
    def LastDetectedEdgeNode1(self) -> int: 
        """
        Return the first node of last topmost detected edge or -1 if undefined (axis picking).
        """
    def LastDetectedEdgeNode2(self) -> int: 
        """
        Return the second node of last topmost detected edge or -1 if undefined (axis picking).
        """
    def LastDetectedElement(self) -> int: 
        """
        Return last topmost detected element or -1 if undefined (axis picking).
        """
    def LastDetectedElementMap(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Return the index map of last detected elements (rectangle selection).
        """
    def LastDetectedNode(self) -> int: 
        """
        Return last topmost detected node or -1 if undefined (axis picking).
        """
    def LastDetectedNodeMap(self) -> OCP.TColStd.TColStd_HPackedMapOfInteger: 
        """
        Return the index map of last detected nodes (rectangle selection).
        """
    def MarkDirty(self) -> None: 
        """
        Marks BVH tree of the set as outdated. It will be rebuild at the next call of BVH()
        """
    def Matches(self,theMgr : OCP.SelectBasics.SelectBasics_SelectingVolumeManager,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks whether the sensitive entity is overlapped by current selecting volume.
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of nodes in triangulation
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def PatchDistance(self) -> float: 
        """
        Maximum allowed distance between consequential elements in patch (ShortRealLast() by default). Has no effect on indexed triangulation.
        """
    def PatchSizeMax(self) -> int: 
        """
        Return patch size limit (1 by default).
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets the owner for all entities in group
        """
    def SetBuilder(self,theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetDetectEdges(self,theToDetect : bool) -> None: 
        """
        Setup keeping of the index of last topmost detected edge (axis picking).
        """
    def SetDetectElementMap(self,theToDetect : bool) -> None: 
        """
        Setup keeping of the index map of last detected elements (rectangle selection).
        """
    def SetDetectElements(self,theToDetect : bool) -> None: 
        """
        Setup keeping of the index of last topmost detected element (axis picking).
        """
    def SetDetectNodeMap(self,theToDetect : bool) -> None: 
        """
        Setup keeping of the index map of last detected nodes (rectangle selection).
        """
    def SetDetectNodes(self,theToDetect : bool) -> None: 
        """
        Setup keeping of the index of last topmost detected node (for axis picking).
        """
    def SetMinMax(self,theMinX : float,theMinY : float,theMinZ : float,theMaxX : float,theMaxY : float,theMaxZ : float) -> None: 
        """
        Assign new not transformed bounding box.
        """
    def SetPatchDistance(self,thePatchDistMax : float) -> None: 
        """
        Assign patch distance limit. Should be set before initialization.
        """
    def SetPatchSizeMax(self,thePatchSizeMax : int) -> None: 
        """
        Assign patch size limit. Should be set before initialization.
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def Size(self) -> int: 
        """
        Returns the length of array of triangles or edges
        """
    def Swap(self,theIdx1 : int,theIdx2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2 in array
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToDetectEdges(self) -> bool: 
        """
        Return flag to keep index of last topmost detected edge, FALSE by default.
        """
    def ToDetectElementMap(self) -> bool: 
        """
        Return flag to keep index map of last detected elements, FALSE by default (rectangle selection).
        """
    def ToDetectElements(self) -> bool: 
        """
        Return flag to keep index of last topmost detected element, TRUE by default.
        """
    def ToDetectNodeMap(self) -> bool: 
        """
        Return flag to keep index map of last detected nodes, FALSE by default (rectangle selection).
        """
    def ToDetectNodes(self) -> bool: 
        """
        Return flag to keep index of last topmost detected node, FALSE by default.
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
class Select3D_SensitiveSegment(Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    A framework to define sensitive zones along a segment One gives the 3D start and end pointA framework to define sensitive zones along a segment One gives the 3D start and end point
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a sensitive if needed
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
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
    def GetConnected(self) -> Select3D_SensitiveEntity: 
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
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theFirstPnt : OCP.gp.gp_Pnt,theLastPnt : OCP.gp.gp_Pnt) -> None: ...
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
class Select3D_SensitiveCurve(Select3D_SensitivePoly, Select3D_SensitiveSet, Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    A framework to define a sensitive 3D curve. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.A framework to define a sensitive 3D curve. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for sensitive set. Must be called manually to build BVH tree for any sensitive set in case if its content was initialized not in a constructor, but element by element
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of a polygon. If location transformation is set, it will be applied
        """
    def Box(self,theIdx : int) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of segment with index theIdx
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of sensitive entity index theIdx in the vector along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the point set. If location transformation is set, it will be applied
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
    def DefaultBVHBuilder_s() -> Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        Returns the copy of this
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
        Returns the amount of segments in poly
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def Points3D(self,theHArrayOfPnt : OCP.TColgp.TColgp_HArray1OfPnt) -> Any: 
        """
        Returns the 3D points of the array used at construction time.
        """
    def SensitivityFactor(self) -> int: 
        """
        allows a better sensitivity for a specific entity in selection algorithms useful for small sized entities.
        """
    def Set(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Sets owner of the entity
        """
    def SetBuilder(self,theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def Size(self) -> int: 
        """
        Returns the amount of segments of the poly
        """
    def Swap(self,theIdx1 : int,theIdx2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2 in the vector
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePoints : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theCurve : OCP.Geom.Geom_Curve,theNbPnts : int=17) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePoints : OCP.TColgp.TColgp_HArray1OfPnt) -> None: ...
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
class Select3D_SensitiveTriangle(Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    A framework to define selection of triangles in a view. This comes into play in the detection of meshing and triangulation in surfaces. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.A framework to define selection of triangles in a view. This comes into play in the detection of meshing and triangulation in surfaces. In some cases this class can raise Standard_ConstructionError and Standard_OutOfRange exceptions. For more details see Select3D_SensitivePoly.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for a sensitive if needed
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of the triangle. If location transformation is set, it will be applied
        """
    def Center3D(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center point of the sensitive triangle created at construction time.
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
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        Returns the copy of this
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
        Checks whether the triangle overlaps current selecting volume
        """
    def NbSubElements(self) -> int: 
        """
        Returns the amount of points
        """
    def OwnerId(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns pointer to owner of the entity
        """
    def Points3D(self,thePnt0 : OCP.gp.gp_Pnt,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt) -> None: 
        """
        Returns the 3D points P1, P2, P3 used at the time of construction.
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,thePnt0 : OCP.gp.gp_Pnt,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,theType : Select3D_TypeOfSensitivity=Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR) -> None: ...
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
class Select3D_SensitiveTriangulation(Select3D_SensitiveSet, Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    A framework to define selection of a sensitive entity made of a set of triangles.A framework to define selection of a sensitive entity made of a set of triangles.
    """
    def BVH(self) -> None: 
        """
        Builds BVH tree for sensitive set. Must be called manually to build BVH tree for any sensitive set in case if its content was initialized not in a constructor, but element by element
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of the triangulation. If location transformation is set, it will be applied
        """
    def Box(self,theIdx : int) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of triangle/edge with index theIdx
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of triangle/edge with index theIdx in array along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of triangulation. If location transformation is set, it will be applied
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
    def DefaultBVHBuilder_s() -> Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        None
        """
    def GetInitLocation(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
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
        Returns the amount of nodes in triangulation
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
    def SetBuilder(self,theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def Size(self) -> int: 
        """
        Returns the length of array of triangles or edges
        """
    def Swap(self,theIdx1 : int,theIdx2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2 in array
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theTrg : OCP.Poly.Poly_Triangulation,theInitLoc : OCP.TopLoc.TopLoc_Location,theFreeEdges : OCP.TColStd.TColStd_HArray1OfInteger,theCOG : OCP.gp.gp_Pnt,theIsInterior : bool) -> None: ...
    @overload
    def __init__(self,theOwnerId : OCP.SelectMgr.SelectMgr_EntityOwner,theTrg : OCP.Poly.Poly_Triangulation,theInitLoc : OCP.TopLoc.TopLoc_Location,theIsInterior : bool=True) -> None: ...
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
class Select3D_SensitiveWire(Select3D_SensitiveSet, Select3D_SensitiveEntity, OCP.Standard.Standard_Transient):
    """
    A framework to define selection of a wire owner by an elastic wire band.A framework to define selection of a wire owner by an elastic wire band.
    """
    def Add(self,theSensitive : Select3D_SensitiveEntity) -> None: 
        """
        Adds the sensitive entity theSensitive to this framework.
        """
    def BVH(self) -> None: 
        """
        Builds BVH tree for sensitive set. Must be called manually to build BVH tree for any sensitive set in case if its content was initialized not in a constructor, but element by element
        """
    def BoundingBox(self) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of the wire. If location transformation is set, it will be applied
        """
    def Box(self,theIdx : int) -> OCP.Graphic3d.Graphic3d_BndBox3d: 
        """
        Returns bounding box of sensitive entity with index theIdx
        """
    def Center(self,theIdx : int,theAxis : int) -> float: 
        """
        Returns geometry center of sensitive entity index theIdx in the vector along the given axis theAxis
        """
    def CenterOfGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        Returns center of the wire. If location transformation is set, it will be applied
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
    def DefaultBVHBuilder_s() -> Select3D_BVHBuilder3d: 
        """
        Return global instance to default BVH builder.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetConnected(self) -> Select3D_SensitiveEntity: 
        """
        None
        """
    def GetEdges(self) -> Any: 
        """
        returns the sensitive edges stored in this wire
        """
    def GetLastDetected(self) -> Select3D_SensitiveEntity: 
        """
        None
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
        Returns the amount of sub-entities
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
        Sets the owner for all entities in wire
        """
    def SetBuilder(self,theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Sets the method (builder) used to construct BVH.
        """
    @staticmethod
    def SetDefaultBVHBuilder_s(theBuilder : Select3D_BVHBuilder3d) -> None: 
        """
        Assign new BVH builder to be used by default for new sensitive sets (assigning is NOT thread-safe!).
        """
    def SetSensitivityFactor(self,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular sensitive entity
        """
    def Size(self) -> int: 
        """
        Returns the length of vector of sensitive entities
        """
    def Swap(self,theIdx1 : int,theIdx2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2 in the vector
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class Select3D_TypeOfSensitivity():
    """
    Provides values for type of sensitivity in 3D. These are used to specify whether it is the interior, the boundary, or the exterior of a 3D sensitive entity which is sensitive.

    Members:

      Select3D_TOS_INTERIOR

      Select3D_TOS_BOUNDARY
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Select3D_TOS_BOUNDARY: OCP.Select3D.Select3D_TypeOfSensitivity # value = Select3D_TypeOfSensitivity.Select3D_TOS_BOUNDARY
    Select3D_TOS_INTERIOR: OCP.Select3D.Select3D_TypeOfSensitivity # value = Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR
    __entries: dict # value = {'Select3D_TOS_INTERIOR': (Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR, None), 'Select3D_TOS_BOUNDARY': (Select3D_TypeOfSensitivity.Select3D_TOS_BOUNDARY, None)}
    __members__: dict # value = {'Select3D_TOS_INTERIOR': Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR, 'Select3D_TOS_BOUNDARY': Select3D_TypeOfSensitivity.Select3D_TOS_BOUNDARY}
    pass
class Select3D_VectorOfHPoly(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : Select3D_SensitivePoly) -> Select3D_SensitivePoly: 
        """
        Append
        """
    def Appended(self) -> Select3D_SensitivePoly: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : Select3D_VectorOfHPoly,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> Select3D_SensitivePoly: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Select3D_SensitivePoly: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Select3D_SensitivePoly: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> Select3D_SensitivePoly: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Select3D_SensitivePoly: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : Select3D_SensitivePoly) -> Select3D_SensitivePoly: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Select3D_SensitivePoly: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : Select3D_VectorOfHPoly) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
Select3D_TOS_BOUNDARY: OCP.Select3D.Select3D_TypeOfSensitivity # value = Select3D_TypeOfSensitivity.Select3D_TOS_BOUNDARY
Select3D_TOS_INTERIOR: OCP.Select3D.Select3D_TypeOfSensitivity # value = Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR
