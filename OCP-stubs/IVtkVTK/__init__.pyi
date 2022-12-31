import OCP.IVtkVTK
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Graphic3d
import OCP.IVtk
import OCP.gp
import OCP.Standard
__all__  = [
"IVtkVTK_ShapeData",
"IVtkVTK_View"
]
class IVtkVTK_ShapeData(OCP.IVtk.IVtk_IShapeData, OCP.IVtk.IVtk_Interface, OCP.Standard.Standard_Transient):
    """
    IShapeData implementation for VTK.IShapeData implementation for VTK.IShapeData implementation for VTK.
    """
    @staticmethod
    def ARRNAME_MESH_TYPES_s() -> str: 
        """
        None
        """
    @staticmethod
    def ARRNAME_SUBSHAPE_IDS_s() -> str: 
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
    def InsertCoordinate(self,theX : float,theY : float,theZ : float) -> int: 
        """
        Insert a coordinate

        Insert a coordinate
        """
    @overload
    def InsertCoordinate(self,thePnt : OCP.gp.gp_Pnt) -> int: ...
    @overload
    def InsertLine(self,theShapeID : int,thePointId1 : int,thePointId2 : int,theMeshType : OCP.IVtk.IVtk_MeshType) -> None: 
        """
        Insert a line.

        Insert a poly-line.
        """
    @overload
    def InsertLine(self,theShapeID : int,thePointIds : OCP.IVtk.IVtk_ShapeIdList,theMeshType : OCP.IVtk.IVtk_MeshType) -> None: ...
    def InsertPoint(self,thePnt : OCP.gp.gp_Pnt,theNorm : OCP.gp.gp_Vec3f) -> int: 
        """
        Insert a coordinate
        """
    def InsertTriangle(self,theShapeID : int,thePointId1 : int,thePointId2 : int,thePointId3 : int,theMeshType : OCP.IVtk.IVtk_MeshType) -> None: 
        """
        Insert a triangle
        """
    def InsertVertex(self,theShapeID : int,thePointId : int,theMeshType : OCP.IVtk.IVtk_MeshType) -> None: 
        """
        Insert a vertex.
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
    def __init__(self) -> None: ...
    def getVtkPolyData(self) -> vtkPolyData: 
        """
        Get VTK PolyData.
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
class IVtkVTK_View(OCP.IVtk.IVtk_IView, OCP.IVtk.IVtk_Interface, OCP.Standard.Standard_Transient):
    """
    ICamera implementation for VTK.ICamera implementation for VTK.ICamera implementation for VTK.
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
    def IsPerspective(self) -> bool: 
        """
        Returns true if this is a perspective view, and false otherwise.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theRenderer : vtkRenderer) -> None: ...
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
