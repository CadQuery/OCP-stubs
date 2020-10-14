import OCP.RWStepDimTol
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepData
import OCP.StepDimTol
import OCP.Interface
__all__  = [
"RWStepDimTol_RWAngularityTolerance",
"RWStepDimTol_RWCircularRunoutTolerance",
"RWStepDimTol_RWCoaxialityTolerance",
"RWStepDimTol_RWCommonDatum",
"RWStepDimTol_RWConcentricityTolerance",
"RWStepDimTol_RWCylindricityTolerance",
"RWStepDimTol_RWDatum",
"RWStepDimTol_RWDatumFeature",
"RWStepDimTol_RWDatumReference",
"RWStepDimTol_RWDatumReferenceCompartment",
"RWStepDimTol_RWDatumReferenceElement",
"RWStepDimTol_RWDatumReferenceModifierWithValue",
"RWStepDimTol_RWDatumSystem",
"RWStepDimTol_RWDatumTarget",
"RWStepDimTol_RWFlatnessTolerance",
"RWStepDimTol_RWGeneralDatumReference",
"RWStepDimTol_RWGeoTolAndGeoTolWthDatRef",
"RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol",
"RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndGeoTolWthMod",
"RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol",
"RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndUneqDisGeoTol",
"RWStepDimTol_RWGeoTolAndGeoTolWthMaxTol",
"RWStepDimTol_RWGeoTolAndGeoTolWthMod",
"RWStepDimTol_RWGeometricTolerance",
"RWStepDimTol_RWGeometricToleranceRelationship",
"RWStepDimTol_RWGeometricToleranceWithDatumReference",
"RWStepDimTol_RWGeometricToleranceWithDefinedAreaUnit",
"RWStepDimTol_RWGeometricToleranceWithDefinedUnit",
"RWStepDimTol_RWGeometricToleranceWithMaximumTolerance",
"RWStepDimTol_RWGeometricToleranceWithModifiers",
"RWStepDimTol_RWLineProfileTolerance",
"RWStepDimTol_RWModifiedGeometricTolerance",
"RWStepDimTol_RWNonUniformZoneDefinition",
"RWStepDimTol_RWParallelismTolerance",
"RWStepDimTol_RWPerpendicularityTolerance",
"RWStepDimTol_RWPlacedDatumTargetFeature",
"RWStepDimTol_RWPositionTolerance",
"RWStepDimTol_RWProjectedZoneDefinition",
"RWStepDimTol_RWRoundnessTolerance",
"RWStepDimTol_RWRunoutZoneDefinition",
"RWStepDimTol_RWRunoutZoneOrientation",
"RWStepDimTol_RWStraightnessTolerance",
"RWStepDimTol_RWSurfaceProfileTolerance",
"RWStepDimTol_RWSymmetryTolerance",
"RWStepDimTol_RWToleranceZone",
"RWStepDimTol_RWToleranceZoneDefinition",
"RWStepDimTol_RWToleranceZoneForm",
"RWStepDimTol_RWTotalRunoutTolerance",
"RWStepDimTol_RWUnequallyDisposedGeometricTolerance"
]
class RWStepDimTol_RWAngularityTolerance():
    """
    Read & Write tool for AngularityTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_AngularityTolerance) -> Any: 
        """
        Reads AngularityTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_AngularityTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_AngularityTolerance) -> None: 
        """
        Writes AngularityTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWCircularRunoutTolerance():
    """
    Read & Write tool for CircularRunoutTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_CircularRunoutTolerance) -> Any: 
        """
        Reads CircularRunoutTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_CircularRunoutTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_CircularRunoutTolerance) -> None: 
        """
        Writes CircularRunoutTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWCoaxialityTolerance():
    """
    Read & Write tool for CoaxialityTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_CoaxialityTolerance) -> Any: 
        """
        Reads CoaxialityTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_CoaxialityTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_CoaxialityTolerance) -> None: 
        """
        Writes CoaxialityTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWCommonDatum():
    """
    Read & Write tool for CommonDatum
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_CommonDatum) -> Any: 
        """
        Reads CommonDatum
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_CommonDatum,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_CommonDatum) -> None: 
        """
        Writes CommonDatum
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWConcentricityTolerance():
    """
    Read & Write tool for ConcentricityTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_ConcentricityTolerance) -> Any: 
        """
        Reads ConcentricityTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_ConcentricityTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_ConcentricityTolerance) -> None: 
        """
        Writes ConcentricityTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWCylindricityTolerance():
    """
    Read & Write tool for CylindricityTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_CylindricityTolerance) -> Any: 
        """
        Reads CylindricityTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_CylindricityTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_CylindricityTolerance) -> None: 
        """
        Writes CylindricityTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWDatum():
    """
    Read & Write tool for Datum
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_Datum) -> Any: 
        """
        Reads Datum
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_Datum,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_Datum) -> None: 
        """
        Writes Datum
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWDatumFeature():
    """
    Read & Write tool for DatumFeature
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_DatumFeature) -> Any: 
        """
        Reads DatumFeature
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_DatumFeature,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_DatumFeature) -> None: 
        """
        Writes DatumFeature
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWDatumReference():
    """
    Read & Write tool for DatumReference
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_DatumReference) -> Any: 
        """
        Reads DatumReference
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_DatumReference,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_DatumReference) -> None: 
        """
        Writes DatumReference
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWDatumReferenceCompartment():
    """
    Read & Write tool for DatumReferenceElement
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_DatumReferenceCompartment) -> Any: 
        """
        Reads DatumReferenceElement
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_DatumReferenceCompartment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_DatumReferenceCompartment) -> None: 
        """
        Writes DatumReferenceElement
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWDatumReferenceElement():
    """
    Read & Write tool for DatumReferenceElement
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_DatumReferenceElement) -> Any: 
        """
        Reads DatumReferenceElement
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_DatumReferenceElement,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_DatumReferenceElement) -> None: 
        """
        Writes DatumReferenceElement
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWDatumReferenceModifierWithValue():
    """
    Read & Write tool for DatumReferenceModifierWithValue
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_DatumReferenceModifierWithValue) -> Any: 
        """
        Reads DatumReferenceModifierWithValue
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_DatumReferenceModifierWithValue) -> None: 
        """
        Writes DatumReferenceModifierWithValue
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWDatumSystem():
    """
    Read & Write tool for DatumSystem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_DatumSystem) -> Any: 
        """
        Reads DatumSystem
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_DatumSystem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_DatumSystem) -> None: 
        """
        Writes DatumSystem
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWDatumTarget():
    """
    Read & Write tool for DatumTarget
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_DatumTarget) -> Any: 
        """
        Reads DatumTarget
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_DatumTarget,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_DatumTarget) -> None: 
        """
        Writes DatumTarget
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWFlatnessTolerance():
    """
    Read & Write tool for FlatnessTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_FlatnessTolerance) -> Any: 
        """
        Reads FlatnessTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_FlatnessTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_FlatnessTolerance) -> None: 
        """
        Writes FlatnessTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeneralDatumReference():
    """
    Read & Write tool for GeneralDatumReference
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeneralDatumReference) -> Any: 
        """
        Reads GeneralDatumReference
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeneralDatumReference,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeneralDatumReference) -> None: 
        """
        Writes GeneralDatumReference
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeoTolAndGeoTolWthDatRef():
    """
    Read & Write Module for GeoTolAndGeoTolWthDatRef
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRef) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRef,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRef) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol():
    """
    Read & Write Module for GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndGeoTolWthMod():
    """
    Read & Write Module for GeoTolAndGeoTolWthDatRefAndGeoTolWthMod
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol():
    """
    Read & Write Module for ReprItemAndLengthMeasureWithUni
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndUneqDisGeoTol():
    """
    Read & Write Module for GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeoTolAndGeoTolWthMaxTol():
    """
    Read & Write Module for GeoTolAndGeoTolWthMaxTol
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthMaxTol) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthMaxTol,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthMaxTol) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeoTolAndGeoTolWthMod():
    """
    Read & Write Module for GeoTolAndGeoTolWthMod
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthMod) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthMod,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeoTolAndGeoTolWthMod) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeometricTolerance():
    """
    Read & Write tool for GeometricTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeometricTolerance) -> Any: 
        """
        Reads GeometricTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeometricTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeometricTolerance) -> None: 
        """
        Writes GeometricTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeometricToleranceRelationship():
    """
    Read & Write tool for GeometricToleranceRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceRelationship) -> Any: 
        """
        Reads GeometricToleranceRelationship
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceRelationship) -> None: 
        """
        Writes GeometricToleranceRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeometricToleranceWithDatumReference():
    """
    Read & Write tool for GeometricToleranceWithDatumReference
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithDatumReference) -> Any: 
        """
        Reads GeometricToleranceWithDatumReference
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithDatumReference,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithDatumReference) -> None: 
        """
        Writes GeometricToleranceWithDatumReference
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeometricToleranceWithDefinedAreaUnit():
    """
    Read & Write tool for GeometricToleranceWithDefinedAreaUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithDefinedAreaUnit) -> Any: 
        """
        Reads GeometricToleranceWithDefinedAreaUnit
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithDefinedAreaUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithDefinedAreaUnit) -> None: 
        """
        Writes GeometricToleranceWithDefinedAreaUnit
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeometricToleranceWithDefinedUnit():
    """
    Read & Write tool for GeometricToleranceWithDefinedUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithDefinedUnit) -> Any: 
        """
        Reads GeometricToleranceWithDefinedUnit
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithDefinedUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithDefinedUnit) -> None: 
        """
        Writes GeometricToleranceWithDefinedUnit
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeometricToleranceWithMaximumTolerance():
    """
    Read & Write tool for GeometricToleranceWithMaximumTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithMaximumTolerance) -> Any: 
        """
        Reads GeometricToleranceWithMaximumTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithMaximumTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithMaximumTolerance) -> None: 
        """
        Writes GeometricToleranceWithMaximumTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWGeometricToleranceWithModifiers():
    """
    Read & Write tool for GeometricToleranceWithModifiers
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithModifiers) -> Any: 
        """
        Reads GeometricToleranceWithModifiers
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithModifiers,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_GeometricToleranceWithModifiers) -> None: 
        """
        Writes GeometricToleranceWithModifiers
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWLineProfileTolerance():
    """
    Read & Write tool for LineProfileTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_LineProfileTolerance) -> Any: 
        """
        Reads LineProfileTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_LineProfileTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_LineProfileTolerance) -> None: 
        """
        Writes LineProfileTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWModifiedGeometricTolerance():
    """
    Read & Write tool for ModifiedGeometricTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_ModifiedGeometricTolerance) -> Any: 
        """
        Reads ModifiedGeometricTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_ModifiedGeometricTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_ModifiedGeometricTolerance) -> None: 
        """
        Writes ModifiedGeometricTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWNonUniformZoneDefinition():
    """
    Read & Write tool for NonUniformZoneDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_NonUniformZoneDefinition) -> Any: 
        """
        Reads NonUniformZoneDefinition
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_NonUniformZoneDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_NonUniformZoneDefinition) -> None: 
        """
        Writes NonUniformZoneDefinition
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWParallelismTolerance():
    """
    Read & Write tool for ParallelismTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_ParallelismTolerance) -> Any: 
        """
        Reads ParallelismTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_ParallelismTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_ParallelismTolerance) -> None: 
        """
        Writes ParallelismTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWPerpendicularityTolerance():
    """
    Read & Write tool for PerpendicularityTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_PerpendicularityTolerance) -> Any: 
        """
        Reads PerpendicularityTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_PerpendicularityTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_PerpendicularityTolerance) -> None: 
        """
        Writes PerpendicularityTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWPlacedDatumTargetFeature():
    """
    Read & Write tool for PlacedDatumTargetFeature
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_PlacedDatumTargetFeature) -> Any: 
        """
        Reads PlacedDatumTargetFeature
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_PlacedDatumTargetFeature,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_PlacedDatumTargetFeature) -> None: 
        """
        Writes PlacedDatumTargetFeature
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWPositionTolerance():
    """
    Read & Write tool for PositionTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_PositionTolerance) -> Any: 
        """
        Reads PositionTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_PositionTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_PositionTolerance) -> None: 
        """
        Writes PositionTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWProjectedZoneDefinition():
    """
    Read & Write tool for ProjectedZoneDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_ProjectedZoneDefinition) -> Any: 
        """
        Reads ProjectedZoneDefinition
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_ProjectedZoneDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_ProjectedZoneDefinition) -> None: 
        """
        Writes ProjectedZoneDefinition
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWRoundnessTolerance():
    """
    Read & Write tool for RoundnessTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_RoundnessTolerance) -> Any: 
        """
        Reads RoundnessTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_RoundnessTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_RoundnessTolerance) -> None: 
        """
        Writes RoundnessTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWRunoutZoneDefinition():
    """
    Read & Write tool for RunoutZoneDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_RunoutZoneDefinition) -> Any: 
        """
        Reads RunoutZoneDefinition
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_RunoutZoneDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_RunoutZoneDefinition) -> None: 
        """
        Writes RunoutZoneDefinition
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWRunoutZoneOrientation():
    """
    Read & Write tool for RunoutZoneOrientation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_RunoutZoneOrientation) -> Any: 
        """
        Reads RunoutZoneOrientation
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_RunoutZoneOrientation) -> None: 
        """
        Writes RunoutZoneOrientation
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWStraightnessTolerance():
    """
    Read & Write tool for StraightnessTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_StraightnessTolerance) -> Any: 
        """
        Reads StraightnessTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_StraightnessTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_StraightnessTolerance) -> None: 
        """
        Writes StraightnessTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWSurfaceProfileTolerance():
    """
    Read & Write tool for SurfaceProfileTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_SurfaceProfileTolerance) -> Any: 
        """
        Reads SurfaceProfileTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_SurfaceProfileTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_SurfaceProfileTolerance) -> None: 
        """
        Writes SurfaceProfileTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWSymmetryTolerance():
    """
    Read & Write tool for SymmetryTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_SymmetryTolerance) -> Any: 
        """
        Reads SymmetryTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_SymmetryTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_SymmetryTolerance) -> None: 
        """
        Writes SymmetryTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWToleranceZone():
    """
    Read & Write tool for ToleranceZone
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_ToleranceZone) -> Any: 
        """
        Reads ToleranceZone
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_ToleranceZone,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_ToleranceZone) -> None: 
        """
        Writes ToleranceZone
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWToleranceZoneDefinition():
    """
    Read & Write tool for ToleranceZoneDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_ToleranceZoneDefinition) -> Any: 
        """
        Reads ToleranceZoneDefinition
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_ToleranceZoneDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_ToleranceZoneDefinition) -> None: 
        """
        Writes ToleranceZoneDefinition
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWToleranceZoneForm():
    """
    Read & Write tool for ToleranceZoneForm
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_ToleranceZoneForm) -> Any: 
        """
        Reads ToleranceZoneForm
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_ToleranceZoneForm) -> None: 
        """
        Writes ToleranceZoneForm
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWTotalRunoutTolerance():
    """
    Read & Write tool for TotalRunoutTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_TotalRunoutTolerance) -> Any: 
        """
        Reads TotalRunoutTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_TotalRunoutTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_TotalRunoutTolerance) -> None: 
        """
        Writes TotalRunoutTolerance
        """
    def __init__(self) -> None: ...
    pass
class RWStepDimTol_RWUnequallyDisposedGeometricTolerance():
    """
    Read & Write tool for UnequallyDisposedGeometricTolerance
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepDimTol.StepDimTol_UnequallyDisposedGeometricTolerance) -> Any: 
        """
        Reads UnequallyDisposedGeometricTolerance
        """
    def Share(self,ent : OCP.StepDimTol.StepDimTol_UnequallyDisposedGeometricTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepDimTol.StepDimTol_UnequallyDisposedGeometricTolerance) -> None: 
        """
        Writes UnequallyDisposedGeometricTolerance
        """
    def __init__(self) -> None: ...
    pass
