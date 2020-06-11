import OCP.RWStepRepr
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepData
import OCP.StepRepr
import OCP.Interface
__all__  = [
"RWStepRepr_RWAllAroundShapeAspect",
"RWStepRepr_RWApex",
"RWStepRepr_RWAssemblyComponentUsage",
"RWStepRepr_RWAssemblyComponentUsageSubstitute",
"RWStepRepr_RWBetweenShapeAspect",
"RWStepRepr_RWCentreOfSymmetry",
"RWStepRepr_RWCharacterizedRepresentation",
"RWStepRepr_RWCompGroupShAspAndCompShAspAndDatumFeatAndShAsp",
"RWStepRepr_RWCompShAspAndDatumFeatAndShAsp",
"RWStepRepr_RWCompositeGroupShapeAspect",
"RWStepRepr_RWCompositeShapeAspect",
"RWStepRepr_RWCompoundRepresentationItem",
"RWStepRepr_RWConfigurationDesign",
"RWStepRepr_RWConfigurationEffectivity",
"RWStepRepr_RWConfigurationItem",
"RWStepRepr_RWConstructiveGeometryRepresentation",
"RWStepRepr_RWConstructiveGeometryRepresentationRelationship",
"RWStepRepr_RWContinuosShapeAspect",
"RWStepRepr_RWDataEnvironment",
"RWStepRepr_RWDefinitionalRepresentation",
"RWStepRepr_RWDerivedShapeAspect",
"RWStepRepr_RWDescriptiveRepresentationItem",
"RWStepRepr_RWExtension",
"RWStepRepr_RWFeatureForDatumTargetRelationship",
"RWStepRepr_RWFunctionallyDefinedTransformation",
"RWStepRepr_RWGeometricAlignment",
"RWStepRepr_RWGlobalUncertaintyAssignedContext",
"RWStepRepr_RWGlobalUnitAssignedContext",
"RWStepRepr_RWIntegerRepresentationItem",
"RWStepRepr_RWItemDefinedTransformation",
"RWStepRepr_RWMakeFromUsageOption",
"RWStepRepr_RWMappedItem",
"RWStepRepr_RWMaterialDesignation",
"RWStepRepr_RWMaterialProperty",
"RWStepRepr_RWMaterialPropertyRepresentation",
"RWStepRepr_RWMeasureRepresentationItem",
"RWStepRepr_RWParallelOffset",
"RWStepRepr_RWParametricRepresentationContext",
"RWStepRepr_RWPerpendicularTo",
"RWStepRepr_RWProductConcept",
"RWStepRepr_RWProductDefinitionShape",
"RWStepRepr_RWPropertyDefinition",
"RWStepRepr_RWPropertyDefinitionRelationship",
"RWStepRepr_RWPropertyDefinitionRepresentation",
"RWStepRepr_RWQuantifiedAssemblyComponentUsage",
"RWStepRepr_RWReprItemAndLengthMeasureWithUnit",
"RWStepRepr_RWReprItemAndLengthMeasureWithUnitAndQRI",
"RWStepRepr_RWReprItemAndPlaneAngleMeasureWithUnit",
"RWStepRepr_RWReprItemAndPlaneAngleMeasureWithUnitAndQRI",
"RWStepRepr_RWRepresentation",
"RWStepRepr_RWRepresentationContext",
"RWStepRepr_RWRepresentationItem",
"RWStepRepr_RWRepresentationMap",
"RWStepRepr_RWRepresentationRelationship",
"RWStepRepr_RWRepresentationRelationshipWithTransformation",
"RWStepRepr_RWShapeAspect",
"RWStepRepr_RWShapeAspectDerivingRelationship",
"RWStepRepr_RWShapeAspectRelationship",
"RWStepRepr_RWShapeAspectTransition",
"RWStepRepr_RWShapeRepresentationRelationshipWithTransformation",
"RWStepRepr_RWSpecifiedHigherUsageOccurrence",
"RWStepRepr_RWStructuralResponseProperty",
"RWStepRepr_RWStructuralResponsePropertyDefinitionRepresentation",
"RWStepRepr_RWTangent",
"RWStepRepr_RWValueRepresentationItem"
]
class RWStepRepr_RWAllAroundShapeAspect():
    """
    Read & Write tool for AllAroundShapeAspect
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_AllAroundShapeAspect) -> Any: 
        """
        Reads AllAroundShapeAspect
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_AllAroundShapeAspect,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_AllAroundShapeAspect) -> None: 
        """
        Writes AllAroundShapeAspect
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWApex():
    """
    Read & Write tool for Apex
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_Apex) -> Any: 
        """
        Reads Apex
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_Apex,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_Apex) -> None: 
        """
        Writes Apex
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWAssemblyComponentUsage():
    """
    Read & Write tool for AssemblyComponentUsage
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_AssemblyComponentUsage) -> Any: 
        """
        Reads AssemblyComponentUsage
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_AssemblyComponentUsage,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_AssemblyComponentUsage) -> None: 
        """
        Writes AssemblyComponentUsage
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWAssemblyComponentUsageSubstitute():
    """
    Read & Write Module for AssemblyComponentUsageSubstitute
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_AssemblyComponentUsageSubstitute) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_AssemblyComponentUsageSubstitute,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_AssemblyComponentUsageSubstitute) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWBetweenShapeAspect():
    """
    Read & Write tool for BetweenShapeAspect
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_BetweenShapeAspect) -> Any: 
        """
        Reads BetweenShapeAspect
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_BetweenShapeAspect,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_BetweenShapeAspect) -> None: 
        """
        Writes BetweenShapeAspect
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWCentreOfSymmetry():
    """
    Read & Write tool for CentreOfSymmetry
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_CentreOfSymmetry) -> Any: 
        """
        Reads CentreOfSymmetry
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_CentreOfSymmetry,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_CentreOfSymmetry) -> None: 
        """
        Writes CentreOfSymmetry
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWCharacterizedRepresentation():
    """
    Read & Write Module for CharacterizedRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_CharacterizedRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_CharacterizedRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_CharacterizedRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWCompGroupShAspAndCompShAspAndDatumFeatAndShAsp():
    """
    Read & Write Module for CompGroupShAspAndCompShAspAndDatumFeatAndShAsp
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWCompShAspAndDatumFeatAndShAsp():
    """
    Read & Write Module for CompShAspAndDatumFeatAndShAsp
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_CompShAspAndDatumFeatAndShAsp) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_CompShAspAndDatumFeatAndShAsp,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_CompShAspAndDatumFeatAndShAsp) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWCompositeGroupShapeAspect():
    """
    Read & Write tool for CompositeGroupShapeAspect
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_CompositeGroupShapeAspect) -> Any: 
        """
        Reads CompositeGroupShapeAspect
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_CompositeGroupShapeAspect,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_CompositeGroupShapeAspect) -> None: 
        """
        Writes CompositeGroupShapeAspect
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWCompositeShapeAspect():
    """
    Read & Write tool for CompositeShapeAspect
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_CompositeShapeAspect) -> Any: 
        """
        Reads CompositeShapeAspect
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_CompositeShapeAspect,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_CompositeShapeAspect) -> None: 
        """
        Writes CompositeShapeAspect
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWCompoundRepresentationItem():
    """
    Read & Write Module for CompoundRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_CompoundRepresentationItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_CompoundRepresentationItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_CompoundRepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWConfigurationDesign():
    """
    Read & Write tool for ConfigurationDesign
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ConfigurationDesign) -> Any: 
        """
        Reads ConfigurationDesign
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ConfigurationDesign,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ConfigurationDesign) -> None: 
        """
        Writes ConfigurationDesign
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWConfigurationEffectivity():
    """
    Read & Write tool for ConfigurationEffectivity
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ConfigurationEffectivity) -> Any: 
        """
        Reads ConfigurationEffectivity
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ConfigurationEffectivity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ConfigurationEffectivity) -> None: 
        """
        Writes ConfigurationEffectivity
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWConfigurationItem():
    """
    Read & Write tool for ConfigurationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ConfigurationItem) -> Any: 
        """
        Reads ConfigurationItem
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ConfigurationItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ConfigurationItem) -> None: 
        """
        Writes ConfigurationItem
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWConstructiveGeometryRepresentation():
    """
    Read & Write Module for ConstructiveGeometryRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ConstructiveGeometryRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ConstructiveGeometryRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ConstructiveGeometryRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWConstructiveGeometryRepresentationRelationship():
    """
    Read & Write Module for ConstructiveGeometryRepresentationRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ConstructiveGeometryRepresentationRelationship) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ConstructiveGeometryRepresentationRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ConstructiveGeometryRepresentationRelationship) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWContinuosShapeAspect():
    """
    Read & Write tool for ContinuosShapeAspect
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ContinuosShapeAspect) -> Any: 
        """
        Reads ContinuosShapeAspect
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ContinuosShapeAspect,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ContinuosShapeAspect) -> None: 
        """
        Writes ContinuosShapeAspect
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWDataEnvironment():
    """
    Read & Write tool for DataEnvironment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_DataEnvironment) -> Any: 
        """
        Reads DataEnvironment
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_DataEnvironment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_DataEnvironment) -> None: 
        """
        Writes DataEnvironment
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWDefinitionalRepresentation():
    """
    Read & Write Module for DefinitionalRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_DefinitionalRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_DefinitionalRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_DefinitionalRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWDerivedShapeAspect():
    """
    Read & Write tool for DerivedShapeAspect
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_DerivedShapeAspect) -> Any: 
        """
        Reads DerivedShapeAspect
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_DerivedShapeAspect,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_DerivedShapeAspect) -> None: 
        """
        Writes DerivedShapeAspect
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWDescriptiveRepresentationItem():
    """
    Read & Write Module for DescriptiveRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_DescriptiveRepresentationItem) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_DescriptiveRepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWExtension():
    """
    Read & Write tool for Extension
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_Extension) -> Any: 
        """
        Reads Extension
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_Extension,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_Extension) -> None: 
        """
        Writes Extension
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWFeatureForDatumTargetRelationship():
    """
    Read & Write tool for FeatureForDatumTargetRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_FeatureForDatumTargetRelationship) -> Any: 
        """
        Reads ShapeAspectRelationship
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_FeatureForDatumTargetRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_FeatureForDatumTargetRelationship) -> None: 
        """
        Writes ShapeAspectRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWFunctionallyDefinedTransformation():
    """
    Read & Write Module for FunctionallyDefinedTransformation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_FunctionallyDefinedTransformation) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_FunctionallyDefinedTransformation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWGeometricAlignment():
    """
    Read & Write tool for GeometricAlignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_GeometricAlignment) -> Any: 
        """
        Reads GeometricAlignment
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_GeometricAlignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_GeometricAlignment) -> None: 
        """
        Writes GeometricAlignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWGlobalUncertaintyAssignedContext():
    """
    Read & Write Module for GlobalUncertaintyAssignedContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_GlobalUncertaintyAssignedContext) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_GlobalUncertaintyAssignedContext,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_GlobalUncertaintyAssignedContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWGlobalUnitAssignedContext():
    """
    Read & Write Module for GlobalUnitAssignedContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_GlobalUnitAssignedContext) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_GlobalUnitAssignedContext,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_GlobalUnitAssignedContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWIntegerRepresentationItem():
    """
    Read & Write Module for IntegerRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_IntegerRepresentationItem) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_IntegerRepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWItemDefinedTransformation():
    """
    Read & Write Module for ItemDefinedTransformation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ItemDefinedTransformation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ItemDefinedTransformation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ItemDefinedTransformation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWMakeFromUsageOption():
    """
    Read & Write tool for MakeFromUsageOption
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_MakeFromUsageOption) -> Any: 
        """
        Reads MakeFromUsageOption
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_MakeFromUsageOption,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_MakeFromUsageOption) -> None: 
        """
        Writes MakeFromUsageOption
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWMappedItem():
    """
    Read & Write Module for MappedItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_MappedItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_MappedItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_MappedItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWMaterialDesignation():
    """
    Read & Write Module for MaterialDesignation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_MaterialDesignation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_MaterialDesignation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_MaterialDesignation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWMaterialProperty():
    """
    Read & Write tool for MaterialProperty
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_MaterialProperty) -> Any: 
        """
        Reads MaterialProperty
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_MaterialProperty,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_MaterialProperty) -> None: 
        """
        Writes MaterialProperty
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWMaterialPropertyRepresentation():
    """
    Read & Write tool for MaterialPropertyRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_MaterialPropertyRepresentation) -> Any: 
        """
        Reads MaterialPropertyRepresentation
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_MaterialPropertyRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_MaterialPropertyRepresentation) -> None: 
        """
        Writes MaterialPropertyRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWMeasureRepresentationItem():
    """
    Read & Write Module for MeasureRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_MeasureRepresentationItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_MeasureRepresentationItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_MeasureRepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWParallelOffset():
    """
    Read & Write tool for ParallelOffset
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ParallelOffset) -> Any: 
        """
        Reads ParallelOffset
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ParallelOffset,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ParallelOffset) -> None: 
        """
        Writes ParallelOffset
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWParametricRepresentationContext():
    """
    Read & Write Module for ParametricRepresentationContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ParametricRepresentationContext) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ParametricRepresentationContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWPerpendicularTo():
    """
    Read & Write tool for PerpendicularTo
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_PerpendicularTo) -> Any: 
        """
        Reads PerpendicularTo
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_PerpendicularTo,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_PerpendicularTo) -> None: 
        """
        Writes PerpendicularTo
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWProductConcept():
    """
    Read & Write tool for ProductConcept
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ProductConcept) -> Any: 
        """
        Reads ProductConcept
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ProductConcept,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ProductConcept) -> None: 
        """
        Writes ProductConcept
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWProductDefinitionShape():
    """
    Read & Write tool for ProductDefinitionShape
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ProductDefinitionShape) -> Any: 
        """
        Reads ProductDefinitionShape
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ProductDefinitionShape,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ProductDefinitionShape) -> None: 
        """
        Writes ProductDefinitionShape
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWPropertyDefinition():
    """
    Read & Write tool for PropertyDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_PropertyDefinition) -> Any: 
        """
        Reads PropertyDefinition
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_PropertyDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_PropertyDefinition) -> None: 
        """
        Writes PropertyDefinition
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWPropertyDefinitionRelationship():
    """
    Read & Write tool for PropertyDefinitionRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_PropertyDefinitionRelationship) -> Any: 
        """
        Reads PropertyDefinitionRelationship
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_PropertyDefinitionRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_PropertyDefinitionRelationship) -> None: 
        """
        Writes PropertyDefinitionRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWPropertyDefinitionRepresentation():
    """
    Read & Write tool for PropertyDefinitionRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_PropertyDefinitionRepresentation) -> Any: 
        """
        Reads PropertyDefinitionRepresentation
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_PropertyDefinitionRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_PropertyDefinitionRepresentation) -> None: 
        """
        Writes PropertyDefinitionRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWQuantifiedAssemblyComponentUsage():
    """
    Read & Write tool for QuantifiedAssemblyComponentUsage
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_QuantifiedAssemblyComponentUsage) -> Any: 
        """
        Reads QuantifiedAssemblyComponentUsage
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_QuantifiedAssemblyComponentUsage,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_QuantifiedAssemblyComponentUsage) -> None: 
        """
        Writes QuantifiedAssemblyComponentUsage
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWReprItemAndLengthMeasureWithUnit():
    """
    Read & Write Module for ReprItemAndLengthMeasureWithUni
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ReprItemAndLengthMeasureWithUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ReprItemAndLengthMeasureWithUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWReprItemAndLengthMeasureWithUnitAndQRI():
    """
    Read & Write Module for ReprItemAndLengthMeasureWithUnitAndQRI
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ReprItemAndLengthMeasureWithUnitAndQRI) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ReprItemAndLengthMeasureWithUnitAndQRI) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWReprItemAndPlaneAngleMeasureWithUnit():
    """
    Read & Write Module for ReprItemAndPlaneAngleMeasureWithUni
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ReprItemAndPlaneAngleMeasureWithUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ReprItemAndPlaneAngleMeasureWithUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWReprItemAndPlaneAngleMeasureWithUnitAndQRI():
    """
    Read & Write Module for ReprItemAndPlaneAngleMeasureWithUnitAndQRI
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ReprItemAndPlaneAngleMeasureWithUnitAndQRI) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ReprItemAndPlaneAngleMeasureWithUnitAndQRI) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWRepresentation():
    """
    Read & Write Module for Representation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_Representation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_Representation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWRepresentationContext():
    """
    Read & Write Module for RepresentationContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_RepresentationContext) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWRepresentationItem():
    """
    Read & Write Module for RepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_RepresentationItem) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWRepresentationMap():
    """
    Read & Write Module for RepresentationMap
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_RepresentationMap) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_RepresentationMap,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_RepresentationMap) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWRepresentationRelationship():
    """
    Read & Write Module for RepresentationRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_RepresentationRelationship) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_RepresentationRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_RepresentationRelationship) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWRepresentationRelationshipWithTransformation():
    """
    Read & Write Module for RepresentationRelationshipWithTransformation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_RepresentationRelationshipWithTransformation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_RepresentationRelationshipWithTransformation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_RepresentationRelationshipWithTransformation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWShapeAspect():
    """
    Read & Write Module for ShapeAspect
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ShapeAspect) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ShapeAspect,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWShapeAspectDerivingRelationship():
    """
    Read & Write tool for ShapeAspectDerivingRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ShapeAspectDerivingRelationship) -> Any: 
        """
        Reads ShapeAspectDerivingRelationship
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ShapeAspectDerivingRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ShapeAspectDerivingRelationship) -> None: 
        """
        Writes ShapeAspectDerivingRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWShapeAspectRelationship():
    """
    Read & Write tool for ShapeAspectRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ShapeAspectRelationship) -> Any: 
        """
        Reads ShapeAspectRelationship
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ShapeAspectRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ShapeAspectRelationship) -> None: 
        """
        Writes ShapeAspectRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWShapeAspectTransition():
    """
    Read & Write tool for ShapeAspectTransition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ShapeAspectTransition) -> Any: 
        """
        Reads ShapeAspectTransition
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ShapeAspectTransition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ShapeAspectTransition) -> None: 
        """
        Writes ShapeAspectTransition
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWShapeRepresentationRelationshipWithTransformation():
    """
    Read & Write Module for ShapeRepresentationRelationshipWithTransformation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ShapeRepresentationRelationshipWithTransformation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_ShapeRepresentationRelationshipWithTransformation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ShapeRepresentationRelationshipWithTransformation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWSpecifiedHigherUsageOccurrence():
    """
    Read & Write tool for SpecifiedHigherUsageOccurrence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_SpecifiedHigherUsageOccurrence) -> Any: 
        """
        Reads SpecifiedHigherUsageOccurrence
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_SpecifiedHigherUsageOccurrence,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_SpecifiedHigherUsageOccurrence) -> None: 
        """
        Writes SpecifiedHigherUsageOccurrence
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWStructuralResponseProperty():
    """
    Read & Write tool for StructuralResponseProperty
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_StructuralResponseProperty) -> Any: 
        """
        Reads StructuralResponseProperty
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_StructuralResponseProperty,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_StructuralResponseProperty) -> None: 
        """
        Writes StructuralResponseProperty
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWStructuralResponsePropertyDefinitionRepresentation():
    """
    Read & Write tool for StructuralResponsePropertyDefinitionRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_StructuralResponsePropertyDefinitionRepresentation) -> Any: 
        """
        Reads StructuralResponsePropertyDefinitionRepresentation
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_StructuralResponsePropertyDefinitionRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_StructuralResponsePropertyDefinitionRepresentation) -> None: 
        """
        Writes StructuralResponsePropertyDefinitionRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWTangent():
    """
    Read & Write tool for Tangent
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_Tangent) -> Any: 
        """
        Reads Tangent
        """
    def Share(self,ent : OCP.StepRepr.StepRepr_Tangent,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_Tangent) -> None: 
        """
        Writes Tangent
        """
    def __init__(self) -> None: ...
    pass
class RWStepRepr_RWValueRepresentationItem():
    """
    Read & Write Module for ValueRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepRepr.StepRepr_ValueRepresentationItem) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepRepr.StepRepr_ValueRepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
