import OCP.RWStepBasic
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepData
import OCP.Interface
import OCP.TCollection
import OCP.StepBasic
__all__  = [
"RWStepBasic_RWAction",
"RWStepBasic_RWActionAssignment",
"RWStepBasic_RWActionMethod",
"RWStepBasic_RWActionRequestAssignment",
"RWStepBasic_RWActionRequestSolution",
"RWStepBasic_RWAddress",
"RWStepBasic_RWApplicationContext",
"RWStepBasic_RWApplicationContextElement",
"RWStepBasic_RWApplicationProtocolDefinition",
"RWStepBasic_RWApproval",
"RWStepBasic_RWApprovalDateTime",
"RWStepBasic_RWApprovalPersonOrganization",
"RWStepBasic_RWApprovalRelationship",
"RWStepBasic_RWApprovalRole",
"RWStepBasic_RWApprovalStatus",
"RWStepBasic_RWCalendarDate",
"RWStepBasic_RWCertification",
"RWStepBasic_RWCertificationAssignment",
"RWStepBasic_RWCertificationType",
"RWStepBasic_RWCharacterizedObject",
"RWStepBasic_RWContract",
"RWStepBasic_RWContractAssignment",
"RWStepBasic_RWContractType",
"RWStepBasic_RWConversionBasedUnit",
"RWStepBasic_RWConversionBasedUnitAndAreaUnit",
"RWStepBasic_RWConversionBasedUnitAndLengthUnit",
"RWStepBasic_RWConversionBasedUnitAndMassUnit",
"RWStepBasic_RWConversionBasedUnitAndPlaneAngleUnit",
"RWStepBasic_RWConversionBasedUnitAndRatioUnit",
"RWStepBasic_RWConversionBasedUnitAndSolidAngleUnit",
"RWStepBasic_RWConversionBasedUnitAndTimeUnit",
"RWStepBasic_RWConversionBasedUnitAndVolumeUnit",
"RWStepBasic_RWCoordinatedUniversalTimeOffset",
"RWStepBasic_RWDate",
"RWStepBasic_RWDateAndTime",
"RWStepBasic_RWDateRole",
"RWStepBasic_RWDateTimeRole",
"RWStepBasic_RWDerivedUnit",
"RWStepBasic_RWDerivedUnitElement",
"RWStepBasic_RWDimensionalExponents",
"RWStepBasic_RWDocument",
"RWStepBasic_RWDocumentFile",
"RWStepBasic_RWDocumentProductAssociation",
"RWStepBasic_RWDocumentProductEquivalence",
"RWStepBasic_RWDocumentRelationship",
"RWStepBasic_RWDocumentRepresentationType",
"RWStepBasic_RWDocumentType",
"RWStepBasic_RWDocumentUsageConstraint",
"RWStepBasic_RWEffectivity",
"RWStepBasic_RWEffectivityAssignment",
"RWStepBasic_RWEulerAngles",
"RWStepBasic_RWExternalIdentificationAssignment",
"RWStepBasic_RWExternalSource",
"RWStepBasic_RWExternallyDefinedItem",
"RWStepBasic_RWGeneralProperty",
"RWStepBasic_RWGroup",
"RWStepBasic_RWGroupAssignment",
"RWStepBasic_RWGroupRelationship",
"RWStepBasic_RWIdentificationAssignment",
"RWStepBasic_RWIdentificationRole",
"RWStepBasic_RWLengthMeasureWithUnit",
"RWStepBasic_RWLengthUnit",
"RWStepBasic_RWLocalTime",
"RWStepBasic_RWMassMeasureWithUnit",
"RWStepBasic_RWMassUnit",
"RWStepBasic_RWMeasureWithUnit",
"RWStepBasic_RWMechanicalContext",
"RWStepBasic_RWNameAssignment",
"RWStepBasic_RWNamedUnit",
"RWStepBasic_RWObjectRole",
"RWStepBasic_RWOrdinalDate",
"RWStepBasic_RWOrganization",
"RWStepBasic_RWOrganizationRole",
"RWStepBasic_RWOrganizationalAddress",
"RWStepBasic_RWPerson",
"RWStepBasic_RWPersonAndOrganization",
"RWStepBasic_RWPersonAndOrganizationRole",
"RWStepBasic_RWPersonalAddress",
"RWStepBasic_RWPlaneAngleMeasureWithUnit",
"RWStepBasic_RWPlaneAngleUnit",
"RWStepBasic_RWProduct",
"RWStepBasic_RWProductCategory",
"RWStepBasic_RWProductCategoryRelationship",
"RWStepBasic_RWProductConceptContext",
"RWStepBasic_RWProductContext",
"RWStepBasic_RWProductDefinition",
"RWStepBasic_RWProductDefinitionContext",
"RWStepBasic_RWProductDefinitionEffectivity",
"RWStepBasic_RWProductDefinitionFormation",
"RWStepBasic_RWProductDefinitionFormationRelationship",
"RWStepBasic_RWProductDefinitionFormationWithSpecifiedSource",
"RWStepBasic_RWProductDefinitionReference",
"RWStepBasic_RWProductDefinitionReferenceWithLocalRepresentation",
"RWStepBasic_RWProductDefinitionRelationship",
"RWStepBasic_RWProductDefinitionWithAssociatedDocuments",
"RWStepBasic_RWProductRelatedProductCategory",
"RWStepBasic_RWProductType",
"RWStepBasic_RWRatioMeasureWithUnit",
"RWStepBasic_RWRoleAssociation",
"RWStepBasic_RWSecurityClassification",
"RWStepBasic_RWSecurityClassificationLevel",
"RWStepBasic_RWSiUnit",
"RWStepBasic_RWSiUnitAndAreaUnit",
"RWStepBasic_RWSiUnitAndLengthUnit",
"RWStepBasic_RWSiUnitAndMassUnit",
"RWStepBasic_RWSiUnitAndPlaneAngleUnit",
"RWStepBasic_RWSiUnitAndRatioUnit",
"RWStepBasic_RWSiUnitAndSolidAngleUnit",
"RWStepBasic_RWSiUnitAndThermodynamicTemperatureUnit",
"RWStepBasic_RWSiUnitAndTimeUnit",
"RWStepBasic_RWSiUnitAndVolumeUnit",
"RWStepBasic_RWSolidAngleMeasureWithUnit",
"RWStepBasic_RWSolidAngleUnit",
"RWStepBasic_RWThermodynamicTemperatureUnit",
"RWStepBasic_RWUncertaintyMeasureWithUnit",
"RWStepBasic_RWVersionedActionRequest",
"RWStepBasic_RWWeekOfYearAndDayDate"
]
class RWStepBasic_RWAction():
    """
    Read & Write tool for Action
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Action) -> Any: 
        """
        Reads Action
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_Action,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Action) -> None: 
        """
        Writes Action
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWActionAssignment():
    """
    Read & Write tool for ActionAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ActionAssignment) -> Any: 
        """
        Reads ActionAssignment
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ActionAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ActionAssignment) -> None: 
        """
        Writes ActionAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWActionMethod():
    """
    Read & Write tool for ActionMethod
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ActionMethod) -> Any: 
        """
        Reads ActionMethod
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ActionMethod,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ActionMethod) -> None: 
        """
        Writes ActionMethod
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWActionRequestAssignment():
    """
    Read & Write tool for ActionRequestAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ActionRequestAssignment) -> Any: 
        """
        Reads ActionRequestAssignment
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ActionRequestAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ActionRequestAssignment) -> None: 
        """
        Writes ActionRequestAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWActionRequestSolution():
    """
    Read & Write tool for ActionRequestSolution
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ActionRequestSolution) -> Any: 
        """
        Reads ActionRequestSolution
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ActionRequestSolution,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ActionRequestSolution) -> None: 
        """
        Writes ActionRequestSolution
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWAddress():
    """
    Read & Write Module for Address
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Address) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Address) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWApplicationContext():
    """
    Read & Write Module for ApplicationContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ApplicationContext) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ApplicationContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWApplicationContextElement():
    """
    Read & Write Module for ApplicationContextElement
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ApplicationContextElement) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ApplicationContextElement,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ApplicationContextElement) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWApplicationProtocolDefinition():
    """
    Read & Write Module for ApplicationProtocolDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ApplicationProtocolDefinition) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ApplicationProtocolDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ApplicationProtocolDefinition) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWApproval():
    """
    Read & Write Module for Approval
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Approval) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_Approval,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Approval) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWApprovalDateTime():
    """
    Read & Write Module for ApprovalDateTime
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ApprovalDateTime) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ApprovalDateTime,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ApprovalDateTime) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWApprovalPersonOrganization():
    """
    Read & Write Module for ApprovalPersonOrganization
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ApprovalPersonOrganization) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ApprovalPersonOrganization,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ApprovalPersonOrganization) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWApprovalRelationship():
    """
    Read & Write Module for ApprovalRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ApprovalRelationship) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ApprovalRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ApprovalRelationship) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWApprovalRole():
    """
    Read & Write Module for ApprovalRole
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ApprovalRole) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ApprovalRole) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWApprovalStatus():
    """
    Read & Write Module for ApprovalStatus
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ApprovalStatus) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ApprovalStatus) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWCalendarDate():
    """
    Read & Write Module for CalendarDate
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_CalendarDate) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_CalendarDate) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWCertification():
    """
    Read & Write tool for Certification
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Certification) -> Any: 
        """
        Reads Certification
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_Certification,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Certification) -> None: 
        """
        Writes Certification
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWCertificationAssignment():
    """
    Read & Write tool for CertificationAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_CertificationAssignment) -> Any: 
        """
        Reads CertificationAssignment
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_CertificationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_CertificationAssignment) -> None: 
        """
        Writes CertificationAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWCertificationType():
    """
    Read & Write tool for CertificationType
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_CertificationType) -> Any: 
        """
        Reads CertificationType
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_CertificationType,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_CertificationType) -> None: 
        """
        Writes CertificationType
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWCharacterizedObject():
    """
    Read & Write tool for CharacterizedObject
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_CharacterizedObject) -> Any: 
        """
        Reads CharacterizedObject
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_CharacterizedObject,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_CharacterizedObject) -> None: 
        """
        Writes CharacterizedObject
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWContract():
    """
    Read & Write tool for Contract
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Contract) -> Any: 
        """
        Reads Contract
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_Contract,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Contract) -> None: 
        """
        Writes Contract
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWContractAssignment():
    """
    Read & Write tool for ContractAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ContractAssignment) -> Any: 
        """
        Reads ContractAssignment
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ContractAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ContractAssignment) -> None: 
        """
        Writes ContractAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWContractType():
    """
    Read & Write tool for ContractType
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ContractType) -> Any: 
        """
        Reads ContractType
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ContractType,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ContractType) -> None: 
        """
        Writes ContractType
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWConversionBasedUnit():
    """
    Read & Write Module for ConversionBasedUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ConversionBasedUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ConversionBasedUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ConversionBasedUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWConversionBasedUnitAndAreaUnit():
    """
    Read & Write Module for RWConversionBasedUnitAndAreaUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndAreaUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndAreaUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndAreaUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWConversionBasedUnitAndLengthUnit():
    """
    Read & Write Module for ConversionBasedUnitAndLengthUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndLengthUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndLengthUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndLengthUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWConversionBasedUnitAndMassUnit():
    """
    Read & Write Module for ConversionBasedUnitAndMassUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndMassUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndMassUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndMassUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWConversionBasedUnitAndPlaneAngleUnit():
    """
    Read & Write Module for ConversionBasedUnitAndPlaneAngleUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndPlaneAngleUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndPlaneAngleUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndPlaneAngleUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWConversionBasedUnitAndRatioUnit():
    """
    Read & Write Module for ConversionBasedUnitAndRatioUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndRatioUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndRatioUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndRatioUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWConversionBasedUnitAndSolidAngleUnit():
    """
    Read & Write Module for ConversionBasedUnitAndSolidAngleUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndSolidAngleUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndSolidAngleUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndSolidAngleUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWConversionBasedUnitAndTimeUnit():
    """
    Read & Write Module for ConversionBasedUnitAndTimeUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndTimeUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndTimeUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndTimeUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWConversionBasedUnitAndVolumeUnit():
    """
    Read & Write Module for ConversionBasedUnitAndVolumeUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndVolumeUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndVolumeUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ConversionBasedUnitAndVolumeUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWCoordinatedUniversalTimeOffset():
    """
    Read & Write Module for CoordinatedUniversalTimeOffset
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_CoordinatedUniversalTimeOffset) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_CoordinatedUniversalTimeOffset) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDate():
    """
    Read & Write Module for Date
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Date) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Date) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDateAndTime():
    """
    Read & Write Module for DateAndTime
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DateAndTime) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DateAndTime,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DateAndTime) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDateRole():
    """
    Read & Write Module for DateRole
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DateRole) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DateRole) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDateTimeRole():
    """
    Read & Write Module for DateTimeRole
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DateTimeRole) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DateTimeRole) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDerivedUnit():
    """
    Read & Write Module for DerivedUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DerivedUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DerivedUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DerivedUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDerivedUnitElement():
    """
    Read & Write Module for DerivedUnitElement
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DerivedUnitElement) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DerivedUnitElement,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DerivedUnitElement) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDimensionalExponents():
    """
    Read & Write Module for DimensionalExponents
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DimensionalExponents) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDocument():
    """
    Read & Write tool for Document
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Document) -> Any: 
        """
        Reads Document
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_Document,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Document) -> None: 
        """
        Writes Document
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDocumentFile():
    """
    Read & Write tool for DocumentFile
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DocumentFile) -> Any: 
        """
        Reads DocumentFile
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DocumentFile,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DocumentFile) -> None: 
        """
        Writes DocumentFile
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDocumentProductAssociation():
    """
    Read & Write tool for DocumentProductAssociation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DocumentProductAssociation) -> Any: 
        """
        Reads DocumentProductAssociation
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DocumentProductAssociation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DocumentProductAssociation) -> None: 
        """
        Writes DocumentProductAssociation
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDocumentProductEquivalence():
    """
    Read & Write tool for DocumentProductEquivalence
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DocumentProductEquivalence) -> Any: 
        """
        Reads DocumentProductEquivalence
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DocumentProductEquivalence,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DocumentProductEquivalence) -> None: 
        """
        Writes DocumentProductEquivalence
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDocumentRelationship():
    """
    Read & Write Module for DocumentRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DocumentRelationship) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DocumentRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DocumentRelationship) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDocumentRepresentationType():
    """
    Read & Write tool for DocumentRepresentationType
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DocumentRepresentationType) -> Any: 
        """
        Reads DocumentRepresentationType
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DocumentRepresentationType,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DocumentRepresentationType) -> None: 
        """
        Writes DocumentRepresentationType
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDocumentType():
    """
    Read & Write Module for DocumentType
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DocumentType) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DocumentType,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DocumentType) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWDocumentUsageConstraint():
    """
    Read & Write Module for DocumentUsageConstraint
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_DocumentUsageConstraint) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_DocumentUsageConstraint,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_DocumentUsageConstraint) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWEffectivity():
    """
    Read & Write Module for Effectivity
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Effectivity) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_Effectivity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Effectivity) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWEffectivityAssignment():
    """
    Read & Write tool for EffectivityAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_EffectivityAssignment) -> Any: 
        """
        Reads EffectivityAssignment
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_EffectivityAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_EffectivityAssignment) -> None: 
        """
        Writes EffectivityAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWEulerAngles():
    """
    Read & Write tool for EulerAngles
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_EulerAngles) -> Any: 
        """
        Reads EulerAngles
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_EulerAngles,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_EulerAngles) -> None: 
        """
        Writes EulerAngles
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWExternalIdentificationAssignment():
    """
    Read & Write tool for ExternalIdentificationAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ExternalIdentificationAssignment) -> Any: 
        """
        Reads ExternalIdentificationAssignment
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ExternalIdentificationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ExternalIdentificationAssignment) -> None: 
        """
        Writes ExternalIdentificationAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWExternalSource():
    """
    Read & Write tool for ExternalSource
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ExternalSource) -> Any: 
        """
        Reads ExternalSource
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ExternalSource,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ExternalSource) -> None: 
        """
        Writes ExternalSource
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWExternallyDefinedItem():
    """
    Read & Write tool for ExternallyDefinedItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ExternallyDefinedItem) -> Any: 
        """
        Reads ExternallyDefinedItem
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ExternallyDefinedItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ExternallyDefinedItem) -> None: 
        """
        Writes ExternallyDefinedItem
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWGeneralProperty():
    """
    Read & Write tool for GeneralProperty
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_GeneralProperty) -> Any: 
        """
        Reads GeneralProperty
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_GeneralProperty,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_GeneralProperty) -> None: 
        """
        Writes GeneralProperty
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWGroup():
    """
    Read & Write tool for Group
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Group) -> Any: 
        """
        Reads Group
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_Group,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Group) -> None: 
        """
        Writes Group
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWGroupAssignment():
    """
    Read & Write tool for GroupAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_GroupAssignment) -> Any: 
        """
        Reads GroupAssignment
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_GroupAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_GroupAssignment) -> None: 
        """
        Writes GroupAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWGroupRelationship():
    """
    Read & Write tool for GroupRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_GroupRelationship) -> Any: 
        """
        Reads GroupRelationship
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_GroupRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_GroupRelationship) -> None: 
        """
        Writes GroupRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWIdentificationAssignment():
    """
    Read & Write tool for IdentificationAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_IdentificationAssignment) -> Any: 
        """
        Reads IdentificationAssignment
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_IdentificationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_IdentificationAssignment) -> None: 
        """
        Writes IdentificationAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWIdentificationRole():
    """
    Read & Write tool for IdentificationRole
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_IdentificationRole) -> Any: 
        """
        Reads IdentificationRole
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_IdentificationRole,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_IdentificationRole) -> None: 
        """
        Writes IdentificationRole
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWLengthMeasureWithUnit():
    """
    Read & Write Module for LengthMeasureWithUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_LengthMeasureWithUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWLengthUnit():
    """
    Read & Write Module for LengthUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_LengthUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_LengthUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_LengthUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWLocalTime():
    """
    Read & Write Module for LocalTime
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_LocalTime) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_LocalTime,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_LocalTime) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWMassMeasureWithUnit():
    """
    Read & Write Module for MassMeasureWithUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_MassMeasureWithUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_MassMeasureWithUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_MassMeasureWithUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWMassUnit():
    """
    Read & Write tool for MassUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_MassUnit) -> Any: 
        """
        Reads MassUnit
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_MassUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_MassUnit) -> None: 
        """
        Writes MassUnit
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWMeasureWithUnit():
    """
    Read & Write Module for MeasureWithUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_MeasureWithUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_MeasureWithUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWMechanicalContext():
    """
    Read & Write Module for MechanicalContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_MechanicalContext) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_MechanicalContext,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_MechanicalContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWNameAssignment():
    """
    Read & Write tool for NameAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_NameAssignment) -> Any: 
        """
        Reads NameAssignment
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_NameAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_NameAssignment) -> None: 
        """
        Writes NameAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWNamedUnit():
    """
    Read & Write Module for NamedUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_NamedUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_NamedUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_NamedUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWObjectRole():
    """
    Read & Write tool for ObjectRole
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ObjectRole) -> Any: 
        """
        Reads ObjectRole
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ObjectRole,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ObjectRole) -> None: 
        """
        Writes ObjectRole
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWOrdinalDate():
    """
    Read & Write Module for OrdinalDate
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_OrdinalDate) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_OrdinalDate) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWOrganization():
    """
    Read & Write Module for Organization
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Organization) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Organization) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWOrganizationRole():
    """
    Read & Write Module for OrganizationRole
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_OrganizationRole) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_OrganizationRole) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWOrganizationalAddress():
    """
    Read & Write Module for OrganizationalAddress
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_OrganizationalAddress) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_OrganizationalAddress,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_OrganizationalAddress) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWPerson():
    """
    Read & Write Module for Person
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Person) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Person) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWPersonAndOrganization():
    """
    Read & Write Module for PersonAndOrganization
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_PersonAndOrganization) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_PersonAndOrganization,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_PersonAndOrganization) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWPersonAndOrganizationRole():
    """
    Read & Write Module for PersonAndOrganizationRole
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_PersonAndOrganizationRole) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_PersonAndOrganizationRole) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWPersonalAddress():
    """
    Read & Write Module for PersonalAddress
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_PersonalAddress) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_PersonalAddress,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_PersonalAddress) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWPlaneAngleMeasureWithUnit():
    """
    Read & Write Module for PlaneAngleMeasureWithUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWPlaneAngleUnit():
    """
    Read & Write Module for PlaneAngleUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_PlaneAngleUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_PlaneAngleUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_PlaneAngleUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProduct():
    """
    Read & Write Module for Product
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_Product) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_Product,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_Product) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductCategory():
    """
    Read & Write Module for ProductCategory
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductCategory) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductCategory) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductCategoryRelationship():
    """
    Read & Write tool for ProductCategoryRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductCategoryRelationship) -> Any: 
        """
        Reads ProductCategoryRelationship
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductCategoryRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductCategoryRelationship) -> None: 
        """
        Writes ProductCategoryRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductConceptContext():
    """
    Read & Write tool for ProductConceptContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductConceptContext) -> Any: 
        """
        Reads ProductConceptContext
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductConceptContext,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductConceptContext) -> None: 
        """
        Writes ProductConceptContext
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductContext():
    """
    Read & Write Module for ProductContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductContext) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductContext,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinition():
    """
    Read & Write Module for ProductDefinition
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinition) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinition,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinition) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinitionContext():
    """
    Read & Write Module for ProductDefinitionContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinitionContext) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinitionContext,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinitionContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinitionEffectivity():
    """
    Read & Write Module for ProductDefinitionEffectivity
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinitionEffectivity) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinitionEffectivity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinitionEffectivity) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinitionFormation():
    """
    Read & Write Module for ProductDefinitionFormation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinitionFormation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinitionFormation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinitionFormation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinitionFormationRelationship():
    """
    Read & Write tool for ProductDefinitionFormationRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinitionFormationRelationship) -> Any: 
        """
        Reads ProductDefinitionFormationRelationship
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinitionFormationRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinitionFormationRelationship) -> None: 
        """
        Writes ProductDefinitionFormationRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinitionFormationWithSpecifiedSource():
    """
    Read & Write Module for ProductDefinitionFormationWithSpecifiedSource
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinitionFormationWithSpecifiedSource) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinitionFormationWithSpecifiedSource,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinitionFormationWithSpecifiedSource) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinitionReference():
    """
    Read & Write Module for ProductDefinitionReference
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinitionReference) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinitionReference,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinitionReference) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinitionReferenceWithLocalRepresentation():
    """
    Read & Write Module for ProductDefinitionReferenceWithLocalRepresentation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinitionReferenceWithLocalRepresentation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinitionReferenceWithLocalRepresentation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinitionReferenceWithLocalRepresentation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinitionRelationship():
    """
    Read & Write tool for ProductDefinitionRelationship
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinitionRelationship) -> Any: 
        """
        Reads ProductDefinitionRelationship
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinitionRelationship,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinitionRelationship) -> None: 
        """
        Writes ProductDefinitionRelationship
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductDefinitionWithAssociatedDocuments():
    """
    Read & Write Module for ProductDefinitionWithAssociatedDocuments
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductDefinitionWithAssociatedDocuments) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductDefinitionWithAssociatedDocuments,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductDefinitionWithAssociatedDocuments) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductRelatedProductCategory():
    """
    Read & Write Module for ProductRelatedProductCategory
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductRelatedProductCategory) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductRelatedProductCategory,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductRelatedProductCategory) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWProductType():
    """
    Read & Write Module for ProductType
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ProductType) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ProductType,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ProductType) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWRatioMeasureWithUnit():
    """
    Read & Write Module for RatioMeasureWithUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_RatioMeasureWithUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_RatioMeasureWithUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_RatioMeasureWithUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWRoleAssociation():
    """
    Read & Write tool for RoleAssociation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_RoleAssociation) -> Any: 
        """
        Reads RoleAssociation
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_RoleAssociation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_RoleAssociation) -> None: 
        """
        Writes RoleAssociation
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSecurityClassification():
    """
    Read & Write Module for SecurityClassification
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SecurityClassification) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_SecurityClassification,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SecurityClassification) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSecurityClassificationLevel():
    """
    Read & Write Module for SecurityClassificationLevel
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SecurityClassificationLevel) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SecurityClassificationLevel) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnit():
    """
    Read & Write Module for SiUnit
    """
    def DecodeName(self,aName : OCP.StepBasic.StepBasic_SiUnitName,text : str) -> bool: 
        """
        None
        """
    def DecodePrefix(self,aPrefix : OCP.StepBasic.StepBasic_SiPrefix,text : str) -> bool: 
        """
        None
        """
    def EncodeName(self,aName : OCP.StepBasic.StepBasic_SiUnitName) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def EncodePrefix(self,aPrefix : OCP.StepBasic.StepBasic_SiPrefix) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnitAndAreaUnit():
    """
    Read & Write Module for SiUnitAndAreaUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnitAndAreaUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnitAndAreaUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnitAndLengthUnit():
    """
    Read & Write Module for SiUnitAndLengthUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnitAndLengthUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnitAndLengthUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnitAndMassUnit():
    """
    Read & Write Module for SiUnitAndMassUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnitAndMassUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnitAndMassUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnitAndPlaneAngleUnit():
    """
    Read & Write Module for SiUnitAndPlaneAngleUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnitAndPlaneAngleUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnitAndPlaneAngleUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnitAndRatioUnit():
    """
    Read & Write Module for SiUnitAndRatioUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnitAndRatioUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnitAndRatioUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnitAndSolidAngleUnit():
    """
    Read & Write Module for SiUnitAndSolidAngleUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnitAndSolidAngleUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnitAndSolidAngleUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnitAndThermodynamicTemperatureUnit():
    """
    Read & Write Module for SiUnitAndThermodynamicTemperatureUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnitAndThermodynamicTemperatureUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnitAndThermodynamicTemperatureUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnitAndTimeUnit():
    """
    Read & Write Module for SiUnitAndTimeUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnitAndTimeUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnitAndTimeUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSiUnitAndVolumeUnit():
    """
    Read & Write Module for SiUnitAndVolumeUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SiUnitAndVolumeUnit) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SiUnitAndVolumeUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSolidAngleMeasureWithUnit():
    """
    Read & Write Module for SolidAngleMeasureWithUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SolidAngleMeasureWithUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_SolidAngleMeasureWithUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SolidAngleMeasureWithUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWSolidAngleUnit():
    """
    Read & Write Module for SolidAngleUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_SolidAngleUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_SolidAngleUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_SolidAngleUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWThermodynamicTemperatureUnit():
    """
    Read & Write tool for ThermodynamicTemperatureUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_ThermodynamicTemperatureUnit) -> Any: 
        """
        Reads ThermodynamicTemperatureUnit
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_ThermodynamicTemperatureUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_ThermodynamicTemperatureUnit) -> None: 
        """
        Writes ThermodynamicTemperatureUnit
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWUncertaintyMeasureWithUnit():
    """
    Read & Write Module for UncertaintyMeasureWithUnit
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_UncertaintyMeasureWithUnit) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_UncertaintyMeasureWithUnit,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_UncertaintyMeasureWithUnit) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWVersionedActionRequest():
    """
    Read & Write tool for VersionedActionRequest
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_VersionedActionRequest) -> Any: 
        """
        Reads VersionedActionRequest
        """
    def Share(self,ent : OCP.StepBasic.StepBasic_VersionedActionRequest,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_VersionedActionRequest) -> None: 
        """
        Writes VersionedActionRequest
        """
    def __init__(self) -> None: ...
    pass
class RWStepBasic_RWWeekOfYearAndDayDate():
    """
    Read & Write Module for WeekOfYearAndDayDate
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepBasic.StepBasic_WeekOfYearAndDayDate) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepBasic.StepBasic_WeekOfYearAndDayDate) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
