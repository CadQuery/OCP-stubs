import OCP.RWStepShape
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepShape
import OCP.StepData
import OCP.Interface
__all__  = [
"RWStepShape_RWAdvancedBrepShapeRepresentation",
"RWStepShape_RWAdvancedFace",
"RWStepShape_RWAngularLocation",
"RWStepShape_RWAngularSize",
"RWStepShape_RWBlock",
"RWStepShape_RWBooleanResult",
"RWStepShape_RWBoxDomain",
"RWStepShape_RWBoxedHalfSpace",
"RWStepShape_RWBrepWithVoids",
"RWStepShape_RWClosedShell",
"RWStepShape_RWCompoundShapeRepresentation",
"RWStepShape_RWConnectedEdgeSet",
"RWStepShape_RWConnectedFaceSet",
"RWStepShape_RWConnectedFaceShapeRepresentation",
"RWStepShape_RWConnectedFaceSubSet",
"RWStepShape_RWContextDependentShapeRepresentation",
"RWStepShape_RWCsgShapeRepresentation",
"RWStepShape_RWCsgSolid",
"RWStepShape_RWDefinitionalRepresentationAndShapeRepresentation",
"RWStepShape_RWDimensionalCharacteristicRepresentation",
"RWStepShape_RWDimensionalLocation",
"RWStepShape_RWDimensionalLocationWithPath",
"RWStepShape_RWDimensionalSize",
"RWStepShape_RWDimensionalSizeWithPath",
"RWStepShape_RWEdge",
"RWStepShape_RWEdgeBasedWireframeModel",
"RWStepShape_RWEdgeBasedWireframeShapeRepresentation",
"RWStepShape_RWEdgeCurve",
"RWStepShape_RWEdgeLoop",
"RWStepShape_RWExtrudedAreaSolid",
"RWStepShape_RWExtrudedFaceSolid",
"RWStepShape_RWFace",
"RWStepShape_RWFaceBasedSurfaceModel",
"RWStepShape_RWFaceBound",
"RWStepShape_RWFaceOuterBound",
"RWStepShape_RWFaceSurface",
"RWStepShape_RWFacetedBrep",
"RWStepShape_RWFacetedBrepAndBrepWithVoids",
"RWStepShape_RWFacetedBrepShapeRepresentation",
"RWStepShape_RWGeometricCurveSet",
"RWStepShape_RWGeometricSet",
"RWStepShape_RWGeometricallyBoundedSurfaceShapeRepresentation",
"RWStepShape_RWGeometricallyBoundedWireframeShapeRepresentation",
"RWStepShape_RWHalfSpaceSolid",
"RWStepShape_RWLimitsAndFits",
"RWStepShape_RWLoop",
"RWStepShape_RWLoopAndPath",
"RWStepShape_RWManifoldSolidBrep",
"RWStepShape_RWManifoldSurfaceShapeRepresentation",
"RWStepShape_RWMeasureQualification",
"RWStepShape_RWMeasureRepresentationItemAndQualifiedRepresentationItem",
"RWStepShape_RWNonManifoldSurfaceShapeRepresentation",
"RWStepShape_RWOpenShell",
"RWStepShape_RWOrientedClosedShell",
"RWStepShape_RWOrientedEdge",
"RWStepShape_RWOrientedFace",
"RWStepShape_RWOrientedOpenShell",
"RWStepShape_RWOrientedPath",
"RWStepShape_RWPath",
"RWStepShape_RWPlusMinusTolerance",
"RWStepShape_RWPointRepresentation",
"RWStepShape_RWPolyLoop",
"RWStepShape_RWPrecisionQualifier",
"RWStepShape_RWQualifiedRepresentationItem",
"RWStepShape_RWRevolvedAreaSolid",
"RWStepShape_RWRevolvedFaceSolid",
"RWStepShape_RWRightAngularWedge",
"RWStepShape_RWRightCircularCone",
"RWStepShape_RWRightCircularCylinder",
"RWStepShape_RWSeamEdge",
"RWStepShape_RWShapeDefinitionRepresentation",
"RWStepShape_RWShapeDimensionRepresentation",
"RWStepShape_RWShapeRepresentation",
"RWStepShape_RWShapeRepresentationWithParameters",
"RWStepShape_RWShellBasedSurfaceModel",
"RWStepShape_RWSolidModel",
"RWStepShape_RWSolidReplica",
"RWStepShape_RWSphere",
"RWStepShape_RWSubedge",
"RWStepShape_RWSubface",
"RWStepShape_RWSweptAreaSolid",
"RWStepShape_RWSweptFaceSolid",
"RWStepShape_RWToleranceValue",
"RWStepShape_RWTopologicalRepresentationItem",
"RWStepShape_RWTorus",
"RWStepShape_RWTransitionalShapeRepresentation",
"RWStepShape_RWTypeQualifier",
"RWStepShape_RWValueFormatTypeQualifier",
"RWStepShape_RWVertex",
"RWStepShape_RWVertexLoop",
"RWStepShape_RWVertexPoint"
]
class RWStepShape_RWAdvancedBrepShapeRepresentation():
    """
    Read & Write Module for AdvancedBrepShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_AdvancedBrepShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_AdvancedBrepShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_AdvancedBrepShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWAdvancedFace():
    """
    Read & Write Module for AdvancedFace
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_AdvancedFace) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_AdvancedFace,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_AdvancedFace) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWAngularLocation():
    """
    Read & Write tool for AngularLocation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_AngularLocation) -> Any: 
        """
        Reads AngularLocation
        """
    def Share(self,ent : OCP.StepShape.StepShape_AngularLocation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_AngularLocation) -> None: 
        """
        Writes AngularLocation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWAngularSize():
    """
    Read & Write tool for AngularSize
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_AngularSize) -> Any: 
        """
        Reads AngularSize
        """
    def Share(self,ent : OCP.StepShape.StepShape_AngularSize,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_AngularSize) -> None: 
        """
        Writes AngularSize
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWBlock():
    """
    Read & Write Module for Block
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Block) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_Block,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Block) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWBooleanResult():
    """
    Read & Write Module for BooleanResult
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_BooleanResult) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_BooleanResult,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_BooleanResult) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWBoxDomain():
    """
    Read & Write Module for BoxDomain
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_BoxDomain) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_BoxDomain,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_BoxDomain) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWBoxedHalfSpace():
    """
    Read & Write Module for BoxedHalfSpace
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_BoxedHalfSpace) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_BoxedHalfSpace,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_BoxedHalfSpace) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWBrepWithVoids():
    """
    Read & Write Module for BrepWithVoids
    """
    def Check(self,ent : OCP.StepShape.StepShape_BrepWithVoids,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_BrepWithVoids) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_BrepWithVoids,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_BrepWithVoids) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWClosedShell():
    """
    Read & Write Module for ClosedShell
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ClosedShell) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ClosedShell,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ClosedShell) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWCompoundShapeRepresentation():
    """
    Read & Write tool for CompoundShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_CompoundShapeRepresentation) -> Any: 
        """
        Reads CompoundShapeRepresentation
        """
    def Share(self,ent : OCP.StepShape.StepShape_CompoundShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_CompoundShapeRepresentation) -> None: 
        """
        Writes CompoundShapeRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWConnectedEdgeSet():
    """
    Read & Write tool for ConnectedEdgeSet
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ConnectedEdgeSet) -> Any: 
        """
        Reads ConnectedEdgeSet
        """
    def Share(self,ent : OCP.StepShape.StepShape_ConnectedEdgeSet,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ConnectedEdgeSet) -> None: 
        """
        Writes ConnectedEdgeSet
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWConnectedFaceSet():
    """
    Read & Write Module for ConnectedFaceSet
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ConnectedFaceSet) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ConnectedFaceSet,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ConnectedFaceSet) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWConnectedFaceShapeRepresentation():
    """
    Read & Write tool for ConnectedFaceShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ConnectedFaceShapeRepresentation) -> Any: 
        """
        Reads ConnectedFaceShapeRepresentation
        """
    def Share(self,ent : OCP.StepShape.StepShape_ConnectedFaceShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ConnectedFaceShapeRepresentation) -> None: 
        """
        Writes ConnectedFaceShapeRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWConnectedFaceSubSet():
    """
    Read & Write tool for ConnectedFaceSubSet
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ConnectedFaceSubSet) -> Any: 
        """
        Reads ConnectedFaceSubSet
        """
    def Share(self,ent : OCP.StepShape.StepShape_ConnectedFaceSubSet,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ConnectedFaceSubSet) -> None: 
        """
        Writes ConnectedFaceSubSet
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWContextDependentShapeRepresentation():
    """
    Read & Write Module for ContextDependentShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ContextDependentShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ContextDependentShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ContextDependentShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWCsgShapeRepresentation():
    """
    Read & Write Module for CsgShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_CsgShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_CsgShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_CsgShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWCsgSolid():
    """
    Read & Write Module for CsgSolid
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_CsgSolid) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_CsgSolid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_CsgSolid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWDefinitionalRepresentationAndShapeRepresentation():
    """
    Read & Write Module for ConversionBasedUnitAndLengthUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_DefinitionalRepresentationAndShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_DefinitionalRepresentationAndShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_DefinitionalRepresentationAndShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWDimensionalCharacteristicRepresentation():
    """
    Read & Write tool for DimensionalCharacteristicRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_DimensionalCharacteristicRepresentation) -> Any: 
        """
        Reads DimensionalCharacteristicRepresentation
        """
    def Share(self,ent : OCP.StepShape.StepShape_DimensionalCharacteristicRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_DimensionalCharacteristicRepresentation) -> None: 
        """
        Writes DimensionalCharacteristicRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWDimensionalLocation():
    """
    Read & Write tool for DimensionalLocation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_DimensionalLocation) -> Any: 
        """
        Reads DimensionalLocation
        """
    def Share(self,ent : OCP.StepShape.StepShape_DimensionalLocation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_DimensionalLocation) -> None: 
        """
        Writes DimensionalLocation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWDimensionalLocationWithPath():
    """
    Read & Write tool for DimensionalLocationWithPath
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_DimensionalLocationWithPath) -> Any: 
        """
        Reads DimensionalLocationWithPath
        """
    def Share(self,ent : OCP.StepShape.StepShape_DimensionalLocationWithPath,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_DimensionalLocationWithPath) -> None: 
        """
        Writes DimensionalLocationWithPath
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWDimensionalSize():
    """
    Read & Write tool for DimensionalSize
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_DimensionalSize) -> Any: 
        """
        Reads DimensionalSize
        """
    def Share(self,ent : OCP.StepShape.StepShape_DimensionalSize,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_DimensionalSize) -> None: 
        """
        Writes DimensionalSize
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWDimensionalSizeWithPath():
    """
    Read & Write tool for DimensionalSizeWithPath
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_DimensionalSizeWithPath) -> Any: 
        """
        Reads DimensionalSizeWithPath
        """
    def Share(self,ent : OCP.StepShape.StepShape_DimensionalSizeWithPath,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_DimensionalSizeWithPath) -> None: 
        """
        Writes DimensionalSizeWithPath
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWEdge():
    """
    Read & Write Module for Edge
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Edge) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_Edge,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Edge) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWEdgeBasedWireframeModel():
    """
    Read & Write tool for EdgeBasedWireframeModel
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_EdgeBasedWireframeModel) -> Any: 
        """
        Reads EdgeBasedWireframeModel
        """
    def Share(self,ent : OCP.StepShape.StepShape_EdgeBasedWireframeModel,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_EdgeBasedWireframeModel) -> None: 
        """
        Writes EdgeBasedWireframeModel
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWEdgeBasedWireframeShapeRepresentation():
    """
    Read & Write tool for EdgeBasedWireframeShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_EdgeBasedWireframeShapeRepresentation) -> Any: 
        """
        Reads EdgeBasedWireframeShapeRepresentation
        """
    def Share(self,ent : OCP.StepShape.StepShape_EdgeBasedWireframeShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_EdgeBasedWireframeShapeRepresentation) -> None: 
        """
        Writes EdgeBasedWireframeShapeRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWEdgeCurve():
    """
    Read & Write Module for EdgeCurve Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepShape.StepShape_EdgeCurve,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_EdgeCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_EdgeCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_EdgeCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWEdgeLoop():
    """
    Read & Write Module for EdgeLoop Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepShape.StepShape_EdgeLoop,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_EdgeLoop) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_EdgeLoop,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_EdgeLoop) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWExtrudedAreaSolid():
    """
    Read & Write Module for ExtrudedAreaSolid
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ExtrudedAreaSolid) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ExtrudedAreaSolid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ExtrudedAreaSolid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWExtrudedFaceSolid():
    """
    Read & Write Module for ExtrudedFaceSolid
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ExtrudedFaceSolid) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ExtrudedFaceSolid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ExtrudedFaceSolid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWFace():
    """
    Read & Write Module for Face
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Face) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_Face,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Face) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWFaceBasedSurfaceModel():
    """
    Read & Write tool for FaceBasedSurfaceModel
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_FaceBasedSurfaceModel) -> Any: 
        """
        Reads FaceBasedSurfaceModel
        """
    def Share(self,ent : OCP.StepShape.StepShape_FaceBasedSurfaceModel,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_FaceBasedSurfaceModel) -> None: 
        """
        Writes FaceBasedSurfaceModel
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWFaceBound():
    """
    Read & Write Module for FaceBound Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepShape.StepShape_FaceBound,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_FaceBound) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_FaceBound,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_FaceBound) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWFaceOuterBound():
    """
    Read & Write Module for FaceOuterBound
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_FaceOuterBound) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_FaceOuterBound,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_FaceOuterBound) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWFaceSurface():
    """
    Read & Write Module for FaceSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_FaceSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_FaceSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_FaceSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWFacetedBrep():
    """
    Read & Write Module for FacetedBrep
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_FacetedBrep) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_FacetedBrep,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_FacetedBrep) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWFacetedBrepAndBrepWithVoids():
    """
    Read & Write Module for FacetedBrepAndBrepWithVoids
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_FacetedBrepAndBrepWithVoids) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_FacetedBrepAndBrepWithVoids,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_FacetedBrepAndBrepWithVoids) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWFacetedBrepShapeRepresentation():
    """
    Read & Write Module for FacetedBrepShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_FacetedBrepShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_FacetedBrepShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_FacetedBrepShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWGeometricCurveSet():
    """
    Read & Write Module for GeometricCurveSet
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_GeometricCurveSet) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_GeometricCurveSet,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_GeometricCurveSet) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWGeometricSet():
    """
    Read & Write Module for GeometricSet
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_GeometricSet) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_GeometricSet,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_GeometricSet) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWGeometricallyBoundedSurfaceShapeRepresentation():
    """
    Read & Write Module for GeometricallyBoundedSurfaceShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_GeometricallyBoundedSurfaceShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_GeometricallyBoundedSurfaceShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_GeometricallyBoundedSurfaceShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWGeometricallyBoundedWireframeShapeRepresentation():
    """
    Read & Write Module for GeometricallyBoundedWireframeShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_GeometricallyBoundedWireframeShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_GeometricallyBoundedWireframeShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_GeometricallyBoundedWireframeShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWHalfSpaceSolid():
    """
    Read & Write Module for HalfSpaceSolid
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_HalfSpaceSolid) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_HalfSpaceSolid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_HalfSpaceSolid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWLimitsAndFits():
    """
    Read & Write Module for LimitsAndFits
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_LimitsAndFits) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_LimitsAndFits) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWLoop():
    """
    Read & Write Module for Loop
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Loop) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Loop) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWLoopAndPath():
    """
    Read & Write Module for LoopAndPath
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_LoopAndPath) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_LoopAndPath,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_LoopAndPath) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWManifoldSolidBrep():
    """
    Read & Write Module for ManifoldSolidBrep
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ManifoldSolidBrep) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ManifoldSolidBrep,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ManifoldSolidBrep) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWManifoldSurfaceShapeRepresentation():
    """
    Read & Write Module for ManifoldSurfaceShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ManifoldSurfaceShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ManifoldSurfaceShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ManifoldSurfaceShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWMeasureQualification():
    """
    Read & Write Module for MeasureQualification
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_MeasureQualification) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_MeasureQualification,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_MeasureQualification) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWMeasureRepresentationItemAndQualifiedRepresentationItem():
    """
    Read & Write Module for MeasureRepresentationItemAndQualifiedRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWNonManifoldSurfaceShapeRepresentation():
    """
    Read & Write tool for NonManifoldSurfaceShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_NonManifoldSurfaceShapeRepresentation) -> Any: 
        """
        Reads NonManifoldSurfaceShapeRepresentation
        """
    def Share(self,ent : OCP.StepShape.StepShape_NonManifoldSurfaceShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_NonManifoldSurfaceShapeRepresentation) -> None: 
        """
        Writes NonManifoldSurfaceShapeRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWOpenShell():
    """
    Read & Write Module for OpenShell
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_OpenShell) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_OpenShell,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_OpenShell) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWOrientedClosedShell():
    """
    Read & Write Module for OrientedClosedShell
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_OrientedClosedShell) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_OrientedClosedShell,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_OrientedClosedShell) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWOrientedEdge():
    """
    Read & Write Module for OrientedEdge
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_OrientedEdge) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_OrientedEdge,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_OrientedEdge) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWOrientedFace():
    """
    Read & Write Module for OrientedFace
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_OrientedFace) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_OrientedFace,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_OrientedFace) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWOrientedOpenShell():
    """
    Read & Write Module for OrientedOpenShell
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_OrientedOpenShell) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_OrientedOpenShell,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_OrientedOpenShell) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWOrientedPath():
    """
    Read & Write Module for OrientedPath
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_OrientedPath) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_OrientedPath,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_OrientedPath) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWPath():
    """
    Read & Write Module for Path
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Path) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_Path,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Path) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWPlusMinusTolerance():
    """
    Read & Write Module for PlusMinusTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_PlusMinusTolerance) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_PlusMinusTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_PlusMinusTolerance) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWPointRepresentation():
    """
    Read & Write tool for PointRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_PointRepresentation) -> Any: 
        """
        Reads PointRepresentation
        """
    def Share(self,ent : OCP.StepShape.StepShape_PointRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_PointRepresentation) -> None: 
        """
        Writes PointRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWPolyLoop():
    """
    Read & Write Module for PolyLoop
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_PolyLoop) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_PolyLoop,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_PolyLoop) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWPrecisionQualifier():
    """
    Read & Write Module for PrecisionQualifier
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_PrecisionQualifier) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_PrecisionQualifier) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWQualifiedRepresentationItem():
    """
    Read & Write Module for QualifiedRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_QualifiedRepresentationItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_QualifiedRepresentationItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_QualifiedRepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWRevolvedAreaSolid():
    """
    Read & Write Module for RevolvedAreaSolid
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_RevolvedAreaSolid) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_RevolvedAreaSolid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_RevolvedAreaSolid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWRevolvedFaceSolid():
    """
    None
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_RevolvedFaceSolid) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_RevolvedFaceSolid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_RevolvedFaceSolid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWRightAngularWedge():
    """
    Read & Write Module for RightAngularWedge
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_RightAngularWedge) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_RightAngularWedge,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_RightAngularWedge) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWRightCircularCone():
    """
    Read & Write Module for RightCircularCone
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_RightCircularCone) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_RightCircularCone,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_RightCircularCone) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWRightCircularCylinder():
    """
    Read & Write Module for RightCircularCylinder
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_RightCircularCylinder) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_RightCircularCylinder,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_RightCircularCylinder) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWSeamEdge():
    """
    Read & Write tool for SeamEdge
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_SeamEdge) -> Any: 
        """
        Reads SeamEdge
        """
    def Share(self,ent : OCP.StepShape.StepShape_SeamEdge,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_SeamEdge) -> None: 
        """
        Writes SeamEdge
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWShapeDefinitionRepresentation():
    """
    Read & Write tool for ShapeDefinitionRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ShapeDefinitionRepresentation) -> Any: 
        """
        Reads ShapeDefinitionRepresentation
        """
    def Share(self,ent : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ShapeDefinitionRepresentation) -> None: 
        """
        Writes ShapeDefinitionRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWShapeDimensionRepresentation():
    """
    Read & Write tool for ShapeDimensionRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ShapeDimensionRepresentation) -> Any: 
        """
        Reads ShapeDimensionRepresentation
        """
    def Share(self,ent : OCP.StepShape.StepShape_ShapeDimensionRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ShapeDimensionRepresentation) -> None: 
        """
        Writes ShapeDimensionRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWShapeRepresentation():
    """
    Read & Write Module for ShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWShapeRepresentationWithParameters():
    """
    Read & Write tool for ShapeRepresentationWithParameters
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ShapeRepresentationWithParameters) -> Any: 
        """
        Reads ShapeRepresentationWithParameters
        """
    def Share(self,ent : OCP.StepShape.StepShape_ShapeRepresentationWithParameters,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ShapeRepresentationWithParameters) -> None: 
        """
        Writes ShapeRepresentationWithParameters
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWShellBasedSurfaceModel():
    """
    Read & Write Module for ShellBasedSurfaceModel
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ShellBasedSurfaceModel) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ShellBasedSurfaceModel,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ShellBasedSurfaceModel) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWSolidModel():
    """
    Read & Write Module for SolidModel
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_SolidModel) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_SolidModel) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWSolidReplica():
    """
    Read & Write Module for SolidReplica
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_SolidReplica) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_SolidReplica,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_SolidReplica) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWSphere():
    """
    Read & Write Module for Sphere
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Sphere) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_Sphere,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Sphere) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWSubedge():
    """
    Read & Write tool for Subedge
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Subedge) -> Any: 
        """
        Reads Subedge
        """
    def Share(self,ent : OCP.StepShape.StepShape_Subedge,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Subedge) -> None: 
        """
        Writes Subedge
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWSubface():
    """
    Read & Write tool for Subface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Subface) -> Any: 
        """
        Reads Subface
        """
    def Share(self,ent : OCP.StepShape.StepShape_Subface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Subface) -> None: 
        """
        Writes Subface
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWSweptAreaSolid():
    """
    Read & Write Module for SweptAreaSolid
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_SweptAreaSolid) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_SweptAreaSolid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_SweptAreaSolid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWSweptFaceSolid():
    """
    Read & Write Module for SweptFaceSolid
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_SweptFaceSolid) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_SweptFaceSolid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_SweptFaceSolid) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWToleranceValue():
    """
    Read & Write Module for ToleranceValue
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ToleranceValue) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_ToleranceValue,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ToleranceValue) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWTopologicalRepresentationItem():
    """
    Read & Write Module for TopologicalRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWTorus():
    """
    Read & Write Module for Torus
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Torus) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_Torus,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Torus) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWTransitionalShapeRepresentation():
    """
    Read & Write Module for TransitionalShapeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_TransitionalShapeRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_TransitionalShapeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_TransitionalShapeRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWTypeQualifier():
    """
    Read & Write Module for TypeQualifier
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_TypeQualifier) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_TypeQualifier) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWValueFormatTypeQualifier():
    """
    Read & Write tool for ValueFormatTypeQualifier
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_ValueFormatTypeQualifier) -> Any: 
        """
        Reads ValueFormatTypeQualifier
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_ValueFormatTypeQualifier) -> None: 
        """
        Writes ValueFormatTypeQualifier
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWVertex():
    """
    Read & Write Module for Vertex
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_Vertex) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_Vertex) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWVertexLoop():
    """
    Read & Write Module for VertexLoop
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_VertexLoop) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_VertexLoop,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_VertexLoop) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepShape_RWVertexPoint():
    """
    Read & Write Module for VertexPoint
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepShape.StepShape_VertexPoint) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepShape.StepShape_VertexPoint,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepShape.StepShape_VertexPoint) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
