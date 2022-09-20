import OCP.IVtk
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import io
import OCP.gp
import OCP.Graphic3d
import OCP.Standard
__all__  = [
"IVtk_DisplayMode",
"IVtk_Interface",
"IVtk_IShapeData",
"IVtk_IShapeMesher",
"IVtk_IView",
"IVtk_IdTypeMap",
"IVtk_IShape",
"IVtk_MeshType",
"IVtk_Pnt2dList",
"IVtk_SelectionMode",
"IVtk_SelectionModeList",
"IVtk_ShapeIdList",
"IVtk_ShapePtrList",
"IVtk_SubShapeMap",
"DM_Shading",
"DM_Wireframe",
"MT_BoundaryEdge",
"MT_FreeEdge",
"MT_FreeVertex",
"MT_IsoLine",
"MT_SeamEdge",
"MT_ShadedFace",
"MT_SharedEdge",
"MT_SharedVertex",
"MT_Undefined",
"MT_WireFrameFace",
"SM_CompSolid",
"SM_Compound",
"SM_Edge",
"SM_Face",
"SM_None",
"SM_Shape",
"SM_Shell",
"SM_Solid",
"SM_Vertex",
"SM_Wire"
]
class IVtk_DisplayMode():
    """
    Enumeration that describes all supported display modes for 3D shapes.

    Members:

      DM_Wireframe

      DM_Shading
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
    DM_Shading: OCP.IVtk.IVtk_DisplayMode # value = <IVtk_DisplayMode.DM_Shading: 1>
    DM_Wireframe: OCP.IVtk.IVtk_DisplayMode # value = <IVtk_DisplayMode.DM_Wireframe: 0>
    __entries: dict # value = {'DM_Wireframe': (<IVtk_DisplayMode.DM_Wireframe: 0>, None), 'DM_Shading': (<IVtk_DisplayMode.DM_Shading: 1>, None)}
    __members__: dict # value = {'DM_Wireframe': <IVtk_DisplayMode.DM_Wireframe: 0>, 'DM_Shading': <IVtk_DisplayMode.DM_Shading: 1>}
    pass
class IVtk_Interface(OCP.Standard.Standard_Transient):
    """
    Base interface for visualisation component.Base interface for visualisation component.Base interface for visualisation component.
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
class IVtk_IShapeData(IVtk_Interface, OCP.Standard.Standard_Transient):
    """
    Interface for working with triangulated data.Interface for working with triangulated data.
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
    def InsertCoordinate(self,theX : float,theY : float,theZ : float) -> int: 
        """
        Insert a coordinate

        Insert a coordinate
        """
    @overload
    def InsertCoordinate(self,thePnt : OCP.gp.gp_Pnt) -> int: ...
    @overload
    def InsertLine(self,theShapeID : int,thePointId1 : int,thePointId2 : int,theMeshType : IVtk_MeshType=IVtk_MeshType.MT_Undefined) -> None: 
        """
        Insert a line.

        Insert a poly-line.
        """
    @overload
    def InsertLine(self,theShapeID : int,thePointIds : IVtk_ShapeIdList,theMeshType : IVtk_MeshType=IVtk_MeshType.MT_Undefined) -> None: ...
    def InsertPoint(self,thePnt : OCP.gp.gp_Pnt,theNorm : OCP.gp.gp_Vec3f) -> int: 
        """
        Insert a coordinate
        """
    def InsertTriangle(self,theShapeID : int,thePointId1 : int,thePointId2 : int,thePointId3 : int,theMeshType : IVtk_MeshType=IVtk_MeshType.MT_Undefined) -> None: 
        """
        Insert a triangle
        """
    def InsertVertex(self,theShapeID : int,thePointId : int,theMeshType : IVtk_MeshType=IVtk_MeshType.MT_Undefined) -> None: 
        """
        Insert a vertex.
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
class IVtk_IShapeMesher(IVtk_Interface, OCP.Standard.Standard_Transient):
    """
    Interface for triangulator of 3D shapes.Interface for triangulator of 3D shapes.Interface for triangulator of 3D shapes.
    """
    def Build(self,theShape : IVtk_IShape,theData : IVtk_IShapeData) -> None: 
        """
        Main entry point for building shape representation
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
class IVtk_IView(IVtk_Interface, OCP.Standard.Standard_Transient):
    """
    Interface for obtaining view transformation parameters.Interface for obtaining view transformation parameters.Interface for obtaining view transformation parameters.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisplayToWorld(self,theDisplayPnt : OCP.gp.gp_XY,theWorldPnt : OCP.gp.gp_XYZ) -> bool: 
        """
        Converts 3D display coordinates into 3D world coordinates.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetAspectRatio(self) -> float: 
        """
        Returns The current view the aspect ratio
        """
    def GetCamera(self,theProj : OCP.Graphic3d.Graphic3d_Mat4d,theOrient : OCP.Graphic3d.Graphic3d_Mat4d) -> Tuple[bool]: 
        """
        Gets camera projection and orientation matrices
        """
    def GetClippingRange(self,theZNear : float,theZFar : float) -> None: 
        """
        Returns The location of the near and far clipping planes along the direction of projection
        """
    def GetDirectionOfProjection(self,theDx : float,theDy : float,theDz : float) -> None: 
        """
        Returns The projection direction vector of this view
        """
    def GetDistance(self) -> float: 
        """
        Returns The focal distance of the view
        """
    def GetEyePosition(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Returns The world coordinates of the camera position
        """
    def GetParallelScale(self) -> float: 
        """
        Returns The current view's zoom factor (for parallel projection)
        """
    def GetPosition(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Returns The world coordinates of the view position
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetScale(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Returns Three doubles containing scale components of the view transformation
        """
    def GetViewAngle(self) -> float: 
        """
        Returns The current view angle (for perspective projection)
        """
    def GetViewCenter(self,theX : float,theY : float) -> None: 
        """
        Returns Two doubles containing the display coordinates of the view window center
        """
    def GetViewUp(self,theDx : float,theDy : float,theDz : float) -> None: 
        """
        Returns The "view up" direction of the view
        """
    def GetViewport(self) -> Tuple[float, float, float, float]: 
        """
        Gets viewport coordinates
        """
    def GetWindowSize(self,theX : int,theY : int) -> None: 
        """
        Gets window size in screen coordinates in pixels
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
    def IsPerspective(self) -> bool: 
        """
        Returns true if this is a perspective view, and false otherwise.
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
class IVtk_IdTypeMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : int) -> bool: 
        """
        Add
        """
    def Added(self,K : int) -> int: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : IVtk_IdTypeMap) -> IVtk_IdTypeMap: 
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
    def Contains(self,K : int) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : IVtk_IdTypeMap) -> bool: ...
    def Differ(self,theOther : IVtk_IdTypeMap) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : IVtk_IdTypeMap,theRight : IVtk_IdTypeMap) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : IVtk_IdTypeMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : IVtk_IdTypeMap) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : IVtk_IdTypeMap) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : IVtk_IdTypeMap,theRight : IVtk_IdTypeMap) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : IVtk_IdTypeMap) -> bool: 
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
    def Remove(self,K : int) -> bool: 
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
    def Subtract(self,theOther : IVtk_IdTypeMap) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : IVtk_IdTypeMap,theRight : IVtk_IdTypeMap) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : IVtk_IdTypeMap,theRight : IVtk_IdTypeMap) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : IVtk_IdTypeMap) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : IVtk_IdTypeMap) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IVtk_IShape(IVtk_Interface, OCP.Standard.Standard_Transient):
    """
    Interface for working with a shape and its sub-shapes ids.Interface for working with a shape and its sub-shapes ids.Interface for working with a shape and its sub-shapes ids.
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
    def GetId(self) -> int: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSubIds(self,theId : int) -> IVtk_ShapeIdList: 
        """
        Get ids of sub-shapes composing a sub-shape with the given id
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
    def SetId(self,theId : int) -> None: 
        """
        None
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
class IVtk_MeshType():
    """
    Enumeration that describes all supported types of mesh parts for 3D shapes.

    Members:

      MT_Undefined

      MT_IsoLine

      MT_FreeVertex

      MT_SharedVertex

      MT_FreeEdge

      MT_BoundaryEdge

      MT_SharedEdge

      MT_WireFrameFace

      MT_ShadedFace

      MT_SeamEdge
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
    MT_BoundaryEdge: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_BoundaryEdge: 4>
    MT_FreeEdge: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_FreeEdge: 3>
    MT_FreeVertex: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_FreeVertex: 1>
    MT_IsoLine: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_IsoLine: 0>
    MT_SeamEdge: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_SeamEdge: 8>
    MT_ShadedFace: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_ShadedFace: 7>
    MT_SharedEdge: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_SharedEdge: 5>
    MT_SharedVertex: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_SharedVertex: 2>
    MT_Undefined: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_Undefined: -1>
    MT_WireFrameFace: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_WireFrameFace: 6>
    __entries: dict # value = {'MT_Undefined': (<IVtk_MeshType.MT_Undefined: -1>, None), 'MT_IsoLine': (<IVtk_MeshType.MT_IsoLine: 0>, None), 'MT_FreeVertex': (<IVtk_MeshType.MT_FreeVertex: 1>, None), 'MT_SharedVertex': (<IVtk_MeshType.MT_SharedVertex: 2>, None), 'MT_FreeEdge': (<IVtk_MeshType.MT_FreeEdge: 3>, None), 'MT_BoundaryEdge': (<IVtk_MeshType.MT_BoundaryEdge: 4>, None), 'MT_SharedEdge': (<IVtk_MeshType.MT_SharedEdge: 5>, None), 'MT_WireFrameFace': (<IVtk_MeshType.MT_WireFrameFace: 6>, None), 'MT_ShadedFace': (<IVtk_MeshType.MT_ShadedFace: 7>, None), 'MT_SeamEdge': (<IVtk_MeshType.MT_SeamEdge: 8>, None)}
    __members__: dict # value = {'MT_Undefined': <IVtk_MeshType.MT_Undefined: -1>, 'MT_IsoLine': <IVtk_MeshType.MT_IsoLine: 0>, 'MT_FreeVertex': <IVtk_MeshType.MT_FreeVertex: 1>, 'MT_SharedVertex': <IVtk_MeshType.MT_SharedVertex: 2>, 'MT_FreeEdge': <IVtk_MeshType.MT_FreeEdge: 3>, 'MT_BoundaryEdge': <IVtk_MeshType.MT_BoundaryEdge: 4>, 'MT_SharedEdge': <IVtk_MeshType.MT_SharedEdge: 5>, 'MT_WireFrameFace': <IVtk_MeshType.MT_WireFrameFace: 6>, 'MT_ShadedFace': <IVtk_MeshType.MT_ShadedFace: 7>, 'MT_SeamEdge': <IVtk_MeshType.MT_SeamEdge: 8>}
    pass
class IVtk_Pnt2dList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : IVtk_Pnt2dList) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.gp.gp_XY,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : OCP.gp.gp_XY) -> OCP.gp.gp_XY: ...
    def Assign(self,theOther : IVtk_Pnt2dList) -> IVtk_Pnt2dList: 
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
    def First(self) -> OCP.gp.gp_XY: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : IVtk_Pnt2dList,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OCP.gp.gp_XY,theIter : Any) -> OCP.gp.gp_XY: ...
    @overload
    def InsertBefore(self,theOther : IVtk_Pnt2dList,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : OCP.gp.gp_XY,theIter : Any) -> OCP.gp.gp_XY: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.gp.gp_XY: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : IVtk_Pnt2dList) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OCP.gp.gp_XY) -> OCP.gp.gp_XY: ...
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
    def __init__(self,theOther : IVtk_Pnt2dList) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class IVtk_SelectionMode():
    """
    Enumeration that describes all supported selection modes for 3D shapes. SM_None means that the shape should become non-selectable. SM_Shape makes the shape selectable as a whole. Other modes activate selection of sub-shapes of corresponding types.

    Members:

      SM_None

      SM_Shape

      SM_Vertex

      SM_Edge

      SM_Wire

      SM_Face

      SM_Shell

      SM_Solid

      SM_CompSolid

      SM_Compound
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
    SM_CompSolid: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_CompSolid: 7>
    SM_Compound: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Compound: 8>
    SM_Edge: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Edge: 2>
    SM_Face: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Face: 4>
    SM_None: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_None: -1>
    SM_Shape: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Shape: 0>
    SM_Shell: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Shell: 5>
    SM_Solid: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Solid: 6>
    SM_Vertex: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Vertex: 1>
    SM_Wire: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Wire: 3>
    __entries: dict # value = {'SM_None': (<IVtk_SelectionMode.SM_None: -1>, None), 'SM_Shape': (<IVtk_SelectionMode.SM_Shape: 0>, None), 'SM_Vertex': (<IVtk_SelectionMode.SM_Vertex: 1>, None), 'SM_Edge': (<IVtk_SelectionMode.SM_Edge: 2>, None), 'SM_Wire': (<IVtk_SelectionMode.SM_Wire: 3>, None), 'SM_Face': (<IVtk_SelectionMode.SM_Face: 4>, None), 'SM_Shell': (<IVtk_SelectionMode.SM_Shell: 5>, None), 'SM_Solid': (<IVtk_SelectionMode.SM_Solid: 6>, None), 'SM_CompSolid': (<IVtk_SelectionMode.SM_CompSolid: 7>, None), 'SM_Compound': (<IVtk_SelectionMode.SM_Compound: 8>, None)}
    __members__: dict # value = {'SM_None': <IVtk_SelectionMode.SM_None: -1>, 'SM_Shape': <IVtk_SelectionMode.SM_Shape: 0>, 'SM_Vertex': <IVtk_SelectionMode.SM_Vertex: 1>, 'SM_Edge': <IVtk_SelectionMode.SM_Edge: 2>, 'SM_Wire': <IVtk_SelectionMode.SM_Wire: 3>, 'SM_Face': <IVtk_SelectionMode.SM_Face: 4>, 'SM_Shell': <IVtk_SelectionMode.SM_Shell: 5>, 'SM_Solid': <IVtk_SelectionMode.SM_Solid: 6>, 'SM_CompSolid': <IVtk_SelectionMode.SM_CompSolid: 7>, 'SM_Compound': <IVtk_SelectionMode.SM_Compound: 8>}
    pass
class IVtk_SelectionModeList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IVtk_SelectionMode) -> IVtk_SelectionMode: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : IVtk_SelectionModeList) -> None: ...
    @overload
    def Append(self,theItem : IVtk_SelectionMode,theIter : Any) -> None: ...
    def Assign(self,theOther : IVtk_SelectionModeList) -> IVtk_SelectionModeList: 
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
    def First(self) -> IVtk_SelectionMode: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : IVtk_SelectionModeList,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : IVtk_SelectionMode,theIter : Any) -> IVtk_SelectionMode: ...
    @overload
    def InsertBefore(self,theItem : IVtk_SelectionMode,theIter : Any) -> IVtk_SelectionMode: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : IVtk_SelectionModeList,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> IVtk_SelectionMode: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : IVtk_SelectionMode) -> IVtk_SelectionMode: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : IVtk_SelectionModeList) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : IVtk_SelectionModeList) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class IVtk_ShapeIdList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : IVtk_ShapeIdList) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : int,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : int) -> int: ...
    def Assign(self,theOther : IVtk_ShapeIdList) -> IVtk_ShapeIdList: 
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
    def First(self) -> int: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : IVtk_ShapeIdList,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : int,theIter : Any) -> int: ...
    @overload
    def InsertBefore(self,theOther : IVtk_ShapeIdList,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : int,theIter : Any) -> int: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> int: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : IVtk_ShapeIdList) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : int) -> int: ...
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
    def __init__(self,theOther : IVtk_ShapeIdList) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class IVtk_ShapePtrList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IVtk_IShape,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : IVtk_ShapePtrList) -> None: ...
    @overload
    def Append(self,theItem : IVtk_IShape) -> IVtk_IShape: ...
    def Assign(self,theOther : IVtk_ShapePtrList) -> IVtk_ShapePtrList: 
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
    def First(self) -> IVtk_IShape: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : IVtk_ShapePtrList,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : IVtk_IShape,theIter : Any) -> IVtk_IShape: ...
    @overload
    def InsertBefore(self,theItem : IVtk_IShape,theIter : Any) -> IVtk_IShape: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : IVtk_ShapePtrList,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> IVtk_IShape: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : IVtk_ShapePtrList) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : IVtk_IShape) -> IVtk_IShape: ...
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
    def __init__(self,theOther : IVtk_ShapePtrList) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class IVtk_SubShapeMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : IVtk_SubShapeMap) -> IVtk_SubShapeMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : IVtk_ShapeIdList) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : IVtk_ShapeIdList) -> IVtk_ShapeIdList: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> IVtk_ShapeIdList: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> IVtk_ShapeIdList: 
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
    def Exchange(self,theOther : IVtk_SubShapeMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> IVtk_ShapeIdList: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : IVtk_ShapeIdList) -> bool: ...
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
    def Seek(self,theKey : int) -> IVtk_ShapeIdList: 
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
    def __init__(self,theOther : IVtk_SubShapeMap) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
DM_Shading: OCP.IVtk.IVtk_DisplayMode # value = <IVtk_DisplayMode.DM_Shading: 1>
DM_Wireframe: OCP.IVtk.IVtk_DisplayMode # value = <IVtk_DisplayMode.DM_Wireframe: 0>
MT_BoundaryEdge: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_BoundaryEdge: 4>
MT_FreeEdge: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_FreeEdge: 3>
MT_FreeVertex: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_FreeVertex: 1>
MT_IsoLine: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_IsoLine: 0>
MT_SeamEdge: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_SeamEdge: 8>
MT_ShadedFace: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_ShadedFace: 7>
MT_SharedEdge: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_SharedEdge: 5>
MT_SharedVertex: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_SharedVertex: 2>
MT_Undefined: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_Undefined: -1>
MT_WireFrameFace: OCP.IVtk.IVtk_MeshType # value = <IVtk_MeshType.MT_WireFrameFace: 6>
SM_CompSolid: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_CompSolid: 7>
SM_Compound: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Compound: 8>
SM_Edge: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Edge: 2>
SM_Face: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Face: 4>
SM_None: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_None: -1>
SM_Shape: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Shape: 0>
SM_Shell: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Shell: 5>
SM_Solid: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Solid: 6>
SM_Vertex: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Vertex: 1>
SM_Wire: OCP.IVtk.IVtk_SelectionMode # value = <IVtk_SelectionMode.SM_Wire: 3>
