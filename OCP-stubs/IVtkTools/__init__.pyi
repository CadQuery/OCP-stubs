import OCP.IVtkTools
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IVtk
import OCP.IVtkOCC
__all__  = [
"IVtkTools_SubPolyDataFilter",
"IVtkTools_ShapeDataSource",
"IVtkTools_ShapeObject",
"IVtkTools_ShapePicker",
"IVtkTools_DisplayModeFilter"
]
class IVtkTools_SubPolyDataFilter():
    """
    Cells filter according to the given set of cells ids.
    """
    @overload
    def AddData(self,theSet : OCP.IVtk.IVtk_IdTypeMap) -> None: 
        """
        Add ids to be passed through this filter.

        Add ids to be passed through this filter.
        """
    @overload
    def AddData(self,theIds : OCP.IVtk.IVtk_ShapeIdList) -> None: ...
    def Clear(self) -> None: 
        """
        Clear ids set to be passed through this filter.
        """
    def GetNumberOfGenerationsFromBase(self,type : str) -> int: 
        """
        None
        """
    @staticmethod
    def GetNumberOfGenerationsFromBaseType_s(type : str) -> int: 
        """
        None
        """
    def IsA(self,type : str) -> int: 
        """
        None
        """
    @staticmethod
    def IsTypeOf_s(type : str) -> int: 
        """
        None
        """
    def NewInstance(self) -> IVtkTools_SubPolyDataFilter: 
        """
        None
        """
    @staticmethod
    def New_s() -> IVtkTools_SubPolyDataFilter: 
        """
        None
        """
    @staticmethod
    def SafeDownCast_s(o : vtkObjectBase) -> IVtkTools_SubPolyDataFilter: 
        """
        None
        """
    @overload
    def SetData(self,theSet : OCP.IVtk.IVtk_IdTypeMap) -> None: 
        """
        Set ids to be passed through this filter.

        Set ids to be passed through this filter.
        """
    @overload
    def SetData(self,theIds : OCP.IVtk.IVtk_ShapeIdList) -> None: ...
    def SetDoFiltering(self,theDoFiltering : bool) -> None: 
        """
        None
        """
    def SetIdsArrayName(self,theArrayName : str) -> None: 
        """
        Set ids array name.
        """
    pass
class IVtkTools_ShapeDataSource():
    """
    VTK data source for OCC shapes polygonal data.
    """
    def Contains(self,theOccShape : OCP.IVtkOCC.IVtkOCC_Shape) -> bool: 
        """
        Checks if the internal OccShape pointer is the same the argument.
        """
    def FastTransformModeOff(self) -> None: 
        """
        None
        """
    def FastTransformModeOn(self) -> None: 
        """
        None
        """
    def GetId(self) -> int: 
        """
        Returns ID of the shape used as a topological input for this data source.
        """
    def GetNumberOfGenerationsFromBase(self,type : str) -> int: 
        """
        None
        """
    @staticmethod
    def GetNumberOfGenerationsFromBaseType_s(type : str) -> int: 
        """
        None
        """
    def GetShape(self) -> OCP.IVtkOCC.IVtkOCC_Shape: 
        """
        Get the source OCCT shape.
        """
    def IsA(self,type : str) -> int: 
        """
        None
        """
    @staticmethod
    def IsTypeOf_s(type : str) -> int: 
        """
        None
        """
    def NewInstance(self) -> IVtkTools_ShapeDataSource: 
        """
        None
        """
    @staticmethod
    def New_s() -> IVtkTools_ShapeDataSource: 
        """
        None
        """
    @staticmethod
    def SafeDownCast_s(o : vtkObjectBase) -> IVtkTools_ShapeDataSource: 
        """
        None
        """
    def SetShape(self,theOccShape : OCP.IVtkOCC.IVtkOCC_Shape) -> None: 
        """
        Set the source OCCT shape.
        """
    def SubShapeIDs(self) -> Any: 
        """
        Access to the shape's sub-shape ids array
        """
    pass
class IVtkTools_ShapeObject():
    """
    VTK holder class for OCC shapes to pass them through pipelines.
    """
    def GetNumberOfGenerationsFromBase(self,type : str) -> int: 
        """
        None
        """
    @staticmethod
    def GetNumberOfGenerationsFromBaseType_s(type : str) -> int: 
        """
        None
        """
    @staticmethod
    def GetOccShape_s(theActor : vtkActor) -> OCP.IVtkOCC.IVtkOCC_Shape: 
        """
        Get OCC shape from VTK data from actor's information object by key.
        """
    def GetShapeSource(self) -> IVtkTools_ShapeDataSource: 
        """
        OCC shape source getter.
        """
    @staticmethod
    def GetShapeSource_s(theActor : vtkActor) -> Any: 
        """
        Get OCC shape source from VTK data from actor's information object by key.
        """
    def IsA(self,type : str) -> int: 
        """
        None
        """
    @staticmethod
    def IsTypeOf_s(type : str) -> int: 
        """
        None
        """
    def NewInstance(self) -> IVtkTools_ShapeObject: 
        """
        None
        """
    @staticmethod
    def New_s() -> IVtkTools_ShapeObject: 
        """
        None
        """
    @staticmethod
    def SafeDownCast_s(o : vtkObjectBase) -> IVtkTools_ShapeObject: 
        """
        None
        """
    def SetShapeSource(self,theDataSource : IVtkTools_ShapeDataSource) -> None: 
        """
        OCC shape source setter.
        """
    @staticmethod
    @overload
    def SetShapeSource_s(theDataSource : IVtkTools_ShapeDataSource,theActor : vtkActor) -> None: 
        """
        Static method to set OCC shape source to VTK dataset in information object with key.

        Static method to set OCC shape source to VTK actor in information object with key.
        """
    @staticmethod
    @overload
    def SetShapeSource_s(theDataSource : IVtkTools_ShapeDataSource,theData : vtkDataSet) -> None: ...
    @staticmethod
    def getKey_s() -> vtkInformationObjectBaseKey: 
        """
        Static method used by shape selection logic in order to establish a connection from vtkActor to OccShape instance.
        """
    pass
class IVtkTools_ShapePicker():
    """
    VTK picker for OCC shapes with OCC selection algorithm.
    """
    def GetNumberOfGenerationsFromBase(self,type : str) -> int: 
        """
        None
        """
    @staticmethod
    def GetNumberOfGenerationsFromBaseType_s(type : str) -> int: 
        """
        None
        """
    def GetPickedActors(self,theIsAll : bool=False) -> Any: 
        """
        Access to the list of actors picked.
        """
    def GetPickedShapesIds(self,theIsAll : bool=False) -> OCP.IVtk.IVtk_ShapeIdList: 
        """
        Access to the list of top-level shapes picked. If all argument is true, the picker returns the list of all OccShape objects found by the picking algorithm. e.g. all shapes under the mouse cursor. Otherwise, ID of the shape closest to the eye is returned.
        """
    def GetPickedSubShapesIds(self,theId : int,theIsAll : bool=False) -> OCP.IVtk.IVtk_ShapeIdList: 
        """
        Access to the list of sub-shapes ids picked.
        """
    @overload
    def GetSelectionModes(self,theShapeActor : vtkActor) -> OCP.IVtk.IVtk_SelectionModeList: 
        """
        Get activated selection modes for a shape.

        Get activated selection modes for a shape actor.
        """
    @overload
    def GetSelectionModes(self,theShape : OCP.IVtk.IVtk_IShape) -> OCP.IVtk.IVtk_SelectionModeList: ...
    def GetTolerance(self) -> float: 
        """
        Getter for tolerance of picking.
        """
    def IsA(self,type : str) -> int: 
        """
        None
        """
    @staticmethod
    def IsTypeOf_s(type : str) -> int: 
        """
        None
        """
    def NewInstance(self) -> IVtkTools_ShapePicker: 
        """
        None
        """
    @staticmethod
    def New_s() -> IVtkTools_ShapePicker: 
        """
        None
        """
    def RemoveSelectableActor(self,theShapeActor : vtkActor) -> None: 
        """
        Remove selectable object from the picker (from internal maps).
        """
    def RemoveSelectableObject(self,theShape : OCP.IVtk.IVtk_IShape) -> None: 
        """
        Remove selectable object from the picker (from internal maps).
        """
    @staticmethod
    def SafeDownCast_s(o : vtkObjectBase) -> IVtkTools_ShapePicker: 
        """
        None
        """
    def SetAreaSelection(self,theIsOn : bool) -> None: 
        """
        Sets area selection on/off
        """
    def SetRenderer(self,theRenderer : vtkRenderer) -> None: 
        """
        Sets the renderer to be used by OCCT selection algorithm
        """
    @overload
    def SetSelectionMode(self,theShape : OCP.IVtk.IVtk_IShape,theMode : OCP.IVtk.IVtk_SelectionMode,theIsTurnOn : bool=True) -> None: 
        """
        Turn on/off a selection mode for a shape actor.

        Turn on/off a selection mode for a shape actor.

        Sets the current selection mode for all visible shape objects.
        """
    @overload
    def SetSelectionMode(self,theMode : OCP.IVtk.IVtk_SelectionMode,theIsTurnOn : bool=True) -> None: ...
    @overload
    def SetSelectionMode(self,theShapeActor : vtkActor,theMode : OCP.IVtk.IVtk_SelectionMode,theIsTurnOn : bool=True) -> None: ...
    def SetTolerance(self,theTolerance : float) -> None: 
        """
        Setter for tolerance of picking.
        """
    pass
class IVtkTools_DisplayModeFilter(IVtkTools_SubPolyDataFilter):
    """
    Cells filter according to the selected display mode by mesh parts types. This filter is used to get parts of a shape according to different display modes.
    """
    @overload
    def AddData(self,theSet : OCP.IVtk.IVtk_IdTypeMap) -> None: 
        """
        Add ids to be passed through this filter.

        Add ids to be passed through this filter.
        """
    @overload
    def AddData(self,theIds : OCP.IVtk.IVtk_ShapeIdList) -> None: ...
    def Clear(self) -> None: 
        """
        Clear ids set to be passed through this filter.
        """
    def FaceBoundaryDraw(self) -> bool: 
        """
        Returns True if drawing Boundary of faces for shading mode is defined.
        """
    def GetDisplayMode(self) -> OCP.IVtk.IVtk_DisplayMode: 
        """
        Get current display mode.
        """
    def GetNumberOfGenerationsFromBase(self,type : str) -> int: 
        """
        None
        """
    @staticmethod
    def GetNumberOfGenerationsFromBaseType_s(type : str) -> int: 
        """
        None
        """
    def IsA(self,type : str) -> int: 
        """
        None
        """
    def IsSmoothShading(self) -> bool: 
        """
        Returns TRUE if vertex normals should be included for smooth shading within DM_Shading mode or not.
        """
    @staticmethod
    def IsTypeOf_s(type : str) -> int: 
        """
        None
        """
    def MeshTypesForMode(self,theMode : OCP.IVtk.IVtk_DisplayMode) -> OCP.IVtk.IVtk_IdTypeMap: 
        """
        Returns list of displaying mesh element types for the given display mode
        """
    def NewInstance(self) -> IVtkTools_DisplayModeFilter: 
        """
        None
        """
    @staticmethod
    def New_s() -> IVtkTools_DisplayModeFilter: 
        """
        None
        """
    @staticmethod
    def SafeDownCast_s(o : vtkObjectBase) -> IVtkTools_DisplayModeFilter: 
        """
        None
        """
    @overload
    def SetData(self,theSet : OCP.IVtk.IVtk_IdTypeMap) -> None: 
        """
        Set ids to be passed through this filter.

        Set ids to be passed through this filter.
        """
    @overload
    def SetData(self,theIds : OCP.IVtk.IVtk_ShapeIdList) -> None: ...
    def SetDisplayMode(self,aMode : OCP.IVtk.IVtk_DisplayMode) -> None: 
        """
        Set display mode to define cells types to be passed through this filter.
        """
    def SetDisplaySharedVertices(self,doDisplay : bool) -> None: 
        """
        Display or not shared vertices.
        """
    def SetDoFiltering(self,theDoFiltering : bool) -> None: 
        """
        None
        """
    def SetFaceBoundaryDraw(self,theToDraw : bool) -> None: 
        """
        Draw Boundary of faces for shading mode
        """
    def SetIdsArrayName(self,theArrayName : str) -> None: 
        """
        Set ids array name.
        """
    def SetMeshTypesForMode(self,theMode : OCP.IVtk.IVtk_DisplayMode,theMeshTypes : OCP.IVtk.IVtk_IdTypeMap) -> None: 
        """
        Set a list of displaying mesh element types for the given display mode
        """
    def SetSmoothShading(self,theIsSmooth : bool) -> None: 
        """
        Set if vertex normals should be included for smooth shading or not.
        """
    pass
