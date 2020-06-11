import OCP.RWStepElement
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepData
import OCP.StepElement
import OCP.Interface
__all__  = [
"RWStepElement_RWAnalysisItemWithinRepresentation",
"RWStepElement_RWCurve3dElementDescriptor",
"RWStepElement_RWCurveElementEndReleasePacket",
"RWStepElement_RWCurveElementSectionDefinition",
"RWStepElement_RWCurveElementSectionDerivedDefinitions",
"RWStepElement_RWElementDescriptor",
"RWStepElement_RWElementMaterial",
"RWStepElement_RWSurface3dElementDescriptor",
"RWStepElement_RWSurfaceElementProperty",
"RWStepElement_RWSurfaceSection",
"RWStepElement_RWSurfaceSectionField",
"RWStepElement_RWSurfaceSectionFieldConstant",
"RWStepElement_RWSurfaceSectionFieldVarying",
"RWStepElement_RWUniformSurfaceSection",
"RWStepElement_RWVolume3dElementDescriptor"
]
class RWStepElement_RWAnalysisItemWithinRepresentation():
    """
    Read & Write tool for AnalysisItemWithinRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_AnalysisItemWithinRepresentation) -> Any: 
        """
        Reads AnalysisItemWithinRepresentation
        """
    def Share(self,ent : OCP.StepElement.StepElement_AnalysisItemWithinRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_AnalysisItemWithinRepresentation) -> None: 
        """
        Writes AnalysisItemWithinRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWCurve3dElementDescriptor():
    """
    Read & Write tool for Curve3dElementDescriptor
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_Curve3dElementDescriptor) -> Any: 
        """
        Reads Curve3dElementDescriptor
        """
    def Share(self,ent : OCP.StepElement.StepElement_Curve3dElementDescriptor,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_Curve3dElementDescriptor) -> None: 
        """
        Writes Curve3dElementDescriptor
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWCurveElementEndReleasePacket():
    """
    Read & Write tool for CurveElementEndReleasePacket
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_CurveElementEndReleasePacket) -> Any: 
        """
        Reads CurveElementEndReleasePacket
        """
    def Share(self,ent : OCP.StepElement.StepElement_CurveElementEndReleasePacket,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_CurveElementEndReleasePacket) -> None: 
        """
        Writes CurveElementEndReleasePacket
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWCurveElementSectionDefinition():
    """
    Read & Write tool for CurveElementSectionDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_CurveElementSectionDefinition) -> Any: 
        """
        Reads CurveElementSectionDefinition
        """
    def Share(self,ent : OCP.StepElement.StepElement_CurveElementSectionDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_CurveElementSectionDefinition) -> None: 
        """
        Writes CurveElementSectionDefinition
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWCurveElementSectionDerivedDefinitions():
    """
    Read & Write tool for CurveElementSectionDerivedDefinitions
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_CurveElementSectionDerivedDefinitions) -> Any: 
        """
        Reads CurveElementSectionDerivedDefinitions
        """
    def Share(self,ent : OCP.StepElement.StepElement_CurveElementSectionDerivedDefinitions,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_CurveElementSectionDerivedDefinitions) -> None: 
        """
        Writes CurveElementSectionDerivedDefinitions
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWElementDescriptor():
    """
    Read & Write tool for ElementDescriptor
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_ElementDescriptor) -> Any: 
        """
        Reads ElementDescriptor
        """
    def Share(self,ent : OCP.StepElement.StepElement_ElementDescriptor,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_ElementDescriptor) -> None: 
        """
        Writes ElementDescriptor
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWElementMaterial():
    """
    Read & Write tool for ElementMaterial
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_ElementMaterial) -> Any: 
        """
        Reads ElementMaterial
        """
    def Share(self,ent : OCP.StepElement.StepElement_ElementMaterial,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_ElementMaterial) -> None: 
        """
        Writes ElementMaterial
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWSurface3dElementDescriptor():
    """
    Read & Write tool for Surface3dElementDescriptor
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_Surface3dElementDescriptor) -> Any: 
        """
        Reads Surface3dElementDescriptor
        """
    def Share(self,ent : OCP.StepElement.StepElement_Surface3dElementDescriptor,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_Surface3dElementDescriptor) -> None: 
        """
        Writes Surface3dElementDescriptor
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWSurfaceElementProperty():
    """
    Read & Write tool for SurfaceElementProperty
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_SurfaceElementProperty) -> Any: 
        """
        Reads SurfaceElementProperty
        """
    def Share(self,ent : OCP.StepElement.StepElement_SurfaceElementProperty,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_SurfaceElementProperty) -> None: 
        """
        Writes SurfaceElementProperty
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWSurfaceSection():
    """
    Read & Write tool for SurfaceSection
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_SurfaceSection) -> Any: 
        """
        Reads SurfaceSection
        """
    def Share(self,ent : OCP.StepElement.StepElement_SurfaceSection,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_SurfaceSection) -> None: 
        """
        Writes SurfaceSection
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWSurfaceSectionField():
    """
    Read & Write tool for SurfaceSectionField
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_SurfaceSectionField) -> Any: 
        """
        Reads SurfaceSectionField
        """
    def Share(self,ent : OCP.StepElement.StepElement_SurfaceSectionField,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_SurfaceSectionField) -> None: 
        """
        Writes SurfaceSectionField
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWSurfaceSectionFieldConstant():
    """
    Read & Write tool for SurfaceSectionFieldConstant
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_SurfaceSectionFieldConstant) -> Any: 
        """
        Reads SurfaceSectionFieldConstant
        """
    def Share(self,ent : OCP.StepElement.StepElement_SurfaceSectionFieldConstant,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_SurfaceSectionFieldConstant) -> None: 
        """
        Writes SurfaceSectionFieldConstant
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWSurfaceSectionFieldVarying():
    """
    Read & Write tool for SurfaceSectionFieldVarying
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_SurfaceSectionFieldVarying) -> Any: 
        """
        Reads SurfaceSectionFieldVarying
        """
    def Share(self,ent : OCP.StepElement.StepElement_SurfaceSectionFieldVarying,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_SurfaceSectionFieldVarying) -> None: 
        """
        Writes SurfaceSectionFieldVarying
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWUniformSurfaceSection():
    """
    Read & Write tool for UniformSurfaceSection
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_UniformSurfaceSection) -> Any: 
        """
        Reads UniformSurfaceSection
        """
    def Share(self,ent : OCP.StepElement.StepElement_UniformSurfaceSection,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_UniformSurfaceSection) -> None: 
        """
        Writes UniformSurfaceSection
        """
    def __init__(self) -> None: ...
    pass
class RWStepElement_RWVolume3dElementDescriptor():
    """
    Read & Write tool for Volume3dElementDescriptor
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepElement.StepElement_Volume3dElementDescriptor) -> Any: 
        """
        Reads Volume3dElementDescriptor
        """
    def Share(self,ent : OCP.StepElement.StepElement_Volume3dElementDescriptor,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepElement.StepElement_Volume3dElementDescriptor) -> None: 
        """
        Writes Volume3dElementDescriptor
        """
    def __init__(self) -> None: ...
    pass
