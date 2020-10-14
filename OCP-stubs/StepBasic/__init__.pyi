import OCP.StepBasic
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.TColStd
import OCP.Standard
import OCP.StepData
import OCP.Interface
__all__  = [
"StepBasic_Action",
"StepBasic_ActionAssignment",
"StepBasic_ActionMethod",
"StepBasic_ActionRequestAssignment",
"StepBasic_ActionRequestSolution",
"StepBasic_Address",
"StepBasic_AheadOrBehind",
"StepBasic_ApplicationContext",
"StepBasic_ApplicationContextElement",
"StepBasic_ApplicationProtocolDefinition",
"StepBasic_Approval",
"StepBasic_ApprovalAssignment",
"StepBasic_ApprovalDateTime",
"StepBasic_ApprovalPersonOrganization",
"StepBasic_ApprovalRelationship",
"StepBasic_ApprovalRole",
"StepBasic_ApprovalStatus",
"StepBasic_NamedUnit",
"StepBasic_Array1OfApproval",
"StepBasic_Array1OfDerivedUnitElement",
"StepBasic_Array1OfDocument",
"StepBasic_Array1OfNamedUnit",
"StepBasic_Array1OfOrganization",
"StepBasic_Array1OfPerson",
"StepBasic_Array1OfProduct",
"StepBasic_Array1OfProductContext",
"StepBasic_Array1OfProductDefinition",
"StepBasic_Array1OfUncertaintyMeasureWithUnit",
"StepBasic_Date",
"StepBasic_Certification",
"StepBasic_CertificationAssignment",
"StepBasic_CertificationType",
"StepBasic_CharacterizedObject",
"StepBasic_Contract",
"StepBasic_ContractAssignment",
"StepBasic_ContractType",
"StepBasic_ConversionBasedUnit",
"StepBasic_ConversionBasedUnitAndAreaUnit",
"StepBasic_ConversionBasedUnitAndLengthUnit",
"StepBasic_ConversionBasedUnitAndMassUnit",
"StepBasic_ConversionBasedUnitAndPlaneAngleUnit",
"StepBasic_ConversionBasedUnitAndRatioUnit",
"StepBasic_ConversionBasedUnitAndSolidAngleUnit",
"StepBasic_ConversionBasedUnitAndTimeUnit",
"StepBasic_ConversionBasedUnitAndVolumeUnit",
"StepBasic_CoordinatedUniversalTimeOffset",
"StepBasic_CalendarDate",
"StepBasic_DateAndTime",
"StepBasic_DateAndTimeAssignment",
"StepBasic_DateAssignment",
"StepBasic_DateRole",
"StepBasic_DateTimeRole",
"StepBasic_DateTimeSelect",
"StepBasic_DerivedUnit",
"StepBasic_DerivedUnitElement",
"StepBasic_ProductDefinitionContext",
"StepBasic_Document",
"StepBasic_DimensionalExponents",
"StepBasic_DigitalDocument",
"StepBasic_DocumentFile",
"StepBasic_DocumentProductAssociation",
"StepBasic_DocumentProductEquivalence",
"StepBasic_DocumentReference",
"StepBasic_DocumentRelationship",
"StepBasic_DocumentRepresentationType",
"StepBasic_DocumentType",
"StepBasic_DocumentUsageConstraint",
"StepBasic_Effectivity",
"StepBasic_EffectivityAssignment",
"StepBasic_EulerAngles",
"StepBasic_IdentificationAssignment",
"StepBasic_ExternalSource",
"StepBasic_ExternallyDefinedItem",
"StepBasic_GeneralProperty",
"StepBasic_Group",
"StepBasic_GroupAssignment",
"StepBasic_GroupRelationship",
"StepBasic_HArray1OfApproval",
"StepBasic_HArray1OfDerivedUnitElement",
"StepBasic_HArray1OfDocument",
"StepBasic_HArray1OfNamedUnit",
"StepBasic_HArray1OfOrganization",
"StepBasic_HArray1OfPerson",
"StepBasic_HArray1OfProduct",
"StepBasic_HArray1OfProductContext",
"StepBasic_HArray1OfProductDefinition",
"StepBasic_HArray1OfUncertaintyMeasureWithUnit",
"StepBasic_ExternalIdentificationAssignment",
"StepBasic_IdentificationRole",
"StepBasic_MeasureWithUnit",
"StepBasic_LengthUnit",
"StepBasic_LocalTime",
"StepBasic_MassMeasureWithUnit",
"StepBasic_MassUnit",
"StepBasic_MeasureValueMember",
"StepBasic_LengthMeasureWithUnit",
"StepBasic_ProductContext",
"StepBasic_NameAssignment",
"StepBasic_AreaUnit",
"StepBasic_ObjectRole",
"StepBasic_OrdinalDate",
"StepBasic_Organization",
"StepBasic_OrganizationAssignment",
"StepBasic_OrganizationRole",
"StepBasic_OrganizationalAddress",
"StepBasic_Person",
"StepBasic_PersonAndOrganization",
"StepBasic_PersonAndOrganizationAssignment",
"StepBasic_PersonAndOrganizationRole",
"StepBasic_PersonOrganizationSelect",
"StepBasic_PersonalAddress",
"StepBasic_ProductDefinition",
"StepBasic_PlaneAngleMeasureWithUnit",
"StepBasic_PlaneAngleUnit",
"StepBasic_Product",
"StepBasic_ProductCategory",
"StepBasic_ProductCategoryRelationship",
"StepBasic_ProductConceptContext",
"StepBasic_MechanicalContext",
"StepBasic_PhysicallyModeledProductDefinition",
"StepBasic_DesignContext",
"StepBasic_ProductDefinitionEffectivity",
"StepBasic_ProductDefinitionFormation",
"StepBasic_ProductDefinitionFormationRelationship",
"StepBasic_ProductDefinitionFormationWithSpecifiedSource",
"StepBasic_ProductDefinitionOrReference",
"StepBasic_ProductDefinitionReference",
"StepBasic_ProductDefinitionReferenceWithLocalRepresentation",
"StepBasic_ProductDefinitionRelationship",
"StepBasic_ProductDefinitionWithAssociatedDocuments",
"StepBasic_ProductOrFormationOrDefinition",
"StepBasic_ProductRelatedProductCategory",
"StepBasic_ProductType",
"StepBasic_RatioMeasureWithUnit",
"StepBasic_RatioUnit",
"StepBasic_RoleAssociation",
"StepBasic_RoleSelect",
"StepBasic_SecurityClassification",
"StepBasic_SecurityClassificationAssignment",
"StepBasic_SecurityClassificationLevel",
"StepBasic_SiPrefix",
"StepBasic_SiUnit",
"StepBasic_SiUnitAndAreaUnit",
"StepBasic_SiUnitAndLengthUnit",
"StepBasic_SiUnitAndMassUnit",
"StepBasic_SiUnitAndPlaneAngleUnit",
"StepBasic_SiUnitAndRatioUnit",
"StepBasic_SiUnitAndSolidAngleUnit",
"StepBasic_SiUnitAndThermodynamicTemperatureUnit",
"StepBasic_SiUnitAndTimeUnit",
"StepBasic_SiUnitAndVolumeUnit",
"StepBasic_SiUnitName",
"StepBasic_SizeMember",
"StepBasic_SizeSelect",
"StepBasic_SolidAngleMeasureWithUnit",
"StepBasic_SolidAngleUnit",
"StepBasic_Source",
"StepBasic_SourceItem",
"StepBasic_ThermodynamicTemperatureUnit",
"StepBasic_TimeMeasureWithUnit",
"StepBasic_TimeUnit",
"StepBasic_UncertaintyMeasureWithUnit",
"StepBasic_Unit",
"StepBasic_VersionedActionRequest",
"StepBasic_VolumeUnit",
"StepBasic_WeekOfYearAndDayDate",
"StepBasic_aobAhead",
"StepBasic_aobBehind",
"StepBasic_aobExact",
"StepBasic_sBought",
"StepBasic_sMade",
"StepBasic_sNotKnown",
"StepBasic_spAtto",
"StepBasic_spCenti",
"StepBasic_spDeca",
"StepBasic_spDeci",
"StepBasic_spExa",
"StepBasic_spFemto",
"StepBasic_spGiga",
"StepBasic_spHecto",
"StepBasic_spKilo",
"StepBasic_spMega",
"StepBasic_spMicro",
"StepBasic_spMilli",
"StepBasic_spNano",
"StepBasic_spPeta",
"StepBasic_spPico",
"StepBasic_spTera",
"StepBasic_sunAmpere",
"StepBasic_sunBecquerel",
"StepBasic_sunCandela",
"StepBasic_sunCoulomb",
"StepBasic_sunDegreeCelsius",
"StepBasic_sunFarad",
"StepBasic_sunGram",
"StepBasic_sunGray",
"StepBasic_sunHenry",
"StepBasic_sunHertz",
"StepBasic_sunJoule",
"StepBasic_sunKelvin",
"StepBasic_sunLumen",
"StepBasic_sunLux",
"StepBasic_sunMetre",
"StepBasic_sunMole",
"StepBasic_sunNewton",
"StepBasic_sunOhm",
"StepBasic_sunPascal",
"StepBasic_sunRadian",
"StepBasic_sunSecond",
"StepBasic_sunSiemens",
"StepBasic_sunSievert",
"StepBasic_sunSteradian",
"StepBasic_sunTesla",
"StepBasic_sunVolt",
"StepBasic_sunWatt",
"StepBasic_sunWeber"
]
class StepBasic_Action(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ActionRepresentation of STEP entity ActionRepresentation of STEP entity Action
    """
    def ChosenMethod(self) -> StepBasic_ActionMethod: 
        """
        Returns field ChosenMethod
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aChosenMethod : StepBasic_ActionMethod) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetChosenMethod(self,ChosenMethod : StepBasic_ActionMethod) -> None: 
        """
        Set field ChosenMethod
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
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
class StepBasic_ActionAssignment(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ActionAssignmentRepresentation of STEP entity ActionAssignmentRepresentation of STEP entity ActionAssignment
    """
    def AssignedAction(self) -> StepBasic_Action: 
        """
        Returns field AssignedAction
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
    def Init(self,aAssignedAction : StepBasic_Action) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetAssignedAction(self,AssignedAction : StepBasic_Action) -> None: 
        """
        Set field AssignedAction
        """
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
class StepBasic_ActionMethod(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ActionMethodRepresentation of STEP entity ActionMethodRepresentation of STEP entity ActionMethod
    """
    def Consequence(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Consequence
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aConsequence : OCP.TCollection.TCollection_HAsciiString,aPurpose : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def Purpose(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Purpose
        """
    def SetConsequence(self,Consequence : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Consequence
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetPurpose(self,Purpose : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Purpose
        """
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
class StepBasic_ActionRequestAssignment(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ActionRequestAssignmentRepresentation of STEP entity ActionRequestAssignmentRepresentation of STEP entity ActionRequestAssignment
    """
    def AssignedActionRequest(self) -> StepBasic_VersionedActionRequest: 
        """
        Returns field AssignedActionRequest
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
    def Init(self,aAssignedActionRequest : StepBasic_VersionedActionRequest) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetAssignedActionRequest(self,AssignedActionRequest : StepBasic_VersionedActionRequest) -> None: 
        """
        Set field AssignedActionRequest
        """
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
class StepBasic_ActionRequestSolution(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ActionRequestSolutionRepresentation of STEP entity ActionRequestSolutionRepresentation of STEP entity ActionRequestSolution
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
    def Init(self,aMethod : StepBasic_ActionMethod,aRequest : StepBasic_VersionedActionRequest) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Method(self) -> StepBasic_ActionMethod: 
        """
        Returns field Method
        """
    def Request(self) -> StepBasic_VersionedActionRequest: 
        """
        Returns field Request
        """
    def SetMethod(self,Method : StepBasic_ActionMethod) -> None: 
        """
        Set field Method
        """
    def SetRequest(self,Request : StepBasic_VersionedActionRequest) -> None: 
        """
        Set field Request
        """
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
class StepBasic_Address(OCP.Standard.Standard_Transient):
    def Country(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def ElectronicMailAddress(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def FacsimileNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasCountry(self) -> bool: 
        """
        None
        """
    def HasElectronicMailAddress(self) -> bool: 
        """
        None
        """
    def HasFacsimileNumber(self) -> bool: 
        """
        None
        """
    def HasInternalLocation(self) -> bool: 
        """
        None
        """
    def HasPostalBox(self) -> bool: 
        """
        None
        """
    def HasPostalCode(self) -> bool: 
        """
        None
        """
    def HasRegion(self) -> bool: 
        """
        None
        """
    def HasStreet(self) -> bool: 
        """
        None
        """
    def HasStreetNumber(self) -> bool: 
        """
        None
        """
    def HasTelephoneNumber(self) -> bool: 
        """
        None
        """
    def HasTelexNumber(self) -> bool: 
        """
        None
        """
    def HasTown(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAinternalLocation : bool,aInternalLocation : OCP.TCollection.TCollection_HAsciiString,hasAstreetNumber : bool,aStreetNumber : OCP.TCollection.TCollection_HAsciiString,hasAstreet : bool,aStreet : OCP.TCollection.TCollection_HAsciiString,hasApostalBox : bool,aPostalBox : OCP.TCollection.TCollection_HAsciiString,hasAtown : bool,aTown : OCP.TCollection.TCollection_HAsciiString,hasAregion : bool,aRegion : OCP.TCollection.TCollection_HAsciiString,hasApostalCode : bool,aPostalCode : OCP.TCollection.TCollection_HAsciiString,hasAcountry : bool,aCountry : OCP.TCollection.TCollection_HAsciiString,hasAfacsimileNumber : bool,aFacsimileNumber : OCP.TCollection.TCollection_HAsciiString,hasAtelephoneNumber : bool,aTelephoneNumber : OCP.TCollection.TCollection_HAsciiString,hasAelectronicMailAddress : bool,aElectronicMailAddress : OCP.TCollection.TCollection_HAsciiString,hasAtelexNumber : bool,aTelexNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def InternalLocation(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def PostalBox(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PostalCode(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Region(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetCountry(self,aCountry : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetElectronicMailAddress(self,aElectronicMailAddress : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFacsimileNumber(self,aFacsimileNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetInternalLocation(self,aInternalLocation : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPostalBox(self,aPostalBox : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPostalCode(self,aPostalCode : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRegion(self,aRegion : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStreet(self,aStreet : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStreetNumber(self,aStreetNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTelephoneNumber(self,aTelephoneNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTelexNumber(self,aTelexNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTown(self,aTown : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def Street(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def StreetNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def TelephoneNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def TelexNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Town(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def UnSetCountry(self) -> None: 
        """
        None
        """
    def UnSetElectronicMailAddress(self) -> None: 
        """
        None
        """
    def UnSetFacsimileNumber(self) -> None: 
        """
        None
        """
    def UnSetInternalLocation(self) -> None: 
        """
        None
        """
    def UnSetPostalBox(self) -> None: 
        """
        None
        """
    def UnSetPostalCode(self) -> None: 
        """
        None
        """
    def UnSetRegion(self) -> None: 
        """
        None
        """
    def UnSetStreet(self) -> None: 
        """
        None
        """
    def UnSetStreetNumber(self) -> None: 
        """
        None
        """
    def UnSetTelephoneNumber(self) -> None: 
        """
        None
        """
    def UnSetTelexNumber(self) -> None: 
        """
        None
        """
    def UnSetTown(self) -> None: 
        """
        None
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
class StepBasic_AheadOrBehind():
    """
    None

    Members:

      StepBasic_aobAhead

      StepBasic_aobExact

      StepBasic_aobBehind
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StepBasic_aobAhead: OCP.StepBasic.StepBasic_AheadOrBehind # value = StepBasic_AheadOrBehind.StepBasic_aobAhead
    StepBasic_aobBehind: OCP.StepBasic.StepBasic_AheadOrBehind # value = StepBasic_AheadOrBehind.StepBasic_aobBehind
    StepBasic_aobExact: OCP.StepBasic.StepBasic_AheadOrBehind # value = StepBasic_AheadOrBehind.StepBasic_aobExact
    __entries: dict # value = {'StepBasic_aobAhead': (StepBasic_AheadOrBehind.StepBasic_aobAhead, None), 'StepBasic_aobExact': (StepBasic_AheadOrBehind.StepBasic_aobExact, None), 'StepBasic_aobBehind': (StepBasic_AheadOrBehind.StepBasic_aobBehind, None)}
    __members__: dict # value = {'StepBasic_aobAhead': StepBasic_AheadOrBehind.StepBasic_aobAhead, 'StepBasic_aobExact': StepBasic_AheadOrBehind.StepBasic_aobExact, 'StepBasic_aobBehind': StepBasic_AheadOrBehind.StepBasic_aobBehind}
    pass
class StepBasic_ApplicationContext(OCP.Standard.Standard_Transient):
    def Application(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Init(self,aApplication : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def SetApplication(self,aApplication : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ApplicationContextElement(OCP.Standard.Standard_Transient):
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
    def FrameOfReference(self) -> StepBasic_ApplicationContext: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aFrameOfReference : StepBasic_ApplicationContext) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ApplicationContext) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ApplicationProtocolDefinition(OCP.Standard.Standard_Transient):
    def Application(self) -> StepBasic_ApplicationContext: 
        """
        None
        """
    def ApplicationInterpretedModelSchemaName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ApplicationProtocolYear(self) -> int: 
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
    def Init(self,aStatus : OCP.TCollection.TCollection_HAsciiString,aApplicationInterpretedModelSchemaName : OCP.TCollection.TCollection_HAsciiString,aApplicationProtocolYear : int,aApplication : StepBasic_ApplicationContext) -> None: 
        """
        None
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
    def SetApplication(self,aApplication : StepBasic_ApplicationContext) -> None: 
        """
        None
        """
    def SetApplicationInterpretedModelSchemaName(self,aApplicationInterpretedModelSchemaName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetApplicationProtocolYear(self,aApplicationProtocolYear : int) -> None: 
        """
        None
        """
    def SetStatus(self,aStatus : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def Status(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
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
class StepBasic_Approval(OCP.Standard.Standard_Transient):
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
    def Init(self,aStatus : StepBasic_ApprovalStatus,aLevel : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Level(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetLevel(self,aLevel : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStatus(self,aStatus : StepBasic_ApprovalStatus) -> None: 
        """
        None
        """
    def Status(self) -> StepBasic_ApprovalStatus: 
        """
        None
        """
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
class StepBasic_ApprovalAssignment(OCP.Standard.Standard_Transient):
    def AssignedApproval(self) -> StepBasic_Approval: 
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
    def Init(self,aAssignedApproval : StepBasic_Approval) -> None: 
        """
        None
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
    def SetAssignedApproval(self,aAssignedApproval : StepBasic_Approval) -> None: 
        """
        None
        """
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
class StepBasic_ApprovalDateTime(OCP.Standard.Standard_Transient):
    """
    Added from StepBasic Rev2 to Rev4Added from StepBasic Rev2 to Rev4Added from StepBasic Rev2 to Rev4
    """
    def DateTime(self) -> StepBasic_DateTimeSelect: 
        """
        None
        """
    def DatedApproval(self) -> StepBasic_Approval: 
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
    def Init(self,aDateTime : StepBasic_DateTimeSelect,aDatedApproval : StepBasic_Approval) -> None: 
        """
        None
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
    def SetDateTime(self,aDateTime : StepBasic_DateTimeSelect) -> None: 
        """
        None
        """
    def SetDatedApproval(self,aDatedApproval : StepBasic_Approval) -> None: 
        """
        None
        """
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
class StepBasic_ApprovalPersonOrganization(OCP.Standard.Standard_Transient):
    def AuthorizedApproval(self) -> StepBasic_Approval: 
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
    def Init(self,aPersonOrganization : StepBasic_PersonOrganizationSelect,aAuthorizedApproval : StepBasic_Approval,aRole : StepBasic_ApprovalRole) -> None: 
        """
        None
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
    def PersonOrganization(self) -> StepBasic_PersonOrganizationSelect: 
        """
        None
        """
    def Role(self) -> StepBasic_ApprovalRole: 
        """
        None
        """
    def SetAuthorizedApproval(self,aAuthorizedApproval : StepBasic_Approval) -> None: 
        """
        None
        """
    def SetPersonOrganization(self,aPersonOrganization : StepBasic_PersonOrganizationSelect) -> None: 
        """
        None
        """
    def SetRole(self,aRole : StepBasic_ApprovalRole) -> None: 
        """
        None
        """
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
class StepBasic_ApprovalRelationship(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingApproval : StepBasic_Approval,aRelatedApproval : StepBasic_Approval) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def RelatedApproval(self) -> StepBasic_Approval: 
        """
        None
        """
    def RelatingApproval(self) -> StepBasic_Approval: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRelatedApproval(self,aRelatedApproval : StepBasic_Approval) -> None: 
        """
        None
        """
    def SetRelatingApproval(self,aRelatingApproval : StepBasic_Approval) -> None: 
        """
        None
        """
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
class StepBasic_ApprovalRole(OCP.Standard.Standard_Transient):
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
    def Init(self,aRole : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Role(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetRole(self,aRole : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ApprovalStatus(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_NamedUnit(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_Array1OfApproval():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfApproval) -> StepBasic_Array1OfApproval: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_Approval: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Approval: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Approval: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_Approval: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_Approval) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_Approval: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfApproval) -> StepBasic_Array1OfApproval: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Approval) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Approval: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepBasic_Approval,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfApproval) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Array1OfDerivedUnitElement():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfDerivedUnitElement) -> StepBasic_Array1OfDerivedUnitElement: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_DerivedUnitElement: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_DerivedUnitElement: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_DerivedUnitElement: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_DerivedUnitElement: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_DerivedUnitElement) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_DerivedUnitElement: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfDerivedUnitElement) -> StepBasic_Array1OfDerivedUnitElement: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_DerivedUnitElement) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_DerivedUnitElement: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepBasic_DerivedUnitElement,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfDerivedUnitElement) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Array1OfDocument():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfDocument) -> StepBasic_Array1OfDocument: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_Document: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Document: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Document: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_Document: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_Document) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_Document: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfDocument) -> StepBasic_Array1OfDocument: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Document) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Document: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfDocument) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepBasic_Document,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Array1OfNamedUnit():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfNamedUnit) -> StepBasic_Array1OfNamedUnit: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_NamedUnit: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_NamedUnit: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_NamedUnit: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_NamedUnit: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_NamedUnit) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_NamedUnit: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfNamedUnit) -> StepBasic_Array1OfNamedUnit: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_NamedUnit) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_NamedUnit: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfNamedUnit) -> None: ...
    @overload
    def __init__(self,theBegin : StepBasic_NamedUnit,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Array1OfOrganization():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfOrganization) -> StepBasic_Array1OfOrganization: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_Organization: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Organization: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Organization: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_Organization: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_Organization) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_Organization: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfOrganization) -> StepBasic_Array1OfOrganization: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Organization) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Organization: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfOrganization) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepBasic_Organization,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Array1OfPerson():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfPerson) -> StepBasic_Array1OfPerson: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_Person: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Person: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Person: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_Person: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_Person) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_Person: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfPerson) -> StepBasic_Array1OfPerson: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Person) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Person: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepBasic_Person,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfPerson) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Array1OfProduct():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfProduct) -> StepBasic_Array1OfProduct: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_Product: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Product: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Product: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_Product: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_Product) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_Product: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfProduct) -> StepBasic_Array1OfProduct: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Product) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Product: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepBasic_Product,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfProduct) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Array1OfProductContext():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfProductContext) -> StepBasic_Array1OfProductContext: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_ProductContext: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_ProductContext: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_ProductContext: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_ProductContext: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_ProductContext) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_ProductContext: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfProductContext) -> StepBasic_Array1OfProductContext: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_ProductContext) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_ProductContext: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepBasic_ProductContext,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfProductContext) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Array1OfProductDefinition():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfProductDefinition) -> StepBasic_Array1OfProductDefinition: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_ProductDefinition: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_ProductDefinition: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_ProductDefinition: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_ProductDefinition: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_ProductDefinition) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_ProductDefinition: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfProductDefinition) -> StepBasic_Array1OfProductDefinition: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_ProductDefinition) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_ProductDefinition: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfProductDefinition) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepBasic_ProductDefinition,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Array1OfUncertaintyMeasureWithUnit():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepBasic_Array1OfUncertaintyMeasureWithUnit) -> StepBasic_Array1OfUncertaintyMeasureWithUnit: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Variable value access
        """
    def First(self) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Returns first element
        """
    def Init(self,theValue : StepBasic_UncertaintyMeasureWithUnit) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfUncertaintyMeasureWithUnit) -> StepBasic_Array1OfUncertaintyMeasureWithUnit: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_UncertaintyMeasureWithUnit) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfUncertaintyMeasureWithUnit) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepBasic_UncertaintyMeasureWithUnit,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepBasic_Date(OCP.Standard.Standard_Transient):
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
    def Init(self,aYearComponent : int) -> None: 
        """
        None
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
    def SetYearComponent(self,aYearComponent : int) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def YearComponent(self) -> int: 
        """
        None
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
class StepBasic_Certification(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CertificationRepresentation of STEP entity CertificationRepresentation of STEP entity Certification
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPurpose : OCP.TCollection.TCollection_HAsciiString,aKind : StepBasic_CertificationType) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Kind(self) -> StepBasic_CertificationType: 
        """
        Returns field Kind
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def Purpose(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Purpose
        """
    def SetKind(self,Kind : StepBasic_CertificationType) -> None: 
        """
        Set field Kind
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetPurpose(self,Purpose : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Purpose
        """
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
class StepBasic_CertificationAssignment(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CertificationAssignmentRepresentation of STEP entity CertificationAssignmentRepresentation of STEP entity CertificationAssignment
    """
    def AssignedCertification(self) -> StepBasic_Certification: 
        """
        Returns field AssignedCertification
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
    def Init(self,aAssignedCertification : StepBasic_Certification) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetAssignedCertification(self,AssignedCertification : StepBasic_Certification) -> None: 
        """
        Set field AssignedCertification
        """
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
class StepBasic_CertificationType(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CertificationTypeRepresentation of STEP entity CertificationTypeRepresentation of STEP entity CertificationType
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
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
    def Init(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
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
class StepBasic_CharacterizedObject(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CharacterizedObjectRepresentation of STEP entity CharacterizedObjectRepresentation of STEP entity CharacterizedObject
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
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
class StepBasic_Contract(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ContractRepresentation of STEP entity ContractRepresentation of STEP entity Contract
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPurpose : OCP.TCollection.TCollection_HAsciiString,aKind : StepBasic_ContractType) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Kind(self) -> StepBasic_ContractType: 
        """
        Returns field Kind
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def Purpose(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Purpose
        """
    def SetKind(self,Kind : StepBasic_ContractType) -> None: 
        """
        Set field Kind
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetPurpose(self,Purpose : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Purpose
        """
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
class StepBasic_ContractAssignment(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ContractAssignmentRepresentation of STEP entity ContractAssignmentRepresentation of STEP entity ContractAssignment
    """
    def AssignedContract(self) -> StepBasic_Contract: 
        """
        Returns field AssignedContract
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
    def Init(self,aAssignedContract : StepBasic_Contract) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetAssignedContract(self,AssignedContract : StepBasic_Contract) -> None: 
        """
        Set field AssignedContract
        """
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
class StepBasic_ContractType(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ContractTypeRepresentation of STEP entity ContractTypeRepresentation of STEP entity ContractType
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
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
    def Init(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
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
class StepBasic_ConversionBasedUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def ConversionFactor(self) -> StepBasic_MeasureWithUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents,aName : OCP.TCollection.TCollection_HAsciiString,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetConversionFactor(self,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ConversionBasedUnitAndAreaUnit(StepBasic_ConversionBasedUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def AreaUnit(self) -> StepBasic_AreaUnit: 
        """
        None
        """
    def ConversionFactor(self) -> StepBasic_MeasureWithUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents,aName : OCP.TCollection.TCollection_HAsciiString,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetAreaUnit(self,anAreaUnit : StepBasic_AreaUnit) -> None: 
        """
        None
        """
    def SetConversionFactor(self,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ConversionBasedUnitAndLengthUnit(StepBasic_ConversionBasedUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def ConversionFactor(self) -> StepBasic_MeasureWithUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents,aName : OCP.TCollection.TCollection_HAsciiString,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
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
    def LengthUnit(self) -> StepBasic_LengthUnit: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetConversionFactor(self,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetLengthUnit(self,aLengthUnit : StepBasic_LengthUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ConversionBasedUnitAndMassUnit(StepBasic_ConversionBasedUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def ConversionFactor(self) -> StepBasic_MeasureWithUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents,aName : OCP.TCollection.TCollection_HAsciiString,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
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
    def MassUnit(self) -> StepBasic_MassUnit: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetConversionFactor(self,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetMassUnit(self,aMassUnit : StepBasic_MassUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ConversionBasedUnitAndPlaneAngleUnit(StepBasic_ConversionBasedUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def ConversionFactor(self) -> StepBasic_MeasureWithUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents,aName : OCP.TCollection.TCollection_HAsciiString,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PlaneAngleUnit(self) -> StepBasic_PlaneAngleUnit: 
        """
        None
        """
    def SetConversionFactor(self,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPlaneAngleUnit(self,aPlaneAngleUnit : StepBasic_PlaneAngleUnit) -> None: 
        """
        None
        """
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
class StepBasic_ConversionBasedUnitAndRatioUnit(StepBasic_ConversionBasedUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def ConversionFactor(self) -> StepBasic_MeasureWithUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents,aName : OCP.TCollection.TCollection_HAsciiString,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def RatioUnit(self) -> StepBasic_RatioUnit: 
        """
        None
        """
    def SetConversionFactor(self,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRatioUnit(self,aRatioUnit : StepBasic_RatioUnit) -> None: 
        """
        None
        """
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
class StepBasic_ConversionBasedUnitAndSolidAngleUnit(StepBasic_ConversionBasedUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def ConversionFactor(self) -> StepBasic_MeasureWithUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents,aName : OCP.TCollection.TCollection_HAsciiString,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetConversionFactor(self,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSolidAngleUnit(self,aSolidAngleUnit : StepBasic_SolidAngleUnit) -> None: 
        """
        None
        """
    def SolidAngleUnit(self) -> StepBasic_SolidAngleUnit: 
        """
        None
        """
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
class StepBasic_ConversionBasedUnitAndTimeUnit(StepBasic_ConversionBasedUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def ConversionFactor(self) -> StepBasic_MeasureWithUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents,aName : OCP.TCollection.TCollection_HAsciiString,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetConversionFactor(self,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTimeUnit(self,aTimeUnit : StepBasic_TimeUnit) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TimeUnit(self) -> StepBasic_TimeUnit: 
        """
        None
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
class StepBasic_ConversionBasedUnitAndVolumeUnit(StepBasic_ConversionBasedUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def ConversionFactor(self) -> StepBasic_MeasureWithUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents,aName : OCP.TCollection.TCollection_HAsciiString,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetConversionFactor(self,aConversionFactor : StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetVolumeUnit(self,aVolumeUnit : StepBasic_VolumeUnit) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def VolumeUnit(self) -> StepBasic_VolumeUnit: 
        """
        None
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
class StepBasic_CoordinatedUniversalTimeOffset(OCP.Standard.Standard_Transient):
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
    def HasMinuteOffset(self) -> bool: 
        """
        None
        """
    def HourOffset(self) -> int: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aHourOffset : int,hasAminuteOffset : bool,aMinuteOffset : int,aSense : StepBasic_AheadOrBehind) -> None: 
        """
        None
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
    def MinuteOffset(self) -> int: 
        """
        None
        """
    def Sense(self) -> StepBasic_AheadOrBehind: 
        """
        None
        """
    def SetHourOffset(self,aHourOffset : int) -> None: 
        """
        None
        """
    def SetMinuteOffset(self,aMinuteOffset : int) -> None: 
        """
        None
        """
    def SetSense(self,aSense : StepBasic_AheadOrBehind) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetMinuteOffset(self) -> None: 
        """
        None
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
class StepBasic_CalendarDate(StepBasic_Date, OCP.Standard.Standard_Transient):
    def DayComponent(self) -> int: 
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
    def Init(self,aYearComponent : int,aDayComponent : int,aMonthComponent : int) -> None: 
        """
        None
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
    def MonthComponent(self) -> int: 
        """
        None
        """
    def SetDayComponent(self,aDayComponent : int) -> None: 
        """
        None
        """
    def SetMonthComponent(self,aMonthComponent : int) -> None: 
        """
        None
        """
    def SetYearComponent(self,aYearComponent : int) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def YearComponent(self) -> int: 
        """
        None
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
class StepBasic_DateAndTime(OCP.Standard.Standard_Transient):
    def DateComponent(self) -> StepBasic_Date: 
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
    def Init(self,aDateComponent : StepBasic_Date,aTimeComponent : StepBasic_LocalTime) -> None: 
        """
        None
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
    def SetDateComponent(self,aDateComponent : StepBasic_Date) -> None: 
        """
        None
        """
    def SetTimeComponent(self,aTimeComponent : StepBasic_LocalTime) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TimeComponent(self) -> StepBasic_LocalTime: 
        """
        None
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
class StepBasic_DateAndTimeAssignment(OCP.Standard.Standard_Transient):
    def AssignedDateAndTime(self) -> StepBasic_DateAndTime: 
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
    def Init(self,aAssignedDateAndTime : StepBasic_DateAndTime,aRole : StepBasic_DateTimeRole) -> None: 
        """
        None
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
    def Role(self) -> StepBasic_DateTimeRole: 
        """
        None
        """
    def SetAssignedDateAndTime(self,aAssignedDateAndTime : StepBasic_DateAndTime) -> None: 
        """
        None
        """
    def SetRole(self,aRole : StepBasic_DateTimeRole) -> None: 
        """
        None
        """
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
class StepBasic_DateAssignment(OCP.Standard.Standard_Transient):
    def AssignedDate(self) -> StepBasic_Date: 
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
    def Init(self,aAssignedDate : StepBasic_Date,aRole : StepBasic_DateRole) -> None: 
        """
        None
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
    def Role(self) -> StepBasic_DateRole: 
        """
        None
        """
    def SetAssignedDate(self,aAssignedDate : StepBasic_Date) -> None: 
        """
        None
        """
    def SetRole(self,aRole : StepBasic_DateRole) -> None: 
        """
        None
        """
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
class StepBasic_DateRole(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_DateTimeRole(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_DateTimeSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a DateTimeSelect Kind Entity that is : 1 -> Date 2 -> LocalTime 3 -> DateAndTime 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Date(self) -> StepBasic_Date: 
        """
        returns Value as a Date (Null if another type)
        """
    def DateAndTime(self) -> StepBasic_DateAndTime: 
        """
        returns Value as a DateAndTime (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def LocalTime(self) -> StepBasic_LocalTime: 
        """
        returns Value as a LocalTime (Null if another type)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepBasic_DerivedUnit(OCP.Standard.Standard_Transient):
    """
    Added from StepBasic Rev2 to Rev4Added from StepBasic Rev2 to Rev4Added from StepBasic Rev2 to Rev4
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
    def Elements(self) -> StepBasic_HArray1OfDerivedUnitElement: 
        """
        None
        """
    def ElementsValue(self,num : int) -> StepBasic_DerivedUnitElement: 
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
    def Init(self,elements : StepBasic_HArray1OfDerivedUnitElement) -> None: 
        """
        None
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
    def NbElements(self) -> int: 
        """
        None
        """
    def SetElements(self,elements : StepBasic_HArray1OfDerivedUnitElement) -> None: 
        """
        None
        """
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
class StepBasic_DerivedUnitElement(OCP.Standard.Standard_Transient):
    """
    Added from StepBasic Rev2 to Rev4Added from StepBasic Rev2 to Rev4Added from StepBasic Rev2 to Rev4
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
    def Exponent(self) -> float: 
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
    def Init(self,aUnit : StepBasic_NamedUnit,aExponent : float) -> None: 
        """
        None
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
    def SetExponent(self,aExponent : float) -> None: 
        """
        None
        """
    def SetUnit(self,aUnit : StepBasic_NamedUnit) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unit(self) -> StepBasic_NamedUnit: 
        """
        None
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
class StepBasic_ProductDefinitionContext(StepBasic_ApplicationContextElement, OCP.Standard.Standard_Transient):
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
    def FrameOfReference(self) -> StepBasic_ApplicationContext: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aFrameOfReference : StepBasic_ApplicationContext,aLifeCycleStage : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def LifeCycleStage(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ApplicationContext) -> None: 
        """
        None
        """
    def SetLifeCycleStage(self,aLifeCycleStage : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_Document(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DocumentRepresentation of STEP entity DocumentRepresentation of STEP entity Document
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aKind : StepBasic_DocumentType) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Kind(self) -> StepBasic_DocumentType: 
        """
        Returns field Kind
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetKind(self,Kind : StepBasic_DocumentType) -> None: 
        """
        Set field Kind
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
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
class StepBasic_DimensionalExponents(OCP.Standard.Standard_Transient):
    def AmountOfSubstanceExponent(self) -> float: 
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
    def ElectricCurrentExponent(self) -> float: 
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
    def Init(self,aLengthExponent : float,aMassExponent : float,aTimeExponent : float,aElectricCurrentExponent : float,aThermodynamicTemperatureExponent : float,aAmountOfSubstanceExponent : float,aLuminousIntensityExponent : float) -> None: 
        """
        None
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
    def LengthExponent(self) -> float: 
        """
        None
        """
    def LuminousIntensityExponent(self) -> float: 
        """
        None
        """
    def MassExponent(self) -> float: 
        """
        None
        """
    def SetAmountOfSubstanceExponent(self,aAmountOfSubstanceExponent : float) -> None: 
        """
        None
        """
    def SetElectricCurrentExponent(self,aElectricCurrentExponent : float) -> None: 
        """
        None
        """
    def SetLengthExponent(self,aLengthExponent : float) -> None: 
        """
        None
        """
    def SetLuminousIntensityExponent(self,aLuminousIntensityExponent : float) -> None: 
        """
        None
        """
    def SetMassExponent(self,aMassExponent : float) -> None: 
        """
        None
        """
    def SetThermodynamicTemperatureExponent(self,aThermodynamicTemperatureExponent : float) -> None: 
        """
        None
        """
    def SetTimeExponent(self,aTimeExponent : float) -> None: 
        """
        None
        """
    def ThermodynamicTemperatureExponent(self) -> float: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TimeExponent(self) -> float: 
        """
        None
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
class StepBasic_DigitalDocument(StepBasic_Document, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aKind : StepBasic_DocumentType) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Kind(self) -> StepBasic_DocumentType: 
        """
        Returns field Kind
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetKind(self,Kind : StepBasic_DocumentType) -> None: 
        """
        Set field Kind
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
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
class StepBasic_DocumentFile(StepBasic_Document, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DocumentFileRepresentation of STEP entity DocumentFileRepresentation of STEP entity DocumentFile
    """
    def CharacterizedObject(self) -> StepBasic_CharacterizedObject: 
        """
        Returns data for supertype CharacterizedObject
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aDocument_Id : OCP.TCollection.TCollection_HAsciiString,aDocument_Name : OCP.TCollection.TCollection_HAsciiString,hasDocument_Description : bool,aDocument_Description : OCP.TCollection.TCollection_HAsciiString,aDocument_Kind : StepBasic_DocumentType,aCharacterizedObject_Name : OCP.TCollection.TCollection_HAsciiString,hasCharacterizedObject_Description : bool,aCharacterizedObject_Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Kind(self) -> StepBasic_DocumentType: 
        """
        Returns field Kind
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetCharacterizedObject(self,CharacterizedObject : StepBasic_CharacterizedObject) -> None: 
        """
        Set data for supertype CharacterizedObject
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetKind(self,Kind : StepBasic_DocumentType) -> None: 
        """
        Set field Kind
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
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
class StepBasic_DocumentProductAssociation(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DocumentProductAssociationRepresentation of STEP entity DocumentProductAssociationRepresentation of STEP entity DocumentProductAssociation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingDocument : StepBasic_Document,aRelatedProduct : StepBasic_ProductOrFormationOrDefinition) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedProduct(self) -> StepBasic_ProductOrFormationOrDefinition: 
        """
        Returns field RelatedProduct
        """
    def RelatingDocument(self) -> StepBasic_Document: 
        """
        Returns field RelatingDocument
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedProduct(self,RelatedProduct : StepBasic_ProductOrFormationOrDefinition) -> None: 
        """
        Set field RelatedProduct
        """
    def SetRelatingDocument(self,RelatingDocument : StepBasic_Document) -> None: 
        """
        Set field RelatingDocument
        """
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
class StepBasic_DocumentProductEquivalence(StepBasic_DocumentProductAssociation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DocumentProductEquivalenceRepresentation of STEP entity DocumentProductEquivalenceRepresentation of STEP entity DocumentProductEquivalence
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingDocument : StepBasic_Document,aRelatedProduct : StepBasic_ProductOrFormationOrDefinition) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedProduct(self) -> StepBasic_ProductOrFormationOrDefinition: 
        """
        Returns field RelatedProduct
        """
    def RelatingDocument(self) -> StepBasic_Document: 
        """
        Returns field RelatingDocument
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedProduct(self,RelatedProduct : StepBasic_ProductOrFormationOrDefinition) -> None: 
        """
        Set field RelatedProduct
        """
    def SetRelatingDocument(self,RelatingDocument : StepBasic_Document) -> None: 
        """
        Set field RelatingDocument
        """
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
class StepBasic_DocumentReference(OCP.Standard.Standard_Transient):
    def AssignedDocument(self) -> StepBasic_Document: 
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
    def Init0(self,aAssignedDocument : StepBasic_Document,aSource : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def SetAssignedDocument(self,aAssignedDocument : StepBasic_Document) -> None: 
        """
        None
        """
    def SetSource(self,aSource : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def Source(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
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
class StepBasic_DocumentRelationship(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelating : StepBasic_Document,aRelated : StepBasic_Document) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def RelatedDocument(self) -> StepBasic_Document: 
        """
        None
        """
    def RelatingDocument(self) -> StepBasic_Document: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRelatedDocument(self,aRelated : StepBasic_Document) -> None: 
        """
        None
        """
    def SetRelatingDocument(self,aRelating : StepBasic_Document) -> None: 
        """
        None
        """
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
class StepBasic_DocumentRepresentationType(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DocumentRepresentationTypeRepresentation of STEP entity DocumentRepresentationTypeRepresentation of STEP entity DocumentRepresentationType
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aRepresentedDocument : StepBasic_Document) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RepresentedDocument(self) -> StepBasic_Document: 
        """
        Returns field RepresentedDocument
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRepresentedDocument(self,RepresentedDocument : StepBasic_Document) -> None: 
        """
        Set field RepresentedDocument
        """
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
class StepBasic_DocumentType(OCP.Standard.Standard_Transient):
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
    def Init(self,apdt : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def ProductDataType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetProductDataType(self,apdt : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_DocumentUsageConstraint(OCP.Standard.Standard_Transient):
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
    def Init(self,aSource : StepBasic_Document,ase : OCP.TCollection.TCollection_HAsciiString,asev : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def SetSource(self,aSource : StepBasic_Document) -> None: 
        """
        None
        """
    def SetSubjectElement(self,ase : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSubjectElementValue(self,asev : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def Source(self) -> StepBasic_Document: 
        """
        None
        """
    def SubjectElement(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SubjectElementValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
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
class StepBasic_Effectivity(OCP.Standard.Standard_Transient):
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
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aid : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def SetId(self,aid : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_EffectivityAssignment(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity EffectivityAssignmentRepresentation of STEP entity EffectivityAssignmentRepresentation of STEP entity EffectivityAssignment
    """
    def AssignedEffectivity(self) -> StepBasic_Effectivity: 
        """
        Returns field AssignedEffectivity
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
    def Init(self,aAssignedEffectivity : StepBasic_Effectivity) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetAssignedEffectivity(self,AssignedEffectivity : StepBasic_Effectivity) -> None: 
        """
        Set field AssignedEffectivity
        """
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
class StepBasic_EulerAngles(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity EulerAnglesRepresentation of STEP entity EulerAnglesRepresentation of STEP entity EulerAngles
    """
    def Angles(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns field Angles
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
    def Init(self,aAngles : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetAngles(self,Angles : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Set field Angles
        """
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
class StepBasic_IdentificationAssignment(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity IdentificationAssignmentRepresentation of STEP entity IdentificationAssignmentRepresentation of STEP entity IdentificationAssignment
    """
    def AssignedId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field AssignedId
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
    def Init(self,aAssignedId : OCP.TCollection.TCollection_HAsciiString,aRole : StepBasic_IdentificationRole) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Role(self) -> StepBasic_IdentificationRole: 
        """
        Returns field Role
        """
    def SetAssignedId(self,AssignedId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field AssignedId
        """
    def SetRole(self,Role : StepBasic_IdentificationRole) -> None: 
        """
        Set field Role
        """
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
class StepBasic_ExternalSource(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ExternalSourceRepresentation of STEP entity ExternalSourceRepresentation of STEP entity ExternalSource
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
    def Init(self,aSourceId : StepBasic_SourceItem) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetSourceId(self,SourceId : StepBasic_SourceItem) -> None: 
        """
        Set field SourceId
        """
    def SourceId(self) -> StepBasic_SourceItem: 
        """
        Returns field SourceId
        """
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
class StepBasic_ExternallyDefinedItem(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ExternallyDefinedItemRepresentation of STEP entity ExternallyDefinedItemRepresentation of STEP entity ExternallyDefinedItem
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
    def Init(self,aItemId : StepBasic_SourceItem,aSource : StepBasic_ExternalSource) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def ItemId(self) -> StepBasic_SourceItem: 
        """
        Returns field ItemId
        """
    def SetItemId(self,ItemId : StepBasic_SourceItem) -> None: 
        """
        Set field ItemId
        """
    def SetSource(self,Source : StepBasic_ExternalSource) -> None: 
        """
        Set field Source
        """
    def Source(self) -> StepBasic_ExternalSource: 
        """
        Returns field Source
        """
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
class StepBasic_GeneralProperty(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeneralPropertyRepresentation of STEP entity GeneralPropertyRepresentation of STEP entity GeneralProperty
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
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
class StepBasic_Group(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GroupRepresentation of STEP entity GroupRepresentation of STEP entity Group
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
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
class StepBasic_GroupAssignment(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GroupAssignmentRepresentation of STEP entity GroupAssignmentRepresentation of STEP entity GroupAssignment
    """
    def AssignedGroup(self) -> StepBasic_Group: 
        """
        Returns field AssignedGroup
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
    def Init(self,aAssignedGroup : StepBasic_Group) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetAssignedGroup(self,AssignedGroup : StepBasic_Group) -> None: 
        """
        Set field AssignedGroup
        """
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
class StepBasic_GroupRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GroupRelationshipRepresentation of STEP entity GroupRelationshipRepresentation of STEP entity GroupRelationship
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingGroup : StepBasic_Group,aRelatedGroup : StepBasic_Group) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedGroup(self) -> StepBasic_Group: 
        """
        Returns field RelatedGroup
        """
    def RelatingGroup(self) -> StepBasic_Group: 
        """
        Returns field RelatingGroup
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedGroup(self,RelatedGroup : StepBasic_Group) -> None: 
        """
        Set field RelatedGroup
        """
    def SetRelatingGroup(self,RelatingGroup : StepBasic_Group) -> None: 
        """
        Set field RelatingGroup
        """
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
class StepBasic_HArray1OfApproval(StepBasic_Array1OfApproval, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfApproval: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfApproval) -> StepBasic_Array1OfApproval: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfApproval: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_Approval: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Approval: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Approval: 
        """
        Variable value access
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
    def First(self) -> StepBasic_Approval: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_Approval) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_Approval: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfApproval) -> StepBasic_Array1OfApproval: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Approval) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Approval: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_Approval) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfApproval) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_HArray1OfDerivedUnitElement(StepBasic_Array1OfDerivedUnitElement, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfDerivedUnitElement: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfDerivedUnitElement) -> StepBasic_Array1OfDerivedUnitElement: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfDerivedUnitElement: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_DerivedUnitElement: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_DerivedUnitElement: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_DerivedUnitElement: 
        """
        Variable value access
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
    def First(self) -> StepBasic_DerivedUnitElement: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_DerivedUnitElement) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_DerivedUnitElement: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfDerivedUnitElement) -> StepBasic_Array1OfDerivedUnitElement: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_DerivedUnitElement) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_DerivedUnitElement: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_DerivedUnitElement) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfDerivedUnitElement) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_HArray1OfDocument(StepBasic_Array1OfDocument, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfDocument: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfDocument) -> StepBasic_Array1OfDocument: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfDocument: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_Document: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Document: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Document: 
        """
        Variable value access
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
    def First(self) -> StepBasic_Document: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_Document) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_Document: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfDocument) -> StepBasic_Array1OfDocument: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Document) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Document: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_Document) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfDocument) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_HArray1OfNamedUnit(StepBasic_Array1OfNamedUnit, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfNamedUnit: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfNamedUnit) -> StepBasic_Array1OfNamedUnit: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfNamedUnit: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_NamedUnit: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_NamedUnit: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_NamedUnit: 
        """
        Variable value access
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
    def First(self) -> StepBasic_NamedUnit: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_NamedUnit) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_NamedUnit: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfNamedUnit) -> StepBasic_Array1OfNamedUnit: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_NamedUnit) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_NamedUnit: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfNamedUnit) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_NamedUnit) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_HArray1OfOrganization(StepBasic_Array1OfOrganization, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfOrganization: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfOrganization) -> StepBasic_Array1OfOrganization: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfOrganization: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_Organization: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Organization: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Organization: 
        """
        Variable value access
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
    def First(self) -> StepBasic_Organization: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_Organization) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_Organization: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfOrganization) -> StepBasic_Array1OfOrganization: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Organization) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Organization: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_Organization) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfOrganization) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_HArray1OfPerson(StepBasic_Array1OfPerson, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfPerson: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfPerson) -> StepBasic_Array1OfPerson: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfPerson: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_Person: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Person: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Person: 
        """
        Variable value access
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
    def First(self) -> StepBasic_Person: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_Person) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_Person: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfPerson) -> StepBasic_Array1OfPerson: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Person) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Person: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepBasic_Array1OfPerson) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_Person) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_HArray1OfProduct(StepBasic_Array1OfProduct, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfProduct: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfProduct) -> StepBasic_Array1OfProduct: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfProduct: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_Product: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_Product: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_Product: 
        """
        Variable value access
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
    def First(self) -> StepBasic_Product: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_Product) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_Product: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfProduct) -> StepBasic_Array1OfProduct: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_Product) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_Product: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_Product) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfProduct) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_HArray1OfProductContext(StepBasic_Array1OfProductContext, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfProductContext: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfProductContext) -> StepBasic_Array1OfProductContext: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfProductContext: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_ProductContext: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_ProductContext: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_ProductContext: 
        """
        Variable value access
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
    def First(self) -> StepBasic_ProductContext: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_ProductContext) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_ProductContext: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfProductContext) -> StepBasic_Array1OfProductContext: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_ProductContext) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_ProductContext: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_ProductContext) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfProductContext) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_HArray1OfProductDefinition(StepBasic_Array1OfProductDefinition, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfProductDefinition: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfProductDefinition) -> StepBasic_Array1OfProductDefinition: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfProductDefinition: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_ProductDefinition: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_ProductDefinition: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_ProductDefinition: 
        """
        Variable value access
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
    def First(self) -> StepBasic_ProductDefinition: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_ProductDefinition) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_ProductDefinition: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfProductDefinition) -> StepBasic_Array1OfProductDefinition: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_ProductDefinition) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_ProductDefinition: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_ProductDefinition) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfProductDefinition) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_HArray1OfUncertaintyMeasureWithUnit(StepBasic_Array1OfUncertaintyMeasureWithUnit, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepBasic_Array1OfUncertaintyMeasureWithUnit: 
        """
        None
        """
    def Assign(self,theOther : StepBasic_Array1OfUncertaintyMeasureWithUnit) -> StepBasic_Array1OfUncertaintyMeasureWithUnit: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepBasic_Array1OfUncertaintyMeasureWithUnit: 
        """
        None
        """
    def ChangeFirst(self) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Variable value access
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
    def First(self) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : StepBasic_UncertaintyMeasureWithUnit) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : StepBasic_Array1OfUncertaintyMeasureWithUnit) -> StepBasic_Array1OfUncertaintyMeasureWithUnit: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepBasic_UncertaintyMeasureWithUnit) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> StepBasic_UncertaintyMeasureWithUnit: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepBasic_UncertaintyMeasureWithUnit) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepBasic_Array1OfUncertaintyMeasureWithUnit) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepBasic_ExternalIdentificationAssignment(StepBasic_IdentificationAssignment, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ExternalIdentificationAssignmentRepresentation of STEP entity ExternalIdentificationAssignmentRepresentation of STEP entity ExternalIdentificationAssignment
    """
    def AssignedId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field AssignedId
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
    def Init(self,aIdentificationAssignment_AssignedId : OCP.TCollection.TCollection_HAsciiString,aIdentificationAssignment_Role : StepBasic_IdentificationRole,aSource : StepBasic_ExternalSource) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Role(self) -> StepBasic_IdentificationRole: 
        """
        Returns field Role
        """
    def SetAssignedId(self,AssignedId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field AssignedId
        """
    def SetRole(self,Role : StepBasic_IdentificationRole) -> None: 
        """
        Set field Role
        """
    def SetSource(self,Source : StepBasic_ExternalSource) -> None: 
        """
        Set field Source
        """
    def Source(self) -> StepBasic_ExternalSource: 
        """
        Returns field Source
        """
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
class StepBasic_IdentificationRole(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity IdentificationRoleRepresentation of STEP entity IdentificationRoleRepresentation of STEP entity IdentificationRole
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
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
class StepBasic_MeasureWithUnit(OCP.Standard.Standard_Transient):
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
    def Init(self,aValueComponent : StepBasic_MeasureValueMember,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
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
    def SetUnitComponent(self,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
        """
    def SetValueComponent(self,aValueComponent : float) -> None: 
        """
        None
        """
    def SetValueComponentMember(self,val : StepBasic_MeasureValueMember) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnitComponent(self) -> StepBasic_Unit: 
        """
        None
        """
    def ValueComponent(self) -> float: 
        """
        None
        """
    def ValueComponentMember(self) -> StepBasic_MeasureValueMember: 
        """
        None
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
class StepBasic_LengthUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_LocalTime(OCP.Standard.Standard_Transient):
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
    def HasMinuteComponent(self) -> bool: 
        """
        None
        """
    def HasSecondComponent(self) -> bool: 
        """
        None
        """
    def HourComponent(self) -> int: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aHourComponent : int,hasAminuteComponent : bool,aMinuteComponent : int,hasAsecondComponent : bool,aSecondComponent : float,aZone : StepBasic_CoordinatedUniversalTimeOffset) -> None: 
        """
        None
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
    def MinuteComponent(self) -> int: 
        """
        None
        """
    def SecondComponent(self) -> float: 
        """
        None
        """
    def SetHourComponent(self,aHourComponent : int) -> None: 
        """
        None
        """
    def SetMinuteComponent(self,aMinuteComponent : int) -> None: 
        """
        None
        """
    def SetSecondComponent(self,aSecondComponent : float) -> None: 
        """
        None
        """
    def SetZone(self,aZone : StepBasic_CoordinatedUniversalTimeOffset) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetMinuteComponent(self) -> None: 
        """
        None
        """
    def UnSetSecondComponent(self) -> None: 
        """
        None
        """
    def Zone(self) -> StepBasic_CoordinatedUniversalTimeOffset: 
        """
        None
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
class StepBasic_MassMeasureWithUnit(StepBasic_MeasureWithUnit, OCP.Standard.Standard_Transient):
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
    def Init(self,aValueComponent : StepBasic_MeasureValueMember,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
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
    def SetUnitComponent(self,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
        """
    def SetValueComponent(self,aValueComponent : float) -> None: 
        """
        None
        """
    def SetValueComponentMember(self,val : StepBasic_MeasureValueMember) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnitComponent(self) -> StepBasic_Unit: 
        """
        None
        """
    def ValueComponent(self) -> float: 
        """
        None
        """
    def ValueComponentMember(self) -> StepBasic_MeasureValueMember: 
        """
        None
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
class StepBasic_MassUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity MassUnitRepresentation of STEP entity MassUnitRepresentation of STEP entity MassUnit
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_MeasureValueMember(OCP.StepData.StepData_SelectReal, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    for Select MeasureValue, i.e. : length_measure,time_measure,plane_angle_measure, solid_angle_measure,ratio_measure,parameter_value, context_dependent_measure,positive_length_measure, positive_plane_angle_measure,positive_ratio_measure, area_measure,volume_measure, count_measurefor Select MeasureValue, i.e. : length_measure,time_measure,plane_angle_measure, solid_angle_measure,ratio_measure,parameter_value, context_dependent_measure,positive_length_measure, positive_plane_angle_measure,positive_ratio_measure, area_measure,volume_measure, count_measurefor Select MeasureValue, i.e. : length_measure,time_measure,plane_angle_measure, solid_angle_measure,ratio_measure,parameter_value, context_dependent_measure,positive_length_measure, positive_plane_angle_measure,positive_ratio_measure, area_measure,volume_measure, count_measure
    """
    def Boolean(self) -> bool: 
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
    def Enum(self) -> int: 
        """
        None
        """
    def EnumText(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
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
    def Kind(self) -> int: 
        """
        None
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        None
        """
    def ParamType(self) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the Kind of the SelectMember, under the form of an enum ParamType
        """
    def Real(self) -> float: 
        """
        None
        """
    def SetBoolean(self,val : bool) -> None: 
        """
        None
        """
    def SetEnum(self,val : int,text : str='') -> None: 
        """
        None
        """
    def SetEnumText(self,val : int,text : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it)
        """
    def SetInteger(self,val : int) -> None: 
        """
        None
        """
    def SetKind(self,kind : int) -> None: 
        """
        None
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        None
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def String(self) -> str: 
        """
        None
        """
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
class StepBasic_LengthMeasureWithUnit(StepBasic_MeasureWithUnit, OCP.Standard.Standard_Transient):
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
    def Init(self,aValueComponent : StepBasic_MeasureValueMember,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
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
    def SetUnitComponent(self,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
        """
    def SetValueComponent(self,aValueComponent : float) -> None: 
        """
        None
        """
    def SetValueComponentMember(self,val : StepBasic_MeasureValueMember) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnitComponent(self) -> StepBasic_Unit: 
        """
        None
        """
    def ValueComponent(self) -> float: 
        """
        None
        """
    def ValueComponentMember(self) -> StepBasic_MeasureValueMember: 
        """
        None
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
class StepBasic_ProductContext(StepBasic_ApplicationContextElement, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisciplineType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FrameOfReference(self) -> StepBasic_ApplicationContext: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aFrameOfReference : StepBasic_ApplicationContext,aDisciplineType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDisciplineType(self,aDisciplineType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ApplicationContext) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_NameAssignment(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NameAssignmentRepresentation of STEP entity NameAssignmentRepresentation of STEP entity NameAssignment
    """
    def AssignedName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field AssignedName
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
    def Init(self,aAssignedName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetAssignedName(self,AssignedName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field AssignedName
        """
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
class StepBasic_AreaUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_ObjectRole(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ObjectRoleRepresentation of STEP entity ObjectRoleRepresentation of STEP entity ObjectRole
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
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
class StepBasic_OrdinalDate(StepBasic_Date, OCP.Standard.Standard_Transient):
    def DayComponent(self) -> int: 
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
    def Init(self,aYearComponent : int,aDayComponent : int) -> None: 
        """
        None
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
    def SetDayComponent(self,aDayComponent : int) -> None: 
        """
        None
        """
    def SetYearComponent(self,aYearComponent : int) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def YearComponent(self) -> int: 
        """
        None
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
class StepBasic_Organization(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasId(self) -> bool: 
        """
        None
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAid : bool,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetId(self,aId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetId(self) -> None: 
        """
        None
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
class StepBasic_OrganizationAssignment(OCP.Standard.Standard_Transient):
    def AssignedOrganization(self) -> StepBasic_Organization: 
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
    def Init(self,aAssignedOrganization : StepBasic_Organization,aRole : StepBasic_OrganizationRole) -> None: 
        """
        None
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
    def Role(self) -> StepBasic_OrganizationRole: 
        """
        None
        """
    def SetAssignedOrganization(self,aAssignedOrganization : StepBasic_Organization) -> None: 
        """
        None
        """
    def SetRole(self,aRole : StepBasic_OrganizationRole) -> None: 
        """
        None
        """
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
class StepBasic_OrganizationRole(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_OrganizationalAddress(StepBasic_Address, OCP.Standard.Standard_Transient):
    def Country(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ElectronicMailAddress(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def FacsimileNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasCountry(self) -> bool: 
        """
        None
        """
    def HasElectronicMailAddress(self) -> bool: 
        """
        None
        """
    def HasFacsimileNumber(self) -> bool: 
        """
        None
        """
    def HasInternalLocation(self) -> bool: 
        """
        None
        """
    def HasPostalBox(self) -> bool: 
        """
        None
        """
    def HasPostalCode(self) -> bool: 
        """
        None
        """
    def HasRegion(self) -> bool: 
        """
        None
        """
    def HasStreet(self) -> bool: 
        """
        None
        """
    def HasStreetNumber(self) -> bool: 
        """
        None
        """
    def HasTelephoneNumber(self) -> bool: 
        """
        None
        """
    def HasTelexNumber(self) -> bool: 
        """
        None
        """
    def HasTown(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAinternalLocation : bool,aInternalLocation : OCP.TCollection.TCollection_HAsciiString,hasAstreetNumber : bool,aStreetNumber : OCP.TCollection.TCollection_HAsciiString,hasAstreet : bool,aStreet : OCP.TCollection.TCollection_HAsciiString,hasApostalBox : bool,aPostalBox : OCP.TCollection.TCollection_HAsciiString,hasAtown : bool,aTown : OCP.TCollection.TCollection_HAsciiString,hasAregion : bool,aRegion : OCP.TCollection.TCollection_HAsciiString,hasApostalCode : bool,aPostalCode : OCP.TCollection.TCollection_HAsciiString,hasAcountry : bool,aCountry : OCP.TCollection.TCollection_HAsciiString,hasAfacsimileNumber : bool,aFacsimileNumber : OCP.TCollection.TCollection_HAsciiString,hasAtelephoneNumber : bool,aTelephoneNumber : OCP.TCollection.TCollection_HAsciiString,hasAelectronicMailAddress : bool,aElectronicMailAddress : OCP.TCollection.TCollection_HAsciiString,hasAtelexNumber : bool,aTelexNumber : OCP.TCollection.TCollection_HAsciiString,aOrganizations : StepBasic_HArray1OfOrganization,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def InternalLocation(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def NbOrganizations(self) -> int: 
        """
        None
        """
    def Organizations(self) -> StepBasic_HArray1OfOrganization: 
        """
        None
        """
    def OrganizationsValue(self,num : int) -> StepBasic_Organization: 
        """
        None
        """
    def PostalBox(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PostalCode(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Region(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetCountry(self,aCountry : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetElectronicMailAddress(self,aElectronicMailAddress : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFacsimileNumber(self,aFacsimileNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetInternalLocation(self,aInternalLocation : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrganizations(self,aOrganizations : StepBasic_HArray1OfOrganization) -> None: 
        """
        None
        """
    def SetPostalBox(self,aPostalBox : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPostalCode(self,aPostalCode : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRegion(self,aRegion : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStreet(self,aStreet : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStreetNumber(self,aStreetNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTelephoneNumber(self,aTelephoneNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTelexNumber(self,aTelexNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTown(self,aTown : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def Street(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def StreetNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def TelephoneNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def TelexNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Town(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def UnSetCountry(self) -> None: 
        """
        None
        """
    def UnSetElectronicMailAddress(self) -> None: 
        """
        None
        """
    def UnSetFacsimileNumber(self) -> None: 
        """
        None
        """
    def UnSetInternalLocation(self) -> None: 
        """
        None
        """
    def UnSetPostalBox(self) -> None: 
        """
        None
        """
    def UnSetPostalCode(self) -> None: 
        """
        None
        """
    def UnSetRegion(self) -> None: 
        """
        None
        """
    def UnSetStreet(self) -> None: 
        """
        None
        """
    def UnSetStreetNumber(self) -> None: 
        """
        None
        """
    def UnSetTelephoneNumber(self) -> None: 
        """
        None
        """
    def UnSetTelexNumber(self) -> None: 
        """
        None
        """
    def UnSetTown(self) -> None: 
        """
        None
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
class StepBasic_Person(OCP.Standard.Standard_Transient):
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
    def FirstName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstName(self) -> bool: 
        """
        None
        """
    def HasLastName(self) -> bool: 
        """
        None
        """
    def HasMiddleNames(self) -> bool: 
        """
        None
        """
    def HasPrefixTitles(self) -> bool: 
        """
        None
        """
    def HasSuffixTitles(self) -> bool: 
        """
        None
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,hasAlastName : bool,aLastName : OCP.TCollection.TCollection_HAsciiString,hasAfirstName : bool,aFirstName : OCP.TCollection.TCollection_HAsciiString,hasAmiddleNames : bool,aMiddleNames : OCP.Interface.Interface_HArray1OfHAsciiString,hasAprefixTitles : bool,aPrefixTitles : OCP.Interface.Interface_HArray1OfHAsciiString,hasAsuffixTitles : bool,aSuffixTitles : OCP.Interface.Interface_HArray1OfHAsciiString) -> None: 
        """
        None
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
    def LastName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def MiddleNames(self) -> OCP.Interface.Interface_HArray1OfHAsciiString: 
        """
        None
        """
    def MiddleNamesValue(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbMiddleNames(self) -> int: 
        """
        None
        """
    def NbPrefixTitles(self) -> int: 
        """
        None
        """
    def NbSuffixTitles(self) -> int: 
        """
        None
        """
    def PrefixTitles(self) -> OCP.Interface.Interface_HArray1OfHAsciiString: 
        """
        None
        """
    def PrefixTitlesValue(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetFirstName(self,aFirstName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetId(self,aId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetLastName(self,aLastName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetMiddleNames(self,aMiddleNames : OCP.Interface.Interface_HArray1OfHAsciiString) -> None: 
        """
        None
        """
    def SetPrefixTitles(self,aPrefixTitles : OCP.Interface.Interface_HArray1OfHAsciiString) -> None: 
        """
        None
        """
    def SetSuffixTitles(self,aSuffixTitles : OCP.Interface.Interface_HArray1OfHAsciiString) -> None: 
        """
        None
        """
    def SuffixTitles(self) -> OCP.Interface.Interface_HArray1OfHAsciiString: 
        """
        None
        """
    def SuffixTitlesValue(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetFirstName(self) -> None: 
        """
        None
        """
    def UnSetLastName(self) -> None: 
        """
        None
        """
    def UnSetMiddleNames(self) -> None: 
        """
        None
        """
    def UnSetPrefixTitles(self) -> None: 
        """
        None
        """
    def UnSetSuffixTitles(self) -> None: 
        """
        None
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
class StepBasic_PersonAndOrganization(OCP.Standard.Standard_Transient):
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
    def Init(self,aThePerson : StepBasic_Person,aTheOrganization : StepBasic_Organization) -> None: 
        """
        None
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
    def SetTheOrganization(self,aTheOrganization : StepBasic_Organization) -> None: 
        """
        None
        """
    def SetThePerson(self,aThePerson : StepBasic_Person) -> None: 
        """
        None
        """
    def TheOrganization(self) -> StepBasic_Organization: 
        """
        None
        """
    def ThePerson(self) -> StepBasic_Person: 
        """
        None
        """
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
class StepBasic_PersonAndOrganizationAssignment(OCP.Standard.Standard_Transient):
    def AssignedPersonAndOrganization(self) -> StepBasic_PersonAndOrganization: 
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
    def Init(self,aAssignedPersonAndOrganization : StepBasic_PersonAndOrganization,aRole : StepBasic_PersonAndOrganizationRole) -> None: 
        """
        None
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
    def Role(self) -> StepBasic_PersonAndOrganizationRole: 
        """
        None
        """
    def SetAssignedPersonAndOrganization(self,aAssignedPersonAndOrganization : StepBasic_PersonAndOrganization) -> None: 
        """
        None
        """
    def SetRole(self,aRole : StepBasic_PersonAndOrganizationRole) -> None: 
        """
        None
        """
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
class StepBasic_PersonAndOrganizationRole(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_PersonOrganizationSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a PersonOrganizationSelect Kind Entity that is : 1 -> Person 2 -> Organization 3 -> PersonAndOrganization 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Organization(self) -> StepBasic_Organization: 
        """
        returns Value as a Organization (Null if another type)
        """
    def Person(self) -> StepBasic_Person: 
        """
        returns Value as a Person (Null if another type)
        """
    def PersonAndOrganization(self) -> StepBasic_PersonAndOrganization: 
        """
        returns Value as a PersonAndOrganization (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepBasic_PersonalAddress(StepBasic_Address, OCP.Standard.Standard_Transient):
    def Country(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ElectronicMailAddress(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def FacsimileNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasCountry(self) -> bool: 
        """
        None
        """
    def HasElectronicMailAddress(self) -> bool: 
        """
        None
        """
    def HasFacsimileNumber(self) -> bool: 
        """
        None
        """
    def HasInternalLocation(self) -> bool: 
        """
        None
        """
    def HasPostalBox(self) -> bool: 
        """
        None
        """
    def HasPostalCode(self) -> bool: 
        """
        None
        """
    def HasRegion(self) -> bool: 
        """
        None
        """
    def HasStreet(self) -> bool: 
        """
        None
        """
    def HasStreetNumber(self) -> bool: 
        """
        None
        """
    def HasTelephoneNumber(self) -> bool: 
        """
        None
        """
    def HasTelexNumber(self) -> bool: 
        """
        None
        """
    def HasTown(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAinternalLocation : bool,aInternalLocation : OCP.TCollection.TCollection_HAsciiString,hasAstreetNumber : bool,aStreetNumber : OCP.TCollection.TCollection_HAsciiString,hasAstreet : bool,aStreet : OCP.TCollection.TCollection_HAsciiString,hasApostalBox : bool,aPostalBox : OCP.TCollection.TCollection_HAsciiString,hasAtown : bool,aTown : OCP.TCollection.TCollection_HAsciiString,hasAregion : bool,aRegion : OCP.TCollection.TCollection_HAsciiString,hasApostalCode : bool,aPostalCode : OCP.TCollection.TCollection_HAsciiString,hasAcountry : bool,aCountry : OCP.TCollection.TCollection_HAsciiString,hasAfacsimileNumber : bool,aFacsimileNumber : OCP.TCollection.TCollection_HAsciiString,hasAtelephoneNumber : bool,aTelephoneNumber : OCP.TCollection.TCollection_HAsciiString,hasAelectronicMailAddress : bool,aElectronicMailAddress : OCP.TCollection.TCollection_HAsciiString,hasAtelexNumber : bool,aTelexNumber : OCP.TCollection.TCollection_HAsciiString,aPeople : StepBasic_HArray1OfPerson,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def InternalLocation(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def NbPeople(self) -> int: 
        """
        None
        """
    def People(self) -> StepBasic_HArray1OfPerson: 
        """
        None
        """
    def PeopleValue(self,num : int) -> StepBasic_Person: 
        """
        None
        """
    def PostalBox(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PostalCode(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Region(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetCountry(self,aCountry : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetElectronicMailAddress(self,aElectronicMailAddress : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFacsimileNumber(self,aFacsimileNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetInternalLocation(self,aInternalLocation : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPeople(self,aPeople : StepBasic_HArray1OfPerson) -> None: 
        """
        None
        """
    def SetPostalBox(self,aPostalBox : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPostalCode(self,aPostalCode : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRegion(self,aRegion : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStreet(self,aStreet : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStreetNumber(self,aStreetNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTelephoneNumber(self,aTelephoneNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTelexNumber(self,aTelexNumber : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTown(self,aTown : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def Street(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def StreetNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def TelephoneNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def TelexNumber(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Town(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def UnSetCountry(self) -> None: 
        """
        None
        """
    def UnSetElectronicMailAddress(self) -> None: 
        """
        None
        """
    def UnSetFacsimileNumber(self) -> None: 
        """
        None
        """
    def UnSetInternalLocation(self) -> None: 
        """
        None
        """
    def UnSetPostalBox(self) -> None: 
        """
        None
        """
    def UnSetPostalCode(self) -> None: 
        """
        None
        """
    def UnSetRegion(self) -> None: 
        """
        None
        """
    def UnSetStreet(self) -> None: 
        """
        None
        """
    def UnSetStreetNumber(self) -> None: 
        """
        None
        """
    def UnSetTelephoneNumber(self) -> None: 
        """
        None
        """
    def UnSetTelexNumber(self) -> None: 
        """
        None
        """
    def UnSetTown(self) -> None: 
        """
        None
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
class StepBasic_ProductDefinition(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Formation(self) -> StepBasic_ProductDefinitionFormation: 
        """
        None
        """
    def FrameOfReference(self) -> StepBasic_ProductDefinitionContext: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aFormation : StepBasic_ProductDefinitionFormation,aFrameOfReference : StepBasic_ProductDefinitionContext) -> None: 
        """
        None
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
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFormation(self,aFormation : StepBasic_ProductDefinitionFormation) -> None: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ProductDefinitionContext) -> None: 
        """
        None
        """
    def SetId(self,aId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_PlaneAngleMeasureWithUnit(StepBasic_MeasureWithUnit, OCP.Standard.Standard_Transient):
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
    def Init(self,aValueComponent : StepBasic_MeasureValueMember,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
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
    def SetUnitComponent(self,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
        """
    def SetValueComponent(self,aValueComponent : float) -> None: 
        """
        None
        """
    def SetValueComponentMember(self,val : StepBasic_MeasureValueMember) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnitComponent(self) -> StepBasic_Unit: 
        """
        None
        """
    def ValueComponent(self) -> float: 
        """
        None
        """
    def ValueComponentMember(self) -> StepBasic_MeasureValueMember: 
        """
        None
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
class StepBasic_PlaneAngleUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_Product(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FrameOfReference(self) -> StepBasic_HArray1OfProductContext: 
        """
        None
        """
    def FrameOfReferenceValue(self,num : int) -> StepBasic_ProductContext: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aFrameOfReference : StepBasic_HArray1OfProductContext) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbFrameOfReference(self) -> int: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_HArray1OfProductContext) -> None: 
        """
        None
        """
    def SetId(self,aId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ProductCategory(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasAdescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetDescription(self) -> None: 
        """
        None
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
class StepBasic_ProductCategoryRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ProductCategoryRelationshipRepresentation of STEP entity ProductCategoryRelationshipRepresentation of STEP entity ProductCategoryRelationship
    """
    def Category(self) -> StepBasic_ProductCategory: 
        """
        Returns field Category
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aCategory : StepBasic_ProductCategory,aSubCategory : StepBasic_ProductCategory) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetCategory(self,Category : StepBasic_ProductCategory) -> None: 
        """
        Set field Category
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetSubCategory(self,SubCategory : StepBasic_ProductCategory) -> None: 
        """
        Set field SubCategory
        """
    def SubCategory(self) -> StepBasic_ProductCategory: 
        """
        Returns field SubCategory
        """
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
class StepBasic_ProductConceptContext(StepBasic_ApplicationContextElement, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ProductConceptContextRepresentation of STEP entity ProductConceptContextRepresentation of STEP entity ProductConceptContext
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
    def FrameOfReference(self) -> StepBasic_ApplicationContext: 
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
    def Init(self,aApplicationContextElement_Name : OCP.TCollection.TCollection_HAsciiString,aApplicationContextElement_FrameOfReference : StepBasic_ApplicationContext,aMarketSegmentType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def MarketSegmentType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field MarketSegmentType
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ApplicationContext) -> None: 
        """
        None
        """
    def SetMarketSegmentType(self,MarketSegmentType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field MarketSegmentType
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_MechanicalContext(StepBasic_ProductContext, StepBasic_ApplicationContextElement, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisciplineType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FrameOfReference(self) -> StepBasic_ApplicationContext: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aFrameOfReference : StepBasic_ApplicationContext,aDisciplineType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDisciplineType(self,aDisciplineType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ApplicationContext) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_PhysicallyModeledProductDefinition(StepBasic_ProductDefinition, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Formation(self) -> StepBasic_ProductDefinitionFormation: 
        """
        None
        """
    def FrameOfReference(self) -> StepBasic_ProductDefinitionContext: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aFormation : StepBasic_ProductDefinitionFormation,aFrameOfReference : StepBasic_ProductDefinitionContext) -> None: 
        """
        None
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
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFormation(self,aFormation : StepBasic_ProductDefinitionFormation) -> None: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ProductDefinitionContext) -> None: 
        """
        None
        """
    def SetId(self,aId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_DesignContext(StepBasic_ProductDefinitionContext, StepBasic_ApplicationContextElement, OCP.Standard.Standard_Transient):
    """
    class added to Schema AP214 around April 1996class added to Schema AP214 around April 1996class added to Schema AP214 around April 1996
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
    def FrameOfReference(self) -> StepBasic_ApplicationContext: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aFrameOfReference : StepBasic_ApplicationContext,aLifeCycleStage : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def LifeCycleStage(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ApplicationContext) -> None: 
        """
        None
        """
    def SetLifeCycleStage(self,aLifeCycleStage : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ProductDefinitionEffectivity(StepBasic_Effectivity, OCP.Standard.Standard_Transient):
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
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aUsage : StepBasic_ProductDefinitionRelationship) -> None: 
        """
        None
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
    def SetId(self,aid : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetUsage(self,aUsage : StepBasic_ProductDefinitionRelationship) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Usage(self) -> StepBasic_ProductDefinitionRelationship: 
        """
        None
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
class StepBasic_ProductDefinitionFormation(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfProduct : StepBasic_Product) -> None: 
        """
        None
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
    def OfProduct(self) -> StepBasic_Product: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetId(self,aId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfProduct(self,aOfProduct : StepBasic_Product) -> None: 
        """
        None
        """
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
class StepBasic_ProductDefinitionFormationRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ProductDefinitionFormationRelationshipRepresentation of STEP entity ProductDefinitionFormationRelationshipRepresentation of STEP entity ProductDefinitionFormationRelationship
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingProductDefinitionFormation : StepBasic_ProductDefinitionFormation,aRelatedProductDefinitionFormation : StepBasic_ProductDefinitionFormation) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: 
        """
        Returns field RelatedProductDefinitionFormation
        """
    def RelatingProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: 
        """
        Returns field RelatingProductDefinitionFormation
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedProductDefinitionFormation(self,RelatedProductDefinitionFormation : StepBasic_ProductDefinitionFormation) -> None: 
        """
        Set field RelatedProductDefinitionFormation
        """
    def SetRelatingProductDefinitionFormation(self,RelatingProductDefinitionFormation : StepBasic_ProductDefinitionFormation) -> None: 
        """
        Set field RelatingProductDefinitionFormation
        """
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
class StepBasic_ProductDefinitionFormationWithSpecifiedSource(StepBasic_ProductDefinitionFormation, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfProduct : StepBasic_Product,aMakeOrBuy : StepBasic_Source) -> None: 
        """
        None
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
    def MakeOrBuy(self) -> StepBasic_Source: 
        """
        None
        """
    def OfProduct(self) -> StepBasic_Product: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetId(self,aId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetMakeOrBuy(self,aMakeOrBuy : StepBasic_Source) -> None: 
        """
        None
        """
    def SetOfProduct(self,aOfProduct : StepBasic_Product) -> None: 
        """
        None
        """
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
class StepBasic_ProductDefinitionOrReference(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a ProductDefinitionOrReference Kind Entity that is : 1 -> ProductDefinition 2 -> ProductDefinitionReference 3 -> ProductDefinitionReferenceWithLocalPresentation 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def ProductDefinition(self) -> StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionReference(self) -> StepBasic_ProductDefinitionReference: 
        """
        returns Value as a ProductDefinitionReference (Null if another type)
        """
    def ProductDefinitionReferenceWithLocalRepresentation(self) -> StepBasic_ProductDefinitionReferenceWithLocalRepresentation: 
        """
        returns Value as a ProductDefinitionReferenceWithLocalRepresentation (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepBasic_ProductDefinitionReference(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity Product_Definition_ReferenceRepresentation of STEP entity Product_Definition_ReferenceRepresentation of STEP entity Product_Definition_Reference
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
    def HasIdOwningOrganizationName(self) -> bool: 
        """
        Returns true if IdOwningOrganizationName exists
        """
    def IdOwningOrganizationName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field IdOwningOrganizationName
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theSource : StepBasic_ExternalSource,theProductId : OCP.TCollection.TCollection_HAsciiString,theProductDefinitionFormationId : OCP.TCollection.TCollection_HAsciiString,theProductDefinitionId : OCP.TCollection.TCollection_HAsciiString,theIdOwningOrganizationName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,theSource : StepBasic_ExternalSource,theProductId : OCP.TCollection.TCollection_HAsciiString,theProductDefinitionFormationId : OCP.TCollection.TCollection_HAsciiString,theProductDefinitionId : OCP.TCollection.TCollection_HAsciiString) -> None: ...
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
    def ProductDefinitionFormationId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field ProductDefinitionFormationId
        """
    def ProductDefinitionId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field ProductDefinitionId
        """
    def ProductId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field ProductId
        """
    def SetIdOwningOrganizationName(self,theIdOwningOrganizationName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field IdOwningOrganizationName
        """
    def SetProductDefinitionFormationId(self,theProductDefinitionFormationId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field ProductDefinitionFormationId
        """
    def SetProductDefinitionId(self,theProductDefinitionId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field ProductDefinitionId
        """
    def SetProductId(self,theProductId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field ProductId
        """
    def SetSource(self,theSource : StepBasic_ExternalSource) -> None: 
        """
        Set field Source
        """
    def Source(self) -> StepBasic_ExternalSource: 
        """
        Returns field Source
        """
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
class StepBasic_ProductDefinitionReferenceWithLocalRepresentation(StepBasic_ProductDefinition, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Formation(self) -> StepBasic_ProductDefinitionFormation: 
        """
        None
        """
    def FrameOfReference(self) -> StepBasic_ProductDefinitionContext: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theSource : StepBasic_ExternalSource,theId : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theFormation : StepBasic_ProductDefinitionFormation,theFrameOfReference : StepBasic_ProductDefinitionContext) -> None: 
        """
        None
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
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFormation(self,aFormation : StepBasic_ProductDefinitionFormation) -> None: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ProductDefinitionContext) -> None: 
        """
        None
        """
    def SetId(self,aId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSource(self,theSource : StepBasic_ExternalSource) -> None: 
        """
        Set field Source
        """
    def Source(self) -> StepBasic_ExternalSource: 
        """
        Returns field Source
        """
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
class StepBasic_ProductDefinitionRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ProductDefinitionRelationshipRepresentation of STEP entity ProductDefinitionRelationshipRepresentation of STEP entity ProductDefinitionRelationship
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingProductDefinition : StepBasic_ProductDefinition,aRelatedProductDefinition : StepBasic_ProductDefinition) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingProductDefinition : StepBasic_ProductDefinitionOrReference,aRelatedProductDefinition : StepBasic_ProductDefinitionOrReference) -> None: ...
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedProductDefinition(self) -> StepBasic_ProductDefinition: 
        """
        Returns field RelatedProductDefinition
        """
    def RelatedProductDefinitionAP242(self) -> StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatedProductDefinition in AP242
        """
    def RelatingProductDefinition(self) -> StepBasic_ProductDefinition: 
        """
        Returns field RelatingProductDefinition
        """
    def RelatingProductDefinitionAP242(self) -> StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatingProductDefinition in AP242
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : StepBasic_ProductDefinition) -> None: 
        """
        Set field RelatedProductDefinition

        Set field RelatedProductDefinition in AP242
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : StepBasic_ProductDefinitionOrReference) -> None: ...
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatingProductDefinition

        Set field RelatingProductDefinition in AP242
        """
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : StepBasic_ProductDefinition) -> None: ...
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
class StepBasic_ProductDefinitionWithAssociatedDocuments(StepBasic_ProductDefinition, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DocIds(self) -> StepBasic_HArray1OfDocument: 
        """
        None
        """
    def DocIdsValue(self,num : int) -> StepBasic_Document: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Formation(self) -> StepBasic_ProductDefinitionFormation: 
        """
        None
        """
    def FrameOfReference(self) -> StepBasic_ProductDefinitionContext: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aFormation : StepBasic_ProductDefinitionFormation,aFrame : StepBasic_ProductDefinitionContext,aDocIds : StepBasic_HArray1OfDocument) -> None: 
        """
        None
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
    def NbDocIds(self) -> int: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetDocIds(self,DocIds : StepBasic_HArray1OfDocument) -> None: 
        """
        None
        """
    def SetDocIdsValue(self,num : int,adoc : StepBasic_Document) -> None: 
        """
        None
        """
    def SetFormation(self,aFormation : StepBasic_ProductDefinitionFormation) -> None: 
        """
        None
        """
    def SetFrameOfReference(self,aFrameOfReference : StepBasic_ProductDefinitionContext) -> None: 
        """
        None
        """
    def SetId(self,aId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_ProductOrFormationOrDefinition(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type ProductOrFormationOrDefinition
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of ProductOrFormationOrDefinition select type 1 -> Product from StepBasic 2 -> ProductDefinitionFormation from StepBasic 3 -> ProductDefinition from StepBasic 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Product(self) -> StepBasic_Product: 
        """
        Returns Value as Product (or Null if another type)
        """
    def ProductDefinition(self) -> StepBasic_ProductDefinition: 
        """
        Returns Value as ProductDefinition (or Null if another type)
        """
    def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: 
        """
        Returns Value as ProductDefinitionFormation (or Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepBasic_ProductRelatedProductCategory(StepBasic_ProductCategory, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasAdescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aProducts : StepBasic_HArray1OfProduct) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbProducts(self) -> int: 
        """
        None
        """
    def Products(self) -> StepBasic_HArray1OfProduct: 
        """
        None
        """
    def ProductsValue(self,num : int) -> StepBasic_Product: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetProducts(self,aProducts : StepBasic_HArray1OfProduct) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetDescription(self) -> None: 
        """
        None
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
class StepBasic_ProductType(StepBasic_ProductRelatedProductCategory, StepBasic_ProductCategory, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasAdescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aProducts : StepBasic_HArray1OfProduct) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbProducts(self) -> int: 
        """
        None
        """
    def Products(self) -> StepBasic_HArray1OfProduct: 
        """
        None
        """
    def ProductsValue(self,num : int) -> StepBasic_Product: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetProducts(self,aProducts : StepBasic_HArray1OfProduct) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetDescription(self) -> None: 
        """
        None
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
class StepBasic_RatioMeasureWithUnit(StepBasic_MeasureWithUnit, OCP.Standard.Standard_Transient):
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
    def Init(self,aValueComponent : StepBasic_MeasureValueMember,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
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
    def SetUnitComponent(self,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
        """
    def SetValueComponent(self,aValueComponent : float) -> None: 
        """
        None
        """
    def SetValueComponentMember(self,val : StepBasic_MeasureValueMember) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnitComponent(self) -> StepBasic_Unit: 
        """
        None
        """
    def ValueComponent(self) -> float: 
        """
        None
        """
    def ValueComponentMember(self) -> StepBasic_MeasureValueMember: 
        """
        None
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
class StepBasic_RatioUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_RoleAssociation(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity RoleAssociationRepresentation of STEP entity RoleAssociationRepresentation of STEP entity RoleAssociation
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
    def Init(self,aRole : StepBasic_ObjectRole,aItemWithRole : StepBasic_RoleSelect) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def ItemWithRole(self) -> StepBasic_RoleSelect: 
        """
        Returns field ItemWithRole
        """
    def Role(self) -> StepBasic_ObjectRole: 
        """
        Returns field Role
        """
    def SetItemWithRole(self,ItemWithRole : StepBasic_RoleSelect) -> None: 
        """
        Set field ItemWithRole
        """
    def SetRole(self,Role : StepBasic_ObjectRole) -> None: 
        """
        Set field Role
        """
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
class StepBasic_RoleSelect(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type RoleSelect
    """
    def ActionAssignment(self) -> StepBasic_ActionAssignment: 
        """
        Returns Value as ActionAssignment (or Null if another type)
        """
    def ActionRequestAssignment(self) -> StepBasic_ActionRequestAssignment: 
        """
        Returns Value as ActionRequestAssignment (or Null if another type)
        """
    def ApprovalAssignment(self) -> StepBasic_ApprovalAssignment: 
        """
        Returns Value as ApprovalAssignment (or Null if another type)
        """
    def ApprovalDateTime(self) -> StepBasic_ApprovalDateTime: 
        """
        Returns Value as ApprovalDateTime (or Null if another type)
        """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of RoleSelect select type 1 -> ActionAssignment from StepBasic 2 -> ActionRequestAssignment from StepBasic 3 -> ApprovalAssignment from StepBasic 4 -> ApprovalDateTime from StepBasic 5 -> CertificationAssignment from StepBasic 6 -> ContractAssignment from StepBasic 7 -> DocumentReference from StepBasic 8 -> EffectivityAssignment from StepBasic 9 -> GroupAssignment from StepBasic 10 -> NameAssignment from StepBasic 11 -> SecurityClassificationAssignment from StepBasic 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CertificationAssignment(self) -> StepBasic_CertificationAssignment: 
        """
        Returns Value as CertificationAssignment (or Null if another type)
        """
    def ContractAssignment(self) -> StepBasic_ContractAssignment: 
        """
        Returns Value as ContractAssignment (or Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DocumentReference(self) -> StepBasic_DocumentReference: 
        """
        Returns Value as DocumentReference (or Null if another type)
        """
    def EffectivityAssignment(self) -> StepBasic_EffectivityAssignment: 
        """
        Returns Value as EffectivityAssignment (or Null if another type)
        """
    def GroupAssignment(self) -> StepBasic_GroupAssignment: 
        """
        Returns Value as GroupAssignment (or Null if another type)
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NameAssignment(self) -> StepBasic_NameAssignment: 
        """
        Returns Value as NameAssignment (or Null if another type)
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def SecurityClassificationAssignment(self) -> StepBasic_SecurityClassificationAssignment: 
        """
        Returns Value as SecurityClassificationAssignment (or Null if another type)
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepBasic_SecurityClassification(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPurpose : OCP.TCollection.TCollection_HAsciiString,aSecurityLevel : StepBasic_SecurityClassificationLevel) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Purpose(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SecurityLevel(self) -> StepBasic_SecurityClassificationLevel: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPurpose(self,aPurpose : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSecurityLevel(self,aSecurityLevel : StepBasic_SecurityClassificationLevel) -> None: 
        """
        None
        """
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
class StepBasic_SecurityClassificationAssignment(OCP.Standard.Standard_Transient):
    def AssignedSecurityClassification(self) -> StepBasic_SecurityClassification: 
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
    def Init(self,aAssignedSecurityClassification : StepBasic_SecurityClassification) -> None: 
        """
        None
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
    def SetAssignedSecurityClassification(self,aAssignedSecurityClassification : StepBasic_SecurityClassification) -> None: 
        """
        None
        """
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
class StepBasic_SecurityClassificationLevel(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
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
class StepBasic_SiPrefix():
    """
    None

    Members:

      StepBasic_spExa

      StepBasic_spPeta

      StepBasic_spTera

      StepBasic_spGiga

      StepBasic_spMega

      StepBasic_spKilo

      StepBasic_spHecto

      StepBasic_spDeca

      StepBasic_spDeci

      StepBasic_spCenti

      StepBasic_spMilli

      StepBasic_spMicro

      StepBasic_spNano

      StepBasic_spPico

      StepBasic_spFemto

      StepBasic_spAtto
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StepBasic_spAtto: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spAtto
    StepBasic_spCenti: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spCenti
    StepBasic_spDeca: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spDeca
    StepBasic_spDeci: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spDeci
    StepBasic_spExa: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spExa
    StepBasic_spFemto: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spFemto
    StepBasic_spGiga: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spGiga
    StepBasic_spHecto: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spHecto
    StepBasic_spKilo: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spKilo
    StepBasic_spMega: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spMega
    StepBasic_spMicro: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spMicro
    StepBasic_spMilli: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spMilli
    StepBasic_spNano: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spNano
    StepBasic_spPeta: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spPeta
    StepBasic_spPico: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spPico
    StepBasic_spTera: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spTera
    __entries: dict # value = {'StepBasic_spExa': (StepBasic_SiPrefix.StepBasic_spExa, None), 'StepBasic_spPeta': (StepBasic_SiPrefix.StepBasic_spPeta, None), 'StepBasic_spTera': (StepBasic_SiPrefix.StepBasic_spTera, None), 'StepBasic_spGiga': (StepBasic_SiPrefix.StepBasic_spGiga, None), 'StepBasic_spMega': (StepBasic_SiPrefix.StepBasic_spMega, None), 'StepBasic_spKilo': (StepBasic_SiPrefix.StepBasic_spKilo, None), 'StepBasic_spHecto': (StepBasic_SiPrefix.StepBasic_spHecto, None), 'StepBasic_spDeca': (StepBasic_SiPrefix.StepBasic_spDeca, None), 'StepBasic_spDeci': (StepBasic_SiPrefix.StepBasic_spDeci, None), 'StepBasic_spCenti': (StepBasic_SiPrefix.StepBasic_spCenti, None), 'StepBasic_spMilli': (StepBasic_SiPrefix.StepBasic_spMilli, None), 'StepBasic_spMicro': (StepBasic_SiPrefix.StepBasic_spMicro, None), 'StepBasic_spNano': (StepBasic_SiPrefix.StepBasic_spNano, None), 'StepBasic_spPico': (StepBasic_SiPrefix.StepBasic_spPico, None), 'StepBasic_spFemto': (StepBasic_SiPrefix.StepBasic_spFemto, None), 'StepBasic_spAtto': (StepBasic_SiPrefix.StepBasic_spAtto, None)}
    __members__: dict # value = {'StepBasic_spExa': StepBasic_SiPrefix.StepBasic_spExa, 'StepBasic_spPeta': StepBasic_SiPrefix.StepBasic_spPeta, 'StepBasic_spTera': StepBasic_SiPrefix.StepBasic_spTera, 'StepBasic_spGiga': StepBasic_SiPrefix.StepBasic_spGiga, 'StepBasic_spMega': StepBasic_SiPrefix.StepBasic_spMega, 'StepBasic_spKilo': StepBasic_SiPrefix.StepBasic_spKilo, 'StepBasic_spHecto': StepBasic_SiPrefix.StepBasic_spHecto, 'StepBasic_spDeca': StepBasic_SiPrefix.StepBasic_spDeca, 'StepBasic_spDeci': StepBasic_SiPrefix.StepBasic_spDeci, 'StepBasic_spCenti': StepBasic_SiPrefix.StepBasic_spCenti, 'StepBasic_spMilli': StepBasic_SiPrefix.StepBasic_spMilli, 'StepBasic_spMicro': StepBasic_SiPrefix.StepBasic_spMicro, 'StepBasic_spNano': StepBasic_SiPrefix.StepBasic_spNano, 'StepBasic_spPico': StepBasic_SiPrefix.StepBasic_spPico, 'StepBasic_spFemto': StepBasic_SiPrefix.StepBasic_spFemto, 'StepBasic_spAtto': StepBasic_SiPrefix.StepBasic_spAtto}
    pass
class StepBasic_SiUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetPrefix(self) -> None: 
        """
        None
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
class StepBasic_SiUnitAndAreaUnit(StepBasic_SiUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def AreaUnit(self) -> StepBasic_AreaUnit: 
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
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def SetAreaUnit(self,anAreaUnit : StepBasic_AreaUnit) -> None: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetPrefix(self) -> None: 
        """
        None
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
class StepBasic_SiUnitAndLengthUnit(StepBasic_SiUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def LengthUnit(self) -> StepBasic_LengthUnit: 
        """
        None
        """
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetLengthUnit(self,aLengthUnit : StepBasic_LengthUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetPrefix(self) -> None: 
        """
        None
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
class StepBasic_SiUnitAndMassUnit(StepBasic_SiUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def MassUnit(self) -> StepBasic_MassUnit: 
        """
        None
        """
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetMassUnit(self,aMassUnit : StepBasic_MassUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetPrefix(self) -> None: 
        """
        None
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
class StepBasic_SiUnitAndPlaneAngleUnit(StepBasic_SiUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def PlaneAngleUnit(self) -> StepBasic_PlaneAngleUnit: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPlaneAngleUnit(self,aPlaneAngleUnit : StepBasic_PlaneAngleUnit) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetPrefix(self) -> None: 
        """
        None
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
class StepBasic_SiUnitAndRatioUnit(StepBasic_SiUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def RatioUnit(self) -> StepBasic_RatioUnit: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def SetRatioUnit(self,aRatioUnit : StepBasic_RatioUnit) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetPrefix(self) -> None: 
        """
        None
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
class StepBasic_SiUnitAndSolidAngleUnit(StepBasic_SiUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def SetSolidAngleUnit(self,aSolidAngleUnit : StepBasic_SolidAngleUnit) -> None: 
        """
        None
        """
    def SolidAngleUnit(self) -> StepBasic_SolidAngleUnit: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetPrefix(self) -> None: 
        """
        None
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
class StepBasic_SiUnitAndThermodynamicTemperatureUnit(StepBasic_SiUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def SetThermodynamicTemperatureUnit(self,aThermodynamicTemperatureUnit : StepBasic_ThermodynamicTemperatureUnit) -> None: 
        """
        None
        """
    def ThermodynamicTemperatureUnit(self) -> StepBasic_ThermodynamicTemperatureUnit: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetPrefix(self) -> None: 
        """
        None
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
class StepBasic_SiUnitAndTimeUnit(StepBasic_SiUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def SetTimeUnit(self,aTimeUnit : StepBasic_TimeUnit) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TimeUnit(self) -> StepBasic_TimeUnit: 
        """
        None
        """
    def UnSetPrefix(self) -> None: 
        """
        None
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
class StepBasic_SiUnitAndVolumeUnit(StepBasic_SiUnit, StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPrefix(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,hasAprefix : bool,aPrefix : StepBasic_SiPrefix,aName : StepBasic_SiUnitName) -> None: 
        """
        None
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
    def Name(self) -> StepBasic_SiUnitName: 
        """
        None
        """
    def Prefix(self) -> StepBasic_SiPrefix: 
        """
        None
        """
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
    def SetName(self,aName : StepBasic_SiUnitName) -> None: 
        """
        None
        """
    def SetPrefix(self,aPrefix : StepBasic_SiPrefix) -> None: 
        """
        None
        """
    def SetVolumeUnit(self,aVolumeUnit : StepBasic_VolumeUnit) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetPrefix(self) -> None: 
        """
        None
        """
    def VolumeUnit(self) -> StepBasic_VolumeUnit: 
        """
        None
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
class StepBasic_SiUnitName():
    """
    None

    Members:

      StepBasic_sunMetre

      StepBasic_sunGram

      StepBasic_sunSecond

      StepBasic_sunAmpere

      StepBasic_sunKelvin

      StepBasic_sunMole

      StepBasic_sunCandela

      StepBasic_sunRadian

      StepBasic_sunSteradian

      StepBasic_sunHertz

      StepBasic_sunNewton

      StepBasic_sunPascal

      StepBasic_sunJoule

      StepBasic_sunWatt

      StepBasic_sunCoulomb

      StepBasic_sunVolt

      StepBasic_sunFarad

      StepBasic_sunOhm

      StepBasic_sunSiemens

      StepBasic_sunWeber

      StepBasic_sunTesla

      StepBasic_sunHenry

      StepBasic_sunDegreeCelsius

      StepBasic_sunLumen

      StepBasic_sunLux

      StepBasic_sunBecquerel

      StepBasic_sunGray

      StepBasic_sunSievert
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StepBasic_sunAmpere: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunAmpere
    StepBasic_sunBecquerel: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunBecquerel
    StepBasic_sunCandela: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunCandela
    StepBasic_sunCoulomb: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunCoulomb
    StepBasic_sunDegreeCelsius: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunDegreeCelsius
    StepBasic_sunFarad: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunFarad
    StepBasic_sunGram: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunGram
    StepBasic_sunGray: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunGray
    StepBasic_sunHenry: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunHenry
    StepBasic_sunHertz: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunHertz
    StepBasic_sunJoule: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunJoule
    StepBasic_sunKelvin: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunKelvin
    StepBasic_sunLumen: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunLumen
    StepBasic_sunLux: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunLux
    StepBasic_sunMetre: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunMetre
    StepBasic_sunMole: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunMole
    StepBasic_sunNewton: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunNewton
    StepBasic_sunOhm: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunOhm
    StepBasic_sunPascal: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunPascal
    StepBasic_sunRadian: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunRadian
    StepBasic_sunSecond: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunSecond
    StepBasic_sunSiemens: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunSiemens
    StepBasic_sunSievert: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunSievert
    StepBasic_sunSteradian: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunSteradian
    StepBasic_sunTesla: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunTesla
    StepBasic_sunVolt: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunVolt
    StepBasic_sunWatt: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunWatt
    StepBasic_sunWeber: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunWeber
    __entries: dict # value = {'StepBasic_sunMetre': (StepBasic_SiUnitName.StepBasic_sunMetre, None), 'StepBasic_sunGram': (StepBasic_SiUnitName.StepBasic_sunGram, None), 'StepBasic_sunSecond': (StepBasic_SiUnitName.StepBasic_sunSecond, None), 'StepBasic_sunAmpere': (StepBasic_SiUnitName.StepBasic_sunAmpere, None), 'StepBasic_sunKelvin': (StepBasic_SiUnitName.StepBasic_sunKelvin, None), 'StepBasic_sunMole': (StepBasic_SiUnitName.StepBasic_sunMole, None), 'StepBasic_sunCandela': (StepBasic_SiUnitName.StepBasic_sunCandela, None), 'StepBasic_sunRadian': (StepBasic_SiUnitName.StepBasic_sunRadian, None), 'StepBasic_sunSteradian': (StepBasic_SiUnitName.StepBasic_sunSteradian, None), 'StepBasic_sunHertz': (StepBasic_SiUnitName.StepBasic_sunHertz, None), 'StepBasic_sunNewton': (StepBasic_SiUnitName.StepBasic_sunNewton, None), 'StepBasic_sunPascal': (StepBasic_SiUnitName.StepBasic_sunPascal, None), 'StepBasic_sunJoule': (StepBasic_SiUnitName.StepBasic_sunJoule, None), 'StepBasic_sunWatt': (StepBasic_SiUnitName.StepBasic_sunWatt, None), 'StepBasic_sunCoulomb': (StepBasic_SiUnitName.StepBasic_sunCoulomb, None), 'StepBasic_sunVolt': (StepBasic_SiUnitName.StepBasic_sunVolt, None), 'StepBasic_sunFarad': (StepBasic_SiUnitName.StepBasic_sunFarad, None), 'StepBasic_sunOhm': (StepBasic_SiUnitName.StepBasic_sunOhm, None), 'StepBasic_sunSiemens': (StepBasic_SiUnitName.StepBasic_sunSiemens, None), 'StepBasic_sunWeber': (StepBasic_SiUnitName.StepBasic_sunWeber, None), 'StepBasic_sunTesla': (StepBasic_SiUnitName.StepBasic_sunTesla, None), 'StepBasic_sunHenry': (StepBasic_SiUnitName.StepBasic_sunHenry, None), 'StepBasic_sunDegreeCelsius': (StepBasic_SiUnitName.StepBasic_sunDegreeCelsius, None), 'StepBasic_sunLumen': (StepBasic_SiUnitName.StepBasic_sunLumen, None), 'StepBasic_sunLux': (StepBasic_SiUnitName.StepBasic_sunLux, None), 'StepBasic_sunBecquerel': (StepBasic_SiUnitName.StepBasic_sunBecquerel, None), 'StepBasic_sunGray': (StepBasic_SiUnitName.StepBasic_sunGray, None), 'StepBasic_sunSievert': (StepBasic_SiUnitName.StepBasic_sunSievert, None)}
    __members__: dict # value = {'StepBasic_sunMetre': StepBasic_SiUnitName.StepBasic_sunMetre, 'StepBasic_sunGram': StepBasic_SiUnitName.StepBasic_sunGram, 'StepBasic_sunSecond': StepBasic_SiUnitName.StepBasic_sunSecond, 'StepBasic_sunAmpere': StepBasic_SiUnitName.StepBasic_sunAmpere, 'StepBasic_sunKelvin': StepBasic_SiUnitName.StepBasic_sunKelvin, 'StepBasic_sunMole': StepBasic_SiUnitName.StepBasic_sunMole, 'StepBasic_sunCandela': StepBasic_SiUnitName.StepBasic_sunCandela, 'StepBasic_sunRadian': StepBasic_SiUnitName.StepBasic_sunRadian, 'StepBasic_sunSteradian': StepBasic_SiUnitName.StepBasic_sunSteradian, 'StepBasic_sunHertz': StepBasic_SiUnitName.StepBasic_sunHertz, 'StepBasic_sunNewton': StepBasic_SiUnitName.StepBasic_sunNewton, 'StepBasic_sunPascal': StepBasic_SiUnitName.StepBasic_sunPascal, 'StepBasic_sunJoule': StepBasic_SiUnitName.StepBasic_sunJoule, 'StepBasic_sunWatt': StepBasic_SiUnitName.StepBasic_sunWatt, 'StepBasic_sunCoulomb': StepBasic_SiUnitName.StepBasic_sunCoulomb, 'StepBasic_sunVolt': StepBasic_SiUnitName.StepBasic_sunVolt, 'StepBasic_sunFarad': StepBasic_SiUnitName.StepBasic_sunFarad, 'StepBasic_sunOhm': StepBasic_SiUnitName.StepBasic_sunOhm, 'StepBasic_sunSiemens': StepBasic_SiUnitName.StepBasic_sunSiemens, 'StepBasic_sunWeber': StepBasic_SiUnitName.StepBasic_sunWeber, 'StepBasic_sunTesla': StepBasic_SiUnitName.StepBasic_sunTesla, 'StepBasic_sunHenry': StepBasic_SiUnitName.StepBasic_sunHenry, 'StepBasic_sunDegreeCelsius': StepBasic_SiUnitName.StepBasic_sunDegreeCelsius, 'StepBasic_sunLumen': StepBasic_SiUnitName.StepBasic_sunLumen, 'StepBasic_sunLux': StepBasic_SiUnitName.StepBasic_sunLux, 'StepBasic_sunBecquerel': StepBasic_SiUnitName.StepBasic_sunBecquerel, 'StepBasic_sunGray': StepBasic_SiUnitName.StepBasic_sunGray, 'StepBasic_sunSievert': StepBasic_SiUnitName.StepBasic_sunSievert}
    pass
class StepBasic_SizeMember(OCP.StepData.StepData_SelectReal, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    For immediate members of SizeSelect, i.e. : ParameterValue (a Real)For immediate members of SizeSelect, i.e. : ParameterValue (a Real)For immediate members of SizeSelect, i.e. : ParameterValue (a Real)
    """
    def Boolean(self) -> bool: 
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
    def Enum(self) -> int: 
        """
        None
        """
    def EnumText(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
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
    def Kind(self) -> int: 
        """
        None
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        None
        """
    def ParamType(self) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the Kind of the SelectMember, under the form of an enum ParamType
        """
    def Real(self) -> float: 
        """
        None
        """
    def SetBoolean(self,val : bool) -> None: 
        """
        None
        """
    def SetEnum(self,val : int,text : str='') -> None: 
        """
        None
        """
    def SetEnumText(self,val : int,text : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it)
        """
    def SetInteger(self,val : int) -> None: 
        """
        None
        """
    def SetKind(self,kind : int) -> None: 
        """
        None
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        None
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def String(self) -> str: 
        """
        None
        """
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
class StepBasic_SizeSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a SelectMember as Real, named as PARAMETER_VALUE 1 -> PositiveLengthMeasure i.e. Real 0 else (i.e. Entity)
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a TrimmingSelect Kind Entity that is : 1 -> SizeMember 0 else (i.e. Real)
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a SizeMember (POSITIVE_LENGTH_MEASURE) as preferred
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def RealValue(self) -> float: 
        """
        returns Value as a Real (Null if another type)
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetRealValue(self,aReal : float) -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepBasic_SolidAngleMeasureWithUnit(StepBasic_MeasureWithUnit, OCP.Standard.Standard_Transient):
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
    def Init(self,aValueComponent : StepBasic_MeasureValueMember,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
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
    def SetUnitComponent(self,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
        """
    def SetValueComponent(self,aValueComponent : float) -> None: 
        """
        None
        """
    def SetValueComponentMember(self,val : StepBasic_MeasureValueMember) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnitComponent(self) -> StepBasic_Unit: 
        """
        None
        """
    def ValueComponent(self) -> float: 
        """
        None
        """
    def ValueComponentMember(self) -> StepBasic_MeasureValueMember: 
        """
        None
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
class StepBasic_SolidAngleUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_Source():
    """
    None

    Members:

      StepBasic_sMade

      StepBasic_sBought

      StepBasic_sNotKnown
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StepBasic_sBought: OCP.StepBasic.StepBasic_Source # value = StepBasic_Source.StepBasic_sBought
    StepBasic_sMade: OCP.StepBasic.StepBasic_Source # value = StepBasic_Source.StepBasic_sMade
    StepBasic_sNotKnown: OCP.StepBasic.StepBasic_Source # value = StepBasic_Source.StepBasic_sNotKnown
    __entries: dict # value = {'StepBasic_sMade': (StepBasic_Source.StepBasic_sMade, None), 'StepBasic_sBought': (StepBasic_Source.StepBasic_sBought, None), 'StepBasic_sNotKnown': (StepBasic_Source.StepBasic_sNotKnown, None)}
    __members__: dict # value = {'StepBasic_sMade': StepBasic_Source.StepBasic_sMade, 'StepBasic_sBought': StepBasic_Source.StepBasic_sBought, 'StepBasic_sNotKnown': StepBasic_Source.StepBasic_sNotKnown}
    pass
class StepBasic_SourceItem(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type SourceItem
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of SourceItem select type 1 -> HAsciiString from TCollection 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Identifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Value as Identifier (or Null if another type)
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        None
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepBasic_ThermodynamicTemperatureUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ThermodynamicTemperatureUnitRepresentation of STEP entity ThermodynamicTemperatureUnitRepresentation of STEP entity ThermodynamicTemperatureUnit
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_TimeMeasureWithUnit(StepBasic_MeasureWithUnit, OCP.Standard.Standard_Transient):
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
    def Init(self,aValueComponent : StepBasic_MeasureValueMember,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
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
    def SetUnitComponent(self,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
        """
    def SetValueComponent(self,aValueComponent : float) -> None: 
        """
        None
        """
    def SetValueComponentMember(self,val : StepBasic_MeasureValueMember) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnitComponent(self) -> StepBasic_Unit: 
        """
        None
        """
    def ValueComponent(self) -> float: 
        """
        None
        """
    def ValueComponentMember(self) -> StepBasic_MeasureValueMember: 
        """
        None
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
class StepBasic_TimeUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_UncertaintyMeasureWithUnit(StepBasic_MeasureWithUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aValueComponent : StepBasic_MeasureValueMember,aUnitComponent : StepBasic_Unit,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetUnitComponent(self,aUnitComponent : StepBasic_Unit) -> None: 
        """
        None
        """
    def SetValueComponent(self,aValueComponent : float) -> None: 
        """
        None
        """
    def SetValueComponentMember(self,val : StepBasic_MeasureValueMember) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnitComponent(self) -> StepBasic_Unit: 
        """
        None
        """
    def ValueComponent(self) -> float: 
        """
        None
        """
    def ValueComponentMember(self) -> StepBasic_MeasureValueMember: 
        """
        None
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
class StepBasic_Unit(OCP.StepData.StepData_SelectType):
    """
    Implements a select type unit (NamedUnit or DerivedUnit)
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a type of Unit Entity 1 -> NamedUnit 2 -> DerivedUnit
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def DerivedUnit(self) -> StepBasic_DerivedUnit: 
        """
        returns Value as a DerivedUnit (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NamedUnit(self) -> StepBasic_NamedUnit: 
        """
        returns Value as a NamedUnit (Null if another type)
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepBasic_VersionedActionRequest(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity VersionedActionRequestRepresentation of STEP entity VersionedActionRequestRepresentation of STEP entity VersionedActionRequest
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aVersion : OCP.TCollection.TCollection_HAsciiString,aPurpose : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Purpose(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Purpose
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetPurpose(self,Purpose : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Purpose
        """
    def SetVersion(self,Version : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Version
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Version(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Version
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
class StepBasic_VolumeUnit(StepBasic_NamedUnit, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> StepBasic_DimensionalExponents: 
        """
        None
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
    def Init(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
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
    def SetDimensions(self,aDimensions : StepBasic_DimensionalExponents) -> None: 
        """
        None
        """
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
class StepBasic_WeekOfYearAndDayDate(StepBasic_Date, OCP.Standard.Standard_Transient):
    def DayComponent(self) -> int: 
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
    def HasDayComponent(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aYearComponent : int,aWeekComponent : int,hasAdayComponent : bool,aDayComponent : int) -> None: 
        """
        None
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
    def SetDayComponent(self,aDayComponent : int) -> None: 
        """
        None
        """
    def SetWeekComponent(self,aWeekComponent : int) -> None: 
        """
        None
        """
    def SetYearComponent(self,aYearComponent : int) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetDayComponent(self) -> None: 
        """
        None
        """
    def WeekComponent(self) -> int: 
        """
        None
        """
    def YearComponent(self) -> int: 
        """
        None
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
StepBasic_aobAhead: OCP.StepBasic.StepBasic_AheadOrBehind # value = StepBasic_AheadOrBehind.StepBasic_aobAhead
StepBasic_aobBehind: OCP.StepBasic.StepBasic_AheadOrBehind # value = StepBasic_AheadOrBehind.StepBasic_aobBehind
StepBasic_aobExact: OCP.StepBasic.StepBasic_AheadOrBehind # value = StepBasic_AheadOrBehind.StepBasic_aobExact
StepBasic_sBought: OCP.StepBasic.StepBasic_Source # value = StepBasic_Source.StepBasic_sBought
StepBasic_sMade: OCP.StepBasic.StepBasic_Source # value = StepBasic_Source.StepBasic_sMade
StepBasic_sNotKnown: OCP.StepBasic.StepBasic_Source # value = StepBasic_Source.StepBasic_sNotKnown
StepBasic_spAtto: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spAtto
StepBasic_spCenti: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spCenti
StepBasic_spDeca: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spDeca
StepBasic_spDeci: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spDeci
StepBasic_spExa: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spExa
StepBasic_spFemto: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spFemto
StepBasic_spGiga: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spGiga
StepBasic_spHecto: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spHecto
StepBasic_spKilo: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spKilo
StepBasic_spMega: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spMega
StepBasic_spMicro: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spMicro
StepBasic_spMilli: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spMilli
StepBasic_spNano: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spNano
StepBasic_spPeta: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spPeta
StepBasic_spPico: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spPico
StepBasic_spTera: OCP.StepBasic.StepBasic_SiPrefix # value = StepBasic_SiPrefix.StepBasic_spTera
StepBasic_sunAmpere: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunAmpere
StepBasic_sunBecquerel: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunBecquerel
StepBasic_sunCandela: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunCandela
StepBasic_sunCoulomb: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunCoulomb
StepBasic_sunDegreeCelsius: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunDegreeCelsius
StepBasic_sunFarad: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunFarad
StepBasic_sunGram: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunGram
StepBasic_sunGray: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunGray
StepBasic_sunHenry: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunHenry
StepBasic_sunHertz: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunHertz
StepBasic_sunJoule: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunJoule
StepBasic_sunKelvin: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunKelvin
StepBasic_sunLumen: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunLumen
StepBasic_sunLux: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunLux
StepBasic_sunMetre: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunMetre
StepBasic_sunMole: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunMole
StepBasic_sunNewton: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunNewton
StepBasic_sunOhm: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunOhm
StepBasic_sunPascal: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunPascal
StepBasic_sunRadian: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunRadian
StepBasic_sunSecond: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunSecond
StepBasic_sunSiemens: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunSiemens
StepBasic_sunSievert: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunSievert
StepBasic_sunSteradian: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunSteradian
StepBasic_sunTesla: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunTesla
StepBasic_sunVolt: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunVolt
StepBasic_sunWatt: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunWatt
StepBasic_sunWeber: OCP.StepBasic.StepBasic_SiUnitName # value = StepBasic_SiUnitName.StepBasic_sunWeber
