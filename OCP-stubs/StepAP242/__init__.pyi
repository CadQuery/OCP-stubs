import OCP.StepAP242
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepRepr
import OCP.StepBasic
import OCP.StepAP214
import OCP.Standard
import OCP.StepShape
import OCP.StepData
import OCP.TCollection
import OCP.StepDimTol
__all__  = [
"StepAP242_ItemIdentifiedRepresentationUsage",
"StepAP242_GeometricItemSpecificUsage",
"StepAP242_IdAttribute",
"StepAP242_IdAttributeSelect",
"StepAP242_DraughtingModelItemAssociation",
"StepAP242_ItemIdentifiedRepresentationUsageDefinition"
]
class StepAP242_ItemIdentifiedRepresentationUsage(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepAP242_ItemIdentifiedRepresentationUsageDefinition: 
        """
        Returns field Definition
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
    def IdentifiedItem(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        Returns field IdentifiedItem
        """
    def IdentifiedItemValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        Returns identified item with given number
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theDefinition : StepAP242_ItemIdentifiedRepresentationUsageDefinition,theUsedRepresentation : OCP.StepRepr.StepRepr_Representation,theIdentifiedItem : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        Init all fields own and inherited
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def NbIdentifiedItem(self) -> int: 
        """
        Returns number of identified items
        """
    def SetDefinition(self,theDefinition : StepAP242_ItemIdentifiedRepresentationUsageDefinition) -> None: 
        """
        Set field Definition
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetIdentifiedItem(self,theIdentifiedItem : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        Set fiels IdentifiedItem
        """
    def SetIdentifiedItemValue(self,num : int,theItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        Set identified item with given number
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetUsedRepresentation(self,theUsedRepresentation : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        Set field UsedRepresentation
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UsedRepresentation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        Returns field UsedRepresentation
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
class StepAP242_GeometricItemSpecificUsage(StepAP242_ItemIdentifiedRepresentationUsage, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepAP242_ItemIdentifiedRepresentationUsageDefinition: 
        """
        Returns field Definition
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
    def IdentifiedItem(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        Returns field IdentifiedItem
        """
    def IdentifiedItemValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        Returns identified item with given number
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theDefinition : StepAP242_ItemIdentifiedRepresentationUsageDefinition,theUsedRepresentation : OCP.StepRepr.StepRepr_Representation,theIdentifiedItem : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        Init all fields own and inherited
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def NbIdentifiedItem(self) -> int: 
        """
        Returns number of identified items
        """
    def SetDefinition(self,theDefinition : StepAP242_ItemIdentifiedRepresentationUsageDefinition) -> None: 
        """
        Set field Definition
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetIdentifiedItem(self,theIdentifiedItem : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        Set fiels IdentifiedItem
        """
    def SetIdentifiedItemValue(self,num : int,theItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        Set identified item with given number
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetUsedRepresentation(self,theUsedRepresentation : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        Set field UsedRepresentation
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UsedRepresentation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        Returns field UsedRepresentation
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
class StepAP242_IdAttribute(OCP.Standard.Standard_Transient):
    def AttributeValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field AttributeValue
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
    def IdentifiedItem(self) -> StepAP242_IdAttributeSelect: 
        """
        Returns IdentifiedItem
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theAttributeValue : OCP.TCollection.TCollection_HAsciiString,theIdentifiedItem : StepAP242_IdAttributeSelect) -> None: 
        """
        Init all field own and inherited
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def SetAttributeValue(self,theAttributeValue : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetIdentifiedItem(self,theIdentifiedItem : StepAP242_IdAttributeSelect) -> None: 
        """
        Set field IdentifiedItem
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
class StepAP242_IdAttributeSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Action(self) -> OCP.StepBasic.StepBasic_Action: 
        """
        returns Value as a Action (Null if another type)
        """
    def Address(self) -> OCP.StepBasic.StepBasic_Address: 
        """
        returns Value as a Address (Null if another type)
        """
    def ApplicationContext(self) -> OCP.StepBasic.StepBasic_ApplicationContext: 
        """
        returns Value as a ApplicationContext (Null if another type)
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
        Recognizes a IdAttributeSelect Kind Entity that is : 1 -> Action 2 -> Address 3 -> ApplicationContext 4 -> DimensionalSize 5 -> GeometricTolerance 6 -> Group 7 -> Reserved for OrganizatonalProject (not implemented in OCCT) 8 -> ProductCategory 9 -> PropertyDefinition 10 -> Representation 11 -> ShapeAspect 12 -> ShapeAspectRelationship 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DimensionalSize(self) -> OCP.StepShape.StepShape_DimensionalSize: 
        """
        returns Value as a DimensionalSize (Null if another type)
        """
    def GeometricTolerance(self) -> OCP.StepDimTol.StepDimTol_GeometricTolerance: 
        """
        returns Value as a GeometricTolerance (Null if another type)
        """
    def Group(self) -> OCP.StepBasic.StepBasic_Group: 
        """
        returns Value as a Group (Null if another type)
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
    def ProductCategory(self) -> OCP.StepBasic.StepBasic_ProductCategory: 
        """
        returns Value as a ProductCategory (Null if another type)
        """
    def PropertyDefinition(self) -> OCP.StepRepr.StepRepr_PropertyDefinition: 
        """
        returns Value as a PropertyDefinition (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def Representation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        returns Value as a Representation (Null if another type)
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
    def ShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        returns Value as a ShapeAspect (Null if another type)
        """
    def ShapeAspectRelationship(self) -> OCP.StepRepr.StepRepr_ShapeAspectRelationship: 
        """
        returns Value as a ShapeAspectRelationship (Null if another type)
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
class StepAP242_DraughtingModelItemAssociation(StepAP242_ItemIdentifiedRepresentationUsage, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepAP242_ItemIdentifiedRepresentationUsageDefinition: 
        """
        Returns field Definition
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
    def IdentifiedItem(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        Returns field IdentifiedItem
        """
    def IdentifiedItemValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        Returns identified item with given number
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theDefinition : StepAP242_ItemIdentifiedRepresentationUsageDefinition,theUsedRepresentation : OCP.StepRepr.StepRepr_Representation,theIdentifiedItem : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        Init all fields own and inherited
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def NbIdentifiedItem(self) -> int: 
        """
        Returns number of identified items
        """
    def SetDefinition(self,theDefinition : StepAP242_ItemIdentifiedRepresentationUsageDefinition) -> None: 
        """
        Set field Definition
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetIdentifiedItem(self,theIdentifiedItem : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        Set fiels IdentifiedItem
        """
    def SetIdentifiedItemValue(self,num : int,theItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        Set identified item with given number
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetUsedRepresentation(self,theUsedRepresentation : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        Set field UsedRepresentation
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UsedRepresentation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        Returns field UsedRepresentation
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
class StepAP242_ItemIdentifiedRepresentationUsageDefinition(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AppliedApprovalAssignment(self) -> OCP.StepAP214.StepAP214_AppliedApprovalAssignment: 
        """
        returns Value as a AppliedApprovalAssignment (Null if another type)
        """
    def AppliedDateAndTimeAssignment(self) -> OCP.StepAP214.StepAP214_AppliedDateAndTimeAssignment: 
        """
        returns Value as a AppliedDateAndTimeAssignment (Null if another type)
        """
    def AppliedDateAssignment(self) -> OCP.StepAP214.StepAP214_AppliedDateAssignment: 
        """
        returns Value as a AppliedDateAssignment (Null if another type)
        """
    def AppliedDocumentReference(self) -> OCP.StepAP214.StepAP214_AppliedDocumentReference: 
        """
        returns Value as a AppliedDocumentReference (Null if another type)
        """
    def AppliedExternalIdentificationAssignment(self) -> OCP.StepAP214.StepAP214_AppliedExternalIdentificationAssignment: 
        """
        returns Value as a AppliedExternalIdentificationAssignment (Null if another type)
        """
    def AppliedGroupAssignment(self) -> OCP.StepAP214.StepAP214_AppliedGroupAssignment: 
        """
        returns Value as a AppliedGroupAssignment (Null if another type)
        """
    def AppliedOrganizationAssignment(self) -> OCP.StepAP214.StepAP214_AppliedOrganizationAssignment: 
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """
    def AppliedPersonAndOrganizationAssignment(self) -> OCP.StepAP214.StepAP214_AppliedPersonAndOrganizationAssignment: 
        """
        returns Value as a AppliedPersonAndOrganizationAssignment (Null if another type)
        """
    def AppliedSecurityClassificationAssignment(self) -> OCP.StepAP214.StepAP214_AppliedSecurityClassificationAssignment: 
        """
        returns Value as a AppliedSecurityClassificationAssignment (Null if another type)
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
        Recognizes a ItemIdentifiedRepresentationUsageDefinition Kind Entity that is : 1 -> AppliedApprovalAssignment 2 -> AppliedDateAndTimeAssignment 3 -> AppliedDateAssignment 4 -> AppliedDocumentReference 5 -> AppliedExternalIdentificationAssignment 6 -> AppliedGroupAssignment 7 -> AppliedOrganizationAssignment 8 -> AppliedPersonAndOrganizationAssignment 9 -> AppliedSecurityClassificationAssignment 10 -> DimensionalSize 11 -> GeneralProperty 12 -> GeometricTolerance 13 -> ProductDefinitionRelationship 14 -> PropertyDefinition 15 -> PropertyDefinitionRelationship 16 -> ShapeAspect 17 -> ShapeAspectRelationship 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DimensionalSize(self) -> OCP.StepShape.StepShape_DimensionalSize: 
        """
        returns Value as a DimensionalSize (Null if another type)
        """
    def GeneralProperty(self) -> OCP.StepBasic.StepBasic_GeneralProperty: 
        """
        returns Value as a GeneralProperty (Null if another type)
        """
    def GeometricTolerance(self) -> OCP.StepDimTol.StepDimTol_GeometricTolerance: 
        """
        returns Value as a GeometricTolerance (Null if another type)
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
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as a ProductDefinitionRelationship (Null if another type)
        """
    def PropertyDefinition(self) -> OCP.StepRepr.StepRepr_PropertyDefinition: 
        """
        returns Value as a PropertyDefinition (Null if another type)
        """
    def PropertyDefinitionRelationship(self) -> OCP.StepRepr.StepRepr_PropertyDefinitionRelationship: 
        """
        returns Value as a PropertyDefinitionRelationship (Null if another type)
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
    def ShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        returns Value as a ShapeAspect (Null if another type)
        """
    def ShapeAspectRelationship(self) -> OCP.StepRepr.StepRepr_ShapeAspectRelationship: 
        """
        returns Value as a ShapeAspectRelationship (Null if another type)
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
