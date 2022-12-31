import OCP.RWStepVisual
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepVisual
import OCP.StepData
import OCP.Interface
__all__  = [
"RWStepVisual_RWAnnotationCurveOccurrence",
"RWStepVisual_RWAnnotationCurveOccurrenceAndGeomReprItem",
"RWStepVisual_RWAnnotationFillArea",
"RWStepVisual_RWAnnotationFillAreaOccurrence",
"RWStepVisual_RWAnnotationOccurrence",
"RWStepVisual_RWAnnotationPlane",
"RWStepVisual_RWAreaInSet",
"RWStepVisual_RWBackgroundColour",
"RWStepVisual_RWCameraImage",
"RWStepVisual_RWCameraModel",
"RWStepVisual_RWCameraModelD2",
"RWStepVisual_RWCameraModelD3",
"RWStepVisual_RWCameraModelD3MultiClipping",
"RWStepVisual_RWCameraModelD3MultiClippingIntersection",
"RWStepVisual_RWCameraModelD3MultiClippingUnion",
"RWStepVisual_RWCameraUsage",
"RWStepVisual_RWCharacterizedObjAndRepresentationAndDraughtingModel",
"RWStepVisual_RWColour",
"RWStepVisual_RWColourRgb",
"RWStepVisual_RWColourSpecification",
"RWStepVisual_RWComplexTriangulatedFace",
"RWStepVisual_RWComplexTriangulatedSurfaceSet",
"RWStepVisual_RWCompositeText",
"RWStepVisual_RWCompositeTextWithExtent",
"RWStepVisual_RWContextDependentInvisibility",
"RWStepVisual_RWContextDependentOverRidingStyledItem",
"RWStepVisual_RWCoordinatesList",
"RWStepVisual_RWCubicBezierTessellatedEdge",
"RWStepVisual_RWCubicBezierTriangulatedFace",
"RWStepVisual_RWCurveStyle",
"RWStepVisual_RWCurveStyleFont",
"RWStepVisual_RWCurveStyleFontPattern",
"RWStepVisual_RWDraughtingCallout",
"RWStepVisual_RWDraughtingModel",
"RWStepVisual_RWDraughtingPreDefinedColour",
"RWStepVisual_RWDraughtingPreDefinedCurveFont",
"RWStepVisual_RWExternallyDefinedCurveFont",
"RWStepVisual_RWFillAreaStyle",
"RWStepVisual_RWFillAreaStyleColour",
"RWStepVisual_RWInvisibility",
"RWStepVisual_RWMechanicalDesignGeometricPresentationArea",
"RWStepVisual_RWMechanicalDesignGeometricPresentationRepresentation",
"RWStepVisual_RWOverRidingStyledItem",
"RWStepVisual_RWPlanarBox",
"RWStepVisual_RWPlanarExtent",
"RWStepVisual_RWPointStyle",
"RWStepVisual_RWPreDefinedColour",
"RWStepVisual_RWPreDefinedCurveFont",
"RWStepVisual_RWPreDefinedItem",
"RWStepVisual_RWPresentationArea",
"RWStepVisual_RWPresentationLayerAssignment",
"RWStepVisual_RWPresentationLayerUsage",
"RWStepVisual_RWPresentationRepresentation",
"RWStepVisual_RWPresentationSet",
"RWStepVisual_RWPresentationSize",
"RWStepVisual_RWPresentationStyleAssignment",
"RWStepVisual_RWPresentationStyleByContext",
"RWStepVisual_RWPresentationView",
"RWStepVisual_RWPresentedItemRepresentation",
"RWStepVisual_RWRepositionedTessellatedGeometricSet",
"RWStepVisual_RWRepositionedTessellatedItem",
"RWStepVisual_RWStyledItem",
"RWStepVisual_RWSurfaceSideStyle",
"RWStepVisual_RWSurfaceStyleBoundary",
"RWStepVisual_RWSurfaceStyleControlGrid",
"RWStepVisual_RWSurfaceStyleFillArea",
"RWStepVisual_RWSurfaceStyleParameterLine",
"RWStepVisual_RWSurfaceStyleReflectanceAmbient",
"RWStepVisual_RWSurfaceStyleRendering",
"RWStepVisual_RWSurfaceStyleRenderingWithProperties",
"RWStepVisual_RWSurfaceStyleSegmentationCurve",
"RWStepVisual_RWSurfaceStyleSilhouette",
"RWStepVisual_RWSurfaceStyleTransparent",
"RWStepVisual_RWSurfaceStyleUsage",
"RWStepVisual_RWTemplate",
"RWStepVisual_RWTemplateInstance",
"RWStepVisual_RWTessellatedAnnotationOccurrence",
"RWStepVisual_RWTessellatedConnectingEdge",
"RWStepVisual_RWTessellatedCurveSet",
"RWStepVisual_RWTessellatedEdge",
"RWStepVisual_RWTessellatedGeometricSet",
"RWStepVisual_RWTessellatedItem",
"RWStepVisual_RWTessellatedPointSet",
"RWStepVisual_RWTessellatedShapeRepresentation",
"RWStepVisual_RWTessellatedShapeRepresentationWithAccuracyParameters",
"RWStepVisual_RWTessellatedShell",
"RWStepVisual_RWTessellatedSolid",
"RWStepVisual_RWTessellatedStructuredItem",
"RWStepVisual_RWTessellatedVertex",
"RWStepVisual_RWTessellatedWire",
"RWStepVisual_RWTextLiteral",
"RWStepVisual_RWTextStyle",
"RWStepVisual_RWTextStyleForDefinedFont",
"RWStepVisual_RWTextStyleWithBoxCharacteristics",
"RWStepVisual_RWTriangulatedFace",
"RWStepVisual_RWViewVolume"
]
class RWStepVisual_RWAnnotationCurveOccurrence():
    """
    Read & Write Module for AnnotationCurveOccurrence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_AnnotationCurveOccurrence) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_AnnotationCurveOccurrence,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_AnnotationCurveOccurrence) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWAnnotationCurveOccurrenceAndGeomReprItem():
    """
    Read & Write Module for StepVisual_AnnotationCurveOccurrenceAndGeomReprItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_AnnotationCurveOccurrenceAndGeomReprItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_AnnotationCurveOccurrenceAndGeomReprItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_AnnotationCurveOccurrenceAndGeomReprItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWAnnotationFillArea():
    """
    Read & Write Module for AnnotationFillArea
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_AnnotationFillArea) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_AnnotationFillArea,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_AnnotationFillArea) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWAnnotationFillAreaOccurrence():
    """
    Read & Write Module for AnnotationFillAreaOccurrence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_AnnotationFillAreaOccurrence) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_AnnotationFillAreaOccurrence,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_AnnotationFillAreaOccurrence) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWAnnotationOccurrence():
    """
    Read & Write Module for AnnotationOccurrence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_AnnotationOccurrence) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_AnnotationOccurrence,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_AnnotationOccurrence) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWAnnotationPlane():
    """
    Read & Write Module for AnnotationPlane
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_AnnotationPlane) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_AnnotationPlane,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_AnnotationPlane) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWAreaInSet():
    """
    Read & Write Module for AreaInSet
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_AreaInSet) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_AreaInSet,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_AreaInSet) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWBackgroundColour():
    """
    Read & Write Module for BackgroundColour
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_BackgroundColour) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_BackgroundColour,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_BackgroundColour) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCameraImage():
    """
    Read & Write Module for CameraImage
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CameraImage) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CameraImage,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CameraImage) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCameraModel():
    """
    Read & Write Module for CameraModel
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CameraModel) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CameraModel) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCameraModelD2():
    """
    Read & Write Module for CameraModelD2
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CameraModelD2) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CameraModelD2,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CameraModelD2) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCameraModelD3():
    """
    Read & Write Module for CameraModelD3
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CameraModelD3) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CameraModelD3,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CameraModelD3) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCameraModelD3MultiClipping():
    """
    Read & Write Module for CameraModelD3MultiClipping
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CameraModelD3MultiClipping) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CameraModelD3MultiClipping,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CameraModelD3MultiClipping) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCameraModelD3MultiClippingIntersection():
    """
    Read & Write Module for CameraModelD3MultiClippingIntersection
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CameraModelD3MultiClippingIntersection) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CameraModelD3MultiClippingIntersection,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CameraModelD3MultiClippingIntersection) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCameraModelD3MultiClippingUnion():
    """
    Read & Write Module for CameraModelD3MultiClippingUnion
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CameraModelD3MultiClippingUnion) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CameraModelD3MultiClippingUnion,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CameraModelD3MultiClippingUnion) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCameraUsage():
    """
    Read & Write Module for CameraUsage
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CameraUsage) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CameraUsage,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CameraUsage) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCharacterizedObjAndRepresentationAndDraughtingModel():
    """
    Read & Write Module for complex STEP entity Characterized_Object & Characterized_Representation & Draughting_Model & Representation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CharacterizedObjAndRepresentationAndDraughtingModel) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CharacterizedObjAndRepresentationAndDraughtingModel,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CharacterizedObjAndRepresentationAndDraughtingModel) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWColour():
    """
    Read & Write Module for Colour
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_Colour) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_Colour) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWColourRgb():
    """
    Read & Write Module for ColourRgb
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_ColourRgb) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_ColourRgb) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWColourSpecification():
    """
    Read & Write Module for ColourSpecification
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_ColourSpecification) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_ColourSpecification) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWComplexTriangulatedFace():
    """
    Read & Write tool for ComplexTriangulatedFace
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_ComplexTriangulatedFace) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_ComplexTriangulatedFace,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_ComplexTriangulatedFace) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWComplexTriangulatedSurfaceSet():
    """
    Read & Write tool for ComplexTriangulatedSurfaceSet
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_ComplexTriangulatedSurfaceSet) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_ComplexTriangulatedSurfaceSet,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_ComplexTriangulatedSurfaceSet) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCompositeText():
    """
    Read & Write Module for CompositeText
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CompositeText) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CompositeText,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CompositeText) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCompositeTextWithExtent():
    """
    Read & Write Module for CompositeTextWithExtent
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CompositeTextWithExtent) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CompositeTextWithExtent,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CompositeTextWithExtent) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWContextDependentInvisibility():
    """
    Read & Write Module for ContextDependentInvisibility
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_ContextDependentInvisibility) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_ContextDependentInvisibility,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_ContextDependentInvisibility) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWContextDependentOverRidingStyledItem():
    """
    Read & Write Module for ContextDependentOverRidingStyledItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_ContextDependentOverRidingStyledItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_ContextDependentOverRidingStyledItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_ContextDependentOverRidingStyledItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCoordinatesList():
    """
    Read & Write Module for AnnotationOccurrence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CoordinatesList) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CoordinatesList) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCubicBezierTessellatedEdge():
    """
    Read & Write tool for CubicBezierTessellatedEdge
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_CubicBezierTessellatedEdge) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_CubicBezierTessellatedEdge,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_CubicBezierTessellatedEdge) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCubicBezierTriangulatedFace():
    """
    Read & Write tool for CubicBezierTriangulatedFace
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_CubicBezierTriangulatedFace) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_CubicBezierTriangulatedFace,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_CubicBezierTriangulatedFace) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCurveStyle():
    """
    Read & Write Module for CurveStyle
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CurveStyle) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CurveStyle,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CurveStyle) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCurveStyleFont():
    """
    Read & Write Module for CurveStyleFont
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CurveStyleFont) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_CurveStyleFont,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CurveStyleFont) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWCurveStyleFontPattern():
    """
    Read & Write Module for CurveStyleFontPattern
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_CurveStyleFontPattern) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_CurveStyleFontPattern) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWDraughtingCallout():
    """
    Read & Write Module for DraughtingCallout
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_DraughtingCallout) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_DraughtingCallout,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_DraughtingCallout) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWDraughtingModel():
    """
    Read & Write tool for DraughtingModel
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_DraughtingModel) -> Any: 
        """
        Reads DraughtingModel
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_DraughtingModel,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_DraughtingModel) -> None: 
        """
        Writes DraughtingModel
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWDraughtingPreDefinedColour():
    """
    Read & Write Module for DraughtingPreDefinedColour
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_DraughtingPreDefinedColour) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_DraughtingPreDefinedColour) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWDraughtingPreDefinedCurveFont():
    """
    Read & Write Module for DraughtingPreDefinedCurveFont
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_DraughtingPreDefinedCurveFont) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_DraughtingPreDefinedCurveFont) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWExternallyDefinedCurveFont():
    """
    Read & Write tool for ExternallyDefinedCurveFont
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_ExternallyDefinedCurveFont) -> Any: 
        """
        Reads ExternallyDefinedCurveFont
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_ExternallyDefinedCurveFont,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_ExternallyDefinedCurveFont) -> None: 
        """
        Writes ExternallyDefinedCurveFont
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWFillAreaStyle():
    """
    Read & Write Module for FillAreaStyle
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_FillAreaStyle) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_FillAreaStyle,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_FillAreaStyle) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWFillAreaStyleColour():
    """
    Read & Write Module for FillAreaStyleColour
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_FillAreaStyleColour) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_FillAreaStyleColour,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_FillAreaStyleColour) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWInvisibility():
    """
    Read & Write Module for Invisibility
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_Invisibility) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_Invisibility,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_Invisibility) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWMechanicalDesignGeometricPresentationArea():
    """
    Read & Write Module for MechanicalDesignGeometricPresentationArea
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationArea) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationArea,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationArea) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWMechanicalDesignGeometricPresentationRepresentation():
    """
    Read & Write Module for MechanicalDesignGeometricPresentationRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWOverRidingStyledItem():
    """
    Read & Write Module for OverRidingStyledItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_OverRidingStyledItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_OverRidingStyledItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_OverRidingStyledItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPlanarBox():
    """
    Read & Write Module for PlanarBox
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PlanarBox) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PlanarBox,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PlanarBox) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPlanarExtent():
    """
    Read & Write Module for PlanarExtent
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PlanarExtent) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PlanarExtent) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPointStyle():
    """
    Read & Write Module for PointStyle
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PointStyle) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PointStyle,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PointStyle) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPreDefinedColour():
    """
    Read & Write Module for PreDefinedColour
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PreDefinedColour) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PreDefinedColour) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPreDefinedCurveFont():
    """
    Read & Write Module for PreDefinedCurveFont
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PreDefinedCurveFont) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PreDefinedCurveFont) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPreDefinedItem():
    """
    Read & Write Module for PreDefinedItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PreDefinedItem) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PreDefinedItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentationArea():
    """
    Read & Write Module for PresentationArea
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentationArea) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PresentationArea,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentationArea) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentationLayerAssignment():
    """
    Read & Write Module for PresentationLayerAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentationLayerAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PresentationLayerAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentationLayerAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentationLayerUsage():
    """
    Read & Write Module for PresentationLayerUsage
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentationLayerUsage) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PresentationLayerUsage,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentationLayerUsage) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentationRepresentation():
    """
    Read & Write Module for PresentationRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentationRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PresentationRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentationRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentationSet():
    """
    Read & Write Module for PresentationSet
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentationSet) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentationSet) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentationSize():
    """
    Read & Write Module for PresentationSize
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentationSize) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PresentationSize,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentationSize) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentationStyleAssignment():
    """
    Read & Write Module for PresentationStyleAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentationStyleAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PresentationStyleAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentationStyleAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentationStyleByContext():
    """
    Read & Write Module for PresentationStyleByContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentationStyleByContext) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PresentationStyleByContext,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentationStyleByContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentationView():
    """
    Read & Write Module for PresentationView
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentationView) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PresentationView,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentationView) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWPresentedItemRepresentation():
    """
    Read & Write Module for PresentedItemRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_PresentedItemRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_PresentedItemRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_PresentedItemRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWRepositionedTessellatedGeometricSet():
    """
    Read & Write tool for complex RepositionedTessellatedGeometricSet
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theAch : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_RepositionedTessellatedGeometricSet) -> Any: 
        """
        Reads RepositionedTessellatedGeometricSet
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_RepositionedTessellatedGeometricSet,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_RepositionedTessellatedGeometricSet) -> None: 
        """
        Writes RepositionedTessellatedGeometricSet
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWRepositionedTessellatedItem():
    """
    Read & Write tool for RepositionedTessellatedItem
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theAch : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_RepositionedTessellatedItem) -> Any: 
        """
        Reads RepositionedTessellatedItem
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_RepositionedTessellatedItem) -> None: 
        """
        Writes RepositionedTessellatedItem
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWStyledItem():
    """
    Read & Write Module for StyledItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_StyledItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_StyledItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_StyledItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceSideStyle():
    """
    Read & Write Module for SurfaceSideStyle
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceSideStyle) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceSideStyle,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceSideStyle) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleBoundary():
    """
    Read & Write Module for SurfaceStyleBoundary
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleBoundary) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleBoundary,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleBoundary) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleControlGrid():
    """
    Read & Write Module for SurfaceStyleControlGrid
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleControlGrid) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleControlGrid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleControlGrid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleFillArea():
    """
    Read & Write Module for SurfaceStyleFillArea
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleFillArea) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleFillArea,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleFillArea) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleParameterLine():
    """
    Read & Write Module for SurfaceStyleParameterLine
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleParameterLine) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleParameterLine,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleParameterLine) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleReflectanceAmbient():
    """
    Read & Write tool for SurfaceStyleReflectanceAmbient
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleReflectanceAmbient) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleReflectanceAmbient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleReflectanceAmbient) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleRendering():
    """
    Read & Write tool for SurfaceStyleRendering
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleRendering) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleRendering,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleRendering) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleRenderingWithProperties():
    """
    Read & Write tool for SurfaceStyleRenderingWithProperties
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleRenderingWithProperties) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleRenderingWithProperties,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleRenderingWithProperties) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleSegmentationCurve():
    """
    Read & Write Module for SurfaceStyleSegmentationCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleSegmentationCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleSegmentationCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleSegmentationCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleSilhouette():
    """
    Read & Write Module for SurfaceStyleSilhouette
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleSilhouette) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleSilhouette,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleSilhouette) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleTransparent():
    """
    Read & Write tool for SurfaceStyleTransparent
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleTransparent) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleTransparent,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleTransparent) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWSurfaceStyleUsage():
    """
    Read & Write Module for SurfaceStyleUsage
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_SurfaceStyleUsage) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_SurfaceStyleUsage,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_SurfaceStyleUsage) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTemplate():
    """
    Read & Write Module for Template
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_Template) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_Template,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_Template) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTemplateInstance():
    """
    Read & Write Module for TemplateInstance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_TemplateInstance) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_TemplateInstance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_TemplateInstance) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedAnnotationOccurrence():
    """
    Read & Write Module for AnnotationOccurrence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_TessellatedAnnotationOccurrence) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_TessellatedAnnotationOccurrence,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_TessellatedAnnotationOccurrence) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedConnectingEdge():
    """
    Read & Write tool for TessellatedConnectingEdge
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedConnectingEdge) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedConnectingEdge,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedConnectingEdge) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedCurveSet():
    """
    Read & Write Module for AnnotationOccurrence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_TessellatedCurveSet) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_TessellatedCurveSet,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_TessellatedCurveSet) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedEdge():
    """
    Read & Write tool for TessellatedEdge
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedEdge) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedEdge,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedEdge) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedGeometricSet():
    """
    Read & Write Module for AnnotationOccurrence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_TessellatedGeometricSet) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_TessellatedGeometricSet,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_TessellatedGeometricSet) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedItem():
    """
    Read & Write Module for AnnotationOccurrence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_TessellatedItem) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_TessellatedItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedPointSet():
    """
    Read & Write tool for TessellatedPointSet
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedPointSet) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedPointSet,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedPointSet) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedShapeRepresentation():
    """
    Read & Write tool for TessellatedShapeRepresentation
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedShapeRepresentation,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedShapeRepresentationWithAccuracyParameters():
    """
    Read & Write tool for TessellatedShapeRepresentationWithAccuracyParameters
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedShapeRepresentationWithAccuracyParameters) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedShapeRepresentationWithAccuracyParameters,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedShapeRepresentationWithAccuracyParameters) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedShell():
    """
    Read & Write tool for TessellatedShell
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedShell) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedShell,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedShell) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedSolid():
    """
    Read & Write tool for TessellatedSolid
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedSolid) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedSolid,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedSolid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedStructuredItem():
    """
    Read & Write tool for TessellatedStructuredItem
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedStructuredItem) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedStructuredItem,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedStructuredItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedVertex():
    """
    Read & Write tool for TessellatedVertex
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedVertex) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedVertex,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedVertex) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTessellatedWire():
    """
    Read & Write tool for TessellatedWire
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TessellatedWire) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TessellatedWire,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TessellatedWire) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTextLiteral():
    """
    Read & Write Module for TextLiteral
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_TextLiteral) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_TextLiteral,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_TextLiteral) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTextStyle():
    """
    Read & Write Module for TextStyle
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_TextStyle) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_TextStyle,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_TextStyle) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTextStyleForDefinedFont():
    """
    Read & Write Module for TextStyleForDefinedFont
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_TextStyleForDefinedFont) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_TextStyleForDefinedFont,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_TextStyleForDefinedFont) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTextStyleWithBoxCharacteristics():
    """
    Read & Write Module for TextStyleWithBoxCharacteristics
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_TextStyleWithBoxCharacteristics) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_TextStyleWithBoxCharacteristics,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_TextStyleWithBoxCharacteristics) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWTriangulatedFace():
    """
    Read & Write tool for TriangulatedFace
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theCheck : OCP.Interface.Interface_Check,theEnt : OCP.StepVisual.StepVisual_TriangulatedFace) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepVisual.StepVisual_TriangulatedFace,theIter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepVisual.StepVisual_TriangulatedFace) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepVisual_RWViewVolume():
    """
    Read & Write Module for ViewVolume
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepVisual.StepVisual_ViewVolume) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepVisual.StepVisual_ViewVolume,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepVisual.StepVisual_ViewVolume) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
