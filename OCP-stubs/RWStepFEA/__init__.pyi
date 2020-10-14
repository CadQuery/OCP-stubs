import OCP.RWStepFEA
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepData
import OCP.StepFEA
import OCP.Interface
__all__  = [
"RWStepFEA_RWAlignedCurve3dElementCoordinateSystem",
"RWStepFEA_RWAlignedSurface3dElementCoordinateSystem",
"RWStepFEA_RWArbitraryVolume3dElementCoordinateSystem",
"RWStepFEA_RWConstantSurface3dElementCoordinateSystem",
"RWStepFEA_RWCurve3dElementProperty",
"RWStepFEA_RWCurve3dElementRepresentation",
"RWStepFEA_RWCurveElementEndOffset",
"RWStepFEA_RWCurveElementEndRelease",
"RWStepFEA_RWCurveElementInterval",
"RWStepFEA_RWCurveElementIntervalConstant",
"RWStepFEA_RWCurveElementIntervalLinearlyVarying",
"RWStepFEA_RWCurveElementLocation",
"RWStepFEA_RWDummyNode",
"RWStepFEA_RWElementGeometricRelationship",
"RWStepFEA_RWElementGroup",
"RWStepFEA_RWElementRepresentation",
"RWStepFEA_RWFeaAreaDensity",
"RWStepFEA_RWFeaAxis2Placement3d",
"RWStepFEA_RWFeaCurveSectionGeometricRelationship",
"RWStepFEA_RWFeaGroup",
"RWStepFEA_RWFeaLinearElasticity",
"RWStepFEA_RWFeaMassDensity",
"RWStepFEA_RWFeaMaterialPropertyRepresentation",
"RWStepFEA_RWFeaMaterialPropertyRepresentationItem",
"RWStepFEA_RWFeaModel",
"RWStepFEA_RWFeaModel3d",
"RWStepFEA_RWFeaModelDefinition",
"RWStepFEA_RWFeaMoistureAbsorption",
"RWStepFEA_RWFeaParametricPoint",
"RWStepFEA_RWFeaRepresentationItem",
"RWStepFEA_RWFeaSecantCoefficientOfLinearThermalExpansion",
"RWStepFEA_RWFeaShellBendingStiffness",
"RWStepFEA_RWFeaShellMembraneBendingCouplingStiffness",
"RWStepFEA_RWFeaShellMembraneStiffness",
"RWStepFEA_RWFeaShellShearStiffness",
"RWStepFEA_RWFeaSurfaceSectionGeometricRelationship",
"RWStepFEA_RWFeaTangentialCoefficientOfLinearThermalExpansion",
"RWStepFEA_RWFreedomAndCoefficient",
"RWStepFEA_RWFreedomsList",
"RWStepFEA_RWGeometricNode",
"RWStepFEA_RWNode",
"RWStepFEA_RWNodeDefinition",
"RWStepFEA_RWNodeGroup",
"RWStepFEA_RWNodeRepresentation",
"RWStepFEA_RWNodeSet",
"RWStepFEA_RWNodeWithSolutionCoordinateSystem",
"RWStepFEA_RWNodeWithVector",
"RWStepFEA_RWParametricCurve3dElementCoordinateDirection",
"RWStepFEA_RWParametricCurve3dElementCoordinateSystem",
"RWStepFEA_RWParametricSurface3dElementCoordinateSystem",
"RWStepFEA_RWSurface3dElementRepresentation",
"RWStepFEA_RWVolume3dElementRepresentation"
]
class RWStepFEA_RWAlignedCurve3dElementCoordinateSystem():
    """
    Read & Write tool for AlignedCurve3dElementCoordinateSystem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_AlignedCurve3dElementCoordinateSystem) -> Any: 
        """
        Reads AlignedCurve3dElementCoordinateSystem
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_AlignedCurve3dElementCoordinateSystem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_AlignedCurve3dElementCoordinateSystem) -> None: 
        """
        Writes AlignedCurve3dElementCoordinateSystem
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWAlignedSurface3dElementCoordinateSystem():
    """
    Read & Write tool for AlignedSurface3dElementCoordinateSystem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_AlignedSurface3dElementCoordinateSystem) -> Any: 
        """
        Reads AlignedSurface3dElementCoordinateSystem
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_AlignedSurface3dElementCoordinateSystem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_AlignedSurface3dElementCoordinateSystem) -> None: 
        """
        Writes AlignedSurface3dElementCoordinateSystem
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWArbitraryVolume3dElementCoordinateSystem():
    """
    Read & Write tool for ArbitraryVolume3dElementCoordinateSystem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_ArbitraryVolume3dElementCoordinateSystem) -> Any: 
        """
        Reads ArbitraryVolume3dElementCoordinateSystem
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_ArbitraryVolume3dElementCoordinateSystem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_ArbitraryVolume3dElementCoordinateSystem) -> None: 
        """
        Writes ArbitraryVolume3dElementCoordinateSystem
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWConstantSurface3dElementCoordinateSystem():
    """
    Read & Write tool for ConstantSurface3dElementCoordinateSystem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_ConstantSurface3dElementCoordinateSystem) -> Any: 
        """
        Reads ConstantSurface3dElementCoordinateSystem
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_ConstantSurface3dElementCoordinateSystem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_ConstantSurface3dElementCoordinateSystem) -> None: 
        """
        Writes ConstantSurface3dElementCoordinateSystem
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWCurve3dElementProperty():
    """
    Read & Write tool for Curve3dElementProperty
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_Curve3dElementProperty) -> Any: 
        """
        Reads Curve3dElementProperty
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_Curve3dElementProperty,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_Curve3dElementProperty) -> None: 
        """
        Writes Curve3dElementProperty
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWCurve3dElementRepresentation():
    """
    Read & Write tool for Curve3dElementRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_Curve3dElementRepresentation) -> Any: 
        """
        Reads Curve3dElementRepresentation
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_Curve3dElementRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_Curve3dElementRepresentation) -> None: 
        """
        Writes Curve3dElementRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWCurveElementEndOffset():
    """
    Read & Write tool for CurveElementEndOffset
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_CurveElementEndOffset) -> Any: 
        """
        Reads CurveElementEndOffset
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_CurveElementEndOffset,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_CurveElementEndOffset) -> None: 
        """
        Writes CurveElementEndOffset
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWCurveElementEndRelease():
    """
    Read & Write tool for CurveElementEndRelease
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_CurveElementEndRelease) -> Any: 
        """
        Reads CurveElementEndRelease
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_CurveElementEndRelease,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_CurveElementEndRelease) -> None: 
        """
        Writes CurveElementEndRelease
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWCurveElementInterval():
    """
    Read & Write tool for CurveElementInterval
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_CurveElementInterval) -> Any: 
        """
        Reads CurveElementInterval
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_CurveElementInterval,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_CurveElementInterval) -> None: 
        """
        Writes CurveElementInterval
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWCurveElementIntervalConstant():
    """
    Read & Write tool for CurveElementIntervalConstant
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_CurveElementIntervalConstant) -> Any: 
        """
        Reads CurveElementIntervalConstant
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_CurveElementIntervalConstant,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_CurveElementIntervalConstant) -> None: 
        """
        Writes CurveElementIntervalConstant
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWCurveElementIntervalLinearlyVarying():
    """
    Read & Write tool for CurveElementIntervalLinearlyVarying
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_CurveElementIntervalLinearlyVarying) -> Any: 
        """
        Reads CurveElementIntervalLinearlyVarying
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_CurveElementIntervalLinearlyVarying,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_CurveElementIntervalLinearlyVarying) -> None: 
        """
        Writes CurveElementIntervalLinearlyVarying
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWCurveElementLocation():
    """
    Read & Write tool for CurveElementLocation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_CurveElementLocation) -> Any: 
        """
        Reads CurveElementLocation
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_CurveElementLocation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_CurveElementLocation) -> None: 
        """
        Writes CurveElementLocation
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWDummyNode():
    """
    Read & Write tool for DummyNode
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_DummyNode) -> Any: 
        """
        Reads DummyNode
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_DummyNode,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_DummyNode) -> None: 
        """
        Writes DummyNode
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWElementGeometricRelationship():
    """
    Read & Write tool for ElementGeometricRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_ElementGeometricRelationship) -> Any: 
        """
        Reads ElementGeometricRelationship
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_ElementGeometricRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_ElementGeometricRelationship) -> None: 
        """
        Writes ElementGeometricRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWElementGroup():
    """
    Read & Write tool for ElementGroup
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_ElementGroup) -> Any: 
        """
        Reads ElementGroup
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_ElementGroup,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_ElementGroup) -> None: 
        """
        Writes ElementGroup
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWElementRepresentation():
    """
    Read & Write tool for ElementRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_ElementRepresentation) -> Any: 
        """
        Reads ElementRepresentation
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_ElementRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_ElementRepresentation) -> None: 
        """
        Writes ElementRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaAreaDensity():
    """
    Read & Write tool for FeaAreaDensity
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaAreaDensity) -> Any: 
        """
        Reads FeaAreaDensity
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaAreaDensity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaAreaDensity) -> None: 
        """
        Writes FeaAreaDensity
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaAxis2Placement3d():
    """
    Read & Write tool for FeaAxis2Placement3d
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaAxis2Placement3d) -> Any: 
        """
        Reads FeaAxis2Placement3d
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaAxis2Placement3d,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaAxis2Placement3d) -> None: 
        """
        Writes FeaAxis2Placement3d
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaCurveSectionGeometricRelationship():
    """
    Read & Write tool for FeaCurveSectionGeometricRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaCurveSectionGeometricRelationship) -> Any: 
        """
        Reads FeaCurveSectionGeometricRelationship
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaCurveSectionGeometricRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaCurveSectionGeometricRelationship) -> None: 
        """
        Writes FeaCurveSectionGeometricRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaGroup():
    """
    Read & Write tool for FeaGroup
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaGroup) -> Any: 
        """
        Reads FeaGroup
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaGroup,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaGroup) -> None: 
        """
        Writes FeaGroup
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaLinearElasticity():
    """
    Read & Write tool for FeaLinearElasticity
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaLinearElasticity) -> Any: 
        """
        Reads FeaLinearElasticity
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaLinearElasticity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaLinearElasticity) -> None: 
        """
        Writes FeaLinearElasticity
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaMassDensity():
    """
    Read & Write tool for FeaMassDensity
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaMassDensity) -> Any: 
        """
        Reads FeaMassDensity
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaMassDensity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaMassDensity) -> None: 
        """
        Writes FeaMassDensity
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaMaterialPropertyRepresentation():
    """
    Read & Write tool for FeaMaterialPropertyRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaMaterialPropertyRepresentation) -> Any: 
        """
        Reads FeaMaterialPropertyRepresentation
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaMaterialPropertyRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaMaterialPropertyRepresentation) -> None: 
        """
        Writes FeaMaterialPropertyRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaMaterialPropertyRepresentationItem():
    """
    Read & Write tool for FeaMaterialPropertyRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaMaterialPropertyRepresentationItem) -> Any: 
        """
        Reads FeaMaterialPropertyRepresentationItem
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaMaterialPropertyRepresentationItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaMaterialPropertyRepresentationItem) -> None: 
        """
        Writes FeaMaterialPropertyRepresentationItem
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaModel():
    """
    Read & Write tool for FeaModel
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaModel) -> Any: 
        """
        Reads FeaModel
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaModel,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaModel) -> None: 
        """
        Writes FeaModel
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaModel3d():
    """
    Read & Write tool for FeaModel3d
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaModel3d) -> Any: 
        """
        Reads FeaModel3d
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaModel3d,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaModel3d) -> None: 
        """
        Writes FeaModel3d
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaModelDefinition():
    """
    Read & Write tool for FeaModelDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaModelDefinition) -> Any: 
        """
        Reads FeaModelDefinition
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaModelDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaModelDefinition) -> None: 
        """
        Writes FeaModelDefinition
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaMoistureAbsorption():
    """
    Read & Write tool for FeaMoistureAbsorption
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaMoistureAbsorption) -> Any: 
        """
        Reads FeaMoistureAbsorption
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaMoistureAbsorption,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaMoistureAbsorption) -> None: 
        """
        Writes FeaMoistureAbsorption
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaParametricPoint():
    """
    Read & Write tool for FeaParametricPoint
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaParametricPoint) -> Any: 
        """
        Reads FeaParametricPoint
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaParametricPoint,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaParametricPoint) -> None: 
        """
        Writes FeaParametricPoint
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaRepresentationItem():
    """
    Read & Write tool for FeaRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaRepresentationItem) -> Any: 
        """
        Reads FeaRepresentationItem
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaRepresentationItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaRepresentationItem) -> None: 
        """
        Writes FeaRepresentationItem
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaSecantCoefficientOfLinearThermalExpansion():
    """
    Read & Write tool for FeaSecantCoefficientOfLinearThermalExpansion
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaSecantCoefficientOfLinearThermalExpansion) -> Any: 
        """
        Reads FeaSecantCoefficientOfLinearThermalExpansion
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaSecantCoefficientOfLinearThermalExpansion,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaSecantCoefficientOfLinearThermalExpansion) -> None: 
        """
        Writes FeaSecantCoefficientOfLinearThermalExpansion
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaShellBendingStiffness():
    """
    Read & Write tool for FeaShellBendingStiffness
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaShellBendingStiffness) -> Any: 
        """
        Reads FeaShellBendingStiffness
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaShellBendingStiffness,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaShellBendingStiffness) -> None: 
        """
        Writes FeaShellBendingStiffness
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaShellMembraneBendingCouplingStiffness():
    """
    Read & Write tool for FeaShellMembraneBendingCouplingStiffness
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaShellMembraneBendingCouplingStiffness) -> Any: 
        """
        Reads FeaShellMembraneBendingCouplingStiffness
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaShellMembraneBendingCouplingStiffness,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaShellMembraneBendingCouplingStiffness) -> None: 
        """
        Writes FeaShellMembraneBendingCouplingStiffness
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaShellMembraneStiffness():
    """
    Read & Write tool for FeaShellMembraneStiffness
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaShellMembraneStiffness) -> Any: 
        """
        Reads FeaShellMembraneStiffness
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaShellMembraneStiffness,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaShellMembraneStiffness) -> None: 
        """
        Writes FeaShellMembraneStiffness
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaShellShearStiffness():
    """
    Read & Write tool for FeaShellShearStiffness
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaShellShearStiffness) -> Any: 
        """
        Reads FeaShellShearStiffness
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaShellShearStiffness,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaShellShearStiffness) -> None: 
        """
        Writes FeaShellShearStiffness
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaSurfaceSectionGeometricRelationship():
    """
    Read & Write tool for FeaSurfaceSectionGeometricRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaSurfaceSectionGeometricRelationship) -> Any: 
        """
        Reads FeaSurfaceSectionGeometricRelationship
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaSurfaceSectionGeometricRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaSurfaceSectionGeometricRelationship) -> None: 
        """
        Writes FeaSurfaceSectionGeometricRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFeaTangentialCoefficientOfLinearThermalExpansion():
    """
    Read & Write tool for FeaTangentialCoefficientOfLinearThermalExpansion
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion) -> Any: 
        """
        Reads FeaTangentialCoefficientOfLinearThermalExpansion
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion) -> None: 
        """
        Writes FeaTangentialCoefficientOfLinearThermalExpansion
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFreedomAndCoefficient():
    """
    Read & Write tool for FreedomAndCoefficient
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FreedomAndCoefficient) -> Any: 
        """
        Reads FreedomAndCoefficient
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FreedomAndCoefficient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FreedomAndCoefficient) -> None: 
        """
        Writes FreedomAndCoefficient
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWFreedomsList():
    """
    Read & Write tool for FreedomsList
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_FreedomsList) -> Any: 
        """
        Reads FreedomsList
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_FreedomsList,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_FreedomsList) -> None: 
        """
        Writes FreedomsList
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWGeometricNode():
    """
    Read & Write tool for GeometricNode
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_GeometricNode) -> Any: 
        """
        Reads GeometricNode
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_GeometricNode,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_GeometricNode) -> None: 
        """
        Writes GeometricNode
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWNode():
    """
    Read & Write tool for Node
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_Node) -> Any: 
        """
        Reads Node
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_Node,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_Node) -> None: 
        """
        Writes Node
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWNodeDefinition():
    """
    Read & Write tool for NodeDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_NodeDefinition) -> Any: 
        """
        Reads NodeDefinition
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_NodeDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_NodeDefinition) -> None: 
        """
        Writes NodeDefinition
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWNodeGroup():
    """
    Read & Write tool for NodeGroup
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_NodeGroup) -> Any: 
        """
        Reads NodeGroup
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_NodeGroup,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_NodeGroup) -> None: 
        """
        Writes NodeGroup
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWNodeRepresentation():
    """
    Read & Write tool for NodeRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_NodeRepresentation) -> Any: 
        """
        Reads NodeRepresentation
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_NodeRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_NodeRepresentation) -> None: 
        """
        Writes NodeRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWNodeSet():
    """
    Read & Write tool for NodeSet
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_NodeSet) -> Any: 
        """
        Reads NodeSet
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_NodeSet,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_NodeSet) -> None: 
        """
        Writes NodeSet
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWNodeWithSolutionCoordinateSystem():
    """
    Read & Write tool for NodeWithSolutionCoordinateSystem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_NodeWithSolutionCoordinateSystem) -> Any: 
        """
        Reads NodeWithSolutionCoordinateSystem
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_NodeWithSolutionCoordinateSystem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_NodeWithSolutionCoordinateSystem) -> None: 
        """
        Writes NodeWithSolutionCoordinateSystem
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWNodeWithVector():
    """
    Read & Write tool for NodeWithVector
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_NodeWithVector) -> Any: 
        """
        Reads NodeWithVector
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_NodeWithVector,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_NodeWithVector) -> None: 
        """
        Writes NodeWithVector
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWParametricCurve3dElementCoordinateDirection():
    """
    Read & Write tool for ParametricCurve3dElementCoordinateDirection
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_ParametricCurve3dElementCoordinateDirection) -> Any: 
        """
        Reads ParametricCurve3dElementCoordinateDirection
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_ParametricCurve3dElementCoordinateDirection,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_ParametricCurve3dElementCoordinateDirection) -> None: 
        """
        Writes ParametricCurve3dElementCoordinateDirection
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWParametricCurve3dElementCoordinateSystem():
    """
    Read & Write tool for ParametricCurve3dElementCoordinateSystem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_ParametricCurve3dElementCoordinateSystem) -> Any: 
        """
        Reads ParametricCurve3dElementCoordinateSystem
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_ParametricCurve3dElementCoordinateSystem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_ParametricCurve3dElementCoordinateSystem) -> None: 
        """
        Writes ParametricCurve3dElementCoordinateSystem
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWParametricSurface3dElementCoordinateSystem():
    """
    Read & Write tool for ParametricSurface3dElementCoordinateSystem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_ParametricSurface3dElementCoordinateSystem) -> Any: 
        """
        Reads ParametricSurface3dElementCoordinateSystem
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_ParametricSurface3dElementCoordinateSystem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_ParametricSurface3dElementCoordinateSystem) -> None: 
        """
        Writes ParametricSurface3dElementCoordinateSystem
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWSurface3dElementRepresentation():
    """
    Read & Write tool for Surface3dElementRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_Surface3dElementRepresentation) -> Any: 
        """
        Reads Surface3dElementRepresentation
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_Surface3dElementRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_Surface3dElementRepresentation) -> None: 
        """
        Writes Surface3dElementRepresentation
        """
    def __init__(self) -> None: ...
    pass
class RWStepFEA_RWVolume3dElementRepresentation():
    """
    Read & Write tool for Volume3dElementRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepFEA.StepFEA_Volume3dElementRepresentation) -> Any: 
        """
        Reads Volume3dElementRepresentation
        """
    def Share(self,ent : OCP.StepFEA.StepFEA_Volume3dElementRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepFEA.StepFEA_Volume3dElementRepresentation) -> None: 
        """
        Writes Volume3dElementRepresentation
        """
    def __init__(self) -> None: ...
    pass
